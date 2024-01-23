---
annotations_creators:
- expert-generated
language:
- en
language_creators:
- expert-generated
license:
- cc0-1.0
multilinguality:
- monolingual
pretty_name: Smithsonian Butterflies
size_categories:
- n<1K
source_datasets:
- original
task_categories:
- image-classification
task_ids:
- multi-label-image-classification
---

# Dataset Card for [Smithsonian Butterflies]

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

- **Homepage:** Smithsonian "Education and Outreach" & "NMNH - Entomology Dept." collections [here](https://collections.si.edu/search/results.htm?q=butterfly&view=list&fq=online_media_type%3A%22Images%22&fq=topic%3A%22Insects%22&fq=data_source%3A%22NMNH+-+Entomology+Dept.%22&media.CC0=true&dsort=title&start=0)

### Dataset Summary

High-res images from Smithsonian "Education and Outreach" & "NMNH - Entomology Dept." collections. Crawled

### Supported Tasks and Leaderboards

Includes metadata about the scientific name of butterflies, but there maybe missing values. Might be good for classification.

### Languages

English

## Dataset Structure

### Data Instances

# Example data

```
{'image_url': 'https://ids.si.edu/ids/deliveryService?id=ark:/65665/m3b3132f6666904de396880d9dc811c5cd',
 'image_alt': 'view Aholibah Underwing digital asset number 1',
 'id': 'ark:/65665/m3b3132f6666904de396880d9dc811c5cd',
 'name': 'Aholibah Underwing',
 'scientific_name': 'Catocala aholibah',
 'gender': None,
 'taxonomy': 'Animalia, Arthropoda, Hexapoda, Insecta, Lepidoptera, Noctuidae, Catocalinae',
 'region': None,
 'locality': None,
 'date': None,
 'usnm_no': 'EO400317-DSP',
 'guid': 'http://n2t.net/ark:/65665/39b506292-715f-45a7-8511-b49bb087c7de',
 'edan_url': 'edanmdm:nmnheducation_10866595',
 'source': 'Smithsonian Education and Outreach collections',
 'stage': None,
 'image': <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=2000x1328 at 0x7F57D0504DC0>,
 'image_hash': '27a5fe92f72f8b116d3b7d65bac84958',
 'sim_score': 0.8440760970115662}
​
```

### Data Fields

sim-score indicates clip score for "pretty butterfly". This is to eliminate non-butterfly images(just id card images etc)

### Data Splits

No specific split exists.

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed]

Crawled from "Education and Outreach" & "NMNH - Entomology Dept." collections found online [here](https://collections.si.edu/search/results.htm?q=butterfly&view=list&fq=online_media_type%3A%22Images%22&fq=topic%3A%22Insects%22&fq=data_source%3A%22NMNH+-+Entomology+Dept.%22&media.CC0=true&dsort=title&start=0)

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

Doesn't include all butterfly species ## Additional Information

### Dataset Curators

Smithsonian "Education and Outreach" & "NMNH - Entomology Dept." collections 

### Licensing Information

Only results marked: CC0

### Citation Information

[More Information Needed]

### Contributions

Thanks to [@cceyda](https://github.com/cceyda) for adding this dataset.