---
license: apache-2.0
language:
- en
multilinguality:
- monolingual
size_categories:
- 10K<n<100K
task_categories:
- depth-estimation
task_ids: []
pretty_name: NYU Depth V2
tags: 
- depth-estimation
paperswithcode_id: nyuv2
dataset_info:
  features:
  - name: image
    dtype: image
  - name: depth_map
    dtype: image
  splits:
  - name: train
    num_bytes: 20212097551
    num_examples: 47584
  - name: validation
    num_bytes: 240785762
    num_examples: 654
  download_size: 35151124480
  dataset_size: 20452883313
---

# Dataset Card for NYU Depth V2

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks](#supported-tasks)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Visualization](#visualization)
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

- **Homepage:** [NYU Depth Dataset V2 homepage](https://cs.nyu.edu/~silberman/datasets/nyu_depth_v2.html)
- **Repository:** Fast Depth [repository](https://github.com/dwofk/fast-depth) which was used to source the dataset in this repository. It is a preprocessed version of the original NYU Depth V2 dataset linked above. It is also used in [TensorFlow Datasets](https://www.tensorflow.org/datasets/catalog/nyu_depth_v2).
- **Papers:** [Indoor Segmentation and Support Inference from RGBD Images](http://cs.nyu.edu/~silberman/papers/indoor_seg_support.pdf) and [FastDepth: Fast Monocular Depth Estimation on Embedded Systems](https://arxiv.org/abs/1903.03273)
- **Point of Contact:** [Nathan Silberman](mailto:silberman@@cs.nyu.edu) and [Diana Wofk](mailto:dwofk@alum.mit.edu)

### Dataset Summary

As per the [dataset homepage](https://cs.nyu.edu/~silberman/datasets/nyu_depth_v2.html):

The NYU-Depth V2 data set is comprised of video sequences from a variety of indoor scenes as recorded by both the RGB and Depth cameras from the Microsoft [Kinect](http://www.xbox.com/kinect). It features:

* 1449 densely labeled pairs of aligned RGB and depth images
* 464 new scenes taken from 3 cities
* 407,024 new unlabeled frames
* Each object is labeled with a class and an instance number (cup1, cup2, cup3, etc)

The dataset has several components:

* Labeled: A subset of the video data accompanied by dense multi-class labels. This data has also been preprocessed to fill in missing depth labels.
* Raw: The raw rgb, depth and accelerometer data as provided by the Kinect.
* Toolbox: Useful functions for manipulating the data and labels.

### Supported Tasks

- `depth-estimation`: Depth estimation is the task of approximating the perceived depth of a given image. In other words, it's about measuring the distance of each image pixel from the camera.
- `semantic-segmentation`: Semantic segmentation is the task of associating every pixel of an image to a class label. 

There are other tasks supported by this dataset as well. You can find more about them by referring to [this resource](https://paperswithcode.com/dataset/nyuv2).


### Languages

English.

## Dataset Structure

### Data Instances

A data point comprises an image and its annotation depth map for both the `train` and `validation` splits. 

```
{
  'image': <PIL.PngImagePlugin.PngImageFile image mode=RGB at 0x1FF32A3EDA0>,
  'depth_map': <PIL.PngImagePlugin.PngImageFile image mode=L at 0x1FF32E5B978>,
}
```

### Data Fields

- `image`: A `PIL.Image.Image` object containing the image. Note that when accessing the image column: `dataset[0]["image"]` the image file is automatically decoded. Decoding of a large number of image files might take a significant amount of time. Thus it is important to first query the sample index before the `"image"` column, *i.e.* `dataset[0]["image"]` should **always** be preferred over `dataset["image"][0]`.
- `depth_map`: A `PIL.Image.Image` object containing the annotation depth map.

### Data Splits

The data is split into training, and validation splits. The training data contains 47584 images, and the validation data contains 654 images.

## Visualization

You can use the following code snippet to visualize samples from the dataset:

```py
from datasets import load_dataset
import numpy as np
import matplotlib.pyplot as plt


cmap = plt.cm.viridis

ds = load_dataset("sayakpaul/nyu_depth_v2")


def colored_depthmap(depth, d_min=None, d_max=None):
    if d_min is None:
        d_min = np.min(depth)
    if d_max is None:
        d_max = np.max(depth)
    depth_relative = (depth - d_min) / (d_max - d_min)
    return 255 * cmap(depth_relative)[:,:,:3] # H, W, C


def merge_into_row(input, depth_target):
    input = np.array(input)
    depth_target = np.squeeze(np.array(depth_target))

    d_min = np.min(depth_target)
    d_max = np.max(depth_target)
    depth_target_col = colored_depthmap(depth_target, d_min, d_max)
    img_merge = np.hstack([input, depth_target_col])
    
    return img_merge


random_indices = np.random.choice(len(ds["train"]), 9).tolist()
train_set = ds["train"]

plt.figure(figsize=(15, 6))

for i, idx in enumerate(random_indices):
    ax = plt.subplot(3, 3, i + 1)
    image_viz = merge_into_row(
        train_set[idx]["image"], train_set[idx]["depth_map"]
    )
    plt.imshow(image_viz.astype("uint8"))
    plt.axis("off")
```

## Dataset Creation

### Curation Rationale

The rationale from [the paper](http://cs.nyu.edu/~silberman/papers/indoor_seg_support.pdf) that introduced the NYU Depth V2 dataset:

> We present an approach to interpret the major surfaces, objects, and support relations of an indoor scene from an RGBD image. Most existing work ignores physical interactions or is applied only to tidy rooms and hallways. Our goal is to parse typical, often messy, indoor scenes into floor, walls, supporting surfaces, and object regions, and to recover support relationships. One of our main interests is to better understand how 3D cues can best inform a structured 3D interpretation.

### Source Data

#### Initial Data Collection 

> The dataset consists of 1449 RGBD images, gathered from a wide range
of commercial and residential buildings in three different US cities, comprising
464 different indoor scenes across 26 scene classes.A dense per-pixel labeling was
obtained for each image using Amazon Mechanical Turk.

### Annotations

#### Annotation process

This is an involved process. Interested readers are referred to Sections 2, 3, and 4 of the [original paper](http://cs.nyu.edu/~silberman/papers/indoor_seg_support.pdf). 

#### Who are the annotators?

AMT annotators.

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

* Original NYU Depth V2 dataset: Nathan Silberman, Derek Hoiem, Pushmeet Kohli, Rob Fergus
* Preprocessed version: Diana Wofk, Fangchang Ma, Tien-Ju Yang, Sertac Karaman, Vivienne Sze

### Licensing Information

The preprocessed NYU Depth V2 dataset is licensed under a [MIT License](https://github.com/dwofk/fast-depth/blob/master/LICENSE).

### Citation Information

```bibtex
@inproceedings{Silberman:ECCV12,
  author    = {Nathan Silberman, Derek Hoiem, Pushmeet Kohli and Rob Fergus},
  title     = {Indoor Segmentation and Support Inference from RGBD Images},
  booktitle = {ECCV},
  year      = {2012}
}

@inproceedings{icra_2019_fastdepth,
	author      = {{Wofk, Diana and Ma, Fangchang and Yang, Tien-Ju and Karaman, Sertac and Sze, Vivienne}},
	title       = {{FastDepth: Fast Monocular Depth Estimation on Embedded Systems}},
	booktitle   = {{IEEE International Conference on Robotics and Automation (ICRA)}},
	year        = {{2019}}
}
```

### Contributions

Thanks to [@sayakpaul](https://huggingface.co/sayakpaul) for adding this dataset.