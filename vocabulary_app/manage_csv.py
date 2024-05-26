import csv

def get_words():
    with open("data/words.csv", "r") as file:
        reader = csv.DictReader(file)
        words = []
        for row in reader:
            words.append(row)
    return words

def insert_word(word, translation, description):
    with open("data/words.csv", "a") as file:
        writer = csv.writer(file, delimiter=";")
        print(translation)
        writer.writerow([word, translation, description])