---
language:
- ar
- en
- he
- de
- it
- fr
- pl
- pt
- ru
- uk
---

# Dataset

## Leipzig Corpora Collection:      
[link](https://wortschatz.uni-leipzig.de/en/download)

## Dataset Description      

The Leipzig Corpora Collection presents corpora in different languages using the same format and comparable sources. All data are available as plain text files and can be imported into a MySQL database by using the provided import script. They are intended both for scientific use by corpus linguists as well as for applications such as knowledge extraction programs.
The corpora are identical in format and similar in size and content. They contain randomly selected sentences in the language of the corpus and are available in sizes from 10,000 sentences up to 1 million sentences. The sources are either newspaper texts or texts randomly collected from the web. The texts are split into sentences. Non-sentences and foreign language material was removed. Because word co-occurrence information is useful for many applications, these data are precomputed and included as well. For each word, the most significant words appearing as immediate left or right neighbor or appearing anywhere within the same sentence are given. More information about the format and content of these files can be found [here](https://wortschatz.uni-leipzig.de/en/download).
The corpora are automatically collected from carefully selected public sources without considering in detail the content of the contained text. No responsibility is taken for the content of the data. In particular, the views and opinions expressed in specific parts of the data remain exclusively with the authors.

If you use one of these corpora in your work we kindly ask you to cite [this paper](http://www.lrec-conf.org/proceedings/lrec2012/pdf/327_Paper.pdf) as:

D. Goldhahn, T. Eckart & U. Quasthoff: Building Large Monolingual Dictionaries at the Leipzig Corpora Collection: From 100 to 200 Languages.
In: Proceedings of the 8th International Language Resources and Evaluation (LREC'12), 2012

## Dataset Usage

!Note: it seems that there is an issue with fetching this dataset in the colab, due to problem of the downloading in the colab from https://pcai056.informatik.uni-leipzig.de

Config "links" contains URLs with corresponding language and id.     

```python
from datasets import load_dataset

ds = load_dataset("imvladikon/leipzig_corpora_collection", "links")
for row in ds["train"]:
    print(row)
```


```
{'id': '0', 'data_id': '0', 'url': 'https://pcai056.informatik.uni-leipzig.de/downloads/corpora/ara_news_2005-2009_10K.tar.gz', 'language': 'Arabic', 'language_short': 'ara', 'year': '2005', 'size': '10K'}
{'id': '1', 'data_id': '1', 'url': 'https://pcai056.informatik.uni-leipzig.de/downloads/corpora/ara_news_2005-2009_30K.tar.gz', 'language': 'Arabic', 'language_short': 'ara', 'year': '2005', 'size': '30K'}
{'id': '2', 'data_id': '2', 'url': 'https://pcai056.informatik.uni-leipzig.de/downloads/corpora/ara_news_2005-2009_100K.tar.gz', 'language': 'Arabic', 'language_short': 'ara', 'year': '2005', 'size': '100K'}
....
```    

Need to choose one of the data_ids to load the dataset, and paste this data_id as the corresponding config 


```python
dataset_he = load_dataset("imvladikon/leipzig_corpora_collection", "heb_wikipedia_2021_1M", split="train")
for row in dataset_he:
    print(row)
```


Example for English:     


```python
dataset_en = load_dataset("imvladikon/leipzig_corpora_collection", "eng-simple_wikipedia_2021_300K", split="train")
for row in dataset_en:
    print(row)
```

### Filtering

```python
links = load_dataset("imvladikon/leipzig_corpora_collection", "links", split="train")

english_2019 = links.filter(lambda x: x["language"] == "English" and x["year"] == "2019")

for sample in english_2019:
    print(sample)
```


