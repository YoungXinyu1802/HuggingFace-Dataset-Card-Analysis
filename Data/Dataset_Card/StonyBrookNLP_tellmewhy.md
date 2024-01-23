---
annotations_creators:
- crowdsourced
language_creators:
- found
language:
- en
license:
- unknown
multilinguality:
- monolingual
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories:
- text2text-generation
task_ids: []
paperswithcode_id: null
pretty_name: TellMeWhy
---

# Dataset Card for NewsCommentary

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
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
  - [Contributions](#contributions)

## Dataset Description

- **Homepage:** https://stonybrooknlp.github.io/tellmewhy/
- **Repository:** https://github.com/StonyBrookNLP/tellmewhy
- **Paper:** https://aclanthology.org/2021.findings-acl.53/
- **Leaderboard:** None
- **Point of Contact:** [Yash Kumar Lal](mailto:ylal@cs.stonybrook.edu)

### Dataset Summary

TellMeWhy is a large-scale crowdsourced dataset made up of more than 30k questions and free-form answers concerning why characters in short narratives perform the actions described.

### Supported Tasks and Leaderboards

The dataset is designed to test why-question answering abilities of models when bound by local context.

### Languages

English

## Dataset Structure

### Data Instances

A typical data point consists of a story, a question and a crowdsourced answer to that question. Additionally, the instance also indicates whether the question's answer would be implicit or if it is explicitly stated in text. If applicable, it also contains Likert scores (-2 to 2) about the answer's grammaticality and validity in the given context.

```
{
    "narrative":"Cam ordered a pizza and took it home. He opened the box to take out a slice. Cam discovered that the store did not cut the pizza for him. He looked for his pizza cutter but did not find it. He had to use his chef knife to cut a slice.",
    "question":"Why did Cam order a pizza?",
    "original_sentence_for_question":"Cam ordered a pizza and took it home.",
    "narrative_lexical_overlap":0.3333333333,
    "is_ques_answerable":"Not Answerable",
    "answer":"Cam was hungry.",
    "is_ques_answerable_annotator":"Not Answerable",
    "original_narrative_form":[
        "Cam ordered a pizza and took it home.",
        "He opened the box to take out a slice.",
        "Cam discovered that the store did not cut the pizza for him.",
        "He looked for his pizza cutter but did not find it.",
        "He had to use his chef knife to cut a slice."
    ],
    "question_meta":"rocstories_narrative_41270_sentence_0_question_0",
    "helpful_sentences":[

    ],
    "human_eval":false,
    "val_ann":[

    ],
    "gram_ann":[

    ]
}
```

### Data Fields

- `question_meta` - Unique meta for each question in the corpus
- `narrative` - Full narrative from ROCStories. Used as the context with which the question and answer are associated
- `question` - Why question about an action or event in the narrative
- `answer` - Crowdsourced answer to the question
- `original_sentence_for_question` - Sentence in narrative from which question was generated
- `narrative_lexical_overlap` - Unigram overlap of answer with the narrative
- `is_ques_answerable` - Majority judgment by annotators on whether an answer to this question is explicitly stated in the narrative. If "Not Answerable", it is part of the Implicit-Answer questions subset, which is harder for models.
- `is_ques_answerable_annotator` - Individual annotator judgment on whether an answer to this question is explicitly stated in the narrative.
- `original_narrative_form` - ROCStories narrative as an array of its sentences
- `human_eval` - Indicates whether a question is a specific part of the test set. Models should be evaluated for their answers on these questions using the human evaluation suite released by the authors. They advocate for this human evaluation to be the correct way to track progress on this dataset.
- `val_ann` - Array of Likert scores (possible sizes are 0 and 3) about whether an answer is valid given the question and context. Empty arrays exist for cases where the human_eval flag is False.
- `gram_ann` - Array of Likert scores (possible sizes are 0 and 3) about whether an answer is grammatical. Empty arrays exist for cases where the human_eval flag is False.

### Data Splits

The data is split into training, valiudation, and test sets.

| Train  | Valid | Test  |
| ------ | ----- | ----- |
| 23964  | 2992  | 3563  |

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

ROCStories corpus (Mostafazadeh et al, 2016)

#### Initial Data Collection and Normalization

ROCStories was used to create why-questions related to actions and events in the stories.

#### Who are the source language producers?

[More Information Needed]

### Annotations

#### Annotation process

Amazon Mechanical Turk workers were provided a story and an associated why-question, and asked to answer. Three answers were collected for each question. For a small subset of questions, the quality of answers was also validated in a second round of annotation. This smaller subset should be used to perform human evaluation of any new models built for this dataset.

#### Who are the annotators?

Amazon Mechanical Turk workers

### Personal and Sensitive Information

None

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Evaluation

To evaluate progress on this dataset, the authors advocate for human evaluation and release a suite with the required settings [here](https://github.com/StonyBrookNLP/tellmewhy). Once inference on the test set has been completed, please filter out the answers on which human evaluation needs to be performed by selecting the questions (one answer per question, deduplication might be needed) in the test set where the `human_eval` flag is set to `True`. This subset can then be used to complete the requisite evaluation on TellMeWhy.

### Dataset Curators

[More Information Needed]

### Licensing Information

[More Information Needed]

### Citation Information

```
@inproceedings{lal-etal-2021-tellmewhy,
    title = "{T}ell{M}e{W}hy: A Dataset for Answering Why-Questions in Narratives",
    author = "Lal, Yash Kumar  and
      Chambers, Nathanael  and
      Mooney, Raymond  and
      Balasubramanian, Niranjan",
    booktitle = "Findings of the Association for Computational Linguistics: ACL-IJCNLP 2021",
    month = aug,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.findings-acl.53",
    doi = "10.18653/v1/2021.findings-acl.53",
    pages = "596--610",
}
```

### Contributions

Thanks to [@yklal95](https://github.com/ykl7) for adding this dataset.