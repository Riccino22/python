import json

def get_words():
    with open("data/words.json", "r") as file:
        words = json.load(file)
    return words


def insert_word(word, translation, description):
    with open("data/words.json", "r") as file:
        words = json.load(file)
    words.append({
        "word": word.capitalize(),
        "translation": translation.capitalize(),
        "definitions": description
    })
    with open("data/words.json", "w") as file:
        json.dump(words, file, indent=4)
        

def delete_word(index):
    with open("data/words.json", "r") as file:
        words = json.load(file)
    words.pop(index)
    
    with open("data/words.json", "w") as file:
        json.dump(words, file, indent=4)