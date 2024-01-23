---
annotations_creators:
- machine-generated
language_creators:
- expert-generated
language:
- en
license:
- mit
multilinguality:
- monolingual
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories:
- image-to-text
- text-to-image
task_ids:
- image-captioning
pretty_name: ShahNegar
---

# ShahNegar (A Plotted version of The Shahnameh)

This dataset is a plotted version of Ferdowsi's Shahnameh (which is a highly-regarded ancient set of Farsi poems) generated using DALL-E mini (aka [craiyon](https://www.craiyon.com/)). You can use this dataset using the code below: 

```python
from datasets import load_dataset

dataset = load_dataset("sadrasabouri/ShahNegar")
```

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

- **Paper:**
- **Point of Contact:** [Sadra Sabouri](mailto:sabouri.sadra@gmail.com)

### Dataset Summary

This dataset contains more than 30K images with their corresponding text from the Shahnameh. For each Shahnameh paragraph, we generated at most 9 images. Images corresponding to the same paragraphs have the same `id` field. There was a human annotation post-process in which we removed some harmful/private generated images from the dataset. After all we reached to more than 30K, 256 * 256 images.

### Supported Tasks and Leaderboards

The main purpose of making this dataset open source is because of its artistic value, but it can also be used for the below tasks:
+ text-to-image
+ image-to-text (image captioning)

### Languages

The Shahnameh was generally written in Farsi (Persian) but the translated version we used for this dataset - [satoor](https://www.sattor.com/english/Shahnameh.pdf) - was completely in English with no alignments for the corresponding Farsi poem. We are planning to add another field to dataset entries which is the corresponding Farsi poem as soon as possible.

## Dataset Structure

### Data Fields

Here is an instance of our dataset:

```json
{
    "image": <PIL Image Bytes>,
    "id": 0,
    "text": "He took up his abode in the mountains, and clad himself and his people in tiger-skins, and from him sprang all kindly nurture and the arts of clothing, till then unknown."
}
```
+ `image`: the image for given text.
+ `id`: the id for the text (**Not for the image**).
+ `text`: the English text for the image.


### Data Splits

This dataset has only a split (`train` split).

## Dataset Creation

The translated version of the Shahnameh was generally derived from the [satoor](https://www.sattor.com/english/Shahnameh.pdf) website. We first extracted texts from the pdf. After that, we divided paragraphs into sentences and give each sentence to the DALL-E mini model through its online API. It generated nine images for each sentence. After a few annotations, we came up with more than 30000 images.

### Annotations

#### Annotation process

Through the process of image generation, we noticed a bias in the DALL-E models towards the word `iran`. It was biased so that each sentence with this given word would have pictures from Iran's political figures which were usually totally irrelevant. The annotation process mainly focused to deal with these pictures. We removed those images which seems to be harmful to those figures and/or were irrelevant to the context.

#### Who are the annotators?

Mahsa Namdar and Sadra Sabouri were the annotators of this dataset.

### Personal and Sensitive Information

Since the textual data is easily downloadable and the images were generated through an image generation model there shouldn't be any personal information in this dataset. Just in case you find something harmful or violating of one's personal information please let us know. We will take proper action as soon as possible.

## Considerations for Using the Data

### Social Impact of Dataset

This dataset is mainly aimed to release for its artistic value. The process of generating images for the Shahnameh - which is one of the most important Farsi poem books - is our precious contribution. This dataset is not only used for this purpose but also can as a dataset in image-to-text and text-to-image tasks. 

### Discussion of Biases

The dataset's possible biases would come from the DALL-E mini biases. It's actually a good practice to check the dataset entries in order to find biases in that model. One it's worth mentioning in this work is the DALL-E mini model's bias for the word `iran` which nearly always comes up with images from political figures of this country.

### Other Known Limitations

There are constant debates in the literature about the limitations of machine-generated datasets. Some believe that since nowadays models are not perfect - and so do their output, it wouldn't be a good idea to use these artificially generated datasets as input to the new model. They suggest that by doing so we are actually limiting our accuracy by the model's accuracy which provided the primary dataset.

## Additional Information

### Dataset Curators

+ Emad Fatemizadeh: The general idea for generating a graphical version of Farsi poems was firstly introduced by him.
+ Sadra Sabouri: He looked up a translated version of the Shahnameh, extract and tokenized poems from it, and used the online DALL-E mini API to generate images from poems.
+ Mahsa Namdar: The process of annotation as a post-process on data has been held by her.

### Licensing Information

MIT

### Citation Information

[More Information Needed]

### Contributions

Thanks to [@sadrasabouri](https://github.com/sadrasabouri) for adding this dataset.
