---
annotations_creators: []
license: []
pretty_name: tabular_benchmark
tags: []
task_categories:
- tabular-classification
- tabular-regression
dataset_info:
- config_name: reg_cat
  splits:
  - reg_cat/*
- config_name: reg_num
  splits:
  - reg_num/*
- config_name: clf_cat
  splits:
  - clf_cat/*
- config_name: clf_num
  splits:
  - clf_num/*
duplicated_from: inria-soda/tabular-benchmark
---

# Tabular Benchmark

## Dataset Description

This dataset is a curation of various datasets from [openML](https://www.openml.org/) and is curated to benchmark performance of various machine learning algorithms.

- **Repository:** https://github.com/LeoGrin/tabular-benchmark/community
- **Paper:** https://hal.archives-ouvertes.fr/hal-03723551v2/document

### Dataset Summary

Benchmark made of curation of various tabular data learning tasks, including:
- Regression from Numerical and Categorical Features
- Regression from Numerical Features
- Classification from Numerical and Categorical Features
- Classification from Numerical Features

### Supported Tasks and Leaderboards

- `tabular-regression`
- `tabular-classification`

## Dataset Structure

### Data Splits

This dataset consists of four splits (folders) based on tasks and datasets included in tasks.

- reg_num: Task identifier for regression on numerical features.
- reg_cat: Task identifier for regression on numerical and categorical features.
- clf_num: Task identifier for classification on numerical features.
- clf_cat: Task identifier for classification on categorical features.

Depending on the dataset you want to load, you can load the dataset by passing `task_name/dataset_name` to `data_files` argument of `load_dataset` like below:

```python
from datasets import load_dataset
dataset = load_dataset("inria_soda/tabular-benchmark", data_files="reg_cat/house_sales.csv")
```


## Dataset Creation

### Curation Rationale

This dataset is curated to benchmark performance of tree based models against neural networks. The process of picking the datasets for curation is mentioned in the paper as below:

- **Heterogeneous columns**. Columns should correspond to features of different nature. This excludes
images or signal datasets where each column corresponds to the same signal on different sensors.
- **Not high dimensional**. We only keep datasets with a d/n ratio below 1/10.
- **Undocumented datasets** We remove datasets where too little information is available. We did keep
datasets with hidden column names if it was clear that the features were heterogeneous.
- **I.I.D. data**. We remove stream-like datasets or time series.
- **Real-world data**. We remove artificial datasets but keep some simulated datasets. The difference is
subtle, but we try to keep simulated datasets if learning these datasets are of practical importance
(like the Higgs dataset), and not just a toy example to test specific model capabilities.
- **Not too small**. We remove datasets with too few features (< 4) and too few samples (< 3 000). For
benchmarks on numerical features only, we remove categorical features before checking if enough
features and samples are remaining.
- **Not too easy**. We remove datasets which are too easy. Specifically, we remove a dataset if a default
Logistic Regression (or Linear Regression for regression) reach a score whose relative difference
with the score of both a default Resnet (from Gorishniy et al. [2021]) and a default HistGradientBoosting model (from scikit learn) is below 5%. Other benchmarks use different metrics to
remove too easy datasets, like removing datasets which can be learnt perfectly by a single decision
classifier [Bischl et al., 2021], but this does not account for different Bayes rate of different datasets.
As tree-based methods have been shown to be superior to Logistic Regression [Fernández-Delgado
et al., 2014] in our setting, a close score for these two types of models indicates that we might
already be close to the best achievable score.
- **Not deterministic**. We remove datasets where the target is a deterministic function of the data. This
mostly means removing datasets on games like poker and chess. Indeed, we believe that these
datasets are very different from most real-world tabular datasets, and should be studied separately

### Source Data


**Numerical Classification**
|dataset_name| n_samples| n_features| original_link| new_link|
|----|----|----|----|----|
|credit| 16714| 10 |https://openml.org/d/151 |https://www.openml.org/d/44089|
|california |20634 |8 |https://openml.org/d/293 |https://www.openml.org/d/44090|
|wine |2554 |11 |https://openml.org/d/722 |https://www.openml.org/d/44091|
|electricity| 38474 |7| https://openml.org/d/821 |https://www.openml.org/d/44120|
|covertype |566602 |10 |https://openml.org/d/993| https://www.openml.org/d/44121|
|pol |10082 |26 |https://openml.org/d/1120 |https://www.openml.org/d/44122|
|house_16H |13488| 16 |https://openml.org/d/1461| https://www.openml.org/d/44123|
|kdd_ipums_la_97-small| 5188 |20 |https://openml.org/d/1489 |https://www.openml.org/d/44124|
|MagicTelescope| 13376| 10| https://openml.org/d/41150 |https://www.openml.org/d/44125|
|bank-marketing |10578 |7 |https://openml.org/d/42769| https://www.openml.org/d/44126|
|phoneme |3172| 5 |https://openml.org/d/1044| https://www.openml.org/d/44127|
|MiniBooNE| 72998| 50 |https://openml.org/d/41168 |https://www.openml.org/d/44128|
|Higgs| 940160 |24| https://www.kaggle.com/c/GiveMeSomeCredit/data?select=cs-training.csv |https://www.openml.org/d/44129|
|eye_movements| 7608 |20 |https://www.dcc.fc.up.pt/ltorgo/Regression/cal_housing.html |https://www.openml.org/d/44130|
|jannis |57580 |54 |https://archive.ics.uci.edu/ml/datasets/wine+quality |https://www.openml.org/d/44131|

**Categorical Classification**
|dataset_name |n_samples| n_features |original_link |new_link|
|----|----|----|----|----|
|electricity |38474| 8 |https://openml.org/d/151| https://www.openml.org/d/44156|
|eye_movements |7608 |23| https://openml.org/d/1044 |https://www.openml.org/d/44157|
|covertype |423680| 54| https://openml.org/d/1114 |https://www.openml.org/d/44159|
|rl |4970 |12 |https://openml.org/d/1596 |https://www.openml.org/d/44160|
|road-safety| 111762 |32 |https://openml.org/d/41160 |https://www.openml.org/d/44161|
|compass |16644 |17 |https://openml.org/d/42803 |https://www.openml.org/d/44162|
|KDDCup09_upselling |5128 |49 |https://www.kaggle.com/datasets/danofer/compass?select=cox-violent-parsed.csv |https://www.openml.org/d/44186|

**Numerical Regression**
|dataset_name| n_samples| n_features| original_link| new_link|
|----|----|----|----|----|
|cpu_act |8192 |21| https://openml.org/d/197 |https://www.openml.org/d/44132|
|pol | 15000| 26 |https://openml.org/d/201| https://www.openml.org/d/44133|
|elevators |16599 |16 |https://openml.org/d/216| https://www.openml.org/d/44134|
|isolet |7797| 613| https://openml.org/d/300| https://www.openml.org/d/44135|
|wine_quality |6497 |11| https://openml.org/d/287 | https://www.openml.org/d/44136|
|Ailerons |13750 |33| https://openml.org/d/296 | https://www.openml.org/d/44137|
|houses |20640| 8| https://openml.org/d/537 | https://www.openml.org/d/44138|
|house_16H |22784| 16 |https://openml.org/d/574 | https://www.openml.org/d/44139|
|diamonds |53940| 6| https://openml.org/d/42225 | https://www.openml.org/d/44140|
|Brazilian_houses |10692| 8 |https://openml.org/d/42688 | https://www.openml.org/d/44141|
|Bike_Sharing_Demand| 17379| 6| https://openml.org/d/42712 | https://www.openml.org/d/44142|
|nyc-taxi-green-dec-2016 |581835| 9| https://openml.org/d/42729 | https://www.openml.org/d/44143|
|house_sales |21613 |15 | https://openml.org/d/42731| https://www.openml.org/d/44144|
|sulfur |10081| 6 | https://openml.org/d/23515 | https://www.openml.org/d/44145|
|medical_charges | 163065 |3 | https://openml.org/d/42720 | https://www.openml.org/d/44146|
|MiamiHousing2016 |13932| 13 |https://openml.org/d/43093 | https://www.openml.org/d/44147|
|superconduct |21263 |79| https://openml.org/d/43174 | https://www.openml.org/d/44148|
|california |20640| 8 |https://www.dcc.fc.up.pt/ ltorgo/Regression/cal_housing.html |https://www.openml.org/d/44025|
|fifa |18063 |5 |https://www.kaggle.com/datasets/stefanoleone992/fifa-22-complete-player-dataset| https://www.openml.org/d/44026|
|year |515345 |90 |https://archive.ics.uci.edu/ml/datasets/yearpredictionmsd| https://www.openml.org/d/44027|





**Categorical Regression**
|dataset_name| n_samples| n_features| original_link| new_link|
|----|----|----|----|----|
|yprop_4_1 |8885 |62 |https://openml.org/d/416 |https://www.openml.org/d/44054|
|analcatdata_supreme |4052| 7 |https://openml.org/d/504 |https://www.openml.org/d/44055|
|visualizing_soil |8641| 4 |https://openml.org/d/688 |https://www.openml.org/d/44056|
|black_friday |166821| 9 |https://openml.org/d/41540| https://www.openml.org/d/44057|
|diamonds | 53940| 9| https://openml.org/d/42225| https://www.openml.org/d/44059|
|Mercedes_Benz_Greener_Manufacturing |4209 |359| https://openml.org/d/42570 |https://www.openml.org/d/44061|
|Brazilian_houses| 10692| 11 |https://openml.org/d/42688 |https://www.openml.org/d/44062|
|Bike_Sharing_Demand| 17379| 11 |https://openml.org/d/42712 |https://www.openml.org/d/44063|
|OnlineNewsPopularity |39644| 59| https://openml.org/d/42724| https://www.openml.org/d/44064|
|nyc-taxi-green-dec-2016| 581835 |16 |https://openml.org/d/42729|https://www.openml.org/d/44065|
|house_sales | 21613| 17| https://openml.org/d/42731| https://www.openml.org/d/44066|
|particulate-matter-ukair-2017 |394299 |6| https://openml.org/d/42207| https://www.openml.org/d/44068|
|SGEMM_GPU_kernel_performance | 241600| 9 |https://openml.org/d/43144| https://www.openml.org/d/44069|


### Dataset Curators

Léo Grinsztajn, Edouard Oyallon, Gaël Varoquaux.

### Licensing Information

[More Information Needed]

### Citation Information

Léo Grinsztajn, Edouard Oyallon, Gaël Varoquaux. Why do tree-based models still outperform deep
learning on typical tabular data?. NeurIPS 2022 Datasets and Benchmarks Track, Nov 2022, New
Orleans, United States. ffhal-03723551v2f