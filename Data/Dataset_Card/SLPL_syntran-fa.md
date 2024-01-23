---
language:
- fa
license: mit
multilinguality:
- monolingual
size_categories:
- 30k<n<50k
task_categories:
- question-answering
- text2text-generation
- text-generation
task_ids: []
pretty_name: SynTranFa
tags:
- conditional-text-generation
- conversational-question-answering
---

# SynTran-fa 
Syntactic Transformed Version of Farsi QA datasets to make fluent responses from questions and short answers. You can use this dataset by the code below:

```python
import datasets
data = datasets.load_dataset('SLPL/syntran-fa', split="train")
```

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
- [Dataset Creation](#dataset-creation)
  - [Source Data](#source-data)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description
 
- **Homepage:** [Sharif-SLPL](https://github.com/Sharif-SLPL)
- **Repository:** [SynTran-fa](https://github.com/agp-internship/syntran-fa)
- **Point of Contact:** [Sadra Sabouri](mailto:sabouri.sadra@gmail.com)

### Dataset Summary

Generating fluent responses has always been challenging for the question-answering task, especially in low-resource languages like Farsi. In recent years there were some efforts for enhancing the size of datasets in Farsi. Syntran-fa is a question-answering dataset that accumulates the former Farsi QA dataset's short answers and proposes a complete fluent answer for each pair of (question, short_answer).

This dataset contains nearly 50,000 indices of questions and answers. The dataset that has been used as our sources are in [Source Data section](#source-data).

The main idea for this dataset comes from [Fluent Response Generation for Conversational Question Answering](https://aclanthology.org/2020.acl-main.19.pdf) where they used a "parser + syntactic rules" module to make different fluent answers from a pair of question and a short answer using a parser and some syntactic rules. In this project, we used [stanza](https://stanfordnlp.github.io/stanza/) as our parser to parse the question and generate a response according to it using the short (sentences without verbs - up to ~4 words) answers. One can continue this project by generating different permutations of the sentence's parts (and thus providing more than one sentence for an answer) or training a seq2seq model which does what we do with our rule-based system (by defining a new text-to-text task).

### Supported Tasks and Leaderboards

This dataset can be used for the question-answering task, especially when you are going to generate fluent responses. You can train a seq2seq model with this dataset to generate fluent responses - as done by [Fluent Response Generation for Conversational Question Answering](https://aclanthology.org/2020.acl-main.19.pdf).

### Languages

+ Persian (fa)

## Dataset Structure
Each row of the dataset will look like something like the below:
```json
{
  'id': 0,
  'question': 'باشگاه هاکی ساوتهمپتون چه نام دارد؟',
  'short_answer': 'باشگاه هاکی ساوتهمپتون',
  'fluent_answer': 'باشگاه هاکی ساوتهمپتون باشگاه هاکی ساوتهمپتون نام دارد.',
  'bert_loss': 1.110097069682014
}
```
+ `id` : the entry id in dataset
+ `question` : the question
+ `short_answer` : the short answer corresponding to the `question` (the primary answer)
+ `fluent_answer` : fluent (long) answer generated from both `question` and the `short_answer` (the secondary answer)
+ `bert_loss` : the loss that [pars-bert](https://huggingface.co/HooshvareLab/bert-base-parsbert-uncased) gives when inputting the `fluent_answer` to it. As it increases the sentence is more likely to be influent.

Note: the dataset is sorted increasingly by the `bert_loss`, so first sentences are more likely to be fluent.

### Data Splits

Currently, the dataset just provided the `train` split. There would be a `test` split soon.

## Dataset Creation

### Source Data
The source datasets that we used are as follows:

+ [PersianQA](https://github.com/sajjjadayobi/PersianQA)
+ [PersianQuAD](https://ieeexplore.ieee.org/document/9729745)

#### Initial Data Collection and Normalization

We extract all short answer (sentences without verbs - up to ~4 words) entries of all open source QA datasets in Farsi and used some rules featuring the question parse tree to make long (fluent) answers.

### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

[More Information Needed]

### Personal and Sensitive Information

The dataset is completely a subset of open source known datasets so all information in it is already there on the internet as a open-source dataset. By the way, we do not take responsibility for any of that.

## Additional Information

### Dataset Curators

The dataset is gathered together completely in the Asr Gooyesh Pardaz company's summer internship under the supervision of Soroush Gooran, Prof. Hossein Sameti, and the mentorship of Sadra Sabouri. This project was Farhan Farsi's first internship project. 

### Licensing Information

MIT

### Citation Information

[More Information Needed]

### Contributions

Thanks to [@farhaaaaa](https://github.com/farhaaaaa) and [@sadrasabouri](https://github.com/sadrasabouri) for adding this dataset.