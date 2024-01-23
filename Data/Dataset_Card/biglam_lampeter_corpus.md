---
annotations_creators:
- no-annotation
paperswithcode_id: null
language:
- en
language_creators:
- found
license:
- cc-by-sa-3.0
multilinguality:
- monolingual
pretty_name: Lampeter Corpus
size_categories:
- n<1K
source_datasets:
- original
task_categories:
- text-classification
task_ids:
- multi-label-classification
- multi-class-classification
---
# Dataset Card for lampeter_corpus

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-instances)
  - [Data Splits](#data-instances)
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

## Dataset Description

- **Homepage:** https://ota.bodleian.ox.ac.uk/repository/xmlui/handle/20.500.12024/3193
- **Repository:** [Needs More Information]
- **Paper:** [Needs More Information]
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** Josef Schmied, Claudia Claridge, Rainer Siemund

### Dataset Summary

The Lampeter Corpus of Early Modern English Tracts is a collection of texts on various subject matter published between 1640 and 1740,  a time that was marked by the rise of mass publication, the development of public discourse in many areas of everyday life and last but not least, the standardisation of British English. Each text belongs to one of the following genres:  Law, Economy, Religion, Politics, Science, Miscellaneous

### Supported Tasks and Leaderboards

- `text-classification`: This dataset comes with dates and genre classifications for each text which can be used to finetune a model for text classification. 

### Languages

The text in the dataset is British English. The associated BCP-47 code is `en-GB`

## Dataset Structure

### Data Instances

A typical data point contains an id, a text, the head of the text (which can be missing on some occasions) and the title. The two features which can be used for classification are `date`, which is the year of publication and `genre` which classifies the text into one of six broad areas.
```
{
'id': 'SciB1735', 
'text': '\nI. WHEN I read your Defence of the British Mathematicians, I could not, Sir, but admire your Courage in asserting with such undoubting Assurance things so easily disproved. This to me seemed unaccountable, till I reflected on what you say (p. 32.) when upon my having appealed to every thinking Reader, whether it be possible to frame any clear Conception of Fluxions, you express yourself in the following manner, "Pray, Sir, who are those thinking Readers you ap\npeal to? Are they Geometricians, or Persons wholly ignorant of Geometry? If the former, I leave it to them: If the latter, I ask how well are they qualified to judge of the Method of Fluxions"? It must be acknowledged you seem by this Dilemma secure in the favour of one Part of your Readers, and the ignorance of the other. I am nevertheless persuaded there are fair and candid Men among the Mathematicians. And for those who are not Mathematicians, I shall endeavour so to unveil this Mystery, [TRUNCATED]', 
'date': '1735', 
'genre': 'Science', '
head': 'A DEFENCE OF FREE-THINKING IN Mathematics; &c.\n', 
'title': 'A defence of free-thinking in mathematics [...]'
}
```

### Data Fields

The dataset contains the following fields: 

- `id`: Unique identifier("string"),
- `text`: ext in the document("string"),
- `date`: Date of publication("date64"),
- `genre`: Broad classification("string"),
- `head`: Often same as title. Can be missing("string"),
- `title`: Title of document("string")


### Data Splits

Train: 120

## Dataset Creation

### Curation Rationale

The period covered by the Lampeter Corpus, 1640 to 1740, marks a crucial period in English history and the elaboration of English as a multi-purpose language. The texts selected for the corpus reflect the standardisation process of English and historical developments between the outbreak of the Civil War and the beginning of the Industrial Revolution. To meet the needs of linguists and historians alike, the Lampeter project has attempted to create a balanced corpus rather than a randomly chosen archive or collection. A balanced corpus, then, is characterised by several transparent sampling criteria.

### Source Data

#### Initial Data Collection and Normalization

The original data is selected according to the following criteria:
- Complete texts only, including dedications, prefaces, postscripts, etc.
- Texts are of varying length, ranging from c. 3,000 to c. 20,000 words.
- Each author appears only once to avoid idiosyncratic language use.
- Major literary figures of the time were excluded since their writing style can be studied in other, existing collections.
- Generally, only first editions of the texts; later editions only if changes were made by the original authors, thus ensuring the authenticity of the language.

#### Who are the source language producers?

Authors of texts between 1640-1740

### Annotations

#### Annotation process

N/A

#### Who are the annotators?

N/A

### Personal and Sensitive Information

N/A

## Considerations for Using the Data

### Social Impact of Dataset

N/A

### Discussion of Biases

The social biases of the time in terms of race, sex, gender, etc. might be encountered in this dataset

### Other Known Limitations

None

## Additional Information

### Dataset Curators

Josef Schmied, Claudia Claridge, Rainer Siemund

### Licensing Information

Creative Commons Attribution-ShareAlike 3.0 Unported (CC BY-SA 3.0)

### Citation Information

University of Oxford, The Lampeter Corpus of Early Modern English Tracts, Oxford Text Archive, http://hdl.handle.net/20.500.12024/3193.