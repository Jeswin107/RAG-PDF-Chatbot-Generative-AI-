import base64
import hashlib
import os
import tempfile
from pathlib import Path
import html
import re
import streamlit as st
from dotenv import load_dotenv
from utils import load_pdf, split_text
from vector_db import create_vector_db
from rag import get_answer
load_dotenv()

st.set_page_config(
    page_title="RAG PDF Chatbot",
    page_icon="pdf.png",
    layout="wide",
    initial_sidebar_state="collapsed",
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def image_to_base64(image_path):
    """Convert an image file into a Base64 string 
       so it can be displayed inside HTML.
    """
    try:
        with open(image_path, "rb") as image_file: 
             return base64.b64encode(image_file.read()).decode("utf-8") 
    except FileNotFoundError: 
        st.error(f"Image file not found: {image_path}") 
        return ""

pdf_icon = image_to_base64(os.path.join(BASE_DIR, "Images", "pdf.png"))
upload_cloud_icon = image_to_base64(os.path.join(BASE_DIR, "Images", "Upload cloud.png"))
user_question_icon = image_to_base64(os.path.join(BASE_DIR, "Images", "User.png"))
ai_answer_icon = image_to_base64(os.path.join(BASE_DIR, "Images", "AI Assistant.png"))

def load_css():
    css_file = Path(__file__).resolve().parent / "style.css"
    if css_file.exists():
        with open(css_file, "r", encoding="utf-8") as f:
            css = f.read()
        css = css.replace("{upload_cloud_icon}", upload_cloud_icon)
        st.markdown(
            f"<style>{css}</style>",
            unsafe_allow_html=True,
        )
load_css()

for key, default in {
    "messages": [],
    "db": None,
    "file_hash": None,
    "processed_name": None,
    "processing": False,
}.items():
    if key not in st.session_state:
        st.session_state[key] = default

st.html(
    f"""
        <div class="mainbox1">
                <div class="hero-row">
                     <img src="data:image/png;base64,{pdf_icon}" class="img1">
                     <div class="hero-text">
                         <h1>
                             <span class="gradient-text">RAG</span>
                             <span class="white-text"> PDF Chatbot</span>
                         </h1>
                         <div class="title-line">
                             <span></span>
                             <b>•</b>
                             <span></span>
                         </div>
                     </div>
                </div>
                 <h2>Upload a PDF and ask questions</h2>
                 <p>Get intelligent answers from your documents using AI.</p>
        </div>   
    """
)

uploaded_file = st.file_uploader(
    "",
    type=["pdf"],
    label_visibility="collapsed",
)

if uploaded_file:
    if uploaded_file.size > 100 * 1024 * 1024:
        st.markdown("""
        <div class="error-box">
            ❌ <b>The PDF is larger than the 100 MB limit.</b>
        </div>
        """, unsafe_allow_html=True)
        st.stop()
    data = uploaded_file.getvalue()
    file_hash = hashlib.sha256(data).hexdigest()
   
    st.html(
    f"""
    <div class="upload-card">
        <div class="pdf-box">PDF</div>
        <div class="file-info">
            <div class="filename">{uploaded_file.name}</div>
            <div class="filesize">{uploaded_file.size / (1024 * 1024):.2f} MB</div>
        </div>
        <div class="success">✓</div>
    </div>
    """)
    
    if st.session_state.file_hash != file_hash:
        st.session_state.db = None
        st.session_state.messages = []
        st.session_state.file_hash = file_hash
        st.session_state.processed_name = None

    if st.session_state.processed_name != uploaded_file.name:
        c1, c2, c3 = st.columns([2,2,2])
        with c2:
            process = st.button(
                 "Generate Knowledge Base",
                 type="primary",
                 use_container_width=True,
            )
        if process:
            if not os.getenv("GOOGLE_API_KEY"):
                st.error("GOOGLE_API_KEY is missing. Add it to your .env file.")
                st.stop()
            with st.spinner("Processing your PDF..."):
                try:
                    with tempfile.NamedTemporaryFile(
                        suffix=".pdf", delete=False
                    ) as tmp:
                        tmp.write(data)
                        pdf_path = tmp.name

                    documents = load_pdf(pdf_path)
                    if not documents:
                        st.markdown("""
                             <div class="error-box">
                             ❌ <b>No readable pages were found in the PDF.</b>
                             </div>
                        """, unsafe_allow_html=True)
                        st.stop()
                    chunks = split_text(documents)
                    if not chunks:
                        st.markdown("""
                             <div class="error-box">
                             ❌ <b>No text could be extracted from the PDF.</b>
                             </div>
                        """, unsafe_allow_html=True)
                        st.stop()
                    st.session_state.db = create_vector_db(
                        chunks, file_hash=file_hash
                    )
                    st.session_state.processed_name = uploaded_file.name
                    st.session_state.messages = []
                    st.rerun()
                except Exception as exc:
                    st.markdown("""
                         <div class="error-box">
                         ❌ <b>Could not process the PDF.</b>
                         </div>
                    """, unsafe_allow_html=True)
                finally:
                    try:
                        os.unlink(pdf_path)
                    except Exception:
                        pass

def _markdown_to_html(text):
    text = html.escape(str(text))
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'(?<!\*)\*([^*\n]+)\*(?!\*)', r'<em>\1</em>', text)
    lines = text.splitlines()
    out, in_ul = [], False
    for line in lines:
        if re.match(r'^\s*[-*]\s+', line):
            if not in_ul:
                out.append('<ul>'); in_ul = True
            item = re.sub(r'^\s*[-*]\s+', '', line)
            out.append(f'<li>{item}</li>')
        else:
            if in_ul:
                out.append('</ul>'); in_ul = False
            if line.strip(): out.append(f'<p>{line}</p>')
    if in_ul: out.append('</ul>')
    return ''.join(out) or '<p></p>'

