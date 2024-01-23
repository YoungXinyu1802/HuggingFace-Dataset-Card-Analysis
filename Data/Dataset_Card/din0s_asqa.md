---
annotations_creators:
- crowdsourced
language:
- en
language_creators:
- expert-generated
license:
- apache-2.0
multilinguality:
- monolingual
pretty_name: ASQA
size_categories:
- 1K<n<10K
source_datasets:
- extended|ambig_qa
tags:
- factoid questions
- long-form answers
task_categories:
- question-answering
task_ids:
- open-domain-qa
---

# Dataset Card for ASQA

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Additional Information](#additional-information)
  - [Contributions](#contributions)

## Dataset Description

- **Repository:** https://github.com/google-research/language/tree/master/language/asqa
- **Paper:** https://arxiv.org/abs/2204.06092
- **Leaderboard:** https://ambigqa.github.io/asqa_leaderboard.html

### Dataset Summary

ASQA is the first long-form question answering dataset that focuses on ambiguous factoid questions. Different from previous long-form answers datasets, each question is annotated with both long-form answers and extractive question-answer pairs, which should be answerable by the generated passage. A generated long-form answer will be evaluated using both ROUGE and QA accuracy. In the paper, we show that these evaluation metrics are well-correlated with human judgments.

### Supported Tasks and Leaderboards

Long-form Question Answering. [Leaderboard](https://ambigqa.github.io/asqa_leaderboard.html)


### Languages

- English

## Dataset Structure

### Data Instances

```py
{
  "ambiguous_question": "Where does the civil liberties act place the blame for the internment of u.s. citizens?",
  "qa_pairs": [
    {
      "context": "No context provided",
      "question": "Where does the civil liberties act place the blame for the internment of u.s. citizens by apologizing on behalf of them?",
      "short_answers": [
        "the people of the United States"
      ],
      "wikipage": None
    },
    {
      "context": "No context provided",
      "question": "Where does the civil liberties act place the blame for the internment of u.s. citizens by making them pay reparations?",
      "short_answers": [
        "United States government"
      ],
      "wikipage": None
    }
  ],
  "wikipages": [
    {
      "title": "Civil Liberties Act of 1988",
      "url": "https://en.wikipedia.org/wiki/Civil%20Liberties%20Act%20of%201988"
    }
  ],
  "annotations": [
    {
      "knowledge": [
        {
          "content": "The Civil Liberties Act of 1988 (Pub.L. 100–383, title I, August 10, 1988, 102 Stat. 904, 50a U.S.C. § 1989b et seq.) is a United States federal law that granted reparations to Japanese Americans who had been interned by the United States government during World War II.",
          "wikipage": "Civil Liberties Act of 1988"
        }
      ],
      "long_answer": "The Civil Liberties Act of 1988 is a United States federal law that granted reparations to Japanese Americans who had been interned by the United States government during World War II. In the act, the blame for the internment of U.S. citizens was placed on the people of the United States, by apologizing on behalf of them. Furthermore, the blame for the internment was placed on the United States government, by making them pay reparations."
    }
  ],
  "sample_id": -4557617869928758000
}
```

### Data Fields

- `ambiguous_question`: ambiguous question from AmbigQA.
- `annotations`: long-form answers to the ambiguous question constructed by ASQA annotators.
- `annotations/knowledge`: list of additional knowledge pieces.
- `annotations/knowledge/content`: a passage from Wikipedia.
- `annotations/knowledge/wikipage`: title of the Wikipedia page the passage was taken from.
- `annotations/long_answer`: annotation.
- `qa_pairs`: Q&A pairs from AmbigQA which are used for disambiguation.
- `qa_pairs/context`: additional context provided.
- `qa_pairs/question`: disambiguated question from AmbigQA.
- `qa_pairs/short_answers`: list of short answers from AmbigQA.
- `qa_pairs/wikipage`: title of the Wikipedia page the additional context was taken from.
- `sample_id`: the unique id of the sample	
- `wikipages`: list of Wikipedia pages visited by AmbigQA annotators.
- `wikipages/title`: title of the Wikipedia page.
- `wikipages/url`: link to the Wikipedia page.

### Data Splits

| **Split** | **Instances** |
|-----------|---------------|
| Train     | 4353          |
| Dev       | 948           |

## Additional Information

### Contributions

Thanks to [@din0s](https://github.com/din0s) for adding this dataset.