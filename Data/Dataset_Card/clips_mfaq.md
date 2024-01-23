---
annotations_creators:
- no-annotation
language_creators:
- other
language:
- cs
- da
- de
- en
- es
- fi
- fr
- he
- hr
- hu
- id
- it
- nl
- 'no'
- pl
- pt
- ro
- ru
- sv
- tr
- vi
license:
- cc0-1.0
multilinguality:
- multilingual
pretty_name: MFAQ - a Multilingual FAQ Dataset
size_categories:
- unknown
source_datasets:
- original
task_categories:
- question-answering
task_ids:
- multiple-choice-qa
---
# MFAQ

🚨 See [MQA](https://huggingface.co/datasets/clips/mqa) or [MFAQ Light](maximedb/mfaq_light) for an updated version of the dataset.

MFAQ is a multilingual corpus of *Frequently Asked Questions* parsed from the [Common Crawl](https://commoncrawl.org/).
```
from datasets import load_dataset
load_dataset("clips/mfaq", "en")
{
  "qa_pairs": [
    {
      "question": "Do  I need a rental Car in Cork?",
      "answer": "If you plan on travelling outside of Cork City, for instance to  Kinsale [...]"
    },
    ...
  ]
}
```

## Languages
We collected around 6M pairs of questions and answers in 21 different languages. To download a language specific subset you need to specify the language key as configuration. See below for an example.
```
load_dataset("clips/mfaq", "en") # replace "en" by any language listed below
```

| Language   | Key | Pairs     | Pages     |
|------------|-----|-----------|-----------|
| All        | all | 6,346,693 | 1,035,649 |
| English    | en  | 3,719,484 | 608,796   |
| German     | de  | 829,098   | 111,618   |
| Spanish    | es  | 482,818   | 75,489    |
| French     | fr  | 351,458   | 56,317    |
| Italian    | it  | 155,296   | 24,562    |
| Dutch      | nl  | 150,819   | 32,574    |
| Portuguese | pt  | 138,778   | 26,169    |
| Turkish    | tr  | 102,373   | 19,002    |
| Russian    | ru  | 91,771    | 22,643    |
| Polish     | pl  | 65,182    | 10,695    |
| Indonesian | id  | 45,839    | 7,910     |
| Norwegian  | no  | 37,711    | 5,143     |
| Swedish    | sv  | 37,003    | 5,270     |
| Danish     | da  | 32,655    | 5,279     |
| Vietnamese | vi  | 27,157    | 5,261     |
| Finnish    | fi  | 20,485    | 2,795     |
| Romanian   | ro  | 17,066    | 3,554     |
| Czech      | cs  | 16,675    | 2,568     |
| Hebrew     | he  | 11,212    | 1,921     |
| Hungarian  | hu  | 8,598     | 1,264     |
| Croatian   | hr  | 5,215     | 819       |

## Data Fields
#### Nested (per page - default)
The data is organized by page. Each page contains a list of questions and answers.
- **id** 
- **language**
- **num_pairs**: the number of FAQs on the page
- **domain**: source web domain of the FAQs
- **qa_pairs**: a list of questions and answers
  - **question**
  - **answer**
  - **language**
  
#### Flattened
The data is organized by pair (i.e. pages are flattened). You can access the flat version of any language by appending `_flat` to the configuration (e.g. `en_flat`). The data will be returned pair-by-pair instead of page-by-page. 
- **domain_id** 
- **pair_id**
- **language**
- **domain**: source web domain of the FAQs
- **question**
- **answer**

## Source Data

This section was adapted from the source data description of [OSCAR](https://huggingface.co/datasets/oscar#source-data)

Common Crawl is a non-profit foundation which produces and maintains an open repository of web crawled data that is both accessible and analysable. Common Crawl's complete web archive consists of petabytes of data collected over 8 years of web crawling. The repository contains raw web page HTML data (WARC files), metdata extracts (WAT files) and plain text extracts (WET files). The organisation's crawlers has always respected nofollow and robots.txt policies.

To construct MFAQ, the WARC files of Common Crawl were used. We looked for `FAQPage` markup in the HTML and subsequently parsed the `FAQItem` from the page. 

## People
This model was developed by [Maxime De Bruyn](https://www.linkedin.com/in/maximedebruyn/), Ehsan Lotfi, Jeska Buhmann and Walter Daelemans.

## Licensing Information
```
These data are released under this licensing scheme.
We do not own any of the text from which these data has been extracted.
We license the actual packaging of these data under the Creative Commons CC0 license ("no rights reserved") http://creativecommons.org/publicdomain/zero/1.0/

Should you consider that our data contains material that is owned by you and should therefore not be reproduced here, please:
* Clearly identify yourself, with detailed contact data such as an address, telephone number or email address at which you can be contacted.
* Clearly identify the copyrighted work claimed to be infringed.
* Clearly identify the material that is claimed to be infringing and information reasonably sufficient to allow us to locate the material.

We will comply to legitimate requests by removing the affected sources from the next release of the corpus.
```

## Citation information
```
@misc{debruyn2021mfaq,
      title={MFAQ: a Multilingual FAQ Dataset}, 
      author={Maxime {De Bruyn} and Ehsan Lotfi and Jeska Buhmann and Walter Daelemans},
      year={2021},
      eprint={2109.12870},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```