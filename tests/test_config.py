"""Tests for configuration management."""

from src.config import Config, load_config


class TestConfig:
    """Tests for Config dataclass."""

    def test_config_default_values(self) -> None:
        """Test Config with default values."""
        config = Config()
        assert config.debug is False
        assert config.environment == "development"
        assert config.port == 8000
        assert config.host == "127.0.0.1"

    def test_config_custom_values(self) -> None:
        """Test Config with custom values."""
        config = Config(
            debug=True,
            environment="production",
            port=9000,
            host="0.0.0.0",
        )
        assert config.debug is True
        assert config.environment == "production"
        assert config.port == 9000
        assert config.host == "0.0.0.0"

    def test_config_is_production(self) -> None:
        """Test is_production method."""
        dev_config = Config(environment="development")
        prod_config = Config(environment="production")
        
        assert dev_config.is_production() is False
        assert prod_config.is_production() is True

    def test_config_is_immutable(self) -> None:
        """Test that Config is immutable (frozen)."""
        config = Config()
        
        with pytest.raises(AttributeError):
            config.debug = True  # type: ignore


class TestLoadConfig:
    """Tests for load_config function."""

    def test_load_config_returns_config_instance(self) -> None:
        """Test that load_config returns a Config instance."""
        config = load_config()
        assert isinstance(config, Config)

    def test_load_config_has_defaults(self) -> None:
        """Test that load_config returns config with default values."""
        config = load_config()
        assert config.debug is False
        assert config.environment == "development"
