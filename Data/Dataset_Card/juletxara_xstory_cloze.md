---
annotations_creators:
- found
language:
- en
- ru
- zh
- es
- ar
- hi
- id
- te
- sw
- eu
- my
language_creators:
- found
- expert-generated
license:
- cc-by-sa-4.0
multilinguality:
- multilingual
paperswithcode_id: null
pretty_name: XStoryCloze
size_categories:
- 1K<n<10K
source_datasets:
- extended|story_cloze
tags: []
task_categories:
- other
task_ids: []
dataset_info:
- config_name: en
  features:
  - name: story_id
    dtype: string
  - name: input_sentence_1
    dtype: string
  - name: input_sentence_2
    dtype: string
  - name: input_sentence_3
    dtype: string
  - name: input_sentence_4
    dtype: string
  - name: sentence_quiz1
    dtype: string
  - name: sentence_quiz2
    dtype: string
  - name: answer_right_ending
    dtype: int32
  splits:
  - name: train
    num_bytes: 118484
    num_examples: 360
  - name: eval
    num_bytes: 495572
    num_examples: 1511
  download_size: 573176
  dataset_size: 614056
- config_name: ru
  features:
  - name: story_id
    dtype: string
  - name: input_sentence_1
    dtype: string
  - name: input_sentence_2
    dtype: string
  - name: input_sentence_3
    dtype: string
  - name: input_sentence_4
    dtype: string
  - name: sentence_quiz1
    dtype: string
  - name: sentence_quiz2
    dtype: string
  - name: answer_right_ending
    dtype: int32
  splits:
  - name: train
    num_bytes: 202961
    num_examples: 360
  - name: eval
    num_bytes: 846720
    num_examples: 1511
  download_size: 1008802
  dataset_size: 1049681
- config_name: zh
  features:
  - name: story_id
    dtype: string
  - name: input_sentence_1
    dtype: string
  - name: input_sentence_2
    dtype: string
  - name: input_sentence_3
    dtype: string
  - name: input_sentence_4
    dtype: string
  - name: sentence_quiz1
    dtype: string
  - name: sentence_quiz2
    dtype: string
  - name: answer_right_ending
    dtype: int32
  splits:
  - name: train
    num_bytes: 116624
    num_examples: 360
  - name: eval
    num_bytes: 487501
    num_examples: 1511
  download_size: 563245
  dataset_size: 604125
- config_name: es
  features:
  - name: story_id
    dtype: string
  - name: input_sentence_1
    dtype: string
  - name: input_sentence_2
    dtype: string
  - name: input_sentence_3
    dtype: string
  - name: input_sentence_4
    dtype: string
  - name: sentence_quiz1
    dtype: string
  - name: sentence_quiz2
    dtype: string
  - name: answer_right_ending
    dtype: int32
  splits:
  - name: train
    num_bytes: 129011
    num_examples: 360
  - name: eval
    num_bytes: 538761
    num_examples: 1511
  download_size: 626890
  dataset_size: 667772
- config_name: ar
  features:
  - name: story_id
    dtype: string
  - name: input_sentence_1
    dtype: string
  - name: input_sentence_2
    dtype: string
  - name: input_sentence_3
    dtype: string
  - name: input_sentence_4
    dtype: string
  - name: sentence_quiz1
    dtype: string
  - name: sentence_quiz2
    dtype: string
  - name: answer_right_ending
    dtype: int32
  splits:
  - name: train
    num_bytes: 171008
    num_examples: 360
  - name: eval
    num_bytes: 701607
    num_examples: 1511
  download_size: 831735
  dataset_size: 872615
- config_name: hi
  features:
  - name: story_id
    dtype: string
  - name: input_sentence_1
    dtype: string
  - name: input_sentence_2
    dtype: string
  - name: input_sentence_3
    dtype: string
  - name: input_sentence_4
    dtype: string
  - name: sentence_quiz1
    dtype: string
  - name: sentence_quiz2
    dtype: string
  - name: answer_right_ending
    dtype: int32
  splits:
  - name: train
    num_bytes: 277601
    num_examples: 360
  - name: eval
    num_bytes: 1165329
    num_examples: 1511
  download_size: 1402058
  dataset_size: 1442930
- config_name: id
  features:
  - name: story_id
    dtype: string
  - name: input_sentence_1
    dtype: string
  - name: input_sentence_2
    dtype: string
  - name: input_sentence_3
    dtype: string
  - name: input_sentence_4
    dtype: string
  - name: sentence_quiz1
    dtype: string
  - name: sentence_quiz2
    dtype: string
  - name: answer_right_ending
    dtype: int32
  splits:
  - name: train
    num_bytes: 131364
    num_examples: 360
  - name: eval
    num_bytes: 549171
    num_examples: 1511
  download_size: 639655
  dataset_size: 680535
- config_name: te
  features:
  - name: story_id
    dtype: string
  - name: input_sentence_1
    dtype: string
  - name: input_sentence_2
    dtype: string
  - name: input_sentence_3
    dtype: string
  - name: input_sentence_4
    dtype: string
  - name: sentence_quiz1
    dtype: string
  - name: sentence_quiz2
    dtype: string
  - name: answer_right_ending
    dtype: int32
  splits:
  - name: train
    num_bytes: 293917
    num_examples: 360
  - name: eval
    num_bytes: 1215543
    num_examples: 1511
  download_size: 1468580
  dataset_size: 1509460
