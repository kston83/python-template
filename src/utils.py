"""Utility functions for the project."""

from typing import Any


def format_message(message: str, prefix: str = "INFO") -> str:
    """Format a message with a prefix.

    Args:
        message: The message to format.
        prefix: The prefix to add to the message. Defaults to "INFO".

    Returns:
        The formatted message.

    Examples:
        >>> format_message("Hello, World!")
        'INFO: Hello, World!'
        >>> format_message("Error occurred", prefix="ERROR")
        'ERROR: Error occurred'
    """
    return f"{prefix}: {message}"


def validate_config(config: dict[str, Any]) -> bool:
    """Validate configuration dictionary.

    Args:
        config: Configuration dictionary to validate.

    Returns:
        True if configuration is valid, False otherwise.

    Examples:
        >>> validate_config({"debug": True, "port": 8000})
        True
        >>> validate_config({})
        False
    """
    required_keys = {"debug", "port"}
    return all(key in config for key in required_keys)
