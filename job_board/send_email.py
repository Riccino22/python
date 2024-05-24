import smtplib, ssl
import os
from dotenv import load_dotenv
import json

load_dotenv()

host = "smtp.gmail.com"
port = 465
email = "riccardoinojosa@gmail.com"
password = os.environ.get("PASSWORD")
print(password)

context = ssl.create_default_context()

default_content = f"""\
Subject: New offer of --tags--

--BODY--
"""

def get_seekers(tags):
    try:
        with open("seekers.json", "r") as file:  
            data = json.load(file)
    except json.decoder.JSONDecodeError:
        data = []
    seekers = []
    for seeker in data:
        added = False
        for tag in tags:
            if tag in seeker["tags"] and added == False:
                seekers.append(seeker)
                added = True
                
    return seekers
    
print(get_seekers("Art"))
    
        

def send(tags, message):
    seekers = get_seekers(tags)
    
    email_content = default_content
    email_content = email_content.replace("--tags--", tags[0])
    email_content = email_content.replace("--BODY--", message)

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(email, password)
        for seeker in seekers:
            server.sendmail(email, seeker["email"], email_content)
    