- config_name: sw
  features:
  - name: story_id
    dtype: string
  - name: input_sentence_1
    dtype: string
  - name: input_sentence_2
    dtype: string
  - name: input_sentence_3
    dtype: string
  - name: input_sentence_4
    dtype: string
  - name: sentence_quiz1
    dtype: string
  - name: sentence_quiz2
    dtype: string
  - name: answer_right_ending
    dtype: int32
  splits:
  - name: train
    num_bytes: 127745
    num_examples: 360
  - name: eval
    num_bytes: 528398
    num_examples: 1511
  download_size: 615263
  dataset_size: 656143
- config_name: eu
  features:
  - name: story_id
    dtype: string
  - name: input_sentence_1
    dtype: string
  - name: input_sentence_2
    dtype: string
  - name: input_sentence_3
    dtype: string
  - name: input_sentence_4
    dtype: string
  - name: sentence_quiz1
    dtype: string
  - name: sentence_quiz2
    dtype: string
  - name: answer_right_ending
    dtype: int32
  splits:
  - name: train
    num_bytes: 131524
    num_examples: 360
  - name: eval
    num_bytes: 540582
    num_examples: 1511
  download_size: 631228
  dataset_size: 672106
- config_name: my
  features:
  - name: story_id
    dtype: string
  - name: input_sentence_1
    dtype: string
  - name: input_sentence_2
    dtype: string
  - name: input_sentence_3
    dtype: string
  - name: input_sentence_4
    dtype: string
  - name: sentence_quiz1
    dtype: string
  - name: sentence_quiz2
    dtype: string
  - name: answer_right_ending
    dtype: int32
  splits:
  - name: train
    num_bytes: 381092
    num_examples: 360
  - name: eval
    num_bytes: 1627322
    num_examples: 1511
  download_size: 1967534
  dataset_size: 2008414
---

# Dataset Card for XStoryCloze

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

- **Homepage:** [https://cs.rochester.edu/nlp/rocstories/](https://cs.rochester.edu/nlp/rocstories/)
- **Repository:** [More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
- **Paper:** [Few-shot Learning with Multilingual Generative Language Models](https://arxiv.org/pdf/2112.10668.pdf)
- **Point of Contact:** [More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
- **Size of downloaded dataset files:** 2.03 MB
- **Size of the generated dataset:** 2.03 MB
- **Total amount of disk used:** 2.05 MB

### Dataset Summary

XStoryCloze consists of the professionally translated version of the [English StoryCloze dataset](https://cs.rochester.edu/nlp/rocstories/) (Spring 2016 version) to 10 non-English languages. This dataset is released by Meta AI.

### Supported Tasks and Leaderboards

commonsense reasoning

### Languages

en, ru, zh (Simplified), es (Latin America), ar, hi, id, te, sw, eu, my.

## Dataset Structure

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

This dataset is intended to be used for evaluating the zero- and few-shot learning capabilities of multlingual language models. We split the data for each language into train and test (360 vs. 1510 examples, respectively). The released data files for different languages maintain a line-by-line alignment.

| name  |train |test|
|-------|-----:|---:|
|en|360|1510|
|ru|360|1510|
|zh|360|1510|
|es|360|1510|
|ar|360|1510|
|hi|360|1510|
|id|360|1510|
|te|360|1510|
|sw|360|1510|
|eu|360|1510|
|my|360|1510|

## Dataset Creation

### Curation Rationale

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

#### Who are the source language producers?

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Annotations

#### Annotation process

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

#### Who are the annotators?

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Personal and Sensitive Information

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Discussion of Biases

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Other Known Limitations

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

## Additional Information

### Dataset Curators

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Licensing Information

XStoryCloze is opensourced under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/legalcode), the same license as the original English StoryCloze.

### Citation Information

```
@article{DBLP:journals/corr/abs-2112-10668,
  author    = {Xi Victoria Lin and
               Todor Mihaylov and
               Mikel Artetxe and
               Tianlu Wang and
               Shuohui Chen and
               Daniel Simig and
               Myle Ott and
               Naman Goyal and
               Shruti Bhosale and
               Jingfei Du and
               Ramakanth Pasunuru and
               Sam Shleifer and
               Punit Singh Koura and
               Vishrav Chaudhary and
               Brian O'Horo and
               Jeff Wang and
               Luke Zettlemoyer and
               Zornitsa Kozareva and
               Mona T. Diab and
               Veselin Stoyanov and
               Xian Li},
  title     = {Few-shot Learning with Multilingual Language Models},
  journal   = {CoRR},
  volume    = {abs/2112.10668},
  year      = {2021},
  url       = {https://arxiv.org/abs/2112.10668},
  eprinttype = {arXiv},
  eprint    = {2112.10668},
  timestamp = {Tue, 04 Jan 2022 15:59:27 +0100},
  biburl    = {https://dblp.org/rec/journals/corr/abs-2112-10668.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```


### Contributions

Thanks to [@juletx](https://github.com/juletx).