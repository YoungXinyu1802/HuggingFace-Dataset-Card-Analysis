---
language:
- ru
multilinguality:
- monolingual
pretty_name: Kinopoisk
size_categories:
- 10K<n<100K
task_categories:
- text-classification
task_ids:
- sentiment-classification
---

### Dataset Summary

Kinopoisk movie reviews dataset (TOP250 & BOTTOM100 rank lists).

In total it contains 36,591 reviews from July 2004 to November 2012.

With following distribution along the 3-point sentiment scale:
- Good: 27,264;
- Bad: 4,751;
- Neutral: 4,576.

### Data Fields

Each sample contains the following fields:
- **part**: rank list top250 or bottom100;
- **movie_name**;
- **review_id**;
- **author**: review author;
- **date**: date of a review;
- **title**: review title;
- **grade3**: sentiment score Good, Bad or Neutral;
- **grade10**: sentiment score on a 10-point scale parsed from text;
- **content**: review text.

### Python
```python3
import pandas as pd
df = pd.read_json('kinopoisk.jsonl', lines=True)
df.sample(5)
```

### Citation
```
@article{blinov2013research,
  title={Research of lexical approach and machine learning methods for sentiment analysis},
  author={Blinov, PD and Klekovkina, Maria and Kotelnikov, Eugeny and Pestov, Oleg},
  journal={Computational Linguistics and Intellectual Technologies},
  volume={2},
  number={12},
  pages={48--58},
  year={2013}
}
```
