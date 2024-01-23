---
annotations_creators:
- expert-generated
language:
- en
- fr
- de
language_creators:
- expert-generated
license:
- cc-by-nc-4.0
multilinguality:
- multilingual
pretty_name: Old Book Illustrations
size_categories:
- 1K<n<10K
source_datasets:
- original
tags:
- lam
- 1800-1900
task_categories:
- text-to-image
- image-to-text
- image-to-image
task_ids:
- image-captioning
---

# Dataset Card for Old Book Illustrations

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Discussion of Biases](#discussion-of-biases)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **[Homepage](https://www.oldbookillustrations.com/)**

### Dataset Summary

The Old Book Illustrations contains 4172 illustrations scanned from old books, this collection was collected & curated by the team of the website [Old Book Illustrations](https://www.oldbookillustrations.com/).
The webmaster of Old Book Illustrations kindly allowed us to scrap these information in order to create this dataset for the [BigLAM initiative](https://huggingface.co/biglam).

### Languages

The captions and descriptions are mostly in English but can contain some sentences from other languages such as French or German.
For instance you can find this description that contains a French sentence:

>The caption reads in the original French: Vue de l’aqueduc de Salones qui conduisait l’eau à Spalatro.

## Dataset Structure

Each row contains information gathered from the page of an illustration on the website [Old Book Illustrations](https://www.oldbookillustrations.com/). As of July 2022, there are 4172 illustrations in this dataset.

### Data Fields

* `rawscan`: the image as originally scanned from the book, without further processing
* `1600px`: the cleaned image, resized to a width of 1600 pixels (height can vary)
* `info_url`: URL to the illustration page on oldbookillustrations.com
* `ìnfo_src`: URL to an icon-sized version of the image
* `info_alt`: short description of the image
* `artist_name`: artist name
* `artist_date`: birth date of the artist
* `artist_countries`: list of the countries the artist is from
* `book_title`: original title of the book the illustration is extracted from
* `book_authors`: list of the authors of the book
* `book_publishers`: list of the publishers of the book
* `openlibrary-url`: URL to the openlibrary entry for the book
* `tags`: list of keywords for this illustration on oldbookillustrations.com
* `illustration_source_name`: list of the sources for this illustration
* `illustration_source_url`: list of the URL for these sources
* `illustration_subject`: category of the subject represented in the illustration
* `illustration_format`: category of the format of the illustration
* `image_title`: title of the image
* `image_caption`: caption of the image. Seems to be the caption that appears next to the image in the book, translated to English if in another language
* `image_description`: longer description of the image. If there is one, it also quotes the caption in the original language
* `rawscan_url`: URL to the rawscan image on oldbookillustration.com
* `1600px_url`: URL to the cleaned image on oldbookillustration.com

## Dataset Creation

### Curation Rationale

This collection was collected & curated by the team of the website [Old Book Illustrations](https://www.oldbookillustrations.com/).
This version contains all the data that was available on the website as of July 2022, but the website is being actively maintained so if you want more old book illustrations, make sure to check [Old Book Illustrations](https://www.oldbookillustrations.com/).

### Source Data

#### Initial Data Collection and Normalization

Initial data is gathered from the website [Old Book Illustrations](https://www.oldbookillustrations.com/). The sources of the illustration scans are specified for each entry in the columns `illustration_source_name` and `illustration_source_url`.

### Personal and Sensitive Information

The Old Book Illustrations' Terms and conditions reads:
>OBI [Old Book Illustrations] explores the art of book illustrations within boundaries defined by time and age, not by subject, treatment, or intent. This means that some illustrations might be deemed offensive, disturbing, misleading, or otherwise objectionable. We do not endorse views or opinions the Illustrations may express, neither do we guarantee that the information conveyed by any Illustration is accurate.

## Considerations for Using the Data

### Discussion of Biases

The Old Book Illustrations' Terms and conditions reads:
>OBI [Old Book Illustrations] explores the art of book illustrations within boundaries defined by time and age, not by subject, treatment, or intent. This means that some illustrations might be deemed offensive, disturbing, misleading, or otherwise objectionable. We do not endorse views or opinions the Illustrations may express, neither do we guarantee that the information conveyed by any Illustration is accurate.

## Additional Information

### Dataset Curators

The Old Book Illustrations collection is curated and maintained by the team of the [Old Book Illustrations website](https://www.oldbookillustrations.com/).

### Licensing Information

[Old Book Illustrations](https://www.oldbookillustrations.com/) website reads:
>We don’t limit the use of the illustrations available on our site, but we accept no responsibility regarding any problem, legal or otherwise, which might result from such use. More specifically, we leave it up to users to make sure that their project complies with the copyright laws of their country of residence.  Text content (descriptions, translations, etc.) is published under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.

The Old Book Illustrations webmaster mentioned that most images are public domain in the US and Europe, but there can be some exceptions. An example are the illustrations from [*Early poems of William Morris*](https://www.oldbookillustrations.com/titles/early-poems-of-william-morris/) as the illustrator died 1955, so her work is not public domain in Europe as of 2022, or [*Under the hill*](https://www.oldbookillustrations.com/titles/under-the-hill/) which was published in the US in 1928 and therefore is not public domain there.

### Citation Information

```bibtex
@misc{old book illustrations_2007,
url={https://www.oldbookillustrations.com/},
journal={Old Book Illustrations}, year={2007}}
```

### Contributions

Thanks to [@gigant](https://huggingface.co/gigant) ([@giganttheo](https://github.com/giganttheo)) for adding this dataset.