---
annotations_creators:
- machine-generated
language_creators:
- machine-generated
language:
- as
- bn
- gu
- hi
- kn
- ml
- mr
- or
- pa
- ta
- te
license:
- cc0-1.0
multilinguality:
- multilingual
pretty_name: naamapadam
size_categories:
- 1M<n<10M
source_datasets:
- original
task_categories:
- token-classification
task_ids:
- named-entity-recognition
---

# Dataset Card for naamapadam

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-instances)
  - [Data Splits](#data-instances)
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

## Dataset Description

- **Homepage:** [Needs More Information]
- **Repository:** https://github.com/AI4Bharat/indicner
- **Paper:** [Needs More Information]
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** Anoop Kunchukuttan

### Dataset Summary

Naamapadam is the largest publicly available Named Entity Annotated dataset for 11 Indic languages. This corpora was created by projecting named entities from English side to the Indic language side of the English-Indic languages parallel corpus. The dataset additionally contains manually labelled test set for 8 Indic languages containing 500-1000 sentences. 


### Supported Tasks and Leaderboards

**Tasks:** NER on Indian languages.

**Leaderboards:** Currently there is no Leaderboard for this dataset.

### Languages
-  `Assamese (as)`
-  `Bengali (bn)`
-  `Gujarati (gu)`
-  `Kannada (kn)`
-  `Hindi (hi)`
-  `Malayalam (ml)`
-  `Marathi (mr)`
-  `Oriya (or)`
-  `Punjabi (pa)`
-  `Tamil (ta)`
-  `Telugu (te)`

## Dataset Structure

### Data Instances

{'words': ['उन्हेनें', 'शिकांगों','में','बोरोडिन','की','पत्नी','को','तथा','वाशिंगटन','में','रूसी','व्यापार','संघ','को','पैसे','भेजे','।'],
 'ner': [0, 3, 0, 1, 0, 0, 0, 0, 3, 0, 5, 6, 6, 0, 0, 0, 0],
 }

### Data Fields

- `words`: Raw tokens in the dataset.
- `ner`: the NER tags for this dataset. 

### Data Splits
(to be updated, see paper for correct numbers)

| Language | Train | Validation | Test |
|---:|---:|---:|---:|
| as | 10266 | 52 | 51 |
| bn | 961679 | 4859 | 607 |
| gu | 472845 | 2389 | 50 |
| hi | 985787 | 13460 | 437 |
| kn | 471763 | 2381 | 1019 |
| ml | 716652 | 3618 | 974 |
| mr | 455248 | 2300 | 1080 |
| or | 196793 | 993 | 994 |
| pa | 463534 | 2340 | 2342 |
| ta | 497882 | 2795 | 49 |
| te | 507741 | 2700 | 53 |


## Usage

You should have the 'datasets' packages installed to be able to use the :rocket: HuggingFace datasets repository. Please use the following command and install via pip:

```code
    pip install datasets
```

To use the dataset, please use:<br/>

```python
    from datasets import load_dataset
    hiner = load_dataset('ai4bharat/naamapadam')
```

## Dataset Creation
We use the parallel corpus from the Samanantar Dataset between English and the 11 major Indian languages to create the NER dataset. We annotate the English portion of the parallel corpus with existing state-of-the-art NER model. We use word-level alignments learned from the parallel corpus to project the entity labels from English to the Indian language.

### Curation Rationale

naamapadam was built from [Samanantar dataset](https://indicnlp.ai4bharat.org/samanantar/). This dataset was built for the task of Named Entity Recognition in Indic languages. The dataset was introduced to introduce new resources to the Indic languages language that was under-served for Natural Language Processing.

### Source Data

[Samanantar dataset](https://indicnlp.ai4bharat.org/samanantar/)

#### Initial Data Collection and Normalization

[Needs More Information]

#### Who are the source language producers?

[Needs More Information]

### Annotations

#### Annotation process

NER annotations were done following the CoNLL-2003 guidelines.

#### Who are the annotators?

The annotations for the testset have been done by volunteers who are proficient in the respective languages. We would like to thank all the volunteers: 

- Anil Mhaske 
- Anoop Kunchukuttan
- Archana Mhaske
- Arnav Mhaske
- Gowtham Ramesh
- Harshit Kedia
- Nitin Kedia
- Rudramurthy V
- Sangeeta Rajagopal
- Sumanth Doddapaneni
- Vindhya DS
- Yash Madhani
- Kabir Ahuja
- Shallu Rani
- Armin Virk

### Personal and Sensitive Information

[Needs More Information]

## Considerations for Using the Data

### Social Impact of Dataset

The purpose of this dataset is to provide a large-scale Named Entity Recognition dataset for Indic languages. Since the information (data points) has been obtained from public resources, we do not think there is a negative social impact in releasing this data. 


### Discussion of Biases

[Needs More Information]

### Other Known Limitations

[Needs More Information]

## Additional Information

### Dataset Curators

[Needs More Information]

### Licensing Information

<!-- <a rel="license" float="left" href="http://creativecommons.org/publicdomain/zero/1.0/">
  <img src="https://licensebuttons.net/p/zero/1.0/88x31.png" style="border-style: none;" alt="CC0" width="100" />
  <img src="https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by.png" style="border-style: none;" alt="CC-BY" width="100" href="http://creativecommons.org/publicdomain/zero/1.0/"/>
</a>
<br/> -->

**CC0 License Statement**
<a rel="license" float="left" href="https://creativecommons.org/about/cclicenses/">
  <img src="https://licensebuttons.net/p/zero/1.0/88x31.png" style="border-style: none;" alt="CC0" width="100"/>
</a>
<br>
<br>
- We do not own any of the text from which this data has been extracted.
- We license the actual packaging of the mined data under the [Creative Commons CC0 license (“no rights reserved”)](http://creativecommons.org/publicdomain/zero/1.0).
- To the extent possible under law, <a rel="dct:publisher" href="https://ai4bharat.iitm.ac.in/"> <span property="dct:title">AI4Bharat</span></a> has waived all copyright and related or neighboring rights to <span property="dct:title">Naamapadam</span> manually collected data and existing sources.
- This work is published from: India.


### Citation Information

If you are using the Naampadam corpus, please cite the following article:
```
@misc{mhaske2022naamapadam,
  doi = {10.48550/ARXIV.2212.10168},
  url = {https://arxiv.org/abs/2212.10168},
  author = {Mhaske, Arnav and Kedia, Harshit and Doddapaneni, Sumanth and Khapra, Mitesh M. and Kumar, Pratyush and Murthy, Rudra and Kunchukuttan, Anoop},
  title = {Naamapadam: A Large-Scale Named Entity Annotated Data for Indic Languages}
  publisher = {arXiv},
  year = {2022},
}
```

<!-- Contributors -->
### Contributors
 - Arnav Mhaske <sub> ([AI4Bharat](https://ai4bharat.org), [IITM](https://www.iitm.ac.in)) </sub>
 - Harshit Kedia <sub> ([AI4Bharat](https://ai4bharat.org), [IITM](https://www.iitm.ac.in)) </sub>
 - Sumanth Doddapaneni <sub> ([AI4Bharat](https://ai4bharat.org), [IITM](https://www.iitm.ac.in)) </sub>
 - Mitesh M. Khapra <sub> ([AI4Bharat](https://ai4bharat.org), [IITM](https://www.iitm.ac.in)) </sub>
 - Pratyush Kumar <sub> ([AI4Bharat](https://ai4bharat.org), [Microsoft](https://www.microsoft.com/en-in/), [IITM](https://www.iitm.ac.in)) </sub> 
 - Rudra Murthy <sub> ([AI4Bharat](https://ai4bharat.org), [IBM](https://www.ibm.com))</sub>
 - Anoop Kunchukuttan <sub> ([AI4Bharat](https://ai4bharat.org), [Microsoft](https://www.microsoft.com/en-in/), [IITM](https://www.iitm.ac.in)) </sub> 

This work is the outcome of a volunteer effort as part of the [AI4Bharat initiative](https://ai4bharat.iitm.ac.in).


<!-- Contact -->
### Contact
- Anoop Kunchukuttan ([anoop.kunchukuttan@gmail.com](mailto:anoop.kunchukuttan@gmail.com))
- Rudra Murthy V ([rmurthyv@in.ibm.com](mailto:rmurthyv@in.ibm.com))