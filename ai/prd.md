# Product Requirements Document (PRD)

## Document Information
- **Project**: Python 3.14 Project Template
- **Last Updated**: February 5, 2026
- **Version**: 1.0
- **Status**: Active

> **Note**: This PRD serves as both the requirements for this template project AND as an example of a well-structured PRD. When using this template for your own project, use this document as a reference for creating your own comprehensive PRD.

---

## 1. Overview

### 1.1 Product Description
The **Python 3.14 Project Template** is a modern, production-ready foundation for Python applications. It provides developers with a pre-configured development environment featuring cutting-edge Python tooling, comprehensive testing infrastructure, type safety, and AI-assisted development support.

### 1.2 Problem Statement
Starting a new Python project often requires hours of setup: configuring package managers, setting up testing frameworks, configuring linters and formatters, establishing code quality standards, and creating project structure. Many projects begin with inconsistent patterns or outdated tooling, leading to technical debt from day one.

### 1.3 Product Vision
To provide a zero-to-production Python project template that:
- Eliminates setup friction for new Python projects
- Enforces modern Python best practices by default
- Supports multiple project types (web apps, CLI tools, libraries)
- Optimizes for AI-assisted development workflows
- Enables Test-Driven Development from the start
- Provides clear, educational examples for Python developers

### 1.4 Target Audience

#### Primary Users
- **Professional Python developers** starting new projects or microservices
- **Development teams** needing standardized Python project structure
- **Open source maintainers** creating new Python packages
- **Python learners** wanting to study modern best practices

#### Secondary Users
- **DevOps engineers** setting up Python service templates
- **AI coding assistants** (GitHub Copilot, Cursor, Claude) working with users
- **Technical leads** establishing team standards

### 1.5 Success Metrics
- **Setup Time**: <5 minutes from clone to first test run
- **Test Coverage**: >80% for example code
- **Code Quality**: 100% Ruff compliance, 100% mypy type coverage
- **Adoption**: GitHub stars, forks, and template uses
- **Developer Satisfaction**: Positive feedback on ease of use and comprehensiveness

---

## 2. Core Features & Requirements

### 2.1 Project Structure
**Purpose**: Provide clear, scalable, maintainable project organization that works for various Python project types.

#### Requirements

**PS.1: Flexible Source Organization**
- **Priority**: P0 (Critical)
- **Description**: Support multiple organizational patterns for different project types
- **Acceptance Criteria**:
  - `src/` directory structure for general projects
  - `app/` pattern documented for web services
  - Clear guidelines for CLI tools, libraries, and script collections
  - Package initialization with proper `__init__.py` files
- **Rationale**: Different project types benefit from different organizational patterns

**PS.2: Test Structure**
- **Priority**: P0 (Critical)
- **Description**: Test organization that mirrors source structure
- **Acceptance Criteria**:
  - `tests/` directory at project root
  - Test files mirror `src/` structure
  - `conftest.py` for shared fixtures
  - Example tests demonstrating best practices
- **Rationale**: Makes tests easy to locate and maintain

**PS.3: Configuration Management**
- **Priority**: P0 (Critical)
- **Description**: Type-safe, centralized configuration system
- **Acceptance Criteria**:
  - `src/config.py` with dataclass-based configuration
  - Support for environment-based configuration
  - Type hints for all configuration values
  - Example of immutable configuration with `frozen=True`
- **Rationale**: Configuration bugs are common; type-safe config prevents many issues

**PS.4: AI Documentation Structure**
- **Priority**: P1 (High)
- **Description**: Comprehensive documentation optimized for AI assistants
- **Acceptance Criteria**:
  - `ai/` directory with PRD, plans, and feature docs
  - `ai/docs/` for feature-specific documentation
  - `ai/example-prompts.md` with practical AI prompts
  - Documentation template in `ai/docs/example-feature.md`
- **Rationale**: AI assistants work better with structured, accessible documentation

**PS.5: Tool Configuration**
- **Priority**: P0 (Critical)
- **Description**: Centralized tool configuration in `pyproject.toml`
- **Acceptance Criteria**:
  - All tool configs in single file
  - No separate config files (no setup.cfg, setup.py, etc.)
  - Clear dependency organization
  - Optional dependency groups for web, cli, db, etc.
