---
task_categories:
- translation

---
# AutoTrain Dataset for project: auto_train

## Dataset Description

This dataset has been automatically processed by AutoTrain for project auto_train.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "source": "\u79fb\u5c45\u9999\u6e2f\u5f8c\uff0c\u60a8\u53ef\u4ee5\u524d\u5f80\u6211\u5011\u7684\u5176\u4e2d\u4e00\u5bb6\u5206\u884c\u7533\u8acb\u4fe1\u7528\u5361\u2014\u2014\u5728\u9019\u88e1\u627e\u5230\u60a8\u6700\u65b9\u4fbf\u7684\u5730\u9ede\u3002",
    "target": "After you move to Hong Kong you can apply for a Credit Card by visiting one of our branches \u2013 find your most convenient location here."
  },
  {
    "source": "\u79fb\u5c45\u9999\u6e2f\u5f8c\uff0c\u60a8\u53ef\u4ee5\u524d\u5f80\u6211\u5011\u7684\u5176\u4e2d\u4e00\u5bb6\u5206\u884c\u7533\u8acb\u5132\u84c4/\u652f\u7968\u8cec\u6236\u2014\u2014\u5728\u9019\u88e1\u627e\u5230\u60a8\u6700\u65b9\u4fbf\u7684\u5730\u9ede\u3002\u5982\u679c\u60a8\u9858\u610f\uff0c\u6211\u5011\u53ef\u4ee5\u5728\u60a8\u62b5\u9054\u5f8c\u70ba\u60a8\u5b89\u6392\u5728\u60a8\u9078\u64c7\u7684\u5206\u884c\u7684\u9810\u7d04\u8a0e\u8ad6\u60a8\u7684\u9280\u884c\u548c\u8ca1\u5bcc\u7ba1\u7406\u9700\u6c42\u3002\u8981\u5b89\u6392\u7d04\u6703\uff0c\u8acb\u806f\u7e6b\u60a8\u7576\u5730\u7684\u82b1\u65d7\u9280\u884c\u4ee3\u8868\u3002",
    "target": "After you move to Hong Kong you can apply for a Savings / Checking Account by visiting one of our branches \u2013 find your most convenient location here.If you wish so, we can schedule an appointment for you in a Branch of your choice upon your arrival to discuss your banking and wealth management needs. To schedule an appointment, contact your local Citibank representative."
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "source": "Value(dtype='string', id=None)",
  "target": "Value(dtype='string', id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 332 |
| valid        | 83 |
