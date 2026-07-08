# AGENTS.md

このファイルは、このリポジトリで作業するエージェント向けのガイドです。

## 目的

PFC バランスを食事ごとに管理する Web アプリを開発します。

- frontend: TypeScript / React / Next.js
- backend: Python / FastAPI / SQLAlchemy / PostgreSQL

## 基本方針

- ドキュメント、コメント、運用メモは日本語で記述する
- backend は clean architecture + DDD を前提に拡張する
- frontend は Next.js App Router を前提に `frontend/src/app` 配下で管理する
- backend は `backend/src/pfc_calc` を Python パッケージのルートとする

## ディレクトリ方針

- frontend の依存関係と scripts は `frontend/package.json` で管理する
- backend の依存関係は `backend/pyproject.toml` で管理する

## 確認コマンド

### frontend

```bash
cd frontend
npm install
npm run lint
npm run build
```

### backend

```bash
cd backend
uv sync
uv run pytest
uv run uvicorn pfc_calc.main:app --reload
```
