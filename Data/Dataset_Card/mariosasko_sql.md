---
license: apache-2.0
viewer: false
---


### Usage

```python
from datasets import load_dataset

# Load everything into "train" set

## Using a query
dset = load_dataset("mariosasko/sql", sql="SELECT * FROM my_dataset LIMIT 10", con="sqlite:///my_db.db")

## Referencing a table
dset = load_dataset("mariosasko/sql", sql="data_table", con="postgres:///db_name")

# Load multiple splits
dset = load_dataset(
    "mariosasko/sql",
    sql={
        "train": "SELECT * FROM my_dataset LIMIT 10",
        "test": "SELECT * FROM my_dataset LIMIT 10 OFFSET 10",
    },
    con="sqlite:///my_db.db"
)
```

`sql` and `con` can only be specified as strings to work with `datasets`' caching mechanism. `pd.read_sql` is used internally for query processing, so refer to its [doc](https://pandas.pydata.org/docs/reference/api/pandas.read_sql.html) for the complete list of supported parameters.