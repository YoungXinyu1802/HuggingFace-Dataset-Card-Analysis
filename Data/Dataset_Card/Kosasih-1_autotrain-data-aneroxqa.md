---
language:
- en
- aa
- ab
- ae
- as
- av
- ar
- ay
- az
- ba
- be
- bh
- bg
- bi
- bm
- bn
- bo
- br
- bs
- ca
- ce
- ch
- co
- cr
- cs
- cu
- cv
- cy
- da
- de
- dv
- dz
- ee
- el
- eo
- es
- et
- eu
- fa
- ff
- fi
- fj
- fo
- fr
- fy
- ga
- gd
- gl
- gn
- gu
- gv
- ha
- he
- hi
- ho
- hr
- ht
- hu
- hy
- hz
- ia
- id
- ie
- ig
- ii
- ik
- io
- is
- it
- iu
- ja
- jv
- ka
- ki
- kg
- kj
- kk
- an
- kl
- km
- kn
- am
- ko
- af
- ak
- kr
- ks
- ky
- la
- lg
- li
- ln
- lb
- lo
- lu
- lv
- mg
- mh
- mi
- lt
- ml
- mk
- mr
- ms
- mt
- my
- na
- mn
- nb
- ne
- ng
- nl
- nn
- 'no'
- nd
- nv
- ady
- aed
- ase
- ach
- sq
- bem
- bzs
- bcl
- ber
- ceb
- swc
- chk
- csg
- csn
- cel
- crs
- zh
- ny
- kw
- kbd
- efi
- fon
- fse
- gil
- guw
- gaa
- hil
- zai
- ilo
- iso
- kqn
- kwy
- kwn
- kab
- rn
- kv
- ku
- rw
- luo
- lue
- lus
- loz
- lua
- lun
- mos
- mfe
- mfs
- nyk
- niu
- se
- nr
- nso
- os
- om
- oj
- oc
- or
- pt
- pag
- pap
- pis
- pon
- ps
- pl
- pi
- pa
- prl
- qu
- roa
- run
- ru
- ro
- rm
- rnd
- sk
- si
- sl
- sm
- sn
- so
- sr
- ss
- st
- zu
- sg
- sv
- sw
- srn
- ssp
- su
- sd
- sc
- sa
- sah
- ti
- tk
- tl
- tn
- to
- tr
- ts
- tt
- tw
- ty
- tll
- tvl
- toi
- tiv
- tpi
- tum
- tzo
- th
- tg
- te
- ta
- tdt
- umb
- ur
- uk
- uz
- ug
- vsl
- vo
- vi
- ve
- wal
- war
- wo
- wa
- wls
- xh
- yua
- yue
- yo
- yap
- yi
- zne
- za
license: mit
task_categories:
- question-answering
pretty_name: AneroxQa
size_categories:
- n>1T
---
# AutoTrain Dataset for project: aneroxqa

## Dataset Description

This dataset has been automatically processed by AutoTrain for project aneroxqa.

### Languages

The BCP-47 code for the dataset's language is en.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "context": "How can I deal with really bad morning sickness?",
    "question": "When does a woman experience morning sickness during pregnancy?",
    "answers.text": [
      "4"
    ],
    "answers.answer_start": [
      0
    ]
  },
  {
    "context": "How long after a aneurysm surgery do you have to stay off work?",
    "question": "What is the recovery time after undergoing surgery for an aneurysm?",
    "answers.text": [
      "5"
    ],
    "answers.answer_start": [
      1
    ]
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "context": "Value(dtype='string', id=None)",
  "question": "Value(dtype='string', id=None)",
  "answers.text": "Sequence(feature=Value(dtype='string', id=None), length=-1, id=None)",
  "answers.answer_start": "Sequence(feature=Value(dtype='int32', id=None), length=-1, id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 2438 |
| valid        | 610 |