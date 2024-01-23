---
annotations_creators:
- crowdsourced
language:
- cs
language_creators:
- crowdsourced
license:
- lgpl-3.0
multilinguality:
- monolingual
pretty_name: Czech Simple Question Answering Dataset
size_categories:
- 1K<n<10K
source_datasets:
- original
tags:
- czech QA
- wikipedia QA
task_categories:
- question-answering
task_ids:
- extractive-qa
---




# Dataset Card for Czech Simple Question Answering Dataset 2.0

This a processed and filtered adaptation of an existing dataset. For raw and larger dataset, see `Dataset Source` section.


## Dataset Description
The data contains questions and answers based on Czech wikipeadia articles.
Each question has an answer (or more) and a selected part of the context as the evidence.
A majority of the answers are extractive - i.e. they are present in the context in the exact form. The remaining cases are

- yes/no questions
- answer is almost in the exact form present in the text, but the form of words was changed to suit the question (declension, ...)
- answered in own words (should be rare, but is not)

All questions in the dataset are answerable from the context. Small minority of questions have multiple answers.
Sometimes it means that any of them is correct (e.g. either "Pacifik" or "Tichý oceán" are correct terms for Pacific Ocean)
and sometimes it means that all of them together are a correct answer (e.g., Who was Leonardo da Vinci? ["painter", "engineer"])

Total number of examples is around:

- 6,250 in train
- 570 in validation
- 850 in test.


## Dataset Features
Each example contains:
- `item_id`: string id of the
- `context`: "reasonably" big chunk (string) of wikipedia article that contains the answer
- `question`: string
- `answers`: list of all answers (string). mostly list of length 1
- `evidence_text`: substring of context (typically one sentence) that is sufficient to answer the question
- `evidence_start`: index in context, such that `context[evidence_start:evidence_end] == evidence_text`
- `evidence_end`: index in context
- `occurences`:
  list of (dictionaries) occurences of the answer(s) in the evidence.
  Each answer was searched with word boundaries ("\b" in regex) and case-sensitive in the evidence.
  If nothing found, try again but case-insensitive.
  If nothing found, try again but case-sensitive without word boundaries.
  If nothing found, try again but case-insensitive without word boundaries.
  This process should supress "false positive" occurences of the answer in the evidence.
  - `start`: index in context
  - `end`: index in context
  - `text`: the answer looked for
- `url`: link to the wikipedia article
- `original_article`: original parsed wikipedia article from which the context is taken
- `question_type`: type of the question, one of: ['ABBREVIATION', 'DATETIME', 'DENOTATION', 'ENTITY', 'LOCATION', 'NUMERIC', 'ORGANIZATION', 'OTHER', 'PERSON', 'YES_NO']
- `answer_type`: type of the answer, one of: ['ABBREVIATION', 'ADJ_PHRASE', 'CLAUSE', 'DATETIME', 'ENTITY', 'LOCATION', 'NUMERIC', 'OTHER', 'PERSON', 'VERB_PHRASE']


## Dataset Source

The dataset is a preprocessed adaptation of existing SQAD 3.0 dataset [link to data](https://lindat.cz/repository/xmlui/handle/11234/1-3069).
This adaptation contains (almost) same data, but converted to a convenient format.
The data was also filtered to remove a statistical bias where the answer was contained
in the first sentence in the article (around 50% of all data in the original dataset, likely
caused by the data collection process).


## Citation

Cite authors of the [original dataset](https://lindat.cz/repository/xmlui/handle/11234/1-3069):

```bibtex
@misc{11234/1-3069,
 title = {sqad 3.0},
 author = {Medve{\v d}, Marek and Hor{\'a}k, Ale{\v s}},
 url = {http://hdl.handle.net/11234/1-3069},
 note = {{LINDAT}/{CLARIAH}-{CZ} digital library at the Institute of Formal and Applied Linguistics ({{\'U}FAL}), Faculty of Mathematics and Physics, Charles University},
 copyright = {{GNU} Library or "Lesser" General Public License 3.0 ({LGPL}-3.0)},
 year = {2019}
}
```
