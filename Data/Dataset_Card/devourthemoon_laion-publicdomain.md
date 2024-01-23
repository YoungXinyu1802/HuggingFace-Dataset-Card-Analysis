annotations_creators:
- machine-generated
language_creators:
- machine-generated
license:
- cc-by-4.0
multilinguality:
- multilingual
pretty_name: laion-publicdomain
size_categories:
- 100K<n<1M
source_datasets: 
-laion/laion2B-en
tags:
- laion
task_categories:
- text-to-image

# Dataset Card for laion-publicdomain

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
- [Dataset Structure](#dataset-structure)
  - [Data Fields](#data-fields)
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
  - [Licensing Information](#licensing-information)

## Dataset Description

- **Homepage:** https://huggingface.co/datasets/devourthemoon/laion-publicdomain
- **Repository:** https://huggingface.co/datasets/devourthemoon/laion-publicdomain
- **Paper:** do i look like a scientist to you
- **Leaderboard:**
- **Point of Contact:** @devourthemoon on twitter

### Dataset Summary

This dataset contains metadata about images from the [LAION2B-eb dataset](https://huggingface.co/laion/laion2B-en) curated to a reasonable best guess of 'ethically sourced' images.

## Dataset Structure

### Data Fields

See the [laion2B](https://laion.ai/blog/laion-400-open-dataset/) release notes.

## Dataset Creation

### Curation Rationale

This dataset contains images whose URLs are either from archive.org or whose license is Creative Commons of some sort. 
This is a useful first pass at "public use" images, as the Creative Commons licenses are primarily voluntary and intended for public use,
and archive.org is a website that archives public domain images.

### Source Data

The source dataset is at laion/laion2B-en and is not affiliated with this project.

### Annotations

#### Annotation process

Laion2B-en is assembled from Common Crawl data.

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

#### Is this dataset as ethical as possible?

*No.* This dataset exists as a proof of concept. Further research could improve the sourcing of the dataset in a number of ways, particularly improving the attribution of files to their original authors.

#### Can I willingly submit my own images to be included in the dataset?

This is a long term goal of this project with the ideal being the generation of 'personalized' AI models for artists. Contact @devourthemoon on Twitter if this interests you.

#### Is this dataset as robust as e.g. LAION2B?

Absolutely not. About 0.17% of the images in the LAION2B dataset matched the filters, leading to just over 600k images in this dataset.

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Licensing Information

When using images from this dataset, please acknowledge the combination of Creative Commons licenses.
This dataset itself follows CC-BY-4.0
