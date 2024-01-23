---
annotations_creators:
- crowdsourced
language_creators:
- crowdsourced
- found
language:
- fi
license:
- gpl-3.0
multilinguality:
- monolingual
size_categories:
- 10K<n<100K
task_categories:
- question-answering
task_ids:
- extractive-qa
pretty_name: SQuAD-v2-fi
tags:
- question-generation
train-eval-index:
- config: plain_text
  task: question-answering
  task_id: extractive_question_answering
  splits:
    train_split: train
    eval_split: validation
  col_mapping:
    question: question
    context: context
    answers:
      text: text
      answer_start: answer_start
---
# Dataset Card for "squad-v2-fi"
### Dataset Summary
Machine translated and normalized Finnish version of the SQuAD-v2.0 dataset. Details about the translation and normalization processes can be found [here](https://helda.helsinki.fi/handle/10138/344973).

Stanford Question Answering Dataset (SQuAD) is a reading comprehension dataset, consisting of questions posed by crowdworkers on a set of Wikipedia articles, where the answer to every question is a segment of text, or span, from the corresponding reading passage, or the question might be unanswerable.
## Dataset Structure
### Data Instances
Example data:
```
{
    "title": "Josefina (Ruotsin kuningatar)",
    "paragraphs": [
        {
            "qas": [
                {
                    "question": "Milloin Josefina Maximiliana Eugenia Napoleona av Leuchtenberg syntyi?",
                    "id": "2149392872931478957",
                    "answers": [
                        {
                            "answer_start": 59,
                            "text": "14. maaliskuuta 1807"
                        }
                    ],
                    "is_impossible": false
                }
            ],
            "context": "Josefina Maximiliana Eugenia Napoleona av Leuchtenberg (14. maaliskuuta 1807 − 7. kesäkuuta 1876, Tukholma) oli Ruotsi-Norjan kuningatar ja kuningas Oskar I:n puoliso."
        }
    ]
}
```
### Data Fields
The data fields are the same among all splits.
#### plain_text
- `id`: a `string` feature.
- `title`: a `string` feature.
- `context`: a `string` feature.
- `question`: a `string` feature.
- `answers`: a dictionary feature containing:
  - `text`: a `string` feature.
  - `answer_start`: a `int32` feature.
### Data Splits
|   name   |train|validation|
|----------|----:|---------:|
|plain_text|92383|      8737|

### Citation Information
```
@MastersThesis{3241c198b3f147faacbc6d8b64ed9419,
  author   = "Kylli{\"a}inen, {Ilmari}",
  title    = "Neural Factoid Question Answering and Question Generation for Finnish",
  language = "en",
  address  = "Helsinki, Finland",
  school   = "University of Helsinki",
  year     = "2022",
  month    = "jun",
  day      = "15",
  url      = "https://helda.helsinki.fi/handle/10138/344973"
}
```