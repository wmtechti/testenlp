import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re
import pandas as pd

# Download necessary NLTK resources
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

# df = pd.read_csv('sample_teste_nlp.csv')
# df = pd.read_csv('doencas-teste-gpt-lematizado.csv')
df = pd.read_csv('sample_teste_nlp_gpt_convetido_para_texto.csv') 

# Initialize stopwords and lemmatizer
stop_words = set(stopwords.words('portuguese'))
lemmatizer = WordNetLemmatizer()

# Function to preprocess text: remove stopwords and apply lemmatization
def preprocess_text(text):
    # Lowercase text, remove non-alphabet characters, and split into words
    words = re.sub(r'[^a-zA-Záéíóúâêîôûãõç\s]', '', text.lower()).split()

    # Remove stopwords and lemmatize each word
    words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
    return ' '.join(words)

# Apply preprocessing to the processed_text column
df['processed_text_gpt_lematizado'] = df['processed_text'].astype(str).apply(preprocess_text)

# Display the first few rows of the modified data
df[['processed_text', 'processed_text_gpt_lematizado']].head()

print("lematizado:")
print(df['processed_text'].head(10), df['processed_text_gpt_lematizado'].head(10))
print({len(df)})

# Dropar a coluna 'nome_da_coluna' 
df = df.drop(columns=['text'])

df.to_csv('sample_teste_nlp_got_lematizado.csv', index=False)
print(df['processed_text_gpt_lematizado'].head(1)) 