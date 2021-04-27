from nltk.stem import WordNetLemmatizer
import inflect
from Chapter01.pos_tagging import pos_tag_nltk, read_text_file, preprocess_text
import sys
sys.path.append('..')


def is_plural_wn(noun):
    wnl = WordNetLemmatizer()
    lemma = wnl.lemmatize(noun, 'n')
    print(lemma)
    plural = True if noun is not lemma else False
    return plural


def is_singular_wn(noun):
    return not(is_plural_wn(noun))


def is_plural_nltk(noun_info):
    pos = noun_info[1]
    if pos == 'NNS':
        return True
    else:
        return False


def is_singular_nltk(noun_info):
    pos = noun_info[1]
    if pos == 'NN':
        return True
    else:
        return False


def get_plural(singular_noun):
    p = inflect.engine()
    return p.plural(singular_noun)


def get_singular(plural_noun):
    p = inflect.engine()
    plural = p.singular_noun(get_plural(plural_noun))
    if plural:
        return plural
    else:
        return plural_noun


def get_nouns(words_with_pos):
    noun_set = ["NN", "NNS"]
    nouns = [word for word in words_with_pos if word[1] in noun_set]
    return nouns


def plurals_wn(words_with_pos):
    other_nouns = []
    for noun_info in words_with_pos:
        word = noun_info[0]
        plural = is_plural_wn(word)
        if plural:
            singular = get_singular(word)
            other_nouns.append(singular)
        else:
            plural = get_plural(word)
            other_nouns.append(plural)
    return other_nouns


def plurals_nltk(nouns):
    other_nouns = []
    for noun_info in nouns:
        word = noun_info[0]
        pos = noun_info[1]
        if pos == "NNS":
            singular = get_singular(noun_info[0])
            other_nouns.append(singular)
        else:
            plural = get_plural(noun_info[0])
            other_nouns.append(plural)
    return other_nouns


def main():
    sherlock_holmes_text = read_text_file("../Chapter01/sherlock_holmes_1.txt")
    sherlock_holmes_text = preprocess_text(sherlock_holmes_text)
    words_with_pos = pos_tag_nltk(sherlock_holmes_text)
    nouns = get_nouns(words_with_pos)
    print(nouns)
    # other_nouns_wn = plurals_wn(nouns)
    # print(other_nouns_wn)
    # other_nouns_nltk = plurals_nltk(nouns)
    # print(other_nouns_nltk)
    # print(is_plural_wn("men"))
    word_info = pos_tag_nltk("men")
    print(word_info)


if __name__ == "__main__":
    main()
