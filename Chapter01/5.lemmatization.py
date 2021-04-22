from nltk.stem import WordNetLemmatizer
from pos_tagging import pos_tag_nltk, read_text_file

lemmatizer = WordNetLemmatizer()

words = ['duck', 'geese', 'cats', 'books']
lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
print(lemmatized_words)

print(lemmatizer.lemmatize('loved', 'v'))
print(lemmatizer.lemmatize('worse', 'a'))

pos_mapping = {'JJ':'a', 'JJR':'a', 'JJS':'a', 'NN':'n',
               'NNS':'n', 'VBD':'v', 'VBG':'v','VBN':'v',
               'VBP':'v', 'VBZ':'v'}
accepted_pos = {'a', 'v', 'n'}

def lemmatize_long_text(text):
    words = pos_tag_nltk(text)
    words = [(word_tuple[0], pos_mapping[word_tuple[1]] if \
      word_tuple[1] in pos_mapping.keys() else
      word_tuple[1]) for word_tuple in words]

    words = [(lemmatizer.lemmatize(word_tuple[0]) if \
               word_tuple[1] in accepted_pos else \
               word_tuple[0],
             word_tuple[1]) for word_tuple in words]
    return words

sherlock_holmes_text = read_text_file("sherlock_holmes_1.txt")
lem_words = lemmatize_long_text(sherlock_holmes_text)
print(lem_words)