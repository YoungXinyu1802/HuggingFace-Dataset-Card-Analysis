---
annotations_creators:
- found
language_creators:
- found
language:
- en
license:
- unknown
multilinguality:
- monolingual
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories:
- summarization
task_ids:
- summarization-other-paper-abstract-generation
paperswithcode_id: multi-document
pretty_name: Multi-Document
---
# Dataset Card for Multi-Document
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
- **Repository:** [Multi-Document repository](https://github.com/arka0821/multi_document_summarization)
- **Paper:** [Multi-Document: A Large-scale Dataset for Extreme Multi-document Summarization of Scientific Articles](https://arxiv.org/abs/2010.14235)
### Dataset Summary
Multi-Document, a large-scale multi-document summarization dataset created from scientific articles. Multi-Document introduces a challenging multi-document summarization task: writing the related-work section of a paper based on its abstract and the articles it references.
### Supported Tasks and Leaderboards
[More Information Needed]
### Languages
The text in the dataset is in English
## Dataset Structure
### Data Instances
{"id": "n3ByHGrxH3bvfrvF", "docs": [{"id": "1394519630182457344", "text": "Clover Bio's COVID-19 vaccine candidate shows immune response against SARS-CoV-2 variants in mouse model https://t.co/wNWa9GQux5"}, {"id": "1398154482463170561", "text": "The purpose of the Vaccine is not to stop you from catching COVID 19. The vaccine introduces the immune system to an inactivated form of the SARS-CoV-2 coronavirus or a small part of it. This then equips the body with the ability to fight the virus better in case you get it. https://t.co/Cz9OU6Zi7P"}, {"id": "1354844652520792071", "text": "The Moderna mRNA COVID-19 vaccine appears to be effective against the novel, rapidly spreading variants of SARS-CoV-2.\nResearchers analysed blood samples from vaccinated people and monkeys- Both contained neutralising antibodies against the virus. \nPT1/2\n#COVID19vaccines #biotech https://t.co/ET1maJznot"}, {"id": "1340189698107518976", "text": "@KhandaniM Pfizer vaccine introduces viral surface protein which is constant accross SARS COV 2 variants into the body. Body builds antibodies against this protein, not any virus. These antibodies instructs macrophages &amp; T-Cells to attack &amp; destroy any COVID-19 v variant  at infection point"}, {"id": "1374368989581778945", "text": "@DelthiaRicks \" Pfizer and BioNTech\u2019s COVID-19 vaccine is an mRNA vaccine, which does not use the live virus but rather a small portion of the viral sequence of the SARS-CoV-2 virus to instruct the body to produce the spike protein displayed on the surface of the virus.\""}, {"id": "1353354819315126273", "text": "Pfizer and BioNTech Publish Results of Study Showing COVID-19 Vaccine Elicits Antibodies that Neutralize Pseudovirus Bearing the SARS-CoV-2 U.K. Strain Spike Protein in Cell Culture | Pfizer https://t.co/YXcSnjLt8C"}, {"id": "1400821856362401792", "text": "Pfizer-BioNTech's covid-19 vaccine elicits lower levels of antibodies against the SARS-CoV-2\u00a0Delta variant\u00a0(B.1.617.2), first discovered in India, in comparison to other variants, said a research published in\u00a0Lancet\u00a0journal.\n https://t.co/IaCMX81X3b"}, {"id": "1367252963190665219", "text": "New research from UNC-Chapel Hill suggests that those who have previously experienced a SARS-CoV-2 infection develop a significant antibody response to the first dose of mRNA-based COVID-19 vaccine.\nhttps://t.co/B4vR1KUQ0w"}, {"id": "1375949502461394946", "text": "Mechanism of a COVID-19 nanoparticle vaccine candidate that elicits a broadly neutralizing antibody response to SARS-CoV-2 variants  https://t.co/nc1L0uvtlI #bioRxiv"}, {"id": "1395428608349548550", "text": "JCI - Efficient maternal to neonatal transfer of antibodies against SARS-CoV-2 and BNT162b2 mRNA COVID-19 vaccine https://t.co/vIBcpPaKFZ"}], "summary": "The COVID-19 vaccine appears to be effective against the novel, rapidly spreading variants of SARS-CoV-2. Pfizer-BioNTech's COVID-19 vaccine use small portion of the viral sequence of the SARS-CoV-2 virus to equip the body with the ability to fight the virus better in case you get it."}
### Data Fields
{'id': text of paper abstract \
 'docs': document id \
 [
   'id': id of text \
   'text': text data \
 ]
  'summary': summary text
 }
### Data Splits
The data is split into a training, validation and test.
| train | validation | test |
|------:|-----------:|-----:|
| 50    |       10   | 5    |
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
```
@article{lu2020multi,
  title={Multi-Document: A Large-scale Dataset for Extreme Multi-document Summarization of Scientific Articles},
  author={Arka Das, India},
  journal={arXiv preprint arXiv:2010.14235},
  year={2022}
}
```
### Contributions
Thanks to [@arka0821] (https://github.com/arka0821/multi_document_summarization) for adding this dataset.

