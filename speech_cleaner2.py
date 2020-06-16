from stopwords import stop_words

def clean_words(words):
    """Removes invalid or irrelevant words"""
    cleaned_words = []
    for word in words:
        if not word.isalpha():
            continue
        if word.lower() in stop_words:
            continue
        cleaned_words.append(word)
    return cleaned_words



