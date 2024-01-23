# MOLD - {M}arathi {O}ffensive {L}anguage {D}ataset

The {M}arathi {O}ffensive {L}anguage {D}ataset (MOLD) contains a collection of 2500 annotated Marathi tweets.

The files included are: 
```
MOLD
│   README.md  
└───data
    │   MOLD_train.csv
    │   MOLD_test.csv
```
- `MOLD_train.csv`: contains 1,875 annotated tweets for the training set.  
- `MOLD_test.csv`: contains 625 annotated tweets for the test set. 


The dataset was annotated using crowdsourcing. The gold labels were assigned taking the agreement of six annotators into consideration. No correction has been carried out on the crowdsourcing annotations. 
Each instance in MOLD has been annotated as offensive or not_offensive




## Citation
If you used MOLD, please refer to this paper:

```bash
@InProceedings{mold,
author = {Gaikwad, Saurabh and Ranasinghe, Tharindu and Zampieri, Marcos and Homan, Christopher M.},
title = {Cross-lingual Offensive Language Identification for Low Resource Languages: The Case of Marathi},
booktitle = {Proceedings of RANLP},
year = {2021}
}
```

