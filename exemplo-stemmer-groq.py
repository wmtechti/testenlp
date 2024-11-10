import nltk
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

text_data = [
    "Patient presents with headache and fever.",
    "Patient has a history of hypertension and diabetes",
    "Patient is taking medication for hypertension and diabetes.",
    "Patient has a family history of heart disease."
]

stemmed_text_data = []
for text in text_data:
    tokens = nltk.word_tokenize(text)
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    stemmed_text_data.append(' '.join(stemmed_tokens))

print(stemmed_text_data)

