from nltk.tokenize import word_tokenize
import spacy

with open('sherlock_holmes_1.txt','r') as f:
    text = f.read()

text = text.replace('\n', ' ')

words = word_tokenize(text)
print(words)


# spacy word tokenize
nlp = spacy.load('en_core_web_sm')
doc = nlp(text)
words = [word.text for word in doc ]
print(words)

