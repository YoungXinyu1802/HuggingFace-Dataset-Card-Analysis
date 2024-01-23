---
pretty_name: Cartoon Set
size_categories:
- 10K<n<100K
task_categories:
- image
- computer-vision
- generative-modelling
license: cc-by-4.0
---
# Dataset Card for Cartoon Set
## Table of Contents
- [Dataset Card for Cartoon Set](#dataset-card-for-cartoon-set)
  - [Table of Contents](#table-of-contents)
  - [Dataset Description](#dataset-description)
    - [Dataset Summary](#dataset-summary)
      - [Usage](#usage)
  - [Dataset Structure](#dataset-structure)
    - [Data Instances](#data-instances)
    - [Data Fields](#data-fields)
    - [Data Splits](#data-splits)
  - [Dataset Creation](#dataset-creation)
    - [Licensing Information](#licensing-information)
    - [Citation Information](#citation-information)
    - [Contributions](#contributions)
## Dataset Description
- **Homepage:** https://google.github.io/cartoonset/
- **Repository:** https://github.com/google/cartoonset/
- **Paper:** XGAN: Unsupervised Image-to-Image Translation for Many-to-Many Mappings
- **Leaderboard:**
- **Point of Contact:**
### Dataset Summary

![Cartoon Set sample image](https://huggingface.co/datasets/cgarciae/cartoonset/resolve/main/sample.png)

[Cartoon Set](https://google.github.io/cartoonset/) is a collection of random, 2D cartoon avatar images. The cartoons vary in 10 artwork categories, 4 color categories, and 4 proportion categories, with a total of ~10^13 possible combinations. We provide sets of 10k and 100k randomly chosen cartoons and labeled attributes.

#### Usage
`cartoonset` provides the images as PNG byte strings, this gives you a bit more flexibility into how to load the data. Here we show 2 ways:

**Using PIL:**
```python
import datasets
from io import BytesIO
from PIL import Image

ds = datasets.load_dataset("cgarciae/cartoonset", "10k") # or "100k"

def process_fn(sample):
    img = Image.open(BytesIO(sample["img_bytes"]))
    ...
    return {"img": img}

ds = ds.map(process_fn, remove_columns=["img_bytes"])
```

**Using TensorFlow:**
```python
import datasets
import tensorflow as tf

hfds = datasets.load_dataset("cgarciae/cartoonset", "10k") # or "100k"

ds = tf.data.Dataset.from_generator(
    lambda: hfds,
    output_signature={
        "img_bytes": tf.TensorSpec(shape=(), dtype=tf.string),
    },
)

def process_fn(sample):
    img = tf.image.decode_png(sample["img_bytes"], channels=3)
    ...
    return {"img": img}

ds = ds.map(process_fn)
```

**Additional features:**
You can also access the features that generated each sample e.g:

```python
ds = datasets.load_dataset("cgarciae/cartoonset", "10k+features") # or "100k+features"
```

Apart from `img_bytes` these configurations add a total of 18 * 2 additional `int` features, these come in `{feature}`, `{feature}_num_categories` pairs where `num_categories` indicates the number of categories for that feature. See [Data Fields](#data-fields) for the complete list of features.

## Dataset Structure
### Data Instances
A sample from the training set is provided below:
```python
{
  'img_bytes': b'0x...',
}
```
If `+features` is added to the dataset name, the following additional fields are provided:

```python
{
  'img_bytes': b'0x...',
  'eye_angle': 0,
  'eye_angle_num_categories': 3,
  'eye_lashes': 0,
  'eye_lashes_num_categories': 2,
  'eye_lid': 0,
  'eye_lid_num_categories': 2,
  'chin_length': 2,
  'chin_length_num_categories': 3,
  ...
}
```

### Data Fields
- `img_bytes`: A byte string containing the raw data of a 500x500 PNG image.

If `+features` is appended to the dataset name, the following additional `int32` fields are provided:

- `eye_angle`
- `eye_angle_num_categories`
- `eye_lashes`
- `eye_lashes_num_categories`
- `eye_lid`
- `eye_lid_num_categories`
- `chin_length`
- `chin_length_num_categories`
- `eyebrow_weight`
- `eyebrow_weight_num_categories`
- `eyebrow_shape`
- `eyebrow_shape_num_categories`
- `eyebrow_thickness`
- `eyebrow_thickness_num_categories`
- `face_shape`
- `face_shape_num_categories`
- `facial_hair`
- `facial_hair_num_categories`
- `facial_hair_num_categories`
- `facial_hair_num_categories`
- `hair`
- `hair_num_categories`
- `hair_num_categories`
- `hair_num_categories`
- `eye_color`
- `eye_color_num_categories`
- `face_color`
- `face_color_num_categories`
- `hair_color`
- `hair_color_num_categories`
- `glasses`
- `glasses_num_categories`
- `glasses_color`
- `glasses_color_num_categories`
- `eyes_slant`
- `eye_slant_num_categories`
- `eyebrow_width`
- `eyebrow_width_num_categories`
- `eye_eyebrow_distance`
- `eye_eyebrow_distance_num_categories`


### Data Splits
Train
## Dataset Creation
### Licensing Information
This data is licensed by Google LLC under a Creative Commons Attribution 4.0 International License.
### Citation Information
```
@article{DBLP:journals/corr/abs-1711-05139,
  author    = {Amelie Royer and
               Konstantinos Bousmalis and
               Stephan Gouws and
               Fred Bertsch and
               Inbar Mosseri and
               Forrester Cole and
               Kevin Murphy},
  title     = {{XGAN:} Unsupervised Image-to-Image Translation for many-to-many Mappings},
  journal   = {CoRR},
  volume    = {abs/1711.05139},
  year      = {2017},
  url       = {http://arxiv.org/abs/1711.05139},
  eprinttype = {arXiv},
  eprint    = {1711.05139},
  timestamp = {Mon, 13 Aug 2018 16:47:38 +0200},
  biburl    = {https://dblp.org/rec/journals/corr/abs-1711-05139.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```
### Contributions
