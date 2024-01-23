---
license: cc-by-4.0
task_categories:
- text-generation
language:
- en
- da
- de
- es
- hr
- it
- nl
- sl
- sr
- tr
- id
size_categories:
- 100K<n<1M
---


# Dataset Card Creation Guide

## Table of Contents
- [Dataset Card Creation Guide](#dataset-card-creation-guide)
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

- **Homepage:** [http://noisy-text.github.io/2021/multi-lexnorm.html]()
- **Paper:** [https://aclanthology.org/2021.wnut-1.55/]()

### Dataset Summary

This is the huggingface version of the MultiLexnorm dataset. 

I'm not affiliated with the creators, I'm just releasing the files in an easier-to-access format after processing.


### Citation Information
```
@inproceedings{van-der-goot-etal-2021-multilexnorm,
    title = "{M}ulti{L}ex{N}orm: A Shared Task on Multilingual Lexical Normalization",
    author = {van der Goot, Rob  and
      Ramponi, Alan  and
      Zubiaga, Arkaitz  and
      Plank, Barbara  and
      Muller, Benjamin  and
      San Vicente Roncal, I{\~n}aki  and
      Ljube{\v{s}}i{\'c}, Nikola  and
      {\c{C}}etino{\u{g}}lu, {\"O}zlem  and
      Mahendra, Rahmad  and
      {\c{C}}olako{\u{g}}lu, Talha  and
      Baldwin, Timothy  and
      Caselli, Tommaso  and
      Sidorenko, Wladimir},
    booktitle = "Proceedings of the Seventh Workshop on Noisy User-generated Text (W-NUT 2021)",
    month = nov,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.wnut-1.55",
    doi = "10.18653/v1/2021.wnut-1.55",
    pages = "493--509",
    abstract = "Lexical normalization is the task of transforming an utterance into its standardized form. This task is beneficial for downstream analysis, as it provides a way to harmonize (often spontaneous) linguistic variation. Such variation is typical for social media on which information is shared in a multitude of ways, including diverse languages and code-switching. Since the seminal work of Han and Baldwin (2011) a decade ago, lexical normalization has attracted attention in English and multiple other languages. However, there exists a lack of a common benchmark for comparison of systems across languages with a homogeneous data and evaluation setup. The MultiLexNorm shared task sets out to fill this gap. We provide the largest publicly available multilingual lexical normalization benchmark including 13 language variants. We propose a homogenized evaluation setup with both intrinsic and extrinsic evaluation. As extrinsic evaluation, we use dependency parsing and part-of-speech tagging with adapted evaluation metrics (a-LAS, a-UAS, and a-POS) to account for alignment discrepancies. The shared task hosted at W-NUT 2021 attracted 9 participants and 18 submissions. The results show that neural normalization systems outperform the previous state-of-the-art system by a large margin. Downstream parsing and part-of-speech tagging performance is positively affected but to varying degrees, with improvements of up to 1.72 a-LAS, 0.85 a-UAS, and 1.54 a-POS for the winning system.",
}
```


### Contributions

Thanks to [@larrylawl](https://github.com/larrylawl) for adding this dataset.
