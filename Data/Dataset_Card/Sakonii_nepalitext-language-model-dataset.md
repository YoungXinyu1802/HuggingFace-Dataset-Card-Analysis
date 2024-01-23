---
annotations_creators:
- no-annotation
language_creators:
- found
- other
language:
- ne
license:
- cc0-1.0
multilinguality:
- monolingual
source_datasets:
- extended|oscar
- extended|cc100
task_categories:
- text-generation
task_ids:
- language-modeling
pretty_name: nepalitext-language-model-dataset
---

# Dataset Card for "nepalitext-language-model-dataset"

### Dataset Summary

"NepaliText" language modeling dataset is a collection of over 13 million Nepali text sequences (phrases/sentences/paragraphs) extracted by combining the datasets: [OSCAR](https://huggingface.co/datasets/oscar) , [cc100](https://huggingface.co/datasets/cc100) and a set of scraped Nepali articles on Wikipedia. 

### Supported Tasks and Leaderboards

This dataset is intended to pre-train language models and word representations on Nepali Language.

### Languages

The data is focused on Nepali language, but may have instances of other languages as well.

## Dataset Structure

### Data Instances

An example:
```
{'text': 'घरेलु मैदानमा भएको च्याम्पियन्स लिगको दोस्रो लेगमा एथ्लेटिको मड्रिडले आर्सनललाई एक शून्यले हराउँदै समग्रमा दुई एकको अग्रताका साथ फाइनलमा प्रवेश गरेको हो ।\n'}
```

### Data Fields

The data fields are:
- `text`: a `string` feature.

### Data Splits

train|test|
----:|---:|
13141222|268189|


## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

[More Information Needed]

### Annotations

The dataset does not contain any additional annotations.

#### Annotation process

[More Information Needed]

#### Who are the annotators?

[More Information Needed]

### Personal and Sensitive Information

Being extracted and scraped from variety of internet sources, Personal and sensitive information might be present. This must be considered before training deep learning models, specially in the case of text-generation models.

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

[More Information Needed]

### Licensing Information

[More Information Needed]

### Citation Information

[More Information Needed]

### Contributions

Thanks to [@Sakonii](https://github.com/Sakonii) for adding this dataset.