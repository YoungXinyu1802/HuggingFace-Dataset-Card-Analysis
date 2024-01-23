---
annotations_creators: []
language: []
language_creators: []
license: []
multilinguality: []
pretty_name: credit-card
size_categories:
- 10K<n<100K
source_datasets: []
tags:
- interpretability
- fairness
- medicine
task_categories:
- tabular-classification
task_ids: []
---

Port of the credit-card dataset from UCI (link [here](https://www.kaggle.com/datasets/uciml/default-of-credit-card-clients-dataset)). See details there and use carefully.

Basic preprocessing done by the [imodels team](https://github.com/csinva/imodels) in [this notebook](https://github.com/csinva/imodels-data/blob/master/notebooks_fetch_data/00_get_datasets_custom.ipynb).

The target is the binary outcome `default.payment.next.month`.

### Sample usage

Load the data:

```
from datasets import load_dataset

dataset = load_dataset("imodels/credit-card")
df = pd.DataFrame(dataset['train'])
X = df.drop(columns=['default.payment.next.month'])
y = df['default.payment.next.month'].values
```

Fit a model:

```
import imodels
import numpy as np

m = imodels.FIGSClassifier(max_rules=5)
m.fit(X, y)
print(m)
```


Evaluate:


```
df_test = pd.DataFrame(dataset['test'])
X_test = df.drop(columns=['default.payment.next.month'])
y_test = df['default.payment.next.month'].values
print('accuracy', np.mean(m.predict(X_test) == y_test))
```