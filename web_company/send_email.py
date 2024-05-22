import smtplib, ssl

host = "smtp.gmail.com"
port = 465
email = "riccardoinojosa@gmail.com"
password = "tehzyrklurhtbfue"

context = ssl.create_default_context()

default_content = f"""\
Subject: sbj

bd
"""

def send(user_email, message):
    email_content = default_content
    email_content = default_content.replace("sbj", "Msg from: " + user_email)
    email_content = email_content.replace("bd", message)


    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(email, password)
        server.sendmail(email, email, email_content)
    