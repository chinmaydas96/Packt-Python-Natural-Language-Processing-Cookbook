import nltk
import spacy


with open('sherlock_holmes_1.txt', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('\n', ' ')

nlp = spacy.load('en_core_web_sm')
doc = nlp(text)

words = [token.text for token in doc]
pos  = [token.pos_ for token in doc]

word_pos_tuple = list(zip(words, pos))
print(word_pos_tuple)

words = nltk.tokenize.word_tokenize(text)
word_with_pos = nltk.pos_tag(words)
print(word_with_pos)
