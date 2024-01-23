---
annotations_creators:
- no-annotation
language_creators:
- found
language:
- en
license:
- unknown
multilinguality:
- monolingual
pretty_name: Team-PIXEL/rendered-bookcorpus
size_categories:
- 1M<n<10M
source_datasets:
- rendered|BookCorpusOpen
task_categories:
- masked-auto-encoding
- rendered-language-modelling
task_ids:
- masked-auto-encoding
- rendered-language-modeling
paperswithcode_id: bookcorpus
---

# Dataset Card for Team-PIXEL/rendered-bookcorpus

## Dataset Description

- **Homepage:** [https://github.com/xplip/pixel](https://github.com/xplip/pixel)
- **Repository:** [https://github.com/xplip/pixel](https://github.com/xplip/pixel)
- **Papers:** [Aligning Books and Movies: Towards Story-like Visual Explanations by Watching Movies and Reading Books
](https://arxiv.org/abs/1506.06724), [Language Modelling with Pixels](https://arxiv.org/abs/2207.06991)
- **Point of Contact:** [Phillip Rust](mailto:p.rust@di.ku.dk)
- **Size of downloaded dataset files:** 63.58 GB
- **Size of the generated dataset:** 63.59 GB
- **Total amount of disk used:** 127.17 GB

### Dataset Summary

This dataset is a version of the BookCorpus available at [https://huggingface.co/datasets/bookcorpusopen](https://huggingface.co/datasets/bookcorpusopen) with examples rendered as images with resolution 16x8464 pixels. 

The original BookCorpus was introduced by Zhu et al. (2015) in [Aligning Books and Movies: Towards Story-Like Visual Explanations by Watching Movies and Reading Books](https://arxiv.org/abs/1506.06724) and contains 17868 books of various genres. The rendered BookCorpus was used to train the [PIXEL](https://huggingface.co/Team-PIXEL/pixel-base) model introduced in the paper [Language Modelling with Pixels](https://arxiv.org/abs/2207.06991) by Phillip Rust, Jonas F. Lotz, Emanuele Bugliarello, Elizabeth Salesky, Miryam de Lhoneux, and Desmond Elliott.

The BookCorpusOpen dataset was rendered book-by-book into 5.4M examples containing approximately 1.1B words in total. The dataset is stored as a collection of 162 parquet files. It was rendered using the script openly available at [https://github.com/xplip/pixel/blob/main/scripts/data/prerendering/prerender_bookcorpus.py](https://github.com/xplip/pixel/blob/main/scripts/data/prerendering/prerender_bookcorpus.py). The text renderer uses a PyGame backend and a collection of merged Google Noto Sans fonts. The PyGame backend does not support complex text layouts (e.g. ligatures and right-to-left scripts) or emoji, so occurrences of such text in the BookCorpus have not been rendered accurately.
Each example consists of a "pixel_values" field which stores a 16x8464 (height, width) grayscale image containing the rendered text, and an integer value "num_patches" which stores how many image patches (when splitting the image into 529 non-overlapping patches of resolution 16x16 pixels) in the associated images contain actual text, i.e. are neither blank (fully white) nor are the fully black end-of-sequence patch.

The rendered BookCorpus can be loaded via the datasets library as follows:

```python
from datasets import load_dataset

# Download the full dataset to disk
load_dataset("Team-PIXEL/rendered-bookcorpus", split="train")

# Stream the dataset directly from the hub
load_dataset("Team-PIXEL/rendered-bookcorpus", split="train", streaming=True)
```

## Dataset Structure

### Data Instances

- **Size of downloaded dataset files:** 63.58 GB
- **Size of the generated dataset:** 63.59 GB
- **Total amount of disk used:** 127.17 GB

An example of 'train' looks as follows.
```
{
    "pixel_values": <PIL.PngImagePlugin.PngImageFile image mode=L size=8464x16
    "num_patches": "498"
}
```

### Data Fields

The data fields are the same among all splits.

- `pixel_values`: an `Image` feature.
- `num_patches`: a `Value(dtype="int64")` feature.

### Data Splits

|train|
|:----|
|5400000|

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

The books have been crawled from smashwords.com, see their [terms of service](https://www.smashwords.com/about/tos) for more information.

A data sheet for this dataset has also been created and published in [Addressing "Documentation Debt" in Machine Learning Research: A Retrospective Datasheet for BookCorpus](https://arxiv.org/abs/2105.05241)

### Citation Information

```bibtex
@InProceedings{Zhu_2015_ICCV,
    title = {Aligning Books and Movies: Towards Story-Like Visual Explanations by Watching Movies and Reading Books},
    author = {Zhu, Yukun and Kiros, Ryan and Zemel, Rich and Salakhutdinov, Ruslan and Urtasun, Raquel and Torralba, Antonio and Fidler, Sanja},
    booktitle = {The IEEE International Conference on Computer Vision (ICCV)},
    month = {December},
    year = {2015}
}
```

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