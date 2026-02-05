## Files
tests/**/*.py

## Rules
- **TDD:** Write tests BEFORE implementation. Red-Green-Refactor cycle.
- **Test Organization:** Mirror source structure in `tests/` directory. Name files `test_{module}.py`.
- **Pytest:** Use pytest as the test runner. Use fixtures for setup/teardown.
- **AAA Pattern:** Follow Arrange-Act-Assert pattern in all test functions.
- **Test Names:** Use descriptive names: `test_{function_name}_{scenario}_{expected_result}`.
- **Parametrize:** Use `@pytest.mark.parametrize` for testing multiple scenarios.
- **Mocking:** Mock external dependencies (databases, APIs, filesystem) using `pytest-mock` or `unittest.mock`.
- **Async Tests:** Use `@pytest.mark.asyncio` for async test functions.
- **Assertions:** Use clear, specific assertions. Include helpful error messages.
- **Coverage:** Aim for high test coverage, but focus on critical paths and edge cases.
- **Independence:** Each test should be independent and able to run in any order.
- **Fast Tests:** Keep unit tests fast. Use fixtures and mocks to avoid slow I/O operations.