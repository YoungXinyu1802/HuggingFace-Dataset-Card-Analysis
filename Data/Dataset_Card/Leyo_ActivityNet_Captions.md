---
annotations_creators:
- expert-generated
language_creators:
- crowdsourced
language:
- en
license:
- other
multilinguality:
- monolingual
pretty_name: ActivityNet Captions
size_categories:
- 10k<n<100K
source_datasets:
- original
task_categories:
- video-captionning
task_ids:
- closed-domain-qa
---


# Dataset Card for ActivityNet Captions
## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)

  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)
## Dataset Description
- **Homepage:** https://cs.stanford.edu/people/ranjaykrishna/densevid/
- **Paper:** https://arxiv.org/abs/1705.00754

### Dataset Summary
The ActivityNet Captions dataset connects videos to a series of temporally annotated sentence descriptions. Each sentence covers an unique segment of the video, describing multiple events that occur. These events may occur over very long or short periods of time and are not limited in any capacity, allowing them to co-occur. On average, each of the 20k videos contains 3.65 temporally localized sentences, resulting in a total of 100k sentences. We find that the number of sentences per video follows a relatively normal distribution. Furthermore, as the video duration increases, the number of sentences also increases. Each sentence has an average length of 13.48 words, which is also normally distributed. You can find more details of the dataset under the ActivityNet Captions Dataset section, and under supplementary materials in the paper.
### Languages
The captions in the dataset are in English.
## Dataset Structure
### Data Fields
- `video_id` : `str` unique identifier for the video
- `video_path`: `str` Path to the video file
-`duration`: `float32` Duration of the video
- `captions_starts`: `List_float32` List of timestamps denoting the time at which each caption starts 
- `captions_ends`: `List_float32` List of timestamps denoting the time at which each caption ends 
- `en_captions`: `list_str` List of english captions describing parts of the video

### Data Splits
|             |train  |validation| test  | Overall |
|-------------|------:|---------:|------:|------:|
|# of videos|10,009	|4,917     |4,885 |19,811 |
### Annotations
Quoting [ActivityNet Captions' paper](https://arxiv.org/abs/1705.00754): \
"Each annotation task was divided into two steps: (1)
Writing a paragraph describing all major events happening
in the videos in a paragraph, with each sentence of the paragraph describing one event, and (2) Labeling the
start and end time in the video in which each sentence in the
paragraph event occurred."
### Who annotated the dataset?
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
### Licensing Information
[More Information Needed]
### Citation Information
```bibtex
@InProceedings{tgif-cvpr2016,
@inproceedings{krishna2017dense,
    title={Dense-Captioning Events in Videos},
    author={Krishna, Ranjay and Hata, Kenji and Ren, Frederic and Fei-Fei, Li and Niebles, Juan Carlos},
    booktitle={International Conference on Computer Vision (ICCV)},
    year={2017}
}
```
### Contributions
Thanks to [@leot13](https://github.com/leot13) for adding this dataset.