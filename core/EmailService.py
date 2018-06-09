# Import smtplib for the actual sending function
from django.conf import settings
import smtplib
# Import the email modules we'll need
from email.message import EmailMessage
from email.mime.text import MIMEText
from jinja2 import Environment        # Jinja2 templating

SMTP_URL = settings.SMTP_URL
SMTP_PORT = settings.SMTP_PORT
EMAIL_ADMIN_USER = settings.EMAIL_ADMIN_USER
EMAIL_ADMIN_PASS = settings.EMAIL_ADMIN_PASS
PASSWORD_RESET_UI_URL = settings.PASSWORD_RESET_UI_URL

TEMPLATE = open("core/reset_password_email_template.html").read()
SUBJECT = "Password Reset"

def send_email(to, content):
    msg = EmailMessage()

    msg = MIMEText(
        Environment().from_string(TEMPLATE).render(
            url= PASSWORD_RESET_UI_URL + content
        ), "html"
    )

    msg['Subject'] = SUBJECT
    msg['From'] = EMAIL_ADMIN_USER
    msg['To'] = to

    s = smtplib.SMTP(SMTP_URL, SMTP_PORT)
    s.ehlo()
    s.starttls()
    s.login(EMAIL_ADMIN_USER, EMAIL_ADMIN_PASS)
    s.send_message(msg)
    s.quit()