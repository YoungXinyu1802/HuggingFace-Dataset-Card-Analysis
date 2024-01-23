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
pretty_name: 'BAAD16: Bangla Authorship Attribution Dataset (16 Authors)'
source_datasets:
- original
task_categories:
- text-classification
task_ids:
- multi-class-classification

---

## Description

**BAAD16** is an **Authorship Attribution dataset for Bengali Literature**. It was collected and analyzed by the authors of [this paper](https://arxiv.org/abs/2001.05316). It was created by scraping text from an online Bangla e-library using custom web crawler and contains literary works of various famous Bangla writers. It contains novels, stories, series, and other works of 16 authors. Each sample document is created with 750 words. The dataset is imbalanced and resembles real-world scenarios more closely, where not all the authors will have a large number of sample texts. The following table gives more details about the dataset.

| Author Name | Number of Samples | Word Count | Unique Word
| --- | --- | --- | --- |
| zahir rayhan        | 185              | 138k | 20k
|nazrul               | 223              | 167k | 33k
|manik bandhopaddhay  | 469              | 351k | 44k
|nihar ronjon gupta   | 476              | 357k | 43k
|bongkim              | 562              | 421k | 62k
|tarashonkor          | 775              | 581k | 84k
|shottojit roy        | 849              | 636k | 67k
|shordindu            | 888              | 666k | 84k
|toslima nasrin       | 931              | 698k | 76k
|shirshendu           | 1048             | 786k | 69k
|zafar iqbal          | 1100             | 825k | 53k
|robindronath         | 1259             | 944k | 89k
|shorotchandra        | 1312             | 984k | 78k
|shomresh             | 1408             | 1056k|69k
|shunil gongopaddhay  | 1963             | 1472k|109k
|humayun ahmed        | 4518             | 3388k |161k
**Total**| 17,966|13,474,500 | 590,660
**Average**|1,122.875|842,156.25| 71,822.25
    

## Citation

If you use this dataset, please cite the paper [Authorship Attribution in Bangla literature using Character-level CNN](https://ieeexplore.ieee.org/abstract/document/9038560/). [Archive link](https://arxiv.org/abs/2001.05316).
```
 @inproceedings{BAAD16Dataset,
  title={Authorship Attribution in Bangla literature using Character-level CNN},
  author={Khatun, Aisha and Rahman, Anisur and Islam, Md Saiful and others},
  booktitle={2019 22nd International Conference on Computer and Information Technology (ICCIT)},
  pages={1--5},
  year={2019},
  organization={IEEE}
  doi={10.1109/ICCIT48885.2019.9038560}
}
 ```
 
This dataset is also available in Mendeley: [BAAD16 dataset](https://data.mendeley.com/datasets/6d9jrkgtvv/4). Always make sure to use the latest version of the dataset. Cite the dataset directly by:
```
@misc{BAAD6Dataset,
  author = {Khatun, Aisha and Rahman, Anisur and Islam, Md. Saiful},
  title = {BAAD16: Bangla Authorship Attribution Dataset},
  year={2019},
  doi = {10.17632/6d9jrkgtvv.4},
  howpublished= {\url{https://data.mendeley.com/datasets/6d9jrkgtvv/4}}
  } 
```