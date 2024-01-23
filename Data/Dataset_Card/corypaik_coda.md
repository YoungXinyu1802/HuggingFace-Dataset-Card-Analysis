---
annotations_creators:
- crowdsourced
language_creators:
- expert-generated
language:
- en
language_bcp47:
- en-US
license:
- apache-2.0
multilinguality:
- monolingual
pretty_name: CoDa
paperswithcode_id: coda
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories:
- text-scoring
task_ids:
- text-scoring-other-distribution-prediction
---

# Dataset Card for CoDa

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

- **Repository:** [nala-cub/coda](https://github.com/nala-cub/coda)
- **Paper:** [The World of an Octopus: How Reporting Bias Influences a Language Model's Perception of Color](https://arxiv.org/abs/2110.08182)
- **Point of Contact:** [Cory Paik](cory.paik@colorado.edu)

### Dataset Summary
*The Color Dataset* (CoDa) is a probing dataset to evaluate the representation of visual properties in language models. CoDa consists of color distributions for 521 common objects, which are split into 3 groups. We denote these groups as Single, Multi, and Any, which represents the typical object of each group.

The default configuration of CoDa uses 10 CLIP-style templates (e.g. "A photo of a [object]"), and 10 cloze-style templates (e.g. "Everyone knows most [object] are
[color]." )

### Supported Tasks and Leaderboards

This version of the dataset consists of the filtered and templated examples as cloze style questions. See the [GitHub](https://github.com/nala-cub/coda) repo for the raw data (e.g. unfiltered annotations) as well as example usage with GPT-2, RoBERTa, ALBERT, and CLIP.

### Languages

The text in the dataset is in English. The associated BCP-47 code is `en-US`.

## Dataset Structure

### Data Instances

An example looks like this:

```json
{
  "text": "All rulers are [MASK].",
  "label": [
    0.0181818176, 0.0363636352, 0.3077272773, 0.0181818176, 0.0363636352,
    0.086363636, 0.0363636352, 0.0363636352, 0.0363636352, 0.086363636,
    0.301363647
  ],
  "template_group": 1,
  "template_idx": 0,
  "class_id": "/m/0hdln",
  "display_name": "Ruler",
  "object_group": 2,
  "ngram": "ruler"
}
```

### Data Fields

- `text`: The templated example. What this is depends on the value of `template_group`.
  - `template_group=0`: A CLIP style example. There are no `[MASK]` tokens in these examples.
  - `template_group=1`: A cloze style example. Note that all templates have `[MASK]` as the last word, but in most cases, the period should be included.
- `label`: A list of probability values for the 11 colors. Note that these are sorted by the alphabetic order of the 11 colors (black, blue, brown, gray, green, orange, pink, purple, red, white, yellow).
- `template_group`: Type of template, `0` corresponds to A CLIP style template (`clip-imagenet`), and `1` corresponds to A cloze style templates (`text-masked`).
- `template_idx`: The index of the template out of all templates
- `class_id`: The Corresponding [OpenImages v6](https://storage.googleapis.com/openimages/web/index.html) `ClassID`.
- `display_name`: The Corresponding [OpenImages v6](https://storage.googleapis.com/openimages/web/index.html) `DisplayName`.
- `object_group`: Object Group, values correspond to `Single`, `Multi`, and `Any`.
- `ngram`: Corresponding n-gram used for lookups.

### Data Splits

Object Splits:

| Group  | All | Train | Valid | Test |
| ------ | --- | ----- | ----- | ---- |
| Single | 198 |   118 |    39 |   41 |
| Multi  | 208 |   124 |    41 |   43 |
| Any    | 115 |    69 |    23 |   23 |
| Total  | 521 |   311 |   103 |  107 |


Example Splits:

| Group  |  All  | Train | Valid | Test |
| ------ | ----- | ----- | ----- | ---- |
| Single |  3946 |  2346 |   780 |  820 |
| Multi  |  4146 |  2466 |   820 |  860 |
| Any    |  2265 |  1352 |   460 |  453 |
| Total  | 10357 |  6164 |  2060 | 2133 |


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

CoDa is licensed under the Apache 2.0 license.

### Citation Information

```
@misc{paik2021world,
      title={The World of an Octopus: How Reporting Bias Influences a Language Model's Perception of Color},
      author={Cory Paik and Stéphane Aroca-Ouellette and Alessandro Roncone and Katharina Kann},
      year={2021},
      eprint={2110.08182},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

### Contributions

Thanks to [@github-username](https://github.com/<github-username>) for adding this dataset.
