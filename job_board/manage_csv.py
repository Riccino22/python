import csv

def get_tags():
    with open('tags.csv', 'r') as f:
        reader = csv.reader(f)
        tags = []
        for row in reader:
            tags.append(row[0])
    return tags
