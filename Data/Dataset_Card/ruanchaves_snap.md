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
pretty_name: SNAP
tags:
- word-segmentation
---

# Dataset Card for SNAP

## Dataset Description

- **Repository:** [ardax/hashtag-segmentor](https://github.com/ardax/hashtag-segmentor)
- **Paper:** [Segmenting hashtags using automatically created training data](http://www.lrec-conf.org/proceedings/lrec2016/pdf/708_Paper.pdf)

### Dataset Summary

Automatically segmented 803K SNAP Twitter Data Set hashtags with the heuristic described in the paper "Segmenting hashtags using automatically created training data".

### Languages

English

## Dataset Structure

### Data Instances

```
{
    "index": 0,
    "hashtag": "BrandThunder",
    "segmentation": "Brand Thunder"
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
@inproceedings{celebi2016segmenting,
  title={Segmenting hashtags using automatically created training data},
  author={Celebi, Arda and {\"O}zg{\"u}r, Arzucan},
  booktitle={Proceedings of the Tenth International Conference on Language Resources and Evaluation (LREC'16)},
  pages={2981--2985},
  year={2016}
}
```

### Contributions

This dataset was added by [@ruanchaves](https://github.com/ruanchaves) while developing the [hashformers](https://github.com/ruanchaves/hashformers) library.
