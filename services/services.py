import logging
import urllib.parse
from io import BytesIO

import requests
from flask import Flask, request, jsonify
from loko_extensions.business.decorators import extract_value_args
from loko_extensions.model.components import Component, save_extensions, Input, Arg

from business.anonymizer import Extractor, Anonymizer
import fitz

app = Flask("anonymization", static_url_path="/web", static_folder="/frontend/dist")

comp = Component("Anonymizer", inputs=[Input("text", service="anonymize")], icon="RiFileLockLine",
                 args=[Arg(name="keep",
                           description="Don't anonymize these entity types. One of 'CARDINAL', 'DATE', 'EVENT', 'FAC', 'GPE', 'LANGUAGE', 'LAW', 'LOC', 'MONEY', 'NORP', 'ORDINAL', 'ORG', 'PER', 'PERCENT', 'PRODUCT', 'QUANTITY', 'TIME', 'WORK_OF_ART'. Comma separated"),
                       Arg(name="entities", type="boolean", description="Returns also extracted entities")])
# extr_comp = Component("Ents")
# pdf = Component("pdf_reader", inputs=[Input("file", service="pdf/text"), Input("url", service="pdf/url")])

save_extensions([comp])

extractor = Extractor()
anonymizer = Anonymizer()


@app.route("/anonymize", methods=["POST"])
@extract_value_args(request)
def anonymize(value, args):
    doc = extractor(value)
    keep = args.get("keep")
    if keep:
        keep = [x.strip() for x in keep.split(",")]
    out = anonymizer(doc, keep)
    return_entities = args.get("entities")
    if return_entities:
        ents = []
        tokens = [token.text for token in doc]

        for e in doc.ents:
            ents.append(dict(label=e.label_, text=e.text, start=e.start, end=e.end))

        return jsonify(dict(anonymized_text=" ".join(out), entities=ents, tokens=tokens))
    return jsonify(" ".join(out))


if __name__ == "__main__":
    app.run("0.0.0.0", 8080)
