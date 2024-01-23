---
annotations_creators:
- expert-generated
language_creators:
- machine-generated
language:
- ru
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
pretty_name: NRU-HSE
tags:
- word-segmentation
---

# Dataset Card for NRU-HSE

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

- **Repository:** [glushkovato/hashtag_segmentation](https://github.com/glushkovato/hashtag_segmentation/)
- **Paper:** [Char-RNN and Active Learning for Hashtag Segmentation](https://arxiv.org/abs/1911.03270)

### Dataset Summary

Real hashtags collected from several pages about civil services on vk.com (a Russian social network) and then segmented manually.

### Languages

Russian

## Dataset Structure

### Data Instances

```
{
  "index": 0, 
  "hashtag": "ЁлкаВЗазеркалье",
  "segmentation": "Ёлка В Зазеркалье"
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
@article{glushkova2019char,
  title={Char-RNN and Active Learning for Hashtag Segmentation},
  author={Glushkova, Taisiya and Artemova, Ekaterina},
  journal={arXiv preprint arXiv:1911.03270},
  year={2019}
}
```

### Contributions

This dataset was added by [@ruanchaves](https://github.com/ruanchaves) while developing the [hashformers](https://github.com/ruanchaves/hashformers) library.