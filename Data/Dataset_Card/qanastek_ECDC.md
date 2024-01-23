---
annotations_creators:
- machine-generated
- expert-generated
language_creators:
- found
language:
- en
license:
- other
multilinguality:
- en-sv
- en-pl
- en-hu
- en-lt
- en-sk
- en-ga
- en-fr
- en-cs
- en-el
- en-it
- en-lv
- en-da
- en-nl
- en-bg
- en-is
- en-ro
- en-no
- en-pt
- en-es
- en-et
- en-mt
- en-sl
- en-fi
- en-de
pretty_name: ECDC
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

# ECDC : An overview of the European Union's highly multilingual parallel corpora

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
    - [No Warranty](#no-warranty)
    - [Citation Information](#citation-information)

## Dataset Description

- **Homepage:** https://joint-research-centre.ec.europa.eu/language-technology-resources/ecdc-translation-memory_en#Introduction
- **Repository:** https://joint-research-centre.ec.europa.eu/language-technology-resources/ecdc-translation-memory_en#Introduction
- **Paper:** https://dl.acm.org/doi/10.1007/s10579-014-9277-0
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [Yanis Labrak](mailto:yanis.labrak@univ-avignon.fr)






### Dataset Summary

In October 2012, the European Union (EU) agency 'European Centre for Disease Prevention and Control' (ECDC) released a translation memory (TM), i.e. a collection of sentences and their professionally produced translations, in twenty-five languages. The data gets distributed via the [web pages of the EC's Joint Research Centre (JRC)](https://joint-research-centre.ec.europa.eu/language-technology-resources/ecdc-translation-memory_en#Introduction).

### Supported Tasks and Leaderboards

`translation`: The dataset can be used to train a model for translation.

### Languages

In our case, the corpora consists of a pair of source and target sentences for all 22 different languages from the European Union (EU).

**List of languages :** `English (en)`, `Swedish (sv)`, `Polish (pl)`, `Hungarian (hu)`,`Lithuanian (lt)`, `Latvian (lv)`, `German (de)`, `Finnish (fi)`, `Slovak (sk)`,`Slovenian (sl)`, `French (fr)`, ,`Czech (cs)`,`Danish (da)`, `Italian (it)`,`Maltese (mt)`,`Dutch (nl)`,`Portuguese (pt)`,`Romanian (ro)`, `Spanish (es)`,`Estonian (et)`, `Bulgarian (bg)`,`Greek (el)`, `Irish (ga)`, `Icelandic (is)` and `Norwegian (no)`.

## Load the dataset with HuggingFace

```python
from datasets import load_dataset
dataset = load_dataset("qanastek/ECDC", "en-it", split='train', download_mode='force_redownload')
print(dataset)
print(dataset[0])
```

## Dataset Structure

### Data Instances

```plain
key,lang,source_text,target_text
doc_0,en-bg,Vaccination against hepatitis C is not yet available.,Засега няма ваксина срещу хепатит С.
doc_1355,en-bg,Varicella infection,Инфекция с варицела
doc_2349,en-bg,"If you have any questions about the processing of your e-mail and related personal data, do not hesitate to include them in your message.","Ако имате въпроси относно обработката на вашия адрес на електронна поща и свързаните лични данни, не се колебайте да ги включите в съобщението си."
doc_192,en-bg,Transmission can be reduced especially by improving hygiene in food production handling.,Предаването на инфекцията може да бъде ограничено особено чрез подобряване на хигиената при манипулациите в хранителната индустрия.
```

### Data Fields

**key** : The document identifier `String`.

**lang** : The pair of source and target language of type `String`.

**source_text** : The source text of type `String`.

**target_text** : The target text of type `String`.

### Data Splits

|lang | key |
|-----|-----|
|en-bg|2567 |
|en-cs|2562 |
|en-da|2577 |
|en-de|2560 |
|en-el|2530 |
|en-es|2564 |
|en-et|2581 |
|en-fi|2617 |
|en-fr|2561 |
|en-ga|1356 |
|en-hu|2571 |
|en-is|2511 |
|en-it|2534 |
|en-lt|2545 |
|en-lv|2542 |
|en-mt|2539 |
|en-nl|2510 |
|en-no|2537 |
|en-pl|2546 |
|en-pt|2531 |
|en-ro|2555 |
|en-sk|2525 |
|en-sl|2545 |
|en-sv|2527 |

## Dataset Creation

### Curation Rationale

For details, check the corresponding [pages](https://joint-research-centre.ec.europa.eu/language-technology-resources/ecdc-translation-memory_en#Introduction).

### Source Data

<!-- #### Initial Data Collection and Normalization

ddd -->

#### Who are the source language producers?

Every data of this corpora as been uploaded by on [JRC](https://joint-research-centre.ec.europa.eu/language-technology-resources/ecdc-translation-memory_en#Introduction).

### Personal and Sensitive Information

The corpora is free of personal or sensitive information.

## Considerations for Using the Data

### Other Known Limitations

The nature of the task introduce a variability in the quality of the target translations.

## Additional Information

### Dataset Curators

__Hugging Face ECDC__: Labrak Yanis, Dufour Richard (Not affiliated with the original corpus)

__An overview of the European Union's highly multilingual parallel corpora__: Steinberger Ralf, Mohamed Ebrahim, Alexandros Poulis, Manuel Carrasco-Benitez, Patrick Schlüter, Marek Przybyszewski & Signe Gilbro.

### Licensing Information

By downloading or using the ECDC-Translation Memory, you are bound by the [ECDC-TM usage conditions (PDF)](https://wt-public.emm4u.eu/Resources/ECDC-TM/2012_10_Terms-of-Use_ECDC-TM.pdf).

### No Warranty

Each Work is provided ‘as is’ without, to the full extent permitted by law, representations,
warranties, obligations and liabilities of any kind, either express or implied, including, but
not limited to, any implied warranty of merchantability, integration, satisfactory quality and
fitness for a particular purpose.

Except in the cases of wilful misconduct or damages directly caused to natural persons, the
Owner will not be liable for any incidental, consequential, direct or indirect damages,
including, but not limited to, the loss of data, lost profits or any other financial loss arising
from the use of, or inability to use, the Work even if the Owner has been notified of the
possibility of such loss, damages, claims or costs, or for any claim by any third party. The
Owner may be liable under national statutory product liability laws as far as such laws apply
to the Work.

### Citation Information

Please cite the following paper when using this dataset.

```latex
@article{10.1007/s10579-014-9277-0,
  author = {Steinberger, Ralf and Ebrahim, Mohamed and Poulis, Alexandros and Carrasco-Benitez, Manuel and Schl\"{u}ter, Patrick and Przybyszewski, Marek and Gilbro, Signe},
  title = {An Overview of the European Union's Highly Multilingual Parallel Corpora},
  year = {2014},
  issue_date = {December  2014},
  publisher = {Springer-Verlag},
  address = {Berlin, Heidelberg},
  volume = {48},
  number = {4},
  issn = {1574-020X},
  url = {https://doi.org/10.1007/s10579-014-9277-0},
  doi = {10.1007/s10579-014-9277-0},
  abstract = {Starting in 2006, the European Commission's Joint Research Centre and other European Union organisations have made available a number of large-scale highly-multilingual parallel language resources. In this article, we give a comparative overview of these resources and we explain the specific nature of each of them. This article provides answers to a number of question, including: What are these linguistic resources? What is the difference between them? Why were they originally created and why was the data released publicly? What can they be used for and what are the limitations of their usability? What are the text types, subject domains and languages covered? How to avoid overlapping document sets? How do they compare regarding the formatting and the translation alignment? What are their usage conditions? What other types of multilingual linguistic resources does the EU have? This article thus aims to clarify what the similarities and differences between the various resources are and what they can be used for. It will also serve as a reference publication for those resources, for which a more detailed description has been lacking so far (EAC-TM, ECDC-TM and DGT-Acquis).},
  journal = {Lang. Resour. Eval.},
  month = {dec},
  pages = {679–707},
  numpages = {29},
  keywords = {DCEP, EAC-TM, EuroVoc, JRC EuroVoc Indexer JEX, Parallel corpora, DGT-TM, Eur-Lex, Highly multilingual, Linguistic resources, DGT-Acquis, European Union, ECDC-TM, JRC-Acquis, Translation memory}
}
```
