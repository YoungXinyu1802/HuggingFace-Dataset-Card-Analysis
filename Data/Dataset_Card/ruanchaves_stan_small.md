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
- conditional-text-generation
task_ids: []
pretty_name: STAN Small
tags:
- word-segmentation
---

# Dataset Card for STAN Small

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

Manually Annotated Stanford Sentiment Analysis Dataset by Bansal et al..

### Languages

English

## Dataset Structure

### Data Instances

```
{
    "index": 300,
    "hashtag": "microsoftfail",
    "segmentation": "microsoft fail",
    "alternatives": {
        "segmentation": [
            "Microsoft fail"
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
@misc{bansal2015deep,
      title={Towards Deep Semantic Analysis Of Hashtags}, 
      author={Piyush Bansal and Romil Bansal and Vasudeva Varma},
      year={2015},
      eprint={1501.03210},
      archivePrefix={arXiv},
      primaryClass={cs.IR}
}
```

### Contributions

This dataset was added by [@ruanchaves](https://github.com/ruanchaves) while developing the [hashformers](https://github.com/ruanchaves/hashformers) library.