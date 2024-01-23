---
annotations_creators:
- found
configs:
- release_v1
language:
- as
- bn
- gu
- hi
- kn
- ml
- mr
- or
- pa
- ta
- te
- en
language_creators:
- crowdsourced
license:
- cc-by-nc-sa-4.0
- mit
multilinguality:
- multilingual
paperswithcode_id: xalign
pretty_name: 'XAlign'
size_categories:
- 100K<n<1M
source_datasets:
- original
tags:
- xalign
- NLG
- low-resource
- LRL
task_categories:
- table-to-text
task_ids:
- rdf-to-text
---

# Dataset Card for XAlign

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
  - [Known Limitations](#known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description
- **Homepage:** [XAlign homepage](https://github.com/tushar117/XAlign)
- **Repository:** [XAlign repo](https://github.com/tushar117/XAlign)
- **Paper:** [XAlign: Cross-lingual Fact-to-Text Alignment and Generation for Low-Resource Languages](https://arxiv.org/abs/2202.00291)
- **Leaderboard:** [Papers With Code Leaderboard for XAlign](https://paperswithcode.com/sota/data-to-text-generation-on-xalign)
- **Point of Contact:** [Tushar Abhishek](tushar.abhishek@research.iiit.ac.in)

### Dataset Summary

It consists of an extensive collection of a high quality cross-lingual fact-to-text dataset where facts are in English and corresponding sentences are in native language for person biographies. The Train & validation splits are created using distant supervision methods and Test data is generated through human annotations.

### Supported Tasks and Leaderboards
- 'Data-to-text Generation': XAlign dataset can be used to train cross-lingual data-to-text generation models. The model performance can measured through any text generation evaluation metrics by taking average across all the languages. [Sagare et al. (2022)](https://arxiv.org/abs/2209.11252) reported average BLEU score of 29.27 and average METEOR score of 53.64 over the test set.

- 'Relation Extraction': XAlign could also be used for cross-lingual relation extraction where relations in English can be extracted from associated native sentence.

See [Papers With Code Leaderboard](https://paperswithcode.com/sota/data-to-text-generation-on-xalign) for more models.

### Languages

Assamese (as), Bengali (bn), Gujarati (gu), Hindi (hi), Kannada (kn), Malayalam (ml), Marathi (mr), Oriya (or), Punjabi (pa), Tamil (ta), Telugu (te), and English (en).

## Dataset Structure

### Data Fields

Each record consist of the following entries:

- sentence (string) : Native language wikipedia sentence. (non-native language strings were removed.)
- `facts` (List[Dict]) : List of facts associated with the sentence where each fact is stored as dictionary.
- language (string) : Language identifier.

The `facts` key contains list of facts where each facts is stored as dictionary. A single record within fact list contains following entries:

- subject (string) : central entity.
- object (string) : entity or a piece of information about the subject.
- predicate (string) : relationship that connects the subject and the object.
- qualifiers (List[Dict]) : It provide additional information about the fact, is stored as list of qualifier where each record is a dictionary. The dictionary contains two keys: qualifier_predicate to represent property of qualifer and qualifier_object to store value for the qualifier's predicate.

### Data Instances
Example from English
```
{
  "sentence": "Mark Paul Briers (born 21 April 1968) is a former English cricketer.",
  "facts": [
    {
      "subject": "Mark Briers",
      "predicate": "date of birth",
      "object": "21 April 1968",
      "qualifiers": []
    },
    {
      "subject": "Mark Briers",
      "predicate": "occupation",
      "object": "cricketer",
      "qualifiers": []
    },
    {
      "subject": "Mark Briers",
      "predicate": "country of citizenship",
      "object": "United Kingdom",
      "qualifiers": []
    }
  ],
  "language": "en"
}
```
Example from one of the low-resource languages (i.e. Hindi)
```
{
  "sentence": "बोरिस पास्तेरनाक १९५८ में साहित्य के क्षेत्र में नोबेल पुरस्कार विजेता रहे हैं।",
  "facts": [
    {
      "subject": "Boris Pasternak",
      "predicate": "nominated for",
      "object": "Nobel Prize in Literature",
      "qualifiers": [
        {
          "qualifier_predicate": "point in time",
          "qualifier_subject": "1958"
        }
      ]
    }
  ],
  "language": "hi"
}
```
### Data Splits

The XAlign dataset has 3 splits: train, validation, and test. Below are the statistics the dataset.

| Dataset splits | Number of Instances in Split |
| --- | --- |
| Train | 499155 |
| Validation | 55469 |
| Test | 7425 |


## Dataset Creation

### Curation Rationale

Most of the existing Data-to-Text datasets are available in English. Also, the structured Wikidata entries for person entities in low resource languages are minuscule in number compared to that in English. Thus, monolingual Data-to-Text for low resource languages suffers from data sparsity. XAlign dataset would be useful in creation of cross-lingual Data-to-Text generation systems that take a set of English facts as input and generates a sentence capturing the fact-semantics in the specified language. 

### Source Data

#### Initial Data Collection and Normalization

The dataset creation process starts with an intial list of ~95K person entities selected from Wikidata and each of which has a link to a corresponding Wikipedia page in at least one of our 11 low resource languages. This leads to a dataset where every instance is a tuple containing entityID, English Wikidata facts, language identifier, Wikipedia URL for the entityID. The facts (in English) are extracted from the 20201221 WikiData dump for each entity using the [WikiData](https://query.wikidata.org) APIs. The facts are gathered only for the speficied Wikidata property (or relation) types that captures most useful factual information for person entities: WikibaseItem, Time, Quantity, and Monolingualtext.This leads to overall ~0.55M data instances across all the 12 languages. Also, for each language, the sentences (along with section information) are extracted from 20210520 Wikipedia XML dump using the pre-processing steps as described [here](https://arxiv.org/abs/2202.00291). 

For every (entity, language) pair, the pre-processed dataset contains a set of English Wikidata facts and a set of Wikipedia sentences in that language. In order to create train and validation dataset, these are later passed through a two-stage automatic aligner as proposed in [abhishek et al. (2022)](https://arxiv.org/abs/2202.00291) to associate a sentence with a subset of facts.

#### Who are the source language producers?

The text are extracted from Wikipedia and facts are retrieved from Wikidata.

### Annotations

#### Annotation process

The Manual annotation of Test dataset was done in two phases. For both the phases, the annotators were presented with (low resource language sentence, list of English facts). They were asked to mark facts present in the given sentence. There were also specific guidelines to ignore redundant facts, handle abbreviations, etc. More detailed annotation guidelines and ethical statement are mentioned [here](https://docs.google.com/document/d/1ucGlf-Jm1ywQ_Fjw9f2UqPeMWPlBnlZA46UY7KuZ0EE/edit)
. In the first phase, we got 60 instances labeled per language by a set of 8 expert annotators (trusted graduate students who understood the task very well). In phase 2, we selected 8 annotators per language from the [National Register of Translators](https://www.ntm.org.in/languages/english/nrtdb.aspx}). We tested these annotators using phase 1 data as golden control set, and shortlisted up to 4 annotators per language who scored highest (on Kappa score with golden annotations).

#### Who are the annotators?

Human annotators were selected appropriately (after screening) from [National Translation Mission](https://www.ntm.org.in) for Test set creation.

### Personal and Sensitive Information

The dataset does not involve collection or storage of any personally identifiable information or offensive information at any stage.

## Considerations for Using the Data

### Social Impact of Dataset

The purpose of the this dataset is to help develop cross-lingual Data-to-Text generation systems that are vital in many downstream Natural Language Processing (NLP) applications like automated dialog systems, domain-specific chatbots, open domain question answering, authoring sports reports, etc. These systems will be useful for powering business applications like Wikipedia text generation given English Infoboxes, automated generation of non-English product descriptions using English product attributes, etc.

### Known Limitations

The XAlign dataset focus only on person biographies and system developed on this dataset might not be generalized to other domains. 

## Additional Information

### Dataset Curators

This dataset is collected by Tushar Abhishek, Shivprasad Sagare, Bhavyajeet Singh, Anubhav Sharma, Manish Gupta and Vasudeva Varma of Information Retrieval and Extraction Lab (IREL), Hyderabad, India. They released [scripts](https://github.com/tushar117/xalign) to collect and process the data into the Data-to-Text format. 

### Licensing Information

The XAlign dataset is released under the [MIT License](https://github.com/tushar117/XAlign/blob/main/LICENSE).

### Citation Information

```
@article{abhishek2022xalign,
  title={XAlign: Cross-lingual Fact-to-Text Alignment and Generation for Low-Resource Languages},
  author={Abhishek, Tushar and Sagare, Shivprasad and Singh, Bhavyajeet and Sharma, Anubhav and Gupta, Manish and Varma, Vasudeva},
  journal={arXiv preprint arXiv:2202.00291},
  year={2022}
}
```

### Contributions

Thanks to [Tushar Abhishek](https://github.com/tushar117), [Shivprasad Sagare](https://github.com/ShivprasadSagare), [Bhavyajeet Singh](https://github.com/bhavyajeet), [Anubhav Sharma](https://github.com/anubhav-sharma13), [Manish Gupta](https://github.com/blitzprecision) and [Vasudeva Varma](vv@iiit.ac.in) for adding this dataset. 

Additional thanks to the annotators from National Translation Mission for their crucial contributions to creation of the test dataset: Bhaswati Bhattacharya, Aditi Sarkar, Raghunandan B. S., Satish M., Rashmi G.Rao, Vidyarashmi PN, Neelima Bhide, Anand Bapat, Krishna Rao N V, Nagalakshmi DV, Aditya Bhardwaj
Vuppula, Nirupama Patel, Asir. T, Sneha Gupta, Dinesh Kumar, Jasmin Gilani, Vivek R, Sivaprasad S, Pranoy J, Ashutosh Bharadwaj, Balaji Venkateshwar, Vinkesh Bansal, Vaishnavi Udyavara, Ramandeep Singh, Khushi Goyal, Yashasvi LN Pasumarthy and Naren Akash.