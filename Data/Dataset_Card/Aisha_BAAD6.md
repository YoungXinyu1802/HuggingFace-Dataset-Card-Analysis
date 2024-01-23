---
annotations_creators:
- found
- crowdsourced
- expert-generated
language_creators:
- found
- crowdsourced
language:
- bn
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: 'BAAD6: Bangla Authorship Attribution Dataset (6 Authors)'
size_categories:
- unknown
source_datasets:
- original
task_categories:
- text-classification
task_ids:
- multi-class-classification
---

## Description

**BAAD6** is an **Authorship Attribution dataset for Bengali Literature**. It was collected and analyzed by Hemayet et al [[1]](https://ieeexplore.ieee.org/document/8631977). The data was obtained from different online posts and blogs. This dataset is balanced among the 6 Authors with 350 sample texts per author. This is a relatively small dataset but is noisy given the sources it was collected from and its cleaning procedure. Nonetheless, it may help evaluate authorship attribution systems as it resembles texts often available on the Internet. Details about the dataset are given in the table below.

| Author | Samples | Word count | Unique word |
| ------ | ------ | ------ | ------ |
|fe|350|357k|53k|
| ij | 350 | 391k | 72k
| mk | 350 | 377k | 47k
| rn | 350 | 231k | 50k
| hm | 350 | 555k | 72k
| rg | 350 | 391k | 58k
**Total** | 2,100 | 2,304,338 | 230,075
**Average** | 350 | 384,056.33 | 59,006.67

## Citation

If you use this dataset, please cite the paper [A Comparative Analysis of Word Embedding Representations in Authorship Attribution of Bengali Literature](https://ieeexplore.ieee.org/document/8631977).

```
@INPROCEEDINGS{BAAD6Dataset,
  author={Ahmed Chowdhury, Hemayet and Haque Imon, Md. Azizul and Islam, Md. Saiful},
  booktitle={2018 21st International Conference of Computer and Information Technology (ICCIT)}, 
  title={A Comparative Analysis of Word Embedding Representations in Authorship Attribution of Bengali Literature}, 
  year={2018},
  volume={},
  number={},
  pages={1-6},
  doi={10.1109/ICCITECHN.2018.8631977}
  }
 ```
 
This dataset is also available in Mendeley: [BAAD6 dataset](https://data.mendeley.com/datasets/w9wkd7g43f/5). Always make sure to use the latest version of the dataset. Cite the dataset directly by:

```
@misc{BAAD6Dataset,
  author = {Ahmed Chowdhury, Hemayet and Haque Imon, Md. Azizul and Khatun, Aisha and Islam, Md. Saiful},
  title = {BAAD6: Bangla Authorship Attribution Dataset},
  year={2018},
  doi = {10.17632/w9wkd7g43f.5},
  howpublished= {\url{https://data.mendeley.com/datasets/w9wkd7g43f/5}}
  } 
```