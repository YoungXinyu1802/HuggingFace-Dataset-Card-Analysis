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
pretty_name: "wikipedia pages chunked for fill-mask"
size_categories:
- 10M<n<100M
source_datasets:
- original
task_categories:
- fill-mask

---

# preprocessed version of rcds/wikipedia-persons-masked

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
Each row contains a part of a wiki page, specified by the size parameter which limits the maximum size in number of tokens per text chunk.
for each chunk the expected name for each mask is given.

### Supported Tasks and Leaderboards

The dataset supports the tasks of fill-mask, but can also be used for other tasks such as question answering,
e.g. "Who is <mask>?"

### Languages

*english only*

## Dataset Structure

In /data find different versions of the full dataset, with original and paraphrased versions as well as chunked to 4096 and 512 tokens.

Use the dataset like this:
```python
from datasets import load_dataset

dataset = load_dataset('rcds/wikipedia-persons-masked', split='train', type='original', size='512')
```

### Data Fields

Columns are:
- texts: the text chunks
- masks: the names for each of the masks in the chunks

### Data Splits

There are no splits, only a default train.

## Dataset Creation

Created by using the tokenizer from allenai/longformer-base-4096 for the 4096 token per chunk version,
and the xml-roberta-large tokenizer for the 512 token version. Chunks are split to fit those token sizes,
with the splits ensuring no words are split in half.
Possible improvements: Last chunk of a page might be much shorter, could join part of the previous one to have more tokens
in the last chunk.

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
