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
pretty_name: "EUWikipedias: A dataset of Wikipedias in the EU languages"
size_categories:
- 10M<n<100M
source_datasets:
- original
task_categories:
- fill-mask

---

# Dataset Card for EUWikipedias: A dataset of Wikipedias in the EU languages

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

Wikipedia dataset containing cleaned articles of all languages.
The datasets are built from the Wikipedia dump
(https://dumps.wikimedia.org/) with one split per language. Each example
contains the content of one full Wikipedia article with cleaning to strip
markdown and unwanted sections (references, etc.).

### Supported Tasks and Leaderboards

The dataset supports the tasks of fill-mask.

### Languages

The following languages are supported: 
bg, cs, da, de, el, en, es, et, fi, fr, ga, hr, hu, it, lt, lv, mt, nl, pl, pt, ro, sk, sl, sv

## Dataset Structure

It is structured in the following format: {date}/{language}_{shard}.jsonl.xz
At the moment only the date '20221120' is supported.

Use the dataset like this:
```python
from datasets import load_dataset

dataset = load_dataset('joelito/EU_Wikipedias', date="20221120", language="de", split='train', streaming=True)
```


### Data Instances

The file format is jsonl.xz and there is one split available (`train`). 

### Data Fields

[More Information Needed]

### Data Splits

[More Information Needed]

## Dataset Creation

This dataset has been created by downloading the wikipedias using [olm/wikipedia](https://huggingface.co/datasets/olm/wikipedia) for the 24 EU languages.
For more information about the creation of the dataset please refer to prepare_wikipedias.py

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
