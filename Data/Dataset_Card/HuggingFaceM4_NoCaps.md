---
license: cc-by-2.0
---
# Dataset Card for NoCaps

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

- **Homepage:** [https://nocaps.org/](https://nocaps.org/)
- **Paper:** [nocaps: novel object captioning at scale](https://openaccess.thecvf.com/content_ICCV_2019/papers/Agrawal_nocaps_novel_object_captioning_at_scale_ICCV_2019_paper.pdf)
- **Leaderboard:**
- **Point of Contact:**: contact@nocaps.org

### Dataset Summary

Dubbed NoCaps for novel object captioning at scale, NoCaps consists of 166,100 human-generated captions describing 15,100 images from the Open Images validation and test sets.
The associated training data consists of COCO image-caption pairs, plus Open Images image-level labels and object bounding boxes.
Since Open Images contains many more classes than COCO, nearly 400 object classes seen in test images have no or very few associated training captions (hence, nocaps).


### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

[More Information Needed]

## Dataset Structure

### Data Instances

Each instance has the following structure:
```
{
    'image': <PIL.JpegImagePlugin.JpegImageFile image mode=L size=732x1024 at 0x7F574A3A9B50>,
    'image_coco_url': 'https://s3.amazonaws.com/nocaps/val/0013ea2087020901.jpg',
    'image_date_captured': '2018-11-06 11:04:33',
    'image_file_name': '0013ea2087020901.jpg',
    'image_height': 1024,
    'image_width': 732,
    'image_id': 0,
    'image_license': 0,
    'image_open_images_id': '0013ea2087020901',
    'annotations_ids': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    'annotations_captions': [
        'A baby is standing in front of a house.',
        'A little girl in a white jacket and sandals.',
        'A young child stands in front of a house.',
        'A child is wearing a white shirt and standing on a side walk. ',
        'A little boy is standing in his diaper with a white shirt on.',
        'A child wearing a diaper and shoes stands on the sidewalk.',
        'A child is wearing a light-colored shirt during the daytime.',
        'A little kid standing on the pavement in a shirt. ',
        'Black and white photo of a little girl smiling.',
        'a cute baby is standing alone with white shirt'
    ]
}
```

### Data Fields

- `image`: The image
- `image_coco_url`: URL for the image
- `image_date_captured`: Date at which the image was captured
- `image_file_name`: The file name for the image
- `image_height`: Height of the image
- `image_width`: Width of the image
- `image_id`: Id of the image
- `image_license`: Not sure what this is, it is always at 0
- `image_open_images_id`: Open image id
- `annotations_ids`: Unique ids for the captions (to use in conjunction with `annotations_captions`)
- `annotations_captions`: Captions for the image (to use in conjunction with `annotations_ids`)

### Data Splits

[More Information Needed]

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

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

Thanks to [@VictorSanh](https://github.com/VictorSanh) for adding this dataset.