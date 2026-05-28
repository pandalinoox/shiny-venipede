import logging


def _create_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    Creates and configures a logger with standard console output format.

    Args:
        name (str): Name of the logger.
        level (int,optional): Logging level, defaults to INFO.

    Returns:
        logging.Logger: Configured logger instance with a stream handler and formatted output.
    """

    logger = logging.getLogger(name)
    if logger.handlers:
        return logger
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    console = logging.StreamHandler()
    console.setLevel(level)
    console.setFormatter(formatter)

    logger.addHandler(console)

    logger.propagate = False

    return logger


error_logger = _create_logger("error_logger", logging.ERROR)
