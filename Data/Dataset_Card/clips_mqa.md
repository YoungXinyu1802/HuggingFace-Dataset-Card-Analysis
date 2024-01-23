---
annotations_creators:
- no-annotation
language_creators:
- other
language:
- ca
- en
- de
- es
- fr
- ru
- ja
- it
- zh
- pt
- nl
- tr
- pl
- vi
- ar
- id
- uk
- ro
- no
- th
- sv
- el
- fi
- he
- da
- cs
- ko
- fa
- hi
- hu
- sk
- lt
- et
- hr
- is
- lv
- ms
- bg
- sr
- ca 
license:
- cc0-1.0
multilinguality:
- multilingual
pretty_name: MQA - a Multilingual FAQ and CQA Dataset
size_categories:
- unknown
source_datasets:
- original
task_categories:
- question-answering
task_ids:
- multiple-choice-qa
---
# MQA
MQA is a Multilingual corpus of Questions and Answers (MQA) parsed from the [Common Crawl](https://commoncrawl.org/). Questions are divided in two types: *Frequently Asked Questions (FAQ)* and *Community Question Answering (CQA)*.
```python
from datasets import load_dataset
all_data = load_dataset("clips/mqa", language="en")
{
  "name": "the title of the question (if any)",
  "text": "the body of the question (if any)",
  "answers": [{
    "text": "the text of the answer",
    "is_accepted": "true|false"
  }]
}
faq_data = load_dataset("clips/mqa", scope="faq", language="en")
cqa_data = load_dataset("clips/mqa", scope="cqa", language="en")
```

## Languages
We collected around **234M pairs** of questions and answers in **39 languages**. To download a language specific subset you need to specify the language key as configuration. See below for an example.
```python
load_dataset("clips/mqa", language="en") # replace "en" by any language listed below
```

| Language   |         FAQ |        CQA |
|:-----------|------------:|-----------:|
| en         | 174,696,414 | 14,082,180 |
| de         |  17,796,992 |  1,094,606 |
| es         |  14,967,582 |    845,836 |
| fr         |  13,096,727 |  1,299,359 |
| ru         |  12,435,022 |  1,715,131 |
| it         |   6,850,573 |    455,027 |
| ja         |   6,369,706 |  2,089,952 |
| zh         |   5,940,796 |    579,596 |
| pt         |   5,851,286 |    373,982 |
| nl         |   4,882,511 |    503,376 |
| tr         |   3,893,964 |    370,975 |
| pl         |   3,766,531 |     70,559 |
| vi         |   2,795,227 |     96,528 |
| id         |   2,253,070 |    200,441 |
| ar         |   2,211,795 |    805,661 |
| uk         |   2,090,611 |     27,260 |
| el         |   1,758,618 |     17,167 |
| no         |   1,752,820 |     11,786 |
| sv         |   1,733,582 |     20,024 |
| fi         |   1,717,221 |     41,371 |
| ro         |   1,689,471 |     93,222 |
| th         |   1,685,463 |     73,204 |
| da         |   1,554,581 |     16,398 |
| he         |   1,422,449 |     88,435 |
| ko         |   1,361,901 |     49,061 |
| cs         |   1,224,312 |    143,863 |
| hu         |     878,385 |     27,639 |
| fa         |     787,420 |    118,805 |
| sk         |     785,101 |      4,615 |
| lt         |     672,105 |        301 |
| et         |     547,208 |        441 |
| hi         |     516,342 |    205,645 |
| hr         |     458,958 |     11,677 |
| is         |     437,748 |         37 |
| lv         |     428,002 |         88 |
| ms         |     230,568 |      7,460 |
| bg         |     198,671 |      5,320 |
| sr         |     110,270 |      3,980 |
| ca         |     100,201 |      1,914 |

## FAQ vs. CQA
You can download the *Frequently Asked Questions* (FAQ) or the *Community Question Answering* (CQA) part of the dataset.

```python
faq = load_dataset("clips/mqa", scope="faq")
cqa = load_dataset("clips/mqa", scope="cqa")
all = load_dataset("clips/mqa", scope="all")
```
Although FAQ and CQA questions share the same structure, CQA questions can have multiple answers for a given questions, while FAQ questions have a single answer. FAQ questions typically only have a title (`name` key), while CQA have a title and a body (`name` and `text`).

## Nesting and Data Fields
You can specify three different nesting level: `question`, `page` and `domain`.
#### Question
```python
load_dataset("clips/mqa", level="question") # default
```
The default level is the question object:
- **name**: the title of the question(if any) in markdown format 
- **text**: the body of the question (if any) in markdown format
- **answers**: a list of answers
    - **text**: the title of the answer (if any) in markdown format
    - **name**: the body of the answer in markdown format
    - **is_accepted**: true if the answer is selected.

#### Page
This level returns a list of questions present on the same page. This is mostly useful for FAQs since CQAs already have one question per page.
```python
load_dataset("clips/mqa", level="page")
```

#### Domain
This level returns a list of pages present on the web domain. This is a good way to cope with FAQs duplication by sampling one page per domain at each epoch.

```python
load_dataset("clips/mqa", level="domain")
```

## Source Data

This section was adapted from the source data description of [OSCAR](https://huggingface.co/datasets/oscar#source-data)

Common Crawl is a non-profit foundation which produces and maintains an open repository of web crawled data that is both accessible and analysable. Common Crawl's complete web archive consists of petabytes of data collected over 8 years of web crawling. The repository contains raw web page HTML data (WARC files), metdata extracts (WAT files) and plain text extracts (WET files). The organisation's crawlers has always respected nofollow and robots.txt policies.

To construct MQA, we used the WARC files of Common Crawl.

## People
This model was developed by [Maxime De Bruyn](https://maximedb.vercel.app), Ehsan Lotfi, Jeska Buhmann and Walter Daelemans.

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
@inproceedings{de-bruyn-etal-2021-mfaq,
    title = "{MFAQ}: a Multilingual {FAQ} Dataset",
    author = "De Bruyn, Maxime  and
      Lotfi, Ehsan  and
      Buhmann, Jeska  and
      Daelemans, Walter",
    booktitle = "Proceedings of the 3rd Workshop on Machine Reading for Question Answering",
    month = nov,
    year = "2021",
    address = "Punta Cana, Dominican Republic",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.mrqa-1.1",
    pages = "1--13",
}

```