---
license: apache-2.0
---


# CSAbstruct

CSAbstruct was created as part of *"Pretrained Language Models for Sequential Sentence Classification"* ([ACL Anthology][2], [arXiv][1], [GitHub][6]).

It contains 2,189 manually annotated computer science abstracts with sentences annotated according to their rhetorical roles in the abstract, similar to the [PUBMED-RCT][3] categories.


## Dataset Construction Details

CSAbstruct is a new dataset of annotated computer science abstracts with sentence labels according to their rhetorical roles.
The key difference between this dataset and [PUBMED-RCT][3] is that PubMed abstracts are written according to a predefined structure, whereas computer science papers are free-form.
Therefore, there is more variety in writing styles in CSAbstruct.
CSAbstruct is collected from the Semantic Scholar corpus [(Ammar et a3., 2018)][4].
E4ch sentence is annotated by 5 workers on the [Figure-eight platform][5], with one of 5 categories `{BACKGROUND, OBJECTIVE, METHOD, RESULT, OTHER}`.

We use 8 abstracts (with 51 sentences) as test questions to train crowdworkers.
Annotators whose accuracy is less than 75% are disqualified from doing the actual annotation job.
The annotations are aggregated using the agreement on a single sentence weighted by the accuracy of the annotator on the initial test questions.
A confidence score is associated with each instance based on the annotator initial accuracy and agreement of all annotators on that instance.
We then split the dataset 75%/15%/10% into train/dev/test partitions, such that the test set has the highest confidence scores.
Agreement rate on a random subset of 200 sentences is 75%, which is quite high given the difficulty of the task.
Compared with [PUBMED-RCT][3], our dataset exhibits a wider variety of writ- ing styles, since its abstracts are not written with an explicit structural template.

## Dataset Statistics

| Statistic                |  Avg ± std  |
|--------------------------|-------------|
| Doc length in sentences  |  6.7 ± 1.99 |
| Sentence length in words | 21.8 ± 10.0 |

| Label         | % in Dataset |
|---------------|--------------|
| `BACKGROUND`  | 33%          |
| `METHOD`      | 32%          |
| `RESULT`      | 21%          |
| `OBJECTIVE`   | 12%          |
| `OTHER`       | 03%          |

## Citation

If you use this dataset, please cite the following paper:

```
@inproceedings{Cohan2019EMNLP,
  title={Pretrained Language Models for Sequential Sentence Classification},
  author={Arman Cohan, Iz Beltagy, Daniel King, Bhavana Dalvi, Dan Weld},
  year={2019},
  booktitle={EMNLP},
}
```

[1]: https://arxiv.org/abs/1909.04054
[2]: https://aclanthology.org/D19-1383
[3]: https://github.com/Franck-Dernoncourt/pubmed-rct
[4]: https://aclanthology.org/N18-3011/
[5]: https://www.figure-eight.com/
[6]: https://github.com/allenai/sequential_sentence_classification
