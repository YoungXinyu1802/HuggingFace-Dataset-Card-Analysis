---
annotations_creators:
  - expert-generated
language:
  - en
language_creators:
  - expert-generated
license:
  - other
multilinguality:
  - monolingual
pretty_name: SemCor
size_categories:
  - 100K<n<1M
source_datasets:
  - original
tags:
  - word sense disambiguation
  - semcor
  - wordnet
task_categories:
  - text-classification
task_ids:
  - topic-classification
---

# Dataset Card for SemCor

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

- **Homepage:** https://web.eecs.umich.edu/~mihalcea/downloads.html#semcor
- **Repository:**
- **Paper:** https://aclanthology.org/H93-1061/
- **Leaderboard:**
- **Point of Contact:**

### Dataset Summary

SemCor 3.0 was automatically created from SemCor 1.6 by mapping WordNet 1.6 to
WordNet 3.0 senses. SemCor 1.6 was created and is property of Princeton
University.

Some (few) word senses from WordNet 1.6 were dropped, and therefore they cannot
be retrieved anymore in the 3.0 database. A sense of 0 (wnsn=0) is used to
symbolize a missing sense in WordNet 3.0.

The automatic mapping was performed within the Language and Information
Technologies lab at UNT, by Rada Mihalcea (rada@cs.unt.edu).

THIS MAPPING IS PROVIDED "AS IS" AND UNT MAKES NO REPRESENTATIONS OR WARRANTIES,
EXPRESS OR IMPLIED. BY WAY OF EXAMPLE, BUT NOT LIMITATION, UNT MAKES NO
REPRESENTATIONS OR WARRANTIES OF MERCHANT- ABILITY OR FITNESS FOR ANY PARTICULAR
PURPOSE.

In agreement with the license from Princeton Univerisity, you are granted
permission to use, copy, modify and distribute this database  
for any purpose and without fee and royalty is hereby granted, provided that you
agree to comply with the Princeton copyright notice and statements, including
the disclaimer, and that the same appear on ALL copies of the database,
including modifications that you make for internal  
use or for distribution.  
Both LICENSE and README files distributed with the SemCor 1.6 package are
included in the current distribution of SemCor 3.0.

### Languages

English

## Additional Information

### Licensing Information

WordNet Release 1.6 Semantic Concordance Release 1.6

This software and database is being provided to you, the LICENSEE, by  
Princeton University under the following license. By obtaining, using  
and/or copying this software and database, you agree that you have  
read, understood, and will comply with these terms and conditions.:

Permission to use, copy, modify and distribute this software and  
database and its documentation for any purpose and without fee or  
royalty is hereby granted, provided that you agree to comply with  
the following copyright notice and statements, including the disclaimer,  
and that the same appear on ALL copies of the software, database and  
documentation, including modifications that you make for internal  
use or for distribution.

WordNet 1.6 Copyright 1997 by Princeton University. All rights reserved.

THIS SOFTWARE AND DATABASE IS PROVIDED "AS IS" AND PRINCETON  
UNIVERSITY MAKES NO REPRESENTATIONS OR WARRANTIES, EXPRESS OR  
IMPLIED. BY WAY OF EXAMPLE, BUT NOT LIMITATION, PRINCETON  
UNIVERSITY MAKES NO REPRESENTATIONS OR WARRANTIES OF MERCHANT-  
ABILITY OR FITNESS FOR ANY PARTICULAR PURPOSE OR THAT THE USE  
OF THE LICENSED SOFTWARE, DATABASE OR DOCUMENTATION WILL NOT  
INFRINGE ANY THIRD PARTY PATENTS, COPYRIGHTS, TRADEMARKS OR  
OTHER RIGHTS.

The name of Princeton University or Princeton may not be used in  
advertising or publicity pertaining to distribution of the software  
and/or database. Title to copyright in this software, database and  
any associated documentation shall at all times remain with  
Princeton University and LICENSEE agrees to preserve same.

### Citation Information

```bibtex
@inproceedings{miller-etal-1993-semantic,
    title = "A Semantic Concordance",
    author = "Miller, George A.  and
      Leacock, Claudia  and
      Tengi, Randee  and
      Bunker, Ross T.",
    booktitle = "{H}uman {L}anguage {T}echnology: Proceedings of a Workshop Held at Plainsboro, New Jersey, March 21-24, 1993",
    year = "1993",
    url = "https://aclanthology.org/H93-1061",
}
```

### Contributions

Thanks to [@thesofakillers](https://github.com/thesofakillers) for adding this
dataset, converting from xml to csv.
