from loguru import logger

from your_pkg.utils.logger_config import logger_config


def main() -> None:
    """Substitute this with your main function."""
    logger.info("Hello, world!")


if __name__ == "__main__":
    logger_config()
    main()
