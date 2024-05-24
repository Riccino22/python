import streamlit as st  # Import the Streamlit library for building web applications
import manage_csv as mcsv  # Import custom module for CSV management
import manage_json as mjson  # Import custom module for JSON management
import send_email  # Import custom module for sending emails

st.title("Publish New Offer")  # Set the title of the Streamlit app
with st.form(key="offer_form"):  # Create a form with a unique key
    title = st.text_input("Title")  # Create a text input field for the offer title
    email = st.text_input("Your email")  # Create a text input field for the user's email
    tags = st.multiselect("Tags", mcsv.get_tags())  # Create a multi-select field for tags, populated from CSV
    description = st.text_area("Description")  # Create a text area for the offer description
    btn = st.form_submit_button()  # Create a submit button for the form
    
    if btn:  # Check if the submit button has been clicked
        mjson.add_to_json("offers.json", {  # Add the offer details to a JSON file
            "title": title,  # Include the title in the JSON
            "tags": tags,  # Include the selected tags in the JSON
            "description": description  # Include the description in the JSON
        })        
        send_email.send(tags, title, description)  # Send an email with the offer details
        st.success("Offer published successfully")  # Display a success message
