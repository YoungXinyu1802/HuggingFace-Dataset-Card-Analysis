---
annotations_creators:
- crowdsourced
language_creators:
- crowdsourced
language: []
license:
- apache-2.0
multilinguality: []
size_categories:
- 1K<n<10K
source_datasets:
- original
task_categories:
- image-classification
task_ids: []
pretty_name: Wildfire image classification dataset collected using images from web
  searches.
---

# Dataset Card for OpenFire

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

- **Homepage:** https://pyronear.org/pyro-vision/datasets.html#openfire
- **Repository:** https://github.com/pyronear/pyro-vision
- **Point of Contact:** Pyronear <https://pyronear.org/en/>

### Dataset Summary

OpenFire is an image classification dataset for wildfire detection, collected
from web searches.

### Supported Tasks and Leaderboards

- `image-classification`: The dataset can be used to train a model for Image Classification.

### Languages

English

## Dataset Structure

### Data Instances

A data point comprises an image URL and its binary label.

```
{
  'image_url': 'https://cdn-s-www.ledauphine.com/images/13C08274-6BA6-4577-B3A0-1E6C1B2A573C/FB1200/photo-1338240831.jpg',
  'is_wildfire': true,
}
```

### Data Fields

- `image_url`: the download URL of the image.
- `is_wildfire`: a boolean value specifying whether there is an ongoing wildfire on the image.

### Data Splits

The data is split into training and validation sets. The training set contains 7143 images and the validation set 792 images.

## Dataset Creation

### Curation Rationale

The curators state that the current wildfire classification datasets typically contain close-up shots of wildfires, with limited variations of weather conditions, luminosity and backrgounds,
making it difficult to assess for real world performance. They argue that the limitations of datasets have partially contributed to the failure of some algorithms in coping
with sun flares, foggy / cloudy weather conditions and small scale.

### Source Data

#### Initial Data Collection and Normalization

OpenFire was collected using images publicly indexed by the search engine DuckDuckGo using multiple relevant queries. The images were then manually cleaned to remove errors.

### Annotations

#### Annotation process

Each web search query was designed to yield a single label (with wildfire or without), and additional human verification was used to remove errors.

#### Who are the annotators?

François-Guillaume Fernandez

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

François-Guillaume Fernandez

### Licensing Information

[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).

### Citation Information

```
@software{Pyronear_PyroVision_2019,
    title={Pyrovision: wildfire early detection},
    author={Pyronear contributors},
    year={2019},
    month={October},
    publisher = {GitHub},
    howpublished = {\url{https://github.com/pyronear/pyro-vision}}
}
```
