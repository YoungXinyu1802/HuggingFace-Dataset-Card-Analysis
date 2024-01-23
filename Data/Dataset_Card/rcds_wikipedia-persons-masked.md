---
annotations_creators:
- other
language_creators:
- found
language:
- en
license:
- cc-by-4.0
multilinguality:
- multilingual
paperswithcode_id: null
pretty_name: "wikipedia persons masked: A filtered version of the wikipedia dataset, with only pages of people."
size_categories:
- 10M<n<100M
source_datasets:
- original
task_categories:
- fill-mask

---

# wikipedia persons masked: A filtered version of the wikipedia dataset, with only pages of people

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
    - [Dataset Summary](#dataset-summary)
    - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
    - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
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
- **Point of Contact:**

### Dataset Summary

Contains ~70k pages from wikipedia, each describing a person. For each page, the person described in the text
is masked with a <mask> token. The ground truth for every mask is provided.

### Supported Tasks and Leaderboards

The dataset supports the tasks of fill-mask, but can also be used for other tasks such as question answering,
e.g. "Who is <mask>?"

### Languages

*english only*

## Dataset Structure

There is one large dataset file (dataset.jsonl.xz), containing all data.

Use the dataset like this:
```python
from datasets import load_dataset

dataset = load_dataset('rcds/wikipedia-persons-masked')
```

### Data Fields

Columns are:
- id: the id in the original dataset
- url: the link to the wikipedia page
- title: the title of the wikipedia page
- text: the original wikipedia text
- sentences: text split to sentences
- paraphrased_sentences: text split to sentences, with each sentence paraphrased (e.g. mutated a bit)
- masked_text_original: original text with entity masked in every occurence (
- masked_entities_original: array of entities masked in masked_text_original
- masked_text_paraphrased: paraphrased text with entity masked in every occurence
- masked_entities_paraphrased: array of entities msked in masked_text_paraphrased

### Data Splits

There are no splits.

## Dataset Creation

This dataset was created by using the wikipedia dataset from huggingface and processing it from there.
People were queried via wikidata. The texts were split with nltk punkt, paraphrased with tuner007's pegasus.
The entity recognition was performed with bert-base-NER by dslim and recognized entities replaced with a mask token. 

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

Thanks to [@skatinger](https://github.com/skatinger) for adding this dataset.