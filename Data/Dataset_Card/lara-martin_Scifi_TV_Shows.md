---
language_creators:
- found
language:
- en
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: Scifi_TV_Shows
size_categories:
- unknown
source_datasets:
- original
task_categories:
- other
task_ids:
- other-other-story-generation
tags:
  - Story Generation
paperswithcode_id: scifi-tv-plots
---

# Dataset Card for Science Fiction TV Show Plots Corpus

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Format](#format)
    - [Using the Dataset with Hugging Face](#call-scifi)
- [Original Dataset Structure](#dataset-structure)
  - [Files in _OriginalStoriesSeparated_ Directory](#original-stories)
- [Additional Information](#additional-information)
  - [Citation](#citation)
  - [Licensing](#licensing)
  
## Dataset Description
A collection of long-running (80+ episodes) science fiction TV show plot synopses, scraped from Fandom.com wikis. Collected Nov 2017. Each episode is considered a "story".

Contains plot summaries from: 
- Babylon 5 (https://babylon5.fandom.com/wiki/Main_Page) - 84 stories
- Doctor Who (https://tardis.fandom.com/wiki/Doctor_Who_Wiki) - 311 stories
- Doctor Who spin-offs - 95 stories
- Farscape (https://farscape.fandom.com/wiki/Farscape_Encyclopedia_Project:Main_Page) - 90 stories
- Fringe (https://fringe.fandom.com/wiki/FringeWiki) - 87 stories
- Futurama (https://futurama.fandom.com/wiki/Futurama_Wiki) - 87 stories
- Stargate (https://stargate.fandom.com/wiki/Stargate_Wiki) - 351 stories
- Star Trek (https://memory-alpha.fandom.com/wiki/Star_Trek) - 701 stories
- Star Wars books (https://starwars.fandom.com/wiki/Main_Page) - 205 stories, each book is a story
- Star Wars Rebels (https://starwarsrebels.fandom.com/wiki/Main_page) - 65 stories 
- X-Files (https://x-files.fandom.com/wiki/Main_Page) - 200 stories

Total: 2276 stories

Dataset is "eventified" and generalized (see LJ Martin, P Ammanabrolu, X Wang, W Hancock, S Singh, B Harrison, and MO Riedl. Event Representations for Automated Story Generation with Deep Neural Nets, Thirty-Second AAAI Conference on Artificial Intelligence (AAAI), 2018. for details on these processes.) and split into train-test-validation sets&mdash;separated by story so that full stories will stay together&mdash;for converting events into full sentences.

---
### Format
| Dataset Split | Number of Stories in Split | Number of Sentences in Split |
| ------------- |--------------------------- |----------------------------- |
| Train         | 1737                       | 257,108                      |
| Validation    | 194                        | 32,855                       |
| Test          | 450                        | 30,938                       |

#### Using the Dataset with Hugging Face
```
from datasets import load_dataset

#download and load the data
dataset = load_dataset('lara-martin/Scifi_TV_Shows') 
#you can then get the individual splits
train = dataset['train']
test = dataset['test']
validation = dataset['validation']
```
Each split has 7 attributes (explained in more detail in the next section):
```
>>> print(train)

 Dataset({
    features: ['story_num', 'story_line', 'event', 'gen_event', 'sent', 'gen_sent', 'entities'],
    num_rows: 257108
})
```

---
## Original Dataset Structure
* File names: scifi-val.txt, scifi-test.txt, & scifi-train.txt
* Each sentence of the stories are split into smaller sentences and the events are extracted.
* Each line of the file contains information about a single sentence, delimited by "|||". Each line contains, in order:
    * The story number
    * The line number (within the story)
    * 5-tuple events in a list (subject, verb, direct object, modifier noun, preposition); e.g., 
    ``
[[u'Voyager', u'run', 'EmptyParameter', u'deuterium', u'out'], [u'Voyager', u'force', u'go', 'EmptyParameter', 'EmptyParameter'], [u'Voyager', u'go', 'EmptyParameter', u'mode', u'into']]
    ``
    * generalized 5-tuple events in a list; events are generalized using WordNet and VerbNet; e.g., 
    ``
    [['<VESSEL>0', 'function-105.2.1', 'EmptyParameter', "Synset('atom.n.01')", u'out'], ['<VESSEL>0', 'urge-58.1-1', u'escape-51.1-1', 'EmptyParameter', 'EmptyParameter'], ['<VESSEL>0', u'escape-51.1-1', 'EmptyParameter', "Synset('statistic.n.01')", u'into']]
    ``
    * original sentence (These sentences are split to contain fewer events per sentence. For the full original sentence, see the OriginalStoriesSeparated directory.); e.g., 
    ``
    The USS Voyager is running out of deuterium as a fuel and is forced to go into Gray mode.
    ``
    * generalized sentence; only nouns are generalized (using WordNet); e.g., 
    ``
    the <VESSEL>0 is running out of Synset('atom.n.01') as a Synset('matter.n.03') and is forced to go into Synset('horse.n.01') Synset('statistic.n.01').
    ``
    * a dictionary of numbered entities by tag within the _entire story_ (e.g. the second entity in the "&lt;ORGANIZATION>" list in the dictionary would be &lt;ORGANIZATION>1 in the story above&mdash;index starts at 0); e.g., 
    ``
    {'<ORGANIZATION>': ['seven of nine', 'silver blood'], '<LOCATION>': ['sickbay', 'astrometrics', 'paris', 'cavern', 'vorik', 'caves'], '<DATE>': ['an hour ago', 'now'], '<MISC>': ['selected works', 'demon class', 'electromagnetic', 'parises', 'mimetic'], '<DURATION>': ['less than a week', 'the past four years', 'thirty seconds', 'an hour', 'two hours'], '<NUMBER>': ['two', 'dozen', '14', '15'], '<ORDINAL>': ['first'], '<PERSON>': ['tom paris', 'harry kim', 'captain kathryn janeway', 'tuvok', 'chakotay', 'jirex', 'neelix', 'the doctor', 'seven', 'ensign kashimuro nozawa', 'green', 'lt jg elanna torres', 'ensign vorik'], '<VESSEL>': ['uss voyager', 'starfleet']}
    ``

### Files in _OriginalStoriesSeparated_ Directory
* Contains unedited, unparsed original stories scraped from the respective Fandom wikis.
* Each line is a story with sentences space-separated. After each story, there is a &lt;EOS> tag on a new line.
* There is one file for each of the 11 domains listed above.
* These are currently not set up to be called through the Hugging Face API and must be extracted from the zip directly.
---
## Additional Information
### Citation
```
@inproceedings{Ammanabrolu2020AAAI, 
title={Story Realization: Expanding Plot Events into Sentences}, 
author={Prithviraj Ammanabrolu and Ethan Tien and Wesley Cheung and Zhaochen Luo and William Ma and Lara J. Martin and Mark O. Riedl}, 
journal={Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)}, 
year={2020}, 
volume={34},
number={05},
url={https://ojs.aaai.org//index.php/AAAI/article/view/6232}
}
```
---
### Licensing
The Creative Commons Attribution 4.0 International License. https://creativecommons.org/licenses/by/4.0/