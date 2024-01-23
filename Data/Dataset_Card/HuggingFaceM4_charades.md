---
annotations_creators:
- crowdsourced
language_creators:
- crowdsourced
language:
- en
license:
- other
multilinguality:
- monolingual
size_categories:
- 1K<n<10K
source_datasets:
- original
task_categories:
- other
task_ids: []
paperswithcode_id: charades
pretty_name: Charades
tags: []
---

# Dataset Card for Charades

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

- **Homepage:** https://prior.allenai.org/projects/charades
- **Repository:** https://github.com/gsig/charades-algorithms
- **Paper:** https://arxiv.org/abs/1604.01753
- **Leaderboard:** https://paperswithcode.com/sota/action-classification-on-charades
- **Point of Contact:** mailto: vision.amt@allenai.org 

### Dataset Summary

Charades is dataset composed of 9848 videos of daily indoors activities collected through Amazon Mechanical Turk. 267 different users were presented with a sentence, that includes objects and actions from a fixed vocabulary, and they recorded a video acting out the sentence (like in a game of Charades). The dataset contains 66,500 temporal annotations for 157 action classes, 41,104 labels for 46 object classes, and 27,847 textual descriptions of the videos

### Supported Tasks and Leaderboards

- `multilabel-action-classification`: The goal of this task is to classify actions happening in a video. This is a multilabel classification. The leaderboard is available [here](https://paperswithcode.com/sota/action-classification-on-charades)


### Languages

The annotations in the dataset are in English.

## Dataset Structure

### Data Instances

```
{
  "video_id": "46GP8",
  "video": "/home/amanpreet_huggingface_co/.cache/huggingface/datasets/downloads/extracted/3f022da5305aaa189f09476dbf7d5e02f6fe12766b927c076707360d00deb44d/46GP8.mp4",
  "subject": "HR43",
  "scene": "Kitchen",
  "quality": 6,
  "relevance": 7,
  "verified": "Yes",
  "script": "A person cooking on a stove while watching something out a window.",
  "objects": ["food", "stove", "window"],
  "descriptions": [
    "A person cooks food on a stove before looking out of a window."
  ],
  "labels": [92, 147],
  "action_timings": [
    [11.899999618530273, 21.200000762939453],
    [0.0, 12.600000381469727]
  ],
  "length": 24.829999923706055
}
```

### Data Fields

- `video_id`: `str` Unique identifier for each video.
- `video`: `str` Path to the video file
- `subject`: `str` Unique identifier for each subject in the dataset
- `scene`: `str` One of 15 indoor scenes in the dataset, such as Kitchen
- `quality`: `int` The quality of the video judged by an annotator (7-point scale, 7=high quality), -100 if missing
- `relevance`: `int` The relevance of the video to the script judged by an annotated (7-point scale, 7=very relevant), -100 if missing
- `verified`: `str` 'Yes' if an annotator successfully verified that the video matches the script, else 'No'
- `script`: `str` The human-generated script used to generate the video
- `descriptions`: `List[str]` List of descriptions by annotators watching the video
- `labels`: `List[int]` Multi-label actions found in the video. Indices from 0 to 156.
- `action_timings`: `List[Tuple[int, int]]` Timing where each of the above actions happened.
- `length`: `float` The length of the video in seconds

<details>
  <summary>
  Click here to see the full list of Charades class labels mapping:
  </summary>
  
  |id|Class|
  |--|-----|
  |c000 | Holding some clothes |
  |c001 | Putting clothes somewhere |
  |c002 | Taking some clothes from somewhere |
  |c003 | Throwing clothes somewhere |
  |c004 | Tidying some clothes |
  |c005 | Washing some clothes |
  |c006 | Closing a door |
  |c007 | Fixing a door |
  |c008 | Opening a door |
  |c009 | Putting something on a table |
  |c010 | Sitting on a table |
  |c011 | Sitting at a table |
  |c012 | Tidying up a table |
  |c013 | Washing a table |
  |c014 | Working at a table |
  |c015 | Holding a phone/camera |
  |c016 | Playing with a phone/camera |
  |c017 | Putting a phone/camera somewhere |
  |c018 | Taking a phone/camera from somewhere |
  |c019 | Talking on a phone/camera |
  |c020 | Holding a bag |
  |c021 | Opening a bag |
  |c022 | Putting a bag somewhere |
  |c023 | Taking a bag from somewhere |
  |c024 | Throwing a bag somewhere |
  |c025 | Closing a book |
  |c026 | Holding a book |
  |c027 | Opening a book |
  |c028 | Putting a book somewhere |
  |c029 | Smiling at a book |
  |c030 | Taking a book from somewhere |
  |c031 | Throwing a book somewhere |
  |c032 | Watching/Reading/Looking at a book |
  |c033 | Holding a towel/s |
  |c034 | Putting a towel/s somewhere |
  |c035 | Taking a towel/s from somewhere |
  |c036 | Throwing a towel/s somewhere |
  |c037 | Tidying up a towel/s |
  |c038 | Washing something with a towel |
  |c039 | Closing a box |
  |c040 | Holding a box |
  |c041 | Opening a box |
  |c042 | Putting a box somewhere |
  |c043 | Taking a box from somewhere |
  |c044 | Taking something from a box |
  |c045 | Throwing a box somewhere |
  |c046 | Closing a laptop |
  |c047 | Holding a laptop |
  |c048 | Opening a laptop |
  |c049 | Putting a laptop somewhere |
  |c050 | Taking a laptop from somewhere |
  |c051 | Watching a laptop or something on a laptop |
  |c052 | Working/Playing on a laptop |
  |c053 | Holding a shoe/shoes |
  |c054 | Putting shoes somewhere |
  |c055 | Putting on shoe/shoes |
  |c056 | Taking shoes from somewhere |
  |c057 | Taking off some shoes |
  |c058 | Throwing shoes somewhere |
  |c059 | Sitting in a chair |
  |c060 | Standing on a chair |
  |c061 | Holding some food |
  |c062 | Putting some food somewhere |
  |c063 | Taking food from somewhere |
  |c064 | Throwing food somewhere |
  |c065 | Eating a sandwich |
  |c066 | Making a sandwich |
  |c067 | Holding a sandwich |
  |c068 | Putting a sandwich somewhere |
  |c069 | Taking a sandwich from somewhere |
  |c070 | Holding a blanket |
  |c071 | Putting a blanket somewhere |
  |c072 | Snuggling with a blanket |
  |c073 | Taking a blanket from somewhere |
  |c074 | Throwing a blanket somewhere |
  |c075 | Tidying up a blanket/s |
  |c076 | Holding a pillow |
  |c077 | Putting a pillow somewhere |
  |c078 | Snuggling with a pillow |
  |c079 | Taking a pillow from somewhere |
  |c080 | Throwing a pillow somewhere |
  |c081 | Putting something on a shelf |
  |c082 | Tidying a shelf or something on a shelf |
  |c083 | Reaching for and grabbing a picture |
  |c084 | Holding a picture |
  |c085 | Laughing at a picture |
  |c086 | Putting a picture somewhere |
  |c087 | Taking a picture of something |
  |c088 | Watching/looking at a picture |
  |c089 | Closing a window |
  |c090 | Opening a window |
  |c091 | Washing a window |
  |c092 | Watching/Looking outside of a window |
  |c093 | Holding a mirror |
  |c094 | Smiling in a mirror |
  |c095 | Washing a mirror |
  |c096 | Watching something/someone/themselves in a mirror |
  |c097 | Walking through a doorway |
  |c098 | Holding a broom |
  |c099 | Putting a broom somewhere |
  |c100 | Taking a broom from somewhere |
  |c101 | Throwing a broom somewhere |
  |c102 | Tidying up with a broom |
  |c103 | Fixing a light |
  |c104 | Turning on a light |
  |c105 | Turning off a light |
  |c106 | Drinking from a cup/glass/bottle |
  |c107 | Holding a cup/glass/bottle of something |
  |c108 | Pouring something into a cup/glass/bottle |
  |c109 | Putting a cup/glass/bottle somewhere |
  |c110 | Taking a cup/glass/bottle from somewhere |
  |c111 | Washing a cup/glass/bottle |
  |c112 | Closing a closet/cabinet |
  |c113 | Opening a closet/cabinet |
  |c114 | Tidying up a closet/cabinet |
  |c115 | Someone is holding a paper/notebook |
  |c116 | Putting their paper/notebook somewhere |
  |c117 | Taking paper/notebook from somewhere |
  |c118 | Holding a dish |
  |c119 | Putting a dish/es somewhere |
  |c120 | Taking a dish/es from somewhere |
  |c121 | Wash a dish/dishes |
  |c122 | Lying on a sofa/couch |
  |c123 | Sitting on sofa/couch |
  |c124 | Lying on the floor |
  |c125 | Sitting on the floor |
  |c126 | Throwing something on the floor |
  |c127 | Tidying something on the floor |
  |c128 | Holding some medicine |
  |c129 | Taking/consuming some medicine |
  |c130 | Putting groceries somewhere |
  |c131 | Laughing at television |
  |c132 | Watching television |
  |c133 | Someone is awakening in bed |
  |c134 | Lying on a bed |
  |c135 | Sitting in a bed |
  |c136 | Fixing a vacuum |
  |c137 | Holding a vacuum |
  |c138 | Taking a vacuum from somewhere |
  |c139 | Washing their hands |
  |c140 | Fixing a doorknob |
  |c141 | Grasping onto a doorknob |
  |c142 | Closing a refrigerator |
  |c143 | Opening a refrigerator |
  |c144 | Fixing their hair |
  |c145 | Working on paper/notebook |
  |c146 | Someone is awakening somewhere |
  |c147 | Someone is cooking something |
  |c148 | Someone is dressing |
  |c149 | Someone is laughing |
  |c150 | Someone is running somewhere |
  |c151 | Someone is going from standing to sitting |
  |c152 | Someone is smiling |
  |c153 | Someone is sneezing |
  |c154 | Someone is standing up from somewhere |
  |c155 | Someone is undressing |
  |c156 | Someone is eating something |
</details>

### Data Splits


|             |train  |validation| test  |
|-------------|------:|---------:|------:|
|# of examples|1281167|50000     |100000 |


## Dataset Creation

### Curation Rationale

> Computer vision has a great potential to help our daily lives by searching for lost keys, watering flowers or reminding us to take a pill. To succeed with such tasks, computer vision methods need to be trained from real and diverse examples of our daily dynamic scenes. While most of such scenes are not particularly exciting, they typically do not appear on YouTube, in movies or TV broadcasts. So how do we collect sufficiently many diverse but boring samples representing our lives? We propose a novel Hollywood in Homes approach to collect such data. Instead of shooting videos in the lab, we ensure diversity by distributing and crowdsourcing the whole process of video creation from script writing to video recording and annotation.

### Source Data

#### Initial Data Collection and Normalization

> Similar to filming, we have a three-step process for generating a video. The first step is generating the script of the indoor video. The key here is to allow workers to generate diverse scripts yet ensure that we have enough data for each category. The second step in the process is to use the script and ask workers to record a video of that sentence being acted out. In the final step, we ask the workers to verify if the recorded video corresponds to script, followed by an annotation procedure.

#### Who are the source language producers?

Amazon Mechnical Turk annotators

### Annotations

#### Annotation process

> Similar to filming, we have a three-step process for generating a video. The first step is generating the script of the indoor video. The key here is to allow workers to generate diverse scripts yet ensure that we have enough data for each category. The second step in the process is to use the script and ask workers to record a video of that sentence being acted out. In the final step, we ask the workers to verify if the recorded video corresponds to script, followed by an annotation procedure.

#### Who are the annotators?

Amazon Mechnical Turk annotators

### Personal and Sensitive Information

Nothing specifically mentioned in the paper.

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

AMT annotators

### Licensing Information

License for Non-Commercial Use

If this software is redistributed, this license must be included. The term software includes any source files, documentation, executables, models, and data.

This software and data is available for general use by academic or non-profit, or government-sponsored researchers.  It may also be used for evaluation purposes elsewhere.  This license does not grant the right to use this software or any derivation of it in a for-profit enterprise.  For commercial use, please contact The Allen Institute for Artificial Intelligence.

This license does not grant the right to modify and publicly release the data in any form.

This license does not grant the right to distribute the data to a third party in any form.

The subjects in this data should be treated with respect and dignity. This license only grants the right to publish short segments or still images in an academic publication where necessary to present examples, experimental results, or observations.

This software comes with no warranty or guarantee of any kind.  By using this software, the user accepts full liability.

The Allen Institute for Artificial Intelligence (C) 2016.

### Citation Information

```bibtex
@article{sigurdsson2016hollywood,
    author = {Gunnar A. Sigurdsson and G{\"u}l Varol and Xiaolong Wang and Ivan Laptev and Ali Farhadi and Abhinav Gupta},
    title = {Hollywood in Homes: Crowdsourcing Data Collection for Activity Understanding},
    journal = {ArXiv e-prints},
    eprint = {1604.01753}, 
    year = {2016},
    url = {http://arxiv.org/abs/1604.01753},
}
```

### Contributions

Thanks to [@apsdehal](https://github.com/apsdehal) for adding this dataset.
