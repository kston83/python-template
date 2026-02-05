# AI Rules for Python 3.14 / uv Template

# General Information

This is a Python project using Python 3.14 and uv for package management, following Test-Driven Development (TDD) principles and modern Python best practices. This template is designed to be flexible and project-agnostic, suitable for web applications, CLI tools, libraries, or any Python project. Always consider the following background information and guidelines when implementing features.

## Quick Reference

### Common Patterns & Structure
- Organize code in the `src/` directory for application code or `app/` for service-based projects.
- Place reusable utilities in `src/utils/` or `app/utils/`.
- Define configuration in `src/config/` or `app/config/`.
- Document features and architecture in `ai/docs/{featureName}.md`.
- For web APIs: organize by feature in `app/api/` or `src/api/`.
- For CLI tools: organize commands in `src/cli/` or `src/commands/`.
- For libraries: organize modules logically by functionality.
- Reference `@file(ai/prd.md)` and `@file(ai/plan.md)` for project requirements and implementation plans.
- Follow TDD: Write tests first, then implement functionality to pass those tests.

### Common Issues & Checks
- Ensure virtual environment is activated and managed by `uv`.
- Run `uv sync` to install/update dependencies from `pyproject.toml`.
- Use absolute imports from your package root (e.g., `from src.models.user import User`).
- Type hint all function parameters and return values using Python's typing module.
- Ensure code passes linting: `ruff check .` and `ruff format .`.
- Run tests with `pytest` before committing code.
- For async operations, use `async/await` consistently.
- Check `pyproject.toml` for project-specific dependencies and tool configurations.

## Background Information

### Project Overview
This is a modern Python application template using Python 3.14 and uv for fast, reliable dependency management. The project emphasizes type safety, testing, and maintainable code architecture. It can be adapted for web services, CLI applications, data processing pipelines, libraries, or any Python project.

### Core Technologies
- **Python 3.14**: Latest Python with enhanced type hints and performance improvements. [cite: python-template-ai/pyproject.toml]
- **uv**: Ultra-fast Python package installer and resolver for dependency management.
- **pytest**: Modern testing framework with fixtures, parametrization, and plugin support. [cite: python-template-ai/pyproject.toml]
- **Ruff**: Extremely fast Python linter and formatter (replaces flake8, black, isort). [cite: python-template-ai/pyproject.toml]
- **mypy**: Static type checker for Python type hints.

### Optional/Project-Specific Technologies
Depending on your project type, you may add:
- **Web Frameworks**: FastAPI, Django, Flask
- **Database**: SQLAlchemy, asyncpg, psycopg3
- **CLI**: Click, Typer, argparse
- **Data/ML**: pandas, numpy, scikit-learn
- **Async**: asyncio, aiohttp, httpx

### Project Architecture
Flexible architecture that adapts to your needs:
- **Web Services**: `app/api/`, `app/core/`, `app/models/`, `app/services/`
- **CLI Tools**: `src/cli/`, `src/commands/`, `src/core/`
- **Libraries**: `src/{package_name}/`, organized by functionality
- **General**: `src/` or `app/` for main code, `tests/` mirroring source structure
- **Configuration**: `pyproject.toml` for all tool configs and dependencies
- **Documentation**: `ai/` for AI-related docs, `docs/` for user docs

### Python Best Practices
- **Type Hints**: Use type hints extensively for all function signatures, variables, and class attributes.
- **Async/Await**: Use `async def` and `await` for I/O-bound operations when appropriate.
- **Error Handling**: Use specific exceptions; create custom exception classes when needed.
- **Immutability**: Prefer immutable data structures; use `dataclasses` with `frozen=True` when appropriate.
- **Function Design**: Keep functions small, focused, and pure when possible.
- **SOLID Principles**: Follow SOLID design principles, especially Single Responsibility.
- **Dependency Injection**: Design for testability; inject dependencies rather than hardcoding them.
- **Configuration**: Use environment variables and config files; never hardcode secrets.
- **Logging**: Use Python's `logging` module; avoid print statements in production code.
- **Resource Management**: Use context managers (`with` statements) for resource cleanup.

### Python Code Style
- **PEP 8:** Follow PEP 8 style guide for Python code.
- **Naming Conventions:**
  - `snake_case` for functions, variables, and module names
  - `PascalCase` for class names
  - `UPPER_CASE` for constants
  - Prefix private attributes with underscore: `_private_method`
- **Docstrings:** Use Google-style or NumPy-style docstrings for functions and classes.
- **Type Hints:** Always include type hints; use `typing` module features like `Optional`, `Union`, `List`, `Dict`.
- **Imports:** 
  - Group imports: stdlib, third-party, local
  - Use absolute imports from `app` module
  - Avoid circular imports

