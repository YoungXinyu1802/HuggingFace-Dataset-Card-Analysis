---
pretty_name: NLQuAD
language:
- en
license:
- cc-by-3.0
size_categories:
- 10K<n<100K
multilinguality:
- monolingual
task_ids:
- extractive-qa
dataset_info:
  features:
  - name: title
    dtype: string
  - name: date
    dtype: string
  - name: paragraphs
    list:
    - name: context
      dtype: string
    - name: qas
      list:
      - name: answers
        list:
        - name: answer_end
          dtype: int64
        - name: answer_start
          dtype: int64
        - name: text
          dtype: string
      - name: id
        dtype: string
      - name: question
        dtype: string
  splits:
  - name: train
    num_bytes: 72036724
    num_examples: 10259
  - name: test
    num_bytes: 9045482
    num_examples: 1280
  - name: validation
    num_bytes: 8876137
    num_examples: 1280
  download_size: 0
  dataset_size: 89958343
---
# Dataset Card for "NLQuAD"

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Additional Information](#additional-information)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)

## Dataset Description


- **Homepage:** [https://github.com/ASoleimaniB/NLQuAD](https://github.com/ASoleimaniB/NLQuAD)
- **Paper: https://aclanthology.org/2021.eacl-main.106/**
- **Size of the generated dataset:** 89.95 MB

### Dataset Summary

This is a copy of the original NLQuAD dataset distributed via [Github](https://github.com/ASoleimaniB/NLQuAD).

NLQuAD is a non-factoid long question answering dataset from BBC news articles.
NLQuAD’s question types and the long length of its context documents as well as answers, make it a challenging real-world task.
NLQuAD consists of news articles as context documents, interrogative sub-headings in the articles as questions, and body paragraphs corresponding to the sub-headings as contiguous answers to the questions.
NLQuAD contains 31k non-factoid questions and long answers collected from 13k BBC news articles.
See example articles in BBC [1](https://www.bbc.com/news/world-asia-china-51230011), [2](https://www.bbc.com/news/world-55709428).
We automatically extract target answers because annotating for non-factoid long QA is extremely challenging and costly.

## Dataset Structure

### Data Instances

An example of 'train' looks as follows.

```json
{
    "title": "Khashoggi murder: Body 'dissolved in acid'",
    "date": "2 November 2018",
    "paragraphs":[
        {
            "context": "A top Turkish official, presidential adviser Yasin Aktay, has said ....",
            "qas":[
              {
                  "question":"What was said in the crown prince's alleged phone call?",
                  "id":"0_0",
                  "answers":[
                    {
                      "text":"During the call with President Donald Trump\'s son-in-law Jared Kushner and national ....",
                      "answer_start":1352,
                      "answer_end": 2108,
                    }
                  ]
              },
              {
                  "question":"What has the investigation found so far?",
                  "id":"0_1",
                  "answers":[
                    {
                      "text":"There is still no consensus on how Khashoggi died. He entered ....",
                      "answer_start":2109,
                      "answer_end": 3128,
                    }
                  ]
              },
            ]
        }
    ]
}
```

### Data Fields

The data fields are the same among all splits.

- `title`: a `string` feature.
- `date`: a `string` feature.
- `paragraphs`: a list feature containing dictionaries:
  - `context`: a `string` feature.
  - `qas`: a list feature containing dictionaries:
    - `question`: a `string` feature.
    - `id`: a `string` feature.
    - `answers`: a list feature containing dictionaries:
      - `text`: a `string` feature.
      - `answer_start`: a `int32` feature.
      - `answer_end`: a `int32` feature
        
### Data Splits

|   name   |train|test|validation|
|----------|----:|----:|---------:|
|          |10259| 1280|     1280|


## Additional Information

### Licensing Information

This dataset is distributed under the [CC BY-NC](https://creativecommons.org/licenses/by-nc/3.0/) licence providing free access for non-commercial and academic usage.

### Citation Information

BibTeX:
```json
@inproceedings{soleimani-etal-2021-nlquad,
    title = "{NLQ}u{AD}: A Non-Factoid Long Question Answering Data Set",
    author = "Soleimani, Amir  and
      Monz, Christof  and
      Worring, Marcel",
    booktitle = "Proceedings of the 16th Conference of the European Chapter of the Association for Computational Linguistics: Main Volume",
    month = apr,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.eacl-main.106",
    doi = "10.18653/v1/2021.eacl-main.106",
    pages = "1245--1255",
    abstract = "We introduce NLQuAD, the first data set with baseline methods for non-factoid long question answering, a task requiring document-level language understanding. In contrast to existing span detection question answering data sets, NLQuAD has non-factoid questions that are not answerable by a short span of text and demanding multiple-sentence descriptive answers and opinions. We show the limitation of the F1 score for evaluation of long answers and introduce Intersection over Union (IoU), which measures position-sensitive overlap between the predicted and the target answer spans. To establish baseline performances, we compare BERT, RoBERTa, and Longformer models. Experimental results and human evaluations show that Longformer outperforms the other architectures, but results are still far behind a human upper bound, leaving substantial room for improvements. NLQuAD{'}s samples exceed the input limitation of most pre-trained Transformer-based models, encouraging future research on long sequence language models.",
}

```