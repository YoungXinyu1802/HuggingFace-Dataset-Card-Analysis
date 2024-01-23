---
annotations_creators:
- expert-generated
language_creators:
- expert-generated
language:
- en
license:
- mit
multilinguality:
- monolingual
pretty_name: PET
size_categories:
- 1K<n<10K
source_datasets: 
  [Friedrich et al. original dataset]
task_categories:
- token-classification
task_ids:
- token classification
- named entity recognition
- relation extraction
---

# PET: A NEW DATASET FOR PROCESS EXTRACTION FROM TEXT

# Dataset Card for PET

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
- [Annotation Guidelines](#annotationguidelines)
- [Update](#updates)
- [Loading data](#loadingdata)


## Dataset Description

- **Homepage:** https://pdi.fbk.eu/pet-dataset/
- **Paper:** https://arxiv.org/abs/2203.04860
- **Point of Contact:** [Patrizio Bellan](pbellan@fbk.eu)

### Dataset Summary

Abstract. Although there is a long tradition of work in NLP on extracting entities and relations from text, to date there exists little work on the acquisition of business processes from unstructured data such as textual corpora of process descriptions. With this work we aim at filling this gap and establishing the first steps towards bridging data-driven information extraction methodologies from Natural Language Processing and the model-based formalization that is aimed from Business Process Management. For this, we develop the first corpus of business process descriptions annotated with activities, actors, activity data, gateways and their conditions. We present our new resource to benchmark the difficulty and challenges of business process extraction from text.

### Supported Tasks and Leaderboards

- Token Classification
- Named Entity Recognition
- Relations Extraction

### Languages

English

## Dataset Structure

Test set to beanchmark *Business Process Extraction from Text* approaches.

### Data Instances
#### Token Classification

For each instance, there is a document name representing the name of the document of the Friedrich *et al.* dataset, an integer representing the number of the sentence, a list of tokens representing the words of the sentence instance, and a list of *ner tags* (in IOB2 format) representing the annotation of process elements of the sentence.

Below, an example of data instance.
```
{
  "document name":"doc-1.1",
  "sentence-ID":1,
  "tokens":["Whenever","the","sales","department","receives","an","order",",","a","new","process","instance","is","created","."],
  "ner-tags":["O","B-Actor","I-Actor","I-Actor","B-Activity","B-Activity Data","I-Activity Data","O","O","O","O","O","O","O","O"]
}
```

#### Relations Extraction


For each instance, there is a document name representing the name of the document of the Friedrich *et al.* dataset, a list of tokens representing the words of the document instance, a list of interger representing the words position within each sentence of the document instance, a list of *ner tags* (in IOB2 format) representing the annotation of the token, a list of sentence id representing for each token the number of the sentence, and a list of relations of the document.

Below, an example of data instance.
```
{
  "document name": "doc-1.1", 
  "tokens": ["A", "small", "company",...],
  "tokens-IDs": [0, 1, 2, ...], 
  "ner_tags": ["O", "O", "O", ...],
  "sentence-IDs": [0, 0, 0, ...],
  "relations": {
                "source-head-sentence-ID": [1, 1, 1, ...], 
                "source-head-word-ID": [4, 4, 4, ...], 
                "relation-type": ["uses", "flow", "actor recipient", ...], 
                "target-head-sentence-ID": [1, 2, 1,...], 
                "target-head-word-ID": [5, 9, 1, ...]
                }
}
```

### Data Fields
#### Token Classification

- *document name*: a string used to represent the name of the document.
- *sentence-ID*: an integer (starting from 0) representing the number of the sentence within the document.
- *tokens*: a list of string representing the words of the sentence
- *ner-tags*: a list of string representing the annotation for each word.

The allowed **ner-tags** are: 
  - **O**: An O tag indicates that a token belongs to no chunk.
  - **B-Actor**: This tag indicates the beginning of an *Actor* chunk.
  - **I-Actor**: This tag indicates that the tag is inside an *Actor*  chunk.
  - **B-Activity**: This tag indicates the beginning of an *Activity* chunk.
  - **I-Activity**: This tag indicates that the tag is inside an *Activity* chunk.
  - **B-Activity Data**: This tag indicates the beginning of an *Activity Data* chunk.
  - **I-Activity Data**: This tag indicates that the tag is inside an *Activity Data* chunk.
  - **B-Further Specification**: This tag indicates the beginning of a *Further Specification* chunk.
  - **I-Further Specification**: This tag indicates that the tag is inside a *Further Specification* chunk.
  - **B-XOR Gateway**: This tag indicates the beginning of a *XOR Gateway* chunk.
  - **I-XOR Gateway**: This tag indicates that the tag is inside a *XOR Gateway* chunk.
  - **B-Condition Specification**: This tag indicates the beginning of a *Condition Specification* chunk.
  - **I-Condition Specification**: This tag indicates that the tag is inside a *Condition Specification* chunk.
  - **B-AND Gateway**: This tag indicates the beginning of an *AND Gateway* chunk.
  - **I-AND Gateway**: This tag indicates that the tag is inside an *AND Gateway* chunk.

To have a complete explanation of each process element tag please refer to the [research paper](https://arxiv.org/abs/2203.04860) and the [annotation guidelines](https://pdi.fbk.eu/pet/annotation-guidelines-for-process-description.pdf).

### Relations Extraction
- *document name*: a string used to represent the name of the document.
- *tokens*: a list of string representing the words of the document
- *tokens-IDs*: a list of interger representing the word position within a sentence.
- *ner_tags*: a list of string representing the annotation for each word. (see ner-tags above)
- *sentence-IDs*: a list of interger representing the sentence number for each word of the document.
- *relations*:: a list of document relations.
  - *source-head-sentence-ID*: a list of sentence ID pointing to the sentence number of the head (first token) of the source entity.
  - *source-head-word-ID*: a list of token ID pointing to the word ID of the head (first token) of the source entity.
  - *relation-type*: a list of relation tags.
  - *target-head-sentence-ID*: a list of sentence ID pointing to the sentence number of the head (first token) of the target entity.
  - *target-head-word-ID*: a list of token ID pointing to the word ID of the head (first token) of the target entity.

For instance, a relation is defined by the instances of *source-head-sentence-ID*, *source-head-word-ID*, *relation-type*, *target-head-sentence-ID*, and *target-head-word-ID* at the same index position.
In the following example, the first relation of the first document is shown:
```python
document_1=modelhub_dataset['test'][0]
relation = {
            'source-head-sentence-ID': document_1['relations']['source-head-sentence-ID'][0],
            'source-head-word-ID': document_1['relations']['source-head-word-ID'][0],
            'relation-type': document_1['relations']['relation-type'][0],
            'target-head-sentence-ID': document_1['relations']['target-head-sentence-ID'][0],
            'target-head-word-ID': document_1['relations']['target-head-sentence-ID'][0],
          }
print(relation)          
```
the output is:
```python
{'relation-type': 'uses',
 'source-head-sentence-ID': 1,
 'source-head-word-ID': 4,
 'target-head-sentence-ID': 1,
 'target-head-word-ID': 1}
```
That means:
  the entity in sentence number *1*, starting at the token position *4* has a *uses* relation with the entity in sentence number *1* starting at token position *1*
  
  
### Data Splits

The data was not splited. It contains the test set only.

## Dataset Creation

### Curation Rationale

Although there is a long tradition of work in NLP on extracting entities and relations from text, to date there exists little work on the acquisition of business processes from unstructured data such as textual corpora of process descriptions. With this work we aim at filling this gap and establishing the first steps towards bridging data-driven information extraction methodologies from Natural Language Processing and the model-based formalization that is aimed from Business Process Management.

### Source Data

#### Initial Data Collection and Normalization


The dataset construction process has been split in five main phases:
  1. Text pre-processing. As the first operation, we check the content of each document and we tokenized it. This initial check was necessary since some of the original texts were automatically translated into English by the authors of the dataset. The translations were never validated, indeed, several errors have been found and fixed.
  
  2. Text Annotation. Each text has been annotated by using the [guidelines](https://pdi.fbk.eu/pet/annotation-guidelines-for-process-description.pdf). The team was composed by five annotators with high expertise in BPMN. Each document has been assigned to three experts that were in change of identifying all the elements and flows with each document. In this phase, we used the the Inception tool to support annotators.
  
  3. Automatic annotation fixing. After the second phase, we ran an automatic procedure relying on a rule-based script to automatically fix annotations that were not compliant with the guidelines. For example, if a modal verb was erroneously included in the annotation of an Activity, the procedure removed it from the annotation. Another example is the missing of the article within an annotation related to an Actor. In this case, the script included it in the annotation. This phase allowed to remove possible annotation errors and to obtain annotations compliant with the guidelines.

  4. Agreement Computation. Here, we computed, on the annotation provided by the experts, the agreement scores for each process element and for each relation between process elements pair adopting the methodology proposed in [Hripcsak *et al.*](https://academic.oup.com/jamia/article/12/3/296/812057?login=true). We measured the agreement in terms of the F1 measure because, besides being straightforward to calculate, it is directly interpretable. Note that chance-corrected measures like *k* approach the F1-measure as the number of cases that raters agree are negative grows. By following such a methodology, an annotation was considered in agreement among the experts if and only if they capture the same span of words and they assign the same process element tag to the annotation.

  5. Reconciliation. The last phase consisted of the mitigation of disagreements within the annotations provided by the experts. The aim of this phase is to obtain a shared and agreed set of gold standard annotations on each text for both entities and relations. Such entities also enable the generation of the related full-connected process model flow that can be rendered by using, but not limited to, a BPMN diagram. During this last phase, among the 47 documents originally included into the dataset, 2 of them were discarded. These texts were not fully annotated by the annotators since they were not be able to completely understand which process elements were actually included in some specific parts of the text. For this reason, the final size of the dataset is 45 textual descriptions of the corresponding process models together with their annotations.
  

#### Who are the source language producers?

English

### Annotations

#### Annotation process
You can read about the annotation process in the original paper https://arxiv.org/abs/2203.04860

#### Who are the annotators?

Expert Annotators

### Personal and Sensitive Information

No personal or sensitive information issues.

## Considerations for Using the Data

### Social Impact of Dataset

The dataset has no social impact

### Discussion of Biases

No bias found in the dataset

### Other Known Limitations

The *Further specification* and *AND Gateway* elements obtained very poor performance on the baselines proposed in the paper.
The *AND Gateway* is the less represented process elements in this dataset.
The *Further Specification* process element was the most difficult element to annotate.

## Additional Information

### Dataset Curators

- Patrizio Bellan (Fondazione Bruno Kessler, Trento, Italy and Free University of Bozen-Bolzano, Bolzano, Italy)
- Mauro Dragoni (Fondazione Bruno Kessler, Trento, Italy)
- Chiara Ghidini (Fondazione Bruno Kessler, Trento, Italy)
- Han van der Aa (University of Mannheim, Mannheim, Germany)
- Simone Ponzetto (University of Mannheim, Mannheim, Germany)

### Licensing Information


### Citation Information

```
@article{DBLP:journals/corr/abs-2203-04860,
  author    = {Patrizio Bellan and
               Han van der Aa and
               Mauro Dragoni and
               Chiara Ghidini and
               Simone Paolo Ponzetto},
  title     = {{PET:} {A} new Dataset for Process Extraction from Natural Language
               Text},
  journal   = {CoRR},
  volume    = {abs/2203.04860},
  year      = {2022},
  url       = {https://doi.org/10.48550/arXiv.2203.04860},
  doi       = {10.48550/arXiv.2203.04860},
  eprinttype = {arXiv},
  eprint    = {2203.04860},
  timestamp = {Wed, 16 Mar 2022 16:39:52 +0100},
  biburl    = {https://dblp.org/rec/journals/corr/abs-2203-04860.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```


### Contributions

Thanks to [Patrizio Bellan](https://pdi.fbk.eu/bellan/) for adding this dataset.


####  <a name="updates"></a>Update
- v1.0.0: Added token classification task
- v1.0.1: Added extraction relation task



## <a name="annotationguidelines"></a>Annotation Guidelines

### Inception Schema

The inception schema can be found [here](https://pdi.fbk.eu/pet/inception-schema.json)

### Annotation Guidelines

The Annotation guidelines and procedures adopted to annotate the PET dataset can be downloaded [here](https://pdi.fbk.eu/pet/annotation-guidelines-for-process-description.pdf)

###  Article

The Article can be downloeaded [here](https://doi.org/10.48550/arXiv.2203.04860)

### Python Interface

A python interface (beta version) to interact with the dataset can be found [here](https://pypi.org/project/petdatasetreader/)

### Benchmarks

A python benchmarking procedure to test approaches on the PET dataset will be released soon.


##  <a name="loadingdata"></a>Loading data
### Token-classification task
```python
from datasets import load_dataset
modelhub_dataset = load_dataset("patriziobellan/PET", name='token-classification')
```

### Relations-extraction task
```python
from datasets import load_dataset
modelhub_dataset = load_dataset("patriziobellan/PET", name='relations-extraction')
