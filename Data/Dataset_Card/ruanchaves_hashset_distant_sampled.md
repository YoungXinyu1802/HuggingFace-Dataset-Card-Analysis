---
annotations_creators:
- machine-generated
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
task_ids: []
pretty_name: HashSet Distant Sampled
tags:
- word-segmentation
---

# Dataset Card for HashSet Distant Sampled

## Dataset Description

- **Repository:** [prashantkodali/HashSet](https://github.com/prashantkodali/HashSet)
- **Paper:** [HashSet -- A Dataset For Hashtag Segmentation](https://arxiv.org/abs/2201.06741)

### Dataset Summary

Hashset is a new dataset consisting on 1.9k manually annotated and 3.3M loosely supervised tweets for testing the 
efficiency of hashtag segmentation models. We compare State of The Art Hashtag Segmentation models on Hashset and other 
baseline datasets (STAN and BOUN). We compare and analyse the results across the datasets to argue that HashSet can act 
as a good benchmark for hashtag segmentation tasks.

HashSet Distant: 3.3M loosely collected camel cased hashtags containing hashtag and their segmentation.

HashSet Distant Sampled is a sample of 20,000 camel cased hashtags from the HashSet Distant dataset.

### Languages

Hindi and English.

## Dataset Structure

### Data Instances

```
{
  'index': 282559, 
  'hashtag': 'Youth4Nation', 
  'segmentation': 'Youth 4 Nation'
}
```

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