if st.session_state.db is not None:
    st.markdown('<div class="chat-title">Your PDF Is Ready...<br>Ask Questions About Your PDF</div>', unsafe_allow_html=True)

    for message in st.session_state.messages:
        role = message.get("role")
        content = message.get("content", "")
        sources = message.get("sources", [])
  
        if role == "user":
          safe_content = html.escape(str(content)).replace("\n", "<br>")
          st.markdown(
             f"""
             <div class="message-row user-row">
                 <div class="user-bubble">
                      <div class="bubble-text">{safe_content}</div>
                 </div>
                 <div class="avatar"><img src="data:image/png;base64,{user_question_icon}"></div>
             </div>
             """,
             unsafe_allow_html=True,
           )  

        elif role == "assistant":
            answer_html = _markdown_to_html(content)
            st.markdown(
             f"""
             <div class="message-row assistant-row">
                 <div class="avatar"><img src="data:image/png;base64,{ai_answer_icon}"></div>
                     <div class="assistant-bubble">
                 <div class="bubble-text">{answer_html}</div>
                 </div>
             </div>
             """,
             unsafe_allow_html=True,
            )
            not_found_message = "I couldn't find that information in the uploaded PDF."
            if sources and str(content).strip() != not_found_message:
                source_text = html.escape(str(sources[0]))
                st.markdown(
                 f"""
                 <div class="source-card">
                    <div class="source-left">
                        <span class="source-icon">▤</span>
                        <span><strong>Sources : </strong>{source_text}</span>
                    </div>
                 </div>
                 """,
                 unsafe_allow_html=True,
                )

    question = st.chat_input("Ask a question about your PDF...")
    if question and question.strip():
        question = question.strip()
        st.session_state.messages.append({
            "role": "user",
            "content": question,
        })
        try:
            with st.spinner("Searching the PDF..."):
                answer, docs = get_answer(
                    question, db=st.session_state.db, return_sources=True
                )
  
            not_found_message = "I couldn't find that information in the uploaded PDF."
            sources, seen = [], set()
            if answer.strip() != not_found_message:
                for doc in docs:
                    page = doc.metadata.get("page")
                    source_name = st.session_state.processed_name
                    page_text = (
                        f"{source_name} (Page {page + 1})"
                        if isinstance(page, int)
                        else source_name
                    )
                    if page_text not in seen:
                        sources.append(page_text)
                        seen.add(page_text)

            st.session_state.messages.append({
                "role": "assistant",
                "content": answer,
                "sources": sources,
            })
            st.rerun()
        except Exception as exc:
            st.session_state.messages.append({
                "role": "assistant",
                "content": f"Sorry, I couldn't answer that question: {exc}",
                "sources": [],
            })
            st.rerun()