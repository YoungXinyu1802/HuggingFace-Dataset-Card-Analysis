
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
dataset = load_dataset("inria-soda/tabular-benchmark", data_files="reg_cat/house_sales.csv")
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
- **Not too easy**. We remove datasets which are too easy. Specifically, we remove a dataset if a simple model (max of a single tree and a regression, logistic or OLS)
 reaches a score whose relative difference with the score of both a default Resnet (from Gorishniy et al. [2021]) and a default HistGradientBoosting model (from scikit learn)
 is below 5%. Other benchmarks use different metrics to remove too easy datasets, like removing datasets perfectly separated by a single decision classifier [Bischl et al., 2021],
 but this ignores varying Bayes rate across datasets. As tree ensembles are superior to simple trees and logistic regresison [Fernández-Delgado et al., 2014], 
 a close score for the simple and powerful models suggests that we are already close to the best achievable score.
- **Not deterministic**. We remove datasets where the target is a deterministic function of the data. This
mostly means removing datasets on games like poker and chess. Indeed, we believe that these
datasets are very different from most real-world tabular datasets, and should be studied separately

### Source Data


**Numerical Classification**
|dataset_name|n_samples|n_features|original_link|new_link|
|---|---|---|---|---|
|electricity|38474.0|7.0|https://www.openml.org/d/151|https://www.openml.org/d/44120|
|covertype|566602.0|10.0|https://www.openml.org/d/293|https://www.openml.org/d/44121|
|pol|10082.0|26.0|https://www.openml.org/d/722|https://www.openml.org/d/44122|
|house_16H|13488.0|16.0|https://www.openml.org/d/821|https://www.openml.org/d/44123|
|MagicTelescope|13376.0|10.0|https://www.openml.org/d/1120|https://www.openml.org/d/44125|
|bank-marketing|10578.0|7.0|https://www.openml.org/d/1461|https://www.openml.org/d/44126|
|Bioresponse|3434.0|419.0|https://www.openml.org/d/4134|https://www.openml.org/d/45019|
|MiniBooNE|72998.0|50.0|https://www.openml.org/d/41150|https://www.openml.org/d/44128|
|default-of-credit-card-clients|13272.0|20.0|https://www.openml.org/d/42477|https://www.openml.org/d/45020|
|Higgs|940160.0|24.0|https://www.openml.org/d/42769|https://www.openml.org/d/44129|
|eye_movements|7608.0|20.0|https://www.openml.org/d/1044|https://www.openml.org/d/44130|
|Diabetes130US|71090.0|7.0|https://www.openml.org/d/4541|https://www.openml.org/d/45022|
|jannis|57580.0|54.0|https://www.openml.org/d/41168|https://www.openml.org/d/45021|
|heloc|10000.0|22.0|"https://www.kaggle.com/datasets/averkiyoliabev/home-equity-line-of-creditheloc?select=heloc_dataset_v1+%281%29.csv"|https://www.openml.org/d/45026|
|credit|16714.0|10.0|"https://www.kaggle.com/c/GiveMeSomeCredit/data?select=cs-training.csv"|https://www.openml.org/d/44089|
|california|20634.0|8.0|"https://www.dcc.fc.up.pt/ltorgo/Regression/cal_housing.html"|https://www.openml.org/d/45028|


**Categorical Classification**
|dataset_name|n_samples|n_features|original_link|new_link|
|---|---|---|---|---|
|electricity|38474.0|8.0|https://www.openml.org/d/151|https://www.openml.org/d/44156|
|eye_movements|7608.0|23.0|https://www.openml.org/d/1044|https://www.openml.org/d/44157|
|covertype|423680.0|54.0|https://www.openml.org/d/1596|https://www.openml.org/d/44159|
|albert|58252.0|31.0|https://www.openml.org/d/41147|https://www.openml.org/d/45035|
|compas-two-years|4966.0|11.0|https://www.openml.org/d/42192|https://www.openml.org/d/45039|
|default-of-credit-card-clients|13272.0|21.0|https://www.openml.org/d/42477|https://www.openml.org/d/45036|
|road-safety|111762.0|32.0|https://www.openml.org/d/42803|https://www.openml.org/d/45038|


