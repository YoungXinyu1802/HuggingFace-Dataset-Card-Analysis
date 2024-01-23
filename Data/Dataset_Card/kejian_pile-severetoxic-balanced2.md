
# Dataset Card for [kejian/pile-severetoxic-balanced2]

## Generation Procedures 

The dataset was constructed using documents from the Pile scored using Perspective API SEVERE-TOXICITY scores.

The procedure was the following:
- The first half of this dataset is kejian/pile-severetoxic-chunk-0, 100k most toxic documents from Pile chunk-0
- The second half of this dataset is kejian/pile-severetoxic-random100k, 100k randomly sampled documents from Pile chunk-3
- Then, the dataset was shuffled and a 9:1 train-test split was done

## Basic Statistics 

The average scores of the most toxic and random half are 0.555 and 0.061, respectively. The average score of the whole dataset is 0.308; the median is 0.385.

![](https://huggingface.co/datasets/kejian/pile-severetoxic-balanced2/resolve/main/score-hist-all.png)

The weighted average score (weighted by document length) is 0.337. The correlation between score and document length is 0.099
