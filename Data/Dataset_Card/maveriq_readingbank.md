---
language:
- en
size_categories:
- 100K<n<1M
---

# Dataset Card for ReadingBank

## Dataset Description

- **Homepage:** https://github.com/doc-analysis/ReadingBank
- **Repository:** https://github.com/doc-analysis/ReadingBank
- **Paper:** https://arxiv.org/pdf/2108.11591.pdf
- **Leaderboard:** 
- **Point of Contact:** Raise github issue on mentioned repository for dataset related matters and contact @maveriq for huggingface dataset port.

### Dataset Summary

ReadingBank is a benchmark dataset for reading order detection built with weak supervision from WORD documents, which contains 500K document images with a wide range of document types as well as the corresponding reading order information.

### Supported Tasks and Leaderboards

Reading Order of documents

### Languages

English

## Dataset Structure

### Data Instances

[More Information Needed]

### Data Fields

- src : text
- tgt : text
- bleu : float
- tgt_index : list of ints
- original_filename : str
- filename : str
- page_idx : int
- src_layout : Bounding boxes for src (list of list of ints)
- tgt_layout : Bounding boxes for tgt (list of list of ints)

### Data Splits

train : 400,000
dev : 50,000
test : 50,000

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

[More Information Needed]