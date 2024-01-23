---
annotations_creators: []
language: []
language_creators: []
license: []
multilinguality: []
pretty_name: compas-recividivsm
size_categories:
- 1K<n<10K
source_datasets: []
tags:
- interpretability
- fairness
task_categories:
- tabular-classification
task_ids: []
---

Port of the compas-recidivism dataset from propublica (github [here](https://github.com/propublica/compas-analysis)). See details there and use carefully, as there are serious known social impacts and biases present in this dataset.

Basic preprocessing done by the [imodels team](https://github.com/csinva/imodels) in [this notebook](https://github.com/csinva/imodels-data/blob/master/notebooks_fetch_data/00_get_datasets_custom.ipynb). 

The target is the binary outcome `is_recid`.

### Sample usage

Load the data:

```
from datasets import load_dataset

dataset = load_dataset("imodels/compas-recidivism")
df = pd.DataFrame(dataset['train'])
X = df.drop(columns=['is_recid'])
y = df['is_recid'].values
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
X_test = df.drop(columns=['is_recid'])
y_test = df['is_recid'].values
print('accuracy', np.mean(m.predict(X_test) == y_test))
```