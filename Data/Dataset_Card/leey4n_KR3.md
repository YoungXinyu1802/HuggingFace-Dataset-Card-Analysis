---
annotations_creators: []
language_creators: []
language:
- ko
license:
- cc-by-nc-sa-4.0
multilinguality:
- monolingual
pretty_name: KR3
size_categories:
- 100K<n<1m
source_datasets: []
task_categories:
- text-classification
task_ids:
- sentiment-classification
---

### KR3: Korean Restaurant Reviews with Ratings
Korean sentiment classification dataset   

- Size: 460K(+180K)
- Language: Korean-centric

### ⚠️ Caution with `Rating` Column
0 stands for negative review, 1 stands for positive review, and 2 stands for ambiguous review.  
**Note that rating 2 is not intended to be used directly for supervised learning(classification).** This data is included for additional pre-training purpose or other usage.  
In other words, this dataset is basically a **binary** sentiment classification task where labels are 0 and 1.  

### 🔍 See More
See all the codes for crawling/preprocessing the dataset and experiments with KR3 in [GitHub Repo](https://github.com/Wittgensteinian/kr3).  
See Kaggle dataset in [Kaggle Dataset](https://www.kaggle.com/ninetyninenewton/kr3-korean-restaurant-reviews-with-ratings).

### Usage
```python
from datasets import load_dataset

kr3 = load_dataset("Wittgensteinian/KR3", name='kr3', split='train')
kr3 = kr3.remove_columns(['__index_level_0__']) # Original file didn't include this column. Suspect it's a hugging face issue.
```
```python
# drop reviews with ambiguous label
kr3_binary = kr3.filter(lambda example: example['Rating'] != 2)
```


### License
**CC BY-NC-SA 4.0**

### Legal Issues
We concluded that the **non-commerical usage and release of KR3 fall into the range of fair use (공정 이용)** stated in the Korean copyright act (저작권법). We further clarify that we **did not agree to the terms of service** from any websites which might prohibit web crawling. In other words, web crawling we've done was proceeded without logging in to the website. Despite all of these, feel free to contact to any of the contributors if you notice any legal issues.

### Contributors & Acknowledgement
(Alphabetical order)

[Dongin Jung](https://github.com/dongin1009)

[Hyunwoo Kwak](https://github.com/Kwak-Hyun-woo)

[Kaeun Lee](https://github.com/Kaeun-Lee)

[Yejoon Lee](https://github.com/wittgensteinian)

This work was done as DIYA 4기. Compute resources needed for the work was supported by [DIYA](https://blog.diyaml.com) and surromind.ai.

