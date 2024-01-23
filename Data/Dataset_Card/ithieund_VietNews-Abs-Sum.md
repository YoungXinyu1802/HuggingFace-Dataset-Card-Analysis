# VietNews-Abs-Sum
A dataset for Vietnamese Abstractive Summarization task.  
It includes all articles from Vietnews (VNDS) dataset which was released by Van-Hau Nguyen et al.  
The articles were collected from tuoitre.vn, vnexpress.net, and nguoiduatin.vn online newspaper by the authors.

# Introduction
This dataset was extracted from Train/Val/Test split of Vietnews dataset. All files from *test_tokenized*, *train_tokenized* and *val_tokenized* directories are fetched and preprocessed with punctuation normalization. The subsets then are stored in the *raw* director with 3 files *train.tsv*, *valid.tsv*, and *test.tsv* accordingly. These files will be considered as the original raw dataset as nothing changes except the punctuation normalization.

As pointed out in *BARTpho: Pre-trained Sequence-to-Sequence Models for Vietnamese*, there are lots of duplicated samples across subsets. Therefore, we do another preprocessing process to remove all the duplicated samples. The process includes the following steps:
- First, remove all duplicates from each subset
- Second, merge all subsets into 1 set with the following order: test + val + train
- Finally, remove all duplicates from that merged set and then split out into 3 new subsets

The final subsets are the same to the orignal subsets but all duplicates were removed. Each subset now has total samples as follows:
- train_no_dups.tsv: 99134 samples
- valid_no_dups.tsv: 22184 samples
- test_no_dups.tsv: 22498 samples

Totally, we have 99134 + 22184 + 22498 = 143816 samples after filtering!  
Note that this result is not the same as the number of samples reported in BARTpho paper, but there is no duplicate inside each subset or across subsets anymore.

These filtered subsets are also exported into JSONLINE format to support future training script that requires this data format.

# Directory structure
- raw: contains 3 raw subset files fetched from Vietnews directories
  - train.tsv
  - val.tsv
  - test.tsv
- processed: contains duplicates filtered subsets
  - test.tsv
  - train.tsv
  - valid.tsv
  - test.jsonl
  - train.jsonl
  - valid.jsonl
  - [and other variants]

# Credits
- Special thanks to Vietnews (VNDS) authors: https://github.com/ThanhChinhBK/vietnews
