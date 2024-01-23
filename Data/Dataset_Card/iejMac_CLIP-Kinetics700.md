---
annotations_creators:
- found
language_creators:
- found
language:
- en
license:
- mit
multilinguality:
- monolingual
pretty_name: CLIP-Kinetics700
size_categories:
- 100K<n<1M
task_categories:
- feature-extraction
- zero-shot-classification
---

# Dataset Card for CLIP-Kinetics70

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Dataset Preprocessing](#dataset-preprocessing)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Source Data](#source-data)
- [Simple Experiments](#dataset-creation)
  - [Zero-shot Evaluation](#zero-shot)
  - [Linear-probe Evaluation](#zero-shot)
  
## Dataset Description
### Dataset Summary

CLIP-Kinetics700 is a compressed version of the Kinetics700 dataset using OpenAI's CLIP model.

The original dataset is ~700 GB making it difficult to use and hold in memory on one machine. By downsampling each video to 1 FPS and encoding the frames using CLIP we we're able to compress the dataset to ~8 GB making it very memory-friendly and easy to use.

### Dataset Preprocessing

[clip-video-encode](https://github.com/iejMac/clip-video-encode) is a tool you can use to easily and efficiently compute CLIP embeddings from video frames. We used it to generate the embeddings for this dataset.

## Dataset Structure

### Data Format

We formatted this as a [WebDataset](https://github.com/webdataset/webdataset) for better data-loading performance when training the models.
Each split contains a list of tar files each with 10000 data samples. This format can be read and used easily using the EmbeddingWebDatasetReader from [clip-video-encode](https://github.com/iejMac/clip-video-encode).

```
CLIP-Kinetics700
 ├── splits.csv
 ├── ds_00000.tar
 |     ├── vid_00000.npy
 |     ├── vid_00000.txt
 |     ├── vid_00000.json
 |     ├── vid_00001.npy
 |     ├── vid_00001.txt
 |     ├── vid_00001.json
 |     └── ...
 |     ├── vid_10000.npy
 |     ├── vid_10000.txt
 |     ├── vid_10000.json
 ├── ds_00001.tar
 |     ├── vid_10001.npy
 |     ├── vid_10001.txt
 |     ├── vid_10001.json
 │     ...
 ...
```


### Data Fields
* vid.npy: the numpy array with the per-frame embeddings. Shape -> (n_frames, 512)
* vid.cap: the "caption" of the video. In this case it is the Kinetics700 label.
* vid.json: additional metadata - YouTube video ID, start time, end time.

### Data Splits
* Train - 536489 samples | 54 tar's
* Validation - 33966 samples | 4 tar's
* Test - 64532 samples | 7 tar's

## Dataset Creation

### Source Data

Data was sourced from DeepMind's [Kinetics700](https://www.deepmind.com/open-source/kinetics) dataset and downloaded using [this](https://github.com/cvdfoundation/kinetics-dataset) convenient repository.

## Simple Experiments

Using [this repository](https://github.com/LAION-AI/temporal-embedding-aggregation) we evaluate CLIP-Kinetics700 with the following simple methods:

### [Zero-shot Evaluation](https://github.com/LAION-AI/temporal-embedding-aggregation/blob/master/src/evaluation/zero_shot.py)

|                  | Accuracy |
| ---------------- | -------- |
|      Top-1       |   0.31   |
|      Top-5       |   0.56   |
| mean(Top1, Top5) |   0.44   |

### [Linear-probe Evaluation](https://github.com/LAION-AI/temporal-embedding-aggregation/blob/master/src/evaluation/linear_probe.py)

|                  | Accuracy |
| ---------------- | -------- |
|      Top-1       |   0.41   |
|      Top-5       |   0.65   |
| mean(Top1, Top5) |   0.53   |
