---
language:
- en
license:
- mit
multilinguality:
- monolingual
size_categories:
- 100K<n<1M
pretty_name: Large Logo Dataset
---

# Dataset Card for Large Logo Dataset (LLD)

## Description

Adapted from the original [LLD dataset](https://data.vision.ee.ethz.ch/sagea/lld/). Original description:

> Designing a logo for a new brand is a lengthy and tedious back-and-forth process between a designer and a client. In this paper we explore to what extent machine learning can solve the creative task of the designer. For this, we build a dataset -- LLD -- of 600k+ logos crawled from the world wide web. Training Generative Adversarial Networks (GANs) for logo synthesis on such multi-modal data is not straightforward and results in mode collapse for some state-of-the-art methods. We propose the use of synthetic labels obtained through clustering to disentangle and stabilize GAN training. We are able to generate a high diversity of plausible logos and we demonstrate latent space exploration techniques to ease the logo design task in an interactive manner. Moreover, we validate the proposed clustered GAN training on CIFAR 10, achieving state-of-the-art Inception scores when using synthetic labels obtained via clustering the features of an ImageNet classifier. GANs can cope with multi-modal data by means of synthetic labels achieved through clustering, and our results show the creative potential of such techniques for logo synthesis and manipulation.

## Schema

``` yaml
- name: <string> Name of the company / organization
- description: <string> Description of what the organization does
- images: <np.uint8, shape(3, 400, 400)> Three logo images of 400x400 
```

## Citations

``` text
@misc{sage2017logodataset,
author={Sage, Alexander and Agustsson, Eirikur and Timofte, Radu and Van Gool, Luc},
title = {LLD - Large Logo Dataset - version 0.1},
year = {2017}, 
howpublished = "\url{https://data.vision.ee.ethz.ch/cvl/lld}"}

```
