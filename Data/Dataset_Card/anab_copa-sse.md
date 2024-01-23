---
annotations_creators:
- crowdsourced
language:
- en
language_creators:
- crowdsourced
license:
- mit
multilinguality:
- monolingual
pretty_name: Semi-structured Explanations for Commonsense Reasoning
size_categories:
- 1K<n<10K
source_datasets: []
tags:
- commonsense reasoning
- explanation
- graph-based reasoning
task_categories:
- text2text-generation
- multiple-choice
task_ids:
- explanation-generation
---

# Dataset Card for COPA-SSE

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

- **Homepage:** https://github.com/a-brassard/copa-sse
- **Paper:** [COPA-SSE: Semi-Structured Explanations for Commonsense Reasoning](https://arxiv.org/abs/2201.06777)
- **Point of Contact:** [Ana Brassard](mailto:ana.brassard@riken.jp)

### Dataset Summary

![Crowdsourcing protocol](crowdsourcing_protocol.png)

COPA-SSE contains crowdsourced explanations for the [Balanced COPA](https://balanced-copa.github.io/) dataset, a variant of the [Choice of Plausible Alternatives (COPA)](https://people.ict.usc.edu/~gordon/copa.html) benchmark. The explanations are formatted as a set of triple-like common sense statements with [ConceptNet](https://conceptnet.io/) relations but freely written concepts.

### Supported Tasks and Leaderboards

Can be used to train a model for explain+predict or predict+explain settings. Suited for both text-based and graph-based architectures. Base task is COPA (causal QA).

### Languages

English

## Dataset Structure

### Data Instances

Validation and test set each contains Balanced COPA samples with added explanations in `.jsonl` format. The question ids match the original questions of the Balanced COPA validation and test sets, respectively.

### Data Fields
Each entry contains:
- the original question (matching format and ids)
- `human-explanations`: a list of explanations each containing:
    - `expl-id`: the explanation id
    - `text`: the explanation in plain text (full sentences)
    - `worker-id`: anonymized worker id (the author of the explanation)   
    - `worker-avg`: the average score the author got for their explanations
    - `all-ratings`: all collected ratings for the explanation
    - `filtered-ratings`: ratings excluding those that failed the control
    - `triples`: the triple-form explanation (a list of ConceptNet-like triples)

Example entry:
```
id: 1, 
asks-for: cause, 
most-plausible-alternative: 1,
p: "My body cast a shadow over the grass.", 
a1: "The sun was rising.", 
a2: "The grass was cut.", 
human-explanations: [
    {expl-id: f4d9b407-681b-4340-9be1-ac044f1c2230, 
     text: "Sunrise causes casted shadows.", 
     worker-id: 3a71407b-9431-49f9-b3ca-1641f7c05f3b, 
     worker-avg: 3.5832864694635025, 
     all-ratings: [1, 3, 3, 4, 3], 
     filtered-ratings: [3, 3, 4, 3], 
     filtered-avg-rating: 3.25, 
     triples: [["sunrise", "Causes", "casted shadows"]]
     }, ...]
```

### Data Splits

Follows original Balanced COPA split: 1000 dev and 500 test instances. Each instance has up to nine explanations.

## Dataset Creation

### Curation Rationale

The goal was to collect human-written explanations to supplement an existing commonsense reasoning benchmark. The triple-like format was designed to support graph-based models and increase the overall data quality, the latter being notoriously lacking in freely-written crowdsourced text.

### Source Data

#### Initial Data Collection and Normalization

The explanations in COPA-SSE are fully crowdsourced via the Amazon Mechanical Turk platform. Workers entered explanations by providing one or more concept-relation-concept triples. The explanations were then rated by different annotators with one- to five-star ratings. The final dataset contains explanations with a range of quality ratings. Additional collection rounds guaranteed that each sample has at least one explanation rated 3.5 stars or higher.  


#### Who are the source language producers?

The original COPA questions (500 dev+500 test) were initially hand-crafted by experts. Similarly, the additional 500 development samples in Balanced COPA were authored by a small team of NLP researchers. Finally, the added explanations and quality ratings in COPA-SSE were collected with the help of Amazon Mechanical Turk workers who passed initial qualification rounds.

### Annotations

#### Annotation process

Workers were shown a Balanced COPA question, its answer, and a short instructional text. Then, they filled in free-form text fields for head and tail concepts and selected the relation from a drop-down menu with a curated selection of ConceptNet relations. Each explanation was rated by five different workers who were shown the same question and answer with five candidate explanations. 

#### Who are the annotators?

The workers were restricted to persons located in the U.S. or G.B., with a HIT approval of 98% or more, and 500 or more approved HITs. Their identity and further personal information are not available.

### Personal and Sensitive Information

N/A

## Considerations for Using the Data

### Social Impact of Dataset

Models trained to output similar explanations as those in COPA-SSE may not necessarily provide convincing or faithful explanations. Researchers should carefully evaluate the resulting explanations before considering any real-world applications.

### Discussion of Biases

COPA questions ask for causes or effects of everyday actions or interactions, some of them containing gendered language. Some explanations may reinforce harmful stereotypes if their reasoning is based on biased assumptions. These biases were not verified during collection. 

### Other Known Limitations

The data was originally intended to be explanation *graphs*, i.e., hypothetical "ideal" subgraphs of a commonsense knowledge graph. While they can still function as valid natural language explanations, their wording may be at times unnatural to a human and may be better suited for graph-based implementations.

## Additional Information

### Dataset Curators

This work was authored by Ana Brassard, Benjamin Heinzerling, Pride Kavumba, and Kentaro Inui. All are both members of the Riken AIP Natural Language Understanding Team and the Tohoku NLP Lab under Tohoku University.

### Licensing Information

COPA-SSE is released under the [MIT License](https://mit-license.org/).

### Citation Information

```
@InProceedings{copa-sse:LREC2022,
  author    = {Brassard, Ana  and  Heinzerling, Benjamin  and  Kavumba, Pride  and  Inui, Kentaro},
  title     = {COPA-SSE: Semi-structured Explanations for Commonsense Reasoning},
  booktitle      = {Proceedings of the Language Resources and Evaluation Conference},
  month          = {June},
  year           = {2022},
  address        = {Marseille, France},
  publisher      = {European Language Resources Association},
  pages     = {3994--4000},
  url       = {https://aclanthology.org/2022.lrec-1.425}
}

```

### Contributions

Thanks to [@a-brassard](https://github.com/a-brassard) for adding this dataset.