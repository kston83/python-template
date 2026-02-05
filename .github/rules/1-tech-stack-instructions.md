## Files
*

## Tech Stack
- **Language**: Python 3.14 [cite: python-template-ai/pyproject.toml]
- **Package Manager**: uv (fast Python package installer and resolver)
- **Testing**: pytest with pytest-asyncio for async support [cite: python-template-ai/pyproject.toml]
- **Linting & Formatting**: Ruff (replaces flake8, black, isort) [cite: python-template-ai/pyproject.toml]
- **Type Checking**: mypy for static type analysis
- **Configuration**: pyproject.toml for all tool configurations and dependencies

## Optional/Project-Specific
- **Web Framework**: FastAPI, Django, Flask (choose based on project needs)
- **Database**: SQLAlchemy, asyncpg, psycopg3 (if database required)
- **CLI**: Click, Typer (if building CLI tools)
- **Async**: asyncio, aiohttp, httpx (for async operations)
- **Data/ML**: pandas, numpy, scikit-learn (for data projects)

## Key Configuration File
- Dependencies & Tools: `@file(python-template-ai/pyproject.toml)`