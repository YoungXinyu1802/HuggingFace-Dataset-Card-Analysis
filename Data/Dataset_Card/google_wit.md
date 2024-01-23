---
annotations_creators:
- machine-generated
language_creators:
- found
language:
- af
- ar
- ast
- azb
- be
- bg
- bn
- br
- ca
- cs
- cy
- da
- de
- el
- en
- eo
- es
- et
- eu
- fa
- fi
- fr
- fy
- ga
- gl
- hr
- hu
- hy
- id
- it
- iw
- ja
- ka
- ko
- la
- lt
- lv
- mk
- ml
- ms
- nl
- nn
- 'no'
- pl
- pt
- ro
- ru
- sk
- sl
- sr
- sv
- th
- tr
- uk
- ur
- vi
- vo
- zh
license:
- cc-by-sa-3.0
multilinguality:
- multilingual
paperswithcode_id: wit
pretty_name: Wikipedia-based Image Text
size_categories:
- 10M<n<100M
source_datasets:
- original
- extended|wikipedia
task_categories:
- text-retrieval
- image-to-text
task_ids:
- text-retrieval-other-text-image-retrieval
- image-captioning
---

# Dataset Card for WIT

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Dataset Preprocessing](#dataset-preprocessing)
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

- **Homepage:** [WIT homepage](https://github.com/google-research-datasets/wit)
- **Repository:** [WIT repository](https://github.com/google-research-datasets/wit)
- **Paper:** [WIT: Wikipedia-based Image Text Dataset for Multimodal Multilingual Machine Learning
](https://arxiv.org/abs/2103.01913)
- **Leaderboard:** [WIT leaderboard](https://www.kaggle.com/c/wikipedia-image-caption)
- **Point of Contact:** [WIT e-mail](mailto:wit-dataset@google.com)

### Dataset Summary

Wikipedia-based Image Text (WIT) Dataset is a large multimodal multilingual dataset. WIT is composed of a curated set of 37.6 million entity rich image-text examples with 11.5 million unique images across 108 Wikipedia languages. Its size enables WIT to be used as a pretraining dataset for multimodal machine learning models.

A few unique advantages of WIT:

* The largest multimodal dataset (time of this writing) by the number of image-text examples.
* A massively multilingual (first of its kind) with coverage for over 100+ languages.
* A collection of diverse set of concepts and real world entities.
* Brings forth challenging real-world test sets.

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


def fetch_single_image(image_url, timeout=None, retries=0):
    for _ in range(retries + 1):
        try:
            request = urllib.request.Request(
                image_url,
                data=None,
                headers={"user-agent": get_datasets_user_agent()},
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
dset = load_dataset("wit")
dset = dset.map(fetch_images, batched=True, batch_size=100, fn_kwargs={"num_threads": num_threads})
```

### Supported Tasks and Leaderboards

- `image-captioning`: This dataset can be used to train a model for image captioning where the goal is to predict a caption given the image.

- `text-retrieval`: The goal in this task is to build a model that retrieves the text closest to an image.

In these tasks, any combination of the `caption_reference_description`, `caption_attribution_description` and `caption_alt_text_description` fields can be used as the input text/caption. 

### Languages

The dataset contains examples from all Wikipedia languages, with the following stats:

Image-Text   | # Lang | Uniq. Images  | # Lang
------------ | ------ | ------------- | ------
total > 1M   | 9      | images > 1M   | 6
total > 500K | 10     | images > 500K | 12
total > 100K | 36     | images > 100K | 35
total > 50K  | 15     | images > 50K  | 17
total > 14K  | 38     | images > 13K  | 38

## Dataset Structure

### Data Instances

```
{
  'language': 'en',
  'page_url': 'https://en.wikipedia.org/wiki/Oxydactylus',
  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/5/5f/Oxydactylus_longipes_fm.jpg',
  'page_title': 'Oxydactylus',
  'section_title': None,
  'hierarchical_section_title': 'Oxydactylus',
  'caption_reference_description': None,
  'caption_attribution_description': 'English: Mounted skeleton of Oxydactylus longipes in the Field Museum of Natural History.',
  'caption_alt_text_description': None,
  'mime_type': 'image/jpeg',
  'original_height': 3564,
  'original_width': 2748,
  'is_main_image': True,
  'attribution_passes_lang_id': True,
  'page_changed_recently': True,
  'context_page_description': 'Oxydactylus is an extinct genus of camelid endemic to North America. It lived from the Late Oligocene to the Middle Miocene, existing for approximately 14 million years. The name is from the Ancient Greek οξύς and δάκτυλος.\nThey had very long legs and necks, and were probably adapted to eating high vegetation, much like modern giraffes. Unlike modern camelids, they had hooves, rather than tough sole-pads, and splayed toes.',
  'context_section_description': 'Oxydactylus is an extinct genus of camelid endemic to North America. It lived from the Late Oligocene to the Middle Miocene (28.4–13.7 mya), existing for approximately 14 million years. The name is from the Ancient Greek οξύς (oxys, "sharp")and δάκτυλος (daktylos, "finger").\n \nThey had very long legs and necks, and were probably adapted to eating high vegetation, much like modern giraffes. Unlike modern camelids, they had hooves, rather than tough sole-pads, and splayed toes.'
}
```

### Data Fields

- `language`: Language code depicting wikipedia language of the page
- `page_url`: URL to wikipedia page
- `image_url`: URL to wikipedia image
- `page_title`: Wikipedia page's title
- `section_title`: Section's title
- `hierarchical_section_title`: Hierarchical section's title
- `caption_reference_description`: This is the caption that is visible on the wiki page directly below the image.
- `caption_attribution_description`: This is the text found on the Wikimedia page of the image. This text is common to all occurrences of that image across all Wikipedias and thus can be in a language different to the original page article.
- `caption_alt_text_description`: This is the “alt” text associated with the image. While not visible in general, it is commonly used for accessibility / screen readers
- `mime_type`: Mime type associated to the image.
- `original_height`: Image height
- `original_width`: Image width
- `is_main_image`: Flag determining if the image is the first image of the page. Usually displayed on the top-right part of the page when using web browsers.
- `attribution_passes_lang_id`: Compared `language` field with the attribution language (written in the prefix of the attribution description). 
- `page_changed_recently`: [More Information Needed] 
- `context_page_description`: Page description corresponds to the short description of the page. It provides a concise explanation of the scope of the page.
- `context_section_description`: Text within the image's section.

<p align='center'>
  <img width='75%' src='https://production-media.paperswithcode.com/datasets/Screenshot_2021-03-04_at_14.26.02.png' alt="Half Dome" /> </br>
<b>Figure: WIT annotation example. </b>
</p>

Details on the field content can be found directly in the [paper, figure 5 and table 12.](https://arxiv.org/abs/2103.01913)

### Data Splits

All data is held in `train` split, with a total of 37046386 rows.

## Dataset Creation

### Curation Rationale

From the [repository](https://github.com/google-research-datasets/wit#motivation):

> Multimodal visio-linguistic models rely on a rich dataset to help them learn to model the relationship between images and texts. Having large image-text datasets can significantly improve performance, as shown by recent works. Furthermore the lack of language coverage in existing datasets (which are mostly only in English) also impedes research in the multilingual multimodal space – we consider this a lost opportunity given the potential shown in leveraging images (as a language-agnostic medium) to help improve our multilingual textual understanding.
>
> To address these challenges and advance research on multilingual, multimodal learning we created the Wikipedia-based Image Text (WIT) Dataset. WIT is created by extracting multiple different texts associated with an image (e.g., as shown in the above image) from Wikipedia articles and Wikimedia image links. This was accompanied by rigorous filtering to only retain high quality image-text sets.
>
> The resulting dataset contains over 37.6 million image-text sets – making WIT the largest multimodal dataset (publicly available at the time of this writing) with unparalleled multilingual coverage – with 12K+ examples in each of 108 languages (53 languages have 100K+ image-text pairs).

### Source Data

#### Initial Data Collection and Normalization

From the [paper, section 3.1](https://arxiv.org/abs/2103.01913):

> We started with all Wikipedia content pages (i.e., ignoring other
pages that have discussions, comments and such). These number about ∼124M pages across 279 languages.

#### Who are the source language producers?

Text was extracted from Wikipedia.

### Annotations

#### Annotation process

WIT was constructed using an automatic process. However it was human-validated.

From the [paper, section 3.7](https://arxiv.org/abs/2103.01913):

> To further verify the quality of the WIT dataset we performed a
study using (crowd-sourced) human annotators. As seen in Fig. 3,
we asked raters to answer 3 questions. Given an image and the page
title, raters first evaluate the quality of the attribution description
and reference description in the first two questions (order randomized). The third question understands the contextual quality of these
text descriptions given the page description and caption. Each response is on a 3-point scale: "Yes" if the text perfectly describes
the image, "Maybe" if it is sufficiently explanatory and "No" if it is
irrelevant or the image is inappropriate.

#### Who are the annotators?

[More Information Needed]

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

From the [paper, section 3.4](https://arxiv.org/abs/2103.01913):

> Lastly we found that certain image-text pairs occurred very
frequently. These were often generic images that did not have
much to do with the main article page. Common examples
included flags, logos, maps, insignia and such. To prevent
biasing the data, we heavily under-sampled all such images

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

[More Information Needed]

### Licensing Information

[More Information Needed]

### Citation Information

```bibtex
@article{srinivasan2021wit,
  title={WIT: Wikipedia-based Image Text Dataset for Multimodal Multilingual Machine Learning},
  author={Srinivasan, Krishna and Raman, Karthik and Chen, Jiecao and Bendersky, Michael and Najork, Marc},
  journal={arXiv preprint arXiv:2103.01913},
  year={2021}
}
```

### Contributions

Thanks to [@thomasw21](https://github.com/thomasw21), [@nateraw](https://github.com/nateraw) and [hassiahk](https://github.com/hassiahk) for adding this dataset.