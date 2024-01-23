---
annotations_creators:
- train: programmatically-generated
- val: programmatically-generated
- test: programmatically-generated, expert-validated
language_creators:
- found
language:
- en
license: 
- other
multilinguality:
- monolingual
size_categories:
- 100K<n<1M
task_categories:
- structure-prediction
task_ids:
- named-entity-recognition
---
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
- **Repository:** [Github](https://github.com/ncats/epi4GARD/tree/master/EpiExtract4GARD#epiextract4gard)
- **Paper:** Pending

### Dataset Summary

EpiSet4NER is a bronze-standard dataset for epidemiological entity recognition of location, epidemiologic types (e.g. "prevalence", "annual incidence", "estimated occurrence"), and epidemiological rates (e.g. "1.7 per 1,000,000 live births", "2.1:1.000.000", "one in five million", "0.03%") created by the [Genetic and Rare Diseases Information Center (GARD)](https://rarediseases.info.nih.gov/), a program in [the National Center for Advancing Translational Sciences](https://ncats.nih.gov/), one of the 27 [National Institutes of Health](https://www.nih.gov/). It was labeled programmatically using spaCy NER and rule-based methods. This weakly-supervised teaching method allowed us to construct this imprecise dataset with minimal manual effort and achieve satisfactory performance on a multi-type token classification problem. The test set was manually corrected by 3 NCATS researchers and a GARD curator (genetic and rare disease expert). It was used to train [EpiExtract4GARD](https://huggingface.co/ncats/EpiExtract4GARD), a BioBERT-based model fine-tuned for NER.

An [example](https://pubmed.ncbi.nlm.nih.gov/24237863/) of 'train' looks as follows.
```
{
    "id": "333",
    "tokens": ['Conclusions', 'The', 'birth', 'prevalence', 'of', 'CLD', 'in', 'the', 'northern', 'Netherlands', 'was', '21.1/10,000', 'births', '.'],
    "ner_tags":  [0, 0, 0, 3, 0, 0, 0, 0, 0, 1, 0, 5, 6, 0],
}
```
### Data Fields

The data fields are the same among all splits.
- `id`: a `string` feature that indicates sentence number.
- `tokens`: a `list` of `string` features.
- `ner_tags`: a `list` of classification labels, with possible values including `O` (0), `B-LOC` (1), `I-LOC` (2), `B-EPI` (3), `I-EPI` (4),`B-STAT` (5),`I-STAT` (6).

### Data Splits

|name |train |validation|test|
|---------|-----:|----:|----:|
|EpiSet \# of abstracts|456|114|50|
|EpiSet \# tokens  |117888|31262|13910|


## Dataset Creation
![EpiSet Creation Flowchart](https://raw.githubusercontent.com/ncats/epi4GARD/master/EpiExtract4GARD/datasets/EpiCustomV3/EpiSet%20Flowchart%20FINAL.png)
*Figure 1:* Creation of EpiSet4NER by NIH/NCATS
Comparing the programmatically labeled test set to the manually corrected test set allowed us to measure the precision, recall, and F1 of the programmatic labeling. 

*Table 1:* Programmatic labeling of EpiSet4NER  

| Evaluation Level |          Entity          | Precision | Recall |   F1  |
|:----------------:|:------------------------:|:---------:|:------:|:-----:|
|   Entity-Level   |          Overall         |   0.559   |  0.662 | 0.606 |
|                  |         Location         |   0.597   |  0.661 | 0.627 |
|                  | Epidemiologic Type       |   0.854   |  0.911 | 0.882 |
|                  |    Epidemiologic Rate    |   0.175   |  0.255 | 0.207 |
|   Token-Level    |          Overall         |   0.805   |  0.710 | 0.755 |
|                  |         Location         |   0.868   |  0.713 | 0.783 |
|                  |    Epidemiologic Type    |   0.908   |  0.908 | 0.908 |
|                  |    Epidemiologic Rate    |   0.739   |  0.645 | 0.689 |

An example of the text labeling:
![Text Labeling](https://raw.githubusercontent.com/ncats/epi4GARD/master/EpiExtract4GARD/datasets/EpiCustomV3/Text%20Labeling4.png)
*Figure 2:* Text Labeling using spaCy and rule-based labeling. Ideal labeling is bolded on the left. Actual programmatic output is on the right. [\[Figure citation\]](https://pubmed.ncbi.nlm.nih.gov/33649778/)

### Curation Rationale

To train ML/DL models that automate the process of rare disease epidemiological curation. This is crucial information to patients & families, researchers, grantors, and policy makers, primarily for funding purposes. 

### Source Data
620 rare disease abstracts classified as epidemiological by a LSTM RNN rare disease epi classifier from 488 diseases. See Figure 1.

#### Initial Data Collection and Normalization

A random sample of 500 disease names were gathered from a list of ~6061 rare diseases tracked by GARD until &ge;50 abstracts had been returned for each disease or the EBI RESTful API results were exhausted. Though we called ~25,000 abstracts from PubMed's db, only 7699 unique abstracts were returned for 488 diseases. Out of 7699 abstracts, only 620 were classified as epidemiological by the LSTM RNN epidemiological classifier.

### Annotations

#### Annotation process

Programmatic labeling. See [here](https://github.com/ncats/epi4GARD/blob/master/EpiExtract4GARD/create_labeled_dataset_V2.ipynb) and then [here](https://github.com/ncats/epi4GARD/blob/master/EpiExtract4GARD/modify_existing_labels.ipynb). The test set was manually corrected after creation. 

#### Who are the annotators?

Programmatic labeling was done by [@William Kariampuzha](https://github.com/wzkariampuzha), one of the NCATS researchers. 
The test set was manually corrected by 2 more NCATS researchers and a GARD curator (genetic and rare disease expert).

### Personal and Sensitive Information

None. These are freely available abstracts from PubMed.

## Considerations for Using the Data

### Social Impact of Dataset

Assisting 25-30 millions Americans with rare diseases. Additionally can be useful for Orphanet or CDC researchers/curators. 

### Discussion of Biases and Limitations

- There were errors in the source file that contained rare disease synonyms of names, which may have led to some unrelated abstracts being included in the training, validation, and test sets. 
- The abstracts were gathered through the EBI API and is thus subject to any biases that the EBI API had. The NCBI API returns very different results as shown by an API analysis here.
- The [long short-term memory recurrent neural network epi classifier](https://pubmed.ncbi.nlm.nih.gov/34457147/) was used to sift the 7699 rare disease abstracts. This model had a hold-out validation F1 score of 0.886 and a test F1 (which was compared against a GARD curator who used full-text articles to determine truth-value of epidemiological abstract) of 0.701. With 620 epi abstracts filtered from 7699 original rare disease abstracts, there are likely several false positives and false negative epi abstracts.
- Tokenization was done by spaCy which may be a limitation (or not) for current and future models trained on this set. 
- The programmatic labeling was very imprecise as seen by Table 1. This is likely the largest limitation of the [BioBERT-based model](https://huggingface.co/ncats/EpiExtract4GARD) trained on this set. 
- The test set was difficult to validate even for general NCATS researchers, which is why we relied on a rare disease expert to verify our modifications. As this task of epidemiological information identification is quite difficult for non-expert humans to complete, this set, and especially a gold-standard dataset in the possible future, represents a challenging gauntlet for NLP systems, especially those focusing on numeracy, to compete on. 

## Additional Information

### Dataset Curators

[NIH GARD](https://rarediseases.info.nih.gov/about-gard/pages/23/about-gard)

### Licensing Information

[More Information Needed]

### Citation Information

[More Information Needed]

### Contributions
Thanks to [@William Kariampuzha](https://github.com/wzkariampuzha) at NCATS/Axle Informatics for adding this dataset.