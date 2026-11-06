from fastapi.testclient import TestClient
from main import app, detect_intent

client = TestClient(app)


# --- Health Check Tests ---
def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


# --- Intents List Test ---
def test_list_intents():
    response = client.get("/intents")
    assert response.status_code == 200
    intents = response.json()["intents"]
    assert "greeting" in intents
    assert "farewell" in intents
    assert "pricing" in intents


# --- Chat Endpoint Tests ---
def test_chat_greeting():
    response = client.post("/chat", json={"message": "Hello!"})
    assert response.status_code == 200
    data = response.json()
    assert data["intent"] == "greeting"
    assert len(data["reply"]) > 0


def test_chat_farewell():
    response = client.post("/chat", json={"message": "Bye bye"})
    assert response.status_code == 200
    assert response.json()["intent"] == "farewell"


def test_chat_pricing():
    response = client.post("/chat", json={"message": "price kya hai?"})
    assert response.status_code == 200
    assert response.json()["intent"] == "pricing"


def test_chat_support():
    response = client.post("/chat", json={"message": "mujhe help chahiye"})
    assert response.status_code == 200
    assert response.json()["intent"] == "support"


def test_chat_general():
    response = client.post("/chat", json={"message": "random something"})
    assert response.status_code == 200
    assert response.json()["intent"] == "general"


# --- Intent Detection Unit Tests ---
def test_detect_intent_greeting():
    assert detect_intent("hi there") == "greeting"
    assert detect_intent("salam") == "greeting"


def test_detect_intent_farewell():
    assert detect_intent("alvida") == "farewell"


def test_detect_intent_pricing():
    assert detect_intent("kitna kharcha hoga") == "pricing"
