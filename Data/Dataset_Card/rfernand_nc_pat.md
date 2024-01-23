---
annotations_creators:
- machine-generated
language:
- en
language_creators:
- machine-generated
license:
- mit
multilinguality:
- monolingual
pretty_name: Active/Passive/Logical Transforms
size_categories:
- 10K<n<100K
- 1K<n<10K
- n<1K
source_datasets:
- original
tags:
- struct2struct
- tree2tree
task_categories:
- text2text-generation
task_ids: []
---
# Dataset Card for Active/Passive/Logical Transforms

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Dataset Subsets (Tasks)](#data-tasks)
  - [Dataset Splits](#data-splits)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
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
- **Point of Contact:** [Roland Fernandez](mailto:rfernand@microsoft.com)

### Dataset Summary

This dataset is a synthetic dataset containing structure-to-structure transformation tasks between 
English sentences in 3 forms: active, passive, and logical.  The dataset also includes several 
tree-transformation diagnostic/warm-up tasks.

### Supported Tasks and Leaderboards

[TBD]

### Languages

All data is in English.

## Dataset Structure

The dataset consists of several subsets, or tasks. Each task contains a train split, a validation split, and a
test split, with most tasks also containing two out-of-distruction splits (one for new adjectives and one for longer adjective phrases).  

Each sample in a split contains a source string, a target string, and 0-2 annotation strings.

### Dataset Subsets (Tasks)
The dataset consists of diagnostic/warm-up tasks and core tasks.  The core tasks represent the translation of English sentences between the active, passive, and logical forms.

The 12 diagnostic/warm-up tasks are:

```
- car_cdr_cons              (small phrase translation tasks that require only: CAR, CDR, or CAR+CDR+CONS operations)
- car_cdr_cons_tuc          (same task as car_cdr_cons, but requires mapping lowercase fillers to their uppercase tokens)
- car_cdr_rcons             (same task as car_cdr_cons, but the CONS samples have their left/right children swapped)
- car_cdr_rcons_tuc         (same task as car_cdr_rcons, but requires mapping lowercase fillers to their uppercase tokens)
- car_cdr_seq               (each samples requires 1-4 combinations of CAR and CDR, as identified by the root filler oken)
- car_cdr_seq_40k           (same task as car_cdr_seq, but train samples increased from 10K to 40K)
- car_cdr_seq_tuc           (same task as car_cdr_seq, but requires mapping lowercase fillers to their uppercase tokens)
- car_cdr_seq_40k_tuc       (same task as car_cdr_seq_tuc, but train samples increased from 10K to 40K)
- car_cdr_seq_path          (similiar to car_cdr_seq, but each needed operation in represented as a node in the left child of the root)
- car_cdr_seq_path_40k      (same task as car_cdr_seq_path, but train samples increased from 10K to 40K)
- car_cdr_seq_path_40k_tuc  (same task as car_cdr_seq_path_40k, but requires mapping lowercase fillers to their uppercase tokens)
- car_cdr_seq_path_tuc      (same task as car_cdr_seq_path, but requires mapping lowercase fillers to their uppercase tokens)
```

There are 14 core tasks are:
```
- active_active_stb         (active sentence translation, from sentence to parenthesized tree form, both directions)
- active_active_stb_40k     (same task as active_active_stb, but train samples increased from 10K to 40K)
- active_logical_ttb        (active to logical tree translation, in both directions)
- active_logical_ttb_40k    (same task as active_logical_ttb, but train samples increased from 10K to 40K)
- active_passive_ssb        (active to passive sentence translation, in both directions)
- active_passive_ssb_40k    (same task as active_passive_ssb, but train samples increased from 10K to 40K)
- active_passive_ttb        (active to passive tree translation, in both directions)
- active_passive_ttb_40k    (same task as active_passive_ttb, but train samples increased from 10K to 40K)
- actpass_logical_tt        (mixture of active to logical and passive to logical tree translations, single direction)
- actpass_logical_tt_40k    (same task as actpass_logical_tt, but train samples increased from 10K to 40K)
- passive_logical_ttb       (passive to logical tree translation, in both directions)
- passive_logical_ttb_40k   (same task as passive_logical_ttb, but train samples increased from 10K to 40K)
- passive_passive_stb       (passive sentence translation, from sentence to parenthesized tree form, both directions)
- passive_passive_stb_40k   (same task as passive_passive_stb, but train samples increased from 10K to 40K)
```

### Data Splits

Most tasks have the following splits:
  - train
  - validation
  - test
  - ood_new
  - ood_long
  
Here is a table showing how the number of examples varies by split (for most tasks):

| Dataset Split | Number of Instances in Split                |
| ------------- | ------------------------------------------- |
| train         | 10,000                                      |
| validation    |  1,250                                      |
| test          |  1,250                                      |
| ood_new       |  1,250                                      |
| ood_long      |  1,250                                      |


### Data Instances

For each sample, there is source and target string.  Source and target string are either plain text, or a parenthesized 
version of a tree, depending on the task.

Here is an example from the *train* split of the *active_passive_ttb* task:

```
{
  'source': '( S ( NP ( DET his ) ( AP ( N cat ) ) ) ( VP ( V discovered ) ( NP ( DET the ) ( AP ( ADJ blue ) ( AP ( N priest ) ) ) ) ) )',
  'target': '( S ( NP ( DET the ) ( AP ( ADJ blue ) ( AP ( N priest ) ) ) ) ( VP ( AUXPS was ) ( VPPS ( V discovered ) ( PPPS ( PPS by ) ( NP ( DET his ) ( AP ( N cat ) ) ) ) ) ) )',
  'direction': 'forward'
}
```

### Data Fields

- `source`: the string denoting the sequence or tree structure to be translated 
- `target`: the string denoting the gold (aka label) sequence or tree structure  

Optional annotation fields (their presence varies by task):

- `direction`: describes the direction of the translation (forward, backward), relative to the task name 
- `count` : a string denoting the count of symbolic operations needed (e.g., "s3") to translate the source to the target
- `class` : a string denoting the type of translation needed

## Dataset Creation

### Curation Rationale

We wanted a dataset comprised of relatively simple English active/passive/logical form translations, where we could focus 
on two types of out of distribution generalization: longer source sequences and new adjectives.  

### Source Data

[N/A]

#### Initial Data Collection and Normalization

[N/A]

#### Who are the source language producers?

The dataset by generated from templates designed by Paul Smolensky and Roland Fernandez.

### Annotations

Besides the source and target structured sequences, some of the subsets (tasks) contain 1-2 additional columns that
describe the category and tree depth of each sample.

#### Annotation process

The annotation columns were generated from the each sample template and source sequence.

#### Who are the annotators?

[N/A]

### Personal and Sensitive Information

No names or other sensitive information are included in the data.

## Considerations for Using the Data

### Social Impact of Dataset

The purpose of this dataset is to help develop models that can translated structured data from one form to another, in a
way that generalizes to out of distribution adjective values and lengths.

### Discussion of Biases

[TBD]

### Other Known Limitations

[TBD]

## Additional Information

### Dataset Curators

The dataset by generated from templates designed by Paul Smolensky and Roland Fernandez.

### Licensing Information

This dataset is released under the [MIT License](https://choosealicense.com/licenses/mit/). 

### Citation Information

[TBD]

### Contributions

Thanks to [@rfernand2](https://github.com/rfernand2) for adding this dataset.
