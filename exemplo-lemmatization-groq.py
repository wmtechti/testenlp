import nltk
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

text_data = [
    "Patient presents with headache and fever.",
    "Patient has a history of hypertension and diabetes",
    "Patient is taking medication for hypertension and diabetes.",
    "Patient has a family history of heart disease."
]

lemmatized_text_data = []
for text in text_data:
    tokens = nltk.word_tokenize(text)
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    lemmatized_text_data.append(' '.join(lemmatized_tokens))

print(lemmatized_text_data)



