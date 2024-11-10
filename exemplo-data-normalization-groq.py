import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import collections
from wordcloud import WordCloud


text_data = [
    "Patient presents with headache and fever.",
    "Patient has a history of hypertension and diabetes.",
    "Patient is taking medication for hypertension and diabetes.",
    "Patient has a family history of heart disease."
]

#### normalized data
normalized_text_data = []
for text in text_data:
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove special characters and numbers
    text = text.lower()  # Convert to lowercase
    normalized_text_data.append(text)

print(normalized_text_data)
print("\n")

#### stop words
stop_words = set(stopwords.words('english'))

normalized_text_data = []
for text in text_data:
    tokens = word_tokenize(text)
    tokens = [token for token in tokens if token not in stop_words]
    normalized_text_data.append(' '.join(tokens))

print(normalized_text_data)
print("\n")

#### visaulization
#### words & frequency
word_freq = collections.Counter(word for text in normalized_text_data for word in text.split())

plt.bar(word_freq.keys(), word_freq.values())
plt.xlabel('Word')
plt.ylabel('Frequency')
plt.title('Word Frequency')
plt.show()

#### wordcloud
word_freq = collections.Counter(word for text in normalized_text_data for word in text.split())

wordcloud = WordCloud().generate_from_frequencies(word_freq)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
