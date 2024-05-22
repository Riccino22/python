import smtplib, ssl

host = "smtp.gmail.com"
port = 465
email = "email@gmail.com"
password = "password"

context = ssl.create_default_context()

default_content = f"""\
Subject: (About ctg) Message from: sbj

bd
"""

def send(user_email, category, message):
    email_content = default_content
    email_content = default_content.replace("sbj", user_email)
    email_content = default_content.replace("ctg", category)
    email_content = email_content.replace("bd", message)


    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(email, password)
        server.sendmail(email, email, email_content)
    