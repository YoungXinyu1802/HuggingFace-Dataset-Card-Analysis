---
annotations_creators:
- expert-generated
language:
- eu
language_creators:
- expert-generated
license:
- cc-by-nc-sa-4.0
multilinguality:
- monolingual
pretty_name: BasqueGLUE
size_categories:
- 100K<n<1M
source_datasets:
- original
tags: []
task_categories:
- text-classification
- token-classification
task_ids:
- intent-classification
- natural-language-inference
- sentiment-classification
- topic-classification
- named-entity-recognition
- coreference-resolution
configs:
- bec
- bhtc
- coref
- intent
- nerc_id
- nerc_od
- qnli
- slot
- vaxx
- wic
dataset_info:
- config_name: bec
  features:
  - name: text
    dtype: string
  - name: label
    dtype:
      class_label:
        names:
          '0': N
          '1': NEU
          '2': P
  - name: idx
    dtype: int32
  splits:
  - name: train
    num_bytes: 693284
    num_examples: 6078
  - name: test
    num_bytes: 148510
    num_examples: 1302
  - name: validation
    num_bytes: 148377
    num_examples: 1302
  download_size: 1217803
  dataset_size: 990171
- config_name: bhtc
  features:
  - name: text
    dtype: string
  - name: label
    dtype:
      class_label:
        names:
          '0': Ekonomia
          '1': Euskal Herria
          '2': Euskara
          '3': Gizartea
          '4': Historia
          '5': Ingurumena
          '6': Iritzia
          '7': Komunikazioa
          '8': Kultura
          '9': Nazioartea
          '10': Politika
          '11': Zientzia
  - name: idx
    dtype: int32
  splits:
  - name: train
    num_bytes: 2431494
    num_examples: 8585
  - name: test
    num_bytes: 523066
    num_examples: 1854
  - name: validation
    num_bytes: 519555
    num_examples: 1857
  download_size: 3896312
  dataset_size: 3474115
- config_name: coref
  features:
  - name: text
    dtype: string
  - name: span1_text
    dtype: string
  - name: span2_text
    dtype: string
  - name: label
    dtype:
      class_label:
        names:
          '0': 'false'
          '1': 'true'
  - name: span1_index
    dtype: int32
  - name: span2_index
    dtype: int32
  - name: idx
    dtype: int32
  splits:
  - name: train
    num_bytes: 365830
    num_examples: 986
  - name: test
    num_bytes: 201378
    num_examples: 587
  - name: validation
    num_bytes: 108632
    num_examples: 320
  download_size: 855074
  dataset_size: 675840
- config_name: intent
  features:
  - name: text
    dtype: string
  - name: label
    dtype:
      class_label:
        names:
          '0': alarm/cancel_alarm
          '1': alarm/modify_alarm
          '2': alarm/set_alarm
          '3': alarm/show_alarms
          '4': alarm/snooze_alarm
          '5': alarm/time_left_on_alarm
          '6': reminder/cancel_reminder
          '7': reminder/set_reminder
          '8': reminder/show_reminders
          '9': weather/checkSunrise
          '10': weather/checkSunset
          '11': weather/find
  - name: idx
    dtype: int32
  splits:
  - name: train
    num_bytes: 182856
    num_examples: 3418
  - name: test
    num_bytes: 56118
    num_examples: 1087
  - name: validation
    num_bytes: 101644
    num_examples: 1904
  download_size: 595375
  dataset_size: 340618
- config_name: nerc_id
  features:
  - name: tokens
    sequence: string
  - name: tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-LOC
          '4': I-LOC
          '5': B-ORG
          '6': I-ORG
          '7': B-MISC
          '8': I-MISC
  - name: idx
    dtype: int32
  splits:
  - name: train
    num_bytes: 946007
    num_examples: 2842
  - name: test
    num_bytes: 653960
    num_examples: 1846
  - name: validation
    num_bytes: 237464
    num_examples: 711
  download_size: 1723325
  dataset_size: 1837431
- config_name: nerc_od
  features:
  - name: tokens
    sequence: string
  - name: tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-LOC
          '4': I-LOC
          '5': B-ORG
          '6': I-ORG
          '7': B-MISC
          '8': I-MISC
  - name: idx
    dtype: int32
  splits:
  - name: train
    num_bytes: 1183471
    num_examples: 3553
  - name: test
    num_bytes: 262853
    num_examples: 598
  - name: validation
    num_bytes: 270028
    num_examples: 601
  download_size: 1613369
  dataset_size: 1716352
