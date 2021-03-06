import sys
sys.path.append('..')

import nltk
import time
import spacy
from Chapter01.dividing_into_sentences import divide_into_sentences_nltk, read_text_file, preprocess_text
from Chapter01.tokenization import tokenize_nltk

nlp = spacy.load('en_core_web_sm')


def pos_tag_tag_spacy(text):
    doc = nlp(text)
    words = [token.text for token in doc]
    pos = [token.pos_ for token in doc]
    return list(zip(words, pos))


def pos_tag_nltk(text):
    words = tokenize_nltk(text)
    words_with_pos = nltk.pos_tag(words)
    return words_with_pos


def pos_tag(text):
    text = preprocess_text(text)
    words_with_pos = pos_tag_nltk(text)
    return words_with_pos


def main():
    sherlock_holmes_text = read_text_file('sherlock_holmes_1.txt')
    sherlock_holmes_text = preprocess_text(sherlock_holmes_text)
    words_with_pos = pos_tag(sherlock_holmes_text)
    print(words_with_pos)


if __name__ == '__main__':
    start = time.time()
    main()
    print("%s s" % (time.time() - start))
