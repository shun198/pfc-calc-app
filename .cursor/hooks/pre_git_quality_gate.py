#!/usr/bin/env python3
import json
import pathlib
import re
import subprocess
import sys


TARGET_COMMAND = re.compile(r"\b(?:git\s+commit|git\s+push|gh\s+pr\s+create)\b")


def emit(payload: dict, exit_code: int = 0) -> None:
    print(json.dumps(payload, ensure_ascii=False))
    raise SystemExit(exit_code)


def run(command: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        command,
        shell=True,
        text=True,
        capture_output=True,
    )


def changed_files() -> set[str]:
    files: set[str] = set()
    commands = [
        "git diff --name-only --cached",
        "git diff --name-only",
        "git diff --name-only HEAD~1..HEAD",
    ]
    for cmd in commands:
        result = run(cmd)
        if result.returncode != 0:
            continue
        for line in result.stdout.splitlines():
            line = line.strip()
            if line:
                files.add(line)
    return files


def detect_languages(files: set[str]) -> set[str]:
    langs: set[str] = set()
    for f in files:
        suffix = pathlib.Path(f).suffix.lower()
        if suffix == ".py":
            langs.add("python")
        elif suffix == ".go":
            langs.add("go")
        elif suffix in {".js", ".jsx", ".ts", ".tsx"}:
            langs.add("node")
    return langs


def package_manager() -> str:
    root = pathlib.Path(".")
    if (root / "pnpm-lock.yaml").exists():
        return "pnpm"
    if (root / "yarn.lock").exists():
        return "yarn"
    return "npm"


def commands_for_language(language: str) -> tuple[list[str], list[str]]:
    if language == "python":
        return (
            ["uv run ruff check .", "ruff check ."],
            ["uv run pytest -q", "pytest -q"],
        )
    if language == "go":
        return (
            ["golangci-lint run", "go vet ./..."],
            ["go test ./..."],
        )
    if language == "node":
        pm = package_manager()
        if pm == "pnpm":
            return (["pnpm lint"], ["pnpm test"])
        if pm == "yarn":
            return (["yarn lint"], ["yarn test --watch=false"])
        return (
            ["npm run lint"],
            ["npm test -- --watch=false"],
        )
    return ([], [])


def execute_candidates(candidates: list[str], label: str, language: str) -> tuple[bool, str]:
    not_found = 0
    last_output = ""
    for cmd in candidates:
        result = run(cmd)
        combined = (result.stdout + "\n" + result.stderr).strip()
        if result.returncode == 0:
            return True, f"{language}:{label} passed with `{cmd}`"
        if result.returncode == 127:
            not_found += 1
            continue
        last_output = combined
        return False, f"{language}:{label} failed with `{cmd}`\n{combined}"
    if not_found == len(candidates):
        return False, f"{language}:{label} no runnable command found"
    return False, f"{language}:{label} failed\n{last_output}"


def main() -> None:
    raw = sys.stdin.read().strip()
    data = json.loads(raw) if raw else {}
    command = data.get("command", "")

    if not TARGET_COMMAND.search(command):
        emit({"permission": "allow"})

    files = changed_files()
    languages = detect_languages(files)
    if not languages:
        emit(
            {
                "permission": "allow",
                "agent_message": "No python/go/node changes detected. Quality gate skipped.",
            }
        )

    failures: list[str] = []
    passes: list[str] = []
    for lang in sorted(languages):
        lint_cmds, test_cmds = commands_for_language(lang)
        lint_ok, lint_message = execute_candidates(lint_cmds, "lint", lang)
        if lint_ok:
            passes.append(lint_message)
        else:
            failures.append(lint_message)
            continue

        test_ok, test_message = execute_candidates(test_cmds, "test", lang)
        if test_ok:
            passes.append(test_message)
        else:
            failures.append(test_message)

    if failures:
        emit(
            {
                "permission": "deny",
                "user_message": "Commit/push/PR作成の前提チェックで失敗しました。linter/testを修正して再実行してください。",
                "agent_message": "\n\n".join(failures),
            }
        )

    emit(
        {
            "permission": "allow",
            "agent_message": "\n".join(passes),
        }
    )


if __name__ == "__main__":
    main()
