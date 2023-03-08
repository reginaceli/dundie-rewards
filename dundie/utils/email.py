import re
import smtplib
from email.mime.text import MIMEText
from dundie.settings import SMTP_HOST, SMPT_PORT, SMPT_TIMEOUT
from dundie.utils.logger import get_logger


log = get_logger()

regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"


def check_valid_email(address):
    """Return True if email is valid"""

    if re.fullmatch(regex, address):
        return True
    else:
        return False


def send_email(from_, to, subject, text):
    if not isinstance(to, list):
        to = [to]

    try:
        with smtplib.SMTP(
            host=SMTP_HOST,
            port=SMPT_PORT,
            time=SMPT_TIMEOUT
        ) as server:
            message = MIMEText(text)
            message["Subject"] = subject
            message["From"] = from_
            message["To"] = ",".join(to)
            server.sendmail(from_, to, message.as_string())
    except Exception:
        log.error("Cannot send email to %s", to)
