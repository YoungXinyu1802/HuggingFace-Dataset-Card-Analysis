---
language:
- en
task_categories:
- conditional-text-generation

---
# AutoTrain Dataset for project: code_summarization

## Dataset Descritpion

This dataset has been automatically processed by AutoTrain for project code_summarization.

### Languages

The BCP-47 code for the dataset's language is en.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "text": "def read(self, table, columns, keyset, index=\"\", limit=0, partition=None):\n        \"\"\"Perform a ``St[...]",
    "target": "Perform a ``StreamingRead`` API request for rows in a table.\n\n        :type table: str\n        :para[...]"
  },
  {
    "text": "def maf_somatic_variant_stats(variant, variant_metadata):\n    \"\"\"\n    Parse out the variant calling [...]",
    "target": "Parse out the variant calling statistics for a given variant from a MAF file\n\n    Assumes the MAF fo[...]"
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
| train        | 800 |
| valid        | 200 |
