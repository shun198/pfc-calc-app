# CLAUDE.md

このファイルは、このリポジトリで作業する人向けの実装・運用メモです。

## リポジトリ概要

このプロジェクトは、食事単位で PFC を記録し、1 日のバランスを確認できるアプリを目指しています。

現時点では small start 構成で、最低限の画面と API の土台を用意しています。

## frontend

- ルート: `frontend`
- アプリ本体: `frontend/src/app`
- フレームワーク: Next.js App Router

### 補足

- App Router を使う都合上、`app` ディレクトリは残す
- ただし repo 全体での見通しを良くするため、配置は `src/app` にしている

## backend

- ルート: `backend`
- Python package: `backend/src/pfc_calc`
- フレームワーク: FastAPI

### アーキテクチャ

- `domain`: entity / repository interface
- `usecases`: application service
- `infrastructure`: DB, config, repository 実装
- `presentation`: FastAPI route, schema, dependency

## テスト方針

- backend の API は `pytest` で確認する
- `health` と `meals` のエンドポイントには最低限の API テストを用意する
- status code はハードコードしない

## 今後の拡張候補

- meal 作成 API の追加
- SQLAlchemy repository の本実装
- Alembic による migration 管理
- frontend の hooks / context 導入
- backend と frontend の接続
