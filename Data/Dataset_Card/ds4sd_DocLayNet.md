---
annotations_creators:
- crowdsourced
license: other
pretty_name: DocLayNet
size_categories:
- 10K<n<100K
tags:
- layout-segmentation
- COCO
- document-understanding
- PDF
task_categories:
- object-detection
- image-segmentation
task_ids:
- instance-segmentation
---

# Dataset Card for DocLayNet

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
- [Dataset Structure](#dataset-structure)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Annotations](#annotations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Homepage:** https://developer.ibm.com/exchanges/data/all/doclaynet/
- **Repository:** https://github.com/DS4SD/DocLayNet
- **Paper:** https://doi.org/10.1145/3534678.3539043
- **Leaderboard:**
- **Point of Contact:**

### Dataset Summary

DocLayNet provides page-by-page layout segmentation ground-truth using bounding-boxes for 11 distinct class labels on 80863 unique pages from 6 document categories. It provides several unique features compared to related work such as PubLayNet or DocBank:

1. *Human Annotation*: DocLayNet is hand-annotated by well-trained experts, providing a gold-standard in layout segmentation through human recognition and interpretation of each page layout
2. *Large layout variability*: DocLayNet includes diverse and complex layouts from a large variety of public sources in Finance, Science, Patents, Tenders, Law texts and Manuals
3. *Detailed label set*: DocLayNet defines 11 class labels to distinguish layout features in high detail.
4. *Redundant annotations*: A fraction of the pages in DocLayNet are double- or triple-annotated, allowing to estimate annotation uncertainty and an upper-bound of achievable prediction accuracy with ML models
5. *Pre-defined train- test- and validation-sets*: DocLayNet provides fixed sets for each to ensure proportional representation of the class-labels and avoid leakage of unique layout styles across the sets.

### Supported Tasks and Leaderboards

We are hosting a competition in ICDAR 2023 based on the DocLayNet dataset. For more information see https://ds4sd.github.io/icdar23-doclaynet/.

## Dataset Structure

### Data Fields

DocLayNet provides four types of data assets:

1. PNG images of all pages, resized to square `1025 x 1025px`
2. Bounding-box annotations in COCO format for each PNG image
3. Extra: Single-page PDF files matching each PNG image
4. Extra: JSON file matching each PDF page, which provides the digital text cells with coordinates and content

The COCO image record are defined like this example

```js
    ...
    {
      "id": 1,
      "width": 1025,
      "height": 1025,
      "file_name": "132a855ee8b23533d8ae69af0049c038171a06ddfcac892c3c6d7e6b4091c642.png",

      // Custom fields:
      "doc_category": "financial_reports" // high-level document category
      "collection": "ann_reports_00_04_fancy", // sub-collection name
      "doc_name": "NASDAQ_FFIN_2002.pdf", // original document filename
      "page_no": 9, // page number in original document
      "precedence": 0, // Annotation order, non-zero in case of redundant double- or triple-annotation
    },
    ...
```

The `doc_category` field uses one of the following constants:

```
financial_reports,
scientific_articles,
laws_and_regulations,
government_tenders,
manuals,
patents
```


### Data Splits

The dataset provides three splits
- `train`
- `val`
- `test`

## Dataset Creation

### Annotations

#### Annotation process

The labeling guideline used for training of the annotation experts are available at [DocLayNet_Labeling_Guide_Public.pdf](https://raw.githubusercontent.com/DS4SD/DocLayNet/main/assets/DocLayNet_Labeling_Guide_Public.pdf).


#### Who are the annotators?

Annotations are crowdsourced.


## Additional Information

### Dataset Curators

The dataset is curated by the [Deep Search team](https://ds4sd.github.io/) at IBM Research.
You can contact us at [deepsearch-core@zurich.ibm.com](mailto:deepsearch-core@zurich.ibm.com).

Curators:
- Christoph Auer, [@cau-git](https://github.com/cau-git)
- Michele Dolfi, [@dolfim-ibm](https://github.com/dolfim-ibm)
- Ahmed Nassar, [@nassarofficial](https://github.com/nassarofficial)
- Peter Staar, [@PeterStaar-IBM](https://github.com/PeterStaar-IBM)

### Licensing Information

License: [CDLA-Permissive-1.0](https://cdla.io/permissive-1-0/)


### Citation Information


```bib
@article{doclaynet2022,
  title = {DocLayNet: A Large Human-Annotated Dataset for Document-Layout Segmentation},
  doi = {10.1145/3534678.353904},
  url = {https://doi.org/10.1145/3534678.3539043},
  author = {Pfitzmann, Birgit and Auer, Christoph and Dolfi, Michele and Nassar, Ahmed S and Staar, Peter W J},
  year = {2022},
  isbn = {9781450393850},
  publisher = {Association for Computing Machinery},
  address = {New York, NY, USA},
  booktitle = {Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining},
  pages = {3743–3751},
  numpages = {9},
  location = {Washington DC, USA},
  series = {KDD '22}
}
```

### Contributions

Thanks to [@dolfim-ibm](https://github.com/dolfim-ibm), [@cau-git](https://github.com/cau-git) for adding this dataset.
