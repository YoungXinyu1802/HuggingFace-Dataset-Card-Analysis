---
language:
- en
license:
- mit
multilinguality:
- monolingual
pretty_name: AESLC - Cleaned & Keyword Extracted
source_datasets:
- aeslc
tags:
- text2text generation
- email
- email generation
- enron
---

## about

- aeslc dataset but cleaned and keywords extracted to a new column
- an EDA website generated via pandas profiling [is on netlify here](https://aeslc-kw-train-eda.netlify.app/)

```
DatasetDict({
    train: Dataset({
        features: ['email_body', 'subject_line', 'clean_email', 'clean_email_keywords'],
        num_rows: 14436
    })
    test: Dataset({
        features: ['email_body', 'subject_line', 'clean_email', 'clean_email_keywords'],
        num_rows: 1906
    })
    validation: Dataset({
        features: ['email_body', 'subject_line', 'clean_email', 'clean_email_keywords'],
        num_rows: 1960
    })
})
```

## Python usage


Basic example notebook [here](https://colab.research.google.com/gist/pszemraj/18742da8db4a99e57e95824eaead285a/scratchpad.ipynb).

```python
from datasets import load_dataset

dataset = load_dataset("postbot/aeslc_kw")
```

## Citation

```
@InProceedings{zhang2019slg,
  author =      "Rui Zhang and Joel Tetreault",
  title =       "This Email Could Save Your Life: Introducing the Task of Email Subject Line Generation",
  booktitle =   "Proceedings of The 57th Annual Meeting of the Association for Computational Linguistics",
  year =        "2019",
  address =     "Florence, Italy"
}
```