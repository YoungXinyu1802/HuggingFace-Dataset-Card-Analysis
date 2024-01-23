---
annotations_creators:
- found
language_creators:
- expert-generated
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
- text2text-generation
- translation
task_ids: []
paperswithcode_id: flores
pretty_name: flores200
tags:
- conditional-text-generation
---

# Dataset Card for Flores200

## Table of Contents

- [Dataset Card for Flores200](#dataset-card-for-flores200)
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

- **Home:** [Flores](https://github.com/facebookresearch/flores)
- **Repository:** [Github](https://github.com/facebookresearch/flores)

### Dataset Summary

FLORES is a benchmark dataset for machine translation between English and low-resource languages.

>The creation of FLORES200 doubles the existing language coverage of FLORES-101. 
Given the nature of the new languages, which have less standardization and require 
more specialized professional translations, the verification process became more complex. 
This required modifications to the translation workflow. FLORES-200 has several languages 
which were not translated from English. Specifically, several languages were translated 
from Spanish, French, Russian and Modern Standard Arabic. Moreover, FLORES-200 also 
includes two script alternatives for four languages. FLORES-200 consists of translations 
from 842 distinct web articles, totaling 3001 sentences. These sentences are divided 
into three splits: dev, devtest, and test (hidden). On average, sentences are approximately 
21 words long.

**Disclaimer**: *The Flores200 dataset is hosted by the Facebook and licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).
### Supported Tasks and Leaderboards
#### Multilingual Machine Translation
Refer to the [Dynabench leaderboard](https://dynabench.org/flores/Flores%20MT%20Evaluation%20(FULL)) for additional details on model evaluation on FLORES-101 in the context of the WMT2021 shared task on [Large-Scale Multilingual Machine Translation](http://www.statmt.org/wmt21/large-scale-multilingual-translation-task.html). Flores 200 is an extention of this.
### Languages
The dataset contains parallel sentences for 200 languages, as mentioned in the original [Github](https://github.com/facebookresearch/flores/blob/master/README.md) page for the project. Languages are identified with the ISO 639-3 code (e.g. `eng`, `fra`, `rus`) plus an additional code describing the script (e.g., "eng_Latn", "ukr_Cyrl"). See [the webpage for code descriptions](https://github.com/facebookresearch/flores/blob/main/flores200/README.md).
Use the configuration `all` to access the full set of parallel sentences for all the available languages in a single command. 
Use a hyphenated pairing to get two langauges in one datapoint (e.g., "eng_Latn-ukr_Cyrl" will provide sentences in the format below).
## Dataset Structure
### Data Instances
A sample from the `dev` split for the Russian language (`ukr_Cyrl` config) is provided below. All configurations have the same structure, and all sentences are aligned across configurations and splits.
```python
{
	'id': 1,
	'sentence': 'У понеділок, науковці зі Школи медицини Стенфордського університету оголосили про винайдення нового діагностичного інструменту, що може сортувати клітини за їх видами: це малесенький друкований чіп, який можна виготовити за допомогою стандартних променевих принтерів десь по одному центу США за штуку.',
	'URL': 'https://en.wikinews.org/wiki/Scientists_say_new_medical_diagnostic_chip_can_sort_cells_anywhere_with_an_inkjet',
	'domain': 'wikinews',
	'topic': 'health',
	'has_image': 0,
	'has_hyperlink': 0
}
```
When using a hyphenated pairing or using the `all` function, data will be presented as follows:
```python
{
    'id': 1, 
    'URL': 'https://en.wikinews.org/wiki/Scientists_say_new_medical_diagnostic_chip_can_sort_cells_anywhere_with_an_inkjet', 
    'domain': 'wikinews', 
    'topic': 'health', 
    'has_image': 0, 
    'has_hyperlink': 0, 
    'sentence_eng_Latn': 'On Monday, scientists from the Stanford University School of Medicine announced the invention of a new diagnostic tool that can sort cells by type: a tiny printable chip that can be manufactured using standard inkjet printers for possibly about one U.S. cent each.', 
    'sentence_ukr_Cyrl': 'У понеділок, науковці зі Школи медицини Стенфордського університету оголосили про винайдення нового діагностичного інструменту, що може сортувати клітини за їх видами: це малесенький друкований чіп, який можна виготовити за допомогою стандартних променевих принтерів десь по одному центу США за штуку.'
}
```
The text is provided as-in the original dataset, without further preprocessing or tokenization.
### Data Fields
- `id`: Row number for the data entry, starting at 1.
- `sentence`: The full sentence in the specific language (may have _lang for pairings)
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
Please refer to the original article [No Language Left Behind: Scaling Human-Centered Machine Translation](https://arxiv.org/abs/2207.04672) for additional information on dataset creation.
## Additional Information
### Dataset Curators
See paper for details.
### Licensing Information
Licensed with Creative Commons Attribution Share Alike 4.0. License available [here](https://creativecommons.org/licenses/by-sa/4.0/).
### Citation Information
Please cite the authors if you use these corpora in your work:
```bibtex
@article{nllb2022,
  author    = {NLLB Team, Marta R. Costa-jussà, James Cross, Onur Çelebi, Maha Elbayad, Kenneth Heafield, Kevin Heffernan, Elahe Kalbassi,  Janice Lam, Daniel Licht, Jean Maillard, Anna Sun, Skyler Wang, Guillaume Wenzek, Al Youngblood, Bapi Akula, Loic Barrault, Gabriel Mejia Gonzalez, Prangthip Hansanti, John Hoffman, Semarley Jarrett, Kaushik Ram Sadagopan, Dirk Rowe, Shannon Spruit, Chau Tran, Pierre Andrews, Necip Fazil Ayan, Shruti Bhosale, Sergey Edunov, Angela Fan, Cynthia Gao, Vedanuj Goswami, Francisco Guzmán, Philipp Koehn, Alexandre Mourachko, Christophe Ropers, Safiyyah Saleem, Holger Schwenk, Jeff Wang},
  title     = {No Language Left Behind: Scaling Human-Centered Machine Translation},
  year      = {2022}
}
```