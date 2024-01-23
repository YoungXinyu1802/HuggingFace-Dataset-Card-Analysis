---
license: cc-by-4.0
---

# Dataset Card for [Dataset Name]

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

- **Homepage:** [https://google.github.io/localized-narratives/(https://google.github.io/localized-narratives/)
- **Repository:**: [https://github.com/google/localized-narratives](https://github.com/google/localized-narratives)
- **Paper:** [Connecting Vision and Language with Localized Narratives](https://arxiv.org/pdf/1912.03098.pdf)
- **Leaderboard:**
- **Point of Contact:**

### Dataset Summary

Localized Narratives, a new form of multimodal image annotations connecting vision and language.
We ask annotators to describe an image with their voice while simultaneously hovering their mouse over the region they are describing.
Since the voice and the mouse pointer are synchronized, we can localize every single word in the description.
This dense visual grounding takes the form of a mouse trace segment per word and is unique to our data.
We annotated 849k images with Localized Narratives: the whole COCO, Flickr30k, and ADE20K datasets, and 671k images of Open Images, all of which we make publicly available.

As of now, there is only the `OpenImages` subset, but feel free to contribute the other subset of Localized Narratives!

`OpenImages_captions` is similar to the `OpenImages` subset. The differences are that captions are groupped per image (images can have multiple captions). For this subset, `timed_caption`, `traces` and `voice_recording` are not available.

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

[More Information Needed]

## Dataset Structure

### Data Instances

Each instance has the following structure:
```
{
  dataset_id: 'mscoco_val2017',
  image_id: '137576',
  annotator_id: 93,
  caption: 'In this image there are group of cows standing and eating th...',
  timed_caption: [{'utterance': 'In this', 'start_time': 0.0, 'end_time': 0.4}, ...],
  traces: [[{'x': 0.2086, 'y': -0.0533, 't': 0.022}, ...], ...],
  voice_recording: 'coco_val/coco_val_137576_93.ogg'
}
```

### Data Fields

Each line represents one Localized Narrative annotation on one image by one annotator and has the following fields:

- `dataset_id`: String identifying the dataset and split where the image belongs, e.g. mscoco_val2017.
- `image_id` String identifier of the image, as specified on each dataset.
- `annotator_id` Integer number uniquely identifying each annotator.
- `caption` Image caption as a string of characters.
- `timed_caption` List of timed utterances, i.e. {utterance, start_time, end_time} where utterance is a word (or group of words) and (start_time, end_time) is the time during which it was spoken, with respect to the start of the recording.
- `traces` List of trace segments, one between each time the mouse pointer enters the image and goes away from it. Each trace segment is represented as a list of timed points, i.e. {x, y, t}, where x and y are the normalized image coordinates (with origin at the top-left corner of the image) and t is the time in seconds since the start of the recording. Please note that the coordinates can go a bit beyond the image, i.e. <0 or >1, as we recorded the mouse traces including a small band around the image.
- `voice_recording` Relative URL path with respect to https://storage.googleapis.com/localized-narratives/voice-recordings where to find the voice recording (in OGG format) for that particular image.

### Data Splits

[More Information Needed]

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

[More Information Needed]

### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

[More Information Needed]

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

[More Information Needed]

### Licensing Information

[More Information Needed]

### Citation Information

[More Information Needed]

### Contributions

Thanks to [@VictorSanh](https://github.com/VictorSanh) for adding this dataset.
