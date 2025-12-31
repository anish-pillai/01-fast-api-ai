# ---- Base image ----
FROM python:3.11-slim

# ---- Environment ----
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ---- System deps ----
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# ---- Workdir ----
WORKDIR /app

# ---- Copy dependency files first (better caching) ----
COPY pyproject.toml uv.lock ./

# ---- Install uv ----
RUN pip install --no-cache-dir uv

# ---- Install Python deps ----
RUN uv sync --frozen

# ---- Copy app code ----
COPY app ./app

# ---- COPY ALEMBIC FILES ----
COPY alembic.ini .
COPY alembic ./alembic

# ---- Expose port ----
EXPOSE 8000

# ---- Start FastAPI (Railway compatible) ----
CMD ["sh", "-c", "uv run uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]