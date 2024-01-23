---
annotations_creators:
- expert-generated
language_creators:
- expert-generated
language:
- en
license:
- unknown
multilinguality:
- monolingual
size_categories:
- 10K<n<100K
source_datasets:
- GitHub
task_categories:
- token-classification
task_ids:
- named-entity-recognition
paperswithcode_id: bc4chemd
pretty_name: bc4chemd_ner
---
# Dataset Card for bc2gm_corpus
## Table of Contents
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
- **Homepage:** [Github](https://biocreative.bioinformatics.udel.edu/resources/biocreative-iv/chemdner-corpus/)
- **Repository:** [Github](https://github.com/cambridgeltl/MTL-Bioinformatics-2016/tree/master/data/BC4CHEMD)
- **Paper:** [NCBI](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4331692/)
- **Leaderboard:**
- **Point of Contact:**
### Dataset Summary
[More Information Needed]
### Supported Tasks and Leaderboards
* Token Classification
* Named Entity Recognition
### Languages
- English
## Dataset Structure
### Data Instances
[More Information Needed]
### Data Fields
- `id`: Sentence identifier.  
- `tokens`: Array of tokens composing a sentence.  
- `ner_tags`: Array of tags, where `0` indicates no disease mentioned, `1` signals the first token of a disease and `2` the subsequent disease tokens.  
### Data Splits
```python
DatasetDict({
    train: Dataset({
        features: ['id', 'tokens', 'ner_tags'],
        num_rows: 30683
    })
    validation: Dataset({
        features: ['id', 'tokens', 'ner_tags'],
        num_rows: 30640
    })
    test: Dataset({
        features: ['id', 'tokens', 'ner_tags'],
        num_rows: 26365
    })
})
```

## Dataset Creation
### Curation Rationale
The automatic extraction of chemical information from text requires the recognition of chemical 
entity mentions as one of its key steps. When developing supervised named entity recognition 
(NER) systems, the availability of a large, manually annotated text corpus is desirable. 
Furthermore, large corpora permit the robust evaluation and comparison of different 
approaches that detect chemicals in documents.

### Source Data
#### Initial Data Collection and Normalization
[More Information Needed]

### Annotations
#### Annotation process
We present the CHEMDNER corpus, a collection of 10,000 PubMed abstracts that contain a 
total of 84,355 chemical entity mentions labeled manually by expert chemistry literature curators, 
following annotation guidelines specifically defined for this task. 

#### Who are the annotators?
Expert chemistry literature curators

### Personal and Sensitive Information
It does not contain this kind of information
The abstracts of the CHEMDNER corpus were selected to be representative for all 
major chemical disciplines. Each of the chemical entity mentions was manually 
labeled according to its structure-associated chemical entity mention (SACEM) 
class: abbreviation, family, formula, identifier, multiple, systematic and 
trivial. The difficulty and consistency of tagging chemicals in text was measured using an agreement study 
between annotators, obtaining a percentage agreement of 91.

### Licensing Information
Unknown

### Citation Information
```latex
@article{Krallinger2015TheCC,
  title={The CHEMDNER corpus of chemicals and drugs and its annotation principles},
  author={Martin Krallinger and Obdulia Rabal and Florian Leitner and Miguel Vazquez and David Salgado and Zhiyong Lu and Robert Leaman and Yanan Lu and Dong-Hong Ji and Daniel M. Lowe and Roger A. Sayle and Riza Theresa Batista-Navarro and Rafal Rak and Torsten Huber and Tim Rockt{\"a}schel and S{\'e}rgio Matos and David Campos and Buzhou Tang and Hua Xu and Tsendsuren Munkhdalai and Keun Ho Ryu and S. V. Ramanan and P. Senthil Nathan and Slavko Zitnik and Marko Bajec and Lutz Weber and Matthias Irmer and Saber Ahmad Akhondi and Jan A. Kors and Shuo Xu and Xin An and Utpal Kumar Sikdar and Asif Ekbal and Masaharu Yoshioka and Thaer M. Dieb and Miji Choi and Karin M. Verspoor and Madian Khabsa and C. Lee Giles and Hongfang Liu and K. E. Ravikumar and Andre Lamurias and Francisco M. Couto and Hong-Jie Dai and Richard Tzong-Han Tsai and C Ata and Tolga Can and Anabel Usie and Rui Alves and Isabel Segura-Bedmar and Paloma Mart{\'i}nez and Julen Oyarz{\'a}bal and Alfonso Valencia},
  journal={Journal of Cheminformatics},
  year={2015},
  volume={7},
  pages={S2 - S2}
}
```

### Contributions
Thanks to [@GamalC](https://github.com/GamalC) for uploading this dataset to GitHub.
