---
dataset_info:
  - config_name: raw
    features:
      - name: image
        dtype: image
      - name: source
        dtype: string
      - name: width
        dtype: int16
      - name: height
        dtype: int16
      - name: dept
        dtype: int8
      - name: segmented
        dtype: int8
      - name: objects
        list:
          - name: name
            dtype:
              class_label:
                names:
                  "0": zebra
                  "1": tree
                  "2": nude
                  "3": crucifixion
                  "4": scroll
                  "5": head
                  "6": swan
                  "7": shield
                  "8": lily
                  "9": mouse
                  "10": knight
                  "11": dragon
                  "12": horn
                  "13": dog
                  "14": palm
                  "15": tiara
                  "16": helmet
                  "17": sheep
                  "18": deer
                  "19": person
                  "20": sword
                  "21": rooster
                  "22": bear
                  "23": halo
                  "24": lion
                  "25": monkey
                  "26": prayer
                  "27": crown of thorns
                  "28": elephant
                  "29": zucchetto
                  "30": unicorn
                  "31": holy shroud
                  "32": cat
                  "33": apple
                  "34": banana
                  "35": chalice
                  "36": bird
                  "37": eagle
                  "38": pegasus
                  "39": crown
                  "40": camauro
                  "41": saturno
                  "42": arrow
                  "43": dove
                  "44": centaur
                  "45": horse
                  "46": hands
                  "47": skull
                  "48": orange
                  "49": monk
                  "50": trumpet
                  "51": key of heaven
                  "52": fish
                  "53": cow
                  "54": angel
                  "55": devil
                  "56": book
                  "57": stole
                  "58": butterfly
                  "59": serpent
                  "60": judith
                  "61": mitre
                  "62": banner
                  "63": donkey
                  "64": shepherd
                  "65": boat
                  "66": god the father
                  "67": crozier
                  "68": jug
                  "69": lance
          - name: pose
            dtype:
              class_label:
                names:
                  "0": stand
                  "1": sit
                  "2": partial
                  "3": Unspecified
                  "4": squats
                  "5": lie
                  "6": bend
                  "7": fall
                  "8": walk
                  "9": push
                  "10": pray
                  "11": undefined
                  "12": kneel
                  "13": unrecognize
                  "14": unknown
                  "15": other
                  "16": ride
          - name: diffult
            dtype: int32
          - name: xmin
            dtype: float64
          - name: ymin
            dtype: float64
          - name: xmax
            dtype: float64
          - name: ymax
            dtype: float64
    splits:
      - name: train
        num_bytes: 9046918
        num_examples: 15156
    download_size: 18160510195
    dataset_size: 9046918
  - config_name: coco
    features:
      - name: image
        dtype: image
      - name: source
        dtype: string
      - name: width
        dtype: int16
      - name: height
        dtype: int16
      - name: dept
        dtype: int8
      - name: segmented
        dtype: int8
      - name: objects
        list:
          - name: category_id
            dtype:
              class_label:
                names:
                  "0": zebra
                  "1": tree
                  "2": nude
                  "3": crucifixion
                  "4": scroll
                  "5": head
                  "6": swan
                  "7": shield
                  "8": lily
                  "9": mouse
                  "10": knight
                  "11": dragon
                  "12": horn
                  "13": dog
                  "14": palm
                  "15": tiara
                  "16": helmet
                  "17": sheep
                  "18": deer
                  "19": person
                  "20": sword
                  "21": rooster
                  "22": bear
                  "23": halo
                  "24": lion
                  "25": monkey
                  "26": prayer
                  "27": crown of thorns
                  "28": elephant
                  "29": zucchetto
                  "30": unicorn
                  "31": holy shroud
                  "32": cat
                  "33": apple
                  "34": banana
                  "35": chalice
                  "36": bird
                  "37": eagle
                  "38": pegasus
                  "39": crown
                  "40": camauro
                  "41": saturno
                  "42": arrow
                  "43": dove
                  "44": centaur
                  "45": horse
                  "46": hands
                  "47": skull
                  "48": orange
                  "49": monk
                  "50": trumpet
                  "51": key of heaven
                  "52": fish
                  "53": cow
                  "54": angel
                  "55": devil
                  "56": book
                  "57": stole
                  "58": butterfly
                  "59": serpent
                  "60": judith
                  "61": mitre
                  "62": banner
                  "63": donkey
                  "64": shepherd
                  "65": boat
                  "66": god the father
                  "67": crozier
                  "68": jug
                  "69": lance
          - name: image_id
            dtype: string
          - name: area
            dtype: int64
          - name: bbox
            sequence: float32
            length: 4
          - name: segmentation
            list:
              list: float32
          - name: iscrowd
            dtype: bool
      - name: image_id
        dtype: string
    splits:
      - name: train
        num_bytes: 8285204
        num_examples: 15156
    download_size: 18160510195
    dataset_size: 8285204