- **Rationale**: Modern Python uses pyproject.toml for all configuration

### 2.2 Development Tools
**Purpose**: Enable efficient development with modern, fast Python tooling.

#### Requirements

**DT.1: uv Package Management**
- **Priority**: P0 (Critical)
- **Description**: Ultra-fast package installation and dependency resolution
- **Acceptance Criteria**:
  - `uv sync` installs all dependencies in <10 seconds
  - Supports optional dependency groups
  - Works with Python 3.14+
  - Clear documentation for adding dependencies
- **Technical Details**:
  - Uses uv 0.1.0+
  - Replaces pip, pip-tools, and virtualenv
  - 10-100x faster than pip
- **Rationale**: Developer time is valuable; fast installs improve productivity

**DT.2: Ruff Linting & Formatting**
- **Priority**: P0 (Critical)
- **Description**: Extremely fast Python linter and formatter
- **Acceptance Criteria**:
  - Replaces flake8, black, isort, and other tools
  - Configured in `pyproject.toml` with comprehensive rules
  - Runs in <1 second on typical projects
  - Zero errors on example code
- **Technical Details**:
  - Linting rules: E, W, F, I, N, UP, ANN, ASYNC, B, C4, DTZ, T10, etc.
  - Line length: 100 characters
  - Python 3.14 target
- **Rationale**: Single tool for multiple quality checks; extraordinarily fast

**DT.3: mypy Type Checking**
- **Priority**: P1 (High)
- **Description**: Static type checking for Python type hints
- **Acceptance Criteria**:
  - Configured in `pyproject.toml`
  - Runs successfully on all example code
  - Clear documentation on running type checks
  - Examples demonstrate proper type hint usage
- **Rationale**: Catch type errors before runtime; improve IDE support

**DT.4: pytest Testing Framework**
- **Priority**: P0 (Critical)
- **Description**: Modern testing with fixtures, parametrization, and async support
- **Acceptance Criteria**:
  - pytest 8.0+ configured in dev dependencies
  - pytest-asyncio for async tests
  - pytest-cov for coverage reporting
  - pytest-mock for mocking
  - Example tests demonstrating AAA pattern
- **Technical Details**:
  - Test discovery from `tests/` directory
  - Coverage reporting with HTML output
  - Parametrized test examples
- **Rationale**: pytest is the modern standard for Python testing

**DT.5: Example Code**
- **Priority**: P0 (Critical)
- **Description**: Working example code demonstrating best practices
- **Acceptance Criteria**:
  - `src/main.py` - Entry point example
  - `src/config.py` - Configuration management
  - `src/utils.py` - Utility functions
  - All code fully type-hinted
  - All code has docstrings
  - All code tested
- **Rationale**: Examples teach by demonstration; developers learn from working code

### 2.3 Code Quality Standards
**Purpose**: Enforce consistent, high-quality code that's maintainable and professional.

#### Requirements

**CQ.1: Universal Type Hints**
- **Priority**: P0 (Critical)
- **Description**: All functions, methods, and variables must have type annotations
- **Acceptance Criteria**:
  - 100% type hint coverage on public APIs
  - Return types specified for all functions
  - Parameter types specified for all functions
  - Complex types using `typing` module
- **Examples**:
  ```python
  def process_items(items: list[str], limit: int = 10) -> dict[str, int]:
      """Process items and return counts."""
      return {item: len(item) for item in items[:limit]}
  ```
- **Rationale**: Type hints prevent bugs, improve IDE support, enable better refactoring

**CQ.2: PEP 8 Compliance**
- **Priority**: P0 (Critical)
- **Description**: All code follows PEP 8 style guide
- **Acceptance Criteria**:
  - `ruff check .` returns zero errors
  - `ruff format .` makes no changes (already formatted)
  - Consistent naming conventions
  - Proper import organization
- **Rationale**: Consistency aids readability and collaboration

