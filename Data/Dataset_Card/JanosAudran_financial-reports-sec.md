---
annotations_creators:
  - expert-generated
language:
  - en
language_creators:
  - expert-generated
license:
  - apache-2.0
multilinguality:
  - monolingual
pretty_name: US public firm Annual Reports (10-K)
size_categories:
  - 10M<n<100M
source_datasets:
  - extended|other
tags:
  - "'finance"
  - financial
  - 10-K
  - 10K
  - 10k
  - 10-k
  - annual
  - reports
  - sec
  - edgar
  - sentiment
  - firm
  - public
  - us'
task_categories:
  - fill-mask
  - text-classification
task_ids:
  - masked-language-modeling
  - multi-class-classification
  - sentiment-classification
dataset_info:
  - config_name: large_lite
    features:
      - name: cik
        dtype: string
      - name: sentence
        dtype: string
      - name: section
        dtype:
          class_label:
            names:
              "0": section_1
              "1": section_10
              "2": section_11
              "3": section_12
              "4": section_13
              "5": section_14
              "6": section_15
              "7": section_1A
              "8": section_1B
              "9": section_2
              "10": section_3
              "11": section_4
              "12": section_5
              "13": section_6
              "14": section_7
              "15": section_7A
              "16": section_8
              "17": section_9
              "18": section_9A
              "19": section_9B
      - name: labels
        struct:
          - name: 1d
            dtype:
              class_label:
                names:
                  "0": positive
                  "1": negative
          - name: 5d
            dtype:
              class_label:
                names:
                  "0": positive
                  "1": negative
          - name: 30d
            dtype:
              class_label:
                names:
                  "0": positive
                  "1": negative
      - name: filingDate
        dtype: string
      - name: docID
        dtype: string
      - name: sentenceID
        dtype: string
      - name: sentenceCount
        dtype: int64
    splits:
      - name: train
        num_bytes: 16424576472
        num_examples: 67316227
      - name: validation
        num_bytes: 423527281
        num_examples: 1585561
      - name: test
        num_bytes: 773116540
        num_examples: 2965174
    download_size: 13362319126
    dataset_size: 17621220293
  - config_name: large_full
    features:
      - name: cik
        dtype: string
      - name: sentence
        dtype: string
      - name: section
        dtype:
          class_label:
            names:
              "0": section_1
              "1": section_10
              "2": section_11
              "3": section_12
              "4": section_13
              "5": section_14
              "6": section_15
              "7": section_1A
              "8": section_1B
              "9": section_2
              "10": section_3
              "11": section_4
              "12": section_5
              "13": section_6
              "14": section_7
              "15": section_7A
              "16": section_8
              "17": section_9
              "18": section_9A
              "19": section_9B
      - name: labels
        struct:
          - name: 1d
            dtype:
              class_label:
                names:
                  "0": positive
                  "1": negative
          - name: 5d
            dtype:
              class_label:
                names:
                  "0": positive
                  "1": negative
          - name: 30d
            dtype:
              class_label:
                names:
                  "0": positive
                  "1": negative
      - name: filingDate
        dtype: string
      - name: name
        dtype: string
      - name: docID
        dtype: string
      - name: sentenceID
        dtype: string
      - name: sentenceCount
        dtype: int64
      - name: tickers
        list: string
      - name: exchanges
        list: string
      - name: entityType
        dtype: string
      - name: sic
        dtype: string
      - name: stateOfIncorporation
        dtype: string
      - name: tickerCount
        dtype: int32
      - name: acceptanceDateTime
        dtype: string
      - name: form
        dtype: string
      - name: reportDate
        dtype: string
      - name: returns
        struct:
          - name: 1d
            struct:
              - name: closePriceEndDate
                dtype: float32
              - name: closePriceStartDate
                dtype: float32
              - name: endDate
                dtype: string
              - name: startDate
                dtype: string
              - name: ret
                dtype: float32
          - name: 5d
            struct:
              - name: closePriceEndDate
                dtype: float32
              - name: closePriceStartDate
                dtype: float32
              - name: endDate
                dtype: string
              - name: startDate
                dtype: string
              - name: ret
                dtype: float32
          - name: 30d
            struct:
              - name: closePriceEndDate
                dtype: float32
              - name: closePriceStartDate
                dtype: float32
              - name: endDate
                dtype: string
              - name: startDate
                dtype: string
              - name: ret
                dtype: float32
    splits:
      - name: train
        num_bytes: 39306095718
        num_examples: 67316227
      - name: validation
        num_bytes: 964030458
        num_examples: 1585561
      - name: test
        num_bytes: 1785383996
        num_examples: 2965174
    download_size: 13362319126
    dataset_size: 42055510172
  - config_name: small_full
    features:
      - name: cik
        dtype: string
      - name: sentence
        dtype: string
      - name: section
        dtype:
          class_label:
            names:
              "0": section_1
              "1": section_1A
              "2": section_1B
              "3": section_2
              "4": section_3
              "5": section_4
              "6": section_5
              "7": section_6
              "8": section_7
              "9": section_7A
              "10": section_8
              "11": section_9
              "12": section_9A
              "13": section_9B
              "14": section_10
              "15": section_11
              "16": section_12
              "17": section_13
              "18": section_14
              "19": section_15
      - name: labels
        struct:
          - name: 1d
            dtype:
              class_label:
                names:
                  "0": positive
                  "1": negative
          - name: 5d
            dtype:
              class_label:
                names:
                  "0": positive
                  "1": negative
          - name: 30d
            dtype:
              class_label:
                names:
                  "0": positive
                  "1": negative
      - name: filingDate
        dtype: string
      - name: name
        dtype: string
      - name: docID
        dtype: string
      - name: sentenceID
        dtype: string
      - name: sentenceCount
        dtype: int64
      - name: tickers
        list: string
      - name: exchanges
        list: string
      - name: entityType
        dtype: string
      - name: sic
        dtype: string
      - name: stateOfIncorporation
        dtype: string
      - name: tickerCount
        dtype: int32
      - name: acceptanceDateTime
        dtype: string
      - name: form
        dtype: string
      - name: reportDate
        dtype: string
      - name: returns
        struct:
          - name: 1d
            struct:
              - name: closePriceEndDate
                dtype: float32
              - name: closePriceStartDate
                dtype: float32
              - name: endDate
                dtype: string
              - name: startDate
                dtype: string
              - name: ret
                dtype: float32
          - name: 5d
            struct:
              - name: closePriceEndDate
                dtype: float32
              - name: closePriceStartDate
                dtype: float32
              - name: endDate
                dtype: string
              - name: startDate
                dtype: string
              - name: ret
                dtype: float32
          - name: 30d
            struct:
              - name: closePriceEndDate
                dtype: float32
              - name: closePriceStartDate
                dtype: float32
              - name: endDate
                dtype: string
              - name: startDate
                dtype: string
              - name: ret
                dtype: float32
    splits:
      - name: train
        num_bytes: 128731540
        num_examples: 200000
      - name: validation
        num_bytes: 13411689
        num_examples: 20000
      - name: test
        num_bytes: 13188331
        num_examples: 20000
    download_size: 42764380
    dataset_size: 155331560
  - config_name: small_lite
    features:
      - name: cik
        dtype: string
      - name: sentence
        dtype: string
      - name: section
        dtype:
          class_label:
            names:
              "0": section_1
              "1": section_1A
              "2": section_1B
              "3": section_2
              "4": section_3
              "5": section_4
              "6": section_5
              "7": section_6
              "8": section_7
              "9": section_7A
              "10": section_8
              "11": section_9
              "12": section_9A
              "13": section_9B
              "14": section_10
              "15": section_11
              "16": section_12
              "17": section_13
              "18": section_14
              "19": section_15
      - name: labels
        struct:
          - name: 1d
            dtype:
              class_label:
                names:
                  "0": positive
                  "1": negative
          - name: 5d
            dtype:
              class_label:
                names:
                  "0": positive
                  "1": negative
          - name: 30d
            dtype:
              class_label:
                names:
                  "0": positive
                  "1": negative
      - name: filingDate
        dtype: string
      - name: docID
        dtype: string
      - name: sentenceID
        dtype: string
      - name: sentenceCount
        dtype: int64
    splits:
      - name: train
        num_bytes: 60681688
        num_examples: 200000
      - name: validation
        num_bytes: 6677389
        num_examples: 20000
      - name: test
        num_bytes: 6351730
        num_examples: 20000
    download_size: 42764380
    dataset_size: 73710807
