---
annotations_creators: []
language: []
language_creators: []
license: []
multilinguality: []
pretty_name: diabetes-readmission
size_categories:
- 100K<n<1M
source_datasets: []
tags:
- interpretability
- fairness
- medicine
task_categories:
- tabular-classification
task_ids: []
---

Port of the diabetes-readmission dataset from UCI (link [here](https://archive.ics.uci.edu/ml/datasets/diabetes+130-us+hospitals+for+years+1999-2008)). See details there and use carefully.

Basic preprocessing done by the [imodels team](https://github.com/csinva/imodels) in [this notebook](https://github.com/csinva/imodels-data/blob/master/notebooks_fetch_data/00_get_datasets_custom.ipynb).

The target is the binary outcome `readmitted`.

### Sample usage

Load the data:

```
from datasets import load_dataset

dataset = load_dataset("imodels/diabetes-readmission")
df = pd.DataFrame(dataset['train'])
X = df.drop(columns=['readmitted'])
y = df['readmitted'].values
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
X_test = df.drop(columns=['readmitted'])
y_test = df['readmitted'].values
print('accuracy', np.mean(m.predict(X_test) == y_test))
```