### Import Guidelines
- Use absolute imports from your package root (e.g., `from src.models.user import User` or `from app.models.user import User`).
- Group imports in the following order:
  1. Standard library imports
  2. Third-party library imports
  3. Local application imports
- Each group should be separated by a blank line.
- Sort imports alphabetically within each group.
- Use `from` imports for specific items when it improves readability.
- Avoid wildcard imports: Never use `from module import *`.
- Use `if TYPE_CHECKING:` for type-only imports to avoid circular dependencies.

## Rules

### General Rules
- Always prioritize requirements from `@file(python-template-ai/ai/prd.md)` and the implementation sequence from `@file(python-template-ai/ai/plan.md)`.
- Reference existing feature documentation in `@file(ai/docs/)` before creating similar logic.
- Use Python type hints strictly. Define types clearly using the `typing` module.
- Follow PEP 8 style guide and ensure code passes Ruff linting: `ruff check .`.
- Document complex logic with comments and docstrings.
- Follow TDD: Write tests first, then implement functionality to make tests pass.
- Use environment variables for configuration; never hardcode secrets or sensitive data.

### Code Organization Rules
- Separate concerns: keep business logic separate from I/O operations.
- Use the service layer pattern for complex business logic.
- Use the repository pattern for data access when working with databases.
- Keep modules focused on a single responsibility.
- Create clear interfaces between layers using protocols or abstract base classes.
- Use dependency injection for better testability and flexibility.
- Organize related functionality into packages with clear `__init__.py` exports.
- For web APIs (FastAPI): organize routes, services, and models by feature.
- For CLI tools: separate command definitions from business logic.
- For libraries: organize by functionality with a clear public API.

### Module Organization
- Organize code into logical modules based on functionality.
- For web applications, consider feature-based organization:
  - `{feature}/service.py`: Business logic
  - `{feature}/models.py`: Data models
  - `{feature}/repository.py`: Data access (if using database)
  - `{feature}/exceptions.py`: Custom exceptions
  - `{feature}/schemas.py`: Data validation schemas
- For libraries, organize by functionality with clear namespaces.
- For CLI tools, separate command definitions from implementation.
- Keep modules loosely coupled and highly cohesive.
- Export public APIs through `__init__.py` using `__all__`.
- Document module purpose and public interfaces.

### Design Principles
- **DRY (Don't Repeat Yourself)**: Extract common patterns into reusable functions/classes.
- **KISS (Keep It Simple)**: Favor simple, clear solutions over clever but complex ones.
- **YAGNI (You Aren't Gonna Need It)**: Don't add functionality until it's needed.
- **Separation of Concerns**: Keep different aspects of the application separate.
- **Fail Fast**: Validate inputs early and raise clear exceptions.
- **Explicit is Better Than Implicit**: Follow the Zen of Python.
- **Type Safety**: Use type hints to catch errors early.
- **Testability**: Design code to be easily testable.
- **Documentation**: Write self-documenting code with clear names and docstrings.

### Documentation
- Document new/updated features in `ai/docs/` following `@file(python-template-ai/ai/docs/example-feature.md)`.
- Include purpose, API endpoints, data models, business logic, database schema, and usage examples.
- Add docstrings to all functions, classes, and modules using Google or NumPy style.
- Keep docstrings current with code changes.
- Document complex algorithms and business rules inline with comments.

# Testing Rules (pytest / TDD)

### General Testing Rules
- Follow Test-Driven Development: Write tests BEFORE implementation.
- Organize tests to mirror the `app/` or `src/` structure in a `tests/` directory.
- Use pytest as the test runner with pytest-asyncio for async tests.
- Follow the Arrange-Act-Assert (AAA) pattern in test functions.
- Use pytest fixtures for shared setup and teardown.
- Mock external dependencies (databases, APIs, services) using `pytest-mock` or `unittest.mock`.
- Name test files as `test_{module}.py` and test functions as `test_{function_name}_{scenario}`.
- Run tests with `pytest` or `pytest -v` for verbose output.

### Unit Testing Rules
- Test business logic independently of I/O operations.
- Test one thing per test function.
- Use pytest parametrize decorator for testing multiple input scenarios.
- Test both happy path and error conditions.
- Ensure test isolation: each test should be independent.
- Use descriptive test names that explain what is being tested.
- Mock external dependencies and focus on the unit under test.

### Integration Testing Rules
- Test interactions between multiple components or modules.
- Use appropriate test fixtures for setup/teardown.
- For database tests, use a test database or in-memory database.
- Clean up resources after each test.
- Test realistic scenarios and data flows.
- Verify side effects and state changes.

### Async Testing Rules
- Use pytest-asyncio for testing async functions.
- Mark async tests with `@pytest.mark.asyncio`.
- Test async context managers and generators properly.
- Mock async dependencies appropriately.

---
Keep this `.github/copilot-instructions.md` file (or the files within `.github/rules/` if you migrate) updated with any new project conventions or best practices.