license: cc-by-nc-2.0
task_categories:
  - object-detection
  - image-classification
tags:
  - lam
  - art
  - historical
pretty_name: "DEArt: Dataset of European Art"
size_categories:
  - 10K<n<100K
---

# Dataset Card for DEArt: Dataset of European Art

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

- **Homepage:**
- **Repository:** https://doi.org/10.5281/zenodo.6984525
- **Paper:** https://arxiv.org/abs/2211.01226
- **Leaderboard:**
- **Point of Contact:**

### Dataset Summary

> DEArt is an object detection and pose classification dataset meant to be a reference for paintings between the XIIth and the XVIIIth centuries. It contains more than 15000 images, about 80% non-iconic, aligned with manual annotations for the bounding boxes identifying all instances of 69 classes as well as 12 possible poses for boxes identifying human-like objects. Of these, more than 50 classes are cultural heritage specific and thus do not appear in other datasets; these reflect imaginary beings, symbolic entities and other categories related to art.

### Supported Tasks and Leaderboards

- `object-detection`: This dataset can be used to train or evaluate models for object-detection on historical document images.
- `image-classification`: This dataset can be used for image classification tasks by using only the labels and not the bounding box information

## Dataset Structure

This dataset has two configurations. These configurations both cover the same data and annotations but provide these annotations in different forms to make it easier to integrate the data with existing processing pipelines.

- The first configuration, `raw, uses the data's original format.
- The second configuration converts the annotations into a format that is closer to the `COCO` annotation format. This is done to make it easier to work with the [`image_processors`](https://huggingface.co/docs/transformers/main_classes/image_processor) (formerly known as`feature_extractor`s) from the `Transformers` models for object detection, which expects data to be in a COCO-style format.

### Data Instances

An instance from the `raw` config:

```python
{'image': <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=1019x1680>,
 'source': 'Europeana Collection',
 'width': 1019,
 'height': 1680,
 'dept': 3,
 'segmented': None,
 'objects': [{'name': 40,
   'pose': 3,
   'diffult': 0,
   'xmin': 259.0,
   'ymin': 166.0,
   'xmax': 679.0,
   'ymax': 479.0},
  {'name': 19,
   'pose': 2,
   'diffult': 0,
   'xmin': 115.0,
   'ymin': 354.0,
   'xmax': 882.0,
   'ymax': 1168.0},
  {'name': 15,
   'pose': 3,
   'diffult': 0,
   'xmin': 445.0,
   'ymin': 1170.0,
   'xmax': 579.0,
   'ymax': 1302.0},
  {'name': 51,
   'pose': 3,
   'diffult': 0,
   'xmin': 354.0,
   'ymin': 1196.0,
   'xmax': 445.0,
   'ymax': 1330.0},
  {'name': 51,
   'pose': 3,
   'diffult': 0,
   'xmin': 580.0,
   'ymin': 1203.0,
   'xmax': 701.0,
   'ymax': 1326.0},
  {'name': 57,
   'pose': 3,
   'diffult': 0,
   'xmin': 203.0,
   'ymin': 642.0,
   'xmax': 882.0,
   'ymax': 1172.0}]}
```

An instance from the `coco` config:

```python
{'image': <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=1019x1680>,
 'source': 'Europeana Collection',
 'width': 1019,
 'height': 1680,
 'dept': 3,
 'segmented': None,
 'image_id': '0',
 'annotations': [{'category_id': 40,
   'image_id': '0',
   'area': 131460,
   'bbox': [259.0, 166.0, 420.0, 313.0],
   'segmentation': [],
   'iscrowd': False},
  {'category_id': 19,
   'image_id': '0',
   'area': 624338,
   'bbox': [115.0, 354.0, 767.0, 814.0],
   'segmentation': [],
   'iscrowd': False},
  {'category_id': 15,
   'image_id': '0',
   'area': 17688,
   'bbox': [445.0, 1170.0, 134.0, 132.0],
   'segmentation': [],
   'iscrowd': False},
  {'category_id': 51,
   'image_id': '0',
   'area': 12194,
   'bbox': [354.0, 1196.0, 91.0, 134.0],
   'segmentation': [],
   'iscrowd': False},
  {'category_id': 51,
   'image_id': '0',
   'area': 14883,
   'bbox': [580.0, 1203.0, 121.0, 123.0],
   'segmentation': [],
   'iscrowd': False},
  {'category_id': 57,
   'image_id': '0',
   'area': 359870,
   'bbox': [203.0, 642.0, 679.0, 530.0],
   'segmentation': [],
   'iscrowd': False}]}
