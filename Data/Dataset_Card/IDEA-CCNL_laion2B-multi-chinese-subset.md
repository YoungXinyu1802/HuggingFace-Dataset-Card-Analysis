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
pretty_name: laion2B-multi-chinese-subset
task_categories:
- feature-extraction
---

# laion2B-multi-chinese-subset

- Github: [Fengshenbang-LM](https://github.com/IDEA-CCNL/Fengshenbang-LM)
- Docs: [Fengshenbang-Docs](https://fengshenbang-doc.readthedocs.io/)

## 简介 Brief Introduction

取自Laion2B多语言多模态数据集中的中文部分，一共143M个图文对。

A subset from Laion2B (a multimodal dataset), around 143M image-text pairs (only Chinese).

## 数据集信息 Dataset Information

大约一共143M个中文图文对。大约占用19GB空间（仅仅是url等文本信息，不包含图片）。

- Homepage: [laion-5b](https://laion.ai/blog/laion-5b/)
- Huggingface: [laion/laion2B-multi](https://huggingface.co/datasets/laion/laion2B-multi)

## 下载 Download

```bash
mkdir laion2b_chinese_release && cd laion2b_chinese_release
for i in {00000..00012}; do wget https://huggingface.co/datasets/IDEA-CCNL/laion2B-multi-chinese-subset/resolve/main/data/train-$i-of-00013.parquet; done
cd ..
```

## Lisence

CC-BY-4.0

## 引用 Citation

如果您在您的工作中使用了我们的模型，可以引用我们的[论文](https://arxiv.org/abs/2209.02970)：

If you are using the resource for your work, please cite the our [paper](https://arxiv.org/abs/2209.02970):

```text
@article{fengshenbang,
  author    = {Junjie Wang and Yuxiang Zhang and Lin Zhang and Ping Yang and Xinyu Gao and Ziwei Wu and Xiaoqun Dong and Junqing He and Jianheng Zhuo and Qi Yang and Yongfeng Huang and Xiayu Li and Yanghan Wu and Junyu Lu and Xinyu Zhu and Weifeng Chen and Ting Han and Kunhao Pan and Rui Wang and Hao Wang and Xiaojun Wu and Zhongshen Zeng and Chongpei Chen and Ruyi Gan and Jiaxing Zhang},
  title     = {Fengshenbang 1.0: Being the Foundation of Chinese Cognitive Intelligence},
  journal   = {CoRR},
  volume    = {abs/2209.02970},
  year      = {2022}
}
```

也可以引用我们的[网站](https://github.com/IDEA-CCNL/Fengshenbang-LM/):

You can also cite our [website](https://github.com/IDEA-CCNL/Fengshenbang-LM/):

```text
@misc{Fengshenbang-LM,
  title={Fengshenbang-LM},
  author={IDEA-CCNL},
  year={2021},
  howpublished={\url{https://github.com/IDEA-CCNL/Fengshenbang-LM}},
}
