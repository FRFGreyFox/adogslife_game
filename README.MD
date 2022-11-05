# linters:

```bash
poetry run isort game
poetry run flakeheaven lint game
poetry run mypy game
poetry run autoflake -r --in-place --remove-unused-variables --remove-all-unused-imports .
```