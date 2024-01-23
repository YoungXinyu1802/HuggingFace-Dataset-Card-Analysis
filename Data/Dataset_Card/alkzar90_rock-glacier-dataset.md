---
annotations_creators:
- human-curator
language:
- en
license:
- mit
pretty_name: RockGlacier
size_categories:
- 1K<n<10K
source_datasets:
- original
task_categories:
- image-classification
task_ids:
- multi-class-image-classification
---
# Dataset Card for Rock Glacier Detection
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
- **Homepage:** [RockGlacier Homepage](https://github.com/alcazar90/rock-glacier-detection)
- **Repository:** [alcazar90/rock-glacier-detection](https://github.com/alcazar90/rock-glacier-detection)
- **Paper:** N/A
- **Leaderboard:** N/A
- **Point of Contact:** N/A

### Dataset Summary

![](https://huggingface.co/datasets/alkzar90/rock-glacier-dataset/resolve/main/assets/rock-glacier-portrait2.png)

Rock Glacier Detection dataset with satelital images of rock glaciers in the Chilean Andes. 

### Supported Tasks and Leaderboards
- `image-classification`: Based on a satelitel images (from sentinel2), the goal of this task is to predict a rock glacier in the geographic area, if there any.
- `image-segmentation`: ...

### Languages
Spanish

## Dataset Structure

### Data Instances

A sample from the image-classification training set is provided below:

```
df = load_dataset("alkzar90/rock-glacier-dataset", name="image-classification")

df["train"][666]

> {'image': <PIL.PngImagePlugin.PngImageFile image mode=RGBA size=128x128 at 0x7FB2EC58C6D0>,
 'labels': 0,
 'path': 'train/cordillera/1512.png'
}
```

A sample from the image-segmentation training set is provided below:

```
df = load_dataset("alkzar90/rock-glacier-dataset", name="image-segmentation")

df["train"][666]

> {'image': <PIL.PngImagePlugin.PngImageFile image mode=RGBA size=128x128 at 0x7FB2EB7C1160>,
 'masks': <PIL.PngImagePlugin.PngImageFile image mode=RGBA size=128x128 at 0x7FB2EC5A08E0>,
 'path': 'train/cordillera/1512.png'}
```

### Data Fields

The data instances have the following fields:

- `image`: A `PIL.Image.Image` object containing the image. Note that when accessing the image column: `dataset[0]["image"]` the image file is automatically decoded. Decoding of a large number of image files might take a significant amount of time. Thus it is important to first query the sample index before the `"image"` column, *i.e.* `dataset[0]["image"]` should **always** be preferred over `dataset["image"][0]`.
- `labels`: an `int` classification label.

Class Label Mappings:

```json
{
  "cordillera": 0
  "glaciar": 1,
}
```

### Data Splits

 
|             |train|validation|  test|
|-------------|----:|---------:|-----:|
|# of examples|7875 |1125      |2700  |

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

```
@ONLINE {rock-glacier-dataset,
    author="CMM - Glaciares (UChile)",
    title="Rock Glacier Dataset",
    month="October",
    year="2022",
    url="https://github.com/alcazar90/rock-glacier-detection"
}
```

### Contributions

Thanks to... 
