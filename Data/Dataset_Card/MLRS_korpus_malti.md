---
pretty_name: Korpus Malti
language:
- mt
multilinguality:
- monolingual
size_categories:
- 10M<n<100M
annotations_creators:
- no-annotation
language_creators:
- found
source_datasets:
- original
task_categories:
- text-generation
- fill-mask
task_ids:
- language-modeling
- masked-language-modeling
license:
- cc-by-nc-sa-4.0
---
# Korpus Malti 🇲🇹

General Corpora for the Maltese Language.

This dataset is composed of texts from various genres/domains written in Maltese.


## Configurations

### Shuffled data

The default configuration (`"shuffled"`) yields the the entire corpus from all genres:
```python
import datasets

dataset = datasets.load_dataset("MLRS/korpus_malti")
```

All sentences are combined together and shuffled, without preserving the sentence order.
No other annotations are present, so an instance would be of the following form:
```json
{
  "text": "Din hija sentenza."
}
```

The training/validation/testing split is what was used to train the [BERTu](https://huggingface.co/MLRS/BERTu) model.

### Domain-split data

All other configurations contain a subset of the data.
For instance, this loads the Wikipedia portion:
```python
import datasets

dataset = datasets.load_dataset("MLRS/korpus_malti", "wiki")
```

For these configurations the data is not shuffled, so the sentence order on a document level is preserved.
An instance from these configurations would take the following form:
```json
{
  "text": ["Din hija sentenza.", "U hawn oħra!"],
}
```

The raw data files contain additional metadata.
Its structure differs from one instance to another, depending on what's available from the source.
This information was typically scraped from the source itself & minimal processing is performed on such data.


## Additional Information

### Dataset Curators

The dataset was created by [Albert Gatt](https://albertgatt.github.io), [Kurt Micallef](https://www.um.edu.mt/profile/kurtmicallef), [Marc Tanti](https://www.um.edu.mt/profile/marctanti), [Lonneke van der Plas](https://sites.google.com/site/lonnekenlp/) and [Claudia Borg](https://www.um.edu.mt/profile/claudiaborg).

### Licensing Information

This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].
Permissions beyond the scope of this license may be available at [https://mlrs.research.um.edu.mt/](https://mlrs.research.um.edu.mt/).

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png

### Citation Information

This work was first presented in [Pre-training Data Quality and Quantity for a Low-Resource Language: New Corpus and BERT Models for Maltese](https://aclanthology.org/2022.deeplo-1.10/).
Cite it as follows: 

```bibtex
@inproceedings{BERTu,
    title = "Pre-training Data Quality and Quantity for a Low-Resource Language: New Corpus and {BERT} Models for {M}altese",
    author = "Micallef, Kurt  and
              Gatt, Albert  and
              Tanti, Marc  and
              van der Plas, Lonneke  and
              Borg, Claudia",
    booktitle = "Proceedings of the Third Workshop on Deep Learning for Low-Resource Natural Language Processing",
    month = jul,
    year = "2022",
    address = "Hybrid",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.deeplo-1.10",
    doi = "10.18653/v1/2022.deeplo-1.10",
    pages = "90--101",
}
```
