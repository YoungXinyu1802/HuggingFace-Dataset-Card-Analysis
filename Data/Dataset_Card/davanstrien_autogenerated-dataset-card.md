---
dataset_info:
  features:
  - name: file
    dtype: string
  - name: image
    dtype: image
  - name: label
    dtype:
      class_label:
        names:
          '0': text-only
          '1': illustrations
  - name: pub_date
    dtype: timestamp[ns]
  - name: page_seq_num
    dtype: int64
  - name: edition_seq_num
    dtype: int64
  - name: batch
    dtype: string
  - name: lccn
    dtype: string
  - name: box
    sequence: float32
  - name: score
    dtype: float64
  - name: ocr
    dtype: string
  - name: place_of_publication
    dtype: string
  - name: geographic_coverage
    dtype: string
  - name: name
    dtype: string
  - name: publisher
    dtype: string
  - name: url
    dtype: string
  - name: page_url
    dtype: string
  splits:
  - name: train
    num_bytes: 48233952
    num_examples: 549
  download_size: 48027719
  dataset_size: 48233952
size_categories:
- n<1K
---
# Dataset Card for "test_dataset_cogapp"

[More Information needed](https://github.com/huggingface/datasets/blob/main/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)


The first row of the dataset looks like 

<!-- [[[cog
from datasets import load_dataset
import json
ds = load_dataset("davanstrien/test_dataset_cogapp")
data = ds['train'][0]
example = json.dumps({k: str(v) for k,v in data.items()}, indent=2) 
cog.out(
    "```\n{}\n```".format(example))
)]]] -->
```
{
  "file": "pst_fenske_ver02_data_sn84026497_00280776129_1880042101_0834_002_6_96.jpg",
  "image": "<PIL.JpegImagePlugin.JpegImageFile image mode=L size=388x395 at 0x11AF00990>",
  "label": "0",
  "pub_date": "1880-04-21 00:00:00",
  "page_seq_num": "834",
  "edition_seq_num": "1",
  "batch": "pst_fenske_ver02",
  "lccn": "sn84026497",
  "box": "[0.649412214756012, 0.6045778393745422, 0.8002520799636841, 0.7152365446090698]",
  "score": "0.9609346985816956",
  "ocr": "H. II. IIASLKT & SOXN, Dealers in General Merchandise In New Store Room nt HASLET'S COS ITERS, 'JTionoMtii, ln. .Tau'y 1st, 1?0.",
  "place_of_publication": "Tionesta, Pa.",
  "geographic_coverage": "['Pennsylvania--Forest--Tionesta']",
  "name": "The Forest Republican. [volume]",
  "publisher": "Ed. W. Smiley",
  "url": "https://news-navigator.labs.loc.gov/data/pst_fenske_ver02/data/sn84026497/00280776129/1880042101/0834/002_6_96.jpg",
  "page_url": "https://chroniclingamerica.loc.gov/data/batches/pst_fenske_ver02/data/sn84026497/00280776129/1880042101/0834.jp2"
}
```
<!-- [[[end]]] -->


<!-- [[[cog
from auto_dataset_card.core import generate_label_breakdown_tables, get_label_counts
ds = load_dataset("davanstrien/test_dataset_cogapp")
data = get_label_counts(ds)
cog.out(
f"""
# Label breakdowns \n
```
{data}
```
""")
]]] -->

# Label breakdowns 

```
{'train': {'text-only': 376, 'illustrations': 173}}
```
<!-- [[[end]]] -->


<!-- [[[cog
from auto_dataset_card.core import generate_label_breakdown_tables, get_label_counts
ds = load_dataset("davanstrien/test_dataset_cogapp")
data = get_label_counts(ds)
tables = generate_label_breakdown_tables(data)
split = tables[0][0]
table = tables[0][1]
cog.out(
f"""
# Label breakdown table for split: {split} \n
{table}
""")
]]] -->

# Label breakdown table for split: train 

| Label         |   Count | Percentage   |
|---------------|---------|--------------|
| text-only     |     376 | 68.49%       |
| illustrations |     173 | 31.51%       |
<!-- [[[end]]] -->