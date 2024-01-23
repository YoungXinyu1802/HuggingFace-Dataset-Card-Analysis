---
annotations_creators:
- expert-generated
language_creators:
- found
language:
- de
license:
- cc-by-4.0
multilinguality:
- monolingual
paperswithcode_id: dataset-of-legal-documents
pretty_name: German Named Entity Recognition in Legal Documents
size_categories:
- 1M<n<10M
source_datasets:
- original
tags:
- ner, named entity recognition, legal ner, legal texts, label classification
task_categories:
- token-classification
task_ids:
- named-entity-recognition
train-eval-index:
- config: conll2003
  task: token-classification
  task_id: entity_extraction
  splits:
    train_split: train
    eval_split: test
  col_mapping:
    tokens: tokens
    ner_tags: tags
---

# Dataset Card for "German LER"

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

- **Homepage:** [https://github.com/elenanereiss/Legal-Entity-Recognition](https://github.com/elenanereiss/Legal-Entity-Recognition)
- **Paper:** [https://arxiv.org/pdf/2003.13016v1.pdf](https://arxiv.org/pdf/2003.13016v1.pdf)
- **Point of Contact:** [elena.leitner@dfki.de](elena.leitner@dfki.de)

### Dataset Summary

A dataset of Legal Documents from German federal court decisions for Named Entity Recognition. The dataset is human-annotated with 19 fine-grained entity classes. The dataset consists of approx. 67,000 sentences and contains 54,000 annotated entities. NER tags use the `BIO` tagging scheme. 

The dataset includes two different versions of annotations, one with a set of 19 fine-grained semantic classes (`ner_tags`) and another one with a set of 7 coarse-grained classes (`ner_coarse_tags`). There are 53,632 annotated entities in total, the majority of which (74.34 %) are legal entities, the others are person, location and organization (25.66 %).

![](https://raw.githubusercontent.com/elenanereiss/Legal-Entity-Recognition/master/docs/Distribution.png)

For more details see [https://arxiv.org/pdf/2003.13016v1.pdf](https://arxiv.org/pdf/2003.13016v1.pdf).

### Supported Tasks and Leaderboards

- **Tasks:** Named Entity Recognition
- **Leaderboards:**

### Languages

German

## Dataset Structure
### Data Instances
```python
{
 'id': '1',
 'tokens': ['Eine', 'solchermaßen', 'verzögerte', 'oder', 'bewusst', 'eingesetzte', 'Verkettung', 'sachgrundloser', 'Befristungen', 'schließt', '§', '14', 'Abs.', '2', 'Satz', '2', 'TzBfG', 'aus', '.'],
 'ner_tags': [38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 3, 22, 22, 22, 22, 22, 22, 38, 38],
 'ner_coarse_tags': [14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 2, 9, 9, 9, 9, 9, 9, 14, 14]
}
```
### Data Fields

```python
{
 'id': Value(dtype='string', id=None),
 'tokens': Sequence(feature=Value(dtype='string', id=None), 
                    length=-1, id=None),
 'ner_tags': Sequence(feature=ClassLabel(num_classes=39, 
                                         names=['B-AN', 
                                                'B-EUN', 
                                                'B-GRT', 
                                                'B-GS', 
                                                'B-INN', 
                                                'B-LD', 
                                                'B-LDS', 
                                                'B-LIT', 
                                                'B-MRK', 
                                                'B-ORG', 
                                                'B-PER', 
                                                'B-RR', 
                                                'B-RS', 
                                                'B-ST', 
                                                'B-STR', 
                                                'B-UN', 
                                                'B-VO', 
                                                'B-VS', 
                                                'B-VT', 
                                                'I-AN', 
                                                'I-EUN', 
                                                'I-GRT', 
                                                'I-GS', 
                                                'I-INN', 
                                                'I-LD', 
                                                'I-LDS', 
                                                'I-LIT', 
                                                'I-MRK', 
                                                'I-ORG', 
                                                'I-PER', 
                                                'I-RR', 
                                                'I-RS', 
                                                'I-ST', 
                                                'I-STR', 
                                                'I-UN', 
                                                'I-VO', 
                                                'I-VS', 
                                                'I-VT', 
                                                'O'], 
                                         id=None), 
                      length=-1, 
                      id=None),
 'ner_coarse_tags': Sequence(feature=ClassLabel(num_classes=15, 
                                                names=['B-LIT', 
                                                       'B-LOC', 
                                                       'B-NRM', 
                                                       'B-ORG', 
                                                       'B-PER', 
                                                       'B-REG', 
                                                       'B-RS', 
                                                       'I-LIT', 
                                                       'I-LOC', 
                                                       'I-NRM', 
                                                       'I-ORG', 
                                                       'I-PER', 
                                                       'I-REG', 
                                                       'I-RS', 
                                                       'O'], 
                                                 id=None), 
                              length=-1, 
                              id=None)
}
```

### Data Splits

|                         | train | validation | test |
|-------------------------|------:|-----------:|-----:|
| Input Sentences         | 53384 |    6666    | 6673 |




## Dataset Creation

### Curation Rationale

Documents in the legal domain contain multiple references to named entities, especially domain-specific named entities, i. e., jurisdictions, legal institutions, etc. Legal documents are unique and differ greatly from newspaper texts. On the one hand, the occurrence of general-domain named entities is relatively rare. On the other hand, in concrete applications, crucial domain-specific entities need to be identified in a reliable way, such as designations of legal norms and references to other legal documents (laws, ordinances, regulations, decisions, etc.). Most NER solutions operate in the general or news domain, which makes them inapplicable to the analysis of legal documents. Accordingly, there is a great need for an NER-annotated dataset consisting of legal documents, including the corresponding development of a typology of semantic concepts and uniform annotation guidelines.

### Source Data

Court decisions from 2017 and 2018 were selected for the dataset, published online by the [Federal Ministry of Justice and Consumer Protection](http://www.rechtsprechung-im-internet.de). The documents originate from seven federal courts: Federal Labour Court (BAG), Federal Fiscal Court (BFH), Federal Court of Justice (BGH), Federal Patent Court (BPatG), Federal Social Court (BSG), Federal Constitutional Court (BVerfG) and Federal Administrative Court (BVerwG). 

#### Initial Data Collection and Normalization

From the table of [contents](http://www.rechtsprechung-im-internet.de/rii-toc.xml), 107 documents from each court were selected (see Table 1). The data was collected from the XML documents, i. e., it was extracted from the XML elements `Mitwirkung, Titelzeile, Leitsatz, Tenor, Tatbestand, Entscheidungsgründe, Gründen, abweichende Meinung, and sonstiger Titel`. The metadata at the beginning of the documents (name of court, date of decision, file number, European Case Law Identifier, document type, laws) and those that belonged to previous legal proceedings was deleted. Paragraph numbers were removed. 

The extracted data was split into sentences, tokenised using [SoMaJo](https://github.com/tsproisl/SoMaJo) and manually annotated in [WebAnno](https://webanno.github.io/webanno/).

#### Who are the source language producers?

The Federal Ministry of Justice and the Federal Office of Justice provide selected decisions. Court decisions were produced by humans.

### Annotations

#### Annotation process

For more details see [annotation guidelines](https://github.com/elenanereiss/Legal-Entity-Recognition/blob/master/docs/Annotationsrichtlinien.pdf) (in German).

<!-- #### Who are the annotators?

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)--> 

### Personal and Sensitive Information

A fundamental characteristic of the published decisions is that all personal information have been anonymised for privacy reasons. This affects the classes person, location and organization. 

<!-- ## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Discussion of Biases

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Other Known Limitations

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

## Additional Information

### Dataset Curators

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)--> 

### Licensing Information

[CC BY-SA 4.0 license](https://creativecommons.org/licenses/by-sa/4.0/)

### Citation Information

```
@misc{https://doi.org/10.48550/arxiv.2003.13016,
  doi = {10.48550/ARXIV.2003.13016},
  url = {https://arxiv.org/abs/2003.13016},  
  author = {Leitner, Elena and Rehm, Georg and Moreno-Schneider, Julián},  
  keywords = {Computation and Language (cs.CL), Information Retrieval (cs.IR), FOS: Computer and information sciences, FOS: Computer and information sciences},  
  title = {A Dataset of German Legal Documents for Named Entity Recognition},  
  publisher = {arXiv},  
  year = {2020},  
  copyright = {arXiv.org perpetual, non-exclusive license}
}

```

### Contributions
