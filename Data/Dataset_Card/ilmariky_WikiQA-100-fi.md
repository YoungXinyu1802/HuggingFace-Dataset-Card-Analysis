---
language:
- fi
license:
- gpl-3.0
multilinguality:
- monolingual
size_categories:
- n<1k
task_categories:
- question-answering
task_ids:
- extractive-qa
pretty_name: WikiQA-100-fi
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
# Dataset Card for "WikiQA-100-fi"
### Dataset Summary
WikiQA-100-fi dataset contains 100 questions related to Finnish Wikipedia articles. The dataset is in the [SQuAD](https://rajpurkar.github.io/SQuAD-explorer/) format, and there are 10 questions for each category identified by the authors of SQuAD. Unlike SQuAD2.0, WikiQA-100-fi contains only answerable questions. The dataset is tiny compared to actual QA test sets, but it still gives an impression of the models' performance on purely native text data collected by a native speaker. The dataset was originally created as an evaluation set for models that had been mostly fine-tuned with automatically translated QA data. More information about the dataset and models created with it can be found [here](https://helda.helsinki.fi/handle/10138/344973).
## Dataset Structure
### Data Instances
Example data:
```
{
    "title": "Folksonomia",
    "paragraphs": [
        {
            "qas": [
                {
                    "question": "Minkälaista sisältöä käyttäjät voivat luokitella folksonomian avulla?",
                    "id": "6t4ufel624",
                    "answers": [
                        {
                            "text": "www-sivuja, valokuvia ja linkkejä",
                            "answer_start": 155
                        }
                    ],
                    "is_impossible": false
                }
            ],
            "context": "Folksonomia (engl. folksonomy) on yhteisöllisesti tuotettu, avoin luokittelujärjestelmä, jonka avulla internet-käyttäjät voivat luokitella sisältöä, kuten www-sivuja, valokuvia ja linkkejä. Etymologisesti folksonomia on peräisin sanojen \"folk\" (suom. väki) ja \"taxonomy\" (suom. taksonomia) leikkimielisestä yhdistelmästä."
        }
    ]
}
```
### Data Fields

#### plain_text
- `id`: a `string` feature.
- `title`: a `string` feature.
- `context`: a `string` feature.
- `question`: a `string` feature.
- `answers`: a dictionary feature containing:
  - `text`: a `string` feature.
  - `answer_start`: a `int32` feature.
### Data Splits
|   name   | test|
|----------|----:|
|plain_text|  100|

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