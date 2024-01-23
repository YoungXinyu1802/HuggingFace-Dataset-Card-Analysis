---
language:
- en
task_categories:
- text-classification

---
# AutoTrain Dataset for project: benign-urls

## Dataset Description

This dataset has been automatically processed by AutoTrain for project benign-urls.

### Languages

The BCP-47 code for the dataset's language is en.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "text": "surveycustomergroup.com",
    "target": 1
  },
  {
    "text": "ssl.dwebsite.com/secure2/ce_isd742/php/public.php?action=listClasses&categoryId=9&programId=5&from=listCategories",
    "target": 1
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "text": "Value(dtype='string', id=None)",
  "target": "ClassLabel(names=['0', '1'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 832 |
| valid        | 209 |
