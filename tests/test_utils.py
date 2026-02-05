"""Tests for utility functions."""

import pytest

from src.utils import format_message, validate_config


class TestFormatMessage:
    """Tests for format_message function."""

    def test_format_message_with_default_prefix(self) -> None:
        """Test format_message with default prefix."""
        result = format_message("Hello, World!")
        assert result == "INFO: Hello, World!"

    def test_format_message_with_custom_prefix(self) -> None:
        """Test format_message with custom prefix."""
        result = format_message("Error occurred", prefix="ERROR")
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


class TestValidateConfig:
    """Tests for validate_config function."""

    def test_validate_config_with_required_keys(self) -> None:
        """Test validate_config with all required keys present."""
        config = {"debug": True, "port": 8000}
        assert validate_config(config) is True

    def test_validate_config_with_missing_keys(self) -> None:
        """Test validate_config with missing required keys."""
        config = {"debug": True}
        assert validate_config(config) is False

    def test_validate_config_with_empty_dict(self) -> None:
        """Test validate_config with empty dictionary."""
        config = {}
        assert validate_config(config) is False

    def test_validate_config_with_extra_keys(self) -> None:
        """Test validate_config with extra keys."""
        config = {"debug": True, "port": 8000, "extra": "value"}
        assert validate_config(config) is True
