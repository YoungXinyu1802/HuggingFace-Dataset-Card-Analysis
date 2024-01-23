---
license: cc
source_datasets:
- original
task_categories:
- image-classification
task_ids:
- multi-class-classification
- multi-class-image-classification
paperswithcode_id: ecoset
pretty_name: Ecoset
tags:
- other-image-classification
- image-classification
---

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
- [Installation](#installation)
  - [Install requirements](#install-requirements)
  - [Download settings](#download-settings)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
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

- **Homepage:** [https://www.kietzmannlab.org/ecoset](https://www.kietzmannlab.org/ecoset/)
- **Repository:** [https://codeocean.com/capsule/9570390/tree/v1](https://codeocean.com/capsule/9570390/tree/v1)
- **Paper:** [https://www.pnas.org/doi/full/10.1073/pnas.2011417118](https://doi.org/10.1073/pnas.2011417118)
- **Point of Contact:** [tim.kietzmann@uni-osnabrueck.de](tim.kietzmann@uni-osnabrueck.de)


### Dataset Summary

Tired of all the dogs in ImageNet (ILSVRC)? Then ecoset is here for you. 1.5m images 
from 565 basic level categories, chosen to be both (i) frequent in linguistic usage, 
and (ii) rated by human observers as concrete (e.g. ‘table’ is concrete, ‘romance’ 
is not).

Ecoset is a typical image recognition dataset, combining images of objects with appropriate 
labels (one label per image). Importantly, ecoset is intended to provide higher ecological 
validity than its counterparts, with a mislabelling error rate < 5% and filtered for NSFW content.
For more information on the dataset, consider reading the [original publication](https://doi.org/10.1073/pnas.2011417118).

Ecoset consists of a train, test, and validation subset which all are openly available to the user.

### Supported Tasks and Leaderboards

Ecoset is a large multi-class single-label object recognition image dataset (similar to ImageNet).

## Installation

### Install Requirements

In order to work with ecoset, please make sure to install the s3 compatible version of huggingface datasets, which should include the `s3fs`, `botocore` and `boto3` modules:

```bash
pip install datasets[s3]
```

If you want to work with the dataset in `Huggingface.datasets`, you might also want to make sure to install PIL (`pip install Pillow`) in order to work with image input. However, downloading the dataset will work despite not having installed PIL.

### Download Settings

Please set `ignore_verifications=True`. when downloading this dataset, else the download will result in an error:

```python
from datasets import load_dataset

dataset = load_dataset("kietzmannlab/ecoset", ignore_verifications=True)
```

| NOTE: If you get errors like: `FileNotFoundError: [Errno 2] No such file or directory:'<DATASET_PATH>'` this is likely due do having previously downloaded the dataset and then cancelling the download. If this is the case for you, you can fix this error by manually removing the dataset path and reinstalling the dataset. |
| --- |
## Dataset Structure


We show detailed information for all the configurations of the dataset. Currently, there is only one setting (`Full`) available, containing all data.


### Data Instances

#### Full

- **Size of downloaded dataset files:** 155 GB
- **Total amount of disk used:** 311 GB

## Dataset Creation

A total of 565 categories were selected based on the following: 1) their word frequency in American television and film subtitles (SUBTLEX_US), 2) the perceived concreteness by human observers, and 3) the availability of a minimum of 700 images. Images were sourced via the overall ImageNet database (the same resource used for ILSVRC 2012) or obtained under CC BY-NC-SA 2.0 license from Bing image search and Flickr. Thorough data cleaning procedures were put in place to remove duplicates and to assure an expected misclassification rate per category of <4%.

### Curation Rationale

More information on the curation of the dataset can be found in the [original publication](https://doi.org/10.1073/pnas.2011417118).

### Source Data

The source data is available under: [https://codeocean.com/capsule/9570390/tree/v1](https://codeocean.com/capsule/9570390/tree/v1)

### Annotations

Each ecoset image folder is annotated with class labels according to the main object depicted in a class of images. No further annotations are added to the dataset.

### Personal and Sensitive Information

The dataset was tested to exclude sensitive images using Yahoo's Open NSFW detection model, removing all image with an NSFW score above 0.8. For this dataset, only images with secured license information was used, which should prevent the inclusion of images without consent of the image's authors and subjects. Despite these measures, it is possible that the images in the dataset contain personal and sensitive information.
  
## Considerations for Using the Data

### Social Impact of Dataset
  
Large-scale image-label datasets such as ImageNet are the backbone of modern Computer Vision. However, such large datasets often suffer from problems like mislabeling, category biases, misrepresentations, and unsafe content. Ecoset was created with the aim to reduce these biases and consequently improve the social impact of Computer Vision techniques trained on the dataset. More information on the social impact of the dataset can be found in the [original publication](https://doi.org/10.1073/pnas.2011417118).

### Discussion of Biases

Despite best efforts to provide an ecologically valid and overall less biased dataset, ecoset is still likely to contain biased data. The category selection of ecoset was based on human concreteness ratings and word frequencies in a corpus consisting of American television and film subtitles. This undoubtedly biases the category selection toward Western cultures. Image inclusion was based on the availability via Bing/Flickr search results as well as the existence of relevant ImageNet categories. Images depicting people, specifically the categories “man,” “woman,” and “child,” were not sampled according to census distributions (age, ethnicity, gender, etc.).

### Other Known Limitations

In addition to points mentioned in [Discussion of Biases](#discussion-of-biases), ecoset image and category distributions do not reflect the naturalistic, egocentric visual input typically encountered in the everyday life of infant and adults.

## Additional Information

### Dataset Curators

The corpus was put together by Johannes Mehrer, Courtney J. Spoerer, Emer C. Jones, Nikolaus Kriegeskorte, and Tim C. Kietzmann.

### Licensing Information

Ecoset is licensed under Creative Commons Attribution-NonCommercial-ShareAlike 2.0 license (cc-by-nc-sa-2.0).

### Citation Information

```
@article{mehrer2021ecologically,
  title={An ecologically motivated image dataset for deep learning yields better models of human vision},
  author={Mehrer, Johannes and Spoerer, Courtney J and Jones, Emer C and Kriegeskorte, Nikolaus and Kietzmann, Tim C},
  journal={Proceedings of the National Academy of Sciences},
  volume={118},
  number={8},
  pages={e2011417118},
  year={2021},
  publisher={National Acad Sciences}
}
```

### Contributions

The ecoset dataloader and dataset card was created by [@DiGyt](https://github.com/DiGyt) on behalf of [@kietzmannlab](https://huggingface.co/kietzmannlab).
For questions and suggestions feel free to reach out.
