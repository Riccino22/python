import smtplib, ssl

host = "smtp.gmail.com"
port = 465
email = "riccardoinojosa@gmail.com"
password = "tehzyrklurhtbfue"

context = ssl.create_default_context()

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(email, password)
    server.sendmail(email, email, "Hi bro")
    