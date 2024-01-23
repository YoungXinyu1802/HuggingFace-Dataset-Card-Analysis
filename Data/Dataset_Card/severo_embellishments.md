---
annotations_creators:
- no-annotation
license:
- cc0-1.0
size_categories:
- n<1K
source_datasets:
- original
pretty_name: Digitised Books - Images identified as Embellishments. c. 1510 - c. 1900.
  JPG
---

# Dataset Card for severo/embellishments

## Dataset Description

- **Homepage:** [Digitised Books - Images identified as Embellishments - Homepage](https://bl.iro.bl.uk/concern/datasets/59d1aa35-c2d7-46e5-9475-9d0cd8df721e)
- **Point of Contact:** [Sylvain Lesage](mailto:sylvain.lesage@huggingface.co)

### Dataset Summary

This small dataset contains the thumbnails of the first 100 entries of [Digitised Books - Images identified as Embellishments. c. 1510 - c. 1900. JPG](https://bl.iro.bl.uk/concern/datasets/59d1aa35-c2d7-46e5-9475-9d0cd8df721e). It has been uploaded to the Hub to reproduce the tutorial by Daniel van Strien: [Using 🤗 datasets for image search](https://danielvanstrien.xyz/metadata/deployment/huggingface/ethics/huggingface-datasets/faiss/2022/01/13/image_search.html).

## Dataset Structure

### Data Instances

A typical row contains an image thumbnail, its filename, and the year of publication of the book it was extracted from.

An example looks as follows:
```
{
 'fname': '000811462_05_000205_1_The Pictorial History of England being a history of the people as well as a hi_1855.jpg',
 'year': '1855',
 'path': 'embellishments/1855/000811462_05_000205_1_The Pictorial History of England being a history of the people as well as a hi_1855.jpg',
 'img': ...
}
```

### Data Fields

- `fname`: the image filename.
- `year`: a string with the year of publication of the book from which the image has been extracted
- `path`: local path to the image
- `img`: a thumbnail of the image with a max height and width of 224 pixels

### Data Splits

The dataset only contains 100 rows, in a single 'train' split.

## Dataset Creation

### Curation Rationale

This dataset was chosen by Daniel van Strien for his tutorial [Using 🤗 datasets for image search](https://danielvanstrien.xyz/metadata/deployment/huggingface/ethics/huggingface-datasets/faiss/2022/01/13/image_search.html), which includes the code in Python to do it.

### Source Data

#### Initial Data Collection and Normalization

As stated on the British Library webpage:
> The images were algorithmically gathered from 49,455 digitised books, equating to 65,227 volumes (25+ million pages), published between c. 1510 - c. 1900. The books cover a wide range of subject areas including philosophy, history, poetry and literature. The images are in .JPEG format.d BCP-47 code is `en`.

#### Who are the source data producers?

British Library, British Library Labs, Adrian Edwards (Curator), Neil Fitzgerald (Contributor ORCID)

### Annotations

The dataset does not contain any additional annotations.

#### Annotation process

[N/A]

#### Who are the annotators?

[N/A]

### Personal and Sensitive Information

[N/A]

## Considerations for Using the Data

### Social Impact of Dataset

[N/A]

### Discussion of Biases

[N/A]

### Other Known Limitations

This is a toy dataset that aims at:
- validating the process described in the tutorial [Using 🤗 datasets for image search](https://danielvanstrien.xyz/metadata/deployment/huggingface/ethics/huggingface-datasets/faiss/2022/01/13/image_search.html) by Daniel van Strien,
- showing the [dataset viewer](https://huggingface.co/datasets/severo/embellishments/viewer/severo--embellishments/train) on an image dataset.

## Additional Information

### Dataset Curators

The dataset was created by Sylvain Lesage at Hugging Face, to replicate the tutorial [Using 🤗 datasets for image search](https://danielvanstrien.xyz/metadata/deployment/huggingface/ethics/huggingface-datasets/faiss/2022/01/13/image_search.html) by Daniel van Strien.

### Licensing Information

CC0 1.0 Universal Public Domain
