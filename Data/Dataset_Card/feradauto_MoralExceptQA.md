---
pretty_name: MoralExceptQA
task_categories: 
- text-classification
---
# Dataset Card for MoralExceptQA

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Repository:** [MoralCoT](https://github.com/feradauto/MoralCoT)
- **Paper:** [When to Make Exceptions: Exploring Language Models as Accounts of Human Moral Judgment](https://arxiv.org/abs/2210.01478)
- **Point of Contact:** [Fernando Gonzalez](mailto:fgonzalez@ethz.ch) , [Zhijing Jin](mailto:zjin@tue.mpg.de)
### Dataset Summary

Challenge set consisting of moral exception question answering of cases that involve potentially permissible moral exceptions. Our challenge set, MoralExceptQA, is drawn from a series of recent moral psychology studies designed to investigate the flexibility of human moral cognition – specifically, the ability of humans to figure out when it is permissible to break a previously established or well-known rule.
### Languages

The language in the dataset is English.

## Dataset Structure

### Data Instances

Each instance is a rule-breaking scenario acompanied by an average human response.

### Data Fields

- `study`: The moral psychology study. Studies were designed to investigate the ability of humans
to figure out when it is permissible to break a previously established or well-known rule.
- `context`: The context of the scenario. Different context within the same study are potentially governed by the same rule.
- `condition`: Condition in the scenario.
- `scenario`: Text description of the scenario.
- `human.response`: Average human response (scale 0 to 1) equivalent to the % of people that considered that breaking the rule is permissible. 

### Data Splits

MoralExceptQA contains one split.

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

Information about the data collection and annotators can be found in the appendix of [our paper](https://arxiv.org/abs/2210.01478).

### Personal and Sensitive Information

 The MoralExceptQA dataset does not have privacy concerns.

## Considerations for Using the Data

### Social Impact of Dataset

The intended use of this work is to contribute to AI safety research. We do not intend this work to be developed as a tool to automate moral decision-making on behalf of humans, but instead as a way of mitigating risks caused by LLMs’ misunderstanding of human values. The MoralExceptQA dataset does not have privacy concerns or offensive content.

### Discussion of Biases

Our subjects are U.S. residents, and therefore our conclusions are limited to this population.


## Additional Information

### Dataset Curators

[More Information Needed]

### Licensing Information

The MoralExceptQA dataset is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/).

### Citation Information

```
@misc{https://doi.org/10.48550/arxiv.2210.01478,
  doi = {10.48550/ARXIV.2210.01478},
  
  url = {https://arxiv.org/abs/2210.01478},
  
  author = {Jin, Zhijing and Levine, Sydney and Gonzalez, Fernando and Kamal, Ojasv and Sap, Maarten and Sachan, Mrinmaya and Mihalcea, Rada and Tenenbaum, Josh and Schölkopf, Bernhard},
  
  keywords = {Computation and Language (cs.CL), Artificial Intelligence (cs.AI), Computers and Society (cs.CY), Machine Learning (cs.LG), FOS: Computer and information sciences, FOS: Computer and information sciences},
  
  title = {When to Make Exceptions: Exploring Language Models as Accounts of Human Moral Judgment},
  
  publisher = {arXiv},
  
  year = {2022},
  
  copyright = {Creative Commons Attribution Share Alike 4.0 International}
}

```