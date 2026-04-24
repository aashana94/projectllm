FROM python:3.12-slim AS base
RUN pip install poetry
WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root --only main

FROM base AS runtime
COPY src/ ./src/
CMD ["poetry", "run", "uvicorn", "my_api.main:app", "--host", "0.0.0.0", "--port", "8000"]