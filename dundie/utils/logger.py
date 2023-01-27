import logging
import os
from logging import handlers

LOG_LEVEL = os.getenv("LOG_LEVEL", "WARNING").upper()

# root logger
logger = logging.getLogger("dundie")

formatter = logging.Formatter(
    "%(asctime)s %(name)s %(levelname)s "
    "l:%(lineno)d f:%(filename)s: %(message)s "
)


def get_logger(filelog="dundie.log"):
    """Returns a configured logger"""

    # file handler
    fh = handlers.RotatingFileHandler(
        filelog,
        maxBytes=10**6,
        backupCount=10)
    fh.setLevel(LOG_LEVEL)
    fh.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(fh)

    return logger