- config_name: qnli
  features:
  - name: question
    dtype: string
  - name: sentence
    dtype: string
  - name: label
    dtype:
      class_label:
        names:
          '0': entailment
          '1': not_entailment
  - name: idx
    dtype: int32
  splits:
  - name: train
    num_bytes: 327189
    num_examples: 1764
  - name: test
    num_bytes: 42569
    num_examples: 238
  - name: validation
    num_bytes: 46359
    num_examples: 230
  download_size: 532399
  dataset_size: 416117
- config_name: slot
  features:
  - name: tokens
    sequence: string
  - name: tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-datetime
          '2': B-location
          '3': B-negation
          '4': B-alarm/alarm_modifier
          '5': B-alarm/recurring_period
          '6': B-reminder/noun
          '7': B-reminder/todo
          '8': B-reminder/reference
          '9': B-reminder/recurring_period
          '10': B-weather/attribute
          '11': B-weather/noun
          '12': I-datetime
          '13': I-location
          '14': I-negation
          '15': I-alarm/alarm_modifier
          '16': I-alarm/recurring_period
          '17': I-reminder/noun
          '18': I-reminder/todo
          '19': I-reminder/reference
          '20': I-reminder/recurring_period
          '21': I-weather/attribute
          '22': I-weather/noun
  - name: idx
    dtype: int32
  splits:
  - name: train
    num_bytes: 388774
    num_examples: 3418
  - name: test
    num_bytes: 114876
    num_examples: 1088
  - name: validation
    num_bytes: 214053
    num_examples: 1900
  download_size: 962250
  dataset_size: 717703
- config_name: vaxx
  features:
  - name: text
    dtype: string
  - name: label
    dtype:
      class_label:
        names:
          '0': AGAINST
          '1': NONE
          '2': FAVOR
  - name: idx
    dtype: int32
  splits:
  - name: train
    num_bytes: 176436
    num_examples: 864
  - name: test
    num_bytes: 70947
    num_examples: 312
  - name: validation
    num_bytes: 42795
    num_examples: 206
  download_size: 333997
  dataset_size: 290178
- config_name: wic
  features:
  - name: sentence1
    dtype: string
  - name: sentence2
    dtype: string
  - name: word
    dtype: string
  - name: label
    dtype:
      class_label:
        names:
          '0': 'false'
          '1': 'true'
  - name: start1
    dtype: int32
  - name: start2
    dtype: int32
  - name: end1
    dtype: int32
  - name: end2
    dtype: int32
  - name: idx
    dtype: int32
  splits:
  - name: train
    num_bytes: 172847108
    num_examples: 408559
  - name: test
    num_bytes: 589578
    num_examples: 1400
  - name: validation
    num_bytes: 251549
    num_examples: 600
  download_size: 22938354
  dataset_size: 173688235
---

# Dataset Card for BasqueGLUE

## Table of Contents

