import re


def word_frequencies(text: str) -> dict:
    cleaned_text = re.sub(r"[^\w\s]", "", text).lower()
    freq = {}
    for word in cleaned_text.split():
        freq[word] = freq.get(word, 0) + 1
    return freq
