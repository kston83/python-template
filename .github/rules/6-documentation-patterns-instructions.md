## Files
ai/docs/**/*.md
src/**/*.py
app/**/*.py

## Rules
- **Feature Docs:** Document new features in `ai/docs/{feature_name}.md` following the example structure.
- **Docstrings:** Use Google-style or NumPy-style docstrings for all public functions, classes, and modules.
- **Type Hints:** Type hints serve as inline documentation. Use them extensively.
- **README:** Keep README.md updated with setup instructions, usage examples, and project overview.
- **API Docs:** For web APIs, leverage framework's automatic documentation (e.g., FastAPI's /docs).
- **Inline Comments:** Use inline comments sparingly for complex algorithms or non-obvious logic.
- **Examples:** Include usage examples in docstrings and feature documentation.
- **Architecture Docs:** Document major architectural decisions in `ai/docs/` or `docs/architecture/`.
- **Keep Current:** Update documentation when code changes. Outdated docs are worse than no docs.
- **Changelog:** Maintain a CHANGELOG.md for tracking changes between versions.