---
annotations_creators:
- crowdsourced
language:
- en
- ar
- bn
- fi
- id
- ja
- sw
- ko
- ru
- te
- th
language_creators:
- crowdsourced
license:
- apache-2.0
multilinguality:
- multilingual
pretty_name: Answerable TyDi QA
size_categories:
- ['100K<n<1M']
source_datasets:
- extended|wikipedia
task_categories:
- question-answering
task_ids:
- extractive-qa
---

# Dataset Card for "answerable-tydiqa"


## Dataset Description

- **Homepage:** [https://github.com/google-research-datasets/tydiqa](https://github.com/google-research-datasets/tydiqa)
- **Paper:** [Paper](https://aclanthology.org/2020.tacl-1.30/)
- **Size of downloaded dataset files:** 75.43 MB
- **Size of the generated dataset:** 131.78 MB
- **Total amount of disk used:** 207.21 MB

### Dataset Summary

[TyDi QA](https://huggingface.co/datasets/tydiqa) is a question answering dataset covering 11 typologically diverse languages. 
Answerable TyDi QA is an extension of the GoldP subtask of the original TyDi QA dataset to also include unanswertable questions.

## Dataset Structure

The dataset contains a train and a validation set, with 116067 and 13325 examples, respectively. Access them with

```py
from datasets import load_dataset
dataset = load_dataset("copenlu/answerable_tydiqa")
train_set = dataset["train"]
validation_set = dataset["validation"]
```

### Data Instances

Here is an example of an instance of the dataset:

```
{'question_text': 'dimanakah  Dr. Ernest François Eugène Douwes Dekker meninggal?',
 'document_title': 'Ernest Douwes Dekker',
 'language': 'indonesian',
 'annotations': 
             {'answer_start': [45],
              'answer_text': ['28 Agustus 1950']
              },
 'document_plaintext': 'Ernest Douwes Dekker wafat dini hari tanggal 28 Agustus 1950 (tertulis di batu nisannya; 29 Agustus 1950 versi van der Veur, 2006) dan dimakamkan di TMP Cikutra, Bandung.',
 'document_url': 'https://id.wikipedia.org/wiki/Ernest%20Douwes%20Dekker'}
```

Description of the dataset columns:

| Column name                  | type        |  Description                                                                                                     |
| -----------                  | ----------- | -----------                                                                                                      |
| document_title               | str         | The title of the Wikipedia article from which the data instance was generated                                    |
| document_url                 | str         | The URL of said article                                                                                          |
| language                     | str         | The language of the data instance                                                                                |
| question_text                | str         | The question to answer                                                                                           |
| document_plaintext           | str         | The context, a Wikipedia paragraph that might or might not contain the answer to the question                    | 
| annotations["answer_start"]  | list[int]   | The char index in 'document_plaintext' where the answer starts. If the question is unanswerable - [-1]  |
| annotations["answer_text"]   | list[str]   | The answer, a span of text from 'document_plaintext'. If the question is unanswerable - ['']            |


**Notice:** If the question is *answerable*, annotations["answer_start"] and annotations["answer_text"] contain a list of length 1  
(In some variations of the dataset the lists might be longer, e.g. if more than one person annotated the instance, but not in our case). 
If the question is *unanswerable*, annotations["answer_start"] will have "-1", while annotations["answer_text"] contain a list with an empty sring.


## Useful stuff

Check out the [datasets ducumentations](https://huggingface.co/docs/datasets/quickstart) to learn how to manipulate and use the dataset. Specifically, you might find the following functions useful:

`dataset.filter`, for filtering out data (useful for keeping instances of specific languages, for example).

`dataset.map`, for manipulating the dataset.

`dataset.to_pandas`, to convert the dataset into a pandas.DataFrame format.


```
@article{tydiqa,
title   = {TyDi QA: A Benchmark for Information-Seeking Question Answering in Typologically Diverse Languages},
author  = {Jonathan H. Clark and Eunsol Choi and Michael Collins and Dan Garrette and Tom Kwiatkowski and Vitaly Nikolaev and Jennimaria Palomaki}
year    = {2020},
journal = {Transactions of the Association for Computational Linguistics}
}

```


### Contributions

Thanks to [@thomwolf](https://github.com/thomwolf), [@albertvillanova](https://github.com/albertvillanova), [@lewtun](https://github.com/lewtun), [@patrickvonplaten](https://github.com/patrickvonplaten) for adding this dataset.