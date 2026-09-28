# 📄 RAG PDF Chatbot – Generative AI

A Streamlit-based **Retrieval-Augmented Generation (RAG)** application that allows users to upload PDF documents and ask questions about their contents.

The application extracts text from PDF files, splits the content into smaller chunks, generates semantic embeddings, stores the embeddings in a vector database, retrieves relevant passages, and uses **Google Gemini** to generate answers based on the uploaded document.

## 🚀 Features

- 📄 Upload PDF documents
- 🔍 Extract text from PDF files
- ✂️ Split documents into smaller text chunks
- 🧠 Generate semantic embeddings
- 🗄️ Store and retrieve document embeddings
- 🔎 Retrieve relevant document passages
- 🤖 Generate answers using Google Gemini
- 💬 Ask questions about uploaded PDFs
- 🌐 Streamlit-based web interface
- 📚 Includes sample PDF documents
- 🎨 Custom responsive UI using CSS

## 🛠️ Technologies Used

- **Python**
- **Streamlit**
- **Google Gemini**
- **ChromaDB / Vector Database**
- **LangChain**
- **PDF Processing**
- **Vector Embeddings**
- **Retrieval-Augmented Generation (RAG)**
- **HTML & CSS**

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
                    │ Vector Database │
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
```

### 📌 RAG Process

1. **Upload PDF** – The user uploads a PDF through the Streamlit interface.
2. **Extract Text** – Text is extracted from the uploaded PDF.
3. **Text Chunking** – The extracted text is divided into smaller chunks.
4. **Generate Embeddings** – The chunks are converted into vector representations.
5. **Store Embeddings** – The generated embeddings are stored in the vector database.
6. **Ask a Question** – The user enters a question related to the uploaded document.
7. **Retrieve Relevant Chunks** – The system searches for the most relevant document content.
8. **Generate Answer** – Google Gemini receives the relevant context and generates an answer.
9. **Display Answer** – The generated response is displayed through the Streamlit interface.

## 📁 Project Structure

## 📁 Project Structure

```text
RAG-PDF-Chatbot-Generative-AI/
│
├── 📁 Images/
│   ├── AI Assistant.png
│   ├── pdf.png
│   ├── Upload cloud.png
│   └── User.png
│
├── 📁 Sample PDFs/
│   ├── Sample Questions.pdf
│   └── SDP_M1.pdf
│
├── 📄 README.md
├── 📄 app.py
├── 📄 rag.py
├── 📄 requirements.txt
├── 📄 style.css
├── 📄 utils.py
└── 📄 vector_db.py

## 📂 File Description

| File / Folder | Description |
|---|---|
| `app.py` | Main Streamlit application and user interface |
| `rag.py` | Handles the Retrieval-Augmented Generation workflow |
| `vector_db.py` | Handles vector database operations and document retrieval |
| `utils.py` | Contains helper functions for PDF processing and other utilities |
| `style.css` | Custom styling for the Streamlit application |
| `requirements.txt` | Python dependencies required to run the project |
| `Images/` | Contains images and UI assets used by the application |
| `Sample PDFs/` | Contains sample PDF documents for testing |
| `README.md` | Project documentation |

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/RAG-PDF-Chatbot-Generative-AI.git
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Navigate to the Project Directory

```bash
cd RAG-PDF-Chatbot-Generative-AI
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS / Linux

```bash
source venv/bin/activate
```

### 5. Install Required Dependencies

```bash
pip install -r requirements.txt
```

## 🔑 Google Gemini API Key

This project requires a **Google Gemini API key** to generate answers.

Create a `.env` file in the project directory and add:

```env
GOOGLE_API_KEY=your_google_api_key
```

Replace `your_google_api_key` with your actual API key.

### ⚠️ Important

Never upload your API key to GitHub.

Add the following to `.gitignore`:

```text
.env
venv/
__pycache__/
*.pyc
```

## ▶️ Run the Application

After installing the dependencies and configuring your API key, run:

```bash
streamlit run app.py
```

The application will start locally and open in your web browser.

## 💻 How to Use

### 1. Start the Application

Run:

```bash
streamlit run app.py
```

### 2. Upload a PDF

Select a PDF document using the upload section.

You can also use one of the sample PDFs available in:

```text
Sample PDFs/
```

### 3. Process the PDF

The application processes the uploaded document by:

- Extracting the text
- Splitting the text into chunks
- Generating embeddings
- Storing the embeddings
- Preparing the document for retrieval

### 4. Ask a Question

Enter a question related to the uploaded PDF.

For example:

```text
What is the main topic discussed in this document?
```

### 5. Get the Answer

The system retrieves relevant information from the PDF and provides it to Google Gemini as context.

Gemini then generates an answer based on the retrieved document content.

## 🧠 RAG Architecture

The application follows a Retrieval-Augmented Generation architecture:

```text
                     PDF Document
                          │
                          ▼
                   Text Extraction
                          │
                          ▼
                    Text Chunking
                          │
                          ▼
                 Generate Embeddings
                          │
                          ▼
                   Vector Database
                          │
                          │
              ┌───────────┘
              │
       User Question
              │
              ▼
       Similarity Search
              │
              ▼
      Relevant Text Chunks
              │
              ▼
        Google Gemini
              │
              ▼
        Generated Answer
```

## 🔍 Why RAG?

Retrieval-Augmented Generation allows the chatbot to answer questions using information retrieved directly from the uploaded PDF.

The system first finds relevant content from the document and then provides that content as context to the Gemini model.

This allows users to interact with their own documents instead of relying only on the language model's general knowledge.

## 📦 Dependencies

The project's required Python packages are listed in:

```text
requirements.txt
```

Install them using:

```bash
pip install -r requirements.txt
```

## 🎨 User Interface

The application uses a custom `style.css` file to provide a customized interface.

The `Images/` folder contains the visual assets used throughout the application.

The interface is designed to provide a clean and user-friendly experience for uploading PDFs and asking questions.

## 📚 Sample PDFs

The repository contains sample PDF documents in:

```text
Sample PDFs/
```

These files can be used to test the chatbot without needing to provide your own PDF initially.

## 🔐 Security

For security:

- Never commit your `.env` file.
- Never expose your Google Gemini API key.
- Use environment variables for API credentials.
- Do not hard-code API keys in Python files.
- Add `.env` to `.gitignore`.

## 🚧 Future Improvements

Possible future improvements include:

- [ ] Multiple PDF upload support
- [ ] Chat history
- [ ] Conversation memory
- [ ] Source and page references
- [ ] Improved document chunking
- [ ] Persistent vector database
- [ ] Support for additional document formats
- [ ] User authentication
- [ ] Improved mobile responsiveness
- [ ] Streaming AI responses
- [ ] Cloud deployment

## 🌐 Deployment

The application can be deployed on platforms that support Streamlit applications.

Before deployment, configure the `GOOGLE_API_KEY` securely using the platform's secrets or environment-variable settings.

Do not upload the `.env` file containing your API key.

## 🤝 Contributing

Contributions are welcome.

To contribute:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Commit your changes.
5. Push your changes.
6. Create a Pull Request.

## 📄 License

This project is intended for educational and demonstration purposes.

## 👨‍💻 Author

**Your Name**

Built with:

**Python • Streamlit • Google Gemini • Vector Database • RAG**

---

⭐ If you find this project useful, consider giving the repository a star!
