---
dataset_info:
  features:
  - name: passage
    dtype: string
  splits:
  - name: train
    num_bytes: 18979214734
    num_examples: 88328203
  download_size: 1025261393
  dataset_size: 18979214734
---
# `chinese_clean_passages_80m`

包含**8千余万**（88328203）个**纯净**中文段落，不包含任何字母、数字。\
Containing more than **80 million pure \& clean** Chinese passages, without any letters/digits/special tokens.

文本长度大部分介于50\~200个汉字之间。\
The passage length is approximately 50\~200 Chinese characters.

通过`datasets.load_dataset()`下载数据，会产生38个大小约340M的数据包，共约12GB，所以请确保有足够空间。\
Downloading the dataset will result in 38 data shards each of which is about 340M and 12GB in total. Make sure there's enough space in your device:)
```
>>> 
passage_dataset = load_dataset('beyond/chinese_clean_passages_80m')

<<<
Downloading data: 100%|█| 341M/341M [00:06<00:00, 52.0MB
Downloading data: 100%|█| 342M/342M [00:06<00:00, 54.4MB
Downloading data: 100%|█| 341M/341M [00:06<00:00, 49.1MB
Downloading data: 100%|█| 341M/341M [00:14<00:00, 23.5MB
Downloading data: 100%|█| 341M/341M [00:10<00:00, 33.6MB
Downloading data: 100%|█| 342M/342M [00:07<00:00, 43.1MB
...(38 data shards)
```


本数据集被用于训练[GENIUS模型中文版](https://huggingface.co/spaces/beyond/genius)，如果这个数据集对您的研究有帮助，请引用以下论文。
This dataset is created for the pre-training of [GENIUS model](https://huggingface.co/spaces/beyond/genius), if you find this dataset useful, please cite our paper. 
```
@article{guo2022genius,
  title={GENIUS: Sketch-based Language Model Pre-training via Extreme and Selective Masking for Text Generation and Augmentation},
  author={Guo, Biyang and Gong, Yeyun and Shen, Yelong and Han, Songqiao and Huang, Hailiang and Duan, Nan and Chen, Weizhu},
  journal={arXiv preprint arXiv:2211.10330},
  year={2022}
}
```


---
Acknowledgment:\
数据是基于[CLUE中文预训练语料集](https://github.com/CLUEbenchmark/CLUE)进行处理、过滤得到的。\
This dataset is processed/filtered from the [CLUE pre-training corpus](https://github.com/CLUEbenchmark/CLUE).

原始数据集引用:
```
@misc{bright_xu_2019_3402023,
author       = {Bright Xu},
title        = {NLP Chinese Corpus: Large Scale Chinese Corpus for NLP },
month        = sep,
year         = 2019,
doi          = {10.5281/zenodo.3402023},
version      = {1.0},
publisher    = {Zenodo},
url          = {https://doi.org/10.5281/zenodo.3402023}
}
```
