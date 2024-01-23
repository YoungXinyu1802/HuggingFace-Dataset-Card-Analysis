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
{'title_body': 'How to determine if 3 points on a 3-D graph are collinear? Let the points $A, B$ and $C$ be $(x_1, y_1, z_1), (x_2, y_2, z_2)$ and $(x_3, y_3, z_3)$ respectively. How do I prove that the 3 points are collinear? What is the formula?',
 'upvoted_answer': 'From $A(x_1,y_1,z_1),B(x_2,y_2,z_2),C(x_3,y_3,z_3)$ we can get their position vectors.\n\n$\\vec{AB}=(x_2-x_1,y_2-y_1,z_2-z_1)$ and $\\vec{AC}=(x_3-x_1,y_3-y_1,z_3-z_1)$.\n\nThen $||\\vec{AB}\\times\\vec{AC}||=0\\implies A,B,C$ collinear.',
```

This particular exampe corresponds to the [following page](https://math.stackexchange.com/questions/947555/how-to-determine-if-3-points-on-a-3-d-graph-are-collinear)

### Data Fields

The fields present in the dataset contain the following informations:

- `title_body`: This is the concatenation of the title and body from the question
- `upvoted_answer`: This is the body from the most upvoted answer

### Data Splits

We provide multiple splits for this dataset, which each refers to a given community channel. We detail the number of pail for each split below:


|                            | Number of pairs   |
| -----                      | ------ | 
| apple | 92,487 |
| english | 100,640 |
| codereview | 41,748 |
| dba | 71,449 |
| mathoverflow | 85,289 |
| electronics | 129,494 |
| mathematica | 59,895 |
| drupal | 67,817 |
| magento | 79,241 |
| gaming | 82,887 |
| ell | 77,892 |
| gamedev | 40,154 |
| gis | 100,254 |
| askubuntu | 267,135 |
| diy | 52,896 |
| academia | 32,137 |
| blender | 54,153 |
| cs | 30,010 |
| chemistry | 27,061 |
| judaism | 26,085 |
| crypto | 19,404 |
| android | 38,077 |
| ja | 17,376 |
| christianity | 11,498 |
| graphicdesign | 28,083 |
| aviation | 18,755 |
| ethereum | 26,124 |
| biology | 19,277 |
| datascience | 20,503 |
| law | 16,133 |
| dsp | 17,430 |
| japanese | 20,948 |
| hermeneutics | 9,516 |
| bicycles | 15,708 |
| arduino | 16,281 |
| history | 10,766 |
| bitcoin | 22,474 |
| cooking | 22,641 |
| hinduism | 8,999 |
| codegolf | 8,211 |
| boardgames | 11,805 |
| emacs | 16,830 |
| economics | 8,844 |
| gardening | 13,246 |
| astronomy | 9,086 |
| islam | 10,052 |
| german | 13,733 |
| fitness | 8,297 |
| french | 10,578 |
| anime | 10,131 |
| craftcms | 11,236 |
| cstheory | 7,742 |
| engineering | 8,649 |
| buddhism | 6,787 |
| linguistics | 6,843 |
| ai | 5,763 |
| expressionengine | 10,742 |
| cogsci | 5,101 |
| chinese | 8,646 |
| chess | 6,392 |
| civicrm | 10,648 |
| literature | 3,539 |
| interpersonal | 3,398 |
| health | 4,494 |
| avp | 6,450 |
| earthscience | 4,396 |
| joomla | 5,887 |
| homebrew | 5,608 |
| expatriates | 4,913 |
| latin | 3,969 |
| matheducators | 2,706 |
| ham | 3,501 |
| genealogy | 2,895 |
| 3dprinting | 3,488 |
| elementaryos | 5,917 |
| bioinformatics | 3,135 |
| devops | 3,462 |
| hsm | 2,517 |
| italian | 3,101 |
| computergraphics | 2,306 |
| martialarts | 1,737 |
| bricks | 3,530 |
| freelancing | 1,663 |
| crafts | 1,659 |
| lifehacks | 2,576 |
| cseducators | 902 |
| materials | 1,101 |
| hardwarerecs | 2,050 |
| iot | 1,359 |
| eosio | 1,940 |
| languagelearning | 948 |
| korean | 1,406 |
| coffee | 1,188 |
| esperanto | 1,466 |
| beer | 1,012 |
| ebooks | 1,107 |
| iota | 775 |
| cardano | 248 |
| drones | 496 |
| conlang | 334 |
| pt | 103,277 |
| stats | 115,679 |
| unix | 155,414 |
| physics | 141,230 |
| tex | 171,628 |
| serverfault | 238,507 |
| salesforce | 87,272 |
| wordpress | 83,621 |
| softwareengineering | 51,326 |
| scifi | 54,805 |
| security | 51,355 |
| ru | 253,289 |
| superuser | 352,610 |
| sharepoint | 80,420 |
| rpg | 40,435 |
| travel | 36,533 |
| worldbuilding | 26,210 |
| meta | 1,000 |
| workplace | 24,012 |
| ux | 28,901 |
| money | 29,404 |
| webmasters | 30,370 |
| raspberrypi | 24,143 |
| photo | 23,204 |
| music | 19,936 |
| philosophy | 13,114 |
| puzzling | 17,448 |
| movies | 18,243 |
| quant | 12,933 |
| politics | 11,047 |
| space | 12,893 |
| mechanics | 18,613 |
| skeptics | 8,145 |
| rus | 16,528 |
| writers | 9,867 |
| webapps | 24,867 |
| softwarerecs | 11,761 |
| networkengineering | 12,590 |
| parenting | 5,998 |
| scicomp | 7,036 |
| sqa | 9,256 |
| sitecore | 7,838 |
| vi | 9,000 |
| spanish | 7,675 |
| pm | 5,435 |
| pets | 6,156 |
| sound | 8,303 |
| reverseengineering | 5,817 |
| outdoors | 5,278 |
| tridion | 5,907 |
| retrocomputing | 3,907 |
| robotics | 4,648 |
| quantumcomputing | 4,320 |
| sports | 4,707 |
| russian | 3,937 |
| opensource | 3,221 |
| woodworking | 2,955 |
| patents | 3,573 |
| tor | 4,167 |
| ukrainian | 1,767 |
| opendata | 3,842 |
| monero | 3,508 |
| sustainability | 1,674 |
| portuguese | 1,964 |
| mythology | 1,595 |
| musicfans | 2,431 |
| or | 1,490 |
| poker | 1,665 |
| windowsphone | 2,807 |
| moderators | 504 |
| stackapps | 1,518 |
| stellar | 1,078 |
| vegetarianism | 585 |
| tezos | 1,169 |
| total | 4,750,619 |

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