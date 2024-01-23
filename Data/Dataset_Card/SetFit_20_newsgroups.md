This is a version of the [20 newsgroups dataset](https://scikit-learn.org/0.19/datasets/twenty_newsgroups.html#the-20-newsgroups-text-dataset) that is provided in Scikit-learn. From the Scikit-learn docs:

> The 20 newsgroups dataset comprises around 18000 newsgroups posts on 20 topics split in two subsets: one for training (or development) and the other one for testing (or for performance evaluation). The split between the train and test set is based upon a messages posted before and after a specific date.

We followed the [recommended practice](https://scikit-learn.org/0.19/datasets/twenty_newsgroups.html#filtering-text-for-more-realistic-training) to remove headers, signature blocks, and quotations from each news article.