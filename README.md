# Run in local

uv run uvicorn app.main:app --reload

# Run Image

docker compose up -d --build

docker compose exec api uv run python -m alembic revision \
  --autogenerate \
  -m "initial tables"

docker compose logs api
