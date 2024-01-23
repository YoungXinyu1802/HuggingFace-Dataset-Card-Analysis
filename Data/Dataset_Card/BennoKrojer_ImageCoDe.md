---
license: afl-3.0
---

# Dataset Card for ImageCoDe

To get started quickly, load descriptions via:
```
from datasets import load_dataset
examples = load_dataset('BennoKrojer/ImageCoDe')
```
And download `image_sets.zip` for all images sets (each directory consisting of 10 images).

## Dataset Description

- **Homepage & Leaderboard:** https://mcgill-nlp.github.io/imagecode/
- **Repository:** https://github.com/McGill-NLP/imagecode
- **Paper:** https://arxiv.org/abs/2203.15867
- **Point of Contact:** benno DOT krojer ÄT gmail DOT com

### Dataset Summary

We introduce ImageCoDe, a vision-and-language benchmark that requires contextual language understanding in the form of pragmatics, temporality, long descriptions and visual nuances. The task: Given a detailed description, retrieve the target image among 10 minimally contrastive images. ImageCoDe contains 21K descriptions and 94K images. THe images are primarily frames based on video datasets.

## Dataset Structure

### Data Instances

An instance contains a description, the corresponding image set name, and the target index:
```
{"image_set": "video-storytelling-videowedding_de8dLXvgV-I-shot6_0",
"image_index": "8",
"description": "The flowers the woman in the teal strapless dress is carrying are completely obscured by the man in the black shirt's head. "}
```
### Data Splits

| Dataset Split | Number of Descriptions in Split |
| ------------- |----------------------------- |
| Train         | 16,594                       |
| Validation    | 2,302                        |
| Test          | 2,306                        |

## Dataset Creation

### Curation Rationale

The main goal of ImageCoDe is to highlight weaknesses of recent Vision-and-Language models regarding complex language and fine-grained visual representations. In addition, we found that the dataset offers plenty of pragmatic examples and is therefore suitable for studying pragmatics.