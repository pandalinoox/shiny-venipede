from shiny_venipede.utils.logger import _create_logger


def test_logger_reuse_returns_same_logger():
    logger1 = _create_logger("test_logger")
    logger2 = _create_logger("test_logger")

    assert logger1 is logger2
    assert len(logger1.handlers) == 1
