---
annotations_creators:
- other
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
- ga
- hr 
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
license:
- cc-by-4.0
multilinguality:
- multilingual
paperswithcode_id: null
pretty_name: "EurlexResources: A Corpus Covering the Largest EURLEX Resources"
size_categories:
- 1M<n<10M
source_datasets:
- original
task_categories:
- fill-mask

---

# Dataset Card for EurlexResources: A Corpus Covering the Largest EURLEX Resources

## Table of Contents

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
    - [Annotations](#annotations)
    - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
    - [Social Impact of Dataset](#social-impact-of-dataset)
    - [Discussion of Biases](#discussion-of-biases)
    - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
    - [Dataset Curators](#dataset-curators)
    - [Licensing Information](#licensing-information)
    - [Citation Information](#citation-information)
    - [Contributions](#contributions)

## Dataset Description

- **Homepage:**
- **Repository:** [GitHub](https://github.com/JoelNiklaus/LegalDatasets/tree/main/pretrain/eurlex)
- **Paper:** 
- **Leaderboard:**
- **Point of Contact:** [Joel Niklaus](mailto:joel.niklaus.2@bfh.ch)

### Dataset Summary

This dataset contains large text resources (~179GB in total) from EURLEX that can be used for pretraining language models.

Use the dataset like this:
```python
from datasets import load_dataset
config = "de_caselaw" # {lang}_{resource}
dataset = load_dataset("joelito/eurlex_resources", config, split='train', streaming=True) 
```

### Supported Tasks and Leaderboards

The dataset supports the task of masked language modeling.

### Languages

The following languages are supported: bg, cs, da, de, el, en, es, et, fi, fr, ga, hr, hu, it, lt, lv, mt, nl, pl, pt, ro, sk, sl, sv

## Dataset Structure

### Data Instances

The file format is jsonl.xz and there is one split available ("train"). 
The following resource types are supported: caselaw, decision, directive, intagr, proposal, recommendation, regulation

More information about the resource types can be found here:
- Caselaw: [EU](https://eur-lex.europa.eu/collection/eu-law/eu-case-law.html)
- Decision: [EU](https://eur-lex.europa.eu/EN/legal-content/summary/european-union-decisions.html), [Wikipedia](https://en.wikipedia.org/wiki/Decision_(European_Union))
- Directive: [EU](https://european-union.europa.eu/institutions-law-budget/law/types-legislation_en), [Wikipedia](https://en.wikipedia.org/wiki/Directive_(European_Union))
- Recommendation: [EU](https://eur-lex.europa.eu/EN/legal-content/glossary/recommendation.html), [Wikipedia](https://en.wikipedia.org/wiki/Recommendation_(European_Union))
- Regulation: [EU](https://european-union.europa.eu/institutions-law-budget/law/types-legislation_en), [Wikipedia](https://en.wikipedia.org/wiki/Regulation_(European_Union))
- Intagr: [EU](https://eur-lex.europa.eu/collection/eu-law/inter-agree.html), [Wikipedia](https://en.wikipedia.org/wiki/Treaties_of_the_European_Union)
- Proposal: No resource found


| Language   | Source         |   Size (MB) |      Tokens |   Documents |   Tokens/Document |
|:-----------|:---------------|------------:|------------:|------------:|------------------:|
| all        | all            |      176558 | 21526462547 |     8267651 |              2603 |
| all        | caselaw        |       32320 |  5465831562 |     2428444 |              2250 |
| all        | decision       |       27974 |  3054210877 |     1267253 |              2410 |
| all        | directive      |        4689 |   682257277 |      103020 |              6622 |
| all        | intagr         |       11264 |  1360585785 |      271055 |              5019 |
| all        | proposal       |       26526 |  3801600560 |      702392 |              5412 |
| all        | recommendation |        1886 |   293127733 |       80277 |              3651 |
| all        | regulation     |       71899 |  6868848753 |     3415210 |              2011 |
| bg         | all            |        7819 |   683675086 |      348691 |              1960 |
| bg         | caselaw        |        1588 |   179453583 |      104434 |              1718 |
| bg         | decision       |        1248 |   102781999 |       54075 |              1900 |
| bg         | directive      |         263 |    28004882 |        4388 |              6382 |
| bg         | intagr         |         603 |    54294524 |       11581 |              4688 |
| bg         | proposal       |        1083 |   103035900 |       29251 |              3522 |
| bg         | recommendation |          89 |     9061227 |        3321 |              2728 |
| bg         | regulation     |        2943 |   207042971 |      141641 |              1461 |
| cs         | all            |        8360 |   934087127 |      449793 |              2076 |
| cs         | caselaw        |        1163 |   208895704 |      104519 |              1998 |
| cs         | decision       |        1102 |   114330830 |       54075 |              2114 |
| cs         | directive      |         186 |    28119441 |        4388 |              6408 |
| cs         | intagr         |         449 |    55008615 |       11581 |              4749 |
| cs         | proposal       |         840 |   121367313 |       29252 |              4149 |
| cs         | recommendation |          64 |    10216343 |        3323 |              3074 |
| cs         | regulation     |        4557 |   396148881 |      242655 |              1632 |
| da         | all            |        7676 |   927426056 |      303594 |              3054 |
| da         | caselaw        |         491 |    46535791 |       59328 |               784 |
| da         | decision       |        1356 |   161197980 |       54085 |              2980 |
| da         | directive      |         207 |    32246780 |        4388 |              7348 |
| da         | intagr         |         506 |    64738297 |       11582 |              5589 |
| da         | proposal       |        1399 |   213540972 |       29257 |              7298 |
| da         | recommendation |         100 |    16169558 |        3352 |              4823 |
| da         | regulation     |        3618 |   392996678 |      141602 |              2775 |
| de         | all            |        9607 |  1259810918 |      348290 |              3617 |
| de         | caselaw        |        1930 |   337759616 |      104228 |              3240 |
| de         | decision       |        1449 |   169687102 |       53980 |              3143 |
| de         | directive      |         218 |    32100715 |        4385 |              7320 |
| de         | intagr         |         531 |    67188513 |       11580 |              5802 |
| de         | proposal       |        1556 |   227441945 |       29219 |              7784 |
| de         | recommendation |         109 |    16914583 |        3318 |              5097 |
| de         | regulation     |        3813 |   408718444 |      141580 |              2886 |
| el         | all            |       12469 |  1378107391 |      349667 |              3941 |
| el         | caselaw        |        2951 |   386130014 |      105138 |              3672 |
| el         | decision       |        1823 |   182486411 |       54150 |              3370 |
| el         | directive      |         321 |    38513818 |        4390 |              8773 |
| el         | intagr         |         701 |    77738992 |       11584 |              6710 |
| el         | proposal       |        2085 |   251594184 |       29290 |              8589 |
| el         | recommendation |         145 |    17742091 |        3357 |              5285 |
| el         | regulation     |        4443 |   423901881 |      141758 |              2990 |
| en         | all            |        9217 |  1161691945 |      348641 |              3332 |
| en         | caselaw        |        1846 |   316782142 |      104422 |              3033 |
| en         | decision       |        1504 |   176469698 |       54054 |              3264 |
| en         | directive      |         204 |    28841387 |        4388 |              6572 |
| en         | intagr         |         499 |    60504759 |       11581 |              5224 |
| en         | proposal       |        1538 |   209851759 |       29242 |              7176 |
| en         | recommendation |          97 |    14694658 |        3320 |              4426 |
| en         | regulation     |        3530 |   354547542 |      141634 |              2503 |
| es         | all            |        8588 |  1077415710 |      348443 |              3092 |
| es         | caselaw        |        1870 |   312501137 |      104312 |              2995 |
| es         | decision       |        1334 |   147730710 |       54001 |              2735 |
| es         | directive      |         221 |    31679902 |        4385 |              7224 |
| es         | intagr         |         516 |    64131203 |       11581 |              5537 |
| es         | proposal       |        1366 |   197060809 |       29224 |              6743 |
| es         | recommendation |          82 |    12355655 |        3319 |              3722 |
| es         | regulation     |        3199 |   311956294 |      141621 |              2202 |
| et         | all            |        6090 |   712559412 |      349615 |              2038 |
| et         | caselaw        |        1074 |   188899781 |      105111 |              1797 |
| et         | decision       |        1069 |   107752981 |       54159 |              1989 |
| et         | directive      |         177 |    25983417 |        4390 |              5918 |
| et         | intagr         |         436 |    51558677 |       11584 |              4450 |
| et         | proposal       |         810 |   114597516 |       29283 |              3913 |
| et         | recommendation |          61 |     9717239 |        3355 |              2896 |
| et         | regulation     |        2464 |   214049801 |      141733 |              1510 |
| fi         | all            |        7346 |   926601752 |      349633 |              2650 |
| fi         | caselaw        |        1596 |   280391862 |      105119 |              2667 |
| fi         | decision       |        1227 |   133158370 |       54163 |              2458 |
| fi         | directive      |         204 |    30439964 |        4389 |              6935 |
| fi         | intagr         |         463 |    56305341 |       11584 |              4860 |
| fi         | proposal       |        1075 |   161285908 |       29288 |              5506 |
| fi         | recommendation |          73 |    11623296 |        3356 |              3463 |
| fi         | regulation     |        2707 |   253397011 |      141734 |              1787 |
| fr         | all            |        9937 |  1383610076 |      348295 |              3972 |
| fr         | caselaw        |        2158 |   400304923 |      104228 |              3840 |
| fr         | decision       |        1473 |   182025567 |       53981 |              3372 |
| fr         | directive      |         222 |    34239059 |        4385 |              7808 |
| fr         | intagr         |         536 |    71340724 |       11580 |              6160 |
| fr         | proposal       |        1592 |   245293973 |       29218 |              8395 |
| fr         | recommendation |         112 |    18413965 |        3318 |              5549 |
| fr         | regulation     |        3845 |   431991865 |      141585 |              3051 |
| ga         | all            |        1028 |   129394560 |      349778 |               369 |
| ga         | caselaw        |          11 |     1322015 |      105205 |                12 |
| ga         | decision       |          87 |     9132798 |       54189 |               168 |
| ga         | directive      |          18 |     2881950 |        4390 |               656 |
| ga         | intagr         |          19 |     3544433 |       11586 |               305 |
| ga         | proposal       |         289 |    51138741 |       29298 |              1745 |
| ga         | recommendation |          10 |     1770503 |        3361 |               526 |
| ga         | regulation     |         594 |    59604120 |      141749 |               420 |
| hr         | all            |        4594 |   479668409 |      348691 |              1375 |
| hr         | caselaw        |         617 |   108134448 |      104434 |              1035 |
| hr         | decision       |         596 |    61443063 |       54075 |              1136 |
| hr         | directive      |         156 |    19255268 |        4388 |              4388 |
| hr         | intagr         |         450 |    44372755 |       11581 |              3831 |
| hr         | proposal       |         552 |    60718165 |       29251 |              2075 |
| hr         | recommendation |          40 |     6313739 |        3321 |              1901 |
| hr         | regulation     |        2183 |   179430971 |      141641 |              1266 |
| hu         | all            |        6653 |   744676866 |      349605 |              2130 |
| hu         | caselaw        |        1278 |   206954585 |      105144 |              1968 |
| hu         | decision       |        1147 |   112655714 |       54156 |              2080 |
| hu         | directive      |         200 |    27421410 |        4389 |              6247 |
| hu         | intagr         |         470 |    54481362 |       11586 |              4702 |
| hu         | proposal       |         912 |   120493483 |       29291 |              4113 |
| hu         | recommendation |          70 |    10294766 |        3357 |              3066 |
| hu         | regulation     |        2576 |   212375546 |      141682 |              1498 |
| it         | all            |        8222 |   963423333 |      303187 |              3177 |
| it         | caselaw        |         526 |    46071081 |       59116 |               779 |
| it         | decision       |        1445 |   166154664 |       53983 |              3077 |
| it         | directive      |         217 |    31786252 |        4385 |              7248 |
| it         | intagr         |         528 |    66036352 |       11580 |              5702 |
| it         | proposal       |        1533 |   224727845 |       29218 |              7691 |
| it         | recommendation |         109 |    16724986 |        3318 |              5040 |
| it         | regulation     |        3865 |   411922153 |      141587 |              2909 |
| lt         | all            |        4909 |   590271724 |      220817 |              2673 |
| lt         | caselaw        |        1137 |   202588185 |      105477 |              1920 |
| lt         | decision       |         551 |    53711077 |       21841 |              2459 |
| lt         | directive      |          88 |    13428712 |        2072 |              6481 |
| lt         | intagr         |         294 |    33148829 |        4051 |              8182 |
| lt         | proposal       |         850 |   121316064 |       29272 |              4144 |
| lt         | recommendation |          64 |    10187341 |        3363 |              3029 |
| lt         | regulation     |        1926 |   155891516 |       54741 |              2847 |
| lv         | all            |        6349 |   752446195 |      349919 |              2150 |
| lv         | caselaw        |        1153 |   205473532 |      105242 |              1952 |
| lv         | decision       |        1103 |   112930883 |       54224 |              2082 |
| lv         | directive      |         186 |    27612314 |        4392 |              6286 |
| lv         | intagr         |         452 |    54724543 |       11630 |              4705 |
| lv         | proposal       |         846 |   120571107 |       29298 |              4115 |
| lv         | recommendation |          64 |    10221637 |        3361 |              3041 |
| lv         | regulation     |        2545 |   220912179 |      141772 |              1558 |
| mt         | all            |        6540 |  1141585121 |      350292 |              3258 |
| mt         | caselaw        |        1164 |   320156230 |      105479 |              3035 |
| mt         | decision       |        1109 |   161249825 |       54280 |              2970 |
| mt         | directive      |         203 |    45493266 |        4392 |             10358 |
| mt         | intagr         |         470 |    79787487 |       11675 |              6834 |
| mt         | proposal       |         878 |   192699148 |       29274 |              6582 |
| mt         | recommendation |          65 |    16698859 |        3363 |              4965 |
| mt         | regulation     |        2650 |   325500306 |      141829 |              2295 |
| nl         | all            |        9586 |  1317883702 |      349407 |              3771 |
| nl         | caselaw        |        1847 |   338694761 |      105005 |              3225 |
| nl         | decision       |        1456 |   178362332 |       54152 |              3293 |
| nl         | directive      |         217 |    33850801 |        4388 |              7714 |
| nl         | intagr         |         529 |    70124352 |       11584 |              6053 |
| nl         | proposal       |        1540 |   239464702 |       29279 |              8178 |
| nl         | recommendation |         111 |    18213240 |        3355 |              5428 |
| nl         | regulation     |        3886 |   439173514 |      141644 |              3100 |
| pl         | all            |        6677 |   780658463 |      350349 |              2228 |
| pl         | caselaw        |        1231 |   212977774 |      105479 |              2019 |
| pl         | decision       |        1125 |   115926181 |       54287 |              2135 |
| pl         | directive      |         197 |    29102885 |        4392 |              6626 |
| pl         | intagr         |         466 |    55384447 |       11680 |              4741 |
| pl         | proposal       |         886 |   125097572 |       29317 |              4267 |
| pl         | recommendation |          68 |    10633172 |        3363 |              3161 |
| pl         | regulation     |        2703 |   231536432 |      141831 |              1632 |
| pt         | all            |        8450 |  1075496120 |      348449 |              3086 |
| pt         | caselaw        |        1763 |   303574704 |      104312 |              2910 |
| pt         | decision       |        1327 |   148950694 |       54007 |              2757 |
| pt         | directive      |         217 |    31807446 |        4385 |              7253 |
| pt         | intagr         |         504 |    61127624 |       11581 |              5278 |
| pt         | proposal       |        1361 |   200827190 |       29224 |              6871 |
| pt         | recommendation |          81 |    12520469 |        3319 |              3772 |
| pt         | regulation     |        3197 |   316687993 |      141621 |              2236 |
| ro         | all            |        6315 |   713047860 |      350300 |              2035 |
| ro         | caselaw        |        1110 |   187613531 |      105516 |              1778 |
| ro         | decision       |        1047 |   103349951 |       54281 |              1903 |
| ro         | directive      |         206 |    27651600 |        4392 |              6295 |
| ro         | intagr         |         481 |    54663108 |       11675 |              4682 |
| ro         | proposal       |         805 |   106000393 |       29274 |              3620 |
| ro         | recommendation |          63 |     9634151 |        3363 |              2864 |
| ro         | regulation     |        2603 |   224135126 |      141799 |              1580 |
| sk         | all            |        6484 |   763317735 |      350570 |              2177 |
| sk         | caselaw        |        1160 |   205490717 |      105608 |              1945 |
| sk         | decision       |        1111 |   114735132 |       54349 |              2111 |
| sk         | directive      |         188 |    27728158 |        4393 |              6311 |
| sk         | intagr         |         458 |    54700961 |       11676 |              4684 |
| sk         | proposal       |         859 |   123177145 |       29290 |              4205 |
| sk         | recommendation |          66 |    10522604 |        3364 |              3128 |
| sk         | regulation     |        2642 |   226963018 |      141890 |              1599 |
| sl         | all            |        6222 |   719535411 |      350574 |              2052 |
| sl         | caselaw        |        1071 |   192339474 |      105608 |              1821 |
| sl         | decision       |        1075 |   108465814 |       54349 |              1995 |
| sl         | directive      |         176 |    25833250 |        4393 |              5880 |
| sl         | intagr         |         441 |    51487014 |       11676 |              4409 |
| sl         | proposal       |         812 |   114959046 |       29290 |              3924 |
| sl         | recommendation |          62 |     9802044 |        3364 |              2913 |
| sl         | regulation     |        2585 |   216648769 |      141894 |              1526 |
| sv         | all            |        7419 |   910071575 |      351051 |              2592 |
| sv         | caselaw        |        1585 |   276785972 |      105980 |              2611 |
| sv         | decision       |        1213 |   129521101 |       54357 |              2382 |
| sv         | directive      |         195 |    28234600 |        4393 |              6427 |
| sv         | intagr         |         463 |    54192873 |       11676 |              4641 |
| sv         | proposal       |        1059 |   155339680 |       29292 |              5303 |
| sv         | recommendation |          79 |    12681607 |        3366 |              3767 |
| sv         | regulation     |        2825 |   253315742 |      141987 |              1784 |

### Data Fields

[More Information Needed]

### Data Splits

[More Information Needed]

## Dataset Creation


### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

The data has been downloaded using the R package [eurlex](https://cran.r-project.org/web/packages/eurlex/vignettes/eurlexpkg.html) between June and August 2022.


#### Who are the source language producers?

[More Information Needed]


### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

[More Information Needed]

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

[More Information Needed]

### Licensing Information

[More Information Needed]

### Citation Information

[More Information Needed]

### Contributions

Thanks to [@JoelNiklaus](https://github.com/joelniklaus) for adding this dataset.
