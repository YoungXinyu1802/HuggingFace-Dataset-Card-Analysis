---
annotations_creators:
- expert-generated
language_creators:
- machine-generated
language:
- hi
- en
license:
- unknown
multilinguality:
- multilingual
size_categories:
- unknown
source_datasets:
- original
task_categories:
- structure-prediction
task_ids:
- named-entity-recognition
pretty_name: HashSet Manual
tags:
- word-segmentation
---

# Dataset Card for HashSet Manual

## Dataset Description

- **Repository:** [prashantkodali/HashSet](https://github.com/prashantkodali/HashSet)
- **Paper:** [HashSet -- A Dataset For Hashtag Segmentation](https://arxiv.org/abs/2201.06741)

### Dataset Summary

Hashset is a new dataset consisting on 1.9k manually annotated and 3.3M loosely supervised tweets for testing the 
efficiency of hashtag segmentation models. We compare State of The Art Hashtag Segmentation models on Hashset and other 
baseline datasets (STAN and BOUN). We compare and analyse the results across the datasets to argue that HashSet can act 
as a good benchmark for hashtag segmentation tasks.

HashSet Manual: contains 1.9k manually annotated hashtags. Each row consists of the hashtag, segmented hashtag ,named entity annotations, whether the hashtag contains mix of hindi and english tokens and/or contains non-english tokens.

### Languages

Mostly Hindi and English.

## Dataset Structure

### Data Instances

```
{
    "index": 10,
    "hashtag": "goodnewsmegan",
    "segmentation": "good news megan",
    "spans": {
        "start": [
            8
        ],
        "end": [
            13
        ],
        "text": [
            "megan"
        ]
    },
    "source": "roman",
    "gold_position": null,
    "mix": false,
    "other": false,
    "ner": true,
    "annotator_id": 1,
    "annotation_id": 2088,
    "created_at": "2021-12-30 17:10:33.800607",
    "updated_at": "2021-12-30 17:10:59.714840",
    "lead_time": 3896.182,
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
            10
        ],
        "candidate": [
            "goodnewsmegan",
            "goodnewsmeg an",
            "goodnews megan",
            "goodnewsmega n",
            "go odnewsmegan",
            "good news megan",
            "good newsmegan",
            "g oodnewsmegan",
            "goodnewsme gan",
            "goodnewsm egan"
        ]
    }
}
```

### Data Fields

- `index`: a numerical index annotated by Kodali et al..
- `hashtag`: the original hashtag.
- `segmentation`: the gold segmentation for the hashtag.
- `spans`: named entity spans. 
- `source`: data source.
- `gold_position`: position of the gold segmentation on the `segmentation` field inside the `rank`.
- `mix`: The hashtag has a mix of English and Hindi tokens.
- `other`: The hashtag has non-English tokens. 
- `ner`: The hashtag has named entities.
- `annotator_id`: annotator ID.
- `annotation_id`: annotation ID.
- `created_at`: Creation date timestamp.
- `updated_at`: Update date timestamp.
- `lead_time`: Lead time field annotated by Kodali et al..
- `rank`: Rank of each candidate selected by a baseline word segmenter ( WordBreaker ).
- `candidates`: Candidates selected by a baseline word segmenter ( WordBreaker ).

## Dataset Creation

- All hashtag segmentation and identifier splitting datasets on this profile have the same basic fields: `hashtag` and `segmentation` or `identifier` and `segmentation`.

- The only difference between `hashtag` and `segmentation` or between `identifier` and `segmentation` are the whitespace characters. Spell checking, expanding abbreviations or correcting characters to uppercase go into other fields.

- There is always whitespace between an alphanumeric character and a sequence of any special characters ( such as `_` , `:`, `~` ). 

- If there are any annotations for named entity recognition and other token classification tasks, they are given in a `spans` field.

## Additional Information

### Citation Information

```
@article{kodali2022hashset,
  title={HashSet--A Dataset For Hashtag Segmentation},
  author={Kodali, Prashant and Bhatnagar, Akshala and Ahuja, Naman and Shrivastava, Manish and Kumaraguru, Ponnurangam},
  journal={arXiv preprint arXiv:2201.06741},
  year={2022}
}
```

### Contributions

This dataset was added by [@ruanchaves](https://github.com/ruanchaves) while developing the [hashformers](https://github.com/ruanchaves/hashformers) library.