from pathlib import Path
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

BASE_DIR = Path(__file__).resolve().parent
DB_ROOT = BASE_DIR / "chroma_db"

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
def create_vector_db(chunks, file_hash=None):
    persist_directory = str(DB_ROOT / (file_hash or "default"))
    Path(persist_directory).mkdir(parents=True, exist_ok=True)
    return Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=persist_directory,
    )
def load_vector_db(file_hash=None):
    persist_directory = str(DB_ROOT / (file_hash or "default"))
    return Chroma(
        persist_directory=persist_directory,
        embedding_function=embedding_model,
    )