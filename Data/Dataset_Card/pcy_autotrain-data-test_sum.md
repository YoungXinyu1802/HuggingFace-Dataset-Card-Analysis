---
language:
- zh
task_categories:
- conditional-text-generation
---
# AutoTrain Dataset for project: test_sum

## Dataset Descritpion

This dataset has been automatically processed by AutoTrain for project test_sum.

### Languages

The BCP-47 code for the dataset's language is zh.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "text": "7\u67086\u65e5\uff0c\u4e2d\u963f\u5408\u4f5c\u8bba\u575b\u7b2c\u4e5d\u5c4a\u90e8\u957f\u7ea7\u4f1a\u8bae\u56e0\u65b0\u51a0\u80ba\u708e\u75ab\u60c5\u4ee5\u89c6\u9891\u8fde\u7ebf\u65b9\u5f0f\u4e3e\u884c\u3002\n\u672c\u5c4a\u4f1a\u8bae\u53d6\u5f97\u4e86\u5706\u6ee1\u6210\u529f\uff0c\u53d1\u8868\u4e09\u4efd\u6210\u679c\u6587\u4ef6\uff0c\u9ad8\u5ea6\u51dd\u805a\u4e2d\u963f\u5171\u8bc6\u3002\u300a\u4e2d\u56fd\u548c\u963f\u62c9\u4f2f\u56fd\u5bb6\u56e2\u7ed3\u6297\u51fb\u65b0\u51a0\u80ba\u708e\u75ab\u60c5\u8054\u5408\u58f0\u660e\u300b\u5c55\u73b0\u4e86\u4e2d\u963f\u6218\u80dc\u75ab\u60c5[...]",
    "target": "\u671b\u6d77\u697c\u52a0\u5f3a\u5408\u4f5c\u5171\u514b\u65f6\u8270\u643a\u624b\u524d\u884c"
  },
  {
    "text": "\u4e60\u8fd1\u5e73\u603b\u4e66\u8bb0\u6307\u51fa\uff1a\u201c\u6293\u4f4f\u4e86\u521b\u65b0\uff0c\u5c31\u6293\u4f4f\u4e86\u7275\u52a8\u7ecf\u6d4e\u793e\u4f1a\u53d1\u5c55\u5168\u5c40\u7684\u2018\u725b\u9f3b\u5b50\u2019\u3002\u201d\u201c\u8c01\u5728\u521b\u65b0\u4e0a\u5148\u884c\u4e00\u6b65\uff0c\u8c01\u5c31\u80fd\u62e5\u6709\u5f15\u9886\u53d1\u5c55\u7684\u4e3b\u52a8\u6743\u3002\u201d\n\u6293\u521b\u65b0\u5c31\u662f\u6293\u53d1\u5c55\uff0c\u8c0b\u521b\u65b0\u5c31\u662f\u8c0b\u672a\u6765\u3002\u5317\u4eac\u9ad8\u6807\u51c6\u63a8\u8fdb\u201c\u4e24\u533a\u201d\u5efa\u8bbe\uff0c\u6838\u5fc3\u4efb[...]",
    "target": "\u6293\u521b\u65b0\u5c31\u662f\u6293\u53d1\u5c55"
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "text": "Value(dtype='string', id=None)",
  "target": "Value(dtype='string', id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 1343 |
| valid        | 336 |
