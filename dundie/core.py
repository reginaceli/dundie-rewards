"""Core modules"""

from dundie.utils.logger import get_logger

log = get_logger()


def load(filepath):
    """Reads data from filepath to the database"""
    try:
        with open(filepath) as file_:
            return file_.readlines()
    except FileNotFoundError as e:
        log.error(str(e))
        raise e
