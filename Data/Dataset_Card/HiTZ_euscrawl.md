---
annotations_creators:
- no-annotation
language:
- eu
language_creators:
- found
license:
- cc
multilinguality:
- monolingual
pretty_name: EusCrawl
size_categories:
- 10M<n<100M
source_datasets:
- original
tags:
- high-quality
- scraping
task_categories:
- text-generation
- fill-mask
task_ids:
- language-modeling
- masked-language-modeling
dataset_info:
  features:
  - name: id
    dtype: int32
  - name: title
    dtype: string
  - name: text
    dtype: string
  - name: source
    dtype: string
  - name: license
    dtype: string
  - name: url
    dtype: string
  splits:
  - name: train
    num_bytes: 2314407002
    num_examples: 1724544
  download_size: 728281801
  dataset_size: 2314407002
---

# Dataset Card for EusCrawl

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

- **Homepage:** https://ixa.ehu.eus/euscrawl/
- **Repository:** 
- **Paper:** https://arxiv.org/abs/2203.08111
- **Leaderboard:**
- **Point of Contact:** a.soroa@ehu.eus

### Dataset Summary

EusCrawl (http://www.ixa.eus/euscrawl/) is a high-quality corpus for
Basque comprising 12.5 million documents and 423 million tokens,
totalling 2.1 GiB of uncompressed text. EusCrawl was built using
ad-hoc scrapers to extract text from 33 Basque websites with
high-quality content, resulting in cleaner text compared to general
purpose approaches.

### Supported Tasks and Leaderboards

EusCrawl is intended for pretraining models for language modeling or masked language modeling.

### Languages

Basque (eu)

## Dataset Structure

### Data Instances

```json
{
    "id": 6,
    "title": "Herriko enpresa handien eta txikien arteko topaketak egingo dituzte",
    "text": "09:30ean hasiko da bilera eta aurkezpena egingo dute Tubacex, JEZ, Envases, Guardian eta Vidrala enpresek. Eskualdeko lantegi motorrekin beste enpresa txikiak eta ertainak egongo dira. Erakunde publikoaren helburua da euren artean ezagutzea eta elkarlana sustatzea.",
    "source": "aiaraldea",
    "license": "cc-by-sa 3.0",
    "url": "https://aiaraldea.eus/laudio/1494603159768-herriko-enpresa-handien-eta-txikien-arteko-topaketak-egingo-dituzte",
}
```

### Data Fields

- "id": example id
- "title": article title
- "text": article text
- "source": article source
- "license": article license
- "url": article url

### Data Splits

The dataset only has one training split because it is intended for pretraining language models.

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

We do not claim ownership of any document in the corpus. All documents
we collected were published under a Creative Commons license in their
original website, and the specific variant can be found in the
"license" field of each document. Should you consider
that our data contains material that is owned by you and you would not
like to be reproduced here, please contact Aitor Soroa at
a.soroa@ehu.eus.

### Citation Information

If you use our corpus or models for academic research, please cite the paper in question:
```bibtex
@misc{artetxe2022euscrawl,
    title={Does corpus quality really matter for low-resource languages?},
    author={Mikel Artetxe, Itziar Aldabe, Rodrigo Agerri,
    Olatz Perez-de-Viñaspre, Aitor Soroa},
    year={2022},
    eprint={2203.08111},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```

### Contributions

Thanks to [@juletx](https://github.com/juletx) for adding this dataset.