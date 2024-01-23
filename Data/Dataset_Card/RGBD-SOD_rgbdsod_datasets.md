---
dataset_info:
  features:
  - name: depth
    dtype: image
  - name: rgb
    dtype: image
  - name: gt
    dtype: image
  - name: name
    dtype: string
  config_name: v1
  splits:
  - name: train
    num_bytes: 7378488019
    num_examples: 8025
  - name: validation
    num_bytes: 4190272788
    num_examples: 4600
  download_size: 3506288426
  dataset_size: 11568760807
---

# RGB-D Salient Object Detection Dataset (RGB-D SOD)

RGB-D Salient Object Detection (RGB-D SOD) aims to detect and segment objects that *visually attract the most human interest* from a pair of color and depth images.

## Train

- COME-8K [8025 samples]

## Dev

- COME-E [4600 samples]

## Test

- Coming soon

## How to use

~~~python
from datasets import load_dataset

dataset = load_dataset(
    "RGBD-SOD/rgbdsod_datasets", "v1", split="train", cache_dir="data"
)
print(dataset[0])
~~~

## BibTeX entry and citation info

```bibtex
@inproceedings{zhang2021rgb,
  title={RGB-D saliency detection via cascaded mutual information minimization},
  author={Zhang, Jing and Fan, Deng-Ping and Dai, Yuchao and Yu, Xin and Zhong, Yiran and Barnes, Nick and Shao, Ling},
  booktitle={Proceedings of the IEEE/CVF International Conference on Computer Vision},
  pages={4338--4347},
  year={2021}
}
```
