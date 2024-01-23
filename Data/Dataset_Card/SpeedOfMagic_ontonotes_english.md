---
annotations_creators:
- found
language_creators:
- found
language:
- en
license:
- unknown
multilinguality:
- monolingual
pretty_name: ontonotes_english
size_categories:
- 10K<n<100K
source_datasets:
- extended|other
task_categories:
- token-classification
task_ids:
- named-entity-recognition
---

# Dataset Card for ontonotes_english

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Homepage:** [CoNLL-2012 Shared Task](https://conll.cemantix.org/2012/data.html), [Author's page](https://cemantix.org/data/ontonotes.html)
- **Repository:**
- **Paper:** [Towards Robust Linguistic Analysis using OntoNotes](https://aclanthology.org/W13-3516/)
- **Leaderboard:** [Papers With Code](https://paperswithcode.com/sota/named-entity-recognition-ner-on-ontonotes-v5)
- **Point of Contact:**

### Dataset Summary

This is preprocessed version of what I assume is OntoNotes v5.0.

Instead of having sentences stored in files, files are unpacked and sentences are the rows now. Also, fields were renamed in order to match [conll2003](https://huggingface.co/datasets/conll2003).

The source of data is from private repository, which in turn got data from another public repository, location of which is unknown :)

Since data from all repositories had no license (creator of the private repository told me so), there should be no licensing issues. But bear in mind, I don't give any guarantees that this is real OntoNotes, and may differ as a result.

### Supported Tasks and Leaderboards

- [Named Entity Recognition on Ontonotes v5 (English)](https://paperswithcode.com/sota/named-entity-recognition-ner-on-ontonotes-v5)
- [Coreference Resolution on OntoNotes](https://paperswithcode.com/sota/coreference-resolution-on-ontonotes)
- [Semantic Role Labeling on OntoNotes](https://paperswithcode.com/sota/semantic-role-labeling-on-ontonotes)

### Languages

English

## Dataset Structure

### Data Instances

```
{
    'tokens': ['Well', ',', 'the', 'Hundred', 'Regiments', 'Offensive', 'was', 'divided', 'into', 'three', 'phases', '.'],
    'ner_tags': [0, 0, 29, 30, 30, 30, 0, 0, 0, 27, 0, 0]
}
```

### Data Fields

- **`tokens`** (*`List[str]`*) : **`words`** in original dataset
- **`ner_tags`** (*`List[ClassLabel]`*) : **`named_entities`** in original dataset. The BIO tags for named entities in the sentence. 
  - tag set : `datasets.ClassLabel(num_classes=37, names=["O", "B-PERSON", "I-PERSON", "B-NORP", "I-NORP", "B-FAC", "I-FAC", "B-ORG", "I-ORG", "B-GPE", "I-GPE", "B-LOC", "I-LOC", "B-PRODUCT", "I-PRODUCT", "B-DATE", "I-DATE", "B-TIME", "I-TIME", "B-PERCENT", "I-PERCENT", "B-MONEY", "I-MONEY", "B-QUANTITY", "I-QUANTITY", "B-ORDINAL", "I-ORDINAL", "B-CARDINAL", "I-CARDINAL", "B-EVENT", "I-EVENT", "B-WORK_OF_ART", "I-WORK_OF_ART", "B-LAW", "I-LAW", "B-LANGUAGE", "I-LANGUAGE",])`

### Data Splits

_train_, _validation_, and _test_

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

[More Information Needed]

### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

[More Information Needed]

### Personal and Sensitive Information

[More Information Needed]

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

No license

### Citation Information

```
@inproceedings{pradhan-etal-2013-towards,
    title = "Towards Robust Linguistic Analysis using {O}nto{N}otes",
    author = {Pradhan, Sameer  and
      Moschitti, Alessandro  and
      Xue, Nianwen  and
      Ng, Hwee Tou  and
      Bj{\"o}rkelund, Anders  and
      Uryupina, Olga  and
      Zhang, Yuchen  and
      Zhong, Zhi},
    booktitle = "Proceedings of the Seventeenth Conference on Computational Natural Language Learning",
    month = aug,
    year = "2013",
    address = "Sofia, Bulgaria",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/W13-3516",
    pages = "143--152",
}
```

### Contributions

Thanks to the author of private repository, that uploaded this dataset.