**CQ.3: Comprehensive Docstrings**
- **Priority**: P1 (High)
- **Description**: All public functions, classes, and modules have docstrings
- **Acceptance Criteria**:
  - Google or NumPy style docstrings
  - Include Args, Returns, Raises sections
  - Include usage examples where helpful
  - Module-level docstrings for all modules
- **Examples**: See `src/config.py` and `src/utils.py`
- **Rationale**: Documentation is essential for maintainability and collaboration

**CQ.4: Test-Driven Development (TDD)**
- **Priority**: P1 (High)
- **Description**: Support and encourage TDD workflow
- **Acceptance Criteria**:
  - Documentation explains TDD process
  - Example tests follow TDD principles
  - README includes TDD workflow section
  - Tests demonstrate Red-Green-Refactor cycle
- **Rationale**: TDD produces better-designed, more testable code

**CQ.5: Immutable Data Structures**
- **Priority**: P2 (Medium)
- **Description**: Prefer immutable data structures where appropriate
- **Acceptance Criteria**:
  - Config uses `@dataclass(frozen=True)`
  - Documentation recommends immutability
  - Examples demonstrate immutable patterns
- **Rationale**: Immutability prevents bugs and aids reasoning about code

### 2.4 AI-Assisted Development
**Purpose**: Optimize template for AI coding assistants (Copilot, Cursor, Claude, etc.)

#### Requirements

**AI.1: Comprehensive Copilot Instructions**
- **Priority**: P1 (High)
- **Description**: Detailed instructions for GitHub Copilot in `.github/copilot-instructions.md`
- **Acceptance Criteria**:
  - Complete instructions file >200 lines
  - Covers all project conventions
  - Includes Python best practices
  - References project structure
  - Includes import guidelines
  - Covers testing patterns
- **Rationale**: AI assistants produce better code with clear instructions

**AI.2: Modular Rule System**
- **Priority**: P2 (Medium)
- **Description**: Optional modular organization of AI rules
- **Acceptance Criteria**:
  - Rules organized in `.github/rules/` directory
  - Separate files for different concerns
  - Instructions can be split or combined based on preference
- **Rationale**: Modular rules are easier to maintain and update

**AI.3: Example AI Prompts**
- **Priority**: P1 (High)
- **Description**: Ready-to-use prompts in `ai/example-prompts.md`
- **Acceptance Criteria**:
  - 10+ practical example prompts
  - Cover common tasks (features, tests, refactoring)
  - Demonstrate file references with @ syntax
  - Include explanations of prompt structure
- **Rationale**: Good prompts help developers leverage AI effectively

**AI.4: Feature Documentation Template**
- **Priority**: P1 (High)
- **Description**: Template for documenting features in `ai/docs/`
- **Acceptance Criteria**:
  - `ai/docs/example-feature.md` with complete template
  - Includes sections for purpose, API, models, logic, database
  - Clear examples
  - Easy to copy and modify
- **Rationale**: Consistent documentation helps AI understand codebase

**AI.5: PRD and Plan Documents**
- **Priority**: P1 (High)
- **Description**: Product requirements and implementation plans in `ai/`
- **Acceptance Criteria**:
  - `ai/prd.md` - This document, comprehensive PRD
  - `ai/plan.md` - Implementation plan with phases
  - Both serve as examples for users
  - Clear, professional formatting
- **Rationale**: Planning documents help AI understand project goals and context

### 2.5 Flexibility & Extensibility
**Purpose**: Support various Python project types without bloat.

#### Requirements

**FL.1: Web Application Support**
- **Priority**: P2 (Medium)
- **Description**: Easy setup for web applications
- **Acceptance Criteria**:
  - Optional dependencies for FastAPI, Flask, Django
  - Documentation for web app structure
  - Example app organization patterns
  - Clear instructions for adding web frameworks
- **Use Cases**:
  - REST APIs with FastAPI
  - Traditional web apps with Flask/Django
  - Microservices
- **Rationale**: Web applications are a common Python use case

**FL.2: CLI Tool Support**
- **Priority**: P2 (Medium)
- **Description**: Easy setup for command-line tools
- **Acceptance Criteria**:
  - Optional dependencies for Click, Typer
  - Documentation for CLI structure
  - Example CLI organization patterns
  - Clear instructions for adding CLI frameworks
