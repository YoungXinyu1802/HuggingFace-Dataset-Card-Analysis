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
pretty_name: EMEA-V3
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

# EMEA-V3 : European parallel translation corpus from the European Medicines Agency

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

- **Homepage:** https://opus.nlpl.eu/EMEA.php
- **Repository:** https://github.com/qanastek/EMEA-V3/
- **Paper:** https://aclanthology.org/L12-1246/
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [Yanis Labrak](mailto:yanis.labrak@univ-avignon.fr)






### Dataset Summary

`EMEA-V3` is a parallel corpus for neural machine translation collected and aligned by [Tiedemann, Jorg](mailto:jorg.tiedemann@lingfil.uu.se) during the [OPUS project](https://opus.nlpl.eu/).  

### Supported Tasks and Leaderboards

`translation`: The dataset can be used to train a model for translation.

### Languages

In our case, the corpora consists of a pair of source and target sentences for all 22 different languages from the European Union (EU).

**List of languages :** `Bulgarian (bg)`,`Czech (cs)`,`Danish (da)`,`German (de)`,`Greek (el)`,`English (en)`,`Spanish (es)`,`Estonian (et)`,`Finnish (fi)`,`French (fr)`,`Hungarian (hu)`,`Italian (it)`,`Lithuanian (lt)`,`Latvian (lv)`,`Maltese (mt)`,`Dutch (nl)`,`Polish (pl)`,`Portuguese (pt)`,`Romanian (ro)`,`Slovak (sk)`,`Slovenian (sl)`,`Swedish (sv)`.

## Load the dataset with HuggingFace

```python
from datasets import load_dataset
dataset = load_dataset("qanastek/EMEA-V3", split='train', download_mode='force_redownload')
print(dataset)
print(dataset[0])
```

## Dataset Structure

### Data Instances

```plain
lang,source_text,target_text
bg-cs,EMEA/ H/ C/ 471,EMEA/ H/ C/ 471
bg-cs,ABILIFY,ABILIFY
bg-cs,Какво представлява Abilify?,Co je Abilify?
bg-cs,"Abilify е лекарство, съдържащо активното вещество арипипразол.","Abilify je léčivý přípravek, který obsahuje účinnou látku aripiprazol."
bg-cs,"Предлага се под формата на таблетки от 5 mg, 10 mg, 15 mg и 30 mg, като диспергиращи се таблетки (таблетки, които се разтварят в устата) от 10 mg, 15 mg и 30 mg, като перорален разтвор (1 mg/ ml) и като инжекционен разтвор (7, 5 mg/ ml).","Je dostupný ve formě tablet s obsahem 5 mg, 10 mg, 15 mg a 30 mg, ve formě tablet dispergovatelných v ústech (tablet, které se rozpustí v ústech) s obsahem 10 mg, 15 mg a 30 mg, jako perorální roztok (1 mg/ ml) nebo jako injekční roztok (7, 5 mg/ ml)."
bg-cs,За какво се използва Abilify?,Na co se přípravek Abilify používá?
```

### Data Fields

**lang** : The pair of source and target language of type `String`.

**source_text** : The source text of type `String`.

**target_text** : The target text of type `String`.

### Data Splits

|        |     bg |     cs |     da |     de |     el |     en |     es |     et |     fi |     fr |     hu |     it |     lt |     lv |     mt |     nl |     pl |     pt |     ro |     sk |     sl |     sv |
|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| **bg** |      0 | 342378 | 349675 | 348061 | 355696 | 333066 | 349936 | 336142 | 341732 | 358045 | 352763 | 351669 | 348679 | 342721 | 351097 | 353942 | 355005 | 347925 | 351099 | 345572 | 346954 | 342927 |
| **cs** | 342378 |      0 | 354824 | 353397 | 364609 | 335716 | 356506 | 340309 | 349040 | 363614 | 358353 | 357578 | 353232 | 347807 | 334353 | 355192 | 358357 | 351244 | 330447 | 346835 | 348411 | 346894 |
| **da** | 349675 | 354824 |      0 | 387202 | 397654 | 360186 | 387329 | 347391 | 379830 | 396294 | 367091 | 388495 | 360572 | 353801 | 342263 | 388250 | 368779 | 382576 | 340508 | 356890 | 357694 | 373510 |
| **de** | 348061 | 353397 | 387202 |      0 | 390281 | 364005 | 386335 | 346166 | 378626 | 393468 | 366828 | 381396 | 360907 | 353151 | 340294 | 377770 | 367080 | 381365 | 337562 | 355805 | 358700 | 376925 |
| **el** | 355696 | 364609 | 397654 | 390281 |      0 | 372824 | 393051 | 354874 | 384889 | 403248 | 373706 | 391389 | 368576 | 360047 | 348221 | 396284 | 372486 | 387170 | 342655 | 364959 | 363778 | 384569 |
| **en** | 333066 | 335716 | 360186 | 364005 | 372824 |      0 | 366769 | 333667 | 357177 | 373152 | 349176 | 361089 | 339899 | 336306 | 324695 | 360418 | 348450 | 361393 | 321233 | 338649 | 338195 | 352587 |
| **es** | 349936 | 356506 | 387329 | 386335 | 393051 | 366769 |      0 | 348454 | 378158 | 394253 | 368203 | 378076 | 360645 | 354126 | 340297 | 381188 | 367091 | 376443 | 337302 | 358745 | 357961 | 379462 |
| **et** | 336142 | 340309 | 347391 | 346166 | 354874 | 333667 | 348454 |      0 | 341694 | 358012 | 352099 | 351747 | 345417 | 339042 | 337302 | 350911 | 354329 | 345856 | 325992 | 343950 | 342787 | 340761 |
| **fi** | 341732 | 349040 | 379830 | 378626 | 384889 | 357177 | 378158 | 341694 |      0 | 387478 | 358869 | 379862 | 352968 | 346820 | 334275 | 379729 | 358760 | 374737 | 331135 | 348559 | 348680 | 368528 |
| **fr** | 358045 | 363614 | 396294 | 393468 | 403248 | 373152 | 394253 | 358012 | 387478 |      0 | 373625 | 385869 | 368817 | 361137 | 347699 | 388607 | 372387 | 388658 | 344139 | 363249 | 366474 | 383274 |
| **hu** | 352763 | 358353 | 367091 | 366828 | 373706 | 349176 | 368203 | 352099 | 358869 | 373625 |      0 | 367937 | 361015 | 354872 | 343831 | 368387 | 369040 | 361652 | 340410 | 357466 | 361157 | 356426 |
| **it** | 351669 | 357578 | 388495 | 381396 | 391389 | 361089 | 378076 | 351747 | 379862 | 385869 | 367937 |      0 | 360783 | 356001 | 341552 | 384018 | 365159 | 378841 | 337354 | 357562 | 358969 | 377635 |
| **lt** | 348679 | 353232 | 360572 | 360907 | 368576 | 339899 | 360645 | 345417 | 352968 | 368817 | 361015 | 360783 |      0 | 350576 | 337339 | 362096 | 361497 | 357070 | 335581 | 351639 | 350916 | 349636 |
| **lv** | 342721 | 347807 | 353801 | 353151 | 360047 | 336306 | 354126 | 339042 | 346820 | 361137 | 354872 | 356001 | 350576 |      0 | 336157 | 355791 | 358607 | 349590 | 329581 | 348689 | 346862 | 345016 |
| **mt** | 351097 | 334353 | 342263 | 340294 | 348221 | 324695 | 340297 | 337302 | 334275 | 347699 | 343831 | 341552 | 337339 | 336157 |      0 | 341111 | 344764 | 335553 | 338137 | 335930 | 334491 | 335353 |
| **nl** | 353942 | 355192 | 388250 | 377770 | 396284 | 360418 | 381188 | 350911 | 379729 | 388607 | 368387 | 384018 | 362096 | 355791 | 341111 |      0 | 369694 | 383913 | 339047 | 359126 | 360054 | 379771 |
| **pl** | 355005 | 358357 | 368779 | 367080 | 372486 | 348450 | 367091 | 354329 | 358760 | 372387 | 369040 | 365159 | 361497 | 358607 | 344764 | 369694 |      0 | 357426 | 335243 | 352527 | 355534 | 353214 |
| **pt** | 347925 | 351244 | 382576 | 381365 | 387170 | 361393 | 376443 | 345856 | 374737 | 388658 | 361652 | 378841 | 357070 | 349590 | 335553 | 383913 | 357426 |      0 | 333365 | 354784 | 352673 | 373392 |
| **ro** | 351099 | 330447 | 340508 | 337562 | 342655 | 321233 | 337302 | 325992 | 331135 | 344139 | 340410 | 337354 | 335581 | 329581 | 338137 | 339047 | 335243 | 333365 |      0 | 332373 | 330329 | 331268 |
| **sk** | 345572 | 346835 | 356890 | 355805 | 364959 | 338649 | 358745 | 343950 | 348559 | 363249 | 357466 | 357562 | 351639 | 348689 | 335930 | 359126 | 352527 | 354784 | 332373 |      0 | 348396 | 346855 |
| **sl** | 346954 | 348411 | 357694 | 358700 | 363778 | 338195 | 357961 | 342787 | 348680 | 366474 | 361157 | 358969 | 350916 | 346862 | 334491 | 360054 | 355534 | 352673 | 330329 | 348396 |      0 | 347727 |
| **sv** | 342927 | 346894 | 373510 | 376925 | 384569 | 352587 | 379462 | 340761 | 368528 | 383274 | 356426 | 377635 | 349636 | 345016 | 335353 | 379771 | 353214 | 373392 | 331268 | 346855 | 347727 |      0 |

## Dataset Creation

### Curation Rationale

For details, check the corresponding [pages](https://opus.nlpl.eu/EMEA.php).

### Source Data

<!-- #### Initial Data Collection and Normalization

ddd -->

#### Who are the source language producers?

Every data of this corpora as been uploaded by [Tiedemann, Jorg](mailto:jorg.tiedemann@lingfil.uu.se) on [Opus](https://opus.nlpl.eu/EMEA.php).

### Personal and Sensitive Information

The corpora is free of personal or sensitive information.

## Considerations for Using the Data

### Other Known Limitations

The nature of the task introduce a variability in the quality of the target translations.

## Additional Information

### Dataset Curators

__Hugging Face EMEA-V3__: Labrak Yanis, Dufour Richard (Not affiliated with the original corpus)

__OPUS : Parallel Data, Tools and Interfaces in OPUS__: [Tiedemann, Jorg](mailto:jorg.tiedemann@lingfil.uu.se).

<!-- ### Licensing Information

ddd -->

### Citation Information

Please cite the following paper when using this dataset.

```latex
@inproceedings{tiedemann-2012-parallel,
    title = Parallel Data, Tools and Interfaces in OPUS,
    author = {
      Tiedemann, Jorg
    },
    booktitle = "Proceedings of the Eighth International Conference on Language Resources and Evaluation (LREC'12)",
    month = may,
    year = 2012,
    address = Istanbul, Turkey,
    publisher = European Language Resources Association (ELRA),
    url = http://www.lrec-conf.org/proceedings/lrec2012/pdf/463_Paper.pdf,
    pages = 2214--2218,
    abstract = This paper presents the current status of OPUS, a growing language resource of parallel corpora and related tools. The focus in OPUS is to provide freely available data sets in various formats together with basic annotation to be useful for applications in computational linguistics, translation studies and cross-linguistic corpus studies. In this paper, we report about new data sets and their features, additional annotation tools and models provided from the website and essential interfaces and on-line services included in the project.,
}
```
