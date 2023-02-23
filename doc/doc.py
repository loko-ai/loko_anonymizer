
anonymizer_doc = '''### Description
**Anonymizer** component  masks text basing on the extracted entities by the **it_nerIta_trf model**.

### Configuration

- **keep** is used to set which kind of entities you don't want to anonymize.

Here you can find the list of available categories:
```
'CARDINAL', 'DATE', 'EVENT', 'FAC', 'GPE', 'LANGUAGE', 'LAW', 'LOC', 'MONEY', 'NORP', 'ORDINAL', 'ORG', 'PER', 
'PERCENT', 'PRODUCT', 'QUANTITY', 'TIME', 'WORK_OF_ART'
``` 

- **entities** allows to visualize the extracted entities.

### Input
The component accepts text in input.

### Output
The output is the masked text if parameter **entities** is set to False. Otherwise, it returns a dictionary containing 
also the extracted entities associated to the text tokenization:

```
{
  "anonymized_text": "Mi chiamo ****** e vivo a ****** .",
  "entities": [
    {
      "end": 3,
      "label": "PER",
      "start": 2,
      "text": "Mario"
    },
    {
      "end": 7,
      "label": "GPE",
      "start": 6,
      "text": "Roma"
    }
  ],
  "tokens": [
    "Mi",
    "chiamo",
    "Mario",
    "e",
    "vivo",
    "a",
    "Roma",
    "."
  ]
}
```
'''