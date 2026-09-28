# 📄 RAG PDF Chatbot – Generative AI

A Streamlit-based **Retrieval-Augmented Generation (RAG)** application that allows users to upload a PDF document and ask questions about its contents.

The application extracts text from the uploaded PDF, splits it into smaller chunks, generates semantic embeddings, stores them in **ChromaDB**, retrieves the most relevant passages for a user's question, and uses **Google Gemini** to generate an answer based on the uploaded document.

## 🚀 Features

- 📄 Upload PDF documents
- 🔍 Extract text from PDF files
- ✂️ Split documents into smaller text chunks
- 🧠 Generate semantic embeddings
- 🗄️ Store embeddings using ChromaDB
- 🔎 Retrieve relevant document passages
- 🤖 Generate answers using Google Gemini
- 💬 Ask questions about the uploaded PDF
- 🌐 Streamlit-based web interface

## 🛠️ Technologies Used

- **Python**
- **Streamlit**
- **Google Gemini**
- **ChromaDB**
- **LangChain**
- **PDF processing**
- **Vector embeddings**
- **Retrieval-Augmented Generation (RAG)**

## 🔄 How It Works

```text
                    ┌─────────────────┐
                    │   Upload PDF    │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Extract PDF Text│
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Split Into      │
                    │ Text Chunks     │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Generate        │
                    │ Embeddings      │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Store in        │
                    │ ChromaDB        │
                    └────────┬────────┘
                             │
                       User Question
                             │
                             ▼
                    ┌─────────────────┐
                    │ Retrieve        │
                    │ Relevant Chunks │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Google Gemini   │
                    │ Generates Answer│
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Display Answer  │
                    └─────────────────┘
