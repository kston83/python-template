# Example AI Prompts for Python 3.14 / uv Template

This document contains example prompts to use with AI coding assistants like GitHub Copilot, Cursor AI, or Claude when working with this template. These prompts are structured to help the AI understand the project architecture (Python 3.14, uv, pytest, Ruff, mypy) and generate consistent, high-quality code by referencing the `.github/copilot-instructions.md` and `.github/rules/` directory.

## Feature Creation

### Create a New Feature with TDD

Following the project structure in @file(.github/rules/2-structure-instructions.md) and Python patterns in @file(.github/rules/3-python-patterns-instructions.md), create a new feature called "user_management" that allows managing user accounts. The feature should include:

- A `User` dataclass in `src/models/user.py` with fields: id, username, email, created_at
- A `UserService` class in `src/services/user_service.py` with methods: create_user, get_user, update_user, delete_user
- A `UserRepository` class in `src/repositories/user_repository.py` for data persistence (in-memory for now)
- Type hints for all functions and classes
- Comprehensive tests in `tests/test_user_management.py` written BEFORE implementation
- Follow TDD approach from @file(.github/rules/5-testing-patterns-instructions.md)

### Extend an Existing Feature

Based on the existing configuration feature in @file(src/config.py), add environment-specific configuration loading from `.env` files. Update the `Config` class to:

- Load from environment variables using `os.getenv()`
- Support different environments (dev, staging, prod)
- Include validation for required configuration
- Maintain type safety with proper type hints
- Add corresponding tests following @file(.github/rules/5-testing-patterns-instructions.md)

## Module Creation

### Create a Database Module

Create a new database module at `src/database.py` that:

- Defines a `Database` protocol or abstract base class
- Implements connection management using context managers
- Includes async support using `async with` statements
- Has proper type hints for all methods
- Follows patterns in @file(.github/rules/3-python-patterns-instructions.md)
- Place corresponding tests in `tests/test_database.py`
- Mock database connections using `pytest-mock`

### Create a Logging Module

Create a logging utility module at `src/utils/logging.py` that:

- Sets up structured logging with JSON output
- Includes log level configuration from environment
- Provides decorators for function/method logging
- Has context manager for temporary log level changes
- Uses type hints extensively
- Follows code quality standards from @file(.github/rules/4-code-quality-instructions.md)
- Include tests for all functionality

## Testing

### Create Comprehensive Tests for Utils

Create comprehensive tests for @file(src/utils.py) following @file(.github/rules/5-testing-patterns-instructions.md). Include:

- Unit tests for each function using AAA pattern (Arrange-Act-Assert)
- Parametrized tests using `@pytest.mark.parametrize` for multiple scenarios
- Edge case testing (empty strings, None values, etc.)
- Error condition testing with `pytest.raises`
- Mock external dependencies if any
- Achieve >90% code coverage

### Create Async Tests

Create tests for an async HTTP client in `tests/test_http_client.py`:

- Use `@pytest.mark.asyncio` for async test functions
- Mock async HTTP calls using `pytest-mock` or `aioresponses`
- Test both successful responses and error conditions
- Test timeout scenarios
- Follow async patterns from @file(.github/rules/3-python-patterns-instructions.md)

## API Development (FastAPI)

### Create a REST API Endpoint

Create a FastAPI endpoint for user management at `app/api/users.py`:

- Define Pydantic models for request/response validation
- Implement GET, POST, PUT, DELETE endpoints
- Use dependency injection for services
- Include proper error handling with HTTPException
- Add comprehensive docstrings
- Follow structure patterns from @file(.github/rules/2-structure-instructions.md)
- Write tests using FastAPI's TestClient

### Create API Middleware

Create middleware for request logging in `app/middleware/logging.py`:

- Log all incoming requests with method, path, and timestamp
- Log response status and duration
- Use Python's `logging` module
- Follow async patterns for FastAPI middleware
- Include type hints
- Add tests for middleware functionality

## CLI Development

### Create a CLI Tool with Click

Create a CLI tool using Click in `src/cli/main.py`:

- Define commands for data processing tasks
- Include options and arguments with proper types
- Add helpful documentation strings
- Implement progress bars for long-running tasks
- Include error handling with user-friendly messages
- Follow patterns from @file(.github/rules/3-python-patterns-instructions.md)
- Write tests using Click's testing utilities

### Add CLI Command Group

Add a command group for database operations to the existing CLI:

- Include commands: `migrate`, `seed`, `reset`
- Use Click's group and decorators
- Include confirmation prompts for destructive operations
- Add `--dry-run` flag for preview mode
- Provide clear help text for all commands
- Test all commands with mocked database operations

## Type Definitions

### Define Domain Models

Define comprehensive type definitions for an e-commerce order system in `src/models/order.py`:

- `Order` dataclass with id, user_id, items, total, status, created_at
- `OrderItem` dataclass with product_id, quantity, price
- `OrderStatus` enum with PENDING, PROCESSING, SHIPPED, DELIVERED, CANCELLED
- Use `dataclasses` with `frozen=True` where appropriate
- Include type hints using `typing` module features
- Add validation methods where needed
- Follow patterns from @file(.github/rules/3-python-patterns-instructions.md)

### Create Protocol Definitions

Create protocol definitions for repository interfaces in `src/protocols/repository.py`:

- Define `Repository` protocol with generic type parameter
- Include methods: save, find_by_id, find_all, delete
- Use `typing.Protocol` for structural subtyping
- Add type hints with generics (`T`, `List[T]`, etc.)
- Include comprehensive docstrings
- Demonstrate protocol usage in example implementation

## Documentation

### Document a Feature

Create documentation for a caching feature in `ai/docs/caching.md` following @file(ai/docs/example-feature.md). Include:

- Overview and purpose
- Data models and types
- API/function signatures
- Usage examples with code snippets
- Performance considerations
- Testing approach
- Integration points

### Add Function Docstrings

Add Google-style docstrings to all functions in `src/services/email_service.py`:

- Include function purpose
- Document all parameters with types
- Document return values
- Include usage examples
- Note any exceptions raised
- Follow documentation patterns from @file(.github/rules/6-documentation-patterns-instructions.md)

## Code Quality

### Refactor for Type Safety

Refactor the existing `data_processor.py` module to improve type safety:

- Add comprehensive type hints to all functions
- Replace `Any` types with specific types
- Use `TypedDict` for dictionary structures
- Add generic types where appropriate
- Ensure mypy strict mode passes
- Follow patterns from @file(.github/rules/4-code-quality-instructions.md)

### Improve Error Handling

Improve error handling in `src/api/handlers.py`:

- Create custom exception classes in `src/exceptions.py`
- Replace generic exceptions with specific ones
- Add proper error messages with context
- Implement error logging
- Add error recovery where possible
- Write tests for error conditions

## Async Programming

### Create Async Data Fetcher

Create an async data fetcher in `src/services/data_fetcher.py`:

- Use `async def` for all I/O-bound operations
- Implement concurrent requests using `asyncio.gather()`
- Add timeout handling with `asyncio.wait_for()`
- Include retry logic with exponential backoff
- Use `aiohttp` or `httpx` for HTTP requests
- Follow async patterns from @file(.github/rules/3-python-patterns-instructions.md)
- Write async tests with `pytest-asyncio`

### Convert Sync to Async

Convert the synchronous file processor in `src/processors/file_processor.py` to async:

- Change all I/O operations to async alternatives
- Use `aiofiles` for async file operations
- Implement batch processing with `asyncio.gather()`
- Maintain type safety with proper async type hints
- Update all tests to use `@pytest.mark.asyncio`
- Ensure backward compatibility if needed