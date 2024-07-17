import smtplib
from email.mime.text import MIMEText
from core.config import settings

def send_email(subject, recipient, body):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = settings.EMAIL_FROM
    msg["To"] = recipient

    try:
        with smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT) as server:
            server.starttls()
            server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
            server.sendmail(settings.EMAIL_FROM, recipient, msg.as_string())
        print("Email Sent with success")
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False
