```markdown
## Files
src/**/*.py
app/**/*.py

## Rules
- **Ruff:** Use Ruff for linting and formatting. Run `ruff check .` and `ruff format .` before committing.
- **Type Safety:** Enable strict type checking with mypy. Add type hints to all public APIs.
- **PEP 8:** Follow PEP 8 style guide. Ruff handles most of this automatically.
- **Docstrings:** Write docstrings for all public functions, classes, and modules using Google or NumPy style.
- **Code Complexity:** Keep functions under 50 lines. Extract complex logic into smaller functions.
- **Magic Numbers:** Avoid magic numbers. Define constants with descriptive names.
- **Comments:** Write comments for "why", not "what". Code should be self-documenting for "what".
- **DRY:** Don't repeat yourself. Extract common patterns into reusable functions or classes.
- **SOLID:** Follow SOLID principles, especially Single Responsibility Principle.
- **Error Messages:** Write clear, actionable error messages that help users understand what went wrong.
```
