import nltk

languages = [
    "english", "spanish", "dutch", "finnish", "german", "italian",
    "portuguese", "turkish", "danish", "french", "hungarian",
    "norwegian", "russian", "swedish"
]


def idiom_detect(text:str) -> str:
    tokens = nltk.word_tokenize(text)
    tokens = [
        t.strip().lower()
        for t in tokens
    ]
    language_count = {}
    for language in languages:
        stop_words = set(nltk.corpus.stopwords.words(language))
        language_count[language] = 0
        for word in tokens:
            if word in stop_words:
                language_count[language] += 1
    return max(language_count, key=language_count.get)
