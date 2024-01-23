---
annotations_creators:
- crowd-sourced
language_creators:
- unknown
language:
- en
license:
- other
multilinguality:
- unknown
size_categories:
- unknown
source_datasets:
- original
task_categories:
- text2text-generation
task_ids:
- text-simplification
pretty_name: wiki_auto_asset_turk
---

# Dataset Card for GEM/wiki_auto_asset_turk

## Dataset Description

- **Homepage:** n/a
- **Repository:** https://github.com/chaojiang06/wiki-auto, [ASSET repository
- **Paper:** https://aclanthology.org/2020.acl-main.709/, [ASSET
- **Leaderboard:** N/A
- **Point of Contact:** WikiAuto: Chao Jiang; ASSET: Fernando Alva-Manchego and Louis Martin; TURK: Wei Xu

### Link to Main Data Card

You can find the main data card on the [GEM Website](https://gem-benchmark.com/data_cards/wiki_auto_asset_turk).

### Dataset Summary 

WikiAuto is an English simplification dataset that we paired with ASSET and TURK, two very high-quality evaluation datasets, as test sets. The input is an English sentence taken from Wikipedia and the target a simplified sentence. ASSET and TURK contain the same test examples but have references that are simplified in different ways (splitting sentences vs. rewriting and splitting).

You can load the dataset via:
```
import datasets
data = datasets.load_dataset('GEM/wiki_auto_asset_turk')
```
The data loader can be found [here](https://huggingface.co/datasets/GEM/wiki_auto_asset_turk).

#### website
n/a

#### paper
[WikiAuto](https://aclanthology.org/2020.acl-main.709/), [ASSET](https://aclanthology.org/2020.acl-main.424/), [TURK](https://aclanthology.org/Q16-1029/)

#### authors
WikiAuto: Chao Jiang, Mounica Maddela, Wuwei Lan, Yang Zhong, Wei Xu; ASSET: Fernando Alva-Manchego, Louis Martin, Antoine Bordes, Carolina Scarton, and Benoîıt Sagot, and Lucia Specia; TURK: Wei Xu, Courtney Napoles, Ellie Pavlick, Quanze Chen, and Chris Callison-Burch

## Dataset Overview

### Where to find the Data and its Documentation

#### Download

<!-- info: What is the link to where the original dataset is hosted? -->
<!-- scope: telescope -->
[Wiki-Auto repository](https://github.com/chaojiang06/wiki-auto), [ASSET repository](https://github.com/facebookresearch/asset), [TURKCorpus](https://github.com/cocoxu/simplification)

#### Paper

<!-- info: What is the link to the paper describing the dataset (open access preferred)? -->
<!-- scope: telescope -->
[WikiAuto](https://aclanthology.org/2020.acl-main.709/), [ASSET](https://aclanthology.org/2020.acl-main.424/), [TURK](https://aclanthology.org/Q16-1029/)

#### BibTex

<!-- info: Provide the BibTex-formatted reference for the dataset. Please use the correct published version (ACL anthology, etc.) instead of google scholar created Bibtex. -->
<!-- scope: microscope -->
WikiAuto: 
```
@inproceedings{jiang-etal-2020-neural,
    title = "Neural {CRF} Model for Sentence Alignment in Text Simplification",
    author = "Jiang, Chao  and
      Maddela, Mounica  and
      Lan, Wuwei  and
      Zhong, Yang  and
      Xu, Wei",
    booktitle = "Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics",
    month = jul,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.acl-main.709",
    doi = "10.18653/v1/2020.acl-main.709",
    pages = "7943--7960",
}
```

ASSET:
```
@inproceedings{alva-manchego-etal-2020-asset,
    title = "{ASSET}: {A} Dataset for Tuning and Evaluation of Sentence Simplification Models with Multiple Rewriting Transformations",
    author = "Alva-Manchego, Fernando  and
      Martin, Louis  and
      Bordes, Antoine  and
      Scarton, Carolina  and
      Sagot, Beno{\^\i}t  and
      Specia, Lucia",
    booktitle = "Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics",
    month = jul,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.acl-main.424",
    pages = "4668--4679",
}
```

TURK:
```
@article{Xu-EtAl:2016:TACL,
 author = {Wei Xu and Courtney Napoles and Ellie Pavlick and Quanze Chen and Chris Callison-Burch},
 title = {Optimizing Statistical Machine Translation for Text Simplification},
 journal = {Transactions of the Association for Computational Linguistics},
 volume = {4},
 year = {2016},
 url = {https://cocoxu.github.io/publications/tacl2016-smt-simplification.pdf},
 pages = {401--415}
 }
 ```

#### Contact Name

<!-- quick -->
<!-- info: If known, provide the name of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
WikiAuto: Chao Jiang; ASSET: Fernando Alva-Manchego and Louis Martin; TURK: Wei Xu

#### Contact Email

<!-- info: If known, provide the email of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
jiang.1530@osu.edu, f.alva@sheffield.ac.uk, louismartincs@gmail.com, wei.xu@cc.gatech.edu

#### Has a Leaderboard?

<!-- info: Does the dataset have an active leaderboard? -->
<!-- scope: telescope -->
no


### Languages and Intended Use

#### Multilingual?

<!-- quick -->
<!-- info: Is the dataset multilingual? -->
<!-- scope: telescope -->
no

#### Covered Languages

<!-- quick -->
<!-- info: What languages/dialects are covered in the dataset? -->
<!-- scope: telescope -->
`English`

#### Whose Language?

<!-- info: Whose language is in the dataset? -->
<!-- scope: periscope -->
Wiki-Auto contains English text only (BCP-47: `en`). It is presented as a translation task where Wikipedia Simple English is treated as its own idiom. For a statement of what is intended (but not always observed) to constitute Simple English on this platform, see [Simple English in Wikipedia](https://simple.wikipedia.org/wiki/Wikipedia:About#Simple_English).
Both ASSET and TURK use crowdsourcing to change references, and their language is thus a combination of the WikiAuto data and the language of the demographic on mechanical Turk

#### License

<!-- quick -->
<!-- info: What is the license of the dataset? -->
<!-- scope: telescope -->
other: Other license

#### Intended Use

<!-- info: What is the intended use of the dataset? -->
<!-- scope: microscope -->
WikiAuto provides a set of aligned sentences from English Wikipedia and Simple English Wikipedia as a resource to train sentence simplification systems.

The authors first crowd-sourced a set of manual alignments between sentences in a subset of the Simple English Wikipedia and their corresponding versions in English Wikipedia (this corresponds to the `manual` config in this version of the dataset), then trained a neural CRF system to predict these alignments.

The trained alignment prediction model was then applied to the other articles in Simple English Wikipedia with an English counterpart to create a larger corpus of aligned sentences (corresponding to the `auto` and `auto_acl` configs here).

[ASSET](https://github.com/facebookresearch/asset) [(Alva-Manchego et al., 2020)](https://www.aclweb.org/anthology/2020.acl-main.424.pdf) is multi-reference dataset for the evaluation of sentence simplification in English. The dataset uses the same 2,359 sentences from [TurkCorpus](https://github.com/cocoxu/simplification/) [(Xu et al., 2016)](https://www.aclweb.org/anthology/Q16-1029.pdf) and each sentence is associated with 10 crowdsourced simplifications. Unlike previous simplification datasets, which contain a single transformation (e.g., lexical paraphrasing in TurkCorpus or sentence
splitting in [HSplit](https://www.aclweb.org/anthology/D18-1081.pdf)), the simplifications in ASSET encompass a variety of rewriting transformations.

TURKCorpus is a high quality simplification dataset where each source (not simple) sentence is associated with 8 human-written simplifications that focus on lexical paraphrasing. It is one of the two evaluation datasets for the text simplification task in GEM. It acts as the validation and test set for paraphrasing-based simplification that does not involve sentence splitting and deletion.

#### Add. License Info

<!-- info: What is the 'other' license of the dataset? -->
<!-- scope: periscope -->
WikiAuto: `CC BY-NC 3.0`, ASSET: `CC BY-NC 4.0`, TURK: `GNU General Public License v3.0`

#### Primary Task

<!-- info: What primary task does the dataset support? -->
<!-- scope: telescope -->
Simplification

#### Communicative Goal

<!-- quick -->
<!-- info: Provide a short description of the communicative goal of a model trained for this task on this dataset. -->
<!-- scope: periscope -->
The goal is to communicate the main ideas of source sentence in a way that is easier to understand by non-native speakers of English.



### Credit

#### Curation Organization Type(s)

<!-- info: In what kind of organization did the dataset curation happen? -->
<!-- scope: telescope -->
`academic`, `industry`

#### Curation Organization(s)

<!-- info: Name the organization(s). -->
<!-- scope: periscope -->
Ohio State University, University of Sheffield, Inria, Facebook AI Research, Imperial College London, University of Pennsylvania, John Hopkins University

#### Dataset Creators

<!-- info: Who created the original dataset? List the people involved in collecting the dataset and their affiliation(s). -->
<!-- scope: microscope -->
WikiAuto: Chao Jiang, Mounica Maddela, Wuwei Lan, Yang Zhong, Wei Xu; ASSET: Fernando Alva-Manchego, Louis Martin, Antoine Bordes, Carolina Scarton, and Benoîıt Sagot, and Lucia Specia; TURK: Wei Xu, Courtney Napoles, Ellie Pavlick, Quanze Chen, and Chris Callison-Burch

#### Funding

<!-- info: Who funded the data creation? -->
<!-- scope: microscope -->
WikiAuto: NSF, ODNI, IARPA, Figure Eight AI, and Criteo. ASSET: PRAIRIE Institute, ANR. TURK: NSF

#### Who added the Dataset to GEM?

<!-- info: Who contributed to the data card and adding the dataset to GEM? List the people+affiliations involved in creating this data card and who helped integrate this dataset into GEM. -->
<!-- scope: microscope -->
GEM v1 had separate data cards for WikiAuto, ASSET, and TURK. They were contributed by Dhruv Kumar and Mounica Maddela. The initial data loader was written by Yacine Jernite. Sebastian Gehrmann merged and extended the data cards and migrated the loader to the v2 infrastructure. 


### Dataset Structure

#### Data Fields

<!-- info: List and describe the fields present in the dataset. -->
<!-- scope: telescope -->
- `source`: A source sentence from one of the datasets
- `target`: A single simplified sentence corresponding to `source`
- `references`: In the case of ASSET/TURK, references is a list of strings corresponding to the different references. 

#### Reason for Structure

<!-- info: How was the dataset structure determined? -->
<!-- scope: microscope -->
The underlying datasets have extensive secondary annotations that can be used in conjunction with the GEM version. We omit those annotations to simplify the format into one that can be used by seq2seq models. 

#### Example Instance

<!-- info: Provide a JSON formatted example of a typical instance in the dataset. -->
<!-- scope: periscope -->
```
{
  'source': 'In early work, Rutherford discovered the concept of radioactive half-life , the radioactive element radon, and differentiated and named alpha and beta radiation .',
 'target': 'Rutherford discovered the radioactive half-life, and the three parts of radiation which he named Alpha, Beta, and Gamma.'
}
```

#### Data Splits

<!-- info: Describe and name the splits in the dataset if there are more than one. -->
<!-- scope: periscope -->
In WikiAuto, which is used as training and validation set, the following splits are provided: 

|                            | Tain   | Dev   | Test   |
| -----                      | ------ | ----- | ----   |
| Total sentence pairs       | 373801 | 73249 | 118074 |
| Aligned sentence pairs     |  1889  |  346  | 677    |

ASSET does not contain a training set; many models use [WikiLarge](https://github.com/XingxingZhang/dress) (Zhang and Lapata, 2017) for training. For GEM, [Wiki-Auto](https://github.com/chaojiang06/wiki-auto) will be used for training the model.

Each input sentence has 10 associated reference simplified sentences. The statistics of ASSET are given below.

|                            | Dev    | Test | Total |
| -----                      | ------ | ---- | ----- |
| Input Sentences            | 2000   | 359  | 2359  |
| Reference Simplifications  | 20000  | 3590 | 23590 |

The test and validation sets are the same as those of [TurkCorpus](https://github.com/cocoxu/simplification/). The split was random.

There are 19.04 tokens per reference on average (lower than 21.29 and 25.49 for TurkCorpus and HSplit, respectively). Most (17,245) of the referece sentences do not involve sentence splitting.

TURKCorpus does not contain a training set; many models use [WikiLarge](https://github.com/XingxingZhang/dress) (Zhang and Lapata, 2017) or [Wiki-Auto](https://github.com/chaojiang06/wiki-auto) (Jiang et. al 2020) for training.

Each input sentence has 8 associated reference simplified sentences. 2,359 input sentences are randomly split into 2,000 validation and 359 test sentences.

|                            | Dev    | Test | Total |
| -----                      | ------ | ---- | ----- |
| Input Sentences            | 2000   | 359  | 2359  |
| Reference Simplifications  | 16000  | 2872 | 18872 |


There are 21.29 tokens per reference on average.



#### Splitting Criteria

<!-- info: Describe any criteria for splitting the data, if used. If there are differences between the splits (e.g., if the training annotations are machine-generated and the dev and test ones are created by humans, or if different numbers of annotators contributed to each example), describe them here. -->
<!-- scope: microscope -->
In our setup, we use WikiAuto as training/validation corpus and ASSET and TURK as test corpora. ASSET and TURK have the same inputs but differ in their reference style. Researchers can thus conduct targeted evaluations based on the strategies that a model should learn. 



## Dataset in GEM

### Rationale for Inclusion in GEM

#### Why is the Dataset in GEM?

<!-- info: What does this dataset contribute toward better generation evaluation and why is it part of GEM? -->
<!-- scope: microscope -->
WikiAuto is the largest open text simplification dataset currently available. ASSET and TURK are high quality test sets that are compatible with WikiAuto. 


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
It's unique setup with multiple test sets makes the task interesting since it allows for evaluation of multiple generations and systems that simplify in different ways. 

#### Ability that the Dataset measures

<!-- info: What aspect of model ability can be measured with this dataset? -->
<!-- scope: periscope -->
simplification


### GEM-Specific Curation

#### Modificatied for GEM?

<!-- info: Has the GEM version of the dataset been modified in any way (data, processing, splits) from the original curated data? -->
<!-- scope: telescope -->
yes

#### GEM Modifications

<!-- info: What changes have been made to he original dataset? -->
<!-- scope: periscope -->
`other`

#### Modification Details

<!-- info: For each of these changes, described them in more details and provided the intended purpose of the modification -->
<!-- scope: microscope -->
We removed secondary annotations and focus on the simple `input->output` format, but combine the different sub-datasets. 

#### Additional Splits?

<!-- info: Does GEM provide additional splits to the dataset? -->
<!-- scope: telescope -->
yes

#### Split Information

<!-- info: Describe how the new splits were created -->
<!-- scope: periscope -->
we split the original test set according to syntactic complexity of the source sentences. To characterize sentence syntactic complexity, we use the 8-level developmental level (d-level) scale proposed by [Covington et al. (2006)](https://www.researchgate.net/publication/254033869_How_complex_is_that_sentence_A_proposed_revision_of_the_Rosenberg_and_Abbeduto_D-Level_Scale) and the implementation of [Lu, Xiaofei (2010)](https://www.jbe-platform.com/content/journals/10.1075/ijcl.15.4.02lu).
We thus split the original test set into 8 subsets corresponding to the 8 d-levels assigned to source sentences. We obtain the following number of instances per level and average d-level of the dataset:

| Total nb. sentences | L0 | L1 | L2 | L3 | L4 | L5 | L6 | L7 | Mean Level |
|-------------------- | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ---------- |
|                 359 |    166 |      0 |     58 |     32 |      5 |     28 |      7 |     63 |       2.38 |



#### Split Motivation

<!-- info: What aspects of the model's generation capacities were the splits created to test? -->
<!-- scope: periscope -->
The goal was to assess performance when simplifying source sentences with different syntactic structure and complexity. 


### Getting Started with the Task

#### Pointers to Resources

<!-- info: Getting started with in-depth research on the task. Add relevant pointers to resources that researchers can consult when they want to get started digging deeper into the task. -->
<!-- scope: microscope -->
There are recent supervised ([Martin et al., 2019](https://arxiv.org/abs/1910.02677), [Kriz et al., 2019](https://www.aclweb.org/anthology/N19-1317/), [Dong et al., 2019](https://www.aclweb.org/anthology/P19-1331/), [Zhang and Lapata, 2017](https://www.aclweb.org/anthology/D17-1062/)) and unsupervised ([Martin et al., 2020](https://arxiv.org/abs/2005.00352v1), [Kumar et al., 2020](https://www.aclweb.org/anthology/2020.acl-main.707/), [Surya et al., 2019](https://www.aclweb.org/anthology/P19-1198/)) text simplification models that can be used as baselines.



#### Technical Terms

<!-- info: Technical terms used in this card and the dataset and their definitions -->
<!-- scope: microscope -->
The common metric used for automatic evaluation is SARI [(Xu et al., 2016)](https://www.aclweb.org/anthology/Q16-1029/).




## Previous Results

### Previous Results

#### Measured Model Abilities

<!-- info: What aspect of model ability can be measured with this dataset? -->
<!-- scope: telescope -->
Simplification

#### Metrics

<!-- info: What metrics are typically used for this task? -->
<!-- scope: periscope -->
`Other: Other Metrics`, `BLEU`

#### Other Metrics

<!-- info: Definitions of other metrics -->
<!-- scope: periscope -->
SARI: A simplification metric that considers both input and references to measure the "goodness" of words that are added, deleted, and kept. 

#### Proposed Evaluation

<!-- info: List and describe the purpose of the metrics and evaluation methodology (including human evaluation) that the dataset creators used when introducing this task. -->
<!-- scope: microscope -->
The original authors of WikiAuto and ASSET used human evaluation to assess the fluency, adequacy, and simplicity (details provided in the paper). For TURK, the authors measured grammaticality, meaning-preservation, and simplicity gain (details in the paper).

#### Previous results available?

<!-- info: Are previous results available? -->
<!-- scope: telescope -->
no



## Dataset Curation

### Original Curation

#### Original Curation Rationale

<!-- info: Original curation rationale -->
<!-- scope: telescope -->
Wiki-Auto provides a new version of the Wikipedia corpus that is larger, contains 75% less defective pairs and has more complex rewrites than the previous WIKILARGE dataset.


ASSET was created in order to improve the evaluation of sentence simplification. It uses the same input sentences as the [TurkCorpus](https://github.com/cocoxu/simplification/) dataset from [(Xu et al., 2016)](https://www.aclweb.org/anthology/Q16-1029.pdf). The 2,359 input sentences of TurkCorpus are a sample of "standard" (not simple) sentences from the [Parallel Wikipedia Simplification (PWKP)](https://www.informatik.tu-darmstadt.de/ukp/research_6/data/sentence_simplification/simple_complex_sentence_pairs/index.en.jsp) dataset [(Zhu et al., 2010)](https://www.aclweb.org/anthology/C10-1152.pdf), which come from the August 22, 2009 version of Wikipedia. The sentences of TurkCorpus were chosen to be of similar length [(Xu et al., 2016)](https://www.aclweb.org/anthology/Q16-1029.pdf). No further information is provided on the sampling strategy.

The TurkCorpus dataset was developed in order to overcome some of the problems with sentence pairs from Standard and Simple Wikipedia: a large fraction of sentences were misaligned, or not actually simpler [(Xu et al., 2016)](https://www.aclweb.org/anthology/Q16-1029.pdf). However, TurkCorpus mainly focused on *lexical paraphrasing*, and so cannot be used to evaluate simplifications involving *compression* (deletion) or *sentence splitting*. HSplit [(Sulem et al., 2018)](https://www.aclweb.org/anthology/D18-1081.pdf), on the other hand, can only be used to evaluate sentence splitting. The reference sentences in ASSET include a wider variety of sentence rewriting strategies, combining splitting, compression and paraphrasing. Annotators were given examples of each kind of transformation individually, as well as all three transformations used at once, but were allowed to decide which transformations to use for any given sentence.

An example illustrating the differences between TurkCorpus, HSplit and ASSET is given below:

> **Original:** He settled in London, devoting himself chiefly to practical teaching.
>
> **TurkCorpus:** He rooted in London, devoting himself mainly to practical teaching.
>
> **HSplit:** He settled in London. He devoted himself chiefly to practical teaching.
>
> **ASSET:** He lived in London. He was a teacher.


#### Communicative Goal

<!-- info: What was the communicative goal? -->
<!-- scope: periscope -->
The goal is to communicate the same information as the source sentence using simpler words and grammar.


#### Sourced from Different Sources

<!-- info: Is the dataset aggregated from different data sources? -->
<!-- scope: telescope -->
yes

#### Source Details

<!-- info: List the sources (one per line) -->
<!-- scope: periscope -->
Wikipedia


### Language Data

#### How was Language Data Obtained?

<!-- info: How was the language data obtained? -->
<!-- scope: telescope -->
`Found`

#### Where was it found?

<!-- info: If found, where from? -->
<!-- scope: telescope -->
`Single website`

#### Language Producers

<!-- info: What further information do we have on the language producers? -->
<!-- scope: microscope -->
The dataset uses language from Wikipedia: some demographic information is provided [here](https://en.wikipedia.org/wiki/Wikipedia:Who_writes_Wikipedia%3F).



#### Data Validation

<!-- info: Was the text validated by a different worker or a data curator? -->
<!-- scope: telescope -->
not validated

#### Was Data Filtered?

<!-- info: Were text instances selected or filtered? -->
<!-- scope: telescope -->
algorithmically

#### Filter Criteria

<!-- info: What were the selection criteria? -->
<!-- scope: microscope -->
The authors mention that they "extracted 138,095 article pairs from the 2019/09 Wikipedia dump using an improved version of the [WikiExtractor](https://github.com/attardi/wikiextractor) library". The [SpaCy](https://spacy.io/) library is used for sentence splitting.



### Structured Annotations

#### Additional Annotations?

<!-- quick -->
<!-- info: Does the dataset have additional annotations for each instance? -->
<!-- scope: telescope -->
crowd-sourced

#### Number of Raters

<!-- info: What is the number of raters -->
<!-- scope: telescope -->
11<n<50

#### Rater Qualifications

<!-- info: Describe the qualifications required of an annotator. -->
<!-- scope: periscope -->
WikiAuto (Figure Eight): No information provided.

ASSET (MTurk): 
- Having a HIT approval rate over 95%, and over 1000 HITs approved. No other demographic or compensation information is provided.
- Passing a Qualification Test (appropriately simplifying sentences). Out of 100 workers, 42 passed the test.
- Being a resident of the United States, United Kingdom or Canada.

TURK (MTurk): 
- Reference sentences were written by workers with HIT approval rate over 95%. No other demographic or compensation information is provided.

#### Raters per Training Example

<!-- info: How many annotators saw each training example? -->
<!-- scope: periscope -->
1

#### Raters per Test Example

<!-- info: How many annotators saw each test example? -->
<!-- scope: periscope -->
>5

#### Annotation Service?

<!-- info: Was an annotation service used? -->
<!-- scope: telescope -->
yes

#### Which Annotation Service

<!-- info: Which annotation services were used? -->
<!-- scope: periscope -->
`Amazon Mechanical Turk`, `Appen`

#### Annotation Values

<!-- info: Purpose and values for each annotation -->
<!-- scope: microscope -->
WikiAuto: Sentence alignment labels were crowdsourced for 500 randomly sampled document pairs (10,123 sentence pairs total). The authors pre-selected several alignment candidates from English Wikipedia for each Simple Wikipedia sentence based on various similarity metrics, then asked the crowd-workers to annotate these pairs. Finally, they trained their alignment model on this manually annotated dataset to obtain automatically aligned sentences (138,095 document pairs, 488,332 sentence pairs).
No demographic annotation is provided for the crowd workers. The [Figure Eight](https://www.figure-eight.com/) platform now part of Appen) was used for the annotation process.

ASSET: The instructions given to the annotators are available [here](https://github.com/facebookresearch/asset/blob/master/crowdsourcing/AMT_AnnotationInstructions.pdf).

TURK: The references are crowdsourced from Amazon Mechanical Turk. The annotators were asked to provide simplifications without losing any information or splitting the input sentence. No other demographic or compensation information is provided in the TURKCorpus paper. The instructions given to the annotators are available in the paper. 




#### Any Quality Control?

<!-- info: Quality control measures? -->
<!-- scope: telescope -->
none


### Consent

#### Any Consent Policy?

<!-- info: Was there a consent policy involved when gathering the data? -->
<!-- scope: telescope -->
yes

#### Consent Policy Details

<!-- info: What was the consent policy? -->
<!-- scope: microscope -->
Both Figure Eight and Amazon Mechanical Turk raters forfeit the right to their data as part of their agreements. 


### Private Identifying Information (PII)

#### Contains PII?

<!-- quick -->
<!-- info: Does the source language data likely contain Personal Identifying Information about the data creators or subjects? -->
<!-- scope: telescope -->
no PII

#### Justification for no PII

<!-- info: Provide a justification for selecting `no PII` above. -->
<!-- scope: periscope -->
Since the dataset is created from Wikipedia/Simple Wikipedia, all the information contained in the dataset is already in the public domain.



### Maintenance

#### Any Maintenance Plan?

<!-- info: Does the original dataset have a maintenance plan? -->
<!-- scope: telescope -->
no



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
The dataset may contain some social biases, as the input sentences are based on Wikipedia. Studies have shown that the English Wikipedia contains both gender biases [(Schmahl et al., 2020)](https://research.tudelft.nl/en/publications/is-wikipedia-succeeding-in-reducing-gender-bias-assessing-changes) and racial biases [(Adams et al., 2019)](https://journals.sagepub.com/doi/pdf/10.1177/2378023118823946).




## Considerations for Using the Data

### PII Risks and Liability

#### Potential PII Risk

<!-- info: Considering your answers to the PII part of the Data Curation Section, describe any potential privacy to the data subjects and creators risks when using the dataset. -->
<!-- scope: microscope -->
All the data is in the public domain.


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
The dataset may contain some social biases, as the input sentences are based on Wikipedia. Studies have shown that the English Wikipedia contains both gender biases [(Schmahl et al., 2020)](https://research.tudelft.nl/en/publications/is-wikipedia-succeeding-in-reducing-gender-bias-assessing-changes) and racial biases [(Adams et al., 2019)](https://journals.sagepub.com/doi/pdf/10.1177/2378023118823946).


#### Unsuited Applications

<!-- info: When using a model trained on this dataset in a setting where users or the public may interact with its predictions, what are some pitfalls to look out for? In particular, describe some applications of the general task featured in this dataset that its curation or properties make it less suitable for. -->
<!-- scope: microscope -->
Since the test datasets contains only 2,359 sentences that are derived from Wikipedia, they are limited to a small subset of topics present on Wikipedia.



