---
license: apache-2.0
---

# Wadhwani AI Pest Management Open Data

This dataset is a Hugging Face adaptor to the official dataset [hosted
on
Github](https://github.com/WadhwaniAI/pest-management-opendata). Please
refer to that repository for detailed and up-to-date documentation.

## Usage

This dataset is large. It is strongly recommended users access it as a
stream:

```python
from datasets import load_dataset
dataset = load_dataset('jerome-ai/pest-management-opendata', streaming=True)
```

Bounding boxes are stored as geospatial types. Once loaded, they can be
read as follows:

```python
from shapely.wkb import loads

for (s, data) in dataset.items():
    for d in data:
        pests = d['pests']
        iterable = map(pests.get, ('label', 'geometry'))
        for (i, j) in zip(*iterable):
            geom = loads(j)
            print(i, geom.bounds)
```

The bounds of a geometry are what most object detection systems
require. See the [Shapely
documentation](https://shapely.readthedocs.io/en/stable/manual.html#object.bounds)
for more.
