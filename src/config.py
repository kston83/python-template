"""Configuration management for the application."""

from dataclasses import dataclass
from typing import Literal


@dataclass(frozen=True)
class Config:
    """Application configuration.

    Attributes:
        debug: Enable debug mode.
        environment: Application environment.
        port: Port number for the application.
        host: Host address for the application.
    """

    debug: bool = False
    environment: Literal["development", "staging", "production"] = "development"
    port: int = 8000
    host: str = "127.0.0.1"

    def is_production(self) -> bool:
        """Check if running in production environment.

        Returns:
            True if environment is production, False otherwise.
        """
        return self.environment == "production"


def load_config() -> Config:
    """Load configuration from environment or defaults.

    Returns:
        Configuration instance with loaded settings.
    """
    # In a real application, you would load from environment variables
    # or configuration files here
    return Config()
