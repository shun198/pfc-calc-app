# backend

FastAPI / SQLAlchemy / PostgreSQL の最小セットアップです。
初期段階から clean architecture + DDD を前提に構成しています。

## Architecture

```text
src/pfc_calc/
├── domain/           # Entity / Repository interface
├── usecases/         # Application services
├── infrastructure/   # SQLAlchemy / settings / repository implementation
└── presentation/     # FastAPI routes / response schemas
```

## Run

```bash
uv sync
uv run uvicorn pfc_calc.main:app --reload
```

## Endpoints

- `GET /api/v1/health`
- `GET /api/v1/meals`
