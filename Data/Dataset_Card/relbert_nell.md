---
language:
- en
license:
- other
multilinguality:
- monolingual
size_categories:
- n<1K
pretty_name: relbert/nell
---

# Dataset Card for "relbert/nell"
## Dataset Description
- **Repository:** [https://github.com/xwhan/One-shot-Relational-Learning](https://github.com/xwhan/One-shot-Relational-Learning)
- **Paper:** [https://aclanthology.org/D18-1223/](https://aclanthology.org/D18-1223/)
- **Dataset:** Never Ending Language Learner (NELL) dataset for one-shot link prediction.

### Dataset Summary
This is NELL-ONE dataset for the few-shots link prediction proposed in [https://aclanthology.org/D18-1223/](https://aclanthology.org/D18-1223/).
Please see [NELL paper](https://www.cs.cmu.edu/~tom/pubs/NELL_aaai15.pdf) to know more about the original dataset.

- Number of instances

|                                 |   train |   validation |   test |                                                                                        
|:--------------------------------|--------:|-------------:|-------:|                                                                                         
| number of pairs                 |    5498 |          878 |   1352 |                                                                                         
| number of unique relation types |      32 |            4 |      6 |   

- Number of pairs in each relation type

|                                                    |   number of pairs (train) |   number of pairs (validation) |   number of pairs (test) |
|:---------------------------------------------------|--------------------------:|-------------------------------:|-------------------------:|
| concept:airportincity                              |                       210 |                              0 |                        0 |
| concept:athleteledsportsteam                       |                       424 |                              0 |                        0 |
| concept:automobilemakercardealersinstateorprovince |                        78 |                              0 |                        0 |
| concept:bankboughtbank                             |                        58 |                              0 |                        0 |
| concept:ceoof                                      |                       271 |                              0 |                        0 |
| concept:cityradiostation                           |                        99 |                              0 |                        0 |
| concept:citytelevisionstation                      |                       316 |                              0 |                        0 |
| concept:countriessuchascountries                   |                       100 |                              0 |                        0 |
| concept:countrycapital                             |                       211 |                              0 |                        0 |
| concept:countryhascitizen                          |                       182 |                              0 |                        0 |
| concept:countryoforganizationheadquarters          |                       166 |                              0 |                        0 |
| concept:countrystates                              |                       169 |                              0 |                        0 |
| concept:drugpossiblytreatsphysiologicalcondition   |                        91 |                              0 |                        0 |
| concept:fatherofperson                             |                       108 |                              0 |                        0 |
| concept:fooddecreasestheriskofdisease              |                         1 |                              0 |                        0 |
| concept:hasofficeincountry                         |                       283 |                              0 |                        0 |
| concept:leaguecoaches                              |                        71 |                              0 |                        0 |
| concept:leaguestadiums                             |                       279 |                              0 |                        0 |
| concept:musicartistmusician                        |                       118 |                              0 |                        0 |
| concept:musicgenressuchasmusicgenres               |                       107 |                              0 |                        0 |
| concept:organizationnamehasacronym                 |                        61 |                              0 |                        0 |
| concept:personalsoknownas                          |                        78 |                              0 |                        0 |
| concept:personleadsgeopoliticalorganization        |                       120 |                              0 |                        0 |
| concept:personmovedtostateorprovince               |                       225 |                              0 |                        0 |
| concept:politicianrepresentslocation               |                       258 |                              0 |                        0 |
| concept:politicianusholdsoffice                    |                       216 |                              0 |                        0 |
| concept:statehascapital                            |                       151 |                              0 |                        0 |
| concept:stateorprovinceoforganizationheadquarters  |                       118 |                              0 |                        0 |
| concept:teamhomestadium                            |                       138 |                              0 |                        0 |
| concept:teamplaysincity                            |                       338 |                              0 |                        0 |
| concept:topmemberoforganization                    |                       354 |                              0 |                        0 |
| concept:wifeof                                     |                        99 |                              0 |                        0 |
| concept:bankbankincountry                          |                         0 |                            229 |                        0 |
| concept:cityalsoknownas                            |                         0 |                            356 |                        0 |
| concept:parentofperson                             |                         0 |                            217 |                        0 |
| concept:politicalgroupofpoliticianus               |                         0 |                             76 |                        0 |
| concept:automobilemakerdealersincity               |                         0 |                              0 |                      177 |
| concept:automobilemakerdealersincountry            |                         0 |                              0 |                       96 |
| concept:geopoliticallocationresidenceofpersion     |                         0 |                              0 |                      143 |
| concept:politicianusendorsespoliticianus           |                         0 |                              0 |                      386 |
| concept:producedby                                 |                         0 |                              0 |                      209 |
| concept:teamcoach                                  |                         0 |                              0 |                      341 |

- Number of entity types

 |                          |   head (train) |   tail (train) |   head (validation) |   tail (validation) |   head (test) |   tail (test) |
|:-------------------------|---------------:|---------------:|--------------------:|--------------------:|--------------:|--------------:|
| actor                    |              6 |              2 |                   0 |                   0 |             0 |             0 |
| airport                  |            152 |              0 |                   0 |                   0 |             0 |             0 |
| astronaut                |              4 |              0 |                   0 |                   1 |             0 |             1 |
| athlete                  |            353 |             21 |                   1 |                   2 |             0 |            59 |
| attraction               |              4 |              1 |                   0 |                   0 |             0 |             0 |
| automobilemaker          |            131 |             29 |                   0 |                   0 |           273 |            54 |
| bank                     |            109 |            126 |                 144 |                   0 |             0 |             0 |
| biotechcompany           |             14 |             80 |                   0 |                   0 |             0 |            10 |
| building                 |              4 |              0 |                   0 |                   0 |             0 |             0 |
| celebrity                |              6 |              5 |                   0 |                   0 |             4 |             2 |
| ceo                      |            423 |              0 |                   0 |                   0 |             0 |             0 |
| city                     |            342 |            852 |                 316 |                 316 |            42 |           161 |
| coach                    |             29 |             61 |                   0 |                   3 |             0 |           245 |
| comedian                 |              1 |              0 |                   0 |                   0 |             0 |             0 |
| company                  |             76 |            549 |                   1 |                   0 |             1 |           144 |
| country                  |            755 |            455 |                   0 |                 197 |            27 |            91 |
| county                   |             36 |             39 |                  11 |                  11 |            10 |             4 |
| creditunion              |              1 |              0 |                   0 |                   0 |             0 |             0 |
| criminal                 |              3 |              0 |                   1 |                   0 |             0 |             1 |
| director                 |              2 |              0 |                   0 |                   0 |             0 |             1 |
| drug                     |             91 |              0 |                   0 |                   0 |             1 |             0 |
| female                   |            116 |              8 |                  38 |                   9 |             3 |             3 |
| geopoliticallocation     |            184 |            112 |                  96 |                  29 |            24 |             8 |
| geopoliticalorganization |             28 |             68 |                   8 |                  21 |             1 |             7 |
| governmentorganization   |             25 |             95 |                  74 |                   0 |             0 |             0 |
| island                   |             15 |              4 |                   4 |                   6 |             1 |             0 |
| journalist               |              4 |              0 |                   0 |                   0 |             0 |             1 |
| male                     |            132 |             78 |                  37 |                  52 |             1 |             5 |
| model                    |              2 |              0 |                   0 |                   0 |             0 |             0 |
| monarch                  |              4 |              3 |                   4 |                   1 |             0 |             0 |
| museum                   |              1 |              5 |                   0 |                   0 |             0 |             0 |
| musicartist              |            118 |              5 |                   0 |                   0 |             0 |             0 |
| musicgenre               |            107 |            107 |                   0 |                   0 |             0 |             0 |
| musician                 |              5 |            124 |                   0 |                   0 |             0 |             0 |
| newspaper                |              3 |              2 |                   0 |                   0 |             0 |             0 |
| organization             |             23 |             86 |                   1 |                   1 |            32 |             2 |
| person                   |            350 |            256 |                 116 |                 131 |             0 |            96 |
| personafrica             |              1 |              3 |                   0 |                   0 |             0 |             0 |
| personasia               |              1 |              3 |                   0 |                   0 |             0 |             0 |
| personaustralia          |             38 |              5 |                   0 |                   0 |             0 |             5 |
| personcanada             |             19 |             14 |                   0 |                   0 |             0 |             0 |
| personeurope             |              9 |              7 |                  14 |                   4 |             0 |             1 |
| personmexico             |             57 |             14 |                   0 |                   0 |             0 |            20 |
| personnorthamerica       |              9 |              6 |                   0 |                   0 |             0 |             3 |
| personsouthamerica       |              1 |              1 |                   0 |                  17 |             0 |             0 |
| personus                 |             41 |             21 |                   2 |                   0 |             1 |             6 |
| planet                   |              1 |              0 |                   0 |                   0 |             0 |             1 |
| politician               |            107 |              5 |                   0 |                   1 |            23 |            58 |
| politicianus             |            408 |             12 |                   3 |                  71 |           352 |           360 |
| politicsblog             |              2 |              3 |                   0 |                   0 |             0 |             0 |
| port                     |              7 |              0 |                   0 |                   0 |             0 |             0 |
| professor                |              7 |              2 |                   0 |                   0 |             1 |             0 |
| publication              |              1 |             21 |                   0 |                   0 |             0 |             0 |
| recordlabel              |              1 |             13 |                   0 |                   0 |             0 |             0 |
| retailstore              |              1 |             15 |                   0 |                   0 |             0 |             0 |
| school                   |             54 |              1 |                   0 |                   0 |            11 |             0 |
| scientist                |              5 |              2 |                   0 |                   1 |             0 |             0 |
| sportsleague             |            356 |             12 |                   0 |                   0 |             0 |             0 |
| sportsteam               |            392 |            430 |                   0 |                   0 |           295 |             0 |
| stateorprovince          |            254 |            602 |                   0 |                   0 |            38 |             0 |
| transportation           |             36 |              2 |                   0 |                   0 |             0 |             0 |
| university               |              3 |             15 |                   0 |                   0 |             0 |             0 |
| visualizablescene        |             20 |              7 |                   3 |                   3 |             3 |             3 |
| visualizablething        |              1 |              1 |                   1 |                   1 |             0 |             0 |
| website                  |              7 |             31 |                   0 |                   0 |             0 |             0 |
| caf_                     |              0 |              1 |                   0 |                   0 |             0 |             0 |
| continent                |              0 |              1 |                   0 |                   0 |             0 |             0 |
| disease                  |              0 |             92 |                   0 |                   0 |             0 |             0 |
| hotel                    |              0 |              1 |                   0 |                   0 |             0 |             0 |
| magazine                 |              0 |              5 |                   0 |                   0 |             0 |             0 |
| nongovorganization       |              0 |              4 |                   0 |                   0 |             0 |             0 |
| nonprofitorganization    |              0 |              2 |                   0 |                   0 |             0 |             0 |
| park                     |              0 |              1 |                   0 |                   0 |             0 |             0 |
| petroleumrefiningcompany |              0 |              6 |                   0 |                   0 |             0 |             0 |
| politicaloffice          |              0 |            216 |                   0 |                   0 |             0 |             0 |
| politicalparty           |              0 |              6 |                   2 |                   0 |             0 |             0 |
| radiostation             |              0 |             93 |                   0 |                   0 |             0 |             0 |
| river                    |              0 |              4 |                   0 |                   0 |             0 |             0 |
| stadiumoreventvenue      |              0 |            417 |                   0 |                   0 |             0 |             0 |
| televisionnetwork        |              0 |              1 |                   0 |                   0 |             0 |             0 |
| televisionstation        |              0 |            221 |                   0 |                   0 |             0 |             0 |
| trainstation             |              0 |              2 |                   0 |                   0 |             0 |             0 |
| writer                   |              0 |              3 |                   1 |                   0 |             0 |             0 |
| zoo                      |              0 |              1 |                   0 |                   0 |             0 |             0 |
| automobilemodel          |              0 |              0 |                   0 |                   0 |           100 |             0 |
| product                  |              0 |              0 |                   0 |                   0 |            62 |             0 |
| software                 |              0 |              0 |                   0 |                   0 |            42 |             0 |
| videogame                |              0 |              0 |                   0 |                   0 |             4 |             0 |

## Dataset Structure
An example of `test` looks as below.
```shell
{
  "relation": "concept:producedby",
  "head": "Toyota Tacoma",
  "head_type": "automobilemodel",
  "tail": "Toyota",
  "tail_type": "automobilemaker"
}
```


## Citation Information
```
@inproceedings{xiong-etal-2018-one,
    title = "One-Shot Relational Learning for Knowledge Graphs",
    author = "Xiong, Wenhan  and
      Yu, Mo  and
      Chang, Shiyu  and
      Guo, Xiaoxiao  and
      Wang, William Yang",
    booktitle = "Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing",
    month = oct # "-" # nov,
    year = "2018",
    address = "Brussels, Belgium",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/D18-1223",
    doi = "10.18653/v1/D18-1223",
    pages = "1980--1990",
    abstract = "Knowledge graphs (KG) are the key components of various natural language processing applications. To further expand KGs{'} coverage, previous studies on knowledge graph completion usually require a large number of positive examples for each relation. However, we observe long-tail relations are actually more common in KGs and those newly added relations often do not have many known triples for training. In this work, we aim at predicting new facts under a challenging setting where only one training instance is available. We propose a one-shot relational learning framework, which utilizes the knowledge distilled by embedding models and learns a matching metric by considering both the learned embeddings and one-hop graph structures. Empirically, our model yields considerable performance improvements over existing embedding models, and also eliminates the need of re-training the embedding models when dealing with newly added relations.",
}
```
