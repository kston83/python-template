"""Main application entry point."""

from src.config import load_config
from src.utils import format_message


def main() -> None:
    """Run the main application."""
    config = load_config()
    message = format_message(f"Application starting on {config.host}:{config.port}")
    print(message)
    print(f"Environment: {config.environment}")
    print(f"Debug mode: {config.debug}")


if __name__ == "__main__":
    main()
