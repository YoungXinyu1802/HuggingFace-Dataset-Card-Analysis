---
annotations_creators:
- no-annotation
language_creators:
- found
language:
- af
- am
- ar
- az
- be
- bg
- bn
- ca
- ceb
- co
- cs
- cy
- da
- de
- el
- en
- eo
- es
- et
- eu
- fa
- fi
- fil
- fr
- fy
- ga
- gd
- gl
- gu
- ha
- haw
- hi
- hmn
- ht
- hu
- hy
- id
- ig
- is
- it
- iw
- ja
- jv
- ka
- kk
- km
- kn
- ko
- ku
- ky
- la
- lb
- lo
- lt
- lv
- mg
- mi
- mk
- ml
- mn
- mr
- ms
- mt
- my
- ne
- nl
- 'no'
- ny
- pa
- pl
- ps
- pt
- ro
- ru
- sd
- si
- sk
- sl
- sm
- sn
- so
- sq
- sr
- st
- su
- sv
- sw
- ta
- te
- tg
- th
- tr
- uk
- und
- ur
- uz
- vi
- xh
- yi
- yo
- zh
- zu
license:
- odc-by
multilinguality:
- multilingual
size_categories:
- n<1K
- 1K<n<10K
- 10K<n<100K
- 100K<n<1M
- 1M<n<10M
- 10M<n<100M
- 100M<n<1B
- 1B<n<10B
source_datasets:
- original
task_categories:
- text-generation
- fill-mask
task_ids:
- language-modeling
paperswithcode_id: mc4
pretty_name: mC4-sampling
language_bcp47:
- bg-Latn
- el-Latn
- hi-Latn
- ja-Latn
- ru-Latn
- zh-Latn
---

# Dataset Card for mC4-sampling

## Table of Contents

