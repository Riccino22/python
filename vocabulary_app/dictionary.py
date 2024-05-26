import nltk
from nltk.corpus import wordnet
#from googletrans import Translator
from deep_translator import GoogleTranslator
# Descargar WordNet
nltk.download('wordnet')

def word_exists(word):
    synsets = wordnet.synsets(word)
    definition = ""
    for synset in synsets:
        definition += f" {synset.definition()}."
    exist = bool(word)
    return exist, definition




def translate_word(word, source_lang='en', target_lang='es'):
    translator = GoogleTranslator(source=source_lang, target=target_lang)
    translation = translator.translate(word)
    return translation

