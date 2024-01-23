---
annotations_creators:
- expert-generated
language_creators:
- other
language:
- en
- ko
language_bcp47:
- en-US
- ko-KR
license:
- cc-by-nc-nd-4.0
multilinguality:
- translation
- multilingual
pretty_name: English-Korean Multitarget Ted Talks Task (MTTT)
task_categories:
- conditional-text-generation
task_ids:
- machine-translation
---

# Dataset Card for english-korean-multitarget-ted-talks-task

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

- **Homepage:** https://www.cs.jhu.edu/~kevinduh/a/multitarget-tedtalks/

### Dataset Summary

- Parallel English-Korean Text Corpus
- Text was originally transcribed to English from various Ted Talks, then translated to Korean by TED translators
- Approximately 166k train, 2k validation, and 2k test sentence pairs.

### Supported Tasks and Leaderboards

- Machine Translation

### Languages

- English
- Korean

## Additional Information

### Dataset Curators

Kevin Duh, "The Multitarget TED Talks Task", http://www.cs.jhu.edu/~kevinduh/a/multitarget-tedtalks/, 2018

### Licensing Information

TED makes its collection available under the Creative Commons BY-NC-ND license. Please acknowledge TED when using this data. We acknowledge the authorship of TED Talks (BY condition). We are not redistributing the transcripts for commercial purposes (NC condition) nor making derivative works of the original contents (ND condition).

### Citation Information

@misc{duh18multitarget,
      author = {Kevin Duh},
      title = {The Multitarget TED Talks Task},
      howpublished = {\url{http://www.cs.jhu.edu/~kevinduh/a/multitarget-tedtalks/}},
      year = {2018},
}