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
- ルート配下に monorepo 管理用の `package.json` は置かない

## 実装時の注意

- API の status code は数値を直書きせず、`fastapi.status` の定数を使う
- backend のテストでは `pytest` を使い、API テストは `fastapi.testclient.TestClient` を基本にする
- import は backend では `pfc_calc...` から始める
- 永続化未実装の段階では stub 実装を usecase 経由で差し替えやすい形に保つ

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
