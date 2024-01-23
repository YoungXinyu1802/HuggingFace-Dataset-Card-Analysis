---
pretty_name: '`natural-questions`'
viewer: false
source_datasets: []
task_categories:
- text-retrieval
---

# Dataset Card for `natural-questions`

The `natural-questions` dataset, provided by the [ir-datasets](https://ir-datasets.com/) package.
For more information about the dataset, see the [documentation](https://ir-datasets.com/natural-questions#natural-questions).

# Data

This dataset provides:
 - `docs` (documents, i.e., the corpus); count=28,390,850


## Usage

```python
from datasets import load_dataset

docs = load_dataset('irds/natural-questions', 'docs')
for record in docs:
    record # {'doc_id': ..., 'text': ..., 'html': ..., 'start_byte': ..., 'end_byte': ..., 'start_token': ..., 'end_token': ..., 'document_title': ..., 'document_url': ..., 'parent_doc_id': ...}

```

Note that calling `load_dataset` will download the dataset (or provide access instructions when it's not public) and make a copy of the
data in 🤗 Dataset format.

## Citation Information

```
@article{Kwiatkowski2019Nq,
  title = {Natural Questions: a Benchmark for Question Answering Research},
  author = {Tom Kwiatkowski and Jennimaria Palomaki and Olivia Redfield and Michael Collins and Ankur Parikh and Chris Alberti and Danielle Epstein and Illia Polosukhin and Matthew Kelcey and Jacob Devlin and Kenton Lee and Kristina N. Toutanova and Llion Jones and Ming-Wei Chang and Andrew Dai and Jakob Uszkoreit and Quoc Le and Slav Petrov},
  year = {2019},
  journal = {TACL}
}
```
