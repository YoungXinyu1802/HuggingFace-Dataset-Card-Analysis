# This is an helper script to load an html enterprise dataset into a datasets object

## How to use

1. Download a NS0 dump at https://dumps.wikimedia.org/other/enterprise_html/runs/20230220/

2. Untar it 

For example with:
```
mkdir enwiki-NS6-20230220-ENTERPRISE-HTML
tar -I pigz -vxf enwiki-NS6-20230220-ENTERPRISE-HTML.json.tar.gz -C enwiki-NS6-20230220-ENTERPRISE-HTML
```

3. Load it:
```python
from datasets import load_dataset

local_path=... # Path to directory where you extracted the NS0 dump
shard_id=...

ds = load_dataset(
    "SaulLu/wikipedia_html_enterprise", 
    shard=shard_id, 
    data_dir=local_path
)
```