### Vocabulary App

#### Features:
- **dictionary.py**: Utilizes NLTK's WordNet for word existence checking and definitions. Integrates Google Translator for translations.
- **main.py**: Streamlit interface to input and save new words. Displays success or error messages based on word existence.
- **manage_csv.py**: Manages CSV storage of words, translations, and definitions.

#### Usage:
1. **Interface**: Use Streamlit to input a new word.
2. **Functionality**: Checks if the word exists, translates it, and stores it in a CSV file (`words.csv`).
3. **Management**: View stored words and their details via the CSV file operations.

#### Requirements:
- **Python Libraries**: NLTK, Streamlit, deep_translator
- **Data Storage**: CSV file (`data/words.csv`) for word storage and management.

#### Setup:
1. **Environment**: Install required Python libraries (`nltk`, `streamlit`, `deep_translator`).
2. **Execution**: Run `main.py` to launch the Streamlit app and start managing vocabulary entries.

