---
license: cc-by-4.0
pretty_name: SQuADShifts
language: en
multilinguality: monolingual
size_categories: 1k<n<10k
source_datasets:
- extended|wikipedia
task_categories:
- question-answering
task_ids:
- extractive-qa
---

# Dataset Card for "lmqg/qa_squadshifts"

## Dataset Description
- **Repository:** [https://github.com/asahi417/lm-question-generation](https://github.com/asahi417/lm-question-generation)
- **Paper:** [https://arxiv.org/abs/2004.14444](https://arxiv.org/abs/2004.14444)
- **Point of Contact:** [Asahi Ushio](http://asahiushio.com/)

### Dataset Summary
This is SQuADShifts dataset with custom split of training/validation/test following [lmqg/qg_squadshifts](https://huggingface.co/datasets/lmqg/qg_squadshifts).


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

|   name      |train  | valid | test |
|-------------|------:|------:|-----:|
|default (all)|9209|6283 |18,844|
| amazon      |3295|1648|4942|
| new_wiki    |2646|1323|3969|
| nyt         |3355|1678|5032|
| reddit      |3268|1634|4901|

## Citation Information

```
@inproceedings{miller2020effect,
  title={The effect of natural distribution shift on question answering models},
  author={Miller, John and Krauth, Karl and Recht, Benjamin and Schmidt, Ludwig},
  booktitle={International Conference on Machine Learning},
  pages={6905--6916},
  year={2020},
  organization={PMLR}
}
```