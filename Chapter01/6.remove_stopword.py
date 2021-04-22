import csv
import nltk
from nltk.probability import FreqDist

csv_file = 'stopwords.csv'

csv_file = 'stopwords.csv'
with open(csv_file, 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',', quotechar='"')
    stopwords = [row[0] for row in reader]

print(stopwords)

stopwords = nltk.corpus.stopwords.words('english')

with open('sherlock_holmes_1.txt', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('\n', ' ')
words = nltk.tokenize.word_tokenize(text)
words = [word for word in words if word.lower() not in stopwords]
print(words)

with open('sherlock_holmes.txt', 'r', encoding='utf-8') as f:
    text = f.read()
text = text.replace('\n', ' ')

words = nltk.tokenize.word_tokenize(text)
freq_dist = FreqDist(word.lower() for word in words)
words_with_frequencies = [(word, freq_dist[word]) for word in freq_dist.keys()]

sorted_words = sorted(words_with_frequencies, key=lambda tup: tup[1])
stopwords = [tuple[0] for tuple in sorted_words if tuple[1] > 250]
print(stopwords)

length_cutoff = int(0.005 * len(sorted_words))
stopwords = [tuple[0] for tuple in sorted_words[-length_cutoff:]]
print(stopwords)
