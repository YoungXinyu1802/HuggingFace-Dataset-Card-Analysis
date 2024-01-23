---
annotations_creators:
- expert-generated
language:
- en
language_creators:
- found
license:
- gpl-3.0
multilinguality:
- monolingual
paperswithcode_id: semi-supervised-exaggeration-detection-of
pretty_name: Scientific Exaggeration Detection
size_categories:
- n<1K
source_datasets: []
tags:
- scientific text
- scholarly text
- inference
- fact checking
- misinformation
task_categories:
- text-classification
task_ids:
- natural-language-inference
- multi-input-text-classification
---

# Dataset Card for Scientific Exaggeration Detection

## Dataset Description

- **Homepage:** https://github.com/copenlu/scientific-exaggeration-detection
- **Repository:** https://github.com/copenlu/scientific-exaggeration-detection
- **Paper:** https://aclanthology.org/2021.emnlp-main.845.pdf

### Dataset Summary

Public trust in science depends on honest and factual communication of scientific papers. However, recent studies have demonstrated a tendency of news media to misrepresent scientific papers by exaggerating their findings. Given this, we present a formalization of and study into the problem of exaggeration detection in science communication. While there are an abundance of scientific papers and popular media articles written about them, very rarely do the articles include a direct link to the original paper, making data collection challenging. We address this by curating a set of labeled press release/abstract pairs from existing expert annotated studies on exaggeration in press releases of scientific papers suitable for benchmarking the performance of machine learning models on the task. Using limited data from this and previous studies on exaggeration detection in science, we introduce MT-PET, a multi-task version of Pattern Exploiting Training (PET), which leverages knowledge from complementary cloze-style QA tasks to improve few-shot learning. We demonstrate that MT-PET outperforms PET and supervised learning both when data is limited, as well as when there is an abundance of data for the main task.

## Dataset Structure

The training and test data are derived from the InSciOut studies from [Sumner et al. 2014](https://www.bmj.com/content/349/bmj.g7015) and [Bratton et al. 2019](https://pubmed.ncbi.nlm.nih.gov/31728413/#:~:text=Results%3A%20We%20found%20that%20the,inference%20from%20non%2Dhuman%20studies.). The splits have the following fields:

```
original_file_id: The ID of the original spreadsheet in the Sumner/Bratton data where the annotations are derived from
press_release_conclusion: The conclusion sentence from the press release
press_release_strength: The strength label for the press release
abstract_conclusion: The conclusion sentence from the abstract
abstract_strength: The strength label for the abstract
exaggeration_label: The final exaggeration label
```

The exaggeration label is one of `same`, `exaggerates`, or `downplays`. The strength label is one of the following:

```
0: Statement of no relationship
1: Statement of correlation
2: Conditional statement of causation
3: Statement of causation
```

## Dataset Creation

See section 4 of the [paper](https://aclanthology.org/2021.emnlp-main.845.pdf) for details on how the dataset was curated. The original InSciOut data can be found [here](https://figshare.com/articles/dataset/InSciOut/903704)

## Citation

```
@inproceedings{wright2021exaggeration,
    title={{Semi-Supervised Exaggeration Detection of Health Science Press Releases}},
    author={Dustin Wright and Isabelle Augenstein},
    booktitle = {Proceedings of EMNLP},
    publisher = {Association for Computational Linguistics},
    year = 2021
}
```


Thanks to [@dwright37](https://github.com/dwright37) for adding this dataset.