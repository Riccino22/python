import csv  # Import the CSV module for reading CSV files

def get_tags():
    with open('tags.csv', 'r') as f:  # Open the CSV file in read mode
        reader = csv.reader(f)  # Create a CSV reader object
        tags = []  # Initialize a list to store tags
        for row in reader:  # Iterate through each row in the CSV
            tags.append(row[0])  # Append the first element of each row to the tags list
    return tags  # Return the list of tags

print(get_tags())  # Debugging: Print the list of tags retrieved from the CSV
