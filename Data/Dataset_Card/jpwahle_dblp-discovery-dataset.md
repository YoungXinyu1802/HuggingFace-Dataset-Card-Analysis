---
annotations_creators:
- found
language:
- en
language_creators:
- found
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: DBLP Discovery Dataset (D3)
size_categories:
- 1M<n<10M
source_datasets:
- extended|s2orc
tags:
- dblp
- s2
- scientometrics
- computer science
- papers
- arxiv
task_categories:
- other
task_ids: []
paperswithcode_id: d3
dataset_info:
- config_name: papers
  download_size: 15876152
  dataset_size: 15876152
- config_name: authors
  download_size: 1177888
  dataset_size: 1177888
---
# Dataset Card for DBLP Discovery Dataset (D3)
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
- **Repository:** https://github.com/jpwahle/lrec22-d3-dataset
- **Paper:** https://aclanthology.org/2022.lrec-1.283/
- **Total size:** 8.71 GB
### Dataset Summary
DBLP is the largest open-access repository of scientific articles on computer science and provides metadata associated with publications, authors, and venues. We retrieved more than 6 million publications from DBLP and extracted pertinent metadata (e.g., abstracts, author affiliations, citations) from the publication texts to create the DBLP Discovery Dataset (D3). D3 can be used to identify trends in research activity, productivity, focus, bias, accessibility, and impact of computer science research. We present an initial analysis focused on the volume of computer science research (e.g., number of papers, authors, research activity), trends in topics of interest, and citation patterns. Our findings show that computer science is a growing research field (15% annually), with an active and collaborative researcher community. While papers in recent years present more bibliographical entries in comparison to previous decades, the average number of citations has been declining. Investigating papers’ abstracts reveals that recent topic trends are clearly reflected in D3. Finally, we list further applications of D3 and pose supplemental research questions. The D3 dataset, our findings, and source code are publicly available for research purposes.
### Supported Tasks and Leaderboards
[More Information Needed]
### Languages
English
## Dataset Structure
### Data Instances
Total size: 8.71 GB
Papers size: 8.13 GB
Authors size: 0.58 GB
### Data Fields
#### Papers
| Feature | Description |
| --- | --- |
| `corpusid` | The unique identifier of the paper. |
| `externalids` | The same paper in other repositories (e.g., DOI, ACL). |
| `title` | The title of the paper. |
| `authors` | The authors of the paper with their `authorid` and `name`. |
| `venue` | The venue of the paper. |
| `year` | The year of the paper publication. |
| `publicationdate` | A more precise publication date of the paper. |
| `abstract` | The abstract of the paper. |
| `outgoingcitations` | The number of references of the paper. |
| `ingoingcitations` | The number of citations of the paper. |
| `isopenaccess` | Whether the paper is open access. |
| `influentialcitationcount` | The number of influential citations of the paper according to SemanticScholar. |
| `s2fieldsofstudy` | The fields of study of the paper according to SemanticScholar. |
| `publicationtypes` | The publication types of the paper. |
| `journal` | The journal of the paper. |
| `updated` | The last time the paper was updated. |
| `url` | A url to the paper in SemanticScholar. |

#### Authors
| Feature | Description |
| --- | --- |
| `authorid` | The unique identifier of the author. |
| `externalids` | The same author in other repositories (e.g., ACL, PubMed). This can include `ORCID` |
| `name` | The name of the author. |
| `affiliations` | The affiliations of the author. |
| `homepage` | The homepage of the author. |
| `papercount` | The number of papers the author has written. |
| `citationcount` | The number of citations the author has received. |
| `hindex` | The h-index of the author. |
| `updated` | The last time the author was updated. |
| `email` | The email of the author. |
| `s2url` | A url to the author in SemanticScholar. |
### Data Splits
- `papers`
- `authors`
## Dataset Creation
### Curation Rationale
Providing a resource to analyze the state of computer science research statistically and semantically.
### Source Data
#### Initial Data Collection and Normalization
DBLP and from v2.0 SemanticScholar
## Additional Information
### Dataset Curators
[Jan Philip Wahle](https://jpwahle.com/)
### Licensing Information
The DBLP Discovery Dataset is released under the CC BY-NC 4.0. By using this corpus, you are agreeing to its usage terms.
### Citation Information
If you use the dataset in any way, please cite:
```bib
@inproceedings{Wahle2022c,
  title        = {D3: A Massive Dataset of Scholarly Metadata for Analyzing the State of Computer Science Research},
  author       = {Wahle, Jan Philip and Ruas, Terry and Mohammad, Saif M. and Gipp, Bela},
  year         = {2022},
  month        = {July},
  booktitle    = {Proceedings of The 13th Language Resources and Evaluation Conference},
  publisher    = {European Language Resources Association},
  address      = {Marseille, France},
  doi          = {},
}
```
Also make sure to cite the following papers if you use SemanticScholar data:
```bib
@inproceedings{ammar-etal-2018-construction,
    title = "Construction of the Literature Graph in Semantic Scholar",
    author = "Ammar, Waleed  and
      Groeneveld, Dirk  and
      Bhagavatula, Chandra  and
      Beltagy, Iz",
    booktitle = "Proceedings of the 2018 Conference of the North {A}merican Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 3 (Industry Papers)",
    month = jun,
    year = "2018",
    address = "New Orleans - Louisiana",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/N18-3011",
    doi = "10.18653/v1/N18-3011",
    pages = "84--91",
}
```
```bib
@inproceedings{lo-wang-2020-s2orc,
    title = "{S}2{ORC}: The Semantic Scholar Open Research Corpus",
    author = "Lo, Kyle  and Wang, Lucy Lu  and Neumann, Mark  and Kinney, Rodney  and Weld, Daniel",
    booktitle = "Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics",
    month = jul,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.acl-main.447",
    doi = "10.18653/v1/2020.acl-main.447",
    pages = "4969--4983"
}
```### Contributions
Thanks to [@jpwahle](https://github.com/jpwahle) for adding this dataset.
