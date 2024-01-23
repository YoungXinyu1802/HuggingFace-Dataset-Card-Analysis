---
task_categories:
- summarization

---
# AutoTrain Dataset for project: fine_tune_table_tm2

## Dataset Description

This dataset has been automatically processed by AutoTrain for project fine_tune_table_tm2.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "text": "List all PO headers with a valid vendor record in database",
    "target": "select * from RETAILBUYER_POHEADER P inner join RETAILBUYER_VENDOR V\non P.VENDOR_ID = V.VENDOR_ID"
  },
  {
    "text": "List all details of PO headers which have a vendor in vendor table",
    "target": "select * from RETAILBUYER_POHEADER P inner join RETAILBUYER_VENDOR V\non P.VENDOR_ID = V.VENDOR_ID"
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
| train        | 32 |
| valid        | 17 |
