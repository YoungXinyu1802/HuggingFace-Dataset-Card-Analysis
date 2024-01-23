---
annotations_creators:
- none
language_creators:
- unknown
language:
- en
license:
- cc-by-sa-3.0
multilinguality:
- unknown
size_categories:
- unknown
source_datasets:
- original
task_categories:
- table-to-text
task_ids: []
pretty_name: totto
tags:
- data-to-text
---

# Dataset Card for GEM/totto

## Dataset Description

- **Homepage:** n/a
- **Repository:** https://github.com/google-research-datasets/totto + [ToTTo Supplementary Repo
- **Paper:** https://aclanthology.org/2020.emnlp-main.89
- **Leaderboard:** https://github.com/google-research-datasets/totto
- **Point of Contact:** Ankur Parikh

### Link to Main Data Card

You can find the main data card on the [GEM Website](https://gem-benchmark.com/data_cards/totto).

### Dataset Summary 

ToTTo is a high-quality English table-to-text dataset with more than 100,000 examples in which a table from Wikipedia with highlighted cells is paired with a sentence that describes the highlighted cells. All examples in the dataset were post-edited in multiple steps to ensure that the targets are fully faithful to the input information.

You can load the dataset via:
```
import datasets
data = datasets.load_dataset('GEM/totto')
```
The data loader can be found [here](https://huggingface.co/datasets/GEM/totto).

#### website
n/a

#### paper
[ACL Anthology](https://aclanthology.org/2020.emnlp-main.89)

#### authors
Ankur Parikh, Xuezhi Wang, Sebastian Gehrmann, Manaal Faruqui, Bhuwan Dhingra, Diyi Yang, Dipanjan Das

## Dataset Overview

### Where to find the Data and its Documentation

#### Download

<!-- info: What is the link to where the original dataset is hosted? -->
<!-- scope: telescope -->
[ToTTo Main Repo](https://github.com/google-research-datasets/totto) + [ToTTo Supplementary Repo](https://github.com/google-research/language/tree/master/language/totto)

#### Paper

<!-- info: What is the link to the paper describing the dataset (open access preferred)? -->
<!-- scope: telescope -->
[ACL Anthology](https://aclanthology.org/2020.emnlp-main.89)

#### BibTex

<!-- info: Provide the BibTex-formatted reference for the dataset. Please use the correct published version (ACL anthology, etc.) instead of google scholar created Bibtex. -->
<!-- scope: microscope -->
```
@inproceedings{parikh-etal-2020-totto,
    title = "{ToTTo}: A Controlled Table-To-Text Generation Dataset",
    author = "Parikh, Ankur  and
      Wang, Xuezhi  and
      Gehrmann, Sebastian  and
      Faruqui, Manaal  and
      Dhingra, Bhuwan  and
      Yang, Diyi  and
      Das, Dipanjan",
    booktitle = "Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.emnlp-main.89",
    doi = "10.18653/v1/2020.emnlp-main.89",
    pages = "1173--1186",
    abstract = "We present ToTTo, an open-domain English table-to-text dataset with over 120,000 training examples that proposes a controlled generation task: given a Wikipedia table and a set of highlighted table cells, produce a one-sentence description. To obtain generated targets that are natural but also faithful to the source table, we introduce a dataset construction process where annotators directly revise existing candidate sentences from Wikipedia. We present systematic analyses of our dataset and annotation process as well as results achieved by several state-of-the-art baselines. While usually fluent, existing methods often hallucinate phrases that are not supported by the table, suggesting that this dataset can serve as a useful research benchmark for high-precision conditional text generation.",
}
```

#### Contact Name

<!-- quick -->
<!-- info: If known, provide the name of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
Ankur Parikh

#### Contact Email

<!-- info: If known, provide the email of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
totto@google.com

#### Has a Leaderboard?

<!-- info: Does the dataset have an active leaderboard? -->
<!-- scope: telescope -->
yes

#### Leaderboard Link

<!-- info: Provide a link to the leaderboard. -->
<!-- scope: periscope -->
[Github](https://github.com/google-research-datasets/totto)

#### Leaderboard Details

<!-- info: Briefly describe how the leaderboard evaluates models. -->
<!-- scope: microscope -->
This dataset has an associated, active [leaderboard](https://github.com/google-research-datasets/totto#leaderboard) maintained by the authors.
The test set ground truth targets / references are private, i.e they are not publicly shared or downloadable - hence, leaderboard submission is necessary for test set evaluation.
To evaluate your model on the dev or test set AND/OR submit to the leaderboard, you need to submit your model files through this [form](https://forms.gle/AcF9TRqWrPhPzztt7) (The form provides an option to opt-out of going on the leaderboard).

The leaderboard reports three sets of BLEU, PARENT and BLEURT scores for each submission - on the overall test set, the *Overlap* subset of the test set and the *non-Overlap* subset of the test set.



### Languages and Intended Use

#### Multilingual?

<!-- quick -->
<!-- info: Is the dataset multilingual? -->
<!-- scope: telescope -->
no

#### Covered Dialects

<!-- info: What dialects are covered? Are there multiple dialects per language? -->
<!-- scope: periscope -->
No specific dialects. The original language is from Wikipedia and it was post-edited by crowdraters 

#### Covered Languages

<!-- quick -->
<!-- info: What languages/dialects are covered in the dataset? -->
<!-- scope: telescope -->
`English`

#### Whose Language?

<!-- info: Whose language is in the dataset? -->
<!-- scope: periscope -->
The language is post-edited English only (BCP-47: `en`) Wikipedia text. No demographic information about annotators is provided. 
Some amounts of what may be called non-English text, including characters such as French accents or Cyrillic characters, could sometimes occur, especially through fields with entity names as values in the input table cells.


#### License

<!-- quick -->
<!-- info: What is the license of the dataset? -->
<!-- scope: telescope -->
cc-by-sa-3.0: Creative Commons Attribution Share Alike 3.0 Unported

#### Intended Use

<!-- info: What is the intended use of the dataset? -->
<!-- scope: microscope -->
ToTTo is a Table-to-Text NLG task, as the paper title says. The task is as follows: Given a Wikipedia table with row names, column names and table cells, with a subset of cells highlighted, generate a natural language description for the highlighted part of the table . The table need not be exactly rectangular in that - cells can sometimes be multi-row or multi-column.

An earlier example of a Table-to-Text NLG task is [Wikibio](https://arxiv.org/abs/1603.07771) - here the inputs were Wikipedia infoboxes (from the top right corner of entity-related Wiki pages). In contrast, ToTTo mostly has Wikipedia tables from the main article content itself. In general, Table-To-Text NLG tasks can be seen as a subclass of Data-To-Text NLG tasks - where the task is to generate natural language descriptions of inputs which are in the form of structured or semi-structured data. In general, all Data-To-Text NLG tasks need not have an explicit table or other structure - e.g the input in [WebNLG](https://www.aclweb.org/anthology/W16-6626.pdf) is simply a list of triples.

Importantly, ToTTo differs from earlier examples of Table-To-Text NLG in that:

1. It does not suffer from the problem of divergent references - where ground truth descriptions themselves have additional information not found in the table. ToTTo overcomes this by having a multi-step annotation process to edit the initial, free-form table descriptions (which are from Wikipedia) to make them faithful, unambiguous and independent of article context.

2. Since it provides **control** in the form of highlighted table cells, it prevents the problem of there being a large number of valid descriptions focussing on different parts of the table.


#### Primary Task

<!-- info: What primary task does the dataset support? -->
<!-- scope: telescope -->
Data-to-Text

#### Communicative Goal

<!-- quick -->
<!-- info: Provide a short description of the communicative goal of a model trained for this task on this dataset. -->
<!-- scope: periscope -->
The speaker is required to produce a single, coherent English sentence that describes the highlighted cells in the given table, also using metadata and any other information from the table as applicable.



### Credit

#### Curation Organization Type(s)

<!-- info: In what kind of organization did the dataset curation happen? -->
<!-- scope: telescope -->
`industry`

#### Curation Organization(s)

<!-- info: Name the organization(s). -->
<!-- scope: periscope -->
Google Research

#### Dataset Creators

<!-- info: Who created the original dataset? List the people involved in collecting the dataset and their affiliation(s). -->
<!-- scope: microscope -->
Ankur Parikh, Xuezhi Wang, Sebastian Gehrmann, Manaal Faruqui, Bhuwan Dhingra, Diyi Yang, Dipanjan Das

#### Funding

<!-- info: Who funded the data creation? -->
<!-- scope: microscope -->
Google Research

#### Who added the Dataset to GEM?

<!-- info: Who contributed to the data card and adding the dataset to GEM? List the people+affiliations involved in creating this data card and who helped integrate this dataset into GEM. -->
<!-- scope: microscope -->
Varun Gangal created the initial data card and Yacine Jernite wrote the data loader. The data card was updated with new splits by Simon Mille. Sebastian Gehrmann ported the data card and loader from the v1 to the v2 version and extended it with the new fields. 


### Dataset Structure

#### Data Fields

<!-- info: List and describe the fields present in the dataset. -->
<!-- scope: telescope -->
- The `table` field is a `List[List[Dict]]` in row-major order, with outer lists representing rows and the inner lists columns.
- Each `Dict` has the fields `column_span: int`, `is_header: bool`, `row_span: int`, and `value: str`.
- Table metadata consists of `table_page_title`, `table_section_title` and `table_section_texts`
- The `highlighted_cells` are represented as `List[[row_index,column_index]]`, with each `[row_index,column_index]` indicating that `table[row_index][column_index]` is highlighted.
- `example_id` is the unique id per example.
- `sentence_annotations[final_sentence]` which is the table description/generation target



#### Reason for Structure

<!-- info: How was the dataset structure determined? -->
<!-- scope: microscope -->
The structure is aimed to encode highlighted tables in a way that allows rows and columns to span multiple fields in width. The other fields are meta-data about the source and the annotations

#### How were labels chosen?

<!-- info: How were the labels chosen? -->
<!-- scope: microscope -->
The initial table-description pairs are tables from Wikipedia articles, extracted through heuristics such as Number Matching (tables and sentences that overlap with a non-date number of atleast 3 non-zero digits) (Refer to Section 4 of the paper for more)

1. Table Readability: Tables which are deemed non-readable (due to foreign language, poor formatting etc - a very small fraction of 0.5%) are removed from the dataset here.
2. Cell Highlighting: The annotator highlights the cells of the table which support the description.
3. Deletion: The annotator removes phrases in the description which are not supported by the highlighted cells
4. Decontextualization: Descriptions may contain pronouns or other forms of anaphora, or other phenomena which depend on the overall article topic - these are fixed by replacement (e.g replacing pronouns with the entity, provided it occurs in the table). The replacements allowed are limited to one, and annotators are also instructed to conserve fluency.
5. Secondary Annotation: A second set of annotators is shown the output of Stage 4, and asked to fix it if required to ensure it is grammatical.


#### Example Instance

<!-- info: Provide a JSON formatted example of a typical instance in the dataset. -->
<!-- scope: periscope -->
The main repository's `README.md` already provides a thorough walkthrough of data instances and fields [here](https://github.com/google-research-datasets/totto#dataset-description)

Below is the instance for a table from the wiki-page for the musical artist _Weird Al' Yankovic_ , likely listing his on-television appearances.

```
    {
      "table_page_title": "'Weird Al' Yankovic",
      "table_webpage_url": "https://en.wikipedia.org/wiki/%22Weird_Al%22_Yankovic",
      "table_section_title": "Television",
      "table_section_text": "",
      "table": "[Described below]",
      "highlighted_cells": [[22, 2], [22, 3], [22, 0], [22, 1], [23, 3], [23, 1], [23, 0]],
      "example_id": 12345678912345678912,
      "sentence_annotations": [{"original_sentence": "In 2016, Al appeared in 2 episodes of BoJack Horseman as Mr. Peanutbutter's brother, Captain Peanutbutter, and was hired to voice the lead role in the 2016 Disney XD series Milo Murphy's Law.",
		      "sentence_after_deletion": "In 2016, Al appeared in 2 episodes of BoJack Horseman as Captain Peanutbutter, and was hired to the lead role in the 2016 series Milo Murphy's Law.",
		      "sentence_after_ambiguity": "In 2016, Al appeared in 2 episodes of BoJack Horseman as Captain Peanutbutter, and was hired for the lead role in the 2016 series Milo Murphy's 'Law.",
		      "final_sentence": "In 2016, Al appeared in 2 episodes of BoJack Horseman as Captain Peanutbutter and was hired for the lead role in the 2016 series Milo Murphy's Law."}],
    }
```

The `table` field is expanded as below:

```
    [
     [
        {
            "column_span": 1,
             "is_header": true,
             "row_span": 1,
             "value": "Year"},
        {    "column_span": 1,
             "is_header": true,
             "row_span": 1,
             "value": "Title"},
        {    "column_span": 1,
             "is_header": true,
             "row_span": 1,
             "value": "Role"},
        {    "column_span": 1,
             "is_header": true,
             "row_span": 1,
             "value": "Notes"}
      ],
      [
        {    "column_span": 1,
             "is_header": false,
             "row_span": 1,
             "value": "1997"},
        {    "column_span": 1,
             "is_header": false,
             "row_span": 1,
             "value": "Eek! The Cat"},
        {    "column_span": 1,
             "is_header": false,
             "row_span": 1,
             "value": "Himself"},
        {    "column_span": 1,
             "is_header": false,
             "row_span": 1,
             "value": "Episode: 'The FugEektive'"}
      ], ...
    ]
```

The [Supplementary Repo](https://github.com/google-research/language/tree/master/language/totto) also provides browsable samples under its `sample/` folder. It additionally provides HTML visualization scripts with their outputs located under the aforementioned folder. The instructions to access and visualize these samples can also be found [here](https://github.com/google-research/language/tree/master/language/totto#visualizing-sample-data).


#### Data Splits

<!-- info: Describe and name the splits in the dataset if there are more than one. -->
<!-- scope: periscope -->
The dataset consists of 120,000 train examples and equi-sized dev and test sets with 7700 examples.
Refer to Table 5 in the paper for a more extensive list of properties about table size, target vocabulary etc and their aggregates.


#### Splitting Criteria

<!-- info: Describe any criteria for splitting the data, if used. If there are differences between the splits (e.g., if the training annotations are machine-generated and the dev and test ones are created by humans, or if different numbers of annotators contributed to each example), describe them here. -->
<!-- scope: microscope -->
The dev and test splits are further equally distributed between  _Overlap_ and _non-Overlap_ .
The examples in the _Overlap_ set are harder on account of the domain shift resulting from them having none of their header (row and column) names in common with those seen during training.

Refer to Table 5 in the paper for a more extensive list of properties about table size, target vocabulary etc and their aggregates.


#### 

<!-- info: What does an outlier of the dataset in terms of length/perplexity/embedding look like? -->
<!-- scope: microscope -->
There are some very large tables in the dataset with thousands of rows. Table 7 shows some of the challenges of the dataset, showing that very few examples require access to the table description itself which makes those examples an outlier. 



## Dataset in GEM

### Rationale for Inclusion in GEM

#### Why is the Dataset in GEM?

<!-- info: What does this dataset contribute toward better generation evaluation and why is it part of GEM? -->
<!-- scope: microscope -->
ToTTo is one of the two datasets representing Table-to-Text NLG in GEM, the other one being [DART](https://arxiv.org/pdf/2007.02871.pdf). Unlike DART, which combines datasets from multiple sources and furnishes them in a unified setting, ToTTo is from a homogeneous source. As explained in the Task Summary above, it also has an annotation process explicitly crafted to reduce divergent descriptions, which is not true of DART.

Furthermore, ToTTo is also an instance of a **controlled** generation task - where in addition to the input (in this case the table) an additional **control** (in this case the highlighted cells) is given as an additional goal for the generation. The DART task formulation does not include controls.


#### Similar Datasets

<!-- info: Do other datasets for the high level task exist? -->
<!-- scope: telescope -->
yes

#### Unique Language Coverage

<!-- info: Does this dataset cover other languages than other datasets for the same task? -->
<!-- scope: periscope -->
no

#### Difference from other GEM datasets

<!-- info: What else sets this dataset apart from other similar datasets in GEM? -->
<!-- scope: microscope -->
The input is much more complex and the quality much better than that of comparable datasets. The highlighted table cells provide a unique challenge to models. 

#### Ability that the Dataset measures

<!-- info: What aspect of model ability can be measured with this dataset? -->
<!-- scope: periscope -->
Reasoning, surface realization


### GEM-Specific Curation

#### Modificatied for GEM?

<!-- info: Has the GEM version of the dataset been modified in any way (data, processing, splits) from the original curated data? -->
<!-- scope: telescope -->
yes

#### Additional Splits?

<!-- info: Does GEM provide additional splits to the dataset? -->
<!-- scope: telescope -->
yes

#### Split Information

<!-- info: Describe how the new splits were created -->
<!-- scope: periscope -->
9 challenge sets for ToTTo were added to the GEM evaluation suite, 8 created specifically for the task and 1 coming from the original data.

1. We created subsets of the training and development sets of 500 randomly selected inputs each.
2. We applied input scrambling on a subset of 500 randomly selected test instances; the order of the highlighted cells was randomly reassigned.
3. For the input size, we created subpopulations based on the number of input highlighted cells in the whole table.

| Input length  | Frequency English |
|---------------|-------------------|
| 1             |               898 |
| 2             |              1850 |
| 3             |              2221 |
| 4             |              1369 |
| 5             |               483 |
| 6             |               379 |
| 7             |               124 |
| 8             |               128 |
| 9             |                61 |
| 10            |                40 |
| 11            |                20 |
| 12            |                26 |
| 13            |                10 |
| 14            |                14 |
| 15            |                14 |
| 16            |                 7 |
| 17            |                 6 |
| 18            |                 5 |
| 19            |                 5 |
| 20            |                 5 |
| 21            |                 4 |
| 22            |                 1 |
| 23            |                 2 |
| 24            |                 4 |
| 25            |                 1 |
| 26...496      |                 1 |

4. We also divided the test set according to the size of the whole table, based on the idea that larger tables represent a bigger space to take into account when generating the highlighted cells; a larger table could be more challenging to generate accurate text than a smaller table. There are 693 different table sizes, ranging from 2 to 15834 cells.

| Table size      |Frequency English|
|-----------------|-----------------|
| 2               |             71  |
| 3               |             52  |
| 4               |             36  |
| 5               |             41  |
| 6               |            144  |
| 7               |             47  |
| 8               |             59  |
| 9               |            105  |
| 10              |            162  |
| 11              |             36  |
| 12              |            158  |
| 13              |             35  |
| 14              |             79  |
| 15              |            136  |
| 16              |            111  |
| 17              |             48  |
| 18              |            123  |
| 19              |             29  |
| 20              |            112  |
| 21              |             91  |
| 22              |             17  |
| 23              |              7  |
| 24              |            169  |
| 25              |             56  |
| 26              |             12  |
| 27              |             40  |
| 28              |             77  |
| 29              |              7  |
| 30              |            122  |
| 31              |              4  |
| 32              |             49  |
| 33              |             21  |
| 34              |              7  |
| 35              |            103  |
| 36              |            131  |
| 37              |             10  |
| 38              |              6  |
| 39              |             26  |
| 40              |            110  |
| 41              |              1  |
| 42              |             54  |
| 43              |              6  |
| 44              |             47  |
| 45              |             79  |
| 46              |              4  |
| 47              |              2  |
| 48              |            114  |
| 49              |             18  |
| 50              |             55  |
| 51              |             11  |
| 52              |             43  |
| 54              |             80  |
| 55              |             73  |
| 56              |             64  |
| 57              |             12  |
| 58              |              1  |
| 60              |            114  |
| 61              |              4  |
| 63              |             39  |
| 64              |             36  |
| 65              |             62  |
| 66              |             48  |
| 67              |              1  |
| 68              |             36  |
| 69              |              6  |
| 70              |             81  |
| 72              |             76  |
| 73              |              1  |
| 74              |              1  |
| 75              |             44  |
| 76              |             33  |
| 77              |             30  |
| 78              |             66  |
| 79              |              1  |
| 80              |             83  |
| 81              |             12  |
| 82              |              1  |
| 84              |             80  |
| 85              |             25  |
| 86              |              1  |
| 87              |              3  |
| 88              |             35  |
| 90              |             78  |
| 91              |             18  |
| 92              |             22  |
| 93              |              5  |
| 94              |              2  |
| 95              |             31  |
| 96              |             50  |
| 98              |             11  |
| 99              |             14  |
| 100             |             48  |
| 102             |             24  |
| 104             |             29  |
| 105             |             36  |
| 106             |              2  |
| 108             |             51  |
| 110             |             31  |
| ...8000+        |   (up to 10)    |

5. We also created three splits based on the subset of test examples in pages about people.
We then used the structured information in WikiData to identify the following information:

-  gender (male, and female),
- nationality grouped by continent (Africa, Asia, Europe, North America, Oceania, and South America)
- ethnicity (African American and all USA)

The categories within gender, ethnicity, and nationality were chosen based on data availability; The ToTTo dataset includes mostly tables that do not focus on people. As a result, only seven people in the original test set are marked as having a non-binary gender. Similar sparsity informed the grouping of nationalities by continent – only 19 countries are represented by more than 10 people in the test set. In case a person has citizenships across multiple continents, we may include the person in any of the included continents.

Finally, ethnicity is very sparsely annotated in WikiData; only 150 test examples in ToTTo have this information and 128 of these are African Americans. We thus are unable to compare the performance on, e.g., Yoruba or Punjabi people, both of which have fewer than five instances. Another caveat here is that only 21 of the 128 people are female. We thus compare the African American population to results on a subset that includes all US citizens.




#### Split Motivation

<!-- info: What aspects of the model's generation capacities were the splits created to test? -->
<!-- scope: periscope -->
generalization, fairness, robustness


### Getting Started with the Task

#### Pointers to Resources

<!-- info: Getting started with in-depth research on the task. Add relevant pointers to resources that researchers can consult when they want to get started digging deeper into the task. -->
<!-- scope: microscope -->
- The highest spot on the leaderboard is currently held by an anonymous method, with BLEU=49.2, PARENT=58.7 and BLEURT=0.249 on the _Overall_ test set.
- The **highest scoring non-anonymous** method is the T5-based method of [Kale, 2020](https://arxiv.org/abs/2005.10433). This method uses a simple row-major linearization scheme to convert the table (it chooses only the highlighted cells and ignores the other cells - table titles and section titles are prefixed at the start of the respective section table) to a flat string. The linearized input - output description pairs from training examples are then used to finetune T5, with BLEU being used as the dev metric to pick checkpoints, and beam search with beam size 10 being the decoding method.

    Though the best numbers from this method are naturally from the largest T5-pretrained architecture (T5-3B), the paper shows improvements over the next-highest BERT-to-BERT method even when using T5-Base or T5-Small, which have the same and lesser parameters than BERT-to-BERT respectively.

- The [Supplementary Repo](https://github.com/google-research/language/tree/master/language/totto) provides several useful modules to get started with for new approach implementation:

    1. Code for the particular preprocessing / linearization scheme used to linearize the tables into flat sequences for the baseline approaches described in the paper has been described and shared [herein](https://github.com/google-research/language/tree/master/language/totto#baseline-preprocessing)

    2. An [evaluation script](https://github.com/google-research/language/tree/master/language/totto#running-the-evaluation-scripts-locally) for locally scoring BLEU and PARENT system outputs on dev (or train) sets. Since BLEURT is a model-based metric, a [slightly separate](https://github.com/google-research/language/tree/master/language/totto#running-the-evaluation-scripts-locall://github.com/google-research/language/tree/master/language/totto#computing-the-bleurt-score) set of instructions is provided to evaluate on the same.




## Previous Results

### Previous Results

#### Measured Model Abilities

<!-- info: What aspect of model ability can be measured with this dataset? -->
<!-- scope: telescope -->
Reasoning, surface realization

#### Metrics

<!-- info: What metrics are typically used for this task? -->
<!-- scope: periscope -->
`BLEU`, `BLEURT`, `Other: Other Metrics`

#### Other Metrics

<!-- info: Definitions of other metrics -->
<!-- scope: periscope -->
Parent: a metric that measures the F-1 score of overlap between input content words and those used in references and those in generated text while ignoring the general surface form. It can thus measure the faithfulness much better than metrics that measure overlap with a reference

#### Proposed Evaluation

<!-- info: List and describe the purpose of the metrics and evaluation methodology (including human evaluation) that the dataset creators used when introducing this task. -->
<!-- scope: microscope -->
The metrics are used as in the leaderboard. The original paper additionally conducted a human evaluation focusing on fluency, faithfulness, and coverage. 
Faithfulness was measured as whether facts in the text are not supported by the input, and coverage as the number of highlighted cells that were considered. They thus represent precision and recall of the content. 

#### Previous results available?

<!-- info: Are previous results available? -->
<!-- scope: telescope -->
yes

#### Relevant Previous Results

<!-- info: What are the most relevant previous results for this task/dataset? -->
<!-- scope: microscope -->
See leaderboard.



## Dataset Curation

### Original Curation

#### Original Curation Rationale

<!-- info: Original curation rationale -->
<!-- scope: telescope -->
Tables occurring in Wikipedia articles were chosen as the data source with the following reasons in mind:

1. Wide coverage in terms of both vocabulary and concepts.
2. Wikipedia tables are not confined to a regular structure, with multi-row or multi-column cells occurring with a sufficient frequency.
3. Likely to contain reasonable-quality, natural text descriptions in the proximity of the table, which are also extractable by heuristics. (see the start of Section 4 for the heuristics used)


To prevent an overlap with the earlier [Wikibio](https://arxiv.org/abs/1603.07771)  dataset which focussed on Infobox-first sentence pairs from Wikipedia biography articles, the authors avoid using Infoboxes as a data source.

The overall curation process of initially collecting free text and then annotator-revising it, was designed to combine the advantages of free-form text descriptions (which are fluent, high-quality and unhurriedly written, but also divergent and unfaithful) with annotator descriptions (which can be tailored to be faithful and to conform exactly to desired task requirements)


#### Communicative Goal

<!-- info: What was the communicative goal? -->
<!-- scope: periscope -->
The speaker is required to produce a single, coherent English sentence that describes the highlighted cells in the given table, also using metadata and any other information from the table as applicable.


#### Sourced from Different Sources

<!-- info: Is the dataset aggregated from different data sources? -->
<!-- scope: telescope -->
yes

#### Source Details

<!-- info: List the sources (one per line) -->
<!-- scope: periscope -->
wikipedia.org


### Language Data

#### How was Language Data Obtained?

<!-- info: How was the language data obtained? -->
<!-- scope: telescope -->
`Crowdsourced`

#### Where was it crowdsourced?

<!-- info: If crowdsourced, where from? -->
<!-- scope: periscope -->
`Other crowdworker platform`

#### Language Producers

<!-- info: What further information do we have on the language producers? -->
<!-- scope: microscope -->
The basic source language producers are Wikipedia authors and/or editors, since the annotation starts with the natural text description near the Wikipedia table.
The auxiliary source language producers are the annotators (two per example) who iteratively revise these descriptions to make them unambiguous and faithful to a subset of highlighted cells in the table.


#### Data Validation

<!-- info: Was the text validated by a different worker or a data curator? -->
<!-- scope: telescope -->
validated by crowdworker

#### Data Preprocessing

<!-- info: How was the text data pre-processed? (Enter N/A if the text was not pre-processed) -->
<!-- scope: microscope -->
The initial table-description pairs are tables from Wikipedia articles, extracted through heuristics such as Number Matching (tables and sentences that overlap with a non-date number of atleast 3 non-zero digits) (Refer to Section 4 of the paper for more)

1. Table Readability: Tables which are deemed non-readable (due to foreign language, poor formatting etc - a very small fraction of 0.5%) are removed from the dataset here.
2. Cell Highlighting: The annotator highlights the cells of the table which support the description.
3. Deletion: The annotator removes phrases in the description which are not supported by the highlighted cells
4. Decontextualization: Descriptions may contain pronouns or other forms of anaphora, or other phenomena which depend on the overall article topic - these are fixed by replacement (e.g replacing pronouns with the entity, provided it occurs in the table). The replacements allowed are limited to one, and annotators are also instructed to conserve fluency.
5. Secondary Annotation: A second set of annotators is shown the output of Stage 4, and asked to fix it if required to ensure it is grammatical.

The paper does not specifically describe the annotation platform or location profiles of the annotators.



#### Was Data Filtered?

<!-- info: Were text instances selected or filtered? -->
<!-- scope: telescope -->
algorithmically

#### Filter Criteria

<!-- info: What were the selection criteria? -->
<!-- scope: microscope -->
After construction of the splits, the data curators filtered training examples that had rare table header combinations (<=5 examples) and which had an overlap with the validation or test splits. 


### Structured Annotations

#### Additional Annotations?

<!-- quick -->
<!-- info: Does the dataset have additional annotations for each instance? -->
<!-- scope: telescope -->
none

#### Annotation Service?

<!-- info: Was an annotation service used? -->
<!-- scope: telescope -->
no


### Consent

#### Any Consent Policy?

<!-- info: Was there a consent policy involved when gathering the data? -->
<!-- scope: telescope -->
yes

#### Consent Policy Details

<!-- info: What was the consent policy? -->
<!-- scope: microscope -->
Annotators were full time employees that were aware of the goal of the project and consented to having the data released as part of the dataset. 


### Private Identifying Information (PII)

#### Contains PII?

<!-- quick -->
<!-- info: Does the source language data likely contain Personal Identifying Information about the data creators or subjects? -->
<!-- scope: telescope -->
no PII

#### Justification for no PII

<!-- info: Provide a justification for selecting `no PII` above. -->
<!-- scope: periscope -->
Since the source data is from wikipedia, only data in the public domain is included in the dataset.


### Maintenance

#### Any Maintenance Plan?

<!-- info: Does the original dataset have a maintenance plan? -->
<!-- scope: telescope -->
yes

#### Maintenance Plan Details

<!-- info: Describe the original dataset's maintenance plan. -->
<!-- scope: microscope -->
For submissions, you can delete your data by emailing totto@google.com from the email account used to sign up for the submission. Deletion requests will be responded to within 60 days. 

#### Maintainer Contact Information

<!-- info: Provide contact information of a person responsible for the dataset maintenance -->
<!-- scope: periscope -->
Ankur Parikh (aparikh@google.com)

#### Any Contestation Mechanism?

<!-- info: Does the maintenance plan include a contestation mechanism allowing individuals to request removal fo content? -->
<!-- scope: periscope -->
form submission

#### Contestation Form Link

<!-- info: Provide the form link or contact information -->
<!-- scope: periscope -->
totto@google.com



## Broader Social Context

### Previous Work on the Social Impact of the Dataset

#### Usage of Models based on the Data

<!-- info: Are you aware of cases where models trained on the task featured in this dataset ore related tasks have been used in automated systems? -->
<!-- scope: telescope -->
no


### Impact on Under-Served Communities

#### Addresses needs of underserved Communities?

<!-- info: Does this dataset address the needs of communities that are traditionally underserved in language technology, and particularly language generation technology? Communities may be underserved for exemple because their language, language variety, or social or geographical context is underepresented in NLP and NLG resources (datasets and models). -->
<!-- scope: telescope -->
no


### Discussion of Biases

#### Any Documented Social Biases?

<!-- info: Are there documented social biases in the dataset? Biases in this context are variations in the ways members of different social categories are represented that can have harmful downstream consequences for members of the more disadvantaged group. -->
<!-- scope: telescope -->
yes

#### Links and Summaries of Analysis Work

<!-- info: Provide links to and summaries of works analyzing these biases. -->
<!-- scope: microscope -->
The original work as well as our GEM paper analyzes some biases

#### Are the Language Producers Representative of the Language?

<!-- info: Does the distribution of language producers in the dataset accurately represent the full distribution of speakers of the language world-wide? If not, how does it differ? -->
<!-- scope: periscope -->
This dataset is created using tables and the table cell contents may hence naturally exhibit biases which have been found to exist in Wikipedia such as some forms of gender bias (e.g [(Graells-Garido et al.,2015)](https://labtomarket.files.wordpress.com/2018/01/wiki_gender_bias.pdf) notes that spouse information is more likely discussed for females than males)

The table descriptions (targets/references) are, as discussed earlier, collected through a two-step process.
1. The natural text description near the table is taken as a starting point. This is Wikipedia article text as created upto that point in time by a chain of collaborative edits from Wikipedia authors.
2. The initial description is revised by chain of two or more annotated revisions, to make it unambiguous and faithful to a set of highlighted table cells.

From their origin in 1), the descriptions may exhibit biases seen in Wikipedia text as mentioned above. From their revisions in 2), the descriptions may show biases originating from annotator-authored text, such as a preference for shorter descriptions since they're faster to write, or linguistic preferences influenced by the locations dominant in the annotator distribution.  (However, note that these are likely to be much reduced since the annotators here are merely revising rather than completely authoring. Moreover, each sentence goes through atleast two annotators, which acts as a check against the personal biases of a single annotator.)

Naturally-occurring text is also known to suffer from other biases such as reporting bias [(Gordon and Van Durme, 2013)](https://openreview.net/forum?id=AzxEzvpdE3Wcy&noteId=vmR8qaby8fqxittps://labtomarket.files.wordpress.com/2018/01/wiki_gender_bias.pdf) - this also applies to this dataset via its origin from Wikipedia.





## Considerations for Using the Data

### PII Risks and Liability

#### Potential PII Risk

<!-- info: Considering your answers to the PII part of the Data Curation Section, describe any potential privacy to the data subjects and creators risks when using the dataset. -->
<!-- scope: microscope -->
Since the source data is from wikipedia, only data in the public domain is included in the dataset.


### Licenses

#### Copyright Restrictions on the Dataset

<!-- info: Based on your answers in the Intended Use part of the Data Overview Section, which of the following best describe the copyright and licensing status of the dataset? -->
<!-- scope: periscope -->
`open license - commercial use allowed`

#### Copyright Restrictions on the Language Data

<!-- info: Based on your answers in the Language part of the Data Curation Section, which of the following best describe the copyright and licensing status of the underlying language data? -->
<!-- scope: periscope -->
`open license - commercial use allowed`


### Known Technical Limitations

#### Technical Limitations

<!-- info: Describe any known technical limitations, such as spurrious correlations, train/test overlap, annotation biases, or mis-annotations, and cite the works that first identified these limitations when possible. -->
<!-- scope: microscope -->
The dataset is limited to topics that are present in Wikipedia, more specifically those topics that are present in articles which contain atleast one table
_Sports_ and _Countries_ form 53.4% of the dataset. The remaining fraction is made up of broader topics like _Europe_, *North America*and _Politics_