---

# Dataset Card for [financial-reports-sec]

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Dataset Configurations](#dataset-configurations)
  - [Usage](#usage)
  - [Supported Tasks](#supported-tasks)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
  - [Dataset Summary Statistics](#dataset-summary-statistics)
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
  - [References](#references)
  - [Citation Information](#citation-information)

## Dataset Description

- **Point of Contact: Aman Khan**

### Dataset Summary

The dataset contains the annual report of US public firms filing with the SEC EDGAR system from 1993-2020. Each annual report (**10K filing**) is broken into 20 sections. Each section is split into individual sentences. Sentiment labels are provided on a **per filing basis** from the market reaction around the filing date for 3 different time windows _[t-1, t+1]_, _[t-1, t+5]_ and _[t-1, t+30]_. Additional metadata for each filing is included in the dataset.

### Dataset Configurations

**Four** configurations are available:

- _**large_lite**_:
  - Contains only the basic features needed. Extra metadata is ommitted.
  - Features List:
    - **cik**
    - **sentence**
    - **section**
    - **labels**
    - **filingDate**
    - **docID**
    - **sentenceID**
    - **sentenceCount**
- _**large_full**_:
  - All features are included.
  - Features List (excluding those already in the lite verison above):
    - **name**
    - **tickers**
    - **exchanges**
    - **entityType**
    - **sic**
    - **stateOfIncorporation**
    - **tickerCount**
    - **acceptanceDateTime**
    - **form**
    - **reportDate**
    - **returns**
- _**small_lite**_:
  - Same as _**large_lite**_ version except that only (200,000/20,000/20,000) sentences are loaded for (train/test/validation) splits.
- _**small_full**_:
  - Same as _**large_full**_ version except that only (200,000/20,000/20,000) sentences are loaded for (train/test/validation) splits.

### Usage

```python
import datasets

# Load the lite configuration of the dataset
raw_dataset = datasets.load_dataset("JanosAudran/financial-reports-sec", "large_lite")

# Load a specific split
raw_dataset = datasets.load_dataset("JanosAudran/financial-reports-sec", "small_full", split="train")
```

### Supported Tasks

The tasks the dataset can be used directly for includes:

- _Masked Language Modelling_
  - A model like BERT can be fine-tuned on this corpus of financial text.
- _Sentiment Analysis_
  - For each annual report a label ["positive", "negative"] is provided based on the market reaction around the filing date (refer to [Annotations](#annotations)).
- _Next Sentence Prediction/Sentence Order Prediction_
  - Sentences extracted from the filings are in their original order and as such the dataset can be adapted very easily for either of these tasks.

### Languages

All sentences are in English.

## Dataset Structure

### Data Instances

Refer to dataset preview.

### Data Fields

**Feature Name**

- Description
- Data type
- Example/Structure

**cik**

- 10 digit identifier used by SEC for a firm.
- _string_
- '0000001750'

**sentence**

- A single sentence from the 10-K filing.
- _string_
- 'The finance agreement is secured by a first priority security interest in all insurance policies, all unearned premium, return premiums, dividend payments and loss payments thereof.'

**section**

- The section of the 10-K filing the sentence is located.
- _ClassLabel_
- ```python
  ClassLabel(names=['section_1', 'section_10', 'section_11', 'section_12', 'section_13', 'section_14', 'section_15', 'section_1A', 'section_1B', 'section_2','section_3', 'section_4', 'section_5', 'section_6', 'section_7', 'section_7A','section_8', 'section_9', 'section_9A', 'section_9B'], id=None)
  ```

**labels**

- The sentiment label for the entire filing (_**positve**_ or _**negative**_) based on different time windows.
- _Dict of ClassLables_
- ```python
  {
    '1d': ClassLabel(names=['positive', 'negative'], id=None),
    '5d': ClassLabel(names=['positive', 'negative'], id=None),
    '30d': ClassLabel(names=['positive', 'negative'], id=None)
  }
  ```

**filingDate**

- The date the 10-K report was filed with the SEC.
- _string_
- '2021-03-10'

**docID**

- Unique ID for identifying the exact 10-K filing. Unique across all configs and splits. Can be used to identify the document from which the sentence came from.
- _string_
- '0000001750_10-K_2020'

**sentenceID**

- Unique ID for identifying the exact sentence. Unique across all configs and splits.
- _string_
- '0000001750_10-K_2020_section_1_100'

**sentenceCount**

- Integer identiying the running sequence for the sentence. Unique **only** for a given config and split.
- _string_
- 123

**name**

- The name of the filing entity
- _string_
- 'Investar Holding Corp'

**tickers**

- List of ticker symbols for the filing entity.
- _List of strings_
- ['ISTR']

**exchanges**

- List of exchanges for the filing entity.
- _List of strings_
- ['Nasdaq']

**entityType**

- The type of entity as identified in the 10-K filing.
- _string_
- 'operating'

**sic**

- Four digit SIC code for the filing entity.
- _string_
- '6022'

**stateOfIncorporation**

- Two character code for the state of incorporation for the filing entity.
- _string_
- 'LA'

**tickerCount**

- _**Internal use**_. Count of ticker symbols. Always 1.
- _int_
- 1

**acceptanceDateTime**

- The full timestamp of when the filing was accepted into the SEC EDGAR system.
- _string_
- '2021-03-10T14:26:11.000Z'

**form**

- The type of filing. Always 10-K in the dataset.
- _string_
- '10-K'

**reportDate**

- The last date in the fiscal year for which the entity is filing the report.
- _string_
- '2020-12-31'

**returns**

- _**Internal use**_. The prices and timestamps used to calculate the sentiment labels.
- _Dict_
- ```python
  {'1d': {
    'closePriceEndDate': 21.45746421813965,
    'closePriceStartDate': 20.64960479736328,
    'endDate': '2021-03-11T00:00:00-05:00',
    'startDate': '2021-03-09T00:00:00-05:00',
    'ret': 0.03912226855754852
    },
  '5d': {
    'closePriceEndDate': 21.743167877197266,
    'closePriceStartDate': 20.64960479736328,
    'endDate': '2021-03-15T00:00:00-04:00',
    'startDate': '2021-03-09T00:00:00-05:00',
    'ret': 0.052958063781261444
    },
  '30d': {
    'closePriceEndDate': 20.63919448852539,
    'closePriceStartDate': 20.64960479736328,
    'endDate': '2021-04-09T00:00:00-04:00',
    'startDate': '2021-03-09T00:00:00-05:00',
    'ret': -0.0005041408003307879}}
  ```

### Data Splits

| Config     |      train | validation |      test |
| ---------- | ---------: | ---------: | --------: |
| large_full | 67,316,227 |  1,585,561 | 2,965,174 |
| large_lite | 67,316,227 |  1,585,561 | 2,965,174 |
| small_full |    200,000 |     20,000 |    20,000 |
| small_lite |    200,000 |     20,000 |    20,000 |

### Dataset Summary Statistics

| Variable                          |      count |  mean |    std |    min |     1% |    25% |   50% |   75% |   99% |       max |
| :-------------------------------- | ---------: | ----: | -----: | -----: | -----: | -----: | ----: | ----: | ----: | --------: |
| Unique Firm Count                 |      4,677 |       |        |        |        |        |       |       |       |           |
| Filings Count                     |     55,349 |       |        |        |        |        |       |       |       |           |
| Sentence Count                    | 71,866,962 |       |        |        |        |        |       |       |       |           |
| Filings per Firm                  |      4,677 |    12 |      9 |      1 |      1 |      4 |    11 |    19 |    27 |        28 |
| Return per Filing - 1d            |     55,349 | 0.008 |  0.394 | -0.973 | -0.253 | -0.023 |     0 |  0.02 | 0.367 |    77.977 |
| Return per Filing - 5d            |     55,349 | 0.013 |  0.584 |  -0.99 | -0.333 | -0.034 |     0 | 0.031 |   0.5 |       100 |
| Return per Filing - 30d           |     55,349 | 0.191 | 22.924 | -0.999 | -0.548 | -0.068 | 0.001 | 0.074 |     1 | 5,002.748 |
| Sentences per Filing              |     55,349 | 1,299 |    654 |      0 |    110 |    839 | 1,268 | 1,681 | 3,135 |     8,286 |
| Sentences by Section - section_1  |     55,349 |   221 |    183 |      0 |      0 |     97 |   180 |   293 |   852 |     2,724 |
| Sentences by Section - section_10 |     55,349 |    24 |     40 |      0 |      0 |      4 |     6 |    20 |   173 |     1,594 |
| Sentences by Section - section_11 |     55,349 |    16 |     47 |      0 |      0 |      3 |     3 |     4 |   243 |       808 |
| Sentences by Section - section_12 |     55,349 |     9 |     14 |      0 |      0 |      3 |     4 |     8 |    56 |     1,287 |
| Sentences by Section - section_13 |     55,349 |     8 |     20 |      0 |      0 |      3 |     3 |     4 |    79 |       837 |
| Sentences by Section - section_14 |     55,349 |    22 |     93 |      0 |      0 |      3 |     3 |     8 |   413 |     3,536 |
| Sentences by Section - section_15 |     55,349 |   177 |    267 |      0 |      0 |      9 |    26 |   315 |  1104 |     4,140 |
| Sentences by Section - section_1A |     55,349 |   197 |    204 |      0 |      0 |      3 |   158 |   292 |   885 |     2,106 |
| Sentences by Section - section_1B |     55,349 |     4 |     31 |      0 |      0 |      1 |     3 |     3 |    13 |     2,414 |
| Sentences by Section - section_2  |     55,349 |    16 |     45 |      0 |      0 |      6 |     8 |    13 |   169 |     1,903 |
| Sentences by Section - section_3  |     55,349 |    14 |     36 |      0 |      0 |      4 |     5 |    12 |   121 |     2,326 |
| Sentences by Section - section_4  |     55,349 |     7 |     17 |      0 |      0 |      3 |     3 |     4 |    66 |       991 |
| Sentences by Section - section_5  |     55,349 |    20 |     41 |      0 |      0 |     10 |    15 |    21 |    87 |     3,816 |
| Sentences by Section - section_6  |     55,349 |     8 |     29 |      0 |      0 |      3 |     4 |     7 |    43 |     2,156 |
| Sentences by Section - section_7  |     55,349 |   265 |    198 |      0 |      0 |    121 |   246 |   373 |   856 |     4,539 |
| Sentences by Section - section_7A |     55,349 |    18 |     52 |      0 |      0 |      3 |     9 |    21 |   102 |     3,596 |
| Sentences by Section - section_8  |     55,349 |   257 |    296 |      0 |      0 |      3 |   182 |   454 |  1105 |     4,431 |
| Sentences by Section - section_9  |     55,349 |     5 |     33 |      0 |      0 |      3 |     3 |     4 |    18 |     2,330 |
| Sentences by Section - section_9A |     55,349 |    17 |     16 |      0 |      0 |      8 |    15 |    23 |    50 |       794 |
| Sentences by Section - section_9B |     55,349 |     4 |     18 |      0 |      0 |      2 |     3 |     4 |    23 |       813 |
| Word count per Sentence           | 71,866,962 |    28 |     22 |      1 |      2 |     16 |    24 |    34 |    98 |     8,675 |

## Dataset Creation

### Curation Rationale

To create this dataset multiple sources of information have to be cleaned and processed for data merging. Starting from the raw filings:

- Useful metadata about the filing and firm was added.
- Time windows around the filing date were carefully created.
- Stock price data was then added for the windows.
- Ambiguous/duplicate records were removed.

### Source Data

#### Initial Data Collection and Normalization

Initial data was collected and processed by the authors of the research paper [**EDGAR-CORPUS: Billions of Tokens Make The World Go Round**](#references). Market price and returns data was collected from Yahoo Finance. Additional metadata was collected from SEC.

#### Who are the source language producers?

US public firms filing with the SEC.

### Annotations

#### Annotation process

Labels for sentiment classification are based on buy-and-hold returns over a fixed time window around the filing date with the SEC i.e. when the data becomes public. Returns are chosen for this process as it reflects the combined market intelligence at parsing the new information in the filings. For each filing date **t** the stock price at **t-1** and **t+W** is used to calculate returns. If, the returns are positive a label of **positive** is assigned else a label of **negative** is assigned. Three different windows are used to assign the labels:

- **1d**: _[t-1, t+1]_
- **5d**: _[t-1, t+5]_
- **30d**: _[t-1, t+30]_

The windows are based on calendar days and are adjusted for weekends and holidays. The rationale behind using 3 windows is as follows:

- A very short window may not give enough time for all the information contained in the filing to be reflected in the stock price.
- A very long window may capture other events that drive stock price for the firm.

#### Who are the annotators?

Financial market participants.

### Personal and Sensitive Information

The dataset contains public filings data from SEC. Market returns data was collected from Yahoo Finance.

## Considerations for Using the Data

### Social Impact of Dataset

Low to none.

### Discussion of Biases

The dataset is about financial information of public companies and as such the tone and style of text is in line with financial literature.

### Other Known Limitations

NA

## Additional Information

### Dataset Curators

**Aman Khan**

### Licensing Information

This dataset is provided under Apache 2.0.

### References

- Lefteris Loukas, Manos Fergadiotis, Ion Androutsopoulos, & Prodromos Malakasiotis. (2021). EDGAR-CORPUS [Data set]. Zenodo. https://doi.org/10.5281/zenodo.5589195

### Citation Information

Please use the following to cite this dataset:

```
@ONLINE{financial-reports-sec,
author = "Aman Khan",
title = "Financial Reports SEC",
url = "https://huggingface.co/datasets/JanosAudran/financial-reports-sec"
}
```
