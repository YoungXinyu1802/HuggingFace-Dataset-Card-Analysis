---
annotations_creators:
- expert-generated
language_creators:
- machine-generated
language:
- en
license:
- unknown
multilinguality:
- monolingual
size_categories:
- unknown
source_datasets:
- original
task_categories:
- structure-prediction
task_ids: []
pretty_name: Dev-Stanford
tags:
- word-segmentation
---

# Dataset Card for Dev-Stanford

## Dataset Description

- **Repository:** [ardax/hashtag-segmentor](https://github.com/ardax/hashtag-segmentor)
- **Paper:** [Segmenting Hashtags and Analyzing Their Grammatical Structure](https://asistdl.onlinelibrary.wiley.com/doi/epdf/10.1002/asi.23989?author_access_token=qbKcE1jrre5nbv_Tn9csbU4keas67K9QMdWULTWMo8NOtY2aA39ck2w5Sm4ePQ1MZhbjCdEuaRlPEw2Kd12jzvwhwoWP0fdroZAwWsmXHPXxryDk_oBCup1i9_VDNIpU)

### Dataset Summary

1000 hashtags manually segmented by Çelebi et al. for development purposes, 
randomly selected from the Stanford Sentiment Tweet Corpus by Sentiment140.

### Languages

English

## Dataset Structure

### Data Instances

```
{
    "index": 15,
    "hashtag": "marathonmonday",
    "segmentation": "marathon monday"
}
```

### Data Fields

- `index`: a numerical index.
- `hashtag`: the original hashtag.
- `segmentation`: the gold segmentation for the hashtag.

## Dataset Creation

- All hashtag segmentation and identifier splitting datasets on this profile have the same basic fields: `hashtag` and `segmentation` or `identifier` and `segmentation`.

- The only difference between `hashtag` and `segmentation` or between `identifier` and `segmentation` are the whitespace characters. Spell checking, expanding abbreviations or correcting characters to uppercase go into other fields.

- There is always whitespace between an alphanumeric character and a sequence of any special characters ( such as `_` , `:`, `~` ). 

- If there are any annotations for named entity recognition and other token classification tasks, they are given in a `spans` field.

## Additional Information

### Citation Information

```
@article{celebi2018segmenting,
  title={Segmenting hashtags and analyzing their grammatical structure},
  author={Celebi, Arda and {\"O}zg{\"u}r, Arzucan},
  journal={Journal of the Association for Information Science and Technology},
  volume={69},
  number={5},
  pages={675--686},
  year={2018},
  publisher={Wiley Online Library}
}
```

### Contributions

This dataset was added by [@ruanchaves](https://github.com/ruanchaves) while developing the [hashformers](https://github.com/ruanchaves/hashformers) library.