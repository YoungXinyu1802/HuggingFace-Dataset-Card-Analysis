---
annotations_creators:
- other
language:
- en
language_creators:
- other
license:
- mit
multilinguality:
- monolingual
pretty_name: twitter financial news
size_categories:
- 10K<n<100K
source_datasets:
- original
tags:
- twitter
- finance
- markets
- stocks
- wallstreet
- quant
- hedgefunds
- markets
task_categories:
- text-classification
task_ids:
- multi-class-classification
---

Read this [BLOG](https://neuralmagic.com/blog/classifying-finance-tweets-in-real-time-with-sparse-transformers/) to see how I fine-tuned a sparse transformer on this dataset.

### Dataset Description

The Twitter Financial News dataset is an English-language dataset containing an annotated corpus of finance-related tweets. This dataset is used to classify finance-related tweets for their topic.

1. The dataset holds 21,107 documents annotated with 20 labels:

```python
topics = {
    "LABEL_0": "Analyst Update",
    "LABEL_1": "Fed | Central Banks",
    "LABEL_2": "Company | Product News",
    "LABEL_3": "Treasuries | Corporate Debt",
    "LABEL_4": "Dividend",
    "LABEL_5": "Earnings",
    "LABEL_6": "Energy | Oil",
    "LABEL_7": "Financials",
    "LABEL_8": "Currencies",
    "LABEL_9": "General News | Opinion",
    "LABEL_10": "Gold | Metals | Materials",
    "LABEL_11": "IPO",
    "LABEL_12": "Legal | Regulation",
    "LABEL_13": "M&A | Investments",
    "LABEL_14": "Macro",
    "LABEL_15": "Markets",
    "LABEL_16": "Politics",
    "LABEL_17": "Personnel Change",
    "LABEL_18": "Stock Commentary",
    "LABEL_19": "Stock Movement",
}
```

The data was collected using the Twitter API. The current dataset supports the multi-class classification task.

### Task: Topic Classification

# Data Splits
There are 2 splits: train and validation. Below are the statistics:

| Dataset Split | Number of Instances in Split                |
| ------------- | ------------------------------------------- |
| Train         | 16,990                                      |
| Validation    | 4,118                                       |


# Licensing Information
The Twitter Financial Dataset (topic) version 1.0.0 is released under the MIT License.