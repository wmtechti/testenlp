import nltk
from nltk.tokenize import word_tokenize
from collections import Counter

# Sample medical record text data
text_data = [
    "Patient presents with headache and fever.",
    "Patient has a history of hypertension and diabetes.",
    "Patient is taking medication for hypertension and diabetes.",
    "Patient has a family history of heart disease."
]

# Tokenize the text data into individual words
tokenized_data = [word_tokenize(text) for text in text_data]

# Calculate word frequencies using Counter
word_freq = Counter(word for text in tokenized_data for word in text)

# Print the top 10 most common words
print(word_freq.most_common(10))

# Calculate frequency of specific words or phrases
specific_word_freq = word_freq['headache']  # Frequency of the word "headache"
specific_phrase_freq = word_freq['hypertension and diabetes']  # Frequency of the phrase "hypertension and diabetes"

print(specific_word_freq)
print(specific_phrase_freq)
