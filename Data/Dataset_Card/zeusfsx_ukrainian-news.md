---
license: unknown
task_categories:
- text-generation
language:
- uk
pretty_name: ukr-news
size_categories:
- 10M<n<100M
tags:
- news
---


# Ukrainian News Dataset

This is a dataset of news articles downloaded from various Ukrainian websites. The dataset contains approximately 10 569 428 JSON objects (news), each with the following fields:

```json
  title: The title of the news article
  text: The text of the news article, which may contain HTML tags(e.g., paragraphs, links, images, etc.)
  url: The URL of the news article
  datetime: The time of publication or when the article was parsed and added to the dataset
  owner: The name of the website that published the news article
```

The JSON objects are divided into parts, and the dataset is available for download via Hugging Face. The terms of use state that all data in this dataset is under the copyright of the owners of the respective websites.

## Accessing the Dataset

The dataset is available for download via the Hugging Face datasets library. You can install the library via pip:

```bash
pip install datasets
```
Once you have installed the library, you can load the dataset using the following code:

```python

from datasets import load_dataset

dataset = load_dataset('zeusfsx/ukrainian-news')
```

This will load the entire dataset into memory. If you prefer to load only a subset of the data, you can specify the split argument:

```python

# Load only the first 10,000 examples from the "train" split
dataset = load_dataset('zeusfsx/ukrainian-news', split='train[:10000]')
```

## Contacts

If you have any questions or comments about this dataset, please contact me at email [zeusfsxtmp@gmail.com]. I will do our best to respond to your inquiry as soon as possible.

## License

The dataset is made available under the terms of use specified by the owners of the respective websites. Please consult the individual websites for more information on their terms of use.