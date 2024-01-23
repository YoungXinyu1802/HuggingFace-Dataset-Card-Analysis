
---
annotations_creators:
- no-annotation
language:
- en
language_creators:
- other
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: COYO-Labeled-300M
size_categories:
- 100M<n<1B
source_datasets:
- original
tags:
- image-labeled pairs
task_categories:
- image-classification
task_ids:
- multi-label-image-classification
---
# Dataset Card for COYO-Labeled-300M
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
- **Homepage:** [COYO homepage](https://kakaobrain.com/contents/?contentId=7eca73e3-3089-43cb-b701-332e8a1743fd)
- **Repository:** [COYO repository](https://github.com/kakaobrain/coyo-dataset)
- **Paper:**
- **Leaderboard:**
- **Point of Contact:** [COYO email](coyo@kakaobrain.com)
### Dataset Summary
**COYO-Labeled-300M** is a dataset of **machine-labeled** 300M images-multi-label pairs. We labeled subset of COYO-700M with a large model (efficientnetv2-xl) trained on imagenet-21k. We followed the same evaluation pipeline as in efficientnet-v2. The labels are top 50 most likely labels out of 21,841 classes from imagenet-21k. The label probabilies are provided rather than label so that the user can select threshold of their choice for multi-label classification use or can take top-1 class for single class classification use.

In other words, **COYO-Labeled-300M** is a ImageNet-like dataset. Instead of human labeled 1.25 million samples, it's machine-labeled 300 million samples. This dataset is similar to JFT-300M which is not released to the public.

### Supported Tasks and Leaderboards
We empirically validated the quality of COYO-Labeled-300M dataset by re-implementing popular model, [ViT](https://arxiv.org/abs/2010.11929). 
We found that our ViT implementation trained on COYO-Labeled-300M performs similar to the performance numbers in the ViT paper trained on JFT-300M.
We also provide weights for the pretrained ViT model on COYO-Labeled-300M as well as its training & fine-tuning code.
### Languages
The labels in the COYO-Labeled-300M dataset consist of English.

## Dataset Structure
### Data Instances
Each instance in COYO-Labeled-300M represents multi-labels and image pair information with meta-attributes.  
And we also provide label information, **imagenet21k_tree.pickle**.  

```
{
  'id': 315,
  'url': 'https://a.1stdibscdn.com/pair-of-blue-and-white-table-lamps-for-sale/1121189/f_121556431538206028457/12155643_master.jpg?width=240',
  'imagehash': 'daf5a50aae4aa54a',
  'labels': [8087, 11054, 8086, 6614, 6966, 8193, 10576, 9710, 4334, 9909, 8090, 10104, 10105, 9602, 5278, 9547, 6978, 12011, 7272, 5273, 6279, 4279, 10903, 8656, 9601, 8795, 9326, 4606, 9907, 9106, 7574, 10006, 7257, 6959, 9758, 9039, 10682, 7164, 5888, 11654, 8201, 4546, 9238, 8197, 10882, 17380, 4470, 5275, 10537, 11548],
  'label_probs': [0.4453125, 0.30419921875, 0.09417724609375, 0.033905029296875, 0.03240966796875, 0.0157928466796875, 0.01406097412109375, 0.01129150390625, 0.00978851318359375, 0.00841522216796875, 0.007720947265625, 0.00634002685546875, 0.0041656494140625, 0.004070281982421875, 0.002910614013671875, 0.0028018951416015625, 0.002262115478515625, 0.0020503997802734375, 0.0017080307006835938, 0.0016880035400390625, 0.0016679763793945312, 0.0016613006591796875, 0.0014324188232421875, 0.0012445449829101562, 0.0011739730834960938, 0.0010318756103515625, 0.0008969306945800781, 0.0008792877197265625, 0.0008726119995117188, 0.0008263587951660156, 0.0007123947143554688, 0.0006799697875976562, 0.0006561279296875, 0.0006542205810546875, 0.0006093978881835938, 0.0006046295166015625, 0.0005769729614257812, 0.00057220458984375, 0.0005636215209960938, 0.00055694580078125, 0.0005092620849609375, 0.000507354736328125, 0.000507354736328125, 0.000499725341796875, 0.000484466552734375, 0.0004456043243408203, 0.0004439353942871094, 0.0004355907440185547, 0.00043392181396484375, 0.00041866302490234375],
  'width': 240,
  'height': 240
}
```


### Data Fields

| name                     | type    | description                                                                                                                                                                                |
|--------------------------|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id                   	| long              	| Unique 64-bit integer ID generated by [monotonically_increasing_id()](https://spark.apache.org/docs/3.1.3/api/python/reference/api/pyspark.sql.functions.monotonically_increasing_id.html) which is the same value that is mapped with the existing COYO-700M. 	|
| url                  	| string            	| The image URL extracted from the `src` attribute of the `<img>`                                                                                                                                                                                                	|
| imagehash            	| string            	| The [perceptual hash(pHash)](http://www.phash.org/) of the image                                                                                                                                                                                               	|
| labels               	| sequence[integer] 	| Inference results of EfficientNetV2-XL model trained on ImageNet-21K dataset (Top 50 indices among 21,841 classes)                                                                                                                                             	|
| label_probs          	| sequence[float]   	| Inference results of EfficientNetV2-XL model trained on ImageNet-21K dataset (Top 50 indices among 21,841 probabilites)                                                                                                                                        	|
| width                	| integer           	| The width of the image                                                                                                                                                                                                                                         	|
| height               	| integer           	| The height of the image                                                                                                                                                                                                                                        	|


### Data Splits

Data was not split, since the evaluation was expected to be performed on more widely used downstream task(s).

## Dataset Creation

### Curation Rationale

We labeled subset of COYO-700M with a large model (efficientnetv2-xl) trained on imagenet-21k. Data sampling was done with a size similar to jft-300m, filtered by a specific threshold for probabilities for the top-1 label.

### Source Data

[COYO-700M](https://huggingface.co/datasets/kakaobrain/coyo-700m)

#### Who are the source language producers?
[Common Crawl](https://commoncrawl.org/) is the data source for COYO-700M.
### Annotations
#### Annotation process
The dataset was built in a fully automated process that did not require human annotation.
#### Who are the annotators?
No human annotation
### Personal and Sensitive Information
The basic instruction, licenses and contributors are the same as for the [coyo-700m](https://huggingface.co/datasets/kakaobrain/coyo-700m).
