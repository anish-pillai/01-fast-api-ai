# Run in local

uv run uvicorn app.main:app --reload

# Run Image

docker run --rm --env-file .env -p 8000:8000 fastapi-ai
