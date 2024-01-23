---
task_categories:
- summarization

---
# AutoTrain Dataset for project: exact_data

## Dataset Description

This dataset has been automatically processed by AutoTrain for project exact_data.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "text": "What is the maximum vendor id of vendor present in vendor table who has been issued a PO in 2021",
    "target": "select max(t1.vendor_id) from RETAILBUYER_POHEADER as t2 inner join RETAILBUYER_VENDOR as t1 on t2.vendor_id = t1.vendor_id where YEAR(t2.po_issuedt) = 2021"
  },
  {
    "text": "What are the product ids, descriptions and sum of quantities ordered for the products in purchase order line items",
    "target": "select L.product_id, t2.product_desc, sum(t1.quantity) from RETAILBUYER_PRODUCT_SOURCE as t2 INNER JOIN RETAILBUYER_POLINEITEM as t1 ON t2.PRODUCT_ID = t1.PRODUCT_ID GROUP BY t1.PRODUCT_ID, t2.product_desc"
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
| train        | 25 |
| valid        | 7 |
