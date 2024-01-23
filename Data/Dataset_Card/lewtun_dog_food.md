---
annotations_creators:
- found
language_creators:
- found
language:
- en
license:
- unknown
multilinguality:
- monolingual
pretty_name: Dog vs Food Dataset
size_categories:
- 1K<n<10K
source_datasets:
- original
task_categories:
- image-classification
task_ids:
- multi-class-image-classification
---

# Dataset Card for the Dog 🐶 vs. Food 🍔 (a.k.a. Dog Food) Dataset

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

- **Homepage:**: https://github.com/qw2243c/Image-Recognition-Dogs-Fried-Chicken-or-Blueberry-Muffins-
- **Repository:** : https://github.com/qw2243c/Image-Recognition-Dogs-Fried-Chicken-or-Blueberry-Muffins-
- **Paper:** : N/A
- **Leaderboard:**: N/A
- **Point of Contact:**: @sasha

### Dataset Summary

This is a dataset for multiclass image classification, between 'dog', 'chicken', and 'muffin' classes. 

The 'dog' class contains images of dogs that look like fried chicken and some that look like images of muffins, while the 'chicken' and 'muffin' classes contains images of (you guessed it) fried chicken and muffins 😋

### Supported Tasks and Leaderboards

TBC

### Languages

The labels are in English (['dog', 'chicken', 'muffin'])

## Dataset Structure

### Data Instances
A sample from the training set is provided below:

```
{
{'image': <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=300x470 at 0x7F176094EF28>, 
'label': 0}

}
```

### Data Fields


- img: A `PIL.JpegImageFile` object containing the 300x470. image. Note that when accessing the image column: `dataset[0]["image"]` the image file is automatically decoded. Decoding of a large number of image files might take a significant amount of time. Thus it is important to first query the sample index before the `"image"` column, *i.e.* `dataset[0]["image"]` should **always** be preferred over `dataset["image"][0]`
- label: 0-1 with the following correspondence
         0 dog
         1 food

### Data Splits

Train (1875 images) and Test (625 images)

## Dataset Creation

### Curation Rationale

N/A

### Source Data

#### Initial Data Collection and Normalization

This dataset was taken from the [qw2243c/Image-Recognition-Dogs-Fried-Chicken-or-Blueberry-Muffins?](https://github.com/qw2243c/Image-Recognition-Dogs-Fried-Chicken-or-Blueberry-Muffins-) Github repository and randomly splitting 25% of the data for validation.

### Annotations

#### Annotation process

This data was scraped from the internet and annotated based on the query words.


### Personal and Sensitive Information

N/A

## Considerations for Using the Data

### Social Impact of Dataset

N/A

### Discussion of Biases

This dataset is balanced -- it has an equal number of images of dogs (1000) compared to chicken (1000 and muffin (1000). This should be taken into account when evaluating models.

### Other Known Limitations

N/A

## Additional Information

### Dataset Curators

This dataset was created by @lanceyjt, @yl3829, @wesleytao, @qw2243c and @asyouhaveknown

### Licensing Information

No information is indicated on the original [github repository](https://github.com/qw2243c/Image-Recognition-Dogs-Fried-Chicken-or-Blueberry-Muffins-).

### Citation Information

N/A

### Contributions

Thanks to [@lewtun](https://github.com/lewtun) for adding this dataset.
