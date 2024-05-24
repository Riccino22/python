import streamlit as st  # Import the Streamlit library for building web applications
import manage_json as mjson  # Import custom module for JSON management
import manage_csv as mcsv  # Import custom module for CSV management

st.title("Find Job")  # Set the title of the Streamlit app
with st.form(key="email_forms"):  # Create a form with a unique key
    name = st.text_input("Full name")  # Create a text input field for the user's full name
    email = st.text_input("Email")  # Create a text input field for the user's email
    phone = st.text_input("Phone")  # Create a text input field for the user's phone number
    tags = st.multiselect("Tags", mcsv.get_tags())  # Create a multi-select field for tags, populated from CSV
    btn = st.form_submit_button()  # Create a submit button for the form
    if btn:  # Check if the submit button has been clicked
        mjson.add_to_json("seekers.json", {  # Add the seeker details to a JSON file
            "name": name,  # Include the name in the JSON
            "email": email,  # Include the email in the JSON
            "phone": phone,  # Include the phone number in the JSON
            "tags": tags  # Include the selected tags in the JSON
        })
