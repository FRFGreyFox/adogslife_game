# requirenments:
- [poetry](https://python-poetry.org/)
- [Microsoft C++ Build Tools (13+)](https://visualstudio.microsoft.com/ru/downloads/)
---

# setup:
```bash
poetry install
```

---

# run game:
```bash
poetry run python main.py
```

---

# linters:
```bash
poetry run isort game
poetry run flakeheaven lint game
poetry run mypy game
poetry run autoflake -r --in-place --remove-unused-variables --remove-all-unused-imports .
```