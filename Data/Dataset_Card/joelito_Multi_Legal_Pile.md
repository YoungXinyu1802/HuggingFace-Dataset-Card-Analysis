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
pretty_name: "MultiLegalPile: A Large-Scale Multilingual Corpus for the Legal Domain"
size_categories:
- 10M<n<100M
source_datasets:
- original
task_categories:
- fill-mask

---

# Dataset Card for MultiLegalPile: A Large-Scale Multilingual Corpus for the Legal Domain

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
- **Repository:**
- **Paper:**
- **Leaderboard:**
- **Point of Contact:** [Joel Niklaus](mailto:joel.niklaus.2@bfh.ch)

### Dataset Summary

The Multi_Legal_Pile is a large-scale multilingual legal dataset suited for pretraining language models.
It spans over 24 languages and five legal text types.

### Supported Tasks and Leaderboards

The dataset supports the tasks of fill-mask.

### Languages

The following languages are supported: bg, cs, da, de, el, en, es, et, fi, fr, ga, hr, hu, it, lt, lv, mt, nl, pl, pt,
ro, sk, sl, sv

## Dataset Structure

It is structured in the following format:
type -> language -> jurisdiction.jsonl.xz

type is one of the following:

- caselaw
- contracts
- legislation
- other
- mc4_legal

`mc4_legal` is a subset of the other type but is listed separately so it can be easily excluded since it is less
permissively licensed than the other types.

Use the dataset like this:

```python
from datasets import load_dataset

config = 'en_contracts'  # {language}_{type}
dataset = load_dataset('joelito/Multi_Legal_Pile', config, split='train', streaming=True)
```

