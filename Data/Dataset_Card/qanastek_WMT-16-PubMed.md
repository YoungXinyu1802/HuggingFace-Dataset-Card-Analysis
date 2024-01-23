---
annotations_creators:
- machine-generated
- expert-generated
language_creators:
- found
language:
- bg
- cs
- da
- de
- el
- en
- es
- et
- fi
- fr
- hu
- it
- lt
- lv
- mt
- nl
- pl
- pt
- ro
- sk
- sl
- sv
multilinguality:
- multilingual
pretty_name: WMT-16-PubMed
size_categories:
- 100K<n<1M
source_datasets:
- extended
task_categories:
- translation
- machine-translation
task_ids:
- translation
- machine-translation
---

# WMT-16-PubMed : European parallel translation corpus from the European Medicines Agency

## Table of Contents
- [Dataset Card for [Needs More Information]](#dataset-card-for-needs-more-information)
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
    - [Source Data](#source-data)
      - [Initial Data Collection and Normalization](#initial-data-collection-and-normalization)
      - [Who are the source language producers?](#who-are-the-source-language-producers)
    - [Personal and Sensitive Information](#personal-and-sensitive-information)
  - [Considerations for Using the Data](#considerations-for-using-the-data)
    - [Other Known Limitations](#other-known-limitations)
  - [Additional Information](#additional-information)
    - [Dataset Curators](#dataset-curators)
    - [Licensing Information](#licensing-information)
    - [Citation Information](#citation-information)

## Dataset Description

- **Homepage:** https://www.statmt.org/wmt16/biomedical-translation-task.html
- **Repository:** https://github.com/biomedical-translation-corpora/corpora
- **Paper:** https://aclanthology.org/W16-2301/
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [Yanis Labrak](mailto:yanis.labrak@univ-avignon.fr)






### Dataset Summary

`WMT-16-PubMed` is a parallel corpus for neural machine translation collected and aligned for ACL 2016 during the [WMT'16 Shared Task: Biomedical Translation Task](https://www.statmt.org/wmt16/biomedical-translation-task.html).  

### Supported Tasks and Leaderboards

`translation`: The dataset can be used to train a model for translation.

### Languages

The corpora consists of a pair of source and target sentences for all 4 different languages :

**List of languages :** `English (en)`,`Spanish (es)`,`French (fr)`,`Portuguese (pt)`.

## Load the dataset with HuggingFace

```python
from datasets import load_dataset
dataset = load_dataset("qanastek/WMT-16-PubMed", split='train', download_mode='force_redownload')
print(dataset)
print(dataset[0])
```

## Dataset Structure

### Data Instances

```plain
         lang    doc_id                                     workshop publisher                                        source_text                                        target_text
0       en-fr  26839447  WMT'16 Biomedical Translation Task - PubMed    pubmed  Global Health: Where Do Physiotherapy and Reha...  La place des cheveux et des poils dans les rit...
1       en-fr  26837117  WMT'16 Biomedical Translation Task - PubMed    pubmed                                            Carabin                                       Les Carabins
2       en-fr  26837116  WMT'16 Biomedical Translation Task - PubMed    pubmed                                In Process Citation  Le laboratoire d'Anatomie, Biomécanique et Org...
3       en-fr  26837115  WMT'16 Biomedical Translation Task - PubMed    pubmed  Comment on the misappropriation of bibliograph...  Du détournement des références bibliographique...
4       en-fr  26837114  WMT'16 Biomedical Translation Task - PubMed    pubmed  Anti-aging medicine, a science-based, essentia...  La médecine anti-âge, une médecine scientifiqu...
...       ...       ...                                          ...       ...                                                ...                                                ...
973972  en-pt  20274330  WMT'16 Biomedical Translation Task - PubMed    pubmed     Myocardial infarction, diagnosis and treatment     Infarto do miocárdio; diagnóstico e tratamento
973973  en-pt  20274329  WMT'16 Biomedical Translation Task - PubMed    pubmed                          The health areas politics                     A política dos campos de saúde
973974  en-pt  20274328  WMT'16 Biomedical Translation Task - PubMed    pubmed  The role in tissue edema and liquid exchanges ...  O papel dos tecidos nos edemas e nas trocas lí...
973975  en-pt  20274327  WMT'16 Biomedical Translation Task - PubMed    pubmed  About suppuration of the wound after thoracopl...  Sôbre as supurações da ferida operatória após ...
973976  en-pt  20274326  WMT'16 Biomedical Translation Task - PubMed    pubmed  Experimental study of liver lesions in the tre...  Estudo experimental das lesões hepáticas no tr...
```

### Data Fields

**lang** : The pair of source and target language of type `String`.

**source_text** : The source text of type `String`.

**target_text** : The target text of type `String`.

### Data Splits

`en-es` : 285,584

`en-fr` : 614,093

`en-pt` : 74,300

## Dataset Creation

### Curation Rationale

For details, check the corresponding [pages](https://www.statmt.org/wmt16/biomedical-translation-task.html).

### Source Data

<!-- #### Initial Data Collection and Normalization

ddd -->

#### Who are the source language producers?

The shared task as been organized by :

* Antonio Jimeno Yepes (IBM Research Australia)
* Aurélie Névéol (LIMSI, CNRS, France)
* Mariana Neves (Hasso-Plattner Institute, Germany)
* Karin Verspoor (University of Melbourne, Australia)

### Personal and Sensitive Information

The corpora is free of personal or sensitive information.

## Considerations for Using the Data

### Other Known Limitations

The nature of the task introduce a variability in the quality of the target translations.

## Additional Information

### Dataset Curators

__Hugging Face WMT-16-PubMed__: Labrak Yanis, Dufour Richard (Not affiliated with the original corpus)

__WMT'16 Shared Task: Biomedical Translation Task__:

* Antonio Jimeno Yepes (IBM Research Australia)
* Aurélie Névéol (LIMSI, CNRS, France)
* Mariana Neves (Hasso-Plattner Institute, Germany)
* Karin Verspoor (University of Melbourne, Australia)

<!-- ### Licensing Information

ddd -->

### Citation Information

Please cite the following paper when using this dataset.

```latex
@inproceedings{bojar-etal-2016-findings,
    title = Findings of the 2016 Conference on Machine Translation,
    author = {
      Bojar, Ondrej  and
      Chatterjee, Rajen  and
      Federmann, Christian  and
      Graham, Yvette  and
      Haddow, Barry  and
      Huck, Matthias  and
      Jimeno Yepes, Antonio  and
      Koehn, Philipp  and
      Logacheva, Varvara  and
      Monz, Christof  and
      Negri, Matteo  and
      Neveol, Aurelie  and
      Neves, Mariana  and
      Popel, Martin  and
      Post, Matt  and
      Rubino, Raphael  and
      Scarton, Carolina  and
      Specia, Lucia  and
      Turchi, Marco  and
      Verspoor, Karin  and
      Zampieri, Marcos,
    },
    booktitle = Proceedings of the First Conference on Machine Translation: Volume 2, Shared Task Papers,
    month = aug,
    year = 2016,
    address = Berlin, Germany,
    publisher = Association for Computational Linguistics,
    url = https://aclanthology.org/W16-2301,
    doi = 10.18653/v1/W16-2301,
    pages = 131--198,
}
```
