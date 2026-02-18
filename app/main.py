from fastapi import FastAPI

app = FastAPI()

@app.post("/ask")
def ask_endpoint(question: dict):
    return {"answer": "This is a test answer.", "sources": ["doc1.md"]}
