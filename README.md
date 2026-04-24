# projectllm

A conversational AI chat application built with FastAPI, served via a clean dark-themed frontend, and powered by a free LLM through OpenRouter.

![Chat UI](my-api/docs/screenshot.png)

---

## Stack

- **FastAPI** — async Python web framework
- **OpenRouter** — LLM API (free tier)
- **Poetry** — dependency management and virtual environments
- **Docker** — containerization
- **GitHub Actions** — CI pipeline

---

## Project Structure

```
my-api/
├── src/
│   └── my_api/
│       ├── __init__.py
│       ├── main.py          # FastAPI app and routes
│       └── static/
│           └── index.html   # Chat frontend
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── docs/
│   └── screenshot.png
├── .github/
│   └── workflows/
│       └── ci.yml
├── Dockerfile
├── docker-compose.yml
├── entrypoint.sh
├── pyproject.toml
└── poetry.lock
```

---

## Getting Started

### Prerequisites

- Python 3.12+
- [Poetry](https://python-poetry.org/docs/#installation)
- An [OpenRouter](https://openrouter.ai) API key (free)

### Install dependencies

```bash
poetry install
```

### Set up environment variables

Create a `.env` file in the project root:

```
OPENROUTER_API_KEY=sk-or-...
```

### Run locally

```bash
poetry run uvicorn src.my_api.main:app --reload --reload-dir src
```

Visit `http://127.0.0.1:8000` to open the chat UI.

---

## Run with Docker

```bash
docker compose up --build
```

Visit `http://localhost:8000`.

---

## Run Tests

```bash
poetry run pytest
```

---

## CI Pipeline

GitHub Actions runs on every push to `main` and every pull request:

1. Installs dependencies via Poetry
2. Runs the test suite
3. Builds the Docker image

See `.github/workflows/ci.yml` for the full configuration.

---

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/` | Serves the chat frontend |
| POST | `/chat` | Sends a message and returns LLM response |

### Example request

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"content": "What is FastAPI?"}'
```

### Example response

```json
{
  "response": "FastAPI is a modern, fast web framework for building APIs with Python..."
}
```