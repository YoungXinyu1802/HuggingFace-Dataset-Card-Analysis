---
license: cc-by-sa-4.0
task_categories:
- text-classification
language:
- en
size_categories:
- 10K<n<100K
---
# squad_v2_factuality_v1
This dataset is derived from "squad_v2" training "context" with the following steps.
1. NER is run to extract entities.
2. Lexicon of person's name, date, organisation name and location are collected.
3. 20% of the time, one of the text attribute (person's name, date, organisation name and location) is randomly replaced. For consistency of context, all other place with the same name is also replaced.

 # Purpose of the Dataset
 The purpose of this dataset is to assess if a language model could detect factuality.