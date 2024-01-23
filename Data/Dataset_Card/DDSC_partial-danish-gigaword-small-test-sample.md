---
dataset_info:
  features:
  - name: text
    dtype: string
  - name: source
    dtype: string
  - name: doc_id
    dtype: string
  - name: LICENSE
    dtype: string
  - name: uri
    dtype: string
  - name: date_built
    dtype: string
  splits:
  - name: train
    num_bytes: 23816547.04337273
    num_examples: 2411
  download_size: 11686492
  dataset_size: 23816547.04337273
language:
- da
pretty_name: Danish Gigaword Test Sample
---
# Dataset Card for "Danish Gigaword Test Sample"

This is a small sample of the dataset `DDSC/partial-danish-gigaword-no-twitter`. It is meant as a small dataset for testing code. It is constructed using the following code:


```python
from datasets import concatenate_datasets, load_dataset

# download dataset from huggingface
dataset = load_dataset("DDSC/partial-danish-gigaword-no-twitter")

# All of the dataset is available in the train split - we can simply:
dataset = dataset["train"]

# downsample it to three domains
legal = dataset.filter(lambda x: x["source"] == "retsinformationdk")
news = dataset.filter(lambda x: x["source"] == "tv2r")
speech = dataset.filter(lambda x: x["source"] == "spont")

# downsample to 1000 samples
legal = legal.select(range(1000))
news = news.select(range(1000))

# combine the three domains
dataset = concatenate_datasets([legal, news, speech])

# upload to hub
dataset.push_to_hub("DDSC/partial-danish-gigaword-small-test-sample")
```