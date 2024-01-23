---
language:
- ace
- bg
- da
- fur
- ilo
- lij
- mzn
- qu
- su
- vi
- af
- bh
- de
- fy
- io
- lmo
- nap
- rm
- sv
- vls
- als
- bn
- diq
- ga
- is
- ln
- nds
- ro
- sw
- vo
- am
- bo
- dv
- gan
- it
- lt
- ne
- ru
- szl
- wa
- an
- br
- el
- gd
- ja
- lv
- nl
- rw
- ta
- war
- ang
- bs
- eml
- gl
- jbo
- nn
- sa
- te
- wuu
- ar
- ca
- en
- gn
- jv
- mg
- no
- sah
- tg
- xmf
- arc
- eo
- gu
- ka
- mhr
- nov
- scn
- th
- yi
- arz
- cdo
- es
- hak
- kk
- mi
- oc
- sco
- tk
- yo
- as
- ce
- et
- he
- km
- min
- or
- sd
- tl
- zea
- ast
- ceb
- eu
- hi
- kn
- mk
- os
- sh
- tr
- ay
- ckb
- ext
- hr
- ko
- ml
- pa
- si
- tt
- az
- co
- fa
- hsb
- ksh
- mn
- pdc
- ug
- ba
- crh
- fi
- hu
- ku
- mr
- pl
- sk
- uk
- zh
- bar
- cs
- hy
- ky
- ms
- pms
- sl
- ur
- csb
- fo
- ia
- la
- mt
- pnb
- so
- uz
- cv
- fr
- id
- lb
- mwl
- ps
- sq
- vec
- be
- cy
- frr
- ig
- li
- my
- pt
- sr
multilinguality:
- multilingual
size_categories:
- 10K<100k
task_categories:
- token-classification
task_ids:
- named-entity-recognition
pretty_name: WikiAnn
---

# Dataset Card for "tner/wikiann"

## Dataset Description

