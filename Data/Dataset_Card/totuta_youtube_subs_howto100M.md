---
dataset_info:
  features:
  - name: instruction
    dtype: string
  - name: response
    dtype: string
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 1260882571
    num_examples: 309136
  download_size: 668637627
  dataset_size: 1260882571
license: apache-2.0
task_categories:
- conversational
language:
- en
pretty_name: 'YouTube Subtitles of Instructions: HowTo100M'
size_categories:
- 10M<n<100M
---

# Dataset Card for youtube_subs_howto100M

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

- **Homepage:** [HowTo100M homepage](https://www.di.ens.fr/willow/research/howto100m/)
- **Repository:** [HowTo100M repository](https://github.com/antoine77340/howto100m)
- **Paper:** [HowTo100M: Learning a Text-Video Embedding by Watching Hundred Million Narrated Video Clips](https://arxiv.org/abs/1906.03327)

### Dataset Summary

The `youtube_subs_howto100M` dataset is an English-language dataset of instruction-response pairs extracted from 309136 YouTube videos. The dataset was orignally inspired by and sourced from the HowTo100M dataset, which was developed for natural language search for video clips.

### Supported Tasks and Leaderboards

- `conversational`: The dataset can be used to train a model for instruction(request) and a long form of response generation. This dataset is originally prepared for the [Open Assistant](https://github.com/LAION-AI/Open-Assistant), which is an open-source chat-based large language model.

### Languages

Currently, all text in the dataset is in English.

## Dataset Structure

### Data Instances

A typical data point comprises an `instruction`, `response`, and a `source`

An example from the youtube_subs_howto100M looks as follows:
```
{"instruction": "Please explain how to remove plaque without going to the dentist 2016", "response": "mineral deposit on teeth is known as tartar or plaque as time passes by the amount of tartar increases and if you don't take care it can cause periodontitis of course the best way to remove tartar is paying a visit to your dentist but another way is to remove plaque at your home in this video you will learn how to remove plaque at home to do so you will need baking soda toothbrush salt you hydrogen peroxide cup you gentle pick you water anti septic mouthwash you step one first mix one tablespoon of bacon soda with TSP of salt into the cup after you at the toothbrush with warm water dip it into the mixture scrub teeth with an in spit continue the same process for five minutes step to mix a cup full with hydrogen peroxide with cup of warm water and rinse your mouth for one minute then spit and rinse with cup of cool water step 3 rub the yellow tartar from teeth with a dental pick be careful not to scrape the gums it may irritate and damage them step 4 rinse mouth with an antiseptic mouthwash and repeat every second day here are some other advice is to help you keep your beautiful smile tomatoes and strawberries tomatoes and strawberries are rich in vitamin C which is excellent for oral health you can rub these fruits directly onto your teeth and let it sit for five minutes this way the tartar buildup will soften cheese being a Swiss or cheddar before meals helps neutralize the acids that involve black creation an ingredient in a cheese works as a barrier agent guava both guava fruit and leaves are considered excellent anti black agents to help remove plaque accumulated on the teeth and gums gloss they have anti-inflammatory and analgesic properties that help reduce swelling and pain in the gums brush your teeth regularly with a soft brush and make vertical movements pay attention on the space between gums and teeth floss regularly consuming spicy food stimulates syllabary glands that way saliva cleans mouth in a natural way five bacteria with an orange peel before going to bed and don't rinse mouth", "source": "YouTube"}
```

### Data Fields

- `instruction`: a request for an explanation.
- `response`: a long text of response sentences, currently not punctuated.
- `source`: the source of the datapoint, currently all `YouTube`.

### Data Splits

The dataset does not have train/valid/eval splits now.

## Dataset Creation

### Curation Rationale

The original HowTo100M dataset was developed for natural language search for video clips, not necessarily for conversational or chat based training. However, the long monologue response can be regarded as a sequence of answers for a question, which can be induced from the video title. Therefore, a good amount of high-quality request-response(long) pairs can be extracted from HowTo100M youtube videos.

Concretely, this dataset is curated like below:

```
for each video in YouTube100M dataset
  if video_title starts with `how to`
    add `Please explain` to the title to make an `instruction`
    extract subtitles from the video to make a `response`
```  

### Source Data

#### Initial Data Collection and Normalization

Refer to the [Curation Rationale](#curation-rationale)

#### Who are the source language producers?

The language producers are YouTube users of the videos in HowTo100M dataset.

### Annotations

#### Annotation process

Refer to the [Curation Rationale](#curation-rationale)

#### Who are the annotators?

[N/A]

### Personal and Sensitive Information

[N/A]

## Considerations for Using the Data

### Social Impact of Dataset

[N/A]

### Discussion of Biases

[N/A]

### Other Known Limitations

Apache license 2.0

## Additional Information

### Dataset Curators

The youtube_subs_howto100M dataset was created by [@totuta](https://github.com/totuta). The original HowTo100M dataset was created by Antoine Miech, Dimitri Zhukov, Jean-Baptiste Alayrac, Makarand Tapaswi, Ivan Laptev, and Josef Sivic.

### Licensing Information

[N/A]

### Citation Information

@inproceedings{miech19howto100m,
   title={How{T}o100{M}: {L}earning a {T}ext-{V}ideo {E}mbedding by {W}atching {H}undred {M}illion {N}arrated {V}ideo {C}lips},
   author={Miech, Antoine and Zhukov, Dimitri and Alayrac, Jean-Baptiste and Tapaswi, Makarand and Laptev, Ivan and Sivic, Josef},
   booktitle={ICCV},
   year={2019},
}

### Contributions

Thanks to [@totuta](https://github.com/totuta) for adding this dataset.