---
annotations_creators:
- found
language_creators:
- expert-generated
language:
- af
- am
- ar
- hy
- as
- ast
- az
- be
- bn
- bs
- bg
- my
- ca
- ceb
- zho
- hr
- cs
- da
- nl
- en
- et
- tl
- fi
- fr
- ff
- gl
- lg
- ka
- de
- el
- gu
- ha
- he
- hi
- hu
- is
- ig
- id
- ga
- it
- ja
- jv
- kea
- kam
- kn
- kk
- km
- ko
- ky
- lo
- lv
- ln
- lt
- luo
- lb
- mk
- ms
- ml
- mt
- mi
- mr
- mn
- ne
- ns
- 'no'
- ny
- oc
- or
- om
- ps
- fa
- pl
- pt
- pa
- ro
- ru
- sr
- sn
- sd
- sk
- sl
- so
- ku
- es
- sw
- sv
- tg
- ta
- te
- th
- tr
- uk
- umb
- ur
- uz
- vi
- cy
- wo
- xh
- yo
- zu
license:
- cc-by-sa-4.0
multilinguality:
- multilingual
- translation
size_categories:
- unknown
source_datasets:
- extended|flores
task_categories:
- text-generation
- translation
task_ids: []
paperswithcode_id: flores
pretty_name: flores101
tags:
- conditional-text-generation
---

# Dataset Card for Flores 101

## Table of Contents

- [Dataset Card for Flores 101](#dataset-card-for-flores-101)
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
  - [Additional Information](#additional-information)
    - [Dataset Curators](#dataset-curators)
    - [Licensing Information](#licensing-information)
    - [Citation Information](#citation-information)

## Dataset Description

- **Home:** [WMT](http://www.statmt.org/wmt21/large-scale-multilingual-translation-task.html)
- **Repository:** [Github](https://github.com/facebookresearch/flores)
- **Blogpost:** [FAIR](https://ai.facebook.com/blog/the-flores-101-data-set-helping-build-better-translation-systems-around-the-world)
- **Paper:** [Arxiv](https://arxiv.org/abs/2106.03193)
- **Point of Contact:** [flores@fb.com](mailto:flores@fb.com)
- **Leaderboard** [Dynabench](https://dynabench.org/flores/Flores%20MT%20Evaluation%20(FULL))

### Dataset Summary

FLORES is a benchmark dataset for machine translation between English and low-resource languages.

Abstract from the original paper:

> One of the biggest challenges hindering progress in low-resource and multilingual machine translation is the lack of good evaluation benchmarks. Current evaluation benchmarks either lack good coverage of low-resource languages, consider only restricted domains, or are low quality because they are constructed using semi-automatic procedures. In this work, we introduce the FLORES evaluation benchmark, consisting of 3001 sentences extracted from English Wikipedia and covering a variety of different topics and domains. These sentences have been translated in 101 languages by professional translators through a carefully controlled process. The resulting dataset enables better assessment of model quality on the long tail of low-resource languages, including the evaluation of many-to-many multilingual translation systems, as all translations are multilingually aligned. By publicly releasing such a high-quality and high-coverage dataset, we hope to foster progress in the machine translation community and beyond.

**Disclaimer**: *The Flores-101 dataset is hosted by the Facebook and licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

### Supported Tasks and Leaderboards

#### Multilingual Machine Translation

Refer to the [Dynabench leaderboard](https://dynabench.org/flores/Flores%20MT%20Evaluation%20(FULL)) for additional details on model evaluation on FLORES-101 in the context of the WMT2021 shared task on [Large-Scale Multilingual Machine Translation](http://www.statmt.org/wmt21/large-scale-multilingual-translation-task.html).

### Languages

The dataset contains parallel sentences for 101 languages, as mentioned in the original [Github](https://github.com/facebookresearch/flores/blob/master/README.md) page for the project. Languages are identified with the ISO 639-3 code (e.g. `eng`, `fra`, `rus`) as in the original dataset.

**New:** Use the configuration `all` to access the full set of parallel sentences for all the available languages in a single command.


## Dataset Structure

### Data Instances

A sample from the `dev` split for the Russian language (`rus` config) is provided below. All configurations have the same structure, and all sentences are aligned across configurations and splits.

```python
{
	'id': 1,
	'sentence': 'В понедельник ученые из Медицинской школы Стэнфордского университета объявили об изобретении нового диагностического инструмента, который может сортировать клетки по их типу; это маленький чип, который можно напечатать, используя стандартный струйный принтер примерно за 1 цент США.',
	'URL': 'https://en.wikinews.org/wiki/Scientists_say_new_medical_diagnostic_chip_can_sort_cells_anywhere_with_an_inkjet',
	'domain': 'wikinews',
	'topic': 'health',
	'has_image': 0,
	'has_hyperlink': 0
}
```

The text is provided as-in the original dataset, without further preprocessing or tokenization.

### Data Fields

- `id`: Row number for the data entry, starting at 1.
- `sentence`: The full sentence in the specific language.
- `URL`: The URL for the English article from which the sentence was extracted.
- `domain`: The domain of the sentence.
- `topic`: The topic of the sentence.
- `has_image`: Whether the  original article contains an image.
- `has_hyperlink`: Whether the  sentence contains a hyperlink.

### Data Splits

|            config| `dev`| `devtest`|
|-----------------:|-----:|---------:|
|all configurations|   997|     1012:|

### Dataset Creation

Please refer to the original article [The FLORES-101 Evaluation Benchmark for Low-Resource and Multilingual Machine Translation](https://arxiv.org/abs/2106.03193) for additional information on dataset creation.

## Additional Information

### Dataset Curators

The original authors of FLORES-101 are the curators of the original dataset. For problems or updates on this 🤗 Datasets version, please contact [gabriele.sarti996@gmail.com](mailto:gabriele.sarti996@gmail.com).

### Licensing Information

Licensed with Creative Commons Attribution Share Alike 4.0. License available [here](https://creativecommons.org/licenses/by-sa/4.0/).

### Citation Information

Please cite the authors if you use these corpora in your work:

```bibtex
@inproceedings{flores101,
  title={The FLORES-101  Evaluation Benchmark for Low-Resource and Multilingual Machine Translation},
  author={Goyal, Naman and Gao, Cynthia and Chaudhary, Vishrav and Chen, Peng-Jen and Wenzek, Guillaume and Ju, Da and Krishnan, Sanjana and Ranzato, Marc'Aurelio and Guzm\'{a}n, Francisco and Fan, Angela},
  journal={arXiv preprint arXiv:2106.03193},
  year={2021}
}
```