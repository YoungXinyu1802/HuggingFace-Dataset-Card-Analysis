---
annotations_creators: []
language_creators:
- other
language:
- en
license:
- other
multilinguality:
- monolingual
size_categories:
- unknown
source_datasets: []
task_categories:
- text-retrieval
- text-generation
task_ids:
- text-simplification
- parsing
pretty_name: deepa2
tags:
- argument-mining
- summarization
- conditional-text-generation
- structure-prediction
---

# `deepa2` Datasets Collection 

## Table of Contents
- [`deepa2` Datasets Collection](#deepa2-datasets-collection)
  - [Table of Contents](#table-of-contents)
  - [Dataset Description](#dataset-description)
    - [Dataset Summary](#dataset-summary)
    - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
    - [Languages](#languages)
  - [Dataset Structure](#dataset-structure)
    - [Sub-Datasets](#sub-datasets)
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

- **Homepage:** [blog post](https://debatelab.github.io/journal/deepa2.html)
- **Repository:** [github](https://github.com/debatelab/deepa2)
- **Paper:** [arxiv](https://arxiv.org/abs/2110.01509)
- **Point of Contact:** [Gregor Betz](gregor.betz@kit.edu)

### Dataset Summary

This is a growing, curated collection of `deepa2` datasets, i.e. datasets that contain comprehensive logical analyses of argumentative texts. The collection comprises: 

* datasets that are built from existing NLP datasets by means of the [`deepa2 bake`](https://github.com/debatelab/deepa2) tool.
* original `deepa2` datasets specifically created for this collection.

The tool [`deepa2 serve`](https://github.com/debatelab/deepa2#integrating-deepa2-into-your-training-pipeline) may be used to render the data in this collection as text2text examples.  

### Supported Tasks and Leaderboards

For each of the tasks tagged for this dataset, give a brief description of the tag, metrics, and suggested models (with a link to their HuggingFace implementation if available). Give a similar description of tasks that were not covered by the structured tag set (repace the `task-category-tag` with an appropriate `other:other-task-name`).

- `conditional-text-generation`: The dataset can be used to train models to generate a fully reconstruction of an argument from a source text, making, e.g., its implicit assumptions explicit.
- `structure-prediction`: The dataset can be used to train models to formalize sentences.
- `text-retrieval`:  The dataset can be used to train models to extract reason statements and conjectures from a given source text.

### Languages

English. Will be extended to cover other languages in the futures.

## Dataset Structure

### Sub-Datasets

This collection contains the following `deepa2` datasets:

* `esnli`: created from e-SNLI with `deepa2 bake` as [described here](https://github.com/debatelab/deepa2/blob/main/docs/esnli.md).
* `enbank` (`task_1`, `task_2`): created from Entailment Bank with `deepa2 bake` as [described here](https://github.com/debatelab/deepa2/blob/main/docs/enbank.md).
* `argq`: created from IBM-ArgQ with `deepa2 bake` as [described here](https://github.com/debatelab/deepa2/blob/main/docs/argq.md).
* `argkp`: created from IBM-KPA with `deepa2 bake` as [described here](https://github.com/debatelab/deepa2/blob/main/docs/argkp.md).
* `aifdb` (`moral-maze`, `us2016`, `vacc-itc`): created from AIFdb with `deepa2 bake` as [described here](https://github.com/debatelab/deepa2/blob/main/docs/aifdb.md).
* `aaac` (`aaac01` and `aaac02`): original, machine-generated contribution; based on an an improved and extended algorithm that backs https://huggingface.co/datasets/debatelab/aaac.

### Data Instances

see: https://github.com/debatelab/deepa2/tree/main/docs

### Data Fields

see: https://github.com/debatelab/deepa2/tree/main/docs

|feature|esnli|enbank|aifdb|aaac|argq|argkp|
|--|--|--|--|--|--|--|
| `source_text` | x | x | x | x | x | x |  
| `title` |   | x |   | x |   |   |
| `gist` | x | x |   | x |   | x |
| `source_paraphrase` | x | x | x | x |   |   |
| `context` |   | x |   | x |   | x |
| `reasons` | x | x | x | x | x |   |
| `conjectures` | x | x | x | x | x |   |
| `argdown_reconstruction` | x | x |   | x |   | x |
| `erroneous_argdown` | x |   |   | x |   |   |
| `premises` | x | x |   | x |   | x |
| `intermediary_conclusion` |   |   |   | x |   |   |
| `conclusion` | x | x |   | x |   | x |
| `premises_formalized` | x |   |   | x |   | x |
| `intermediary_conclusion_formalized` |   |   |   | x |   |   |
| `conclusion_formalized` | x |   |   | x |   | x |
| `predicate_placeholders` |   |   |   | x |   |   |
| `entity_placeholders` |   |   |   | x |   |   |
| `misc_placeholders` | x |   |   | x |   | x |
| `plchd_substitutions` | x |   |   | x |   | x |

### Data Splits

Each sub-dataset contains three splits: `train`, `validation`, and `test`.

## Dataset Creation

### Curation Rationale

Many NLP datasets focus on tasks that are relevant for logical analysis and argument reconstruction. This collection is the attempt to unify these resources in a common framework.

### Source Data

See: [Sub-Datasets](#sub-datasets)

## Additional Information

### Dataset Curators

Gregor Betz, KIT; Kyle Richardson, Allen AI

### Licensing Information

We re-distribute the the imported sub-datasets under their original license:

|Sub-dataset|License|
|--|--|
|esnli|MIT|
|aifdb|free for academic use ([TOU](https://arg-tech.org/index.php/research/argument-corpora/))|
|enbank|CC BY 4.0|
|aaac|CC BY 4.0|
|argq|CC BY SA 4.0|
|argkp|Apache|

### Citation Information

```
@article{betz2021deepa2,
      title={DeepA2: A Modular Framework for Deep Argument Analysis with Pretrained Neural Text2Text Language Models}, 
      author={Gregor Betz and Kyle Richardson},
      year={2021},
      eprint={2110.01509},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

<!--If the dataset has a [DOI](https://www.doi.org/), please provide it here.-->

