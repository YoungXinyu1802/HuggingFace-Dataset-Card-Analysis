---
annotations_creators:
- crowdsourced
language_creators:
- crowdsourced
language:
- zh
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: laion-high-resolution-chinese
task_categories:
- feature-extraction
---

# laion-high-resolution-chinese

## 简介 Brief Introduction

取自Laion5B-high-resolution多语言多模态数据集中的中文部分，一共2.66M个图文对。

A subset from Laion5B-high-resolution (a multimodal dataset), around 2.66M image-text pairs (only Chinese).

## 数据集信息 Dataset Information

大约一共2.66M个中文图文对。大约占用381MB空间（仅仅是url等文本信息，不包含图片）。

- Homepage: [laion-5b](https://laion.ai/blog/laion-5b/)
- Huggingface: [laion/laion-high-resolution](https://huggingface.co/datasets/laion/laion-high-resolution)

## 下载 Download

```bash
mkdir release && cd release
for i in {00000..00015}; do wget https://huggingface.co/datasets/wanng/laion-high-resolution-chinese/resolve/main/data/train-$i-of-00016.parquet; done
cd ..
```

## Lisence

CC-BY-4.0
