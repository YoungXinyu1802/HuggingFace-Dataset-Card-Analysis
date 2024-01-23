---
annotations_creators:
- expert-generated
- found
language_creators:
- found
- expert-generated
license: []
multilinguality:
- translation
pretty_name: opus
size_categories: []
source_datasets: []
tags:
- parallel-corpus
task_categories:
- translation
task_ids: []
---

# Dataset Card for [opus]

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
**Disclaimer.** Loading of dataset is slow, thus it may not be feasible when loading at scale. I'd suggest to use the other OPUS datasets on Huggingface which loads a specific corpus.

Loads [OPUS](https://opus.nlpl.eu/) as HuggingFace dataset. OPUS is an open parallel corpus covering 700+ languages and 1100+ datasets.

Given a `src` and `tgt` language, this repository can load *all* available parallel corpus. To my knowledge, other OPUS datasets on Huggingface loads a specific corpus


**Requirements**. 

```
pip install pandas

# pip install my fork of `opustools`
git clone https://github.com/larrylawl/OpusTools.git
pip install -e OpusTools/opustools_pkg
```

**Example Usage**.

```
# args follows `opustools`: https://pypi.org/project/opustools/

src="en"
tgt="id"
download_dir="data"  # dir to save downloaded files
corpus="bible-uedin" # corpus name. Leave as `None` to download all available corpus for the src-tgt pair.


dataset = load_dataset("larrylawl/opus", 
                       src=src, 
                       tgt=tgt,
                       download_dir=download_dir,
                       corpus=corpus)
                       )
```

**Disclaimer**.

This repository is still in active development. Do make a PR if there're any issues!

### Dataset Summary

[More Information Needed]

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

Available languages can be viewed on the [OPUS API](https://opus.nlpl.eu/opusapi/?languages=True)

## Dataset Structure

### Data Instances

```
{'src': 'In the beginning God created the heavens and the earth .',
 'tgt': 'Pada mulanya , waktu Allah mulai menciptakan alam semesta'}
```

### Data Fields

```
features = {
            "src": datasets.Value("string"),
            "tgt": datasets.Value("string"),
        }
```

### Data Splits

Merged all data into train split.

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

[More Information Needed]

### Citation Information

[More Information Needed]

### Contributions

Thanks to [@larrylawl](https://larrylawl.github.io/) for adding this dataset.