- [Dataset Card for mC4-sampling](#dataset-card-for-mc4-sampling)
  - [Table of Contents](#table-of-contents)
  - [Dataset Description](#dataset-description)
    - [Dataset Summary](#dataset-summary)
    - [Dataset Sampling](#dataset-sampling)
    - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
    - [Languages](#languages)
  - [Dataset Structure](#dataset-structure)
    - [Data Instances](#data-instances)
    - [Data Fields](#data-fields)
    - [Data Splits](#data-splits)
  - [Additional Information](#additional-information)
    - [Dataset Curators](#dataset-curators)
    - [Licensing Information](#licensing-information)
    - [Citation Information](#citation-information)
    - [Contributions](#contributions)

## Dataset Description

- **Homepage:** https://huggingface.co/bertin-project/bertin-roberta-base-spanish

### Dataset Summary

This dataset builds upon the AllenAI version of the original [mC4](https://huggingface.co/datasets/allenai/c4) and adds sampling methods to perform perplexity-based filtering on the fly. Please, refer to [BERTIN Project](https://huggingface.co/bertin-project/bertin-roberta-base-spanish).

The original dataset is mC4, the multilingual colossal, cleaned version of Common Crawl's web crawl corpus. Based on Common Crawl dataset: "https://commoncrawl.org".

108 languages are available and are reported in the [`mc4` dataset](https://huggingface.co/datasets/mc4#dataset-summary).

You can load the mC4 subset of any language like this:

```python
from datasets import load_dataset

en_mc4 = load_dataset("mc4", "en")
```

And if you can even specify a list of languages:

```python
from datasets import load_dataset

mc4_subset_with_five_languages = load_dataset("mc4", languages=["en", "fr", "es", "de", "zh"])
```

### Dataset Sampling

There are 3 main different ways of getting sampled versions of mc4 using this dataset.

#### Random

Arguably, the simplest of methods. It keeps a document based on a probability threshold we called `factor`. It defaults to `0.5` for random sampling:

```python
def _should_keep_doc_random(self, doc, factor=None, **kwargs):
    factor = 0.5 if factor is None else factor
    return self.rng.uniform() <= factor
```

The way to use this sampling method is by adding an extra parameter to the instantiation of the dataset:

```python
from datasets import load_dataset

mc4random = load_dataset(
    "bertin-project/mc4-sampling", "es",
    split="train",
    streaming=True,
    sampling_method="random",
    factor=0.5,
)
for sample in mc4random:
    print(sample)
    break
```

#### Gaussian

This sampling method tries to adjust to the underlying distribution while oversampling the central quartiles of the perplexity distribution of the documents in mC4 for a given language. Two parameters control the shape of the approximation, `factor` (peakness of the exponential function) and `width` (spread). Default values are selected for Spanish.

```python
def _should_keep_doc_gaussian(self, doc, factor=None, width=None, boundaries=None, **kwargs):
    perplexity = self.get_perplexity(doc)
    width = (9 / 2) if width is None else width
    factor = 0.78 if factor is None else factor
    median = 662247.50212365 if boundaries is None else boundaries[1]
    exponential = np.exp((-1 / width) * ((perplexity - median) / median) ** 2)
    weighted_perplexity = factor * exponential
    return self.rng.uniform() < weighted_perplexity
```

In order to use this sampling methods, information about the quartile boundaries of the underlying distribution need to be calculated beforehand and passed in to the instantiation of the dataset. Moreover, the path to a [KenLM model](https://github.com/kpu/kenlm/) (5-gram language model) or an object with a method `.score(text:str) -> float` need to also be passed in for the calculation of the perplexity value of a document. KenLM can be installed with pip:

```bash
pip install https://github.com/kpu/kenlm/archive/master.zip
```

```python
from datasets import load_dataset

mc4gaussian = load_dataset(
    "bertin-project/mc4-sampling",
    "es",
    split="train",
    streaming=True,
    sampling_method="gaussian",
    perplexity_model="./es.arpa.bin",
    boundaries=[536394.99320948, 662247.50212365, 919250.87225178],
    factor=0.78,
    width=9/2,
)
for sample in mc4gaussian:
    print(sample)
    break
```

Facebook has created and released 5-gram Kneser-Ney models for 100 languages available to download and use within the KenLM library. To download your own Kneser-Ney language model, chose a language code from the next list:

```bash
af,ar,az,be,bg,bn,ca,cs,da,de,el,en,es,et,fa,fi,fr,gu,he,hi,hr,hu,hy,id,is,it,ja,ka,kk,km,kn,ko,lt,lv,mk,ml,mn,mr,my,ne,nl,no,pl,pt,ro,ru,uk,zh
```

And run the next download command replacing `lang` with your own language code:

```bash
wget http://dl.fbaipublicfiles.com/cc_net/lm/lang.arpa.bin
```

### Stepwise

The stepwise sampling method uses a simple criteria by oversampling from the central quartiles inversely proportionally their range. Only `boundaries`, `factor` (strength of the oversampling), and `perplexity_model` are needed:

```python
def _should_keep_doc_step(self, doc, factor=None, boundaries=None, **kwargs):
    perplexity = self.get_perplexity(doc)
    factor = 1.5e5 if factor is None else factor
    if boundaries is None:
        boundaries = [536394.99320948, 662247.50212365, 919250.87225178]
    if perplexity <= boundaries[0]:
        quartile_range = boundaries[0]
    elif boundaries[0] < perplexity < boundaries[1]:
        quartile_range = boundaries[1] - boundaries[0]
    elif boundaries[1] < perplexity < boundaries[2]:
        quartile_range = boundaries[2] - boundaries[1]
    elif perplexity >= boundaries[2]:
        quartile_range = 10 * boundaries[2]
    probability = factor / quartile_range
    return self.rng.uniform() < probability
```

In order to use this sampling method, a similar invocation is needed:

```python
mc4stepwsie = load_dataset(
    "bertin-project/mc4-sampling",
    "es",
    split="train",
    streaming=True,
    sampling_method="stepwise",
    perplexity_model="./es.arpa.bin",
    boundaries=[536394.99320948, 662247.50212365, 919250.87225178],
    factor=1.5e5,
)
for sample in mc4stepwsie:
    print(sample)
    break
```

### Supported Tasks and Leaderboards

mC4-sampling is mainly intended to pretrain language models and word representations on a budget.

### Languages

The dataset supports 108 languages.

## Dataset Structure

### Data Instances

An example form the `en` config is:

```
{'timestamp': '2018-06-24T01:32:39Z',
 'text': 'Farm Resources in Plumas County\
Show Beginning Farmer Organizations & Professionals (304)\
There are 304 resources serving Plumas County in the following categories:\
Map of Beginning Farmer Organizations & Professionals serving Plumas County\
Victoria Fisher - Office Manager - Loyalton, CA\
Amy Lynn Rasband - UCCE Plumas-Sierra Administrative Assistant II - Quincy , CA\
Show Farm Income Opportunities Organizations & Professionals (353)\
There are 353 resources serving Plumas County in the following categories:\
Farm Ranch And Forest Retailers (18)\
Map of Farm Income Opportunities Organizations & Professionals serving Plumas County\
Warner Valley Wildlife Area - Plumas County\
Show Farm Resources Organizations & Professionals (297)\
There are 297 resources serving Plumas County in the following categories:\
Map of Farm Resources Organizations & Professionals serving Plumas County\
There are 57 resources serving Plumas County in the following categories:\
Map of Organic Certification Organizations & Professionals serving Plumas County',
 'url': 'http://www.californialandcan.org/Plumas/Farm-Resources/'}
```

### Data Fields

The data have several fields:

- `url`: url of the source as a string
- `text`: text content as a string
- `timestamp`: timestamp as a string

### Data Splits

The same splits as in [mC4 are available](https://huggingface.co/datasets/mc4#data-splits).

## Additional Information

### Licensing Information

BERTIN Project is releasing this dataset under the same terms AllenAI released mC4, that is, those of the ODC-BY. By using this, you are also bound by the Common Crawl terms of use in respect of the content contained in the dataset.

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

Dataset contributed by [@versae](https://github.com/versae).

Thanks to [@dirkgr](https://github.com/dirkgr) and [@lhoestq](https://github.com/lhoestq) for adding the original mC4 dataset.
