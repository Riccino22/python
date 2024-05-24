import streamlit as st  # Import the Streamlit library for building web applications
import manage_csv as mcsv  # Import custom module for CSV management
import manage_json as mjson  # Import custom module for JSON management

st.set_page_config(layout="wide")  # Set the page layout to wide mode
st.title("Search Offer By Tags")  # Set the title of the Streamlit app

offers = mjson.get_json("offers.json")  # Load offers from a JSON file into a variable
with st.form(key="search"):  # Create a form with a unique key
    col1, col2 = st.columns([4, 1])  # Create two columns with specified width ratios
    
    with col1:  # Define the first column
        tags = st.multiselect("Tags", mcsv.get_tags())  # Create a multi-select field for tags, populated from CSV
    with col2:  # Define the second column
        st.write("")  # Add an empty line for spacing
        st.write("")  # Add another empty line for spacing
        btn = st.form_submit_button("Search")  # Create a submit button for the form
    
    if btn:  # Check if the submit button has been clicked
        for offer in offers:  # Iterate through each offer in the loaded offers
            if all([tag in offer["tags"] for tag in tags]):  # Check if all selected tags are in the offer's tags
                with st.container():  # Create a container to group elements
                    st.subheader(offer["title"])  # Display the offer's title as a subheader
                    st.write(offer["description"])  # Display the offer's description
