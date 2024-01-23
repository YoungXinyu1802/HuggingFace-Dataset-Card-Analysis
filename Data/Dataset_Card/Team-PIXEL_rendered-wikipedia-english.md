---
annotations_creators:
- no-annotation
language_creators:
- crowdsourced
language:
- en
license:
- cc-by-sa-3.0
- gfdl
multilinguality:
- monolingual
pretty_name: Team-PIXEL/rendered-wikipedia-english
size_categories:
- 10M<n<100M
source_datasets:
- original
task_categories:
- masked-auto-encoding
- rendered-language-modelling
task_ids:
- masked-auto-encoding
- rendered-language-modeling
paperswithcode_id: null
---

# Dataset Card for Team-PIXEL/rendered-wikipedia-english


## Dataset Description

- **Homepage:** [https://github.com/xplip/pixel](https://github.com/xplip/pixel)
- **Repository:** [https://github.com/xplip/pixel](https://github.com/xplip/pixel)
- **Paper:** [Language Modelling with Pixels](https://arxiv.org/abs/2207.06991)
- **Point of Contact:** [Phillip Rust](mailto:p.rust@di.ku.dk)
- **Size of downloaded dataset files:** 125.66 GB
- **Size of the generated dataset:** 125.56 GB
- **Total amount of disk used:** 251.22 GB

### Dataset Summary

This dataset contains the full English Wikipedia from February 1, 2018, rendered into images of 16x8464 resolution.

The original text dataset was built from a [Wikipedia dump](https://dumps.wikimedia.org/). Each example in the original *text* dataset contained the content of one full Wikipedia article with cleaning to strip markdown and unwanted sections (references, etc.). Each *rendered* example contains a subset of one full article. This rendered English Wikipedia was used to train the [PIXEL](https://huggingface.co/Team-PIXEL/pixel-base) model introduced in the paper [Language Modelling with Pixels](https://arxiv.org/abs/2207.06991) by Phillip Rust, Jonas F. Lotz, Emanuele Bugliarello, Elizabeth Salesky, Miryam de Lhoneux, and Desmond Elliott.

The original Wikipedia text dataset was rendered article-by-article into 11.4M examples containing approximately 2B words in total. The dataset is stored as a collection of 338 parquet files.

It was rendered using the script openly available at [https://github.com/xplip/pixel/blob/main/scripts/data/prerendering/prerender_wikipedia.py](https://github.com/xplip/pixel/blob/main/scripts/data/prerendering/prerender_wikipedia.py). The text renderer uses a PyGame backend and a collection of merged Google Noto Sans fonts. The PyGame backend does not support complex text layouts (e.g. ligatures and right-to-left scripts) or emoji, so occurrences of such text in the Wikipedia data have not been rendered accurately.
Each example consists of a "pixel_values" field which stores a 16x8464 (height, width) grayscale image containing the rendered text, and an integer value "num_patches" which stores how many image patches (when splitting the image into 529 non-overlapping patches of resolution 16x16 pixels) in the associated images contain actual text, i.e. are neither blank (fully white) nor are the fully black end-of-sequence patch.

You can load the dataset as follows:

```python
from datasets import load_dataset

# Download the full dataset to disk
load_dataset("Team-PIXEL/rendered-wikipedia-english", split="train")

# Stream the dataset directly from the hub
load_dataset("Team-PIXEL/rendered-wikipedia-english", split="train", streaming=True)
```

## Dataset Structure

### Data Instances

- **Size of downloaded dataset files:** 125.66 GB
- **Size of the generated dataset:** 125.56 GB
- **Total amount of disk used:** 251.22 GB

An example of 'train' looks as follows.
```
{
    "pixel_values": <PIL.PngImagePlugin.PngImageFile image mode=L size=8464x16
    "num_patches": "469"
}
```

### Data Fields

The data fields are the same among all splits.

- `pixel_values`: an `Image` feature.
- `num_patches`: a `Value(dtype="int64")` feature.

### Data Splits

|train|
|:----|
|11446535|

## Dataset Creation

### Curation Rationale

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

#### Who are the source language producers?

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Annotations

#### Annotation process

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

#### Who are the annotators?

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Personal and Sensitive Information

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Discussion of Biases

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Other Known Limitations

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

## Additional Information

### Dataset Curators

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Licensing Information

Most of Wikipedia's text and many of its images are co-licensed under the Creative Commons Attribution-ShareAlike 3.0 Unported License (CC BY-SA) and the GNU Free Documentation License (GFDL) (unversioned, with no invariant sections, front-cover texts, or back-cover texts).

Some text has been imported only under CC BY-SA and CC BY-SA-compatible license and cannot be reused under GFDL; such text will be identified on the page footer, in the page history, or on the discussion page of the article that utilizes the text.

### Citation Information

```bibtex
@article{rust-etal-2022-pixel,
  title={Language Modelling with Pixels},
  author={Phillip Rust and Jonas F. Lotz and Emanuele Bugliarello and Elizabeth Salesky and Miryam de Lhoneux and Desmond Elliott},
  journal={arXiv preprint},
  year={2022},
  url={https://arxiv.org/abs/2207.06991}
}
```


### Contact Person

This dataset was added by Phillip Rust.

Github: [@xplip](https://github.com/xplip)

Twitter: [@rust_phillip](https://twitter.com/rust_phillip)