---
annotations_creators:
- crowdsourced
language_creators:
- crowdsourced
language:
- zh
license:
- cc-by-nc-sa-4.0
multilinguality:
- monolingual
pretty_name: Wukong100M
task_categories:
- feature-extraction
---


# wukong100m

## 简介 Brief Introduction

取自Noah-Wukong多语言多模态数据集中的中文部分，一共100M个图文对。

A subset from Noah-Wukong (a multimodal dataset), around 100M image-text pairs (only Chinese).

## 数据集信息 Dataset Information

大约一共100M个中文图文对。大约占用16GB空间（仅仅是url等文本信息，不包含图片）。下载成功率在80%左右。（虽然我没有统计下载之后会占用多少空间，但是，可以说非常非常大）

- Homepage: [Noah-Wukong](https://wukong-dataset.github.io/wukong-dataset/index.html)

## 下载 Download

```bash
mkdir wukong100m && cd wukong100m
for i in {00000..00031}; do wget https://huggingface.co/datasets/wanng/wukong100m/resolve/main/data/train-$i-of-00032.parquet; done
cd ..
```

## Lisence

CC BY-NC-SA 4.0
