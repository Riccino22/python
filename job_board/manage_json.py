import json  # Import the json module for JSON operations

def add_seeker(name, email, phone, tags):  # Define a function named add_seeker with parameters name, email, phone, and tags
    with open("seekers.json", "r") as file:  # Open the file "seekers.json" in read mode
        seekers = json.load(file)  # Load the JSON data from the file into the seekers variable
        print(seekers)  # Print the loaded data
    
    seekers.append({  # Append a dictionary to the seekers list
        "name": name,  # Key "name" with value name
        "email": email,  # Key "email" with value email
        "phone": phone,  # Key "phone" with value phone
        "tags": tags  # Key "tags" with value tags
    })
    
    seeker_id = 0  # Initialize the seeker_id variable to 0
    for seeker in seekers:  # Iterate through each seeker in the seekers list
        seeker_id += 1  # Increment the seeker_id by 1
        seeker["id"] = seeker_id  # Add a key "id" with value seeker_id to each seeker dictionary
        
    with open("seekers.json", "w") as file:  # Open the file "seekers.json" in write mode
        json.dump(seekers, file, indent=4)  # Write the seekers list to the file in JSON format with indentation
