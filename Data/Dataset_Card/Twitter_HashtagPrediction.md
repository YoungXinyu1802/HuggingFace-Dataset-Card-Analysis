---
license: cc-by-4.0
language: 
  - sl
  - ur
  - sd
  - pl
  - vi
  - sv
  - am
  - da
  - mr
  - no
  - gu
  - in
  - ja
  - el
  - lv
  - it
  - ca
  - is
  - cs
  - te
  - tl
  - ro
  - ckb
  - pt
  - ps
  - zh
  - sr
  - pa
  - si
  - ml
  - ht
  - kn
  - ar
  - hu
  - nl
  - bg
  - bn
  - ne
  - hi
  - de
  - ko
  - fi
  - fr
  - es
  - et
  - en
  - fa
  - lt
  - or
  - cy
  - eu
  - iw
  - ta
  - th
  - tr
tags:
  - Twitter
  - Multilingual
  - Classification
  - Benchmark
---


# Hashtag Prediction Dataset from paper TwHIN-BERT: A Socially-Enriched Pre-trained Language Model for Multilingual Tweet Representations
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-green.svg?style=flat-square)](https://huggingface.co/datasets/Twitter/HashtagPrediction/discussions) [![arXiv](https://img.shields.io/badge/arXiv-2203.15827-b31b1b.svg)](https://arxiv.org/abs/2209.07562) [![Github](https://img.shields.io/badge/Github-TwHIN--BERT-brightgreen?logo=github)](https://github.com/xinyangz/TwHIN-BERT)


This repo contains the Hashtag prediction dataset from our paper [TwHIN-BERT: A Socially-Enriched Pre-trained Language Model for Multilingual Tweet Representations](https://arxiv.org/abs/2209.07562). <br />
[[arXiv]](https://arxiv.org/abs/2209.07562)
[[HuggingFace Models]](https://huggingface.co/Twitter/twhin-bert-base)
[[Github repo]](https://github.com/xinyangz/TwHIN-BERT)

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

## Download
Use the `hashtag-classification-id.zip` in this repo. [Link](https://huggingface.co/datasets/Twitter/HashtagPrediction/blob/main/hashtag-classification-id.zip).

Check the first-author's GitHub repo for any supplemental dataset material or code. [Link](https://github.com/xinyangz/TwHIN-BERT)

## Dataset Description

The hashtag prediction dataset is a multilingual classification dataset. Separate datasets are given for different languages. We first select 500 (or all available) popular hashtags of each language and then sample 10k (or all available) popular Tweets that contain these hashtags. We make sure each Tweet will have exactly one of the selected hashtags.

The evaluation task is a multiclass classification task, with hashtags as labels. We remove the hashtag from the Tweet, and let the model predict the removed hashtag.

We provide Tweet ID and raw text hashtag labels in `tsv` files. For each language, we provide train, development, and test splits.

To use the dataset, you must hydrate the Tweet text with [Twitter API](https://developer.twitter.com/en/docs/twitter-api), and **remove the hashtag used for label from each Tweet** .

The data format is displayed below.

| ID | label |
| ------------- | ------------- |
| 1   | hashtag |
| 2   | another hashtag |

## Citation
If you use our dataset in your work, please cite the following:
```bib
@article{zhang2022twhin,
  title={TwHIN-BERT: A Socially-Enriched Pre-trained Language Model for Multilingual Tweet Representations},
  author={Zhang, Xinyang and Malkov, Yury and Florez, Omar and Park, Serim and McWilliams, Brian and Han, Jiawei and El-Kishky, Ahmed},
  journal={arXiv preprint arXiv:2209.07562},
  year={2022}
}
```