* [Table of Contents](#table-of-contents)
* [Dataset Description](#dataset-description) 
  * [Dataset Summary](#dataset-summary)
  * [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  * [Languages](#languages)
* [Dataset Structure](#dataset-structure) 
  * [Data Instances](#data-instances)
  * [Data Fields](#data-fields)
  * [Data Splits](#data-splits)
* [Dataset Creation](#dataset-creation) 
  * [Curation Rationale](#curation-rationale)
  * [Source Data](#source-data)
  * [Annotations](#annotations)
  * [Personal and Sensitive Information](#personal-and-sensitive-information)
* [Considerations for Using the Data](#considerations-for-using-the-data) 
  * [Social Impact of Dataset](#social-impact-of-dataset)
  * [Discussion of Biases](#discussion-of-biases)
  * [Other Known Limitations](#other-known-limitations)
* [Additional Information](#additional-information) 
  * [Dataset Curators](#dataset-curators)
  * [Licensing Information](#licensing-information)
  * [Citation Information](#citation-information)
  * [Contributions](#contributions)

## Dataset Description

* **Repository:** <https://github.com/orai-nlp/BasqueGLUE>
* **Paper:** [BasqueGLUE: A Natural Language Understanding Benchmark for Basque](http://www.lrec-conf.org/proceedings/lrec2022/pdf/2022.lrec-1.172.pdf)
* **Point of Contact:** [Contact Information](https://github.com/orai-nlp/BasqueGLUE#contact-information)

### Dataset Summary

Natural Language Understanding (NLU) technology has improved significantly over the last few years, and multitask benchmarks such as GLUE are key to evaluate this improvement in a robust and general way. These benchmarks take into account a wide and diverse set of NLU tasks that require some form of language understanding, beyond the detection of superficial, textual clues. However, they are costly to develop and language-dependent, and therefore they are only available for a small number of languages.

We present BasqueGLUE, the first NLU benchmark for Basque, which has been elaborated from previously existing datasets and following similar criteria to those used for the construction of GLUE and SuperGLUE. BasqueGLUE is freely available under an open license.

| Dataset        | \|Train\| | \|Val\| | \|Test\| | Task                   | Metric | Domain          |
|----------------|----------:|--------:|---------:|------------------------|:------:|-----------------|
| NERCid         |   51,539  |  12,936 |  35,855  | NERC                   | F1     | News            |
| NERCood        |   64,475  |  14,945 |  14,462  | NERC                   | F1     | News, Wikipedia |
| FMTODeu_intent |    3,418  |   1,904 |   1,087  | Intent classification  | F1     | Dialog system   |
| FMTODeu_slot   |   19,652  |  10,791 |   5,633  | Slot filling           | F1     | Dialog system   |
| BHTCv2         |    8,585  |   1,857 |   1,854  | Topic classification   | F1     | News            |
| BEC2016eu      |    6,078  |   1,302 |   1,302  | Sentiment analysis     | F1     | Twitter         |
| VaxxStance     |      864  |     206 |     312  | Stance detection       | MF1*   | Twitter         |
| QNLIeu         |    1,764  |     230 |     238  | QA/NLI                 | Acc    | Wikipedia       |
| WiCeu          |  408,559  |     600 |   1,400  | WSD                    | Acc    | Wordnet         |
| EpecKorrefBin  |      986  |     320 |     587  | Coreference resolution | Acc    | News            |

### Supported Tasks and Leaderboards

This benchmark comprises the following tasks:

#### NERCid

This dataset contains sentences from the news domain with manually annotated named entities. The data is the merge of EIEC (a dataset of a collection of news wire articles from Euskaldunon Egunkaria newspaper, (Alegria et al. 2004)), and newly annotated data from naiz.eus. The data is annotated following the BIO annotation scheme over four categories: person, organization, location, and miscellaneous.

#### NERCood

This dataset contains sentences with manually annotated named entities. The training data is the merge of EIEC (a dataset of a collection of news wire articles from Euskaldunon Egunkaria newspaper, (Alegria et al. 2004)), and newly annotated data from naiz.eus. The data is annotated following the BIO annotation scheme over four categories: person, organization, location, and miscellaneous. For validation and test sets, sentences from Wikipedia were annotated following the same annotation guidelines.

#### FMTODeu_intent

This dataset contains utterance texts and intent annotations drawn from the manually-annotated Facebook Multilingual Task Oriented Dataset (FMTOD) (Schuster et al. 2019). Basque translated data was drawn from the datasets created for Building a Task-oriented Dialog System for languages with no training data: the Case for Basque (de Lacalle et al. 2020). The examples are annotated with one of 12 different intent classes corresponding to alarm, reminder or weather related actions.

#### FMTODeu_slot

This dataset contains utterance texts and sequence intent argument annotations designed for slot filling tasks, drawn from the manually-annotated Facebook Multilingual Task Oriented Dataset (FMTOD) (Schuster et al. 2019). Basque translated data was drawn from the datasets created for Building a Task-oriented Dialog System for languages with no training data: the Case for Basque (de Lacalle et al. 2020). The task is a sequence labelling task similar to NERC, following BIO annotation scheme over 11 categories.

#### BHTCv2

The corpus contains 12,296 news headlines (brief article descriptions) from the Basque weekly newspaper [Argia](https://www.argia.eus). Topics are classified uniquely according to twelve thematic categories.

#### BEC2016eu

The Basque Election Campaign 2016 Opinion Dataset (BEC2016eu) is a new dataset for the task of sentiment analysis, a sequence classification task, which contains tweets about the campaign for the Basque elections from 2016. The crawling was carried out during the election campaign period (2016/09/09-2016/09/23), by monitoring the main parties and their respective candidates. The tweets were manually annotated as positive, negative or neutral.

#### VaxxStance

The VaxxStance (Agerri et al., 2021) dataset originally provides texts and stance annotations for social media texts around the anti-vaccine movement. Texts are given a label indicating whether they express an AGAINST, FAVOR or NEUTRAL stance towards the topic.

#### QNLIeu

This task includes the QA dataset ElkarHizketak (Otegi et al. 2020), a low resource conversational Question Answering (QA) dataset for Basque created by native speaker volunteers. The dataset is built on top of Wikipedia sections about popular people and organizations, and it contains around 400 dialogues and 1600 question and answer pairs. The task was adapted into a sentence-pair binary classification task, following the design of QNLI for English (Wang et al. 2019). Each question and answer pair are given a label indicating whether the answer is entailed by the question.

#### WiCeu

Word in Context or WiC (Pilehvar and Camacho-Collados 2019) is a word sense disambiguation (WSD) task, designed as a particular form of sentence pair binary classification. Given two text snippets and a polyse mous word that appears in both of them (the span of the word is marked in both snippets), the task is to determine whether the word has the same sense in both sentences. This dataset is based on the EPEC-EuSemcor (Pociello et al. 2011) sense-tagged corpus.

#### EpecKorrefBin

EPEC-KORREF-Bin is a dataset derived from EPEC-KORREF (Soraluze et al. 2012), a corpus of Basque news documents with manually annotated mentions and coreference chains, which we have been converted into a binary classification task. In this task, the model has to predict whether two mentions from a text, which can be pronouns, nouns or noun phrases, are referring to the same entity.

#### Leaderboard

Results obtained for two BERT base models as a baseline for the Benchmark.


|                                                            |  AVG  |  NERC |  F_intent | F_slot  |  BHTC |  BEC  |  Vaxx |  QNLI |  WiC  | coref |
|------------------------------------------------------------|:-----:|:-----:|:---------:|:-------:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| Model                                                      |       |   F1  |    F1     |   F1    |   F1  |   F1  |  MF1  |  acc  |  acc  |  acc  |
|[BERTeus](https://huggingface.co/ixa-ehu/berteus-base-cased)| 73.23 | 81.92 |   82.52   |  74.34  | 78.26 | 69.43 | 59.30 | 74.26 | 70.71 | 68.31 |
|[ElhBERTeu](https://huggingface.co/elh-eus/ElhBERTeu)       | 73.71 | 82.30 |   82.24   |  75.64  | 78.05 | 69.89 | 63.81 | 73.84 | 71.71 | 65.93 |

The results obtained on NERC are the average of in-domain and out-of-domain NERC.

### Languages

Data are available in Basque (BCP-47 `eu`)

## Dataset Structure

### Data Instances

#### NERCid/NERCood

An example of 'train' looks as follows:
```
{
  "idx": 0,
  "tags": ["O", "O", "O", "O", "B-ORG", "O", ...],
  "tokens": ["Greba", "orokorrera", "deitu", "du", "EHk", "27rako", ...]
}
```
#### FMTODeu_intent

An example of 'train' looks as follows:
```
{
  "idx": 0,
  "label": "alarm/modify_alarm", 
  "text": "aldatu alarma 7am-tik 7pm-ra , mesedez"
}
```
#### FMTODeu_slot

An example of 'train' looks as follows:
```
{
  "idx": 923, 
  "tags": ["O", "B-reminder/todo", "I-datetime", "I-datetime", "B-reminder/todo"], 
  "tokens": ["gogoratu", "zaborra", "gaur", "gauean", "ateratzea"]
}
```
#### BHTCv2

An example of 'test' looks as follows:
```
{
  "idx": 0, 
  "label": "Gizartea", 
  "text": "Genero berdintasunaz, hezkuntzaz eta klase gizarteaz hamar liburu baino gehiago..."
}
```
#### BEC2016eu

An example of 'test' looks as follows:

```
{
  "idx": 0,
  "label": "NEU",
  "text": '"Emandako hitza bete egingo dut" Urkullu\nBa galdeketa enegarrenez daramazue programan (ta zuen AHTa...)\n#I25debatea #URL"'
}
```

#### VaxxStance

An example of 'train' looks as follows:
```
{
  "idx": 0, 
  "label": "FAVOR", 
  "text": "\"#COVID19 Oraingo datuak, izurriaren dinamika, txertoaren eragina eta birusaren..
}

```
#### QNLIeu

An example of 'train' looks as follows:
```
{
  "idx": 1, 
  "label": "not_entailment", 
  "question": "Zein posiziotan jokatzen du Busquets-ek?", 
  "sentence": "Busquets 23 partidatan izan zen konbokatua eta 2 gol sartu zituen."
}
```
#### WiCeu

An example of 'test' looks as follows:
```
{
  "idx": 16, 
  "label": false, 
  "word": "udal", 
  "sentence1": "1a . Lekeitioko udal mugarteko Alde Historikoa Birgaitzeko Plan Berezia behin...", 
  "sentence2": "Diezek kritikatu egin zuen EAJk zenbait udaletan EH gobernu taldeetatik at utzi...", 
  "start1": 16, 
  "start2": 40, 
  "end1": 21, 
  "end2": 49
}
```

#### EpecKorrefBin

An example of 'train' looks as follows:
```
{
  "idx": 6, 
  "label": false, 
  "text": "Isuntza da faborito nagusia Elantxobeko banderan . ISUNTZA trainerua da faborito nagusia bihar Elantxoben jokatuko den bandera irabazteko .", 
  "span1_text": "Elantxobeko banderan", 
  "span2_text": "ISUNTZA trainerua", 
  "span1_index": 4, 
  "span2_index": 8
  }
```

### Data Fields

#### NERCid

* `tokens`: a list of `string` features
* `tags`: a list of entity labels, with possible values including `person` (PER), `location` (LOC), `organization` (ORG), `miscellaneous` (MISC)
* `idx`: an `int32` feature

#### NERCood

* `tokens`: a list of `string` features
* `tags`: a list of entity labels, with possible values including `person` (PER), `location` (LOC), `organization` (ORG), `miscellaneous` (MISC)
* `idx`: an `int32` feature

#### FMTODeu_intent

* `text`: a `string` feature
* `label`: an intent label, with possible values including: 
  * `alarm/cancel_alarm`
  * `alarm/modify_alarm`
  * `alarm/set_alarm`
  * `alarm/show_alarms`
  * `alarm/snooze_alarm`
  * `alarm/time_left_on_alarm`
  * `reminder/cancel_reminder`
  * `reminder/set_reminder`
  * `reminder/show_reminders`
  * `weather/checkSunrise`
  * `weather/checkSunset`
  * `weather/find`
* `idx`: an `int32` feature

#### FMTODeu_slot

* `tokens`: a list of `string` features
* `tags`: a list of intent labels, with possible values including: 
  * `datetime`
  * `location`
  * `negation`
  * `alarm/alarm_modifier`
  * `alarm/recurring_period`
  * `reminder/noun`
  * `reminder/todo`
  * `reminder/reference`
  * `reminder/recurring_period`
  * `weather/attribute`
  * `weather/noun`
* `idx`: an `int32` feature

#### BHTCv2

* `text`: a `string` feature
* `label`: a polarity label, with possible values including `neutral` (NEU), `negative` (N), `positive` (P)
* `idx`: an `int32` feature

#### BEC2016eu

* `text`: a `string` feature
* `label`: a topic label, with possible values including: 
  * `Ekonomia`
  * `Euskal Herria`
  * `Euskara`
  * `Gizartea`
  * `Historia`
  * `Ingurumena`
  * `Iritzia`
  * `Komunikazioa`
  * `Kultura`
  * `Nazioartea`
  * `Politika`
  * `Zientzia`
* `idx`: an `int32` feature

#### VaxxStance

* `text`: a `string` feature
* `label`: a stance label, with possible values including `AGAINST`, `FAVOR`, `NONE`
* `idx`: an `int32` feature

#### QNLIeu

* `question`: a `string` feature
* `sentence`: a `string` feature
* `label`: an entailment label, with possible values including `entailment`, `not_entailment`
* `idx`: an `int32` feature

#### WiCeu

* `word`: a `string` feature
* `sentence1`: a `string` feature
* `sentence2`: a `string` feature
* `label`: a `boolean` label indicating sense agreement, with possible values including `true`, `false`
* `start1`: an `int` feature indicating character position where word occurence begins in first sentence
* `start2`: an `int` feature indicating character position where word occurence begins in second sentence
* `end1`: an `int` feature indicating character position where word occurence ends in first sentence
* `end2`: an `int` feature indicating character position where word occurence ends in second sentence
* `idx`: an `int32` feature

#### EpecKorrefBin

* `text`: a `string` feature.
* `label`: a `boolean` coreference label, with possible values including `true`, `false`.
* `span1_text`: a `string` feature
* `span2_text`:  a `string` feature
* `span1_index`: an `int` feature indicating token index where `span1_text` feature occurs in `text`
* `span2_index`: an `int` feature indicating token index where `span2_text` feature occurs in `text`
* `idx`: an `int32` feature

### Data Splits

| Dataset | \|Train\| | \|Val\| | \|Test\| |
|---------|--------:|------:|-------:|
| NERCid | 51,539 | 12,936 | 35,855 |
| NERCood | 64,475 | 14,945 | 14,462 |
| FMTODeu_intent | 3,418 | 1,904 | 1,087 |
| FMTODeu_slot | 19,652 | 10,791 | 5,633 |
| BHTCv2 | 8,585 | 1,857 | 1,854 |
| BEC2016eu | 6,078 | 1,302 | 1,302 |
| VaxxStance | 864 | 206 | 312 |
| QNLIeu | 1,764 | 230 | 238 |
| WiCeu | 408,559 | 600 | 1,400 |
| EpecKorrefBin | 986 | 320 | 587 |



## Dataset Creation

### Curation Rationale

We believe that BasqueGLUE is a significant contribution towards developing NLU tools in Basque, which we believe will facilitate the technological advance for the Basque language. In order to create BasqueGLUE we took as a reference the GLUE and SuperGLUE frameworks. When possible, we re-used existing datasets for Basque, adapting them to the corresponding task formats if necessary. Additionally, BasqueGLUE also includes six new datasets that have not been published before. In total, BasqueGLUE consists of nine Basque NLU tasks and covers a wide range of tasks with different difficulties across several domains. As with the original GLUE benchmark, the training data for the tasks vary in size, which allows to measure the performance of how the models transfer knowledge across tasks.

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

Gorka Urbizu [1], Iñaki San Vicente [1], Xabier Saralegi [1], Rodrigo Agerri [2] and Aitor Soroa [2]

Affiliation of the authors:

[1] orai NLP Technologies

[2] HiTZ Center - Ixa, University of the Basque Country UPV/EHU

### Licensing Information

Each dataset of the BasqueGLUE benchmark has it's own license (due to most of them being or being derived from already existing datasets). See their respective README files for details.

Here we provide a brief summary of their licenses:

| Dataset | License |
|---------|---------|
| NERCid | CC BY-NC-SA 4.0 |
| NERCood | CC BY-NC-SA 4.0 |
| FMTODeu_intent | CC BY-NC-SA 4.0 |
| FMTODeu_slot | CC BY-NC-SA 4.0 |
| BHTCv2 | CC BY-NC-SA 4.0 |
| BEC2016eu | Twitter's license + CC BY-NC-SA 4.0 |
| VaxxStance | Twitter's license + CC BY 4.0 |
| QNLIeu | CC BY-SA 4.0 |
| WiCeu | CC BY-NC-SA 4.0 |
| EpecKorrefBin | CC BY-NC-SA 4.0 |

For the rest of the files of the benchmark, including the loading and evaluation scripts, the following license applies:

Copyright (C) by Orai NLP Technologies.
This benchmark and evaluation scripts are licensed under the Creative Commons Attribution Share Alike 4.0
International License (CC BY-SA 4.0). To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/.

### Citation Information

```
@InProceedings{urbizu2022basqueglue,
  author    = {Urbizu, Gorka  and  San Vicente, Iñaki  and  Saralegi, Xabier  and  Agerri, Rodrigo  and  Soroa, Aitor},
  title     = {BasqueGLUE: A Natural Language Understanding Benchmark for Basque},
  booktitle      = {Proceedings of the Language Resources and Evaluation Conference},
  month          = {June},
  year           = {2022},
  address        = {Marseille, France},
  publisher      = {European Language Resources Association},
  pages     = {1603--1612},
  abstract  = {Natural Language Understanding (NLU) technology has improved significantly over the last few years and multitask benchmarks such as GLUE are key to evaluate this improvement in a robust and general way. These benchmarks take into account a wide and diverse set of NLU tasks that require some form of language understanding, beyond the detection of superficial, textual clues. However, they are costly to develop and language-dependent, and therefore they are only available for a small number of languages. In this paper, we present BasqueGLUE, the first NLU benchmark for Basque, a less-resourced language, which has been elaborated from previously existing datasets and following similar criteria to those used for the construction of GLUE and SuperGLUE. We also report the evaluation of two state-of-the-art language models for Basque on BasqueGLUE, thus providing a strong baseline to compare upon. BasqueGLUE is freely available under an open license.},
  url       = {https://aclanthology.org/2022.lrec-1.172}
}
```

### Contributions

Thanks to [@richplant](https://github.com/richplant) for adding this dataset to hugginface.
