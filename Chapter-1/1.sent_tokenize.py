import nltk
import spacy
from nltk.tokenize import sent_tokenize

with open('sherlock_holmes_1.txt', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('\n', ' ')


# Sentence tokenizer using tokenizer data

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
senteces = tokenizer.tokenize(text)
print(senteces)

# Sentence tokenizer using sent_tokenize
sentences = sent_tokenize(text)
print(sentences)

# Spacy tokenizer
nlp = spacy.load("en_core_web_sm")
doc = nlp(text)
sentences = [sentence.text for sentence in doc.sents]
print(sentences)