- **Use Cases**:
  - Developer tools
  - System utilities
  - Data processing scripts
- **Rationale**: Python excels at CLI tools

**FL.3: Library Development Support**
- **Priority**: P2 (Medium)
- **Description**: Structure suitable for distributable packages
- **Acceptance Criteria**:
  - Proper package structure
  - `pyproject.toml` configured for distribution
  - Documentation on library organization
  - Example of public API exports
- **Use Cases**:
  - Open source libraries
  - Internal company packages
  - Reusable components
- **Rationale**: Python's packaging ecosystem is important

**FL.4: Script Collection Support**
- **Priority**: P2 (Medium)
- **Description**: Support for collections of utility scripts
- **Acceptance Criteria**:
  - Flexible `src/` organization
  - Shared utilities in `src/utils/`
  - Documentation for script organization
- **Use Cases**:
  - Data processing pipelines
  - Automation scripts
  - Internal tools
- **Rationale**: Not every project needs a full framework

**FL.5: Optional Dependencies**
- **Priority**: P1 (High)
- **Description**: Keep base template lightweight with optional dependency groups
- **Acceptance Criteria**:
  - Base template has minimal dependencies
  - Optional groups: web, cli, db, async
  - Clear documentation on adding dependencies
  - Examples of using optional dependencies
- **Rationale**: Don't force dependencies users don't need

---

## 3. Technical Requirements

### 3.1 Performance

**Requirement**: Fast developer workflows
- **Dependency Installation**: <10 seconds with uv
- **Test Execution**: <5 seconds for example tests
- **Linting**: <1 second with Ruff
- **Formatting**: <1 second with Ruff
- **Type Checking**: <3 seconds with mypy

**Rationale**: Developer time is valuable; fast feedback loops improve productivity.

### 3.2 Compatibility

**Python Version**: Python 3.14+
- **Rationale**: Latest Python features, performance improvements, enhanced type hints

**Operating Systems**:
- macOS (primary)
- Linux (Ubuntu, Debian, RHEL, etc.)
- Windows (with WSL recommended)

**Package Manager**: uv 0.1.0+
- **Fallback**: Standard pip/virtualenv still works but not recommended

### 3.3 Code Quality Metrics

**Test Coverage**: >80% for all example code
- Measured with pytest-cov
- HTML coverage reports generated
- Critical paths have 100% coverage

**Type Coverage**: 100% for public APIs
- All public functions type-hinted
- Complex types properly annotated
- Passes mypy strict mode

**Linting**: Zero errors with Ruff
- Comprehensive rule set enabled
- No ignores in example code
- Clear linting instructions

### 3.4 Developer Experience

**Setup Time**: <5 minutes
- Clone repository
- Run `uv sync`
- Run `uv run pytest`
- All tests pass

**Documentation Quality**:
- Comprehensive README with examples
- Clear quick start guide
- Multiple usage examples
- Troubleshooting section
- AI prompt examples

**Error Messages**:
- Clear, actionable error messages
- Type errors caught early
- Test failures with helpful output

### 3.5 Security

**No Hardcoded Secrets**: All sensitive data via environment variables
**Dependency Security**: Regular updates to dependencies
**Secure Defaults**: Configuration defaults are secure
**.gitignore**: Prevents committing sensitive files

---

## 4. User Stories

### 4.1 Developer Starting New Project

**As a** Python developer starting a new project  
**I want** a pre-configured template with modern tooling  
**So that** I can focus on building features instead of setup

**Acceptance Criteria**:
- Clone template in <1 minute
- Install dependencies in <10 seconds
- Run example code immediately
- Understand structure from README
- Add first feature within 30 minutes

### 4.2 Team Establishing Standards

**As a** technical lead  
**I want** a standardized Python project structure  
**So that** all team projects follow consistent patterns

**Acceptance Criteria**:
- Template enforces team standards
- Easy to customize for team needs
- Clear documentation for team members
- AI instructions reflect team practices
- Can create internal template fork

