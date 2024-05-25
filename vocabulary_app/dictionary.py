import nltk
from nltk.corpus import wordnet

# Descargar WordNet
nltk.download('wordnet')

def word_exists(word):
    return bool(wordnet.synsets(word))

