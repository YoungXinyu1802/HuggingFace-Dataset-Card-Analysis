---
annotations_creators:
- no-annotation
language_creators:
- found
language:
- es
license:
- odc-by
size_categories:
- n<1K
- 1K<n<10K
- 10K<n<100K
- 100K<n<1M
- 1M<n<10M
- 10M<n<100M
- 100M<n<1B
source_datasets:
- mc4
- bertin-project/mc4-sampling
task_categories:
- text-generation
- fill-mask
task_ids:
- language-modeling
pretty_name: mC4-es-sampled
---

# Dataset Card for mC4-es-sampled

## Table of Contents

- [Dataset Card for mC4-es-sampled](#dataset-card-for-mc4-es-sampled)
  - [Table of Contents](#table-of-contents)
  - [Dataset Description](#dataset-description)
    - [Dataset Summary](#dataset-summary)
    - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
    - [Languages](#languages)
  - [Dataset Structure](#dataset-structure)
    - [Data Instances](#data-instances)
    - [Data Fields](#data-fields)
    - [Data Splits](#data-splits)
  - [Dataset Creation](#dataset-creation)
    - [Curation Rationale](#curation-rationale)
  - [Additional Information](#additional-information)
    - [Dataset Curators](#dataset-curators)
    - [Licensing Information](#licensing-information)
    - [Citation Information](#citation-information)
    - [Contributions](#contributions)

## Dataset Description

- **Homepage:** https://huggingface.co/datasets/allenai/c4
- **Paper:** https://arxiv.org/abs/1910.10683

### Dataset Summary

This dataset is the result of applying perplexity sampling to the Spanish portion of mC4 using [`mc4-sampling`](https://huggingface.co/datasets/bertin-project/mc4-sampling/). Please, refer to [BERTIN Project](https://huggingface.co/bertin-project/bertin-roberta-base-spanish).

You can load the mC4 Spanish sampled like this:

```python
from datasets import load_dataset

for config in ("random", "stepwise", "gaussian"):
    mc4es = load_dataset(
        "bertin-project/mc4-es-sampled",
        config,
        split="train",
        streaming=True
    ).shuffle(buffer_size=1000)
    for sample in mc4es:
        print(config, sample)
        break       
```
Alternatively, you can bypass the `datasets` library and quickly download (\~1.5hrs, depending on connection) a specific config in the same order used to pre-train BERTIN models in a massive (\~200GB) JSON-lines files:

```python
import io
import gzip
import json
import sys

import requests
from tqdm import tqdm

_DATA_URL_TRAIN = "https://huggingface.co/datasets/bertin-project/mc4-es-sampled/resolve/main/mc4-es-train-50M-{config}-shard-{index:04d}-of-{n_shards:04d}.json.gz"


def main(config="stepwise"):
    data_urls = [
        _DATA_URL_TRAIN.format(
            config=config,
            index=index + 1,
            n_shards=1024,
        )
        for index in range(1024)
    ]
    with open(f"mc4-es-train-50M-{config}.jsonl", "w") as f:
        for dara_url in tqdm(data_urls):
            response = requests.get(dara_url)
            bio = io.BytesIO(response.content)
            with gzip.open(bio, "rt", encoding="utf8") as g:
                for line in g:
                    json_line = json.loads(line.strip())
                    f.write(json.dumps(json_line) + "\
")


if __name__ == "__main__":
    main(sys.argv[1])
```

### Supported Tasks and Leaderboards

mC4-es-sampled is mainly intended for reproducibility purposes of the BERTIN Project and to pretrain language models and word representations on medium budgets.

### Languages

The dataset only supports the Spanish language.

## Dataset Structure

### Data Instances

An example form the `Gaussian` config:

```python
{'timestamp': '2018-10-20T06:20:53Z', 'text': 'Ortho HyaluroTop 200 aporta el colágeno y ácido hialurónico que, con la edad, se producen en menor cantidad. La vitamina C promueve la producción de colágeno para mantener la piel sana y protege a las células contra los radicales libres causados ??por la contaminación ambiental y los rayos UV.', 'url': 'https://www.farmaciagaleno.com/orthonat-hyalurotop-200-30-capsulas'}
```

### Data Fields

The data have several fields:

- `url`: url of the source as a string
- `text`: text content as a string
- `timestamp`: timestamp as a string

### Data Splits

The resulting mC4 subsets for Spanish are reported in this table:

| config   | train   |
|:---------|:--------|
| stepwise | 50M     |
| random   | 50M     |
| gaussian | 50M     |

The split `validation` is exactly the same as the original `mc4` dataset.

## Dataset Creation

### Curation Rationale

This dataset was built from the original [`mc4`](https://huggingface.co/datasets/mc4) by applying perplexity-sampling via [`mc4-sampling`](https://huggingface.co/datasets/bertin-project/mc4-sampling) for Spanish.

## Additional Information

### Dataset Curators

Original data by [Common Crawl](https://commoncrawl.org/).

### Licensing Information

AllenAI are releasing this dataset under the terms of ODC-BY. By using this, you are also bound by the Common Crawl terms of use in respect of the content contained in the dataset.

### Citation Information

To cite this dataset:
```bibtex
@article{BERTIN,
	author = {Javier De la Rosa y Eduardo G. Ponferrada y Manu Romero y Paulo Villegas y Pablo González de Prado Salas y María Grandury},
	title = {{BERTIN}: Efficient Pre-Training of a Spanish Language Model using Perplexity Sampling},
	journal = {Procesamiento del Lenguaje Natural},
	volume = {68},
	number = {0},
	year = {2022},
	keywords = {},
	abstract = {The pre-training of large language models usually requires massive amounts of resources, both in terms of computation and data. Frequently used web sources such as Common Crawl might contain enough noise to make this pretraining sub-optimal. In this work, we experiment with different sampling methods from the Spanish version of mC4, and present a novel data-centric technique which we name perplexity sampling that enables the pre-training of language models in roughly half the amount of steps and using one fifth of the data. The resulting models are comparable to the current state-of-the-art, and even achieve better results for certain tasks. Our work is proof of the versatility of Transformers, and paves the way for small teams to train their models on a limited budget.},
	issn = {1989-7553},
	url = {http://journal.sepln.org/sepln/ojs/ojs/index.php/pln/article/view/6403},
	pages = {13--23}
}
```

If you use this dataset, we would love to hear about it! Reach out on twitter, GitHub, Discord, or shoot us an email.

To cite the original `mc4` dataset:
```
@article{2019t5,
    author = {Colin Raffel and Noam Shazeer and Adam Roberts and Katherine Lee and Sharan Narang and Michael Matena and Yanqi Zhou and Wei Li and Peter J. Liu},
    title = {Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer},
    journal = {arXiv e-prints},
    year = {2019},
    archivePrefix = {arXiv},
    eprint = {1910.10683},
}
```

### Contributions

Dataset contributed by [@versae](https://github.com/versae) for BERTIN Project.

Thanks to [@dirkgr](https://github.com/dirkgr) and [@lhoestq](https://github.com/lhoestq) for adding the original mC4 dataset.
