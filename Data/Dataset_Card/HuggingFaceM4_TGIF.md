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
pretty_name: TGIF
size_categories:
- 100K<n<1M
source_datasets:
- original
task_categories:
- question-answering
- visual-question-answering
task_ids:
- closed-domain-qa
---


# Dataset Card for [Dataset Name]
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
- **Homepage:** http://raingo.github.io/TGIF-Release/
- **Repository:** https://github.com/raingo/TGIF-Release
- **Paper:** https://arxiv.org/abs/1604.02748
- **Point of Contact:** mailto: yli@cs.rochester.edu
### Dataset Summary
The Tumblr GIF (TGIF) dataset contains 100K animated GIFs and 120K sentences describing visual content of the animated GIFs. The animated GIFs have been collected from Tumblr, from randomly selected posts published between May and June of 2015. We provide the URLs of animated GIFs in this release. The sentences are collected via crowdsourcing, with a carefully designed annotation interface that ensures high quality dataset. We provide one sentence per animated GIF for the training and validation splits, and three sentences per GIF for the test split. The dataset shall be used to evaluate animated GIF/video description techniques.
### Languages
The captions in the dataset are in English.
## Dataset Structure
### Data Fields
- `video_path`: `str` "https://31.media.tumblr.com/001a8b092b9752d260ffec73c0bc29cd/tumblr_ndotjhRiX51t8n92fo1_500.gif"
-`video_bytes`: `large_bytes` video file in bytes format
- `en_global_captions`: `list_str` List of english captions describing the entire video

### Data Splits
|             |train  |validation| test  | Overall |
|-------------|------:|---------:|------:|------:|
|# of GIFs|80,000	|10,708     |11,360 |102,068 |
### Annotations
Quoting [TGIF paper](https://arxiv.org/abs/1604.02748): \
"We annotated animated GIFs with natural language descriptions using the crowdsourcing service CrowdFlower.
We carefully designed our annotation task with various
quality control mechanisms to ensure the sentences are both
syntactically and semantically of high quality.
A total of 931 workers participated in our annotation
task. We allowed workers only from Australia, Canada, New Zealand, UK and USA in an effort to collect fluent descriptions from native English speakers. Figure 2 shows the
instructions given to the workers. Each task showed 5 animated GIFs and asked the worker to describe each with one
sentence. To promote language style diversity, each worker
could rate no more than 800 images (0.7% of our corpus).
We paid 0.02 USD per sentence; the entire crowdsourcing
cost less than 4K USD. We provide details of our annotation
task in the supplementary material."
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
This dataset is provided to be used for approved non-commercial research purposes. No personally identifying information is available in this dataset.
### Citation Information
```bibtex
@InProceedings{tgif-cvpr2016,
  author = {Li, Yuncheng and Song, Yale and Cao, Liangliang and Tetreault, Joel and Goldberg, Larry and Jaimes, Alejandro and Luo, Jiebo},
  title = "{TGIF: A New Dataset and Benchmark on Animated GIF Description}",
  booktitle = {The IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
  month = {June},
  year = {2016}
}
```
### Contributions
Thanks to [@leot13](https://github.com/leot13) for adding this dataset.
