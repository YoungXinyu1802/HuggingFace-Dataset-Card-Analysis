---
annotations_creators:
- expert-generated
language_creators:
- machine-generated
language:
- en
license:
- agpl-3.0
multilinguality:
- monolingual
size_categories:
- unknown
source_datasets:
- original
task_categories:
- structure-prediction
task_ids: []
pretty_name: STAN Large
tags:
- word-segmentation
---

# Dataset Card for STAN Large

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
- [Dataset Creation](#dataset-creation)
- [Additional Information](#additional-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Repository:** [mounicam/hashtag_master](https://github.com/mounicam/hashtag_master)
- **Paper:** [Multi-task Pairwise Neural Ranking for Hashtag Segmentation](https://aclanthology.org/P19-1242/)

### Dataset Summary

The description below was taken from the paper "Multi-task Pairwise Neural Ranking for Hashtag Segmentation"
by Maddela et al..

"STAN large, our new expert curated dataset, which includes all 12,594 unique English hashtags and their 
associated tweets from the same Stanford dataset.

STAN small is the most commonly used dataset in previous work. However, after reexamination, we found annotation 
errors in 6.8% of the hashtags in this dataset, which is significant given that the error rate of the state-of-the art 
models is only around 10%. Most of the errors were related to named entities. For example, #lionhead, 
which refers to the “Lionhead” video game company, was labeled as “lion head”.

We therefore constructed the STAN large dataset of 12,594 hashtags with additional quality control for human annotations."

### Languages

English

## Dataset Structure

### Data Instances

```
{
    "index": 15,
    "hashtag": "PokemonPlatinum",
    "segmentation": "Pokemon Platinum",
    "alternatives": {
        "segmentation": [
            "Pokemon platinum"
        ]
    }
}
```

### Data Fields

- `index`: a numerical index.
- `hashtag`: the original hashtag.
- `segmentation`: the gold segmentation for the hashtag.
- `alternatives`: other segmentations that are also accepted as a gold segmentation.

Although `segmentation` has exactly the same characters as `hashtag` except for the spaces, the segmentations inside `alternatives` may have characters corrected to uppercase.

## Dataset Creation

- All hashtag segmentation and identifier splitting datasets on this profile have the same basic fields: `hashtag` and `segmentation` or `identifier` and `segmentation`.

- The only difference between `hashtag` and `segmentation` or between `identifier` and `segmentation` are the whitespace characters. Spell checking, expanding abbreviations or correcting characters to uppercase go into other fields.

- There is always whitespace between an alphanumeric character and a sequence of any special characters ( such as `_` , `:`, `~` ). 

- If there are any annotations for named entity recognition and other token classification tasks, they are given in a `spans` field.

## Additional Information

### Citation Information

```
@inproceedings{maddela-etal-2019-multi,
    title = "Multi-task Pairwise Neural Ranking for Hashtag Segmentation",
    author = "Maddela, Mounica  and
      Xu, Wei  and
      Preo{\c{t}}iuc-Pietro, Daniel",
    booktitle = "Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics",
    month = jul,
    year = "2019",
    address = "Florence, Italy",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/P19-1242",
    doi = "10.18653/v1/P19-1242",
    pages = "2538--2549",
    abstract = "Hashtags are often employed on social media and beyond to add metadata to a textual utterance with the goal of increasing discoverability, aiding search, or providing additional semantics. However, the semantic content of hashtags is not straightforward to infer as these represent ad-hoc conventions which frequently include multiple words joined together and can include abbreviations and unorthodox spellings. We build a dataset of 12,594 hashtags split into individual segments and propose a set of approaches for hashtag segmentation by framing it as a pairwise ranking problem between candidate segmentations. Our novel neural approaches demonstrate 24.6{\%} error reduction in hashtag segmentation accuracy compared to the current state-of-the-art method. Finally, we demonstrate that a deeper understanding of hashtag semantics obtained through segmentation is useful for downstream applications such as sentiment analysis, for which we achieved a 2.6{\%} increase in average recall on the SemEval 2017 sentiment analysis dataset.",
}
```

### Contributions

This dataset was added by [@ruanchaves](https://github.com/ruanchaves) while developing the [hashformers](https://github.com/ruanchaves/hashformers) library.