---
annotations_creators:
- found
language_creators:
- found
language:
- en
license:
- cc-by-sa-4.0
multilinguality:
- monolingual
size_categories:
- 1K<n<10K
source_datasets:
- original
task_categories:
- summarization
task_ids: []
tags:
- query-based-summarization
---

# Dataset Card for answersumm

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-instances)
  - [Data Splits](#data-instances)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)

## Dataset Description

- **Homepage:** https://github.com/Alex-Fabbri/AnswerSumm
- **Paper:** [AnswerSumm: A Manually-Curated Dataset and Pipeline for Answer Summarization](https://arxiv.org/abs/2111.06474)
- **Point of Contact:** [Alex Fabbri](mailto:afabbri@salesforce.com)

### Dataset Summary

The AnswerSumm dataset is an English-language dataset of questions and answers collected from a [StackExchange data dump](https://archive.org/details/stackexchange). The dataset was created to support the task of query-focused answer summarization with an emphasis on multi-perspective answers. 
The dataset consists of over 4200 such question-answer threads annotated by professional linguists and includes over 8700 summaries. We decompose the task into several annotation stages, including sentence selection, sentence clustering, cluster summarization, and overall summarization. For each thread, the annotator writes two summaries, one in which the annotator is asked to mark sentences that are included in the final summary and instructed to more closely use the words in these sentences rather than abstract. We have multiple annotators for a subset of the examples in the test set. 


### Languages

The text in the dataset is in English. 

## Dataset Structure

### Data Instances

A data point comprises a question with a `title` field containing the overview of the question and a `question` that elaborates on the title.  The answers are sentence tokenized and contain relevance labels, labels for inclusion in the final summary, and cluster labels. We include cluster summaries, overall summaries, and additional metadata. 

An example from the AnswerSumm test set looks as follows:
```json
{
  "example_id": 9_24,
  "annotator_id": [1], 
  "question": {
    "author": "gaming.stackexchange.com/users/11/Jeffrey",
    "forum": "gaming.stackexchange.com",
    "link": "gaming.stackexchange.com/questions/1",
    "question": "Now that the Engineer update has come, there will be lots of Engineers building up everywhere.  How should this best be handled?",
    "question_tags": "\<team-fortress-2\>",
    "title": "What is a good strategy to deal with lots of engineers turtling on the other team?"
  }, 
  "answers": [
    {  
      "answer_details": {
        "author": "gaming.stackexchange.com/users/44/Corv1nus", 
        "score": 49 
      }
      "sents": [
        "text": "Lots of medics with lots of ubers on high-damage-dealing classes." 
        "label": [0],
        "label_summ": [0],
        "cluster_id": [[-1]],
      ]
      ...
    },
    ...
  ]
  "summaries": [
     [
      "Demomen usually work best against a sentry farm. Heavies or pyros can also be effective. Medics should be in the frontline to absorb the shock. Build a teleporter to help your team through.",
      "Demomen are best against a sentry farm. Heavies or pyros can also be effective. The medic should lead the uber combo. ..."
     ]
  ]
  "cluster_summaries":[
    "Demomen are best against a sentry farm.",
    "Heavies or pyros can also be effective.",
    ...
  ]
}

```

            

### Data Fields

- question: contains metadata about the question and forum
    - question: the body of the question post
    - title: the title of the question post
    - question_tags: user-provided question tags
    - link: link to the original question
    - author: link to the author's user page (as requested by StackExchange's attribution policy)

- answers: list of sentence-tokenized answers
    - answer_details: dictionary consisting of link to answer author's user page (author) and community-assigned score (score)
    - sents: sentences that compose the answer
      - text: the sentence text
      - label: a list (to generalize to multi-annotator scenarios) of whether the sentence is labeled as relevant or not for answering the question. 
      - label_summ: a list of whether the sentence was used to write the first annotator-created summary (that is the first summary in `summaries`)
      - cluster_id: a list of lists (potentially multiple annotators and a sentence can be in potentially multiple clusters) of the clusters a sentence belongs to. -1 implies no cluster. This label can be used to aggregate sentences into clusters across answers. 

- summaries: list of list of summaries. Each annotator wrote two summaries. The first in the list is the summary in which the instructor was told to mark sentences relevant for inclusion in the summary and then closely use the words of these sentences, while for the second summary the annotator was asked to paraphrase and condense the cluster summaries but was not asked to reduce abstraction.

- annotator_id: a list of the ids of the annotator(s) who completed all tasks related to that thread.

- mismatch_info: a dict of any issues in processing the excel files on which annotations were completed. 
  - rel_sent_not_in_cluster: list of booleans indicating whether there are sentences that are labeled as relevant but were not included in a cluster. 
  - cluster_sents_not_matched: list of sentences that were found in a cluster but which our processing script didn't automatically match to sentences in the source answers. If cluster summarization is of interest to the user you may want to process these examples separately using clusters_orig. 

### Data Splits

The data is split into training, validation, and test sets using stratified sampling on the source forums. There are 2783, 500, and 1000 train/validation/test threads, respectively.

## Dataset Creation

### Curation Rationale

AnswerSumm was built to provide a testbed for query-focused summarization of multi-perspective answers. The data collection was designed to tackle multiple subtasks including sentence selection, clustering, cluster summarization, and overall summarization. 

### Source Data

#### Initial Data Collection and Normalization

The data was obtained by filtering examples based on a whitelist of forums from StackExchange which we believed would be able to be summarized by a lay person. We describe. We asked annotators to remove examples which required technical knowledge or additional context beyond what was present in the answers. 

#### Who are the source language producers?

The language producers are the users of the StackExchange forums sampled.

### Annotations

#### Annotation process

Please see our [paper](https://arxiv.org/pdf/2111.06474.pdf) for additional annotation details. We began with a pre-pilot of 50 examples, followed by a pilot of 500 and a final annotation of 5000 examples. This release contains the results of the final data collection. We will release the instructions used in data collection. 

#### Who are the annotators?

The annotators are professional linguists who were obtained through an internal contractor. 

### Personal and Sensitive Information

We did not anonymize the data. We followed the specifications from StackExchange [here](https://archive.org/details/stackexchange) to include author information.

## Considerations for Using the Data

### Social Impact of Dataset

The purpose of this dataset is to help develop systems that automatically summarize multi-perspective answers. A system that succeeds at this task would be able to summarize many perspectives present in an answer and not limit itself to a single perspective.

### Discussion of Biases

While StackExchange allows for the exchange of information and ideas, hate and harassment may exist on this site. While our annotators did not flag examples in this process, we encourage users of the dataset to reach out with concerns. 
We also note that this dataset is limited in its monolingual coverage. 


## Additional Information

### Dataset Curators

The dataset was collected by Alex Fabbri, Xiaojian Wu, Srini Iyer, Haoran Li, and Mona Diab during work done at Facebook. 

### Licensing Information

The data is released under cc-by-sa 4.0 following the original StackExchange [release](https://archive.org/details/stackexchange).

### Citation Information

```bibtex
@misc{fabbri-etal-2022-answersumm,
      title={AnswerSumm: A Manually-Curated Dataset and Pipeline for Answer Summarization}, 
      author={Alexander R. Fabbri and Xiaojian Wu and Srini Iyer and Haoran Li and Mona Diab },
      year={2022},
      eprint={2111.06474},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2111.06474}
}
```
