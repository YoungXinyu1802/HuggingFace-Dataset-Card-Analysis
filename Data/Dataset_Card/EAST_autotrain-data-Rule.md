---
language:
- zh
task_categories:
- text-classification
---
# AutoTrain Dataset for project: Rule

## Dataset Descritpion

This dataset has been automatically processed by AutoTrain for project Rule.

### Languages

The BCP-47 code for the dataset's language is zh.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "text": "\u672c\u516c\u53f8\u4f1a\u5728\u60a8\u767b\u5f55\u53ca\u7248\u672c\u66f4\u65b0\u65f6\u4ee5\u63a8\u9001\u901a\u77e5\u3001\u5f39\u6846\u7684\u5f62\u5f0f\u5411\u60a8\u5c55\u793a\u53d8\u66f4\u540e\u7684\u9690\u79c1\u653f\u7b56",
    "target": 1
  },
  {
    "text": "\u6211\u4eec\u53ef\u80fd\u9002\u65f6\u4f1a\u5bf9\u672c\u9690\u79c1\u6743\u653f\u7b56\u8fdb\u884c\u8c03\u6574\u6216\u53d8\u66f4\uff0c\u672c\u9690\u79c1\u6743\u653f\u7b56\u7684\u4efb\u4f55\u66f4\u65b0\u5c06\u4ee5\u6807\u6ce8\u66f4\u65b0\u65f6\u95f4\u7684\u65b9\u5f0f\u516c\u5e03\u5728\u6211\u4eec\u7f51\u7ad9\u4e0a\uff0c\u9664\u6cd5\u5f8b\u6cd5\u89c4\u6216\u76d1\u7ba1\u89c4\u5b9a\u53e6\u6709\u5f3a\u5236\u6027\u89c4\u5b9a\u5916\uff0c\u7ecf\u8c03\u6574\u6216\u53d8\u66f4\u7684\u5185\u5bb9\u4e00\u7ecf\u901a\u77e5\u6216\u516c\u5e03\u540e\u76847\u65e5\u540e\u751f\u6548",
    "target": 0
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "text": "Value(dtype='string', id=None)",
  "target": "ClassLabel(num_classes=2, names=['0', '1'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 70 |
| valid        | 19 |
