---
annotations_creators:
- found
language_creators:
- found
language:
- ar
- es
- eu
- hi
- id
- zh
- ru
- my
license:
- unknown
multilinguality:
- multilingual
size_categories:
- 1K<n<10K
source_datasets:
- original
task_ids: []
tags:
- other-story-completion
---
# Dataset Card for "story_cloze"
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

### Dataset Summary
Story Cloze Test' is a new commonsense reasoning framework for evaluating story understanding, 
story generation, and script learning.This test requires a system to choose the correct ending 
to a four-sentence story.

### Data Instances
- **Size of downloaded dataset files:** 2.03 MB
- **Size of the generated dataset:** 2.03 MB
- **Total amount of disk used:** 2.05 MB
An example of 'train' looks as follows.
```
{'answer_right_ending': 1,
 'input_sentence_1': 'Rick grew up in a troubled household.',
 'input_sentence_2': 'He never found good support in family, and turned to gangs.',
 'input_sentence_3': "It wasn't long before Rick got shot in a robbery.",
 'input_sentence_4': 'The incident caused him to turn a new leaf.',
 'sentence_quiz1': 'He is happy now.',
 'sentence_quiz2': 'He joined a gang.',
 'story_id': '138d5bfb-05cc-41e3-bf2c-fa85ebad14e2'}
```

### Data Fields

The data fields are the same among all splits.
- `input_sentence_1`: The first statement in the story.
- `input_sentence_2`: The second statement in the story.
- `input_sentence_3`: The third statement in the story.
- `input_sentence_4`: The forth statement in the story.
- `sentence_quiz1`: first possible continuation of the story. 
- `sentence_quiz2`: second possible continuation of the story. 
- `answer_right_ending`: correct possible ending; either 1 or 2. 
- `story_id`: story id. 

### Data Splits

| name  |validation |test|
|-------|-----:|---:|
|lang|1871|1871|
