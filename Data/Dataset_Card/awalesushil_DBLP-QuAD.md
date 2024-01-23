---
annotations_creators:
- expert-generated
language:
- en
language_creators:
- machine-generated
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: 'DBLP-QuAD: A Question Answering Dataset over the DBLP Scholarly Knowledge Graph'
size_categories:
- 1K<n<10K
source_datasets:
- original
tags:
- knowledge-base-qa
task_categories:
- question-answering
task_ids: []
---

# Dataset Card for DBLP-QuAD

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

- **Homepage:** [DBLP-QuAD Homepage]()
- **Repository:** [DBLP-QuAD Repository](https://github.com/awalesushil/DBLP-QuAD)
- **Paper:** DBLP-QuAD: A Question Answering Dataset over the DBLP Scholarly Knowledge Graph
- **Point of Contact:** [Sushil Awale](mailto:sushil.awale@web.de)

### Dataset Summary

DBLP-QuAD is a scholarly knowledge graph question answering dataset with 10,000 question - SPARQL query pairs targeting the DBLP knowledge graph. The dataset is split into 7,000 training, 1,000 validation and 2,000 test questions.

## Dataset Structure

### Data Instances

An example of a question is given below:

```
{
    "id": "Q0577",
    "query_type": "MULTI_FACT",
    "question": {
        "string": "What are the primary affiliations of the authors of the paper 'Graphical Partitions and Graphical Relations'?"
    },
    "paraphrased_question": {
        "string": "List the primary affiliations of the authors of 'Graphical Partitions and Graphical Relations'."
    },
    "query": {
        "sparql": "SELECT DISTINCT ?answer WHERE { <https://dblp.org/rec/journals/fuin/ShaheenS19> <https://dblp.org/rdf/schema#authoredBy> ?x . ?x <https://dblp.org/rdf/schema#primaryAffiliation> ?answer }"
    },
    "template_id": "TP11",
    "entities": [
        "<https://dblp.org/rec/journals/fuin/ShaheenS19>"
    ],
    "relations": [
        "<https://dblp.org/rdf/schema#authoredBy>",
        "<https://dblp.org/rdf/schema#primaryAffiliation>"
    ],
    "temporal": false,
    "held_out": true
}

```
### Data Fields

- `id`: the id of the question
- `question`: a string containing the question
- `paraphrased_question`: a paraphrased version of the question
- `query`: a SPARQL query that answers the question
- `query_type`: the type of the query
- `query_template`: the template of the query
- `entities`: a list of entities in the question
- `relations`: a list of relations in the question
- `temporal`: a boolean indicating whether the question contains a temporal expression
- `held_out`: a boolean indicating whether the question is held out from the training set

### Data Splits

The dataset is split into 7,000 training, 1,000 validation and 2,000 test questions.

## Additional Information

### Licensing Information

DBLP-QuAD is licensed under the [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

### Citation Information

In review.

### Contributions

Thanks to [@awalesushil](https://github.com/awalesushil) for adding this dataset.
