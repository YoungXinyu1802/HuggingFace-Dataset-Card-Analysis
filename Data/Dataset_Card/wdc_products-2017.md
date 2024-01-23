---
annotations_creators:
- weak supervision
- expert-generated
language:
- en
language_bcp47:
- en-US
license:
- unknown
multilinguality:
- monolingual
pretty_name: products-2017
size_categories:
- 1K<n<10K
- 10K<n<100K
source_datasets:
- original
task_categories: 
- text-classification
- data-integration
task_ids:
- entity-matching
- identity-resolution
- product-matching
paperswithcode_id: wdc-products
---

# Dataset Card for [products-2017]

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
- [Additional Information](#additional-information)
  - [Citation Information](#citation-information)

## Dataset Description

- **Homepage:** [LSPCv2 Homepage](http://webdatacommons.org/largescaleproductcorpus/v2/index.html)
- **Point of Contact:** [Ralph Peeters](mailto:ralph.peeters@uni-mannheim.de)

### Dataset Summary

Many e-shops have started to mark-up product data within their HTML pages using the schema.org vocabulary. The Web Data Commons project regularly extracts such data from the Common Crawl, a large public web crawl. The Web Data Commons Training and Test Sets for Large-Scale Product Matching contain product offers from different e-shops in the form of binary product pairs (with corresponding label "match" or "no match")

In order to support the evaluation of machine learning-based matching methods, the data is split into training, validation and test set. We provide training and validation sets in four different sizes for four product categories. The labels of the test sets were manually checked while those of the training sets were derived using shared product identifiers from the Web via weak supervision.

The data stems from the WDC Product Data Corpus for Large-Scale Product Matching - Version 2.0 which consists of 26 million product offers originating from 79 thousand websites.


### Supported Tasks and Leaderboards

Entity Matching, Product Matching

### Languages

English

## Dataset Structure

### Data Instances

The data is structured as pairs of product offers with the corresponding match/non-match label. This is an example instance from the computers category:

```
{"pair_id":"581109#16637861","label":0,"id_left":581109,"category_left":"Computers_and_Accessories","cluster_id_left":1324529,"brand_left":"\"Gigabyte\"@en","title_left":" \"Gigabyte Radeon RX 480 G1 Gaming 4096MB GDDR5 PCI-Express Graphics Card\"@en \"Gigabyte Gr| OcUK\"@en","description_left":"\"GV-RX480G1 GAMING-4GD, Core Clock: 1202MHz, Boost Clock: 1290MHz, Memory: 4096MB 7000MHz GDDR5, Stream Processors: 2304, Crossfire Ready, VR Ready, FreeSync Ready, 3 Years Warranty\"@en ","price_left":null,"specTableContent_left":null,"id_right":16637861,"category_right":"Computers_and_Accessories","cluster_id_right":107415,"brand_right":"\"Gigabyte\"@en","title_right":" \"Gigabyte Radeon RX 550 Gaming OC 2048MB GDDR5 PCI-Express Graphics Card\"@en \"Gigabyte Gr| OcUK\"@en","description_right":"\"GV-RX550GAMING OC-2GD, Boost: 1219MHz, Memory: 2048MB 7000MHz GDDR5, Stream Processors: 512, DirectX 12 Support, 3 Years Warranty\"@en ","price_right":null,"specTableContent_right":null}
```

### Data Fields

- pair_id: unique identifier of a pair (string)
- label: binary label, match or non-match (int)

The following attributes are contained twice, once for the first and once for the second product offer

- id: unique id of the product offer (int)
- category: product category (string)
- cluster_id: id of the product cluster from the original corpus this offer belongs to (int)
- brand: brand of the product (string)
- title: product title (string)
- description: longer product description (string)
- price: price of the product offer (string)
- specTableContent: additional data found in specification tables on the webpage that contains the product offer (string)

### Data Splits
- Computers
  - Test set - 1100 pairs
  - Small Train set - 2267 pairs
  - Small Validation set - 567 pairs
  - Medium Train set - 6475 pairs
  - Medium Validation set - 1619 pairs
  - Large Train set - 26687 pairs
  - Large Validation set - 6672 pairs
  - XLarge Train set - 54768 pairs
  - Xlarge Validation set - 13693 pairs

- Cameras
  - Test set - 1100 pairs
  - Small Train set - 1508 pairs
  - Small Validation set - 378 pairs
  - Medium Train set - 4204 pairs
  - Medium Validation set - 1051 pairs
  - Large Train set - 16028 pairs
  - Large Validation set - 4008 pairs
  - XLarge Train set - 33821 pairs
  - Xlarge Validation set - 8456 pairs

- Watches
  - Test set - 1100 pairs
  - Small Train set - 1804 pairs
  - Small Validation set - 451 pairs
  - Medium Train set - 5130 pairs
  - Medium Validation set - 1283 pairs
  - Large Train set - 21621 pairs
  - Large Validation set - 5406 pairs
  - XLarge Train set - 49255 pairs
  - Xlarge Validation set - 12314 pairs

- Shoes
  - Test set - 1100 pairs
  - Small Train set - 1650 pairs
  - Small Validation set - 413 pairs
  - Medium Train set - 4644 pairs
  - Medium Validation set - 1161 pairs
  - Large Train set - 18391 pairs
  - Large Validation set - 4598 pairs
  - XLarge Train set - 33943 pairs
  - Xlarge Validation set - 8486 pairs


## Dataset Creation

### Annotations

#### Annotation process

- Training and Validation sets: distant supervision via shared schema.org product IDs
- Test sets: Single expert annotator

#### Who are the annotators?

[Ralph Peeters](https://www.uni-mannheim.de/dws/people/researchers/phd-students/ralph-peeters/)

## Additional Information

### Citation Information

```
@inproceedings{primpeli2019wdc,
  title={The WDC training dataset and gold standard for large-scale product matching},
  author={Primpeli, Anna and Peeters, Ralph and Bizer, Christian},
  booktitle={Companion Proceedings of The 2019 World Wide Web Conference},
  pages={381--386},
  year={2019}
}
```
