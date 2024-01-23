---
language:
- en
license:
- other
multilinguality:
- monolingual
size_categories:
- n<1K
pretty_name: relbert/t_rex
---

# Dataset Card for "relbert/t_rex"
## Dataset Description
- **Repository:** [https://hadyelsahar.github.io/t-rex/](https://hadyelsahar.github.io/t-rex/)
- **Paper:** [https://aclanthology.org/L18-1544/](https://aclanthology.org/L18-1544/)
- **Dataset:** Cleaned T-REX for link prediction.

## Dataset Summary
This is the T-REX dataset proposed in [https://aclanthology.org/L18-1544/](https://aclanthology.org/L18-1544/).
The test split is universal across different version, which is manually checked by the author of [relbert/t_rex](https://huggingface.co/datasets/relbert/t_rex), 
and the test split contains predicates that is not included in the train/validation split.
The train/validation splits are created for each configuration by the ratio of 9:1. 
The number of triples in each split is summarized in the table below.

***Note:*** To make it consistent with other datasets ([nell](https://huggingface.co/datasets/relbert/nell) and [conceptnet](https://huggingface.co/datasets/relbert/conceptnet)), we rename predicate/subject/object as relation/head/tail.

- Number of instances (`filter_unified.min_entity_4_max_predicate_10`) 

 |                                 |   train |   validation |   test |
|:--------------------------------|--------:|-------------:|-------:|
| number of pairs                 |     603 |           68 |    122 |
| number of unique relation types |     157 |           52 |     34 |

- Number of pairs in each relation type (`filter_unified.min_entity_4_max_predicate_10`)

 |                                                           |   number of pairs (train) |   number of pairs (validation) |   number of pairs (test) |
|:----------------------------------------------------------|--------------------------:|-------------------------------:|-------------------------:|
| [Academic Subject] studies [Topic]                        |                         3 |                              0 |                        0 |
| [Airline] is in [Airline Alliance]                        |                         3 |                              2 |                        0 |
| [Army] has [Fleet]                                        |                         9 |                              1 |                        0 |
| [Art Work] follows after [Art Work]                       |                         2 |                              1 |                        0 |
| [Art Work] is a translation of [Art Work]                 |                         2 |                              1 |                        0 |
| [Art Work] is painted by [Person]                         |                         1 |                              2 |                        0 |
| [Art Work] is sculpted by [Person]                        |                         4 |                              0 |                        0 |
| [Art Work] is written by [Person]                         |                         1 |                              0 |                        0 |
| [Artifact] has a shape of [Shape]                         |                         1 |                              0 |                        0 |
| [Artifact] is a patron saint of [Country]                 |                         4 |                              0 |                        0 |
| [Artifact] is a type of [Type]                            |                         3 |                              0 |                        0 |
| [Artifact] is built on [Date]                             |                         5 |                              0 |                        0 |
| [Artifact] is discovered by [Person]                      |                         4 |                              0 |                        0 |
| [Artifact] is formation of [Army]                         |                         1 |                              1 |                        0 |
| [Artifact] is formed from [Artifact]                      |                         9 |                              0 |                        0 |
| [Artifact] is influenced by [Artifact]                    |                         6 |                              1 |                        0 |
| [Artifact] is maintained by [Company]                     |                         6 |                              2 |                        0 |
| [Artifact] is name of [Artifact]                          |                        10 |                              0 |                        0 |
| [Artifact] is named after [Person]                        |                         5 |                              0 |                        0 |
| [Artifact] is the OS of [Software]                        |                         3 |                              0 |                        0 |
| [Artifact] is the platform of [Game]                      |                         4 |                              0 |                        0 |
| [Artifact] is used for its namesake of [Artifact]         |                         3 |                              0 |                        0 |
| [Artists] leads [Movement]                                |                         7 |                              0 |                        0 |
| [Award] is presented by [Company]                         |                         1 |                              0 |                        0 |
| [Bank] is the central bank of [Country]                   |                         1 |                              0 |                        0 |
| [Bridge] crosses [Artifact]                               |                         3 |                              1 |                        0 |
| [Bridge] crosses [River]                                  |                         1 |                              0 |                        0 |
| [Building] has an architectural style of [Person]         |                         5 |                              0 |                        0 |
| [City] is a twin city of [City]                           |                         6 |                              2 |                        0 |
| [City] is in [Country]                                    |                         1 |                              0 |                        0 |
| [City] is the capital of [Country]                        |                         2 |                              0 |                        0 |
| [Company] is a subsidiary of [Company]                    |                         3 |                              1 |                        0 |
| [Company] is in a sector of [Sector]                      |                         2 |                              0 |                        0 |
| [Company] operates [Vehicle]                              |                         1 |                              0 |                        0 |
| [Company] owns [Product]                                  |                         3 |                              1 |                        0 |
| [Company] publishes [Art Work]                            |                         7 |                              0 |                        0 |
| [Competition] is a league of [Sport]                      |                         2 |                              2 |                        0 |
| [Council] is the council of [Country]                     |                         6 |                              0 |                        0 |
| [Country] has [History]                                   |                         2 |                              0 |                        0 |
| [Country] is [Political Party] assembly                   |                         4 |                              1 |                        0 |
| [Country] is enclaved by [Country]                        |                         4 |                              0 |                        0 |
| [Country] is in [Continent]                               |                         2 |                              0 |                        0 |
| [Country] joins [War]                                     |                         2 |                              1 |                        0 |
| [Country]'s county seat is [Location]                     |                         6 |                              0 |                        0 |
| [Country]'s flag is [Artifact]                            |                         1 |                              0 |                        0 |
| [Culture] is originated in [Country]                      |                         2 |                              0 |                        0 |
| [Currency] is used in [Country]                           |                         3 |                              2 |                        0 |
| [Disease] is caused by [Virus]                            |                         4 |                              0 |                        0 |
| [Event] is since [Date]                                   |                         3 |                              0 |                        0 |
| [Event] takes place at [Location]                         |                         4 |                              0 |                        0 |
| [Fictional Character] is a mascot of [Sport Team]         |                         2 |                              1 |                        0 |
| [Fictional Character] is from [Art Work]                  |                         6 |                              1 |                        0 |
| [Food] is made from [Ingredient]                          |                         6 |                              0 |                        0 |
| [Government] is the government of [Country]               |                         4 |                              0 |                        0 |
| [Government] is the jurisdiction of [City]                |                         1 |                              0 |                        0 |
| [Group] has a section of [Group]                          |                         6 |                              1 |                        0 |
| [Group] is a predecessor of [Group]                       |                         5 |                              0 |                        0 |
| [Group] is a religious order of [Group]                   |                         1 |                              0 |                        0 |
| [Group] is created on [Date]                              |                         6 |                              0 |                        0 |
| [Group] is founded at [Location]                          |                         9 |                              0 |                        0 |
| [Group] is founded by [Person]                            |                         6 |                              0 |                        0 |
| [Group] is founded on [Date]                              |                         2 |                              0 |                        0 |
| [Group] is legislature of [Country]                       |                         2 |                              0 |                        0 |
| [Group] is the parliament of [Country]                    |                         2 |                              0 |                        0 |
| [Group]'s leader is [Person]                              |                         3 |                              0 |                        0 |
| [Head of Government] is appointed by [Head of Government] |                         1 |                              0 |                        0 |
| [Island] is [Country]                                     |                         1 |                              0 |                        0 |
| [Job] is the head of state in [Location]                  |                         1 |                              0 |                        0 |
| [Land] is [Country]                                       |                         1 |                              1 |                        0 |
| [Language] consists of [Alphabet]                         |                         4 |                              0 |                        0 |
| [Language] is a dialect of [Language]                     |                         5 |                              0 |                        0 |
| [Location] is a sovereign state of [Location]             |                         7 |                              1 |                        0 |
| [Location] is an Indian reservation in [Country]          |                         9 |                              0 |                        0 |
| [Location] is an administrative center of [Location]      |                         6 |                              0 |                        0 |
| [Location] is exclave of [Country]                        |                         4 |                              0 |                        0 |
| [Location] is in [Planet]                                 |                         1 |                              0 |                        0 |
| [Location] is next to [Location]                          |                         1 |                              0 |                        0 |
| [Location] is on the coast of [Ocean]                     |                         5 |                              0 |                        0 |
| [Location] is split from [Location]                       |                         2 |                              0 |                        0 |
| [Location] is the highest peak in [Country]               |                         2 |                              0 |                        0 |
| [Medication] is for [Disease]                             |                         4 |                              0 |                        0 |
| [Movie] is [Genre]                                        |                         9 |                              1 |                        0 |
| [Movie] is a libretto by [Person]                         |                         6 |                              0 |                        0 |
| [Movie] is a spinoff of [Movie]                           |                         1 |                              0 |                        0 |
| [Movie] is in the universe of [Art Work]                  |                         1 |                              0 |                        0 |
| [Movie] is produced by [Company]                          |                         6 |                              1 |                        0 |
| [Music Artist] is [Genre]                                 |                         7 |                              0 |                        0 |
| [Music] is made by [Artist]                               |                         1 |                              1 |                        0 |
| [Music] is released on [Date]                             |                         4 |                              0 |                        0 |
| [Organization]'s ideology is [Ideology]                   |                         5 |                              0 |                        0 |
| [PC]'s cpu is [CPU]                                       |                         8 |                              1 |                        0 |
| [Person] and [Person] are married                         |                         5 |                              0 |                        0 |
| [Person] belongs to [Record Label]                        |                         1 |                              1 |                        0 |
| [Person] built [Artifact]                                 |                         5 |                              0 |                        0 |
| [Person] causes [War]                                     |                         2 |                              0 |                        0 |
| [Person] creates [Work]                                   |                         4 |                              0 |                        0 |
| [Person] dies at [Location]                               |                         5 |                              2 |                        0 |
| [Person] dies on [Date]                                   |                         5 |                              1 |                        0 |
| [Person] has a house in [Location]                        |                         9 |                              0 |                        0 |
| [Person] is [Occupation]                                  |                         3 |                              0 |                        0 |
| [Person] is [Sex]                                         |                         2 |                              1 |                        0 |
| [Person] is a candidate of [Election]                     |                         3 |                              1 |                        0 |
| [Person] is a chancellor of [Country]                     |                         4 |                              0 |                        0 |
| [Person] is a coach of [Sport Team]                       |                         3 |                              0 |                        0 |
| [Person] is a concubine of [Person]                       |                         4 |                              0 |                        0 |
| [Person] is a consort of [Person]                         |                         3 |                              1 |                        0 |
| [Person] is a husband of [Person]                         |                         2 |                              0 |                        0 |
| [Person] is a manager of [Sport Team]                     |                         3 |                              0 |                        0 |
| [Person] is a member of [Music Group]                     |                         6 |                              1 |                        0 |
| [Person] is a mistress of [Person]                        |                         4 |                              0 |                        0 |
| [Person] is a premier of [Group]                          |                         3 |                              0 |                        0 |
| [Person] is a presenter of [TV show]                      |                         2 |                              0 |                        0 |
| [Person] is a student of [Person]                         |                         1 |                              0 |                        0 |
| [Person] is active in [Location]                          |                         2 |                              1 |                        0 |
| [Person] is awarded by [Award]                            |                         5 |                              0 |                        0 |
| [Person] is born in [Country]                             |                         5 |                              1 |                        0 |
| [Person] is born in [Location]                            |                         4 |                              1 |                        0 |
| [Person] is born on [Date]                                |                         5 |                              2 |                        0 |
| [Person] is buried at [Tomb]                              |                         5 |                              0 |                        0 |
| [Person] is drafted by [Group]                            |                         3 |                              0 |                        0 |
| [Person] is from [Era]                                    |                         6 |                              0 |                        0 |
| [Person] is in [Prison]                                   |                         3 |                              0 |                        0 |
| [Person] is killed by [Person]                            |                         2 |                              1 |                        0 |
| [Person] is played at [Group]                             |                         7 |                              3 |                        0 |
| [Person] is the chair of [Group]                          |                         1 |                              0 |                        0 |
| [Person] is the emperor of [Country]                      |                         6 |                              0 |                        0 |
| [Person] is the leader of [Dynasty]                       |                         4 |                              1 |                        0 |
| [Person] is the mayor of [City]                           |                         2 |                              0 |                        0 |
| [Person] is the monarch of [Country]                      |                         4 |                              0 |                        0 |
| [Person] is the president of [Country]                    |                         3 |                              1 |                        0 |
| [Person] is the prime minister of [Country]               |                         3 |                              1 |                        0 |
| [Person] is the queen of [Country]                        |                         5 |                              0 |                        0 |
| [Person] live in [Location]                               |                         8 |                              1 |                        0 |
| [Person] plays in [Movie]                                 |                         3 |                              0 |                        0 |
| [Person] plays in [Sport Team]                            |                         8 |                              0 |                        0 |
| [Person] studies [Academic Subject]                       |                         6 |                              1 |                        0 |
| [Person] studies at [School]                              |                         9 |                              1 |                        0 |
| [Pet] is a pet of [Person]                                |                         1 |                              0 |                        0 |
| [Planet] is in the orbit of [Orbit]                       |                         1 |                              0 |                        0 |
| [Play] is performed by [Person]                           |                         7 |                              2 |                        0 |
| [Railway] is in [Location]                                |                         4 |                              0 |                        0 |
| [Religion] is a denomination by [Artifact]                |                         2 |                              2 |                        0 |
| [River] drains [Location]                                 |                         5 |                              0 |                        0 |
| [River] is a tributary of [River]                         |                         4 |                              0 |                        0 |
| [River] outflows to [Location]                            |                         3 |                              0 |                        0 |
| [Software] is under license of [License]                  |                         5 |                              3 |                        0 |
| [Software] is used for [Purpose]                          |                         3 |                              0 |                        0 |
| [Software] is written in [Programming Language]           |                         6 |                              1 |                        0 |
| [Sport Team] is an affiliate of [Sport Team]              |                         2 |                              1 |                        0 |
| [Sport Team] plays at [Competition]                       |                         5 |                              0 |                        0 |
| [Sport Team] plays in [Competition]                       |                         8 |                              0 |                        0 |
| [Sport Team] wins [Competition]                           |                         5 |                              0 |                        0 |
| [Sport Team]'s home field is [Location]                   |                         4 |                              0 |                        0 |
| [Star] is a [Constellation]                               |                         1 |                              0 |                        0 |
| [State] is a state of [Country]                           |                         1 |                              0 |                        0 |
| [System] is a system in [Artifact]                        |                         7 |                              2 |                        0 |
| [Town] is in [Location]                                   |                         1 |                              0 |                        0 |
| [Art Work] is directed by [Person]                        |                         0 |                              1 |                        0 |
| [Planet] is a satellite of [Planet]                       |                         0 |                              2 |                        0 |
| [Act] is signed by [Person]                               |                         0 |                              0 |                        2 |
| [Airline] has a hub in [Location]                         |                         0 |                              0 |                        7 |
| [Artifact] is a coat of arms of [Group]                   |                         0 |                              0 |                        5 |
| [Artifact] is a result of [Artifact]                      |                         0 |                              0 |                        1 |
| [Artifact] is found in [Artifact]                         |                         0 |                              0 |                        4 |
| [Artifact] is in [Color]                                  |                         0 |                              0 |                        4 |
| [Artifact] is manufactured by [Company]                   |                         0 |                              0 |                        5 |
| [Artist] is produced by [Person]                          |                         0 |                              0 |                        1 |
| [City] is a capital town of [Country]                     |                         0 |                              0 |                        6 |
| [Country] claims [City]                                   |                         0 |                              0 |                        1 |
| [Country] is a member of [Group]                          |                         0 |                              0 |                        4 |
| [Event] starts on [Date]                                  |                         0 |                              0 |                        2 |
| [Group] is [Religion]                                     |                         0 |                              0 |                        6 |
| [Group] is legislative body of [Country]                  |                         0 |                              0 |                        8 |
| [Group] is merged into [Group]                            |                         0 |                              0 |                        4 |
| [Group] speaks [Language]                                 |                         0 |                              0 |                        5 |
| [License] is approved by [Organization]                   |                         0 |                              0 |                        3 |
| [Location] is a ballpark of [Sport Team]                  |                         0 |                              0 |                        3 |
| [Location] is a river mouth of [Bay]                      |                         0 |                              0 |                        1 |
| [Movie] is screenplayed by [Person]                       |                         0 |                              0 |                        5 |
| [Movie] stars [Actor]                                     |                         0 |                              0 |                        2 |
| [Music] is an anthem of [Country]                         |                         0 |                              0 |                        1 |
| [Occupation] lives in [Location]                          |                         0 |                              0 |                        1 |
| [Person] belongs to [Political Party]                     |                         0 |                              0 |                       10 |
| [Person] is a chief executive of [Company]                |                         0 |                              0 |                        1 |
| [Person] is a child of [Person]                           |                         0 |                              0 |                        2 |
| [Person] is the king of [Country]                         |                         0 |                              0 |                        4 |
| [Person] plays [Instrument]                               |                         0 |                              0 |                        6 |
| [Person] speaks [Language]                                |                         0 |                              0 |                        1 |
| [Radio Program] is broadcasted on [Radio Channel]         |                         0 |                              0 |                        3 |
| [Software] is developed by [Company]                      |                         0 |                              0 |                        1 |
| [Station] is the terminus of [Railway]                    |                         0 |                              0 |                        3 |
| [TV Series] is broadcasted on [TV Channel]                |                         0 |                              0 |                        1 |
| [Timezone] is a timezon in [Country]                      |                         0 |                              0 |                        9 |

### Other Statistics

|                                             |   number of pairs |   number of unique relation types |
|:--------------------------------------------|------------------:|----------------------------------:|
| min_entity_1_max_predicate_100 (train)      |              7075 |                               212 |
| min_entity_1_max_predicate_100 (validation) |               787 |                               166 |
| min_entity_1_max_predicate_50 (train)       |              4131 |                               212 |
| min_entity_1_max_predicate_50 (validation)  |               459 |                               156 |
| min_entity_1_max_predicate_25 (train)       |              2358 |                               212 |
| min_entity_1_max_predicate_25 (validation)  |               262 |                               144 |
| min_entity_1_max_predicate_10 (train)       |              1134 |                               210 |
| min_entity_1_max_predicate_10 (validation)  |               127 |                                94 |
| min_entity_2_max_predicate_100 (train)      |              4873 |                               195 |
| min_entity_2_max_predicate_100 (validation) |               542 |                               139 |
| min_entity_2_max_predicate_50 (train)       |              3002 |                               193 |
| min_entity_2_max_predicate_50 (validation)  |               334 |                               139 |
| min_entity_2_max_predicate_25 (train)       |              1711 |                               195 |
| min_entity_2_max_predicate_25 (validation)  |               191 |                               113 |
| min_entity_2_max_predicate_10 (train)       |               858 |                               194 |
| min_entity_2_max_predicate_10 (validation)  |                96 |                                81 |
| min_entity_3_max_predicate_100 (train)      |              3659 |                               173 |
| min_entity_3_max_predicate_100 (validation) |               407 |                               116 |
| min_entity_3_max_predicate_50 (train)       |              2336 |                               174 |
| min_entity_3_max_predicate_50 (validation)  |               260 |                               115 |
| min_entity_3_max_predicate_25 (train)       |              1390 |                               173 |
| min_entity_3_max_predicate_25 (validation)  |               155 |                                94 |
| min_entity_3_max_predicate_10 (train)       |               689 |                               171 |
| min_entity_3_max_predicate_10 (validation)  |                77 |                                59 |
| min_entity_4_max_predicate_100 (train)      |              2995 |                               158 |
| min_entity_4_max_predicate_100 (validation) |               333 |                               105 |
| min_entity_4_max_predicate_50 (train)       |              1989 |                               157 |
| min_entity_4_max_predicate_50 (validation)  |               222 |                               102 |
| min_entity_4_max_predicate_25 (train)       |              1221 |                               158 |
| min_entity_4_max_predicate_25 (validation)  |               136 |                                76 |
| min_entity_4_max_predicate_10 (train)       |               603 |                               157 |
| min_entity_4_max_predicate_10 (validation)  |                68 |                                52 |


### Filtering to Remove Noise
We apply filtering to keep triples with alpha-numeric subject and object, as well as triples with at least either of subject or object is a named-entity.
After the filtering, we manually remove too vague and noisy predicate, and unify same predicates with different names (see the annotation [here](https://huggingface.co/datasets/relbert/t_rex/raw/main/predicate_manual_check.csv)).

| Dataset   | `raw`     | `filter`  | `filter_unified` |
|:----------|----------:|----------:|-----------------:|
| Triples   | 941,663   | 583,333   | 432,795          |
| Predicate | 931       | 659       | 247              |
| Entity    | 270,801   | 197,163   | 149,172          |

### Filtering to Purify the Dataset
We reduce the size of the dataset by applying filtering based on the number of predicates and entities in the triples.
We first remove triples that contain either of subject or object with the occurrence in the dataset that is lower than `min entity`.
Then, we reduce the number triples in each predicate to be less than `max predicate`. 
If the number of triples in a predicate is higher than `max predicate`, 
we choose top-`max predicate` triples based on the frequency of the subject and the object, or random sampling.

- distribution of entities

<img src="https://huggingface.co/datasets/relbert/t_rex/resolve/main/data/stats.entity_distribution.png" alt="" width="600" style="margin-left:'auto' margin-right:'auto' display:'block'"/>

- distribution of predicates

<img src="https://huggingface.co/datasets/relbert/t_rex/resolve/main/data/stats.predicate_distribution.png" alt="" width="600" style="margin-left:'auto' margin-right:'auto' display:'block'"/>


## Dataset Structure
An example looks as follows.
```shell
{
  "tail": "Persian",
  "head": "Tajik",
  "title": "Tandoor bread",
  "text": "Tandoor bread (Arabic: \u062e\u0628\u0632 \u062a\u0646\u0648\u0631 khubz tannoor, Armenian: \u0569\u0578\u0576\u056b\u0580 \u0570\u0561\u0581 tonir hats, Azerbaijani: T\u0259ndir \u00e7\u00f6r\u0259yi, Georgian: \u10d7\u10dd\u10dc\u10d8\u10e1 \u10de\u10e3\u10e0\u10d8 tonis puri, Kazakh: \u0442\u0430\u043d\u0434\u044b\u0440 \u043d\u0430\u043d tandyr nan, Kyrgyz: \u0442\u0430\u043d\u0434\u044b\u0440 \u043d\u0430\u043d tandyr nan, Persian: \u0646\u0627\u0646 \u062a\u0646\u0648\u0631\u06cc nan-e-tanuri, Tajik: \u043d\u043e\u043d\u0438 \u0442\u0430\u043d\u0443\u0440\u0439 noni tanuri, Turkish: Tand\u0131r ekme\u011fi, Uyghur: ) is a type of leavened bread baked in a clay oven called a tandoor, similar to naan. In Pakistan, tandoor breads are popular especially in the Khyber Pakhtunkhwa and Punjab regions, where naan breads are baked in tandoor clay ovens fired by wood or charcoal. These tandoor-prepared naans are known as tandoori naan.",
  "relation": "[Artifact] is a type of [Type]"
}
```

## Reproduce the Dataset

```shell
git clone https://huggingface.co/datasets/relbert/t_rex
cd t_rex
mkdir data_raw
cd data_raw
cd data_raw
wget https://figshare.com/ndownloader/files/8760241
unzip 8760241
cd ../
python process.py
python unify_predicate.py
python filtering_purify.py
python create_split.py
```

## Citation Information
```
@inproceedings{elsahar2018t,
  title={T-rex: A large scale alignment of natural language with knowledge base triples},
  author={Elsahar, Hady and Vougiouklis, Pavlos and Remaci, Arslen and Gravier, Christophe and Hare, Jonathon and Laforest, Frederique and Simperl, Elena},
  booktitle={Proceedings of the Eleventh International Conference on Language Resources and Evaluation (LREC 2018)},
  year={2018}
} 
```
