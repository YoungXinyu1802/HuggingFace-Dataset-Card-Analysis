---
annotations_creators:
- expert-generated
- crowdsourced
language:
- en
language_creators:
- found
- crowdsourced
- expert-generated
license:
- c-uda
multilinguality:
- monolingual
paperswithcode_id: totto
pretty_name: HiTab
size_categories:
- 10K<n<100K
source_datasets:
- original
- extended|totto
tags: []
task_categories:
- table-to-text
- question-answering
task_ids: []
dataset_info:
  features:
  - name: id
    dtype: string
  - name: table_id
    dtype: string
  - name: table_source
    dtype: string
  - name: sentence_id
    dtype: string
  - name: sub_sentence_id
    dtype: string
  - name: sub_sentence
    dtype: string
  - name: question
    dtype: string
  - name: answer
    dtype: large_string
  - name: aggregation
    dtype: large_string
  - name: linked_cells
    dtype: large_string
  - name: answer_formulas
    dtype: large_string
  - name: reference_cells_map
    dtype: large_string
  - name: table_content
    dtype: large_string
  splits:
  - name: train
    num_bytes: 36419103
    num_examples: 7417
  - name: validation
    num_bytes: 8312699
    num_examples: 1671
  - name: test
    num_bytes: 7710891
    num_examples: 1584
  download_size: 6462957
  dataset_size: 52442693
---

# Dataset Card for HiTab

## Dataset Description
- **Homepage:** https://www.microsoft.com/en-us/research/publication/hitab-a-hierarchical-table-dataset-for-question-answering-and-natural-language-generation/
- **Repository:** https://github.com/microsoft/HiTab/blob/main/LICENSE
- **Paper:** https://aclanthology.org/2022.acl-long.78/

### Dataset Summary
HiTab is a dataset for question answering and data-to-text over hierarchical tables . It contains 10,672 samples and 3,597 tables from statistical reports (StatCan, NSF) and Wikipedia (ToTTo). 98.1% of the tables in HiTab are with hierarchies.

### Supported Tasks and Leaderboards
Table-to-Text Generation, Question Answering

### Languages
English

### Data Instances
3,597 tables, 10,686 sentences

### Data Splits
train, test, validation

## Dataset Creation
During the dataset annotation process, annotators first manually collect tables and descriptive sentences highly-related to tables on statistical websites written by professional analysts. Then these descriptions are revised to questions to preserve the original meanings and analyses.

### Licensing Information

This dataset follows the Computational Use of Data Agreement v1.0.

### Citation Information

```
@article{cheng2021hitab,
  title={HiTab: A Hierarchical Table Dataset for Question Answering and Natural Language Generation},
  author={Cheng, Zhoujun and Dong, Haoyu and Wang, Zhiruo and Jia, Ran and Guo, Jiaqi and Gao, Yan and Han, Shi and Lou, Jian-Guang and Zhang, Dongmei},
  journal={arXiv preprint arXiv:2108.06712},
  year={2021}
}