---
annotations_creators:
- found
language_creators:
- found
language:
- id
license:
- cc-by-sa-4.0
multilinguality:
- monolingual
size_categories:
- 10M<n<100M
source_datasets:
- original
task_categories:
- image-to-text
task_ids:
- image-captioning
pretty_name: Laion Indo 70M
---

# Dataset Card for Laion Indo 70M

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Dataset Preprocessing](#dataset-preprocessing)
  - [Supported Tasks](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-instances)
  - [Data Splits](#data-instances)
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

## Dataset Description

- **Paper:** [LAION-400M: Open Dataset of CLIP-Filtered 400 Million Image-Text Pairs](https://arxiv.org/abs/2111.02114)

### Dataset Summary

Laion Indo is a Translated subset laion 400m dataset with 70 million  image-text pairs specifically meant to be used for visionand-language Indonesia pre-training.
The Dataset translated using custom marian model

### Dataset Preprocessing

This dataset doesn't download the images locally by default. Instead, it exposes URLs to the images. To fetch the images, use the following code:

```python
from concurrent.futures import ThreadPoolExecutor
from functools import partial
import io
import urllib

import PIL.Image

from datasets import load_dataset
from datasets.utils.file_utils import get_datasets_user_agent


USER_AGENT = get_datasets_user_agent()


def fetch_single_image(image_url, timeout=None, retries=0):
    for _ in range(retries + 1):
        try:
            request = urllib.request.Request(
                image_url,
                data=None,
                headers={"user-agent": USER_AGENT},
            )
            with urllib.request.urlopen(request, timeout=timeout) as req:
                image = PIL.Image.open(io.BytesIO(req.read()))
            break
        except Exception:
            image = None
    return image


def fetch_images(batch, num_threads, timeout=None, retries=0):
    fetch_single_image_with_args = partial(fetch_single_image, timeout=timeout, retries=retries)
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        batch["image"] = list(executor.map(fetch_single_image_with_args, batch["image_url"]))
    return batch


num_threads = 20
dset = load_dataset("munggok/Laion_Indo")
dset = dset.map(fetch_images, batched=True, batch_size=100, fn_kwargs={"num_threads": num_threads})
```

### Supported Tasks and Leaderboards

- `image-captioning`: This dataset can be used to train model for the Image Captioning task.

### Languages

All captions Translated in Indonesia.

## Dataset Structure

### Data Instances

Each instance represents a single image with a caption:

```
{
  'image_url': 'image_url',
  'caption': 'text here',
  'meta' : 'metadata from orginal laion'
}
```

### Data Fields

- `image_url`: Static URL for downloading the image associated with the post.
- `caption`: Textual description of the image.
- `meta` : Containing meta data from laion original dataset (Width,Height,NSFW,Similarity)

### Data Splits

There is only training data, with a total of 70662144 rows

## Dataset Creation

### Curation Rationale


### Source Data

#### Initial Data Collection and Normalization

From the paper: LAION-400M: Open Dataset of CLIP-Filtered 400 Million Image-Text Pairs](https://arxiv.org/abs/2111.02114)
#### Who are the source language producers?

Not specified.

### Annotations

#### Annotation process

Annotations are extracted jointly with the images using the automatic pipeline.

#### Who are the annotators?

Not specified.

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

Soravit Changpinyo, Piyush Sharma, Nan Ding and Radu Soricut.

### Licensing Information

CC BY-NC-SA 4.0

### Citation Information

```bibtex
@article{DBLP:journals/corr/abs-2111-02114,
  author    = {Christoph Schuhmann and
               Richard Vencu and
               Romain Beaumont and
               Robert Kaczmarczyk and
               Clayton Mullis and
               Aarush Katta and
               Theo Coombes and
               Jenia Jitsev and
               Aran Komatsuzaki},
  title     = {{LAION-400M:} Open Dataset of CLIP-Filtered 400 Million Image-Text
               Pairs},
  journal   = {CoRR},
  volume    = {abs/2111.02114},
  year      = {2021},
  url       = {https://arxiv.org/abs/2111.02114},
  eprinttype = {arXiv},
  eprint    = {2111.02114},
  timestamp = {Fri, 05 Nov 2021 15:25:54 +0100},
  biburl    = {https://dblp.org/rec/journals/corr/abs-2111-02114.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```
