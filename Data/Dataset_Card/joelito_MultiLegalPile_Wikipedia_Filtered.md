---
annotations_creators:
- other
language_creators:
- found
language:
- bg 
- cs 
- da 
- de 
- el 
- en
- es 
- et 
- fi 
- fr 
- ga
- hr 
- hu 
- it 
- lt 
- lv 
- mt
- nl 
- pl 
- pt 
- ro 
- sk 
- sl 
- sv
license:
- cc-by-4.0
multilinguality:
- multilingual
paperswithcode_id: null
pretty_name: "MultiLegalPile_Wikipedia_Filtered: A filtered version of the MultiLegalPile dataset, together with wikipedia articles."
size_categories:
- 10M<n<100M
source_datasets:
- original
task_categories:
- fill-mask

---

# Dataset Card for MultiLegalPile_Wikipedia_Filtered: A filtered version of the MultiLegalPile dataset, together with wikipedia articles

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

- **Homepage:**
- **Repository:** 
- **Paper:** 
- **Leaderboard:**
- **Point of Contact:** [Joel Niklaus](mailto:joel.niklaus.2@bfh.ch)

### Dataset Summary

The Multi_Legal_Pile is a large-scale multilingual legal dataset suited for pretraining language models.
It spans over 24 languages and four legal text types. 

### Supported Tasks and Leaderboards

The dataset supports the tasks of fill-mask.

### Languages

The following languages are supported: 
bg, cs, da, de, el, en, es, et, fi, fr, ga, hr, hu, it, lt, lv, mt, nl, pl, pt, ro, sk, sl, sv

## Dataset Structure

It is structured in the following format: {language}_{text_type}_{shard}.jsonl.xz

text_type is one of the following:

- caselaw
- contracts
- legislation
- other
- wikipedia


Use the dataset like this:
```python
from datasets import load_dataset

config = 'en_contracts' # {language}_{text_type}
dataset = load_dataset('joelito/Multi_Legal_Pile', config, split='train', streaming=True)
```

'config' is a combination of language and text_type, e.g. 'en_contracts' or 'de_caselaw'.
To load all the languages or all the text_types, use 'all' instead of the language or text_type (e.g., '
all_legislation').

### Data Instances

The file format is jsonl.xz and there is a `train` and `validation` split available. 
Since some configurations are very small or non-existent, they might not contain a train split or not be present at all.

The complete dataset consists of five large subsets:
- [Native Multi Legal Pile](https://huggingface.co/datasets/joelito/Multi_Legal_Pile)
- [Eurlex Resources](https://huggingface.co/datasets/joelito/eurlex_resources) 
- [MC4 Legal](https://huggingface.co/datasets/joelito/mc4_legal)
- [Pile of Law](https://huggingface.co/datasets/pile-of-law/pile-of-law)
- [EU Wikipedias](https://huggingface.co/datasets/joelito/EU_Wikipedias)

### Data Fields

[More Information Needed]

### Data Splits

[More Information Needed]

## Dataset Creation

This dataset has been created by combining the following datasets:
Native Multi Legal Pile, Eurlex Resources, MC4 Legal, Pile of Law, EU Wikipedias.
It has been filtered to remove short documents (less than 64 whitespace-separated tokens) and 
documents with more than 30% punctuation or numbers (see prepare_legal_data.py for more details).

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

[More Information Needed]

### Citation Information

```
TODO add citation
```

### Contributions

Thanks to [@JoelNiklaus](https://github.com/joelniklaus) for adding this dataset.
