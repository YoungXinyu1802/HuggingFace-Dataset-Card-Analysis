---
dataset_info:
  features:
  - name: image_id
    dtype: int64
  - name: image
    dtype: image
  - name: width
    dtype: int32
  - name: height
    dtype: int32
  - name: objects
    sequence:
    - name: bw_id
      dtype: string
    - name: category_id
      dtype:
        class_label:
          names:
            '0': Photograph
            '1': Illustration
            '2': Map
            '3': Comics/Cartoon
            '4': Editorial Cartoon
            '5': Headline
            '6': Advertisement
    - name: image_id
      dtype: string
    - name: id
      dtype: int64
    - name: area
      dtype: int64
    - name: bbox
      sequence: float32
      length: 4
    - name: iscrowd
      dtype: bool
  splits:
  - name: train
    num_bytes: 2854507
    num_examples: 2846
  - name: validation
    num_bytes: 731782
    num_examples: 712
  download_size: 1200053819
  dataset_size: 3586289
license: cc0-1.0
task_categories:
- object-detection
tags:
- lam
- newspapers
- document-layout
pretty_name: Beyond Words
size_categories:
- 1K<n<10K
---

# Dataset Card for Beyond Words

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

- **Homepage:** https://labs.loc.gov/
- **Repository:** https://github.com/LibraryOfCongress/newspaper-navigator
- **Paper:** https://arxiv.org/abs/2005.01583
- **Leaderboard:**
- **Point of Contact:** LC-Labs@loc.gov

### Dataset Summary

[More Information Needed]

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

[More Information Needed]

## Dataset Structure

### Data Instances

[More Information Needed]

### Data Fields

[More Information Needed]

### Data Splits

[More Information Needed]

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

```bibtex
@inproceedings{10.1145/3340531.3412767,
author = {Lee, Benjamin Charles Germain and Mears, Jaime and Jakeway, Eileen and Ferriter, Meghan and Adams, Chris and Yarasavage, Nathan and Thomas, Deborah and Zwaard, Kate and Weld, Daniel S.},
title = {The Newspaper Navigator Dataset: Extracting Headlines and Visual Content from 16 Million Historic Newspaper Pages in Chronicling America},
year = {2020},
isbn = {9781450368599},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3340531.3412767},
doi = {10.1145/3340531.3412767},
abstract = {Chronicling America is a product of the National Digital Newspaper Program, a partnership between the Library of Congress and the National Endowment for the Humanities to digitize historic American newspapers. Over 16 million pages have been digitized to date, complete with high-resolution images and machine-readable METS/ALTO OCR. Of considerable interest to Chronicling America users is a semantified corpus, complete with extracted visual content and headlines. To accomplish this, we introduce a visual content recognition model trained on bounding box annotations collected as part of the Library of Congress's Beyond Words crowdsourcing initiative and augmented with additional annotations including those of headlines and advertisements. We describe our pipeline that utilizes this deep learning model to extract 7 classes of visual content: headlines, photographs, illustrations, maps, comics, editorial cartoons, and advertisements, complete with textual content such as captions derived from the METS/ALTO OCR, as well as image embeddings. We report the results of running the pipeline on 16.3 million pages from the Chronicling America corpus and describe the resulting Newspaper Navigator dataset, the largest dataset of extracted visual content from historic newspapers ever produced. The Newspaper Navigator dataset, finetuned visual content recognition model, and all source code are placed in the public domain for unrestricted re-use.},
booktitle = {Proceedings of the 29th ACM International Conference on Information &amp; Knowledge Management},
pages = {3055–3062},
numpages = {8},
keywords = {digital humanities, dataset, chronicling america, newspaper navigator, document analysis, information retrieval, digital libraries and archives, public domain, historic newspapers},
location = {Virtual Event, Ireland},
series = {CIKM '20}
}
```

### Contributions

Thanks to [@davanstrien](https://github.com/davanstrien) for adding this dataset.