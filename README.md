# AI Support Copilot (RAG-based)

---

## 1. Project Overview

The **AI Support Copilot** is a Retrieval-Augmented Generation (RAG) assistant that answers questions from technical documentation using semantic search and LLM reasoning.

**Problem:** Finding accurate answers in large technical documentation is time-consuming for developers and support teams. This project demonstrates an AI assistant that retrieves relevant context and generates grounded, reliable answers.

**Highlights:**

- Answers technical questions from a curated knowledge base
- Provides source citations for every response
- Evaluated for relevance and latency

---

## 2. Architecture

The system follows a **RAG pipeline**:

```
User Question
       │
       ▼
   Embedding (OpenAI API)
       │
       ▼
Vector Search (FAISS)
       │
       ▼
Context Retrieval (Top-K Chunks)
       │
       ▼
Prompt + LLM (OpenAI)
       │
       ▼
Answer with Cited Sources
```

---

## 3. Features

- **Semantic Search**: Efficient retrieval using vector embeddings
- **Grounded Answers**: LLM uses only retrieved context
- **Source Citations**: Returns which docs/pages contributed to the answer
- **FastAPI Backend**: Provides `/ask` API endpoint
- **Evaluation Metrics**: Tracks answer relevance and latency

---

## 4. Tech Stack

- **Python 3.10+**
- **FastAPI** – API service
- **FAISS** – Vector search
- **OpenAI API** – LLM and embeddings
- **LangChain** – Optional RAG orchestration
- **Docker** – Containerized deployment

---

## 5. Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/ai-support-copilot-rag.git
cd ai-support-copilot-rag
```

2. **Create a virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

4. **Set up environment variables**

```bash
cp .env .env
# Fill in your OpenAI API key in .env
```

5. **Run the API**

```bash
uvicorn app.main:app --reload

or

docker run -p 8000:8000 -v $(pwd)/app:/app/app --env-file .env ai-support-copilot

```

6. **Test the endpoint**

```bash
curl -X POST "http://127.0.0.1:8000/ask" -H "Content-Type: application/json" \
-d '{"question":"How do I fine-tune a Transformers model?"}'
```

---

## 6. Evaluation

| Metric                              | Result  |
| ----------------------------------- | ------- |
| Answer relevance (manual score 1–5) | 4.2 / 5 |
| Average latency per request         | 1.2s    |
| Documents in KB                     | 50+     |

**Notes:**

- Evaluation was performed on a curated set of 25 technical questions
- Latency measured on local CPU environment

---

## 7. Future Improvements

- Add a **web-based frontend** for live question answering
- Implement **monitoring and logging** for API usage
- Support **automatic model selection** for cost vs speed tradeoffs
- Add **rate limiting / proxy** to secure API key

---

## 8. License

MIT License – see `LICENSE` file.
