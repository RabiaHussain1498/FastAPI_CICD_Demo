# FastAPI CI/CD Demo

![CI Pipeline](https://github.com/RabiaHussain1498/FastAPI_CICD_Demo/actions/workflows/ci.yml/badge.svg)
![CD Pipeline](https://github.com/RabiaHussain1498/FastAPI_CICD_Demo/actions/workflows/cd.yml/badge.svg)

A simple **FastAPI** application demonstrating a complete **CI/CD pipeline** using GitHub Actions.

---

## Features

- **3 REST Endpoints** — `/health`, `/intents`, `/chat`
- **Bilingual Intent Detection** — English + Urdu support
- **CI Pipeline** — Lint + Test on every push
- **CD Pipeline** — Auto-deploy to Railway on `main` push

---

## Project Structure

```
FastAPI_CICD_Demo/
├── main.py                        # FastAPI application
├── requirements.txt               # Python dependencies (pinned)
├── Procfile                       # Deployment config
├── runtime.txt                    # Python version
├── tests/
│   ├── conftest.py                # Test setup
│   └── test_main.py               # 10 test cases
└── .github/
    └── workflows/
        ├── ci.yml                 # Lint + Test pipeline
        └── cd.yml                 # Deploy to Railway
```

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Server health check |
| GET | `/intents` | List all intents |
| POST | `/chat` | Send a message, get intent-based reply |

### POST `/chat` — Example

**Request:**
```json
{ "message": "Hello!" }
```

**Response:**
```json
{
  "reply": "Hello! How can I help you today?",
  "intent": "greeting"
}
```

---

## CI/CD Pipeline

```
Push to GitHub
      |
      v
  Lint (ruff)
      |
      v
  Tests (pytest + coverage)
      |
      v  (only on main)
  Deploy to Railway
```

---

## Run Locally

```bash
git clone https://github.com/RabiaHussain1498/FastAPI_CICD_Demo.git
cd FastAPI_CICD_Demo
pip install -r requirements.txt
python main.py
```

Visit: http://localhost:8000/docs

---

## Run Tests

```bash
pytest tests/ -v --cov=main
```
