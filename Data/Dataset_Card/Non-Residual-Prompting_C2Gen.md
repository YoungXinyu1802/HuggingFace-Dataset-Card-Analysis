---
language:
- en
license:
- cc-by-sa-4.0
size_categories:
- <100K
task_categories:
- text-generation
---
# Dataset Card for Contextualized CommonGen(C2Gen)

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-instances)
  - [Data Splits](#data-instances)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Initial Data Collection and Normalization](#initial-cata-collection-and-normalization)
- [Licensing Information](#licensing-information)
 

## Dataset Description

- **Repository:** [Non-Residual Prompting](https://github.com/FreddeFrallan/Non-Residual-Prompting)
- **Paper:** [Fine-Grained Controllable Text Generation Using Non-Residual Prompting](https://aclanthology.org/2022.acl-long.471)
- **Point of Contact:** [Fredrik Carlsson](mailto:Fredrik.Carlsson@ri.se)


### Dataset Summary

CommonGen [Lin et al., 2020](https://arxiv.org/abs/1911.03705) is a dataset for the constrained text generation task of word inclusion. But the task does not allow to include context. Therefore, to complement CommonGen, we provide an extended test set C2Gen [Carlsson et al., 2022](https://aclanthology.org/2022.acl-long.471) where an additional context is provided for each set of target words. The task is therefore reformulated to both generate commonsensical text which include the given words, and also have the generated text adhere to the given context.

### Languages

English

## Dataset Structure

### Data Instances

{"Context": "The show came on the television with people singing. The family all gathered to watch. They all became silent when the show came on.", "Words": ["follow", "series", "voice"]}

### Data Fields

- context: the generated text by the model should adhere to this text
- words: the words that should be included in the generated continuation

### Data Splits

Test

## Dataset Creation

### Curation Rationale

C2Gen was created because the authors of the paper believed that the task formulation of CommonGen is too narrow, and that it needlessly incentivizes researchers
to focus on methods that do not support context. Which is orthogonal to their belief that many application areas necessitates the consideration of surrounding context. Therefore, to complement CommonGen, they provide an extended test set where an additional context is provided for each set of target words.

### Initial Data Collection and Normalization

The dataset was constructed with the help the crowd sourcing platform MechanicalTurk. Each remaining concept set manually received a textual context. To assure the quality of the data generation, only native English speakers with a recorded high acceptance were allowed to participate. Finally, all contexts were manually verified, and fixed in terms of typos and poor quality. Furthermore we want to raise awareness that C2GEN can contain personal data or offensive content. If you would encounter such a sample, please reach out to us.

## Licensing Information

license: cc-by-sa-4.0
