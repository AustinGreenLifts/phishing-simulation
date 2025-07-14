import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(subject, sender, recipients, body, from_email):
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)

    html_part = MIMEText(body, 'html')
    msg.attach(html_part)

    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login('{Insert Email}', '{App Code}')
        server.sendmail(sender, ', '.join(recipients), msg.as_string())
