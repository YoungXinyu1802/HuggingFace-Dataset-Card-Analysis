---
pretty_name: Danish WIT
language:
- da
license:
- cc-by-sa-4.0
size_categories:
- 100K<n<1M
source_datasets:
- wikimedia/wit_base
task_categories:
- image-to-text
- zero-shot-image-classification
- feature-extraction
task_ids:
- image-captioning
---

# Dataset Card for Danish WIT

## Dataset Description

- **Repository:** <https://gist.github.com/saattrupdan/bb6c9c52d9f4b35258db2b2456d31224>
- **Point of Contact:** [Dan Saattrup Nielsen](mailto:dan.nielsen@alexandra.dk)
- **Size of downloaded dataset files:** 7.5 GB
- **Size of the generated dataset:** 7.8 GB
- **Total amount of disk used:** 15.3 GB

### Dataset Summary

Google presented the Wikipedia Image Text (WIT) dataset in [July
2021](https://dl.acm.org/doi/abs/10.1145/3404835.3463257), a dataset which contains
scraped images from Wikipedia along with their descriptions. WikiMedia released
WIT-Base in [September
2021](https://techblog.wikimedia.org/2021/09/09/the-wikipedia-image-caption-matching-challenge-and-a-huge-release-of-image-data-for-research/),
being a modified version of WIT where they have removed the images with empty
"reference descriptions", as well as removing images where a person's face covers more
than 10% of the image surface, along with inappropriate images that are candidate for
deletion. This dataset is the Danish portion of the WIT-Base dataset, consisting of
roughly 160,000 images with associated Danish descriptions. We release the dataset
under the [CC BY-SA 4.0 license](https://creativecommons.org/licenses/by-sa/4.0/), in
accordance with WIT-Base's [identical
license](https://huggingface.co/datasets/wikimedia/wit_base#licensing-information).


### Supported Tasks and Leaderboards

Training machine learning models for caption generation, zero-shot image classification
and text-image search are the intended tasks for this dataset. No leaderboard is active
at this point.


### Languages

The dataset is available in Danish (`da`).


## Dataset Structure

### Data Instances

- **Size of downloaded dataset files:** 7.5 GB
- **Size of the generated dataset:** 7.8 GB
- **Total amount of disk used:** 15.3 GB

An example from the `train` split looks as follows.
```
{
    "image": {
        "bytes": b"\xff\xd8\xff\xe0\x00\x10JFIF...",
        "path": None
    },
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/4/45/Bispen_-_inside.jpg",
    "embedding": [2.8568285, 2.9562542, 0.33794892, 8.753725, ...],
    "metadata_url": "http://commons.wikimedia.org/wiki/File:Bispen_-_inside.jpg",
    "original_height": 3161,
    "original_width": 2316,
    "mime_type": "image/jpeg",
    "caption_attribution_description": "Kulturhuset Bispen set indefra. Biblioteket er til venstre",
    "page_url": "https://da.wikipedia.org/wiki/Bispen",
    "attribution_passes_lang_id": True,
    "caption_alt_text_description": None,
    "caption_reference_description": "Bispen set indefra fra 1. sal, hvor ....",
    "caption_title_and_reference_description": "Bispen [SEP] Bispen set indefra ...",
    "context_page_description": "Bispen er navnet på det offentlige kulturhus i ...",
    "context_section_description": "Bispen er navnet på det offentlige kulturhus i ...",
    "hierarchical_section_title": "Bispen",
    "is_main_image": True,
    "page_changed_recently": True,
    "page_title": "Bispen",
    "section_title": None
}
```

### Data Fields

The data fields are the same among all splits.

- `image`: a `dict` feature.
- `image_url`: a `str` feature.
- `embedding`: a `list` feature.
- `metadata_url`: a `str` feature.
- `original_height`: an `int` or `NaN` feature.
- `original_width`: an `int` or `NaN` feature.
- `mime_type`: a `str` or `None` feature.
- `caption_attribution_description`: a `str` or `None` feature.
- `page_url`: a `str` feature.
- `attribution_passes_lang_id`: a `bool` or `None` feature.
- `caption_alt_text_description`: a `str` or `None` feature.
- `caption_reference_description`: a `str` or `None` feature.
- `caption_title_and_reference_description`: a `str` or `None` feature.
- `context_page_description`: a `str` or `None` feature.
- `context_section_description`: a `str` or `None` feature.
- `hierarchical_section_title`: a `str` feature.
- `is_main_image`: a `bool` or `None` feature.
- `page_changed_recently`: a `bool` or `None` feature.
- `page_title`: a `str` feature.
- `section_title`: a `str` or `None` feature.

### Data Splits

Roughly 2.60% of the WIT-Base dataset comes from the Danish Wikipedia. We have split
the resulting 168,740 samples into a training set, validation set and testing set of
the following sizes:

|   split | samples |
|---------|--------:|
| train   | 167,460 |
| val     | 256     |
| test    | 1,024   |


## Dataset Creation

### Curation Rationale

It is quite cumbersome to extract the Danish portion of the WIT-Base dataset,
especially as the dataset takes up 333 GB of disk space, so the curation of Danish-WIT
is purely to make it easier to work with the Danish portion of it.

### Source Data

The original data was collected from WikiMedia's
[WIT-Base](https://huggingface.co/datasets/wikimedia/wit_base) dataset, which in turn
comes from Google's [WIT](https://huggingface.co/datasets/google/wit) dataset.


## Additional Information

### Dataset Curators

[Dan Saattrup Nielsen](https://saattrupdan.github.io/) from the [The Alexandra
Institute](https://alexandra.dk/) curated this dataset.

### Licensing Information

The dataset is licensed under the [CC BY-SA 4.0
license](https://creativecommons.org/licenses/by-sa/4.0/).
