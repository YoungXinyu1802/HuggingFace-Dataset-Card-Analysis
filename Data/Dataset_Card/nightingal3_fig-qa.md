---
annotations_creators:
- expert-generated
- crowdsourced
language_creators:
- crowdsourced
language:
- en
license:
- mit
multilinguality:
- monolingual
pretty_name: Fig-QA
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories:
- multiple-choice
task_ids:
- multiple-choice-qa
---

# Dataset Card for Fig-QA

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Splits](#data-splits)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Discussion of Biases](#discussion-of-biases)
- [Additional Information](#additional-information)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)

## Dataset Description

- **Repository:** https://github.com/nightingal3/Fig-QA 
- **Paper:** https://arxiv.org/abs/2204.12632
- **Leaderboard:** https://explainaboard.inspiredco.ai/leaderboards?dataset=fig_qa
- **Point of Contact:** emmy@cmu.edu

### Dataset Summary

This is the dataset for the paper [Testing the Ability of Language Models to Interpret Figurative Language](https://arxiv.org/abs/2204.12632). Fig-QA consists of 10256 examples of human-written creative metaphors that are paired as a Winograd schema. It can be used to evaluate the commonsense reasoning of models. The metaphors themselves can also be used as training data for other tasks, such as metaphor detection or generation. 

### Supported Tasks and Leaderboards

You can evaluate your models on the test set by submitting to the [leaderboard](https://explainaboard.inspiredco.ai/leaderboards?dataset=fig_qa) on Explainaboard. Click on "New" and select `qa-multiple-choice` for the task field. Select `accuracy` for the metric. You should upload results in the form of a system output file in JSON or JSONL format. 

### Languages

English only currently

### Data Splits

Train-{S, M(no suffix), XL}: different training set sizes
Dev
Test (labels not provided for test set)

## Considerations for Using the Data

### Discussion of Biases

These metaphors are human-generated and may contain insults or other explicit content. Authors of the paper manually removed offensive content, but users should keep in mind that some potentially offensive content may remain in the dataset.

## Additional Information

### Licensing Information

MIT License

### Citation Information

If you found the dataset useful, please cite this paper:

    @misc{https://doi.org/10.48550/arxiv.2204.12632,
      doi = {10.48550/ARXIV.2204.12632},
      url = {https://arxiv.org/abs/2204.12632},
      author = {Liu, Emmy and Cui, Chen and Zheng, Kenneth and Neubig, Graham},
      keywords = {Computation and Language (cs.CL), Artificial Intelligence (cs.AI), FOS: Computer and information sciences, FOS: Computer and information sciences},
      title = {Testing the Ability of Language Models to Interpret Figurative Language},
      publisher = {arXiv},
      year = {2022},
      copyright = {Creative Commons Attribution Share Alike 4.0 International}
    }
  