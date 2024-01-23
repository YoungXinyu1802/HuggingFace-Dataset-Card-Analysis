---
license: cc-by-4.0
pretty_name: SQuAD with QG split.
language: en
multilinguality: monolingual
size_categories: 1M<
source_datasets:
- extended|wikipedia
task_categories:
- question-answering
task_ids:
- extractive-qa
---

# Dataset Card for "lmqg/qa_squad"

## Dataset Description
- **Repository:** [https://github.com/asahi417/lm-question-generation](https://github.com/asahi417/lm-question-generation)
- **Paper:** [https://rajpurkar.github.io/SQuAD-explorer/](https://rajpurkar.github.io/SQuAD-explorer/)
- **Point of Contact:** [Asahi Ushio](http://asahiushio.com/)

### Dataset Summary
This is the SQuAD v1 dataset with the train/validatio/test split used in [qg_squad](https://huggingface.co/datasets/lmqg/qg_squad).


### Supported Tasks and Leaderboards
* `question-answering`

### Languages
English (en)

## Dataset Structure

### Data Fields
The data fields are the same among all splits.

#### plain_text

- `id`: a `string` feature of id
- `title`: a `string` feature of title of the paragraph 
- `context`: a `string` feature of paragraph 
- `question`: a `string` feature of question
- `answers`: a `json` feature of answers

### Data Splits

|train    |validation|test    |
|--------:|---------:|-------:|
|   75,722|    10,570|  11,877|

## Citation Information

```
@article{2016arXiv160605250R,
       author = {{Rajpurkar}, Pranav and {Zhang}, Jian and {Lopyrev},
                 Konstantin and {Liang}, Percy},
        title = "{SQuAD: 100,000+ Questions for Machine Comprehension of Text}",
      journal = {arXiv e-prints},
         year = 2016,
          eid = {arXiv:1606.05250},
        pages = {arXiv:1606.05250},
archivePrefix = {arXiv},
       eprint = {1606.05250},
}
```