### 4.3 Developer Learning Best Practices

**As a** Python developer improving my skills  
**I want** examples of modern Python best practices  
**So that** I can learn professional development patterns

**Acceptance Criteria**:
- Example code demonstrates best practices
- Comments explain design decisions
- Tests show TDD approach
- Documentation teaches patterns
- AI instructions explain reasoning

### 4.4 AI Assistant Helping Developer

**As** GitHub Copilot  
**I want** clear, structured project documentation  
**So that** I can generate better, more accurate code

**Acceptance Criteria**:
- Comprehensive Copilot instructions
- Clear project structure
- Documented patterns and conventions
- Example prompts for common tasks
- Feature documentation in `ai/docs/`

### 4.5 Open Source Maintainer

**As an** open source maintainer  
**I want** a professional project structure  
**So that** contributors can easily understand and contribute

**Acceptance Criteria**:
- Professional README
- Clear contribution guidelines
- Comprehensive tests
- Type hints for API clarity
- Good documentation

---

## 5. Technical Architecture

### 5.1 Directory Structure

```
python-template/
├── .github/
│   ├── copilot-instructions.md    # AI assistant configuration
│   └── rules/                     # Modular AI rules (optional)
│       ├── 0-global-instructions.md
│       ├── 1-tech-stack-instructions.md
│       ├── 2-structure-instructions.md
│       ├── 3-python-patterns-instructions.md
│       ├── 4-code-quality-instructions.md
│       ├── 5-testing-patterns-instructions.md
│       └── 6-documentation-patterns-instructions.md
├── ai/
│   ├── prd.md                     # This document
│   ├── plan.md                    # Implementation plan
│   ├── example-prompts.md         # AI prompt examples
│   └── docs/                      # Feature documentation
│       └── example-feature.md
├── src/                           # Source code
│   ├── __init__.py
│   ├── main.py                    # Application entry point
│   ├── config.py                  # Configuration management
│   └── utils.py                   # Utility functions
├── tests/                         # Tests (mirrors src/)
│   ├── __init__.py
│   ├── conftest.py                # Shared fixtures
│   ├── test_config.py
│   └── test_utils.py
├── .gitignore                     # Git ignore rules
├── pyproject.toml                 # Project config & dependencies
└── README.md                      # Project documentation
```

### 5.2 Technology Stack

**Core**:
- Python 3.14
- uv (package management)

**Development Tools**:
- pytest 8.0+ (testing)
- pytest-asyncio (async testing)
- pytest-cov (coverage)
- pytest-mock (mocking)
- Ruff (linting & formatting)
- mypy (type checking)

**Optional** (based on project type):
- **Web**: FastAPI, uvicorn, pydantic OR Flask OR Django
- **CLI**: Click, Typer, rich
- **Database**: SQLAlchemy, asyncpg, psycopg
- **Async HTTP**: httpx, aiohttp

### 5.3 Design Patterns

**Configuration**: Dataclass-based, type-safe, immutable
**Testing**: Arrange-Act-Assert (AAA) pattern
**Error Handling**: Specific exceptions, clear messages
**Code Organization**: Feature-based or layer-based (depends on project type)
**Dependency Management**: Dependency injection for testability

### 5.4 Code Quality Tools Integration

**Ruff** (pyproject.toml):
```toml
[tool.ruff]
target-version = "py314"
line-length = 100

[tool.ruff.lint]
select = ["E", "W", "F", "I", "N", "UP", "ANN", "ASYNC", "B", ...]
```

**pytest** (pyproject.toml):
```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
```

**mypy** (pyproject.toml):
```toml
[tool.mypy]
python_version = "3.14"
warn_return_any = true
warn_unused_configs = true
```

---

## 6. Non-Functional Requirements

### 6.1 Usability
- Setup completes in <5 minutes
- README provides clear quick start
- Examples are easy to understand
- Error messages guide users to solutions

### 6.2 Maintainability
- Modular code organization
- Comprehensive tests (>80% coverage)
- Clear documentation
- Well-structured type hints
- Consistent patterns throughout

