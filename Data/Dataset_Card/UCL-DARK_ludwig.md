---
annotations_creators:
- expert-generated
language:
- en
language_creators:
- expert-generated
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: ludwig
size_categories:
- n<1K
source_datasets:
- original
tags:
- implicature
- pragmatics
- language
- llm
- conversation
- dialogue
task_categories:
- text-generation
- fill-mask
task_ids:
- language-modeling
- masked-language-modeling
---

# Dataset Card for LUDWIG

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

- **Homepage:**
- **Repository: https://github.com/ucl-dark/ludwig**
- **Paper: TODO**
- **Leaderboard: TODO**
- **Point of Contact: Laura Ruis**

### Dataset Summary

LUDWIG (**L**anguage **U**nderstanding **W**ith **I**mplied meanin**G**) is a dataset containing English conversational implicatures.
Implicature is the act of meaning or implying one thing by saying something else. 
There's different types of implicatures, from simple ones like "Some guests came to the party" 
(implying not all guests came) to more complicated implicatures that depend on context like 
"A: Are you going to the party this Friday? B: There's a global pandemic.", implying no. Implicatures serve a wide range of
goals in communication: efficiency, style, navigating social interactions, and more. We cannot fully
understand utterances without understanding their implications.  
The implicatures in this dataset  are conversational because they come in utterance-response tuples. 
Each tuple has an implicature associated with it,
which is the implied meaning of the response. For example:

Utterance: Are you going to the party this Friday?  
Response: There's a global pandemic.  
Implicature: No. 

This dataset can be used to evaluate language models on their pragmatic language understanding.

### Supported Tasks and Leaderboards

- ```text-generation```: The dataset can be used to evaluate a models ability to generate the correct next token, i.e. "yes" or "no", depending on the implicature. For example, if you pass the model an example wrapped in a template like "Esther asked 'Are you coming to the party this Friday' and Juan responded 'There's a global pandemic', which means" the correct completion would be "no". Success in this task can be determined by the ability to generate the correct answer or by the ability to give the right token a higher likelihood than the wrong token, e.g. p("no") > p("yes").
- ```fill-mask```: The dataset can be used to evaluate a models ability to fill the correct token, i.e. "yes" or "no", depending on the implicature. For example, if you pass the model an example wrapped in a template like "Esther asked 'Are you coming to the party this Friday' and Juan responded 'There's a global pandemic', which means [mask]" the correct mask-fill would be "no". Success in this task can be determined by the ability to fill the correct answer or by the ability to give the right token a higher likelihood than the wrong token, e.g. p("no") > p("yes").

### Languages

English

## Dataset Structure

### Data Instances

Find below an example of a 1-shot example instance (1-shot because there's 1 prompt example).
```
{
  "id": 1,
  "utterance": "Are you going to the party this Friday?",
  "response": "There's a global pandemic.",
  "implicature": "No.",
  "incoherent_implicature": "Yes".
  "prompts": [
      {
          "utterance": "Was that hot?",
          "response": "The sun was scorching.",
          "implicature": "Yes.",
          "incoherent_implicature": "No.".
      }
  ]
}
```

### Data Fields

```
{
  "id": int,  # unique identifier of data points
  "utterance": str,  # the utterance in this example
  "response": str,  # the response in this example
  "implicature": str,  # the implied meaning of the response, e.g. 'yes'
  "incoherent_implicature": str,  # the wrong implied meaning, e.g. 'no'
  "prompts": [  # optional: prompt examples from the validation set
      {
          "utterance": str,
          "response": str,
          "implicature": str,
          "incoherent_implicature": str,
      }
  ]
}
```

### Data Splits

**Validation**: 118 instances that can be used for finetuning or few-shot learning  
**Test**: 600 instances that can be used for evaluating models.

NB: the splits weren't originally part of the paper that presents this dataset. The same goes for the k-shot prompts. Added
by @LauraRuis.

## Dataset Creation

### Curation Rationale

Pragmatic language understanding is a crucial aspect of human communication, and implicatures are the primary object of study in this field.
We want computational models of language to understand all the speakers implications.

### Source Data

#### Initial Data Collection and Normalization

"Conversational implicatures in English dialogue: Annotated dataset", Elizabeth Jasmi George and Radhika Mamidi 2020.

[Link to paper](https://doi.org/10.1016/j.procs.2020.04.251)

#### Who are the source language producers?

These written representations of the utterances are collected manually by scraping and transcribing from relevant sources from August, 2019 to August, 2020. The source of dialogues in the data include TOEFL listening comprehension short conversations, movie dialogues from IMSDb and websites explaining idioms, similes, metaphors and hyperboles. The implicatures are annotated manually.

### Annotations

#### Annotation process

Manually annotated by dataset collectors.

#### Who are the annotators?

Authors of the original paper.

### Personal and Sensitive Information

All the data is public and not sensitive.

## Considerations for Using the Data

### Social Impact of Dataset

Any application that requires communicating with humans requires pragmatic language understanding.

### Discussion of Biases

Implicatures can be biased to specific cultures. For example, whether the Pope is Catholic (a common used response implicature to indicate "yes") might not be common knowledge for everyone.
Implicatures are also language-specific, the way people use pragmatic language depends on the language. This dataset only focuses on the English language.

### Other Known Limitations

None yet.

## Additional Information

### Dataset Curators

Elizabeth Jasmi George and Radhika Mamidi

### Licensing Information

[license](https://creativecommons.org/licenses/by/4.0/)

### Citation Information

```
@article{George:Mamidi:2020,
 author = {George, Elizabeth Jasmi and Mamidi, Radhika},
 doi = {10.1016/j.procs.2020.04.251},
 journal = {Procedia Computer Science},
 keywords = {},
 note = {https://doi.org/10.1016/j.procs.2020.04.251},
 number = {},
 pages = {2316-2323},
 title = {Conversational implicatures in English dialogue: Annotated dataset},
 url = {https://app.dimensions.ai/details/publication/pub.1128198497},
 volume = {171},
 year = {2020}
}
```

### Contributions

Thanks to [@LauraRuis](https://github.com/LauraRuis) for adding this dataset.