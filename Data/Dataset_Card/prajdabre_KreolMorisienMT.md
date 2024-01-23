---
license: cc
---

MorisienMT is a dataset for Mauritian Creole Machine Translation. 
This dataset consists of training, development and test set splits for English--Creole as well as French--Creole translation.
The data comes from a variety of sources and hence can be considered as belonging to the general domain.

The development and test sets consist of 500 and 1000 sentences respectively. Both evaluation sets are trilingual.

The training set for English--Creole contains 21,810 lines.
The training set for French--Creole contains 15,239 lines.
Additionally, one can extract a trilingual English-French-Creole training set of 13,861 lines using Creole as a pivot.

Finally, we also provide a Creole monolingual corpus of 45,364 lines.

Note that a significant portion of the dataset is a dictionary of word pairs/triplets, nevertheless it is a start.

Usage: (TODO: beautify)
1. Using huggingface datasets: load_dataset("prajdabre/MorisienMT", "en-cr", split="train")
2. Convert to moses format: load the dataset as in step 1, each item is a json object so iterate over the loaded dataset object and use the key and value, "input" and "target" respectively, to get the translation pairs.

Feel free to use the dataset for your research but don't forget to attribute our upcoming paper which will be uploaded to arxiv shortly.

Note: MorisienMT was originally partly developed by Dr Aneerav Sukhoo from the University of Mauritius in 2014 when he was a visiting researcher in IIT Bombay. 
Dr Sukhoo and I worked on the MT experiments together, but never publicly released the dataset back then. 
Furthermore, the dataset splits and experiments were not done in a highly principled manner, which is required in the present day. 
Therefore, we improve the quality of splits and officially release the data for people to use.