```

### Data Fields

The fields for the COCO config:

- `image`: The Image being annotated
- `source`: source of the image i.e.'Europeana Collection'
- `width`: width of the image
- `height`: height of the image
- `dept`: number of channels in the image
- `segmented`: Whether the image has been segmented
- `image_id`: ID for the image
- `annotations`: annotations in coco format, consisting of a list containing dictionaries with the following keys:
  - `bbox`: bounding boxes for the images
  - `category_id`: a label for the image
  - `image_id`: id for the image
  - `iscrowd`: COCO `iscrowd` flag
  - `segmentation`: COCO segmentation annotations (empty in this case but kept for compatibility with other processing scripts)

### Data Splits

The dataset doesn't define set splits, so only a train split is provided. The paper associated with the dataset does discuss a train and validation split, but it doesn't appear this split was shared.

## Dataset Creation

### Curation Rationale

The creators of the dataset authors outline some of their motivations for creating the dataset in the abstract for their paper:

> Large datasets that were made publicly available to the research community over the last 20 years have been a key enabling factor for the advances in deep learning algorithms for NLP or computer vision. These datasets are generally pairs of aligned image / manually annotated metadata, where images are photographs of everyday life. Scholarly and historical content, on the other hand, treat subjects that are not necessarily popular to a general audience, they may not always contain a large number of data points, and new data may be difficult or impossible to collect. Some exceptions do exist, for instance, scientific or health data, but this is not the case for cultural heritage (CH). The poor performance of the best models in computer vision - when tested over artworks - coupled with the lack of extensively annotated datasets for CH, and the fact that artwork images depict objects and actions not captured by photographs, indicate that a CH-specific dataset would be highly valuable for this community. We propose DEArt, at this point primarily an object detection and pose classification dataset meant to be a reference for paintings between the XIIth and the XVIIIth centuries. It contains more than 15000 images, about 80% non-iconic, aligned with manual annotations for the bounding boxes identifying all instances of 69 classes as well as 12 possible poses for boxes identifying human-like objects. Of these, more than 50 classes are CH-specific and thus do not appear in other datasets; these reflect imaginary beings, symbolic entities and other categories related to art. Additionally, existing datasets do not include pose annotations.

### Source Data

The source data comes from several cultural heritage institutions that have shared openly licenced images. The dictionary below shows the institutions and the frequency with which they are the provider of images in the dataset.

```python
{'National Museum in Warsaw': 2030,
 'Europeana Collection': 1991,
 'The Art Institute of Chicago': 1237,
 'The Metropolitan Museum of Art': 1218,
 'Rijksmuseum': 1066,
 'National Gallery of Art': 871,
 'Philadelphia Museum of Art': 774,
 'WikiArt': 687,
 'National museum in Krakow': 661,
 'National Gallery of Denmark': 660,
 'British Museum': 618,
 'Victoria and Albert Museum': 561,
 'Paul Mellon Centre': 391,
 'National Gallery of Scotland': 384,
 'Yale University Art Gallery': 376,
 'Museo Nacional Thyssen-Bornemisza': 332,
 'Harvard Art Museum': 279,
 'The National Museum of Norvay': 270,
 'LACMA': 262,
 'The Cleveland Museum of Art': 242,
 'The Leiden Collection': 159,
 'The Clark Museum': 77,
 'Pharos': 6,
 'Wikimedia Commons': 2,
 'Wikipedia': 1,
 'Unknown': 1}
```

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

[More Information Needed]

### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

[More Information Needed]

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

[More Information Needed]

### Licensing Information

[More Information Needed]

### Citation Information

[More Information Needed]

### Contributions

Thanks to [@github-username](https://github.com/<github-username>) for adding this dataset.
