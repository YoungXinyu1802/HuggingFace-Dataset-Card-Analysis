---
annotations_creators:
- expert-generated
language_creators:
- expert-generated
language:
- en
license:
- cc-by-4.0
multilinguality:
- monolingual
size_categories:
- 10K<n<100K
source_datasets: []
task_categories:
- text-classification
- structure-prediction
task_ids:
- multi-class-classification
- named-entity-recognition
- parsing
---

# Dataset Card for sd-nlp
## Table of Contents
- [Dataset Card for [EMBO/sd-nlp-non-tokenized]](#dataset-card-for-dataset-name)
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
      - [Initial Data Collection and Normalization](#initial-data-collection-and-normalization)
      - [Who are the source language producers?](#who-are-the-source-language-producers)
    - [Annotations](#annotations)
      - [Annotation process](#annotation-process)
      - [Who are the annotators?](#who-are-the-annotators)
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
- **Homepage:** https://sourcedata.embo.org
- **Repository:** https://github.com/source-data/soda-roberta
- **Paper:**
- **Leaderboard:**
- **Point of Contact:** thomas.lemberger@embo.org, jorge.abreu@embo.org
### Dataset Summary
This dataset is based on the content of the SourceData (https://sourcedata.embo.org) database, which contains manually annotated figure legends written in English and extracted from scientific papers in the domain of cell and molecular biology (Liechti et al, Nature Methods, 2017, https://doi.org/10.1038/nmeth.4471). 
Unlike the dataset [`sd-nlp`](https://huggingface.co/datasets/EMBO/sd-nlp), pre-tokenized with the `roberta-base` tokenizer, this dataset is not previously tokenized, but just splitted into words. Users can therefore use it to fine-tune other models. 
Additional details at https://github.com/source-data/soda-roberta
### Supported Tasks and Leaderboards
Tags are provided as [IOB2-style tags](https://en.wikipedia.org/wiki/Inside%E2%80%93outside%E2%80%93beginning_(tagging)).
`PANELIZATION`: figure captions (or figure legends) are usually composed of segments that each refer to one of several 'panels' of the full figure. Panels tend to represent results obtained with a coherent method and depicts data points that can be meaningfully compared to each other. `PANELIZATION` provide the start (B-PANEL_START) of these segments and allow to train for recogntion of the boundary between consecutive panel lengends.
`NER`: biological and chemical entities are labeled. Specifically the following entities are tagged:
- `SMALL_MOLECULE`: small molecules
- `GENEPROD`: gene products (genes and proteins)
- `SUBCELLULAR`: subcellular components
- `CELL`: cell types and cell lines.
- `TISSUE`: tissues and organs
- `ORGANISM`: species
- `EXP_ASSAY`: experimental assays
`ROLES`: the role of entities with regard to the causal hypotheses tested in the reported results. The tags are:
- `CONTROLLED_VAR`: entities that are associated with experimental variables and that subjected to controlled and targeted perturbations.
- `MEASURED_VAR`: entities that are associated with the variables measured and the object of the measurements.
`BORING`: entities are marked with the tag `BORING` when they are more of descriptive value and not directly associated with causal hypotheses ('boring' is not an ideal choice of word, but it is short...). Typically, these entities are so-called 'reporter' geneproducts, entities used as common baseline across samples, or specify the context of the experiment (cellular system, species, etc...).
### Languages
The text in the dataset is English.
## Dataset Structure
### Data Instances
```json
{'text': '(E) Quantification of the number of cells without γ-Tubulin at centrosomes (γ-Tub -) in pachytene and diplotene spermatocytes in control, Plk1(∆/∆) and BI2536-treated spermatocytes. Data represent average of two biological replicates per condition. ',
 'labels': [0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  13,
  14,
  14,
  14,
  14,
  14,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  3,
  4,
  4,
  4,
  4,
  4,
  4,
  4,
  4,
  0,
  0,
  0,
  0,
  5,
  6,
  6,
  6,
  6,
  6,
  6,
  6,
  6,
  6,
  6,
  0,
  0,
  3,
  4,
  4,
  4,
  4,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  7,
  8,
  8,
  8,
  8,
  8,
  8,
  8,
  8,
  8,
  8,
  8,
  8,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  3,
  4,
  4,
  4,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  1,
  2,
  2,
  2,
  2,
  2,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  7,
  8,
  8,
  8,
  8,
  8,
  8,
  8,
  8,
  8,
  8,
  8,
  8,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0]}
```
### Data Fields
- `text`: `str` of the text
- `label_ids` dictionary composed of list of strings on a character-level:
  - `entity_types`: `list` of `strings` for the IOB2 tags for entity type; possible value in `["O", "I-SMALL_MOLECULE",  "B-SMALL_MOLECULE",  "I-GENEPROD", "B-GENEPROD", "I-SUBCELLULAR", "B-SUBCELLULAR", "I-CELL", "B-CELL", "I-TISSUE", "B-TISSUE", "I-ORGANISM", "B-ORGANISM", "I-EXP_ASSAY", "B-EXP_ASSAY"]`
  - `panel_start`: `list` of `strings` for IOB2 tags `["O", "B-PANEL_START"]`  

### Data Splits
```python
  DatasetDict({
      train: Dataset({
          features: ['text', 'labels'],
          num_rows: 66085
      })
      test: Dataset({
          features: ['text', 'labels'],
          num_rows: 8225
      })
      validation: Dataset({
          features: ['text', 'labels'],
          num_rows: 7948
      })
  })
```
## Dataset Creation
### Curation Rationale
The dataset was built to train models for the automatic extraction of a knowledge graph based from the scientific literature. The dataset can be used to train character-based models for text segmentation and named entity recognition. 
### Source Data
#### Initial Data Collection and Normalization
Figure legends were annotated according to the SourceData framework described in Liechti et al 2017 (Nature Methods, 2017, https://doi.org/10.1038/nmeth.4471). The curation tool at https://curation.sourcedata.io was used to segment figure legends into panel legends, tag enities, assign experiemental roles and normalize with standard identifiers (not available in this dataset). The source data was downloaded from the SourceData API (https://api.sourcedata.io) on 21 Jan 2021.
#### Who are the source language producers?
The examples are extracted from the figure legends from scientific papers in cell and molecular biology. 
### Annotations
#### Annotation process
The annotations were produced manually with expert curators from the SourceData project (https://sourcedata.embo.org)
#### Who are the annotators?
Curators of the SourceData project.
### Personal and Sensitive Information
None known.
## Considerations for Using the Data
### Social Impact of Dataset
Not applicable.
### Discussion of Biases
The examples are heavily biased towards cell and molecular biology and are enriched in examples from papers published in EMBO Press journals (https://embopress.org)
### Other Known Limitations
[More Information Needed]
## Additional Information
### Dataset Curators
Thomas Lemberger, EMBO.
### Licensing Information
CC BY 4.0
### Citation Information
[More Information Needed]
### Contributions
Thanks to [@tlemberger](https://github.com/tlemberger>) and [@drAbreu](https://github.com/drAbreu>) for adding this dataset.