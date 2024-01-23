---

# Dataset Card for KAMEL: Knowledge Analysis with Multitoken Entities in Language Models
## Table of Contents
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
https://github.com/JanKalo/KAMEL
- **Repository:**
https://github.com/JanKalo/KAMEL
- **Paper:**
@inproceedings{kalo2022kamel,
  title={KAMEL: Knowledge Analysis with Multitoken Entities in Language Models},
  author={Kalo, Jan-Christoph and Fichtel, Leandra},
  booktitle={Automated Knowledge Base Construction},
  year={2022}
}
### Dataset Summary
This dataset provides the data for KAMEL, a probing dataset for language models that contains factual knowledge
from Wikidata and Wikipedia.

See the paper for more details.  For more information, also see:
https://github.com/JanKalo/KAMEL
### Languages
en
## Dataset Structure
### Data Instances


### Data Fields
KAMEL has the following fields:
* index: the id
* sub_label: a label for the subject 
* obj_uri: Wikidata uri for the object 
* obj_labels:  multiple labels for the object
* chosen_label: the preferred label  
* rel_uri: Wikidata uri for the relation
* rel_label: a label for the relation

### Data Splits
The dataset is split into a training, validation, and test dataset.
It contains 234 Wikidata relations. 
For each relation there exist 200 training, 100 validation,
and 100 test instances.

## Dataset Creation
### Curation Rationale
This dataset was gathered and created to explore what knowledge graph facts are memorized by large language models.
### Source Data
#### Initial Data Collection and Normalization
See the reaserch paper and website for more detail. The dataset was
created from Wikidata and Wikipedia.
### Annotations
#### Annotation process
There is no human annotation, but only automatic linking from Wikidata facts to Wikipedia articles.
The details about the process can be found in the paper.
#### Who are the annotators?
Machine Annotations
### Personal and Sensitive Information
Unkown, but likely information about famous people mentioned in the English Wikipedia.
## Considerations for Using the Data
### Social Impact of Dataset
The goal for the work is to probe the understanding of language models.
### Discussion of Biases
Since the data is created from Wikipedia and Wikidata, the existing biases from these two data sources may also be reflected in KAMEL.
## Additional Information
### Dataset Curators
The authors of KAMEL at Vrije Universiteit Amsterdam and Technische Universität Braunschweig.
### Licensing Information
The Creative Commons Attribution-Noncommercial 4.0 International License. see https://github.com/facebookresearch/LAMA/blob/master/LICENSE
### Citation Information
@inproceedings{kalo2022kamel,
  title={KAMEL: Knowledge Analysis with Multitoken Entities in Language Models},
  author={Kalo, Jan-Christoph and Fichtel, Leandra},
  booktitle={Automated Knowledge Base Construction},
  year={2022}
}

