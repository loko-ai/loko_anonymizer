<html><p><a href="https://loko-ai.com/" target="_blank" rel="noopener"> <img style="vertical-align: middle;" src="https://user-images.githubusercontent.com/30443495/196493267-c328669c-10af-4670-bbfa-e3029e7fb874.png" width="8%" align="left" /> </a></p>
<h1>Loko Anonymizer</h1><br></html>

**Loko Anonymizer** is a Loko extension dealing with masking text based on a NER model.

The "Anonymization Dashboard" allows you to enter free text or insert a pdf url, e.g. https://www.italgiure.giustizia.it/xway/application/nif/clean/hc.dll?verbo=attach&db=snpen&id=./20230203/snpen@s60@a2023@n04901@tS.clean.pdf:
<p align="center">
<img src="https://user-images.githubusercontent.com/30443495/217218465-a9320941-c62d-4041-9f3b-56edef7f0b4c.png" width="80%" />
</p>

When you click on "Mask", it shows both the Masked result and Extracted entities.

Basing on the <a href="https://huggingface.co/bullmount/it_nerIta_trf">it_nerIta_trf</a> model, it first extracts 
entities from text, and then masks them:

<p align="center"><img src="https://user-images.githubusercontent.com/30443495/220401420-83b303fb-d748-48e8-aed2-ba5debdd11af.png" width="80%" /></p>

In the block's configuration, you can set which kind of entities you don't want to anonymize, using **keep** parameter:

<p align="center"><img src="https://user-images.githubusercontent.com/30443495/220404289-e730f47a-496f-472e-ba21-ec60c0aab7b5.png" width="80%" /></p>

Here you can find the list of available categories:
```
'CARDINAL', 'DATE', 'EVENT', 'FAC', 'GPE', 'LANGUAGE', 'LAW', 'LOC', 'MONEY', 'NORP', 'ORDINAL', 'ORG', 'PER', 
'PERCENT', 'PRODUCT', 'QUANTITY', 'TIME', 'WORK_OF_ART'
```

You can set whether to return the list of extracted entities using the **entities** parameter:

<p align="center"><img src="https://user-images.githubusercontent.com/30443495/220405990-6f66313a-4916-4f09-8319-e30318b1b6e4.png" width="80%" /></p>

Each entity is represented by a dictionary:

```
{
    "label": "PER",
    "start": 7,
    "end": 10,
    "text": "Dumitru Aurelian Gabriel"
}
```

*start* and *end* refer to the tokenization of the text given in input to the block.
