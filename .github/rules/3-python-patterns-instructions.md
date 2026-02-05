## Files
src/**/*.py
app/**/*.py

## Rules
- **Type Hints:** Always use type hints for function parameters, return values, and class attributes.
- **Imports:** Follow standard import grouping: stdlib, third-party, local (separated by blank lines).
- **Functions:** Keep functions small, focused, and pure when possible. One function, one responsibility.
- **Classes:** Use dataclasses or Pydantic models for data structures. Prefer composition over inheritance.
- **Error Handling:** Use specific exception types. Create custom exceptions for domain-specific errors.
- **Async/Await:** Use `async def` and `await` for I/O-bound operations. Be consistent with async patterns.
- **Context Managers:** Use `with` statements for resource management (files, connections, locks).
- **Constants:** Define constants at module level using UPPER_CASE naming.
- **State Management:** For web apps, use dependency injection. Avoid global mutable state.
- **Immutability:** Prefer immutable data structures. Use `frozen=True` for dataclasses when appropriate.
- **Naming:** Use descriptive names. `snake_case` for functions/variables, `PascalCase` for classes.

