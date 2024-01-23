---
annotations_creators:
- crowdsourced
license: apache-2.0
pretty_name: ICDAR 2023 Competition on Robust Layout Segmentation in Corporate Documents
size_categories:
- n<1K
tags:
- layout-segmentation
- COCO
- document-understanding
- PDF
- icdar
- competition
task_categories:
- object-detection
- image-segmentation
task_ids:
- instance-segmentation
---

# Dataset Card for ICDAR 2023 Competition on Robust Layout Segmentation in Corporate Documents

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

- **Homepage:** https://ds4sd.github.io/icdar23-doclaynet/
- **Leaderboard:** https://eval.ai/web/challenges/challenge-page/1923/leaderboard
- **Point of Contact:**

### Dataset Summary

This is the official competition dataset for the _ICDAR 2023 Competition on Robust Layout Segmentation in Corporate Documents_.
You are invited to advance the research in accurately segmenting the layout on a broad range of document styles and domains. To achieve this, we challenge you to develop a model that can correctly identify and segment the layout components in document pages as bounding boxes on a competition data-set we provide.

For more information see https://ds4sd.github.io/icdar23-doclaynet/.


#### Training resources

In our recently published [DocLayNet](https://github.com/DS4SD/DocLayNet) dataset, which contains 80k+ human-annotated document pages exposing diverse layouts, we define 11 classes for layout components (paragraphs, headings, tables, figures, lists, mathematical formulas and several more). We encourage you to use this dataset for training and internal evaluation of your solution.
Further, you may consider any other publicly available document layout dataset for training (e.g. [PubLayNet](https://github.com/ibm-aur-nlp/PubLayNet), [DocBank](https://github.com/doc-analysis/DocBank)).

 
### Supported Tasks and Leaderboards

This is the official dataset of the ICDAR 2023 Competition on Robust Layout Segmentation in Corporate Documents.
For more information see https://ds4sd.github.io/icdar23-doclaynet/.

#### Evaluation Metric

Your submissions on our [EvalAI challenge](https://eval.ai/web/challenges/challenge-page/1923/) will be evaluated using the Mean Average Precision (mAP) @ Intersection-over-Union (IoU) [0.50:0.95] metric, as used in the [COCO](https://cocodataset.org/) object detection competition.  In detail, we will calculate the average precision for a sequence of IoU thresholds ranging from 0.50 to 0.95 with a step size of 0.05. This metric is computed for every document category in the competition-dataset. Then the mean of the average precisions on all categories is computed as the final score.

#### Submission 

We ask you to upload a JSON file in [COCO results format](https://cocodataset.org/#format-results) [here](https://eval.ai/web/challenges/challenge-page/1923/submission), with complete layout bounding-boxes for each page sample. The given `image_id`s must correspond to the ones we publish with the competition data-set's `coco.json`. For each submission you make, the computed mAP will be provided for each category as well as combined. The [leaderboard](https://eval.ai/web/challenges/challenge-page/1923/leaderboard/4545/Total) will be ranked based on the overall mAP.


## Dataset Structure

### Data Fields

DocLayNet provides four types of data assets:

1. PNG images of all pages, resized to square `1025 x 1025px`
2. ~~Bounding-box annotations in COCO format for each PNG image~~ (annotations will be released at the end of the competition)
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
reports,
manuals,
patents,
pthers
```


### Data Splits

The dataset provides three splits
- `dev`, which is extracted from the [DocLayNet](https://github.com/DS4SD/DocLayNet) dataset
- `test`, which contains new data for the competition

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

A publication will be submitted at the end of the competition. Meanwhile, we suggest the cite our original dataset paper.

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
