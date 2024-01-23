---
dataset_info:
  features:
  - name: image_lt
    dtype: image
  - name: image_rt
    dtype: image
  - name: category
    dtype: int32
  - name: instance
    dtype: int32
  - name: elevation
    dtype: int32
  - name: azimuth
    dtype: int32
  - name: lighting
    dtype: int32
  splits:
  - name: train
    num_bytes: 117947794.0
    num_examples: 24300
  - name: test
    num_bytes: 118130266.0
    num_examples: 24300
  download_size: 236815224
  dataset_size: 236078060.0
---
# Dataset Card for "smallnorb"

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

**NOTE:** This dataset is an unofficial port of small NORB based on a [repo from Andrea Palazzi](https://github.com/ndrplz/small_norb) using this [script](https://colab.research.google.com/drive/1Tx20uP1PrnyarsNCWf1dN9EQyr38BDIE?usp=sharing). For complete and accurate information, we highly recommend visiting the dataset's original homepage.

- **Homepage:** https://cs.nyu.edu/~ylclab/data/norb-v1.0-small/
- **Paper:** https://ieeexplore.ieee.org/document/1315150

### Dataset Summary

From the dataset's [homepage](https://cs.nyu.edu/~ylclab/data/norb-v1.0-small/):

> This database is intended for experiments in 3D object reocgnition from shape. It contains images of 50 toys belonging to 5 generic categories: four-legged animals, human figures, airplanes, trucks, and cars. The objects were imaged by two cameras under 6 lighting conditions, 9 elevations (30 to 70 degrees every 5 degrees), and 18 azimuths (0 to 340 every 20 degrees).
>
> The training set is composed of 5 instances of each category (instances 4, 6, 7, 8 and 9), and the test set of the remaining 5 instances (instances 0, 1, 2, 3, and 5).

## Dataset Structure

### Data Instances

An example of an instance in this dataset:

```
{
  'image_lt': <PIL.PngImagePlugin.PngImageFile image mode=L size=96x96 at 0x...>,
  'image_rt': <PIL.PngImagePlugin.PngImageFile image mode=L size=96x96 at 0x...>,
  'category': 0,
  'instance': 8,
  'elevation': 6,
  'azimuth': 4,
  'lighting': 4
}
```

### Data Fields

Explanation of this dataset's fields:

- `image_lt`: a PIL image of an object from the dataset taken with one of two cameras
- `image_rt`: a PIL image of an object from the dataset taken with one of two cameras
- `category`: the category of the object shown in the images
- `instance`: the instance of the category of the object shown in the images
- `elevation`: the label of the elevation of the cameras used in capturing a picture of the object
- `azimuth`: the label of the azimuth of the cameras used in capturing a picture of the object
- `lighting`: the label of the lighting condition used in capturing a picture of the object

For more information on what these categories and labels pertain to, please see [Dataset Summary](#dataset-summary) or the [repo](https://github.com/ndrplz/small_norb) used in processing the dataset.

### Data Splits

Information on this dataset's splits:

|      | train | test  |
|------|------:|------:|
| size | 24300 | 24300 |

## Additional Information

### Dataset Curators

Credits from the dataset's [homepage](https://cs.nyu.edu/~ylclab/data/norb-v1.0-small/):

> [Fu Jie Huang](http://www.cs.nyu.edu/jhuangfu/), [Yann LeCun](http://yann.lecun.com/)
> 
> Courant Institute, New York University
> 
> October, 2005

### Licensing Information

From the dataset's [homepage](https://cs.nyu.edu/~ylclab/data/norb-v1.0-small/):

> This database is provided for research purposes. It cannot be sold. Publications that include results obtained with this database should reference the following paper:
> 
> Y. LeCun, F.J. Huang, L. Bottou, Learning Methods for Generic Object Recognition with Invariance to Pose and Lighting. IEEE Computer Society Conference on Computer Vision and Pattern Recognition (CVPR) 2004

### Citation Information

From the dataset's [homepage](https://cs.nyu.edu/~ylclab/data/norb-v1.0-small/):

> Publications that include results obtained with this database should reference the following paper:
> 
> Y. LeCun, F.J. Huang, L. Bottou, Learning Methods for Generic Object Recognition with Invariance to Pose and Lighting. IEEE Computer Society Conference on Computer Vision and Pattern Recognition (CVPR) 2004

```
@inproceedings{lecun2004learning,
  title={Learning methods for generic object recognition with invariance to pose and lighting},
  author={LeCun, Yann and Huang, Fu Jie and Bottou, Leon},
  booktitle={Proceedings of the 2004 IEEE Computer Society Conference on Computer Vision and Pattern Recognition, 2004. CVPR 2004.},
  volume={2},
  pages={II--104},
  year={2004},
  organization={IEEE}
}
```

DOI: [10.1109/CVPR.2004.1315150](https://doi.org/10.1109/CVPR.2004.1315150)

### Contributions

Code to process small NORB adapted from [Andrea Palazzi's repo](https://github.com/ndrplz/small_norb) with this [script](https://colab.research.google.com/drive/1Tx20uP1PrnyarsNCWf1dN9EQyr38BDIE?usp=sharing).