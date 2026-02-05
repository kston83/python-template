"""Shared test fixtures and configuration."""

import pytest


@pytest.fixture
def sample_config() -> dict[str, str | int | bool]:
    """Provide a sample configuration for testing.

    Returns:
        A dictionary containing sample configuration values.
    """
    return {
        "debug": True,
        "port": 8000,
        "host": "localhost",
        "environment": "test",
    }
