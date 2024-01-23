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
pretty_name: Test-Stanford
tags:
- word-segmentation
---

# Dataset Card for Test-Stanford

## Dataset Description

- **Paper:** [Towards Deep Semantic Analysis Of Hashtags](https://arxiv.org/abs/1501.03210)

### Dataset Summary

Manually Annotated Stanford Sentiment Analysis Dataset by Bansal et al..

### Languages

English

## Dataset Structure

### Data Instances

```
{
    "index": 1467856821,
    "hashtag": "therapyfail",
    "segmentation": "therapy fail",
    "gold_position": 8,
    "rank": {
        "position": [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20
        ],
        "candidate": [
            "therap y fail",
            "the rap y fail",
            "t her apy fail",
            "the rap yfail",
            "t he rap y fail",
            "thera py fail",
            "ther apy fail",
            "th era py fail",
            "therapy fail",
            "therapy fai l",
            "the r apy fail",
            "the rapyfa il",
            "the rapy fail",
            "t herapy fail",
            "the rapyfail",
            "therapy f ai l",
            "therapy fa il",
            "the rapyf a il",
            "therapy f ail",
            "the ra py fail"
        ]
    }
}
```

### Data Fields

- `index`: a numerical index annotated by Kodali et al..
- `hashtag`: the original hashtag.
- `segmentation`: the gold segmentation for the hashtag.
- `gold_position`: position of the gold segmentation on the `segmentation` field inside the `rank`.
- `rank`: Rank of each candidate selected by a baseline word segmenter ( Segmentations Seeder Module ).

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