---
pretty_name: IMDb
task_categories:
- text-classification
task_ids:
- sentiment-classification
language:
- en
license:
- other
multilinguality:
- monolingual
size_categories:
- 10K<n<100K
---
# Dataset Card for IMDb Movie Reviews

## Dataset Description

- **Homepage:** [http://ai.stanford.edu/~amaas/data/sentiment/](http://ai.stanford.edu/~amaas/data/sentiment/)
- **Repository:** [More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
- **Paper:** [More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
- **Point of Contact:** [More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
- **Size of downloaded dataset files:** [More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
- **Size of the generated dataset:** [More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
- **Total amount of disk used:** [More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Dataset Summary

This is a custom train/test/validation split of the IMDb Large Movie Review Dataset available from [http://ai.stanford.edu/~amaas/data/sentiment/](http://ai.stanford.edu/~amaas/data/sentiment/).

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

[More Information Needed]

## Dataset Structure

#### IMDb_movie_reviews
An example of 'train':
```
{
    "text": "Beautifully photographed and ably acted, generally, but the writing is very slipshod. There are scenes of such unbelievability that there is no joy in the watching. The fact that the young lover has a twin brother, for instance, is so contrived that I groaned out loud. And the "emotion-light bulb connection" seems gimmicky, too.<br /><br />I don\'t know, though. If you have a few glasses of wine and feel like relaxing with something pretty to look at with a few flaccid comedic scenes, this is a pretty good movie. No major effort on the part of the viewer required. But Italian film, especially Italian comedy, is usually much, much better than this."
    "label": 0,
}
```

### Data Fields

The data fields are the same among all splits.

#### IMDb_movie_reviews
- `text`: a `string` feature.
- `label`: a classification label, with values `neg` (0), `pos` (1).

### Data Splits

|   name           | train | validation |  test |
|------------------|------:|-----------:|------:|
|IMDb_movie_reviews| 36000 |       4000 | 10000 |

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

[More Information Needed]

### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

[More Information Needed]

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

[More Information Needed]

### Licensing Information

[More Information Needed]

### Citation Information

```
@InProceedings{maas-EtAl:2011:ACL-HLT2011,
  author    = {Maas, Andrew L.  and  Daly, Raymond E.  and  Pham, Peter T.  and  Huang, Dan  and  Ng, Andrew Y.  and  Potts, Christopher},
  title     = {Learning Word Vectors for Sentiment Analysis},
  booktitle = {Proceedings of the 49th Annual Meeting of the Association for Computational Linguistics: Human Language Technologies},
  month     = {June},
  year      = {2011},
  address   = {Portland, Oregon, USA},
  publisher = {Association for Computational Linguistics},
  pages     = {142--150},
  url       = {http://www.aclweb.org/anthology/P11-1015}
}

```

### Contributions

[More Information Needed]