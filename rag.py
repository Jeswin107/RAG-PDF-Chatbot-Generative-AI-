import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from vector_db import load_vector_db
load_dotenv()

def _llm():
    key = os.getenv("GOOGLE_API_KEY")
    if not key:
        raise RuntimeError("GOOGLE_API_KEY is not configured.")
    return ChatGoogleGenerativeAI(
        model=os.getenv("GEMINI_MODEL", "gemini-3.6-flash"),
        google_api_key=key,
        temperature=0.2,
    )

def get_answer(question, db=None, return_sources=False):
    db = db or load_vector_db()
    docs = db.similarity_search(question, k=5)
    if not docs:
        answer = "I couldn't find that information in the uploaded PDF."
        return (answer, []) if return_sources else answer
    context = "\n\n".join(
        f"[Page {doc.metadata.get('page', 0) + 1}]\n{doc.page_content}"
        for doc in docs
    )
    prompt = f"""You answer questions about an uploaded PDF.

Rules:
- Use ONLY the supplied context.
- Do not invent or use outside knowledge.
- If the context does not contain the answer, say exactly:
"I couldn't find that information in the uploaded PDF."
- Give a clear, concise answer.
- When useful, use bullets or short numbered steps.

Context:
{context}

Question:
{question}

Answer:"""

    response = _llm().invoke(prompt)
    answer = response.content if isinstance(response.content, str) else str(response.content)
    return (answer, docs) if return_sources else answer
