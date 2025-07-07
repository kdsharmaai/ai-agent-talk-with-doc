# 📝 Talk with Doc – AI-Powered PDF Q&A Agent

[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://python.org)
[![LangGraph](https://img.shields.io/badge/LangGraph-Agentic%20AI-purple.svg)](https://langchain-ai.github.io/langgraph/)
[![Flask](https://img.shields.io/badge/Flask-Web%20Framework-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-Apache-yellow.svg)](https://www.apache.org/licenses/LICENSE-2.0.txt)

> **Interact with your PDF documents using AI! Upload a PDF, ask questions, and get instant, accurate answers directly from your document's content. Powered by LangGraph, LangChain, and OpenAI.**

## 🚀 Overview

**Talk with Doc** is an advanced AI agent that enables direct Q&A with your PDF documents. Upload a PDF, ask any question, and receive answers extracted from the document—instantly. Built with Flask, LangGraph, and LangChain, this project demonstrates the power of agentic AI for document understanding and retrieval-augmented generation (RAG).

### ✨ Key Features

- **📄 Direct PDF Q&A**: Get answers only if the information is present in your PDF
- **🤖 AI-Powered Extraction**: Uses LLMs for accurate, context-aware answers
- **🚀 Fast & Interactive**: Instant responses with a modern, animated UI
- **🔒 Privacy-First**: Your documents are processed locally (no cloud upload)
- **🖼️ Sample Files**: Try with provided sample PDFs for instant demo
- **🎨 Modern UI/UX**: Futuristic, responsive, and accessible web interface

## 🏗️ Architecture

### LangGraph Agentic AI Implementation

This project leverages **LangGraph** for stateful, multi-step reasoning:

- **Reasoning Chains**: Multi-step process for PDF ingestion and Q&A
- **Tool Utilization**: Intelligent use of LLMs and PDF parsing
- **State Management**: Maintains conversation and document context
- **Error Handling**: Graceful responses for missing or ambiguous content
- **Modular Design**: Easily extensible for new document types or features

### Technology Stack

```
Frontend:
├── HTML5 + CSS3 (Futuristic Design)
├── Vanilla JavaScript (Interactive UI)
└── Responsive Web Design

Backend:
├── Python 3.10+
├── Flask (Web Framework)
├── LangGraph (Agentic AI)
├── LangChain (LLM Integration)
└── Poetry (Dependency Management)

APIs & Services:
├── OpenAI (LLM for Q&A)
├── PyPDF (PDF parsing)
```

## 🛠️ Installation & Setup

### Prerequisites

- Python 3.10 or higher
- Poetry (for dependency management)
- Internet connection for LLM API access

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/kdsharmaai/ai-agent-talk-with-doc.git
   cd ai-agent-talk-with-doc
   ```

2. **Install dependencies**
   ```bash
   poetry install
   ```

3. **Run the application**
   ```bash
   poetry run python main.py
   ```

4. **Access the interface**
   ```
   Open http://localhost:5002/ai-agent-talk-with-doc in your browser
   ```

## 🎯 Usage Examples

### Example Questions
```
"What is the main topic of this document?"
"Summarize section 2."
"Who is the author?"
"List all key findings."
"What are the conclusions?"
```

### How to Use
- **Step 1:** Upload a PDF document (max 500 KB)
- **Step 2:** Enter your question about the document
- **Step 3:** Click 'Submit' to get an answer from the document

Try with sample files:
- [Meta-Quarter-2025-Results.pdf](static/Meta-Quarter-2025-Results.pdf)

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root (if using OpenAI or other API keys):

```env
# API Keys (if required)
OPENAI_API_KEY=your_openai_api_key

# Application Settings
FLASK_ENV=development
DEBUG=True
```

### Customization

- **Add New Tools**: Extend with new document types or Q&A logic
- **Custom Prompts**: Modify the agent's reasoning prompts
- **UI Customization**: Update the futuristic interface design

## 📊 Project Structure

```
ai-agent-talk-with-doc/
├── main.py              # Flask application entry point
├── nodes.py             # LangGraph node definitions (PDF ingest, Q&A)
├── graph.py             # LangGraph workflow definition
├── pyproject.toml       # Poetry configuration
├── poetry.lock          # Dependency lock file
├── README.md            # Project documentation
├── static/              # Static assets (sample PDFs, images, loader)
│   ├── favicon-16x16.png
│   ├── graph.png
│   ├── loader.gif
│   └── Meta-Quarter-2025-Results.pdf
├── uploads/             # Uploaded PDF files (runtime)
└── templates/           # HTML templates
    └── index.html       # Main interface
```

## 🤖 AI Agent Capabilities

### Intelligent Query Processing
- **Context Awareness**: Understands user intent from natural language
- **Direct Extraction**: Answers only if content is present in the PDF
- **Multi-Modal Queries**: Handles complex instructions and summaries
- **Error Recovery**: Responds gracefully if answer is not found

### Tool Utilization
- **PDF Ingestion**: Loads and parses PDF content
- **LLM Q&A**: Uses OpenAI (or compatible) LLM for answer extraction

### Reasoning Chain
```
User Query → PDF Ingestion → LLM Q&A → Response Generation
```

## 🌟 Features in Detail

### Document Q&A Intelligence
- **Section Summaries**: Summarize any part of your document
- **Fact Extraction**: Pull out facts, lists, or data
- **Author/Meta Info**: Extract author, date, or other metadata
- **Flexible Queries**: Ask about any aspect of your PDF

### User Experience
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Futuristic Interface**: Modern, animated, and accessible
- **Real-Time Feedback**: Loader and status indicators
- **Sample Files**: Demo the system instantly

## 📄 License

This project is licensed under the Apache License - see the [LICENSE.txt](LICENSE.txt) file for details.

## 🙏 Acknowledgments

- **LangGraph Team**: For the agentic AI framework
- **LangChain & OpenAI**: For LLM and RAG capabilities
- **Flask Community**: For the excellent web framework
- **PyPDF**: For robust PDF parsing

---

<div align="center">

**Built with ❤️ using LangGraph, LangChain, and modern AI technologies**

</div>