### 6.3 Extensibility
- Easy to add new dependencies
- Optional dependency groups
- Clear examples for customization
- Adaptable to different project types

### 6.4 Reliability
- All example code tested
- CI/CD ready (optional GitHub Actions)
- Dependency pinning available
- Stable, well-maintained tools

### 6.5 Portability
- Works on macOS, Linux, Windows
- Pure Python (no platform-specific code in examples)
- Clear documentation for platform differences

---

## 7. Constraints & Assumptions

### 7.1 Constraints
- **Python Version**: Requires Python 3.14+ (for latest features)
- **Package Manager**: Strongly recommends uv (but pip still works)
- **Tool Choices**: Opinionated tool selection (Ruff, pytest, mypy)
- **Structure**: Opinionated but flexible structure

### 7.2 Assumptions
- Users have basic Python knowledge
- Users understand virtual environments
- Users have git installed
- Users can install Python 3.14 or higher
- Users want modern, best-practice Python development

### 7.3 Out of Scope
- Specific business logic implementations
- Production deployment configurations
- Container/Docker setup (can be added by user)
- CI/CD pipelines (optional, not included by default)
- Database migrations (depends on project)
- Authentication/authorization (depends on project)

---

## 8. Future Considerations

### 8.1 Potential Enhancements
- **GitHub Actions**: Pre-configured CI/CD workflows
- **Pre-commit Hooks**: Automated quality checks before commit
- **Docker Support**: Example Dockerfile and docker-compose
- **VS Code Config**: Recommended extensions and settings
- **Additional Examples**: More complete example applications
- **Documentation Site**: Sphinx or MkDocs setup
- **Performance Monitoring**: Example integration with monitoring tools
- **Logging**: Structured logging examples
- **CLI for Bootstrap**: Command to create new projects from template

### 8.2 Community Contributions
- Web framework templates (FastAPI starter, Flask starter, Django starter)
- CLI tool templates
- Data science project template
- ML/AI project template
- Microservices template
- Additional AI assistant configurations

### 8.3 Long-term Vision
- Become the de-facto Python project template
- Build ecosystem of domain-specific extensions
- Integration with more AI coding assistants
- Template gallery for different use cases
- Community-driven best practices
- Regular updates for new Python versions

---

## 9. Risks & Mitigations

### 9.1 Risk: Tool Compatibility
**Risk**: New tools may conflict or break with updates  
**Probability**: Medium  
**Impact**: Medium  
**Mitigation**: Pin dependency versions, regular testing, changelogs

### 9.2 Risk: Python Version Availability
**Risk**: Python 3.14 may not be available on all systems  
**Probability**: High  
**Impact**: Low  
**Mitigation**: Document installation, provide fallback instructions, pyenv recommended

### 9.3 Risk: Opinionated Choices
**Risk**: Users may prefer different tools (Black vs Ruff, etc.)  
**Probability**: High  
**Impact**: Low  
**Mitigation**: Document choices, explain rationale, keep customization easy

### 9.4 Risk: Complexity for Beginners
**Risk**: Too many tools may overwhelm beginners  
**Probability**: Medium  
**Impact**: Medium  
**Mitigation**: Excellent documentation, clear examples, gradual learning curve

---

## 10. Appendix

### 10.1 Glossary
- **uv**: Ultra-fast Python package installer and resolver
- **Ruff**: Fast Python linter and formatter (replaces multiple tools)
- **mypy**: Static type checker for Python
- **pytest**: Modern Python testing framework
- **TDD**: Test-Driven Development methodology
- **PEP 8**: Python Enhancement Proposal 8, Python style guide
- **Type Hints**: Python type annotations for static analysis

### 10.2 References
- [Python 3.14 Documentation](https://docs.python.org/3.14/)
- [uv Documentation](https://github.com/astral-sh/uv)
- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [pytest Documentation](https://docs.pytest.org/)
- [mypy Documentation](https://mypy.readthedocs.io/)
- [PEP 8 Style Guide](https://pep8.org/)

### 10.3 Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-02-05 | Template Author | Initial comprehensive PRD |

---

**End of Product Requirements Document**