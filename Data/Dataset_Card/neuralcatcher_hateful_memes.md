# The Hateful Memes Challenge README

The Hateful Memes Challenge is a dataset and benchmark created by Facebook AI to drive and measure progress on multimodal reasoning and understanding. The task focuses on detecting hate speech in multimodal memes.

Please see the paper for further details:

[The Hateful Memes Challenge: Detecting Hate Speech in Multimodal Memes
D. Kiela, H. Firooz, A. Mohan, V. Goswami, A. Singh, P. Ringshia, D. Testuggine](
https://arxiv.org/abs/2005.04790)

For more details, see also the website:

https://hatefulmemeschallenge.com

# Dataset details

The files for this folder are arranged as follows:

img/                    -        the PNG images
train.jsonl             -        the training set
dev_seen.jsonl          -        the "seen" development set
test_seen.jsonl         -        the "seen" test set
dev_unseen.jsonl        -        the "unseen" development set
test_unseen.jsonl       -        the "unseen" test set

The "seen" dataset was presented in the NeurIPS paper; the “unseen” dev and test set were released as a part of the NeurIPS 2020 competition.

The .jsonl format contains one JSON-encoded example per line, each of which has the following fields:

‘text’        - the text occurring in the meme
‘img’         - the path to the image in the img/ directory
‘label’       - the label for the meme (0=not-hateful, 1=hateful), provided for train and dev

The metric to use is AUROC. You may also report accuracy in addition, since this is arguably more interpretable. To compute these metrics, we recommend the roc_auc_score and accuracy_score methods in sklearn.metrics, with default settings.

# Getting started
To get started working on this dataset, there's an easy-to-use "starter kit" available in MMF: https://github.com/facebookresearch/mmf/tree/master/projects/hateful_memes.

# Note on Annotator Accuracy
As is to be expected with a dataset of this size and nature, some of the examples in the training set have been misclassified. We are not claiming that our dataset labels are completely accurate, or even that all annotators would agree on a particular label. Misclassifications, although possible, should be very rare in the dev and seen test set, however, and we will take extra care with the unseen test set.

As a reminder, the annotations collected for this dataset were not collected using Facebook annotators and we did not employ Facebook’s hate speech policy. As such, the dataset labels do not in any way reflect Facebook’s official stance on this matter.

# License
The dataset is licensed under the terms in the `LICENSE.txt` file.

# Image Attribution
If you wish to display example memes in your paper, please provide the following attribution:

*Image is a compilation of assets, including ©Getty Image.*

# Citations
If you wish to cite this work, please use the following BiBTeX:

```
@inproceedings{Kiela:2020hatefulmemes,
 author = {Kiela, Douwe and Firooz, Hamed and Mohan, Aravind and Goswami, Vedanuj and Singh, Amanpreet and Ringshia, Pratik and Testuggine, Davide},
 booktitle = {Advances in Neural Information Processing Systems},
 editor = {H. Larochelle and M. Ranzato and R. Hadsell and M. F. Balcan and H. Lin},
 pages = {2611--2624},
 publisher = {Curran Associates, Inc.},
 title = {The Hateful Memes Challenge: Detecting Hate Speech in Multimodal Memes},
 url = {https://proceedings.neurips.cc/paper/2020/file/1b84c4cee2b8b3d823b30e2d604b1878-Paper.pdf},
 volume = {33},
 year = {2020}
}
```

# Contact
If you have any questions or comments on the dataset, please contact hatefulmemeschallenge@fb.com or one of the authors.
