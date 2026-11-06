import re

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="CI/CD Demo API", version="1.0.0")


# --- Models ---
class MessageRequest(BaseModel):
    message: str


class MessageResponse(BaseModel):
    reply: str
    intent: str


# --- Simple intent detection (no LLM needed) ---
def detect_intent(message: str) -> str:
    # punctuation hata do, lowercase karo, words list banao
    clean = re.sub(r"[^\w\s]", "", message.lower())
    words = clean.split()
    if any(w in words for w in ["hello", "hi", "hey", "salam", "hii"]):
        return "greeting"
    elif any(w in words for w in ["bye", "goodbye", "alvida"]) or "khuda hafiz" in clean:
        return "farewell"
    elif any(w in words for w in ["price", "cost", "rate", "kitna", "kharcha"]):
        return "pricing"
    elif any(w in words for w in ["help", "support", "madad", "problem"]):
        return "support"
    else:
        return "general"


REPLIES = {
    "greeting": "Hello! Mein aapki kaise madad kar sakta hoon?",
    "farewell": "Allah Hafiz! Have a great day!",
    "pricing": "Hamari pricing ke liye sales team se contact karein.",
    "support": "Support ke liye support@company.com pe email karein.",
    "general": "Aapka sawaal samajh gaya. Hum jald jawab denge.",
}


# --- Endpoints ---
@app.get("/health")
def health_check():
    return {"status": "ok", "message": "Server is running!"}


@app.get("/intents")
def list_intents():
    return {"intents": list(REPLIES.keys())}


@app.post("/chat", response_model=MessageResponse)
def chat(request: MessageRequest):
    intent = detect_intent(request.message)
    reply = REPLIES[intent]
    return MessageResponse(reply=reply, intent=intent)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