**Numerical Regression**
|dataset_name|n_samples|n_features|original_link|new_link|
|---|---|---|---|---|
|cpu_act|8192.0|21.0|https://www.openml.org/d/197|https://www.openml.org/d/44132|
|pol|15000.0|26.0|https://www.openml.org/d/201|https://www.openml.org/d/44133|
|elevators|16599.0|16.0|https://www.openml.org/d/216|https://www.openml.org/d/44134|
|wine_quality|6497.0|11.0|https://www.openml.org/d/287|https://www.openml.org/d/44136|
|Ailerons|13750.0|33.0|https://www.openml.org/d/296|https://www.openml.org/d/44137|
|yprop_4_1|8885.0|42.0|https://www.openml.org/d/416|https://www.openml.org/d/45032|
|houses|20640.0|8.0|https://www.openml.org/d/537|https://www.openml.org/d/44138|
|house_16H|22784.0|16.0|https://www.openml.org/d/574|https://www.openml.org/d/44139|
|delays_zurich_transport|5465575.0|9.0|https://www.openml.org/d/40753|https://www.openml.org/d/45034|
|diamonds|53940.0|6.0|https://www.openml.org/d/42225|https://www.openml.org/d/44140|
|Brazilian_houses|10692.0|8.0|https://www.openml.org/d/42688|https://www.openml.org/d/44141|
|Bike_Sharing_Demand|17379.0|6.0|https://www.openml.org/d/42712|https://www.openml.org/d/44142|
|nyc-taxi-green-dec-2016|581835.0|9.0|https://www.openml.org/d/42729|https://www.openml.org/d/44143|
|house_sales|21613.0|15.0|https://www.openml.org/d/42731|https://www.openml.org/d/44144|
|sulfur|10081.0|6.0|https://www.openml.org/d/23515|https://www.openml.org/d/44145|
|medical_charges|163065.0|5.0|https://www.openml.org/d/42720|https://www.openml.org/d/44146|
|MiamiHousing2016|13932.0|14.0|https://www.openml.org/d/43093|https://www.openml.org/d/44147|
|superconduct|21263.0|79.0|https://www.openml.org/d/43174|https://www.openml.org/d/44148|


**Categorical Regression**
|dataset_name|n_samples|n_features|original_link|new_link|
|---|---|---|---|---|
|topo_2_1|8885.0|255.0|https://www.openml.org/d/422|https://www.openml.org/d/45041|
|analcatdata_supreme|4052.0|7.0|https://www.openml.org/d/504|https://www.openml.org/d/44055|
|visualizing_soil|8641.0|4.0|https://www.openml.org/d/688|https://www.openml.org/d/44056|
|delays_zurich_transport|5465575.0|12.0|https://www.openml.org/d/40753|https://www.openml.org/d/45045|
|diamonds|53940.0|9.0|https://www.openml.org/d/42225|https://www.openml.org/d/44059|
|Allstate_Claims_Severity|188318.0|124.0|https://www.openml.org/d/42571|https://www.openml.org/d/45046|
|Mercedes_Benz_Greener_Manufacturing|4209.0|359.0|https://www.openml.org/d/42570|https://www.openml.org/d/44061|
|Brazilian_houses|10692.0|11.0|https://www.openml.org/d/42688|https://www.openml.org/d/44062|
|Bike_Sharing_Demand|17379.0|11.0|https://www.openml.org/d/42712|https://www.openml.org/d/44063|
|Airlines_DepDelay_1M|1000000.0|5.0|https://www.openml.org/d/42721|https://www.openml.org/d/45047|
|nyc-taxi-green-dec-2016|581835.0|16.0|https://www.openml.org/d/42729|https://www.openml.org/d/44065|
|abalone|4177.0|8.0|https://www.openml.org/d/42726|https://www.openml.org/d/45042|
|house_sales|21613.0|17.0|https://www.openml.org/d/42731|https://www.openml.org/d/44066|
|seattlecrime6|52031.0|4.0|https://www.openml.org/d/42496|https://www.openml.org/d/45043|
|medical_charges|163065.0|5.0|https://www.openml.org/d/42720|https://www.openml.org/d/45048|
|particulate-matter-ukair-2017|394299.0|6.0|https://www.openml.org/d/42207|https://www.openml.org/d/44068|
|SGEMM_GPU_kernel_performance|241600.0|9.0|https://www.openml.org/d/43144|https://www.openml.org/d/44069|


### Dataset Curators

Léo Grinsztajn, Edouard Oyallon, Gaël Varoquaux.

### Licensing Information

[More Information Needed]

### Citation Information

Léo Grinsztajn, Edouard Oyallon, Gaël Varoquaux. Why do tree-based models still outperform deep
learning on typical tabular data?. NeurIPS 2022 Datasets and Benchmarks Track, Nov 2022, New
Orleans, United States. ffhal-03723551v2f
