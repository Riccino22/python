import csv

def get_tags():
    with open('tags.csv', 'r') as f:
        reader = csv.reader(f)
        tags = []
        for row in reader:
            tags.append(row[0])
    return tags

print(get_tags())

"""
def add_seeker(name, email, phone):
    with open("job_seekers.csv", "a", newline='') as file:
        fieldnames = ["name","email","phone"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        # Si el archivo está vacío, escribe los nombres de las columnas
        if file.tell() == 0:
            writer.writeheader()
        
        # Escribe el nuevo buscador en el archivo
        writer.writerow({
            "name": name,
            "email": email,
            "phone": phone
        })
"""