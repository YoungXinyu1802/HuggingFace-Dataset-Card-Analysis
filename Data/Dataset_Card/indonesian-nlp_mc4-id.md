---
annotations_creators:
- no-annotation
language_creators:
- found
language:
- id
license:
- odc-by
multilinguality:
- monolingual
size_categories:
  tiny:
  - 1M<n<10M
  small:
  - 10M<n<100M
  medium:
  - 10M<n<100M
  large:
  - 10M<n<100M
  full:
  - 100M<n<1B
source_datasets:
- extended
task_categories:
- text-generation
task_ids:
- language-modeling
paperswithcode_id: mc4
pretty_name: mC4-id
---

# Dataset Card for Clean(maybe) Indonesia mC4 

## Dataset Description

- **Original Homepage:** [HF Hub](https://huggingface.co/datasets/allenai/c4)
- **Paper:** [ArXiv](https://arxiv.org/abs/1910.10683)

### Dataset Summary

A thoroughly cleaned version of the Indonesia split of the multilingual colossal, cleaned version of Common Crawl's web crawl corpus (mC4). Based on the [Common Crawl dataset](https://commoncrawl.org). The original version was prepared by [AllenAI](https://allenai.org/), hosted at the address [https://huggingface.co/datasets/allenai/c4](https://huggingface.co/datasets/allenai/c4).


### Data Fields

The data contains the following fields:

- `url`: url of the source as a string
- `text`: text content as a string
- `timestamp`: timestamp of extraction as a string

### Data Splits


You can load any subset like this:

```python
from datasets import load_dataset

mc4_id_tiny = load_dataset("munggok/mc4-id", "tiny")
```

Since splits are quite large, you may want to traverse them using the streaming mode available starting from 🤗 Datasets v1.9.0:

```python
from datasets import load_dataset

mc4_id_full_stream = load_dataset("munggok/mc4-id", "full", split='train', streaming=True)
print(next(iter(mc4_id_full_stream))) # Prints the example presented above
```

## Dataset Creation

Refer to the original paper for more considerations regarding the choice of sources and the scraping process for creating `mC4`.

## Considerations for Using the Data

### Discussion of Biases

Despite the cleaning procedure aimed at removing vulgarity and profanity, it must be considered that model trained on this scraped corpus will inevitably reflect biases present in blog articles and comments on the Internet. This makes the corpus especially interesting in the context of studying data biases and how to limit their impacts.

## Additional Information

### Dataset Curators

Authors at AllenAI are the original curators for the `mc4` corpus.

### Licensing Information

AllenAI are releasing this dataset under the terms of ODC-BY. By using this, you are also bound by the Common Crawl terms of use in respect of the content contained in the dataset.

### Citation Information

If you use this dataset in your work, please cite us and the original mC4 authors as:

```

@inproceedings{xue-etal-2021-mt5,
    title = "m{T}5: A Massively Multilingual Pre-trained Text-to-Text Transformer",
    author = "Xue, Linting  and
      Constant, Noah  and
      Roberts, Adam  and
      Kale, Mihir  and
      Al-Rfou, Rami  and
      Siddhant, Aditya  and
      Barua, Aditya  and
      Raffel, Colin",
    booktitle = "Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies",
    month = jun,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.naacl-main.41",
    doi = "10.18653/v1/2021.naacl-main.41",
    pages = "483--498",
}
```

### Contributions

Thanks to [@dirkgr](https://github.com/dirkgr) and [@lhoestq](https://github.com/lhoestq) for adding this dataset.
