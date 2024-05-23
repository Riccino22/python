import smtplib, ssl
import os
host = "smtp.gmail.com"
port = 465
email = "riccardoinojosa@gmail.com"
password = os.environ.get("PASSWORD")
print(password)

context = ssl.create_default_context()

default_content = f"""\
Subject: (About --CATEGORY--) Message from: --EMAIL--

--BODY--
"""

def send(user_email, category, message):
    email_content = default_content
    email_content = email_content.replace("--EMAIL--", user_email)
    email_content = email_content.replace("--CATEGORY--", category)
    email_content = email_content.replace("--BODY--", message)


    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(email, password)
        server.sendmail(email, email, email_content)
    