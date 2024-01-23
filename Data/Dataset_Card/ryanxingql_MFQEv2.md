---
license: apache-2.0
---
# MFQEv2 Dataset

For some video enhancement/restoration tasks, lossless reference videos are necessary.

We open-source the dataset used in our [MFQEv2 paper](https://arxiv.org/abs/1902.09707), which includes 108 lossless YUV videos for training and 18 test videos recommended by [ITU-T](https://ieeexplore.ieee.org/document/6317156).

## 1. Content

- 108 lossless YUV videos for training.
- 18 lossless YUV videos for test, recommended by ITU-T.
- An HEVC compression tool box.

43.1 GB in total.

## 2. Download Raw Videos

[[Dropbox]](https://www.dropbox.com/sh/tphdy1lmlpz7zq3/AABR4Qim-P-3xGtouWk6ohi5a?dl=0)

or [[百度网盘 (key: mfqe)]](https://pan.baidu.com/s/1oBZf75bFGRanLmQQLAg4Ew)

## 3. Compress Videos

We compress both training and test videos by [HM](https://hevc.hhi.fraunhofer.de/) 16.5 at low delay P (LDP) mode with QP=37. The video compression toolbox is provided at the dataset folder.

We will get:

```tex
MFQEv2_dataset/
├── train_108/
│   ├── raw/
│   └── HM16.5_LDP/
│       └── QP37/
├── test_18/
│   ├── raw/
│   └── HM16.5_LDP/
│       └── QP37/
├── video_compression/
│   └── ...
└── README.md
```

### Ubuntu

1. `cd video_compression/`
2. Edit `option.yml`.
3. `chmod +x TAppEncoderStatic`
4. `python unzip_n_compress.py`

### Windows

1. Unzip `train_108.zip` and `test_18.zip` manually!
2. `cd video_compression\`
3. Edit `option.yml` (e.g., `system: windows`).
4. `python unzip_n_compress.py`

## 4. Citation

If you find this helpful, please star and cite:

```tex
@article{2019xing,
	doi = {10.1109/tpami.2019.2944806},
	url = {https://doi.org/10.1109%2Ftpami.2019.2944806},
	year = 2021,
	month = {mar},
	publisher = {Institute of Electrical and Electronics Engineers ({IEEE})},
	volume = {43},
	number = {3},
	pages = {949--963},
	author = {Zhenyu Guan and Qunliang Xing and Mai Xu and Ren Yang and Tie Liu and Zulin Wang},
	title = {{MFQE} 2.0: A New Approach for Multi-Frame Quality Enhancement on Compressed Video},
	journal = {{IEEE} Transactions on Pattern Analysis and Machine Intelligence}
}
```
