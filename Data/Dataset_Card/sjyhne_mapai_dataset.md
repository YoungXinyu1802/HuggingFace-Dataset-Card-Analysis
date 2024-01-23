---
license: cc-by-4.0
dataset_info:
  features:
  - name: image
    dtype: image
  - name: lidar
    dtype: image
  - name: mask
    dtype: image
  - name: filename
    dtype: string
  splits:
  - name: validation
    num_bytes: 2192377881.0
    num_examples: 1500
  - name: task1_test
    num_bytes: 1893839365.136
    num_examples: 1368
  - name: task2_test
    num_bytes: 1372710117.0
    num_examples: 978
  - name: train
    num_bytes: 10403414735.0
    num_examples: 7000
  download_size: 7060470972
  dataset_size: 15862342098.136
features:
- name: image
  dtype: image
- name: lidar
  dtype: image
- name: mask
  dtype: image
- name: filename
  dtype: string
splits:
- name: validation
  num_bytes: 2192349531
  num_examples: 1500
- name: task1_test
  num_bytes: 1893803900.136
  num_examples: 1368
- name: task2_test
  num_bytes: 1372684773
  num_examples: 978
- name: train
  num_bytes: 10403282435
  num_examples: 7000
download_size: 7060394132
dataset_size: 15862120639.136
---

# Dataset Card for the MapAI Dataset

## Dataset Description

- **Repository:** [MapAI: Precision in Building Segmentation - Github Repository](https://github.com/Sjyhne/MapAI-Competition)
- **Paper:** [MapAI: Precision in Building Segmentation](https://journals.uio.no/NMI/article/view/9849)
- **Point of Contact:** [Sander Riisøen Jyhne](mailto:sander.jyhne@kartverket.no)
- **Leaderboard:** [Papers with Code leaderboard for MapAI: Precision in Building Segmentation Dataset](https://paperswithcode.com/dataset/sander-jyhne)

### Dataset Summary

The dataset comprises 7500 training images and 1500 validation images from Denmark. The test dataset is split into two tasks, where the first task (1368 images) is to segment the buildings only using aerial images. In contrast, the second task (978 images) allows using aerial images and lidar data. All data samples have a resolution of 500x500. The aerial images are RGB images, while the lidar data are rasterized. The ground truth masks have two classes, building, and background. All data derives from a production setting, which means that there will be buildings that are not present in the ground truth and vice versa.

### Supported Tasks and Leaderboards
- 'segmentation'

### Data Fields

- 'image': A 500x500x3 RGB orthophoto
- 'lidar': A 500x500 rasterized LiDAR image
- 'mask': A 500x500 ground truth mask where 1's are buildings and 0's are background
- 'filename': An identifying filename for the data tile

### Data Splits

The MapAI Dataset has four splits; _train_, _validation_, _task1_test_, _task2_test_. Below are the statistics for each split.

| Dataset Split | Number of Instances in Split                |
| ------------- | ------------------------------------------- |
| Train         | 7 500                                       |
| Validation    | 1 500                                       |
| Task1_test    | 1 368                                       |
| Task2_test    | 978                                         |

### Social Impact of Dataset

The purpose of the dataset is to help develop models for accurate segmentation of buildings, which will help downstream tasks such as 3-dimensional building construction.

### Citation Information

```
@article{Jyhne2022,
   author = {Sander Jyhne and Morten Goodwin and Per-Arne Andersen and Ivar Oveland and Alexander Salveson Nossum and Karianne Ormseth and Mathilde Ørstavik and Andrew C Flatman},
   doi = {10.5617/NMI.9849},
   issn = {2703-9196},
   issue = {3},
   journal = {Nordic Machine Intelligence},
   keywords = {Aerial Images,Deep Learning,Image segmentation,machine learning,remote sensing,semantic segmentation},
   month = {9},
   pages = {1-3},
   title = {MapAI: Precision in Building Segmentation},
   volume = {2},
   url = {https://journals.uio.no/NMI/article/view/9849},
   year = {2022},
}
```