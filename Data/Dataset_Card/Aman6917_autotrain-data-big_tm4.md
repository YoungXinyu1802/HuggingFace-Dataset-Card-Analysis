---
task_categories:
- summarization

---
# AutoTrain Dataset for project: big_tm4

## Dataset Description

This dataset has been automatically processed by AutoTrain for project big_tm4.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "text": "I would like to request the count of vendors that are situated in Houston and have received a purchase order.",
    "target": "select max(RETAILBUYER_VENDOR.vendor_id) from RETAILBUYER_POHEADER\ninner join\nRETAILBUYER_VENDOR \non\nRETAILBUYER_POHEADER.vendor_id = RETAILBUYER_VENDOR.vendor_id\nwhere RETAILBUYER_VENDOR.Vendor_City  = 'Houston'"
  },
  {
    "text": "List all vendors and their details for whom no PO has been issued",
    "target": "select * from RETAILBUYER_VENDOR\nwhere vendor_id not in (select vendor_id from RETAILBUYER_POHEADER)"
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
| train        | 356 |
| valid        | 90 |
