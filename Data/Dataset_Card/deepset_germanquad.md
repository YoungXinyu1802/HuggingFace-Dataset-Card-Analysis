---
thumbnail: https://thumb.tildacdn.com/tild3433-3637-4830-a533-353833613061/-/resize/720x/-/format/webp/germanquad.jpg
language:
- de
multilinguality:
- monolingual
source_datasets:
- original
task_categories:
- question-answering
- text-retrieval
task_ids:
- extractive-qa
- closed-domain-qa
- open-domain-qa
train-eval-index:
- config: plain_text
  task: question-answering
  task_id: extractive_question_answering
  splits:
    train_split: train
    eval_split: test
  col_mapping:
    context: context
    question: question
    answers.text: answers.text
    answers.answer_start: answers.answer_start
---

![bert_image](https://thumb.tildacdn.com/tild3433-3637-4830-a533-353833613061/-/resize/720x/-/format/webp/germanquad.jpg)
# Dataset Card for germanquad

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-instances)
  - [Data Splits](#data-instances)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Citation Information](#citation-information)

## Dataset Description

- **Homepage:** https://deepset.ai/germanquad
- **Repository:** https://github.com/deepset-ai/haystack
- **Paper:** https://arxiv.org/abs/2104.12741

### Dataset Summary
In order to raise the bar for non-English QA, we are releasing a high-quality, human-labeled German QA dataset consisting of 13 722 questions, incl. a three-way annotated test set.
The creation of GermanQuAD is inspired by insights from existing datasets as well as our labeling experience from several industry projects. We combine the strengths of SQuAD, such as high out-of-domain performance, with self-sufficient questions that contain all relevant information for open-domain QA as in the NaturalQuestions dataset. Our training and test datasets do not overlap like other popular datasets and include complex questions that cannot be answered with a single entity or only a few words.

### Supported Tasks and Leaderboards

- `extractive-qa`, `closed-domain-qa`, `open-domain-qa`, `text-retrieval`: This dataset is intended to be used for `open-domain-qa`, but can also be used for information retrieval tasks.

### Languages

The sentences in the dataset are in German (de).

## Dataset Structure

### Data Instances

A sample from the training set is provided below:

```
{
    "paragraphs": [
        {
            "qas": [
                {
                    "question": "Von welchem Gesetzt stammt das Amerikanische ab? ",
                    "id": 51870,
                    "answers": [
                        {
                            "answer_id": 53778,
                            "document_id": 43958,
                            "question_id": 51870,
                            "text": "britischen Common Laws",
                            "answer_start": 146,
                            "answer_category": "SHORT"
                        }
                    ],
                    "is_impossible": false
                }
            ],
            "context": "Recht_der_Vereinigten_Staaten\
\
=== Amerikanisches Common Law ===\
Obwohl die Vereinigten Staaten wie auch viele Staaten des Commonwealth Erben des britischen Common Laws sind, setzt sich das amerikanische Recht bedeutend davon ab. Dies rührt größtenteils von dem langen Zeitraum her, in dem sich das amerikanische Recht unabhängig vom Britischen entwickelt hat. Entsprechend schauen die Gerichte in den Vereinigten Staaten bei der Analyse von eventuell zutreffenden britischen Rechtsprinzipien im Common Law gewöhnlich nur bis ins frühe 19. Jahrhundert.\
Während es in den Commonwealth-Staaten üblich ist, dass Gerichte sich Entscheidungen und Prinzipien aus anderen Commonwealth-Staaten importieren, ist das in der amerikanischen Rechtsprechung selten. Ausnahmen bestehen hier nur, wenn sich überhaupt keine relevanten amerikanischen Fälle finden lassen, die Fakten nahezu identisch sind und die Begründung außerordentlich überzeugend ist. Frühe amerikanische Entscheidungen zitierten oft britische Fälle, solche Zitate verschwanden aber während des 19. Jahrhunderts, als die Gerichte eindeutig amerikanische Lösungen zu lokalen Konflikten fanden. In der aktuellen Rechtsprechung beziehen sich fast alle Zitate auf amerikanische Fälle.\
Einige Anhänger des Originalismus und der strikten Gesetzestextauslegung (''strict constructionism''), wie zum Beispiel der verstorbene Bundesrichter am Obersten Gerichtshof, Antonin Scalia, vertreten die Meinung, dass amerikanische Gerichte ''nie'' ausländische Fälle überprüfen sollten, die nach dem Unabhängigkeitskrieg entschieden wurden, unabhängig davon, ob die Argumentation überzeugend ist oder nicht. Die einzige Ausnahme wird hier in Fällen gesehen, die durch die Vereinigten Staaten ratifizierte völkerrechtliche Verträge betreffen. Andere Richter, wie zum Beispiel Anthony Kennedy und Stephen Breyer vertreten eine andere Ansicht und benutzen ausländische Rechtsprechung, sofern ihre Argumentation für sie überzeugend, nützlich oder hilfreich ist.",
            "document_id": 43958
        }
    ]
},
```

### Data Fields

- `id`: a `string` feature.
- `context`: a `string` feature.
- `question`: a `string` feature.
- `answers`: a dictionary feature containing:
  - `text`: a `string` feature.
  - `answer_start`: a `int32` feature.
### Data Splits

The dataset is split into a one-way annotated training set and a three-way annotated test set of German Wikipedia passages (paragraphs). Each passage is
from a different article.

|      |passages|questions|answers|
|----------|----:|---------:|---------:|
|train|2540|     11518|11518|
|test|474|     2204|6536|

## Additional Information

### Dataset Curators

The dataset was initially created by Timo Möller, Julian Risch, Malte Pietsch, Julian Gutsch, Tom Hersperger, Luise Köhler, Iuliia Mozhina, and Justus Peter, during work done at deepset.ai

### Citation Information

```
@misc{möller2021germanquad,
      title={GermanQuAD and GermanDPR: Improving Non-English Question Answering and Passage Retrieval}, 
      author={Timo Möller and Julian Risch and Malte Pietsch},
      year={2021},
      eprint={2104.12741},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```