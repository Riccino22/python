import nltk
from nltk.corpus import wordnet
from nltk.corpus import words
from deep_translator import GoogleTranslator


nltk.download('words')

nltk.download('wordnet')

def word_exists(word):
    synsets = wordnet.synsets(word)
    word_list = words.words()
    definition = ""
    for synset in synsets:
        definition += f" {synset.definition()}."
        word_list = words.words()
        
    if word.lower() in word_list:
        return True, definition
    else:
        return False, ""


def translate_word(word, source_lang='en', target_lang='es'):
    translator = GoogleTranslator(source=source_lang, target=target_lang)
    translation = translator.translate(word)
    return translation
