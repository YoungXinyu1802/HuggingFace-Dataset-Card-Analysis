---
license: cc0-1.0
task_categories:
- summarization
language:
- bn
size_categories:
- 1K<n<10K
---

# Bengali Abstractive News Summarization (BANS)

## Dataset Description

- **Homepage:** 
- **Repository:** 
- **Paper:** [BANS PAPER](https://doi.org/10.1007/978-981-33-4673-4_4)
- **Leaderboard:** 
- **Point of Contact:** [Prithwiraj Bhattacharjee](prithwiraj_cse@lus.ac.bd)

### Dataset Summary

Nowadays news or text summarization becomes very popular in the NLP field. Both the extractive and abstractive approaches of summarization are implemented in different languages. A significant amount of data is a primary need for any summarization. For the Bengali language, there are only a few datasets are available. Our dataset is made for Bengali Abstractive News Summarization (BANS) purposes. As abstractive summarization is basically neural network-based it needs more and more data to perform well. So we made a standard Bengali abstractive summarization data crawling from online Bengali news portal bangla.bdnews24.com. We crawled more than 19k articles and summaries and standardized the data.
### Downloading the data

```
from datasets import load_dataset

train = load_dataset("sustcsenlp/bn_news_summarization",split="train")

```


### Dataset Description


| Description      | Data Info. |
| ----------- | ----------- |
|     Total no of articles      | 19096       |
| Total no of summaries   | 19096        |
|   Maximum no of words in an article	   | 76                  |
|  Maximum no of words in a summary	    |  12                  |
|  Minimum no of words in an article	     |  5                    |
|    Minimum no of words in a summary  |  3                  |

### Languages

This dataset contains Bangla Text Data.

## Acknowledgement

We would like to thank Shahjalal University of Science and Technology (SUST) research center and SUST NLP research group for their support.

### Citation Information

```
@InProceedings{10.1007/978-981-33-4673-4_4,
author="Bhattacharjee, Prithwiraj
and Mallick, Avi
and Saiful Islam, Md.
and Marium-E-Jannat",
editor="Kaiser, M. Shamim
and Bandyopadhyay, Anirban
and Mahmud, Mufti
and Ray, Kanad",
title="Bengali Abstractive News Summarization (BANS): A Neural Attention Approach",
booktitle="Proceedings of International Conference on Trends in Computational and Cognitive Engineering",
year="2021",
publisher="Springer Singapore",
address="Singapore",
pages="41--51",
abstract="Bhattacharjee, PrithwirajMallick, AviSaiful Islam, Md.Marium-E-JannatAbstractive summarization is the process of generating novel sentences based on the information extracted from the original text document while retaining the context. Due to abstractive summarization's underlying complexities, most of the past research work has been done on the extractive summarization approach. Nevertheless, with the triumph of the sequence-to-sequence (seq2seq) model, abstractive summarization becomes more viable. Although a significant number of notable research has been done in the English language based on abstractive summarization, only a couple of works have been done on Bengali abstractive news summarization (BANS). In this article, we presented a seq2seq based Long Short-Term Memory (LSTM) network model with attention at encoder-decoder. Our proposed system deploys a local attention-based model that produces a long sequence of words with lucid and human-like generated sentences with noteworthy information of the original document. We also prepared a dataset of more than 19 k articles and corresponding human-written summaries collected from bangla.bdnews24.com (https://bangla.bdnews24.com/) which is till now the most extensive dataset for Bengali news document summarization and publicly published in Kaggle (https://www.kaggle.com/prithwirajsust/bengali-news-summarization-dataset) We evaluated our model qualitatively and quantitatively and compared it with other published results. It showed significant improvement in terms of human evaluation scores with state-of-the-art approaches for BANS.",
isbn="978-981-33-4673-4"
}

```

### Contributors

| Name      | University |
| ----------- | ----------- |
| Prithwiraj Bhattacharjee      | Shahjalal University of Science and Technology       |
| Avi Mallick   | Shahjalal University of Science and Technology        |
| Md. Saiful Islam                   |   Shahjalal University of Science and Technology    |
| Marium-E-Jannat       | Shahjalal University of Science and Technology  |