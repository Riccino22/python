import smtplib, ssl  # Import libraries for sending emails securely
import os  # Import the os module for interacting with the operating system
from dotenv import load_dotenv  # Import function to load environment variables from a .env file
import json  # Import the json module for working with JSON data

load_dotenv()  # Load environment variables from .env file

host = "smtp.gmail.com"  # SMTP server host
port = 465  # Port for SMTP SSL connection
email =  os.environ.get("EMAIL")  # Sender's email address
password = os.environ.get("PASSWORD")  # Get password from environment variable

context = ssl.create_default_context()  # Create SSL context for secure connection

default_content = f"""\
Subject: NEW OFFER: --TITLE--

--BODY--

"""  # Default email content template

def get_seekers(tags):
    try:
        with open("seekers.json", "r") as file:  # Open JSON file containing seeker data
            data = json.load(file)  # Load JSON data into variable
    except json.decoder.JSONDecodeError:  # Handle JSON decoding error
        data = []  # If there's an error, initialize data as an empty list
    seekers = []  # Initialize list to store matching seekers
    for seeker in data:  # Iterate through each seeker in the data
        added = False  # Initialize flag to track if seeker has already been added
        for tag in tags:  # Iterate through each tag in the provided tags
            if tag in seeker["tags"] and added == False:  # Check if seeker's tags match any of the provided tags
                seekers.append(seeker)  # Add seeker to the list of matching seekers
                added = True  # Update flag to indicate seeker has been added
    return seekers  # Return list of matching seekers


def send(tags, title, message):
    seekers = get_seekers(tags)  # Get matching seekers for provided tags
    
    email_content = default_content  # Initialize email content with default template
    email_content = email_content.replace("--TITLE--", title)  # Replace placeholder with offer title
    email_content = email_content.replace("--BODY--", message)  # Replace placeholder with offer message

    with smtplib.SMTP_SSL(host, port, context=context) as server:  # Connect to SMTP server
        server.login(email, password)  # Login to sender's email account
        for seeker in seekers:  # Iterate through each matching seeker
            server.sendmail(email, seeker["email"], email_content)  # Send email to seeker
