---
annotations_creators:
- no-annotation
language_creators:
- crowdsourced
language:
- he
license:
- pddl
multilinguality:
- monolingual
size_categories:
- n<1K
source_datasets:
- original
task_categories:
- text-generation
task_ids:
- language-modeling
pretty_name: Knesset Meetings Corpus
---
# Dataset Card
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
- **Homepage:** [https://zenodo.org/record/2707356](https://zenodo.org/record/2707356)
- **Repository:** [https://github.com/NLPH/knesset-2004-2005](https://github.com/NLPH/knesset-2004-2005)
- **Paper:** 
- **Point of Contact:** 
- **Size of downloaded dataset files:** 
- **Size of the generated dataset:** 
- **Total amount of disk used:**
### Dataset Summary

An example of a sample:
```
{
    "text": <text content of given document>,
    "path": <file path to docx>
}
```

Dataset usage
Available "kneset16","kneset17","knesset_tagged" configurations
And only train set.
```python
train_ds = load_dataset("imvladikon/knesset_meetings_corpus", "kneset16", split="train")
```


The Knesset Meetings Corpus 2004-2005 is made up of two components:

* Raw texts - 282 files made up of 867,725 lines together. These can be downloaded in two formats:

  * As ``doc`` files, encoded using ``windows-1255`` encoding:

    * ``kneset16.zip`` - Contains 164 text files made up of 543,228 lines together. `[MILA host] <http://yeda.cs.technion.ac.il:8088/corpus/software/corpora/knesset/txt/docs/kneset16.zip>`_ `[Github Mirror] <https://github.com/NLPH/knesset-2004-2005/blob/master/kneset16.zip?raw=true>`_
  
    * ``kneset17.zip`` - Contains 118 text files made up of 324,497 lines together. `[MILA host] <http://yeda.cs.technion.ac.il:8088/corpus/software/corpora/knesset/txt/docs/kneset17.zip>`_ `[Github Mirror] <https://github.com/NLPH/knesset-2004-2005/blob/master/kneset17.zip?raw=true>`_
  
  * As ``txt`` files, encoded using ``utf8`` encoding:

    * ``kneset.tar.gz`` - An archive of all the raw text files, divided into two folders: `[Github mirror] <https://github.com/NLPH/knesset-2004-2005/blob/master/kneset.tar.gz>`_

      * ``16`` - Contains 164 text files made up of 543,228 lines together.
  
      * ``17`` - Contains 118 text files made up of 324,497 lines together.
    
    * ``knesset_txt_16.tar.gz``- Contains 164 text files made up of 543,228 lines together. `[MILA host] <http://yeda.cs.technion.ac.il:8088/corpus/software/corpora/knesset/txt/utf8/knesset_txt_16.tar.gz>`_ `[Github Mirror] <https://github.com/NLPH/knesset-2004-2005/blob/master/knesset_txt_16.tar.gz?raw=true>`_
    
    * ``knesset_txt_17.zip`` - Contains 118 text files made up of 324,497 lines together. `[MILA host] <http://yeda.cs.technion.ac.il:8088/corpus/software/corpora/knesset/txt/utf8/knesset_txt_17.zip>`_ `[Github Mirror] <https://github.com/NLPH/knesset-2004-2005/blob/master/knesset_txt_17.zip?raw=true>`_
 
* Tokenized and morphologically tagged texts - Tagged versions exist only for the files in the ``16`` folder. The texts are encoded using `MILA's XML schema for corpora <http://www.mila.cs.technion.ac.il/eng/resources_standards.html>`_. These can be downloaded in two ways:

  * ``knesset_tagged_16.tar.gz`` - An archive of all tokenized and tagged files. `[MILA host] <http://yeda.cs.technion.ac.il:8088/corpus/software/corpora/knesset/tagged/knesset_tagged_16.tar.gz>`_ `[Archive.org mirror] <https://archive.org/details/knesset_transcripts_2004_2005>`_
  
    
Mirrors
-------

This repository is a mirror of this dataset `found on MILA's website <http://www.mila.cs.technion.ac.il/eng/resources_corpora_haknesset.html>`_.

Zenodo mirror: `https://zenodo.org/record/2707356 <https://zenodo.org/record/2707356>`_
    
    
License
-------

All Knesset meeting protocols are in the `public domain <https://en.wikipedia.org/wiki/Public_domain>`_ (`רשות הציבור <https://he.wikipedia.org/wiki/%D7%A8%D7%A9%D7%95%D7%AA_%D7%94%D7%A6%D7%99%D7%91%D7%95%D7%A8>`_) by law. These files are thus in the public doamin and do not require any license or public domain dedication to set their status.

.. |DOI| image:: https://zenodo.org/badge/DOI/10.5281/zenodo.2707356.svg
   :target: https://doi.org/10.5281/zenodo.2707356

.. |LICENCE| image:: https://github.com/NLPH/knesset-2004-2005/blob/master/public_domain_shield.svg
   :target: https://en.wikipedia.org/wiki/Public_domain

.. |PUBDOM| image:: https://github.com/NLPH/knesset-2004-2005/blob/master/public_domain.png
   :target: https://en.wikipedia.org/wiki/Public_domain
### Supported Tasks and Leaderboards
[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
### Languages
[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
## Dataset Structure


## Dataset Creation
### Curation Rationale
[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
### Source Data
#### Initial Data Collection and Normalization
[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
#### Who are the source language producers?
[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
### Annotations
#### Annotation process
[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
#### Who are the annotators?
[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
### Personal and Sensitive Information
[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
## Considerations for Using the Data
### Social Impact of Dataset
[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
### Discussion of Biases
[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
### Other Known Limitations
[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
## Additional Information
### Dataset Curators
[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
### Licensing Information
The dataset is available under the [ Open Data Commons Public Domain Dedication & License 1.0](https://opendatacommons.org/licenses/pddl/).
### Citation Information
[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Contributions
