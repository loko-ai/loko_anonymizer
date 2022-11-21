import spacy

nlp = spacy.load("it_nerIta_trf")
print(nlp.get_pipe("ner").labels)


class Extractor:
    def __call__(self, text: str):
        return nlp(text)


class Anonymizer:
    def __call__(self, doc, keep=None):
        keep = keep or []
        m = {}
        for e in doc.ents:
            for i in range(e.start, e.end):
                if not e.label_ in keep:
                    m[i] = True
        out = []
        for i, e in enumerate(doc):
            if i in m:
                out.append("******")
            else:
                out.append(e.text)
        return out