- **Repository:** [T-NER](https://github.com/asahi417/tner)
- **Paper:** [https://aclanthology.org/P17-1178/](https://aclanthology.org/P17-1178/)
- **Dataset:** WikiAnn
- **Domain:** Wikipedia
- **Number of Entity:** 3


### Dataset Summary
WikiAnn NER dataset formatted in a part of [TNER](https://github.com/asahi417/tner) project.
- Entity Types: `LOC`, `ORG`, `PER`

## Dataset Structure

### Data Instances
An example of `train` of `ja` looks as follows.

```
{
  'tokens': ['#', '#', 'ユ', 'リ', 'ウ', 'ス', '・', 'ベ', 'ー', 'リ', 'ッ', 'ク', '#', '1', '9','9','9'],
  'tags': [6, 6, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6]
}
```

### Label ID
The label2id dictionary can be found at [here](https://huggingface.co/datasets/tner/wikiann/raw/main/dataset/label.json).
```python
{
    "B-LOC": 0,
    "B-ORG": 1,
    "B-PER": 2,
    "I-LOC": 3,
    "I-ORG": 4,
    "I-PER": 5,
    "O": 6
}
```

### Data Splits

| language     |   train |   validation |   test |
|:-------------|--------:|-------------:|-------:|
| ace          |     100 |          100 |    100 |
| bg           |   20000 |        10000 |  10000 |
| da           |   20000 |        10000 |  10000 |
| fur          |     100 |          100 |    100 |
| ilo          |     100 |          100 |    100 |
| lij          |     100 |          100 |    100 |
| mzn          |     100 |          100 |    100 |
| qu           |     100 |          100 |    100 |
| su           |     100 |          100 |    100 |
| vi           |   20000 |        10000 |  10000 |
| af           |    5000 |         1000 |   1000 |
| bh           |     100 |          100 |    100 |
| de           |   20000 |        10000 |  10000 |
| fy           |    1000 |         1000 |   1000 |
| io           |     100 |          100 |    100 |
| lmo          |     100 |          100 |    100 |
| nap          |     100 |          100 |    100 |
| rm           |     100 |          100 |    100 |
| sv           |   20000 |        10000 |  10000 |
| vls          |     100 |          100 |    100 |
| als          |     100 |          100 |    100 |
| bn           |   10000 |         1000 |   1000 |
| diq          |     100 |          100 |    100 |
| ga           |    1000 |         1000 |   1000 |
| is           |    1000 |         1000 |   1000 |
| ln           |     100 |          100 |    100 |
| nds          |     100 |          100 |    100 |
| ro           |   20000 |        10000 |  10000 |
| sw           |    1000 |         1000 |   1000 |
| vo           |     100 |          100 |    100 |
| am           |     100 |          100 |    100 |
| bo           |     100 |          100 |    100 |
| dv           |     100 |          100 |    100 |
| gan          |     100 |          100 |    100 |
| it           |   20000 |        10000 |  10000 |
| lt           |   10000 |        10000 |  10000 |
| ne           |     100 |          100 |    100 |
| ru           |   20000 |        10000 |  10000 |
| szl          |     100 |          100 |    100 |
| wa           |     100 |          100 |    100 |
| an           |    1000 |         1000 |   1000 |
| br           |    1000 |         1000 |   1000 |
| el           |   20000 |        10000 |  10000 |
| gd           |     100 |          100 |    100 |
| ja           |   20000 |        10000 |  10000 |
| lv           |   10000 |        10000 |  10000 |
| nl           |   20000 |        10000 |  10000 |
| rw           |     100 |          100 |    100 |
| ta           |   15000 |         1000 |   1000 |
| war          |     100 |          100 |    100 |
| ang          |     100 |          100 |    100 |
| bs           |   15000 |         1000 |   1000 |
| eml          |     100 |          100 |    100 |
| gl           |   15000 |        10000 |  10000 |
| jbo          |     100 |          100 |    100 |
| map-bms      |     100 |          100 |    100 |
| nn           |   20000 |         1000 |   1000 |
| sa           |     100 |          100 |    100 |
| te           |    1000 |         1000 |   1000 |
| wuu          |     100 |          100 |    100 |
| ar           |   20000 |        10000 |  10000 |
| ca           |   20000 |        10000 |  10000 |
| en           |   20000 |        10000 |  10000 |
| gn           |     100 |          100 |    100 |
| jv           |     100 |          100 |    100 |
| mg           |     100 |          100 |    100 |
| no           |   20000 |        10000 |  10000 |
| sah          |     100 |          100 |    100 |
| tg           |     100 |          100 |    100 |
| xmf          |     100 |          100 |    100 |
| arc          |     100 |          100 |    100 |
| cbk-zam      |     100 |          100 |    100 |
| eo           |   15000 |        10000 |  10000 |
| gu           |     100 |          100 |    100 |
| ka           |   10000 |        10000 |  10000 |
| mhr          |     100 |          100 |    100 |
| nov          |     100 |          100 |    100 |
| scn          |     100 |          100 |    100 |
| th           |   20000 |        10000 |  10000 |
| yi           |     100 |          100 |    100 |
| arz          |     100 |          100 |    100 |
| cdo          |     100 |          100 |    100 |
| es           |   20000 |        10000 |  10000 |
| hak          |     100 |          100 |    100 |
| kk           |    1000 |         1000 |   1000 |
| mi           |     100 |          100 |    100 |
| oc           |     100 |          100 |    100 |
| sco          |     100 |          100 |    100 |
| tk           |     100 |          100 |    100 |
| yo           |     100 |          100 |    100 |
| as           |     100 |          100 |    100 |
| ce           |     100 |          100 |    100 |
| et           |   15000 |        10000 |  10000 |
| he           |   20000 |        10000 |  10000 |
| km           |     100 |          100 |    100 |
| min          |     100 |          100 |    100 |
| or           |     100 |          100 |    100 |
| sd           |     100 |          100 |    100 |
| tl           |   10000 |         1000 |   1000 |
| zea          |     100 |          100 |    100 |
| ast          |    1000 |         1000 |   1000 |
| ceb          |     100 |          100 |    100 |
| eu           |   10000 |        10000 |  10000 |
| hi           |    5000 |         1000 |   1000 |
| kn           |     100 |          100 |    100 |
| mk           |   10000 |         1000 |   1000 |
| os           |     100 |          100 |    100 |
| sh           |   20000 |        10000 |  10000 |
| tr           |   20000 |        10000 |  10000 |
| zh-classical |     100 |          100 |    100 |
| ay           |     100 |          100 |    100 |
| ckb          |    1000 |         1000 |   1000 |
| ext          |     100 |          100 |    100 |
| hr           |   20000 |        10000 |  10000 |
| ko           |   20000 |        10000 |  10000 |
| ml           |   10000 |         1000 |   1000 |
| pa           |     100 |          100 |    100 |
| si           |     100 |          100 |    100 |
| tt           |    1000 |         1000 |   1000 |
| zh-min-nan   |     100 |          100 |    100 |
| az           |   10000 |         1000 |   1000 |
| co           |     100 |          100 |    100 |
| fa           |   20000 |        10000 |  10000 |
| hsb          |     100 |          100 |    100 |
| ksh          |     100 |          100 |    100 |
| mn           |     100 |          100 |    100 |
| pdc          |     100 |          100 |    100 |
| simple       |   20000 |         1000 |   1000 |
| ug           |     100 |          100 |    100 |
| zh-yue       |   20000 |        10000 |  10000 |
| ba           |     100 |          100 |    100 |
| crh          |     100 |          100 |    100 |
| fi           |   20000 |        10000 |  10000 |
| hu           |   20000 |        10000 |  10000 |
| ku           |     100 |          100 |    100 |
| mr           |    5000 |         1000 |   1000 |
| pl           |   20000 |        10000 |  10000 |
| sk           |   20000 |        10000 |  10000 |
| uk           |   20000 |        10000 |  10000 |
| zh           |   20000 |        10000 |  10000 |
| bar          |     100 |          100 |    100 |
| cs           |   20000 |        10000 |  10000 |
| fiu-vro      |     100 |          100 |    100 |
| hy           |   15000 |         1000 |   1000 |
| ky           |     100 |          100 |    100 |
| ms           |   20000 |         1000 |   1000 |
| pms          |     100 |          100 |    100 |
| sl           |   15000 |        10000 |  10000 |
| ur           |   20000 |         1000 |   1000 |
| bat-smg      |     100 |          100 |    100 |
| csb          |     100 |          100 |    100 |
| fo           |     100 |          100 |    100 |
| ia           |     100 |          100 |    100 |
| la           |    5000 |         1000 |   1000 |
| mt           |     100 |          100 |    100 |
| pnb          |     100 |          100 |    100 |
| so           |     100 |          100 |    100 |
| uz           |    1000 |         1000 |   1000 |
| be-x-old     |    5000 |         1000 |   1000 |
| cv           |     100 |          100 |    100 |
| fr           |   20000 |        10000 |  10000 |
| id           |   20000 |        10000 |  10000 |
| lb           |    5000 |         1000 |   1000 |
| mwl          |     100 |          100 |    100 |
| ps           |     100 |          100 |    100 |
| sq           |    5000 |         1000 |   1000 |
| vec          |     100 |          100 |    100 |
| be           |   15000 |         1000 |   1000 |
| cy           |   10000 |         1000 |   1000 |
| frr          |     100 |          100 |    100 |
| ig           |     100 |          100 |    100 |
| li           |     100 |          100 |    100 |
| my           |     100 |          100 |    100 |
| pt           |   20000 |        10000 |  10000 |
| sr           |   20000 |        10000 |  10000 |
| vep          |     100 |          100 |    100 |

### Citation Information

```
@inproceedings{pan-etal-2017-cross,
    title = "Cross-lingual Name Tagging and Linking for 282 Languages",
    author = "Pan, Xiaoman  and
      Zhang, Boliang  and
      May, Jonathan  and
      Nothman, Joel  and
      Knight, Kevin  and
      Ji, Heng",
    booktitle = "Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = jul,
    year = "2017",
    address = "Vancouver, Canada",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/P17-1178",
    doi = "10.18653/v1/P17-1178",
    pages = "1946--1958",
    abstract = "The ambitious goal of this work is to develop a cross-lingual name tagging and linking framework for 282 languages that exist in Wikipedia. Given a document in any of these languages, our framework is able to identify name mentions, assign a coarse-grained or fine-grained type to each mention, and link it to an English Knowledge Base (KB) if it is linkable. We achieve this goal by performing a series of new KB mining methods: generating {``}silver-standard{''} annotations by transferring annotations from English to other languages through cross-lingual links and KB properties, refining annotations through self-training and topic selection, deriving language-specific morphology features from anchor links, and mining word translation pairs from cross-lingual links. Both name tagging and linking results for 282 languages are promising on Wikipedia data and on-Wikipedia data.",
}
```