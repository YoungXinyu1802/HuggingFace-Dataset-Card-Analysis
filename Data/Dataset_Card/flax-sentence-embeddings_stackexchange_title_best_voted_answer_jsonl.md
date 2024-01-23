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

### Data Splits

We provide multiple splits for this dataset, which each refers to a given community channel. We detail the number of pail for each split below:


|                            | Number of pairs   |
| -----                      | ------ | 
| gaming | 82,887 |
| dba | 71,449 |
| codereview | 41,748 |
| gis | 100,254 |
| english | 100,640 |
| mathoverflow | 85,289 |
| askubuntu | 267,135 |
| electronics | 129,494 |
| apple | 92,487 |
| diy | 52,896 |
| magento | 79,241 |
| gamedev | 40,154 |
| mathematica | 59,895 |
| ell | 77,892 |
| judaism | 26,085 |
| drupal | 67,817 |
| blender | 54,153 |
| biology | 19,277 |
| android | 38,077 |
| crypto | 19,404 |
| christianity | 11,498 |
| cs | 30,010 |
| academia | 32,137 |
| chemistry | 27,061 |
| aviation | 18,755 |
| history | 10,766 |
| japanese | 20,948 |
| cooking | 22,641 |
| law | 16,133 |
| hermeneutics | 9,516 |
| hinduism | 8,999 |
| graphicdesign | 28,083 |
| dsp | 17,430 |
| bicycles | 15,708 |
| ethereum | 26,124 |
| ja | 17,376 |
| arduino | 16,281 |
| bitcoin | 22,474 |
| islam | 10,052 |
| datascience | 20,503 |
| german | 13,733 |
| codegolf | 8,211 |
| boardgames | 11,805 |
| economics | 8,844 |
| emacs | 16,830 |
| buddhism | 6,787 |
| gardening | 13,246 |
| astronomy | 9,086 |
| anime | 10,131 |
| fitness | 8,297 |
| cstheory | 7,742 |
| engineering | 8,649 |
| chinese | 8,646 |
| linguistics | 6,843 |
| cogsci | 5,101 |
| french | 10,578 |
| literature | 3,539 |
| ai | 5,763 |
| craftcms | 11,236 |
| health | 4,494 |
| chess | 6,392 |
| interpersonal | 3,398 |
| expressionengine | 10,742 |
| earthscience | 4,396 |
| civicrm | 10,648 |
| joomla | 5,887 |
| homebrew | 5,608 |
| latin | 3,969 |
| ham | 3,501 |
| hsm | 2,517 |
| avp | 6,450 |
| expatriates | 4,913 |
| matheducators | 2,706 |
| genealogy | 2,895 |
| 3dprinting | 3,488 |
| devops | 3,462 |
| bioinformatics | 3,135 |
| computergraphics | 2,306 |
| elementaryos | 5,917 |
| martialarts | 1,737 |
| hardwarerecs | 2,050 |
| lifehacks | 2,576 |
| crafts | 1,659 |
| italian | 3,101 |
| freelancing | 1,663 |
| materials | 1,101 |
| bricks | 3,530 |
| cseducators | 902 |
| eosio | 1,940 |
| iot | 1,359 |
| languagelearning | 948 |
| beer | 1,012 |
| ebooks | 1,107 |
| coffee | 1,188 |
| esperanto | 1,466 |
| korean | 1,406 |
| cardano | 248 |
| conlang | 334 |
| drones | 496 |
| iota | 775 |
| salesforce | 87,272 |
| wordpress | 83,621 |
| rpg | 40,435 |
| scifi | 54,805 |
| stats | 115,679 |
| serverfault | 238,507 |
| physics | 141,230 |
| sharepoint | 80,420 |
| security | 51,355 |
| worldbuilding | 26,210 |
| softwareengineering | 51,326 |
| superuser | 352,610 |
| meta | 1,000 |
| money | 29,404 |
| travel | 36,533 |
| photo | 23,204 |
| webmasters | 30,370 |
| workplace | 24,012 |
| ux | 28,901 |
| philosophy | 13,114 |
| music | 19,936 |
| politics | 11,047 |
| movies | 18,243 |
| space | 12,893 |
| skeptics | 8,145 |
| raspberrypi | 24,143 |
| rus | 16,528 |
| puzzling | 17,448 |
| webapps | 24,867 |
| mechanics | 18,613 |
| writers | 9,867 |
| networkengineering | 12,590 |
| parenting | 5,998 |
| softwarerecs | 11,761 |
| quant | 12,933 |
| spanish | 7,675 |
| scicomp | 7,036 |
| pets | 6,156 |
| sqa | 9,256 |
| sitecore | 7,838 |
| vi | 9,000 |
| outdoors | 5,278 |
| sound | 8,303 |
| pm | 5,435 |
| reverseengineering | 5,817 |
| retrocomputing | 3,907 |
| tridion | 5,907 |
| quantumcomputing | 4,320 |
| sports | 4,707 |
| robotics | 4,648 |
| russian | 3,937 |
| opensource | 3,221 |
| woodworking | 2,955 |
| ukrainian | 1,767 |
| opendata | 3,842 |
| patents | 3,573 |
| mythology | 1,595 |
| portuguese | 1,964 |
| tor | 4,167 |
| monero | 3,508 |
| sustainability | 1,674 |
| musicfans | 2,431 |
| poker | 1,665 |
| or | 1,490 |
| windowsphone | 2,807 |
| stackapps | 1,518 |
| moderators | 504 |
| vegetarianism | 585 |
| tezos | 1,169 |
| stellar | 1,078 |
| pt | 103,277 |
| unix | 155,414 |
| tex | 171,628 |
| ru | 253,289 |
| total | 4,750,619 |

## Dataset Creation

### Curation Rationale

We primary designed this dataset for sentence embeddings training. Indeed sentence embeddings may be trained using a contrastive learning setup for which the model is trained to associate each sentence with its corresponding pair out of multiple proposition. Such models require many examples to be efficient and thus the dataset creation may be tedious. Community networks such as Stack Exchange allow us to build many examples semi-automatically.

### Source Data

The source data are dumps from [Stack Exchange](https://archive.org/details/stackexchange)

#### Initial Data Collection and Normalization

We collected the data from the math community. 

We filtered out questions which title or body length is bellow 20 characters and questions for which body length is above 4096 characters.

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