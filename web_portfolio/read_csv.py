import csv

def read_projects_file():
    with open("projects.csv", "r") as file:
        csvfile = csv.DictReader(file, delimiter=";")
        projects = []
        for row in csvfile:
            projects.append(row)
    return projects 
