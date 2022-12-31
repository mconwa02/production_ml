import logging
from enum import Enum
from logging import handlers


class LEVELS(Enum):
    debug = logging.DEBUG
    info = logging.INFO
    warning = logging.WARNING
    error = logging.ERROR
    critical = logging.CRITICAL


LOG_FILENAME = "logging_rotating_file.py"


def main_logger():

    logging.basicConfig(level=logging.INFO)

    logger = logging.getLogger(name="production-ml-logs")

    handler = handlers.RotatingFileHandler(
        filename=LOG_FILENAME,
        maxBytes=20,
    )

    logger.addHandler(handler)

    return logger


if __name__ == "__main__":
    main_logger()
