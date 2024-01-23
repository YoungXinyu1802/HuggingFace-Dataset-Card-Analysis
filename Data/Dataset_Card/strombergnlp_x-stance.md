---
annotations_creators:
- crowdsourced
language_creators:
- found
language:
- de
- fr
license:
- mit
multilinguality:
- multilingual
size_categories:
- 10K<n<100K
source_datasets: []
task_categories:
- text-classification
task_ids:
- fact-checking
pretty_name: X-Stance
tags:
- stance-detection
---

# Dataset Card for X-Stance

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

- **Repository:** [https://github.com/ZurichNLP/xstance](https://github.com/ZurichNLP/xstance)
- **Paper:** [http://ceur-ws.org/Vol-2624/paper9.pdf](http://ceur-ws.org/Vol-2624/paper9.pdf), [https://arxiv.org/abs/2003.08385](https://arxiv.org/abs/2003.08385)
- **Point of Contact:** [Jannis Vamvas](https://twitter.com/j_vamvas)

### Dataset Summary

The x-stance dataset contains more than 150 political questions, and 67k comments written by candidates on those questions. The comments are partly German, partly French and Italian. The data have been extracted from the Swiss voting advice platform Smartvote.

### Languages

German, French/Italian

## Dataset Structure

### Data Instances
An example of 'train' looks as follows:
```
{
    'id': '0', 
    'question': 'Eine Volksinitiative fordert, dass die Gesamtfläche der Bauzonen in der Schweiz für die nächsten 20 Jahre auf dem heutigen Stand begrenzt wird. Befürworten Sie dieses Anliegen?', 
    'comment': 'Eine fixe Grösse verbieten, ist das falsche Mittel', '
    'label': 0
}
```

### Data Fields

- `id`: a 'string' feature.
- `question`: a 'string' expressing a claim/topic.
- `comment`: a 'string' to be classified for its stance to the source.
- `label`: 
```
            0: "AGAINST",
            1: "FAVOR"
```

### Data Splits

|languages|name|instances|
|---------|----|----:|
|de|train|33850|
|de|validation|2871|
|de|test|11891|
|fr|train|11790|
|fr|validation|1055|
|fr|test|5814|

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

[MIT License](https://github.com/ZurichNLP/xstance/blob/master/LICENSE)

### Citation Information

```
@article{vamvas2020x,
  title={X-stance: A multilingual multi-target dataset for stance detection},
  author={Vamvas, Jannis and Sennrich, Rico},
  journal={arXiv preprint arXiv:2003.08385},
  year={2020}
}
```

### Contributions

Thanks to [mkonxd](https://github.com/mkonxd), [leondz](https://github.com/leondz) for adding this dataset.
