import spacy
import neuralcoref

nlp = spacy.load('en_core_web_sm')
# neuralcoref.add_to_pipeline(nlp)
neuralcoref.add_to_pipe(nlp, conv_dict={'Deepika': ['woman']})


def main():
    text = "Deepika has a dog. She loves him. The movie star has always been fond of animals."
    print(text)
    doc = nlp(text)
    print(doc._.coref_resolved)


if __name__ == '__main__':
    main()
