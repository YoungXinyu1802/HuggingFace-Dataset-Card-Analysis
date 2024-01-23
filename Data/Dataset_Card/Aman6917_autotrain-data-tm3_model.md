---
task_categories:
- summarization

---
# AutoTrain Dataset for project: tm3_model

## Dataset Description

This dataset has been automatically processed by AutoTrain for project tm3_model.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "text": "List all PO headers with a valid vendor record in database",
    "target": "select * from RETAILBUYER_POHEADER as t2 inner join RETAILBUYER_VENDOR as t1 on t2.VENDOR_ID = t1.VENDOR_ID"
  },
  {
    "text": "List all details of PO headers which have a vendor in vendor table",
    "target": "select * from RETAILBUYER_POHEADER as t2 inner join RETAILBUYER_VENDOR as t1 on t2.VENDOR_ID = t1.VENDOR_ID"
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
| train        | 49 |
| valid        | 17 |
