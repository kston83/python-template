# Python 3.14 Project Template

A modern, production-ready Python project template optimized for Python 3.14, featuring fast dependency management with [uv](https://github.com/astral-sh/uv), comprehensive testing with pytest, and AI-assisted development support.

## ✨ Features

- **🐍 Python 3.14** - Latest Python with enhanced type hints and performance improvements
- **⚡ uv Package Manager** - Ultra-fast Python package installer and resolver
- **🧪 pytest** - Modern testing framework with async support and comprehensive fixtures
- **🔍 Ruff** - Extremely fast Python linter and formatter (replaces flake8, black, isort)
- **📘 mypy** - Static type checker for Python type hints
- **🤖 AI-Optimized** - Comprehensive GitHub Copilot instructions for AI-assisted development
- **📁 Flexible Structure** - Adaptable for web apps, CLI tools, libraries, or script collections
- **✅ Test-Driven Development** - Built-in TDD workflow with example tests

## 🚀 Quick Start

### Prerequisites

- Python 3.14 or higher
- [uv](https://github.com/astral-sh/uv) package manager

### Installation

1. **Clone this repository** (or use it as a template):
   ```bash
   git clone https://github.com/yourusername/python-template.git my-project
   cd my-project
   ```

2. **Install dependencies** with uv:
   ```bash
   uv sync
   ```

3. **Run the example application**:
   ```bash
   uv run python src/main.py
   ```

4. **Run tests**:
   ```bash
   uv run pytest
   ```

5. **Run linting and formatting**:
   ```bash
   uv run ruff check .
   uv run ruff format .
   ```

6. **Run type checking**:
   ```bash
   uv run mypy src/
   ```

## 📁 Project Structure

```
python-template/
├── .github/
│   ├── copilot-instructions.md    # Main AI assistant configuration
│   └── rules/                     # Modular AI rules
│       ├── 0-global-instructions.md
│       ├── 1-tech-stack-instructions.md
│       ├── 2-structure-instructions.md
│       ├── 3-python-patterns-instructions.md
│       ├── 4-code-quality-instructions.md
│       ├── 5-testing-patterns-instructions.md
│       └── 6-documentation-patterns-instructions.md
├── ai/
│   ├── prd.md                     # Product requirements document
│   ├── plan.md                    # Implementation plan
│   ├── example-prompts.md         # AI prompt examples
│   └── docs/                      # Feature documentation
│       └── example-feature.md
├── src/                           # Source code
│   ├── __init__.py
│   ├── main.py                    # Application entry point
│   ├── config.py                  # Configuration management
│   └── utils.py                   # Utility functions
├── tests/                         # Tests (mirrors src/ structure)
│   ├── __init__.py
│   ├── conftest.py                # Shared test fixtures
│   ├── test_config.py
│   └── test_utils.py
├── .gitignore                     # Git ignore rules
├── pyproject.toml                 # Project configuration & dependencies
└── README.md                      # This file
```

## 🎯 Usage

### For Web Applications

Add a web framework to dependencies:

```bash
# FastAPI (recommended for modern async APIs)
uv add fastapi uvicorn[standard] pydantic

# Flask (traditional synchronous framework)
uv add flask

# Django (full-featured framework)
uv add django
```

Organize code in `app/` directory by feature:
```
app/
├── api/
│   ├── users/
│   │   ├── routes.py
│   │   ├── service.py
│   │   └── models.py
│   └── tasks/
│       ├── routes.py
│       ├── service.py
│       └── models.py
├── core/
│   ├── config.py
│   └── database.py
└── main.py
```

### For CLI Tools

Add a CLI framework to dependencies:

```bash
# Click (popular and mature)
uv add click

# Typer (modern with type hints)
uv add typer rich
```

Organize code in `src/cli/`:
```
src/
├── cli/
│   ├── __init__.py
│   ├── main.py
│   └── commands/
│       ├── init.py
│       ├── build.py
│       └── deploy.py
└── core/
    └── logic.py
```

### For Libraries

Organize by functionality:
```
src/
├── mylib/
│   ├── __init__.py
│   ├── core.py
│   ├── utils.py
│   └── models.py
└── __init__.py
```

### For Script Collections

Keep `src/` structure with individual script files:
```
src/
├── process_data.py
├── generate_reports.py
├── cleanup_logs.py
└── utils/
    ├── file_helpers.py
    └── date_helpers.py
```

## 🧪 Testing

This template follows **Test-Driven Development (TDD)** principles:

1. **Write tests first** - Define expected behavior with tests
2. **Run tests (they should fail)** - Red phase
3. **Implement feature** - Write minimal code to pass tests
4. **Run tests again (they should pass)** - Green phase
5. **Refactor** - Improve code while keeping tests passing

### Running Tests

```bash
# Run all tests
uv run pytest

# Run with coverage report
uv run pytest --cov=src --cov-report=html

# Run specific test file
uv run pytest tests/test_utils.py

# Run tests matching a pattern
uv run pytest -k "test_config"

# Run with verbose output
uv run pytest -v
```

### Writing Tests

Example test following AAA (Arrange-Act-Assert) pattern:

```python
import pytest
from src.utils import format_message


class TestFormatMessage:
    """Tests for format_message function."""

    def test_format_message_with_custom_prefix(self) -> None:
        """Test format_message with custom prefix."""
        # Arrange
        message = "Error occurred"
        prefix = "ERROR"

        # Act
        result = format_message(message, prefix=prefix)

        # Assert
        assert result == "ERROR: Error occurred"

    @pytest.mark.parametrize(
        ("message", "prefix", "expected"),
        [
            ("Test", "DEBUG", "DEBUG: Test"),
            ("Warning", "WARN", "WARN: Warning"),
            ("", "INFO", "INFO: "),
        ],
    )
    def test_format_message_parametrized(
        self, message: str, prefix: str, expected: str
    ) -> None:
        """Test format_message with various inputs."""
        result = format_message(message, prefix=prefix)
        assert result == expected
```

## 🤖 AI-Assisted Development

This template is optimized for AI coding assistants like GitHub Copilot, Cursor AI, or Claude.

### Key Features

1. **Comprehensive Rules** - Located in `.github/copilot-instructions.md` and `.github/rules/`
2. **Example Prompts** - See `ai/example-prompts.md` for ready-to-use prompts
3. **Feature Documentation** - Template for documenting features in `ai/docs/`
4. **Context-Aware** - AI assistants can reference project structure and patterns

### Sample AI Prompts

Create a new feature:
```
Following the project structure in @file(.github/rules/2-structure-instructions.md),
create a user authentication feature with JWT tokens. Include models, services,
repository, and comprehensive tests following TDD.
```

Add tests for existing code:
```
Create comprehensive tests for @file(src/utils.py) following
@file(.github/rules/5-testing-patterns-instructions.md). Include parametrized
tests and edge cases.
```

Refactor for type safety:
```
Add comprehensive type hints to @file(src/services/email_service.py) following
@file(.github/rules/3-python-patterns-instructions.md). Ensure mypy strict mode passes.
```

See `ai/example-prompts.md` for more examples.

## 🔧 Configuration

### pyproject.toml

All project configuration is in `pyproject.toml`:

- **Project metadata** - Name, version, description, dependencies
- **Ruff configuration** - Linting and formatting rules
- **pytest configuration** - Test discovery and options
- **mypy configuration** - Type checking settings
- **Coverage configuration** - Test coverage settings

### Optional Dependencies

Uncomment or add to `[project.optional-dependencies]` in `pyproject.toml`:

```toml
[project.optional-dependencies]
web = ["fastapi>=0.110.0", "uvicorn[standard]>=0.27.0"]
cli = ["click>=8.1.0", "rich>=13.7.0"]
db = ["sqlalchemy>=2.0.0", "asyncpg>=0.29.0"]
```

Install optional dependencies:
```bash
uv sync --extra web
uv sync --extra cli
uv sync --extra db
```

## 📝 Code Quality Standards

### Type Hints

All code must include type hints:

```python
def process_data(items: list[str], limit: int) -> dict[str, int]:
    """Process items and return counts."""
    return {item: len(item) for item in items[:limit]}
```

### Docstrings

Use Google or NumPy style docstrings:

```python
def calculate_total(items: list[float], tax_rate: float = 0.1) -> float:
    """Calculate total cost including tax.

    Args:
        items: List of item prices.
        tax_rate: Tax rate as decimal (default: 0.1 for 10%).

    Returns:
        Total cost including tax.

    Raises:
        ValueError: If tax_rate is negative.

    Examples:
        >>> calculate_total([10.0, 20.0], tax_rate=0.1)
        33.0
    """
    if tax_rate < 0:
        raise ValueError("Tax rate cannot be negative")
    subtotal = sum(items)
    return subtotal * (1 + tax_rate)
```

### Code Style

- **PEP 8** compliance (enforced by Ruff)
- **snake_case** for functions and variables
- **PascalCase** for classes
- **UPPER_CASE** for constants
- **Descriptive names** over brevity
- **No magic numbers** - use named constants

## 🛠️ Development Workflow

1. **Create a feature branch**
   ```bash
   git checkout -b feature/my-feature
   ```

2. **Write tests first** (TDD)
   ```bash
   # Edit tests/test_my_feature.py
   uv run pytest tests/test_my_feature.py  # Should fail
   ```

3. **Implement feature**
   ```bash
   # Edit src/my_feature.py
   uv run pytest tests/test_my_feature.py  # Should pass
   ```

4. **Run all quality checks**
   ```bash
   uv run ruff check .          # Linting
   uv run ruff format .         # Formatting
   uv run mypy src/             # Type checking
   uv run pytest                # All tests
   ```

5. **Commit and push**
   ```bash
   git add .
   git commit -m "feat: add my feature"
   git push origin feature/my-feature
   ```

## 📚 Additional Resources

- [Python 3.14 Documentation](https://docs.python.org/3.14/)
- [uv Documentation](https://github.com/astral-sh/uv)
- [pytest Documentation](https://docs.pytest.org/)
- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [mypy Documentation](https://mypy.readthedocs.io/)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

## 📄 License

MIT License - see LICENSE file for details (add LICENSE file as needed)

## 🙋 Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/python-template/issues)
- **Documentation**: See `ai/` directory for detailed guides
- **AI Prompts**: See `ai/example-prompts.md` for AI assistant examples

---

**Happy Coding! 🚀**

Built with ❤️ using Python 3.14 and modern development tools.
