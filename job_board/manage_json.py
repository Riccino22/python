import json  # Import the JSON module for working with JSON data  

def add_to_json(filename, data):  # Define a function to add data to a JSON file  
    try:  
        with open(filename, "r") as file:  # Open the JSON file in read mode  
            info = json.load(file)  # Load the JSON data into a variable  
    except json.decoder.JSONDecodeError:  # Handle JSON decoding error  
        info = []  # If there's an error, initialize info as an empty list  
    
    info.append(data)  # Append the new data to the list  
    
    for index, item in enumerate(info):  # Iterate through each item in the list  
        item["id"] = index + 1  # Add an "id" field to each item, starting from 1  
    
    with open(filename, "w") as file:  # Open the JSON file in write mode  
        json.dump(info, file, indent=4)  # Write the updated JSON data to the file with indentation  

def get_json(filename):  # Define a function to retrieve data from a JSON file  
    try:  
        with open(filename, "r") as file:  # Open the JSON file in read mode  
            info = json.load(file)  # Load the JSON data into a variable  
    except json.decoder.JSONDecodeError:  # Handle JSON decoding error  
        info = []  # If there's an error, initialize info as an empty list  
    return info  # Return the retrieved JSON data  
