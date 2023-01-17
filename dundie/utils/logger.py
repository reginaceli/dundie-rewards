import logging
from logging import handlers
import os


LOG_LEVEL = os.getenv("LOG_LEVEL", "WARNING").upper()

# root logger
logger = logging.getLogger('dundie')

fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s '
    'l:%(lineno)d f:%(filename)s: %(message)s '
)


def get_logger(filelog="dundie.log"):
    """Returns a configured logger"""

    # file handler
    fh = handlers.RotatingFileHandler(
        filelog,
        maxBytes=10**6,
        backupCount=10
    )
    fh.setLevel(LOG_LEVEL)
    fh.setFormatter(fmt)

    # add ch to logger
    logger.addHandler(fh)

    return logger
