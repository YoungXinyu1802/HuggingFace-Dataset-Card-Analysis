---
annotations_creators:
- expert-generated
- crowdsourced
language:
- nl
language_creators:
- machine-generated
license:
- cc-by-2.0
multilinguality:
- monolingual
pretty_name: Contentious Contexts Corpus
size_categories:
- 1K<n<10K
source_datasets:
- original
tags:
- newspapers
- historic
- dutch
- problematic
- ConConCor
task_categories:
- text-classification
task_ids:
- sentiment-scoring
- multi-label-classification
---
# Dataset Card for Contentious Contexts Corpus

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

- **Homepage:** [ConConCor](https://github.com/cultural-ai/ConConCor)

- **Repository:** [ConConCor](https://github.com/cultural-ai/ConConCor)
- **Paper:** [N/A]
- **Leaderboard:** [N/A]
- **Point of Contact:** [Jacco van Ossenbruggen](https://github.com/jrvosse)

**Note** One can also find a Datasheet produced by the creators of this dataset as a [PDF document](https://github.com/cultural-ai/ConConCor/blob/main/Dataset/DataSheet.pdf)

### Dataset Summary

This dataset contains extracts from historical Dutch newspapers containing keywords of potentially contentious words (according to present-day sensibilities). The dataset contains multiple annotations per instance, given the option to quantify agreement scores for annotations. This dataset can be used to track how words and their meanings have changed over time

### Supported Tasks and Leaderboards

- `text-classification`: This dataset can be used for tracking how the meanings of words in different contexts have changed and become contentious over time

### Languages

The text in the dataset is in Dutch. The responses are available in both English and Dutch. Suggestions, where present, are only in Dutch. The associated BCP-47 code is `nl`


## Dataset Structure

### Data Instances

```
{
  'extract_id': 'H97', 
  'text': 'en waardoor het eerste doel wordt voorbijgestreefd om voor den 5D5c5Y   5d-5@5j5g5d5e5Z5V5V5c een speciale eigen werkingssfeer te 
   scheppen.Intusschen is het', 
  'target': '5D           5c5Y5d-5@5j5g5d5e5Z5V5V5c', 
  'annotator_responses_english': [
    {'id': 'unknown_2a', 'response': 'Not contentious'}, 
    {'id': 'unknown_2b', 'response': 'Contentious according to current standards'}, 
    {'id': 'unknown_2c', 'response': "I don't know"}, 
    {'id': 'unknown_2d', 'response': 'Contentious according to current standards'}, 
    {'id': 'unknown_2e', 'response': 'Not contentious'}, 
    {'id': 'unknown_2f', 'response': "I don't know"}, 
    {'id': 'unknown_2g', 'response': 'Not contentious'}], 
  'annotator_responses_dutch': [
    {'id': 'unknown_2a', 'response': 'Niet omstreden'},
    {'id': 'unknown_2b', 'response': 'Omstreden naar huidige maatstaven'}, 
    {'id': 'unknown_2c', 'response': 'Weet ik niet'}, 
    {'id': 'unknown_2d', 'response': 'Omstreden naar huidige maatstaven'}, 
    {'id': 'unknown_2e', 'response': 'Niet omstreden'}, 
    {'id': 'unknown_2f', 'response': 'Weet ik niet'}, 
    {'id': 'unknown_2g', 'response': 'Niet omstreden'}], 
  'annotator_suggestions': [
    {'id': 'unknown_2a', 'suggestion': ''}, 
    {'id': 'unknown_2b', 'suggestion': 'ander ras nodig'}, 
    {'id': 'unknown_2c', 'suggestion': 'personen van ander ras'}, 
    {'id': 'unknown_2d', 'suggestion': ''},
    {'id': 'unknown_2e', 'suggestion': ''}, 
    {'id': 'unknown_2f', 'suggestion': ''}, 
    {'id': 'unknown_2g', 'suggestion': 'ras'}]
}
```

### Data Fields

|extract_id|text|target|annotator_responses_english|annotator_responses_dutch|annotator_suggestions|
|---|---|---|---|---|---|
|Unique identifier|Text|Target phrase or word|Response(translated to English)|Response in Dutch|Suggestions, if present|


### Data Splits

Train: 2720

## Dataset Creation

### Curation Rationale

> Cultural heritage institutions recognise the problem of language use in their collections. The cultural objects in archives, libraries, and museums contain words and phrases that are inappropriate in modern society but were used broadly back in times. Such words can be offensive and discriminative. In our work, we use the term "contentious" to refer to all (potentially) inappropriate or otherwise sensitive words. For example, words suggestive of some (implicit or explicit) bias towards or against something. The National Archives of the Netherlands stated that they "explore the possibility of explaining language that was acceptable and common in the past and providing it with contemporary alternatives", meanwhile "keeping the original descriptions [with contentious words], because they give an idea of the time in which they were made or included in the collection". There is a page on the institution website where people can report "offensive language".

### Source Data

#### Initial Data Collection and Normalization

> The queries were run on OCR'd versions of the Europeana Newspaper collection, as provided by the KB National Library of the Netherlands. We limited our pool to text categorised as "article", thus excluding other types of texts such as advertisements and family notices. We then only focused our sample on the 6 decades between 1890-01-01 and 1941-12-31, as this is the period available in the Europeana newspaper corpus. The dataset represents a stratified sample set over target word, decade, and newspaper issue distribution metadata. For the final set of extracts for annotation, we gave extracts sampling weights proportional to their actual probabilities, as estimated from the initial set of extracts via trigram frequencies, rather than sampling uniformly.

#### Who are the source language producers?

[N/A]

### Annotations

#### Annotation process

> The annotation process included 3 stages: pilot annotation, expert annotation, and crowdsourced annotation on the "Prolific" platform. All stages required the participation of Dutch speakers. The pilot stage was intended for testing the annotation layout, the instructions clarity, the number of sentences provided as context, the survey questions, and the difficulty of the task in general. The Dutch-speaking members of the Cultural AI Lab were asked to test the annotation process and give their feedback anonymously using Google Sheets. Six volunteers contributed to the pilot stage, each annotating the same 40 samples where either a context of 3 or 5 sentences surrounding the term were given. An individual annotation sheet had a table layout with 4 options to choose for every sample
> - 'Omstreden'(Contentious)
> - 'Niet omstreden'(Not contentious)
> - 'Weet ik niet'(I don't know)
> - 'Onleesbare OCR'(Illegible OCR)</br>
2 open fields 
> - 'Andere omstreden termen in de context'(Other contentious terms in the context)
> - 'Notities'(Notes)</br>
and the instructions in the header. The rows were the samples with the highlighted words, the tickboxes for every option, and 2 empty cells for the open questions. The obligatory part of the annotation was to select one of the 4 options for every sample. Finding other contentious terms in the given sample, leaving notes, and answering 4 additional open questions at the end of the task were optional. Based on the received feedback and the answers to the open questions in the pilot study, the following decisions were made regarding the next, experts' annotation stage:
> - The annotation layout was built in Google Forms as a questionnaire instead of the table layout in Google Sheets to make the data collection and analysis faster as the number of participants would increase;
> - The context window of 5 sentences per sample was found optimal;
> - The number of samples per annotator was increased to 50;
> - The option 'Omstreden' (Contentious) was changed to 'Omstreden naar huidige maatstaven' ('Contentious according to current standards') to clarify that annotators should judge contentiousness of the word's use in context from today's perspective;
> - The annotation instruction was edited to clarify 2 points: (1) that annotators while judging contentiousness should take into account not only a bolded word but also the context surrounding it, and (2) if a word seems even slightly contentious to an annotator, they should choose the option 'Omstreden naar huidige maatstaven' (Contentious according to current standards);
> - The non-required field for every sample 'Notities' (Notes) was removed as there was an open question at the end of the annotation, where participants could leave their comments;
> - Another open question was added at the end of the annotation asking how much time it took to complete the annotation.

#### Who are the annotators?

Volunteers and Expert annotators 

### Personal and Sensitive Information

[N/A]

## Considerations for Using the Data

## Accessing the annotations 

Each example text has multiple annotations. These annotations may not always agree. There are various approaches one could take to calculate agreement, including a majority vote, rating some annotators more highly, or calculating a score based on the 'votes' of annotators. Since there are many ways of doing this, we have not implemented this as part of the dataset loading script.  

An example of how one could generate an "OCR quality rating" based on the number of times an annotator labelled an example with `Illegible OCR`:

```python 
from collections import Counter


def calculate_ocr_score(example):
    annotator_responses = [response['response'] for response in example['annotator_responses_english']]
    counts = Counter(annotator_responses)
    bad_ocr_ratings = counts.get("Illegible OCR")
    if bad_ocr_ratings is None:
        bad_ocr_ratings = 0
    return round(1 - bad_ocr_ratings/len(annotator_responses),3)
 
 
 dataset = dataset.map(lambda example: {"ocr_score":calculate_ocr_score(example)})
 ```
        
To take the majority vote (or return a tie) based on whether a example is labelled contentious or not:

```python

def most_common_vote(example):
    annotator_responses = [response['response'] for response in example['annotator_responses_english']]
    counts = Counter(annotator_responses)
    contentious_count = counts.get("Contentious according to current standards")
    if not contentious_count:
        contentious_count = 0
    not_contentious_count = counts.get("Not contentious")
    if not not_contentious_count:
        not_contentious_count = 0
    if contentious_count > not_contentious_count:
        return "contentious"
    if contentious_count < not_contentious_count:
        return "not_contentious"
    if contentious_count == not_contentious_count:
        return "tied"
```

### Social Impact of Dataset

This dataset can be used to see how words change in meaning over time

### Discussion of Biases

> Due to the nature of the project, some examples used in this documentation may be shocking or offensive. They are provided only as an illustration or explanation of the resulting dataset and do not reflect the opinions of the project team or their organisations.

Since this project was explicitly created to help assess bias, it should be used primarily in the context of assess bias, and methods for detecting bias. 


### Other Known Limitations

[Needs More Information]

## Additional Information

### Dataset Curators

[Cultural AI](https://github.com/cultural-ai)

### Licensing Information

CC-BY

### Citation Information

```
@misc{ContentiousContextsCorpus2021,
  author = {Cultural AI},
  title = {Contentious Contexts Corpus},
  year = {2021},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\\url{https://github.com/cultural-ai/ConConCor}},
}
```