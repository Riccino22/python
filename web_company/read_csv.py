import csv

def read_members_file():
    with open("members.csv", "r") as file:
        csvfile = csv.DictReader(file, delimiter=",")
        members = []
        for row in csvfile:
            members.append(row)
    return members 
