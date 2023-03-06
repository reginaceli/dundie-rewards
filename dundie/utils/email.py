import re


regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"


def check_valid_email(address):
    """Return True if email is valid"""

    if re.fullmatch(regex, address):
        return True
    else:
        return False
