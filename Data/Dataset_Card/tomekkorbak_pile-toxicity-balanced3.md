## Generation procedure

The dataset was constructed using documents from [the Pile](https://pile.eleuther.ai/) scored using using [Perspective API](http://perspectiveapi.com) toxicity scores.

The procedure was the following:
1. A chunk of the Pile (2.2m documents) was scored using the Perspective API (on May 18-20 2022) giving [`tomekkorbak/pile-chunk-toxicity-scored-3`](https://huggingface.co/datasets/tomekkorbak/pile-chunk-toxicity-scored-3).
1. The first half of this dataset is 100k *most* toxic documents from `pile-chunk-toxicity-scored-3`
2. The first half of this dataset is 100k documents sampled randomly from of `pile-chunk-toxicity-scored-3`
3. Then, the dataset was shuffled and a 9:1 train-test split was done

## Basic stats

The average document-level scores of the bad and random halves are 0.34 and 0.05, respectively. The average token-level score of the whole dataset is 0.2025. The average document-level score is 0.1983.

## Score histogram

![](https://huggingface.co/datasets/tomekkorbak/pile-toxicity-balanced3/resolve/main/Screenshot%202022-05-20%20at%2020.32.05.png)
