from loguru import logger


def logger_config() -> None:
    logger.remove()

    logger.add(
        sink="logging.log",
        format="<level>{time:YYYY-MM-DD HH:mm:ss.SSS}  {level: <8} {message}</level>",
        level="DEBUG",
        backtrace=True,
        diagnose=True,
    )
