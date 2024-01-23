---
annotations_creators:
- found
language_creators:
- found
language:
- en
license:
- cc-by-nc-sa-4.0
multilinguality:
- multilingual
pretty_name: stackexchange
size_categories:
- unknown
source_datasets:
- original
task_categories:
- question-answering
task_ids:
- closed-domain-qa
---

# Dataset Card Creation Guide

## Table of Contents
- [Dataset Card Creation Guide](#dataset-card-creation-guide)
  - [Table of Contents](#table-of-contents)
  - [Dataset Description](#dataset-description)
    - [Dataset Summary](#dataset-summary)
    - [Languages](#languages)
  - [Dataset Structure](#dataset-structure)
    - [Data Instances](#data-instances)
    - [Data Fields](#data-fields)
    - [Data Splits](#data-splits)
  - [Dataset Creation](#dataset-creation)
    - [Curation Rationale](#curation-rationale)
    - [Source Data](#source-data)
      - [Initial Data Collection and Normalization](#initial-data-collection-and-normalization)
      - [Who are the source language producers?](#who-are-the-source-language-producers)s
  - [Additional Information](#additional-information)
    - [Licensing Information](#licensing-information)
    - [Citation Information](#citation-information)
    - [Contributions](#contributions)

## Dataset Description

- **Homepage:** [stackexchange](https://archive.org/details/stackexchange)
- **Repository:** [flax-sentence-embeddings](https://github.com/nreimers/flax-sentence-embeddings)

### Dataset Summary

We automatically extracted question and answer (Q&A) pairs from [Stack Exchange](https://stackexchange.com/) network. Stack Exchange gather many Q&A communities across 50 online plateform, including the well known Stack Overflow and other technical sites. 100 millon developpers consult Stack Exchange every month. The dataset is a parallel corpus with each question mapped to the top rated answer. The dataset is split given communities which cover a variety of domains from 3d printing, economics, raspberry pi or emacs. An exhaustive list of all communities is available [here](https://stackexchange.com/sites).

### Languages

Stack Exchange mainly consist of english language (en).

## Dataset Structure

### Data Instances

Each data samples is presented as follow:

```
{'title_body': "Is there a Stack Exchange icon available? StackAuth /sites route provides all the site's icons except for the one of the Stack Exchange master site.\nCould you please provide it in some way (a static SVG would be good)?",
 'upvoted_answer': 'Here it is!\n\nDead link: SVG version here\nNote: the same restrictions on this trademarked icon that apply here, also apply to the icon above.',
 'downvoted_answer': 'No, the /sites route is not the right place for that.\n\n/sites enumerates all websites that expose API end-points. StackExchange.com does not expose such an endpoint, so it does not (and will not) appear in the results.'}
```

This particular exampe corresponds to the [following page](https://stackapps.com/questions/1508/is-there-a-stack-exchange-icon-available)

### Data Fields

The fields present in the dataset contain the following informations:

- `title_body`: This is the concatenation of the title and body from the question
- `upvoted_answer`: This is the body from the most upvoted answer
- `downvoted_answer`: This is the body from the most downvoted answer

### Data Splits

We provide multiple splits for this dataset, which each refers to a given community channel. We detail the number of pail for each split below:


|                            | Number of pairs   |
| -----                      | ------ | 
| english | 13,003 |
| academia | 2,465 |
| christianity | 1,502 |
| apple | 6,696 |
| electronics | 4,014 |
| gaming | 7,321 |
| askubuntu | 9,975 |
| ell | 4,438 |
| hermeneutics | 1,719 |
| judaism | 2,216 |
| diy | 2,037 |
| law | 1,297 |
| history | 1,099 |
| islam | 2,037 |
| dba | 2,502 |
| cooking | 2,064 |
| gamedev | 1,598 |
| drupal | 1,714 |
| chemistry | 1,523 |
| android | 2,830 |
| mathoverflow | 1,109 |
| magento | 1,849 |
| buddhism | 770 |
| gis | 1,843 |
| graphicdesign | 1,565 |
| codereview | 666 |
| aviation | 903 |
| bicycles | 984 |
| japanese | 1,124 |
| cs | 936 |
| german | 1,047 |
| interpersonal | 469 |
| biology | 832 |
| bitcoin | 1,068 |
| blender | 1,312 |
| crypto | 595 |
| anime | 802 |
| boardgames | 691 |
| hinduism | 343 |
| french | 632 |
| fitness | 567 |
| economics | 441 |
| chinese | 611 |
| codegolf | 333 |
| linguistics | 442 |
| astronomy | 371 |
| arduino | 595 |
| chess | 402 |
| cstheory | 314 |
| ja | 328 |
| martialarts | 254 |
| mathematica | 262 |
| dsp | 387 |
| ethereum | 479 |
| health | 299 |
| cogsci | 221 |
| earthscience | 229 |
| gardening | 210 |
| datascience | 325 |
| literature | 191 |
| matheducators | 177 |
| lifehacks | 316 |
| engineering | 227 |
| ham | 158 |
| 3dprinting | 109 |
| italian | 181 |
| emacs | 188 |
| homebrew | 176 |
| ai | 130 |
| avp | 152 |
| expatriates | 132 |
| elementaryos | 224 |
| cseducators | 67 |
| hsm | 70 |
| expressionengine | 91 |
| joomla | 124 |
| freelancing | 70 |
| crafts | 72 |
| genealogy | 86 |
| latin | 55 |
| hardwarerecs | 58 |
| devops | 53 |
| coffee | 47 |
| beer | 57 |
| languagelearning | 42 |
| ebooks | 54 |
| bricks | 79 |
| civicrm | 85 |
| bioinformatics | 39 |
| esperanto | 56 |
| computergraphics | 30 |
| conlang | 8 |
| korean | 28 |
| iota | 31 |
| eosio | 44 |
| craftcms | 26 |
| iot | 10 |
| drones | 6 |
| cardano | 7 |
| materials | 1 |
| ru | 6,305 |
| softwareengineering | 4,238 |
| scifi | 5,176 |
| workplace | 4,317 |
| serverfault | 7,969 |
| rpg | 4,212 |
| physics | 8,362 |
| superuser | 17,425 |
| worldbuilding | 2,087 |
| security | 3,069 |
| pt | 3,718 |
| unix | 6,173 |
| meta | 61 |
| politics | 1,468 |
| stats | 2,238 |
| movies | 1,577 |
| photo | 1,432 |
| wordpress | 3,046 |
| music | 1,228 |
| philosophy | 1,184 |
| skeptics | 670 |
| money | 1,905 |
| salesforce | 1,781 |
| parenting | 624 |
| raspberrypi | 1,011 |
| travel | 1,317 |
| mechanics | 842 |
| tex | 1,095 |
| ux | 1,107 |
| sharepoint | 1,691 |
| webapps | 1,906 |
| puzzling | 784 |
| networkengineering | 476 |
| webmasters | 854 |
| sports | 455 |
| rus | 514 |
| space | 405 |
| writers | 407 |
| pets | 322 |
| pm | 241 |
| russian | 353 |
| spanish | 366 |
| sound | 365 |
| quant | 340 |
| sqa | 353 |
| outdoors | 221 |
| softwarerecs | 348 |
| retrocomputing | 135 |
| mythology | 103 |
| portuguese | 144 |
| opensource | 123 |
| scicomp | 127 |
| ukrainian | 87 |
| patents | 137 |
| sustainability | 152 |
| poker | 115 |
| robotics | 110 |
| woodworking | 93 |
| reverseengineering | 97 |
| sitecore | 122 |
| tor | 137 |
| vi | 95 |
| windowsphone | 153 |
| vegetarianism | 35 |
| moderators | 23 |
| quantumcomputing | 46 |
| musicfans | 78 |
| tridion | 68 |
| opendata | 45 |
| tezos | 11 |
| stellar | 3 |
| or | 13 |
| monero | 26 |
| stackapps | 15 |
| total | 210,748 |

## Dataset Creation

### Curation Rationale

We primary designed this dataset for sentence embeddings training. Indeed sentence embeddings may be trained using a contrastive learning setup for which the model is trained to associate each sentence with its corresponding pair out of multiple proposition. Such models require many examples to be efficient and thus the dataset creation may be tedious. Community networks such as Stack Exchange allow us to build many examples semi-automatically.

### Source Data

The source data are dumps from [Stack Exchange](https://archive.org/details/stackexchange)

#### Initial Data Collection and Normalization

We collected the data from the math community. 

We filtered out questions which title or body length is bellow 20 characters and questions for which body length is above 4096 characters.
When extracting most upvoted answer, we filtered to pairs for which their is at least 100 votes gap between most upvoted and downvoted answers.

#### Who are the source language producers?

Questions and answers are written by the community developpers of Stack Exchange.

## Additional Information

### Licensing Information

Please see the license information at: https://archive.org/details/stackexchange

### Citation Information

```
@misc{StackExchangeDataset,
  author = {Flax Sentence Embeddings Team},
  title = {Stack Exchange question pairs},
  year = {2021},
  howpublished = {https://huggingface.co/datasets/flax-sentence-embeddings/},
}
```


### Contributions

Thanks to the Flax Sentence Embeddings team for adding this dataset.