'config' is a combination of language and text_type, e.g. 'en_contracts' or 'de_caselaw'.
To load all the languages or all the text_types, use 'all' instead of the language or text_type (e.g., '
all_legislation').

### Data Instances

The file format is jsonl.xz and there is one split available ("train").

The complete dataset (689GB) consists of four large subsets:

- Native Multi Legal Pile (112GB)
- Eurlex Resources (179GB)
- Legal MC4 (106GB)
- Pile of Law (292GB)

#### Native Multilingual Legal Pile data

| Language | Text Type   | Jurisdiction | Source                             | Size (MB) | Tokens | Documents | Words/Document | URL | License |
|:---------|:------------|:-------------|:-----------------------------------|----------:|-------:|----------:|---------------:|-----|--------:|
| bg       | legislation | Bulgaria     | MARCELL                            |       588 |    xxx |       xxx |            xxx |     |         |
| cs       | caselaw     | Czechia      | CzCDC Constitutional Court         |       713 |    xxx |       xxx |            xxx |     |         |
| cs       | caselaw     | Czechia      | CzCDC Supreme Administrative Court |      1248 |    xxx |       xxx |            xxx |     |         |
| cs       | caselaw     | Czechia      | CzCDC Supreme Court                |      1566 |    xxx |       xxx |            xxx |     |         |
| da       | caselaw     | Denmark      | DDSC                               |       205 |    xxx |       xxx |            xxx |     |         |
| da       | legislation | Denmark      | DDSC                               |      1464 |    xxx |       xxx |            xxx |     |         |
| de       | caselaw     | Germany      | openlegaldata                      |      4310 |    xxx |       xxx |            xxx |     |         |
| de       | caselaw     | Switzerland  | entscheidsuche                     |      6937 |    xxx |       xxx |            xxx |     |         |
| de       | legislation | Germany      | openlegaldata                      |        96 |    xxx |       xxx |            xxx |     |         |
| de       | legislation | Switzerland  | lexfind                            |       299 |    xxx |       xxx |            xxx |     |         |
| en       | legislation | Switzerland  | lexfind                            |         9 |    xxx |       xxx |            xxx |     |         |
| en       | legislation | UK           | uk-lex                             |       262 |    xxx |       xxx |            xxx |     |         |
| fr       | caselaw     | Belgium      | jurportal                          |       104 |    xxx |       xxx |            xxx |     |         |
| fr       | caselaw     | France       | CASS                               |       266 |    xxx |       xxx |            xxx |     |         |
| fr       | caselaw     | Luxembourg   | judoc                              |       277 |    xxx |       xxx |            xxx |     |         |
| fr       | caselaw     | Switzerland  | entscheidsuche                     |      5100 |    xxx |       xxx |            xxx |     |         |
| fr       | legislation | Switzerland  | lexfind                            |       219 |    xxx |       xxx |            xxx |     |         |
| fr       | legislation | Belgium      | ejustice                           |       178 |    xxx |       xxx |            xxx |     |         |
| hu       | legislation | Hungary      | MARCELL                            |       239 |    xxx |       xxx |            xxx |     |         |
| it       | caselaw     | Switzerland  | entscheidsuche                     |      1274 |    xxx |       xxx |            xxx |     |         |
| it       | legislation | Switzerland  | lexfind                            |       141 |    xxx |       xxx |            xxx |     |         |
| nl       | legislation | Belgium      | ejustice                           |       178 |    xxx |       xxx |            xxx |     |         |
| pl       | legislation | Poland       | MARCELL                            |       264 |    xxx |       xxx |            xxx |     |         |
| pt       | caselaw     | Brazil       | RulingBR                           |       173 |    xxx |       xxx |            xxx |     |         |
| pt       | caselaw     | Brazil       | CRETA                              |     19000 |    xxx |       xxx |            xxx |     |         |
| pt       | caselaw     | Brazil       | CJPG                               |     63480 |    xxx |       xxx |            xxx |     |         |
| ro       | legislation | Romania      | MARCELL                            |      2704 |    xxx |       xxx |            xxx |     |         |
| sk       | legislation | Slovakia     | MARCELL                            |       192 |    xxx |       xxx |            xxx |     |         |
| sl       | legislation | Slovenia     | MARCELL                            |       753 |    xxx |       xxx |            xxx |     |         |
| total    | all         | all          | all                                |    112239 |    xxx |       xxx |            xxx |     |         |

#### Eurlex Resources

See [Eurlex Resources](https://huggingface.co/datasets/joelito/eurlex_resources#data-instances) for more information.

#### Legal-MC4

See [Legal-MC4](https://huggingface.co/datasets/joelito/legal-mc4#data-instances) for more information.

#### Pile-of-Law

See [Pile-of-Law](https://huggingface.co/datasets/pile-of-law/pile-of-law#data-instances) for more information.

| Language   | Type        | Jurisdiction   | Source                               |   Size (MB) |      Tokens |   Documents |   Tokens/Document | Part of Multi_Legal_Pile   |
|:-----------|:------------|:---------------|:-------------------------------------|------------:|------------:|------------:|------------------:|:---------------------------|
| en         | all         | all            | all                                  |      503712 | 50547777921 |     9872444 |              5120 | yes                        |
| en         | caselaw     | EU             | echr                                 |         298 |    28374996 |        8480 |              3346 | yes                        |
| en         | caselaw     | Canada         | canadian_decisions                   |         486 |    45438083 |       11343 |              4005 | yes                        |
| en         | caselaw     | US             | dol_ecab                             |         942 |    99113541 |       28211 |              3513 | no                         |
| en         | caselaw     | US             | scotus_oral_arguments                |        1092 |   108228951 |        7996 |             13535 | no                         |
| en         | caselaw     | US             | tax_rulings                          |        1704 |   166915887 |       54064 |              3087 | no                         |
| en         | caselaw     | US             | nlrb_decisions                       |        2652 |   294471818 |       32080 |              9179 | no                         |
| en         | caselaw     | US             | scotus_filings                       |        4018 |   593870413 |       63775 |              9311 | yes                        |
| en         | caselaw     | US             | bva_opinions                         |       35238 |  4084140080 |      839523 |              4864 | no                         |
| en         | caselaw     | US             | courtlistener_docket_entry_documents |      139006 | 12713614864 |     1983436 |              6409 | yes                        |
| en         | caselaw     | US             | courtlistener_opinions               |      158110 | 15899704961 |     4518445 |              3518 | yes                        |
| en         | contracts   | --             | tos                                  |           4 |      391890 |          50 |              7837 | no                         |
| en         | contracts   | US             | cfpb_creditcard_contracts            |         188 |    25984824 |        2638 |              9850 | yes                        |
| en         | contracts   | US             | edgar                                |       28698 |  2936402810 |      987926 |              2972 | yes                        |
| en         | contracts   | US             | atticus_contracts                    |       78300 |  7997013703 |      650833 |             12287 | yes                        |
| en         | legislation | US             | fre                                  |           2 |      173325 |          68 |              2548 | no                         |
| en         | legislation | US             | frcp                                 |           4 |      427614 |          92 |              4647 | no                         |
| en         | legislation | US             | eoir                                 |          62 |     6109737 |        2229 |              2741 | no                         |
| en         | legislation | --             | constitutions                        |          66 |     5984865 |         187 |             32004 | yes                        |
| en         | legislation | US             | federal_register                     |         424 |    39854787 |        5414 |              7361 | yes                        |
| en         | legislation | US             | uscode                               |         716 |    78466325 |          58 |           1352867 | yes                        |
| en         | legislation | EU             | euro_parl                            |         808 |    71344326 |        9672 |              7376 | no                         |
| en         | legislation | US             | cfr                                  |        1788 |   160849007 |         243 |            661930 | yes                        |
| en         | legislation | US             | us_bills                             |        3394 |   320723838 |      112483 |              2851 | yes                        |
| en         | legislation | EU             | eurlex                               |        3504 |   401324829 |      142036 |              2825 | no                         |
| en         | legislation | US             | state_codes                          |       18066 |  1858333235 |         217 |           8563747 | yes                        |
| en         | other       | --             | bar_exam_outlines                    |           4 |      346924 |          59 |              5880 | no                         |
| en         | other       | US             | ftc_advisory_opinions                |           4 |      509025 |         145 |              3510 | no                         |
| en         | other       | US             | olc_memos                            |          98 |    12764635 |        1384 |              9223 | yes                        |
| en         | other       | --             | cc_casebooks                         |         258 |    24857378 |          73 |            340512 | no                         |
| en         | other       | --             | un_debates                           |         360 |    31152497 |        8481 |              3673 | no                         |
| en         | other       | --             | r_legaladvice                        |         798 |    72605386 |      146671 |               495 | no                         |
| en         | other       | US             | founding_docs                        |        1118 |   100390231 |      183664 |               546 | no                         |
| en         | other       | US             | oig                                  |        5056 |   566782244 |       38954 |             14550 | yes                        |
| en         | other       | US             | congressional_hearings               |       16448 |  1801110892 |       31514 |             57152 | no                         |

### Data Fields

[More Information Needed]

### Data Splits

[More Information Needed]

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed]

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

```
TODO add citation
```

### Contributions

Thanks to [@JoelNiklaus](https://github.com/joelniklaus) for adding this dataset.
