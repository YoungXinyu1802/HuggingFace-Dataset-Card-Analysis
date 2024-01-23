---
annotations_creators:
- none
language_creators:
- unknown
language:
- en
license:
- mit
multilinguality:
- unknown
size_categories:
- unknown
source_datasets:
- original
task_categories:
- table-to-text
task_ids: []
pretty_name: dart
tags:
- data-to-text
---

# Dataset Card for GEM/dart

## Dataset Description

- **Homepage:** n/a
- **Repository:** https://github.com/Yale-LILY/dart
- **Paper:** https://aclanthology.org/2021.naacl-main.37/
- **Leaderboard:** https://github.com/Yale-LILY/dart#leaderboard
- **Point of Contact:** Dragomir Radev, Rui Zhang, Nazneen Rajani

### Link to Main Data Card

You can find the main data card on the [GEM Website](https://gem-benchmark.com/data_cards/dart).

### Dataset Summary 

DART is an English dataset aggregating multiple other data-to-text dataset in a common triple-based format. The new format is completely flat, thus not requiring a model to learn hierarchical structures, while still retaining the full information. 

You can load the dataset via:
```
import datasets
data = datasets.load_dataset('GEM/dart')
```
The data loader can be found [here](https://huggingface.co/datasets/GEM/dart).

#### website
n/a

#### paper
[ACL Anthology](https://aclanthology.org/2021.naacl-main.37/)

#### authors
Linyong Nan, Dragomir Radev, Rui Zhang, Amrit Rau, Abhinand Sivaprasad, Chiachun Hsieh, Xiangru Tang, Aadit Vyas, Neha Verma, Pranav Krishna, Yangxiaokang Liu, Nadia Irwanto, Jessica Pan, Faiaz Rahman, Ahmad Zaidi, Mutethia Mutuma, Yasin Tarabar, Ankit Gupta, Tao Yu, Yi Chern Tan, Xi Victoria Lin, Caiming Xiong, Richard Socher, Nazneen Fatema Rajani

## Dataset Overview

### Where to find the Data and its Documentation

#### Download

<!-- info: What is the link to where the original dataset is hosted? -->
<!-- scope: telescope -->
[Github](https://github.com/Yale-LILY/dart)

#### Paper

<!-- info: What is the link to the paper describing the dataset (open access preferred)? -->
<!-- scope: telescope -->
[ACL Anthology](https://aclanthology.org/2021.naacl-main.37/)

#### BibTex

<!-- info: Provide the BibTex-formatted reference for the dataset. Please use the correct published version (ACL anthology, etc.) instead of google scholar created Bibtex. -->
<!-- scope: microscope -->
```
@inproceedings{nan-etal-2021-dart,
    title = "{DART}: Open-Domain Structured Data Record to Text Generation",
    author = "Nan, Linyong  and
      Radev, Dragomir  and
      Zhang, Rui  and
      Rau, Amrit  and
      Sivaprasad, Abhinand  and
      Hsieh, Chiachun  and
      Tang, Xiangru  and
      Vyas, Aadit  and
      Verma, Neha  and
      Krishna, Pranav  and
      Liu, Yangxiaokang  and
      Irwanto, Nadia  and
      Pan, Jessica  and
      Rahman, Faiaz  and
      Zaidi, Ahmad  and
      Mutuma, Mutethia  and
      Tarabar, Yasin  and
      Gupta, Ankit  and
      Yu, Tao  and
      Tan, Yi Chern  and
      Lin, Xi Victoria  and
      Xiong, Caiming  and
      Socher, Richard  and
      Rajani, Nazneen Fatema",
    booktitle = "Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies",
    month = jun,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.naacl-main.37",
    doi = "10.18653/v1/2021.naacl-main.37",
    pages = "432--447",
    abstract = "We present DART, an open domain structured DAta Record to Text generation dataset with over 82k instances (DARTs). Data-to-text annotations can be a costly process, especially when dealing with tables which are the major source of structured data and contain nontrivial structures. To this end, we propose a procedure of extracting semantic triples from tables that encodes their structures by exploiting the semantic dependencies among table headers and the table title. Our dataset construction framework effectively merged heterogeneous sources from open domain semantic parsing and spoken dialogue systems by utilizing techniques including tree ontology annotation, question-answer pair to declarative sentence conversion, and predicate unification, all with minimum post-editing. We present systematic evaluation on DART as well as new state-of-the-art results on WebNLG 2017 to show that DART (1) poses new challenges to existing data-to-text datasets and (2) facilitates out-of-domain generalization. Our data and code can be found at https://github.com/Yale-LILY/dart.",
}
```

#### Contact Name

<!-- quick -->
<!-- info: If known, provide the name of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
Dragomir Radev, Rui Zhang, Nazneen Rajani

#### Contact Email

<!-- info: If known, provide the email of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
{dragomir.radev, r.zhang}@yale.edu, {nazneen.rajani}@salesforce.com

#### Has a Leaderboard?

<!-- info: Does the dataset have an active leaderboard? -->
<!-- scope: telescope -->
yes

#### Leaderboard Link

<!-- info: Provide a link to the leaderboard. -->
<!-- scope: periscope -->
[Leaderboard](https://github.com/Yale-LILY/dart#leaderboard)

#### Leaderboard Details

<!-- info: Briefly describe how the leaderboard evaluates models. -->
<!-- scope: microscope -->
Several state-of-the-art table-to-text models were evaluated on DART, such as BART ([Lewis et al., 2020](https://arxiv.org/pdf/1910.13461.pdf)), Seq2Seq-Att ([MELBOURNE](https://webnlg-challenge.loria.fr/files/melbourne_report.pdf)) and End-to-End Transformer ([Castro Ferreira et al., 2019](https://arxiv.org/pdf/1908.09022.pdf)).
The leaderboard reports BLEU, METEOR, TER, MoverScore, BERTScore and BLEURT scores.


### Languages and Intended Use

#### Multilingual?

<!-- quick -->
<!-- info: Is the dataset multilingual? -->
<!-- scope: telescope -->
no

#### Covered Dialects

<!-- info: What dialects are covered? Are there multiple dialects per language? -->
<!-- scope: periscope -->
It is an aggregated from multiple other datasets that use general US-American or British English without differentiation between dialects. 

#### Covered Languages

<!-- quick -->
<!-- info: What languages/dialects are covered in the dataset? -->
<!-- scope: telescope -->
`English`

#### Whose Language?

<!-- info: Whose language is in the dataset? -->
<!-- scope: periscope -->
The dataset is aggregated from multiple others that were crowdsourced on different platforms. 

#### License

<!-- quick -->
<!-- info: What is the license of the dataset? -->
<!-- scope: telescope -->
mit: MIT License

#### Intended Use

<!-- info: What is the intended use of the dataset? -->
<!-- scope: microscope -->
The dataset is aimed to further research in natural language generation from semantic data.

#### Primary Task

<!-- info: What primary task does the dataset support? -->
<!-- scope: telescope -->
Data-to-Text

#### Communicative Goal

<!-- quick -->
<!-- info: Provide a short description of the communicative goal of a model trained for this task on this dataset. -->
<!-- scope: periscope -->
The speaker is required to produce coherent sentences and construct a trees structured ontology of the column headers.




### Credit

#### Curation Organization Type(s)

<!-- info: In what kind of organization did the dataset curation happen? -->
<!-- scope: telescope -->
`academic`, `industry`

#### Curation Organization(s)

<!-- info: Name the organization(s). -->
<!-- scope: periscope -->
Yale University, Salesforce Research, Penn State University, The University of Hong Kong, MIT

#### Dataset Creators

<!-- info: Who created the original dataset? List the people involved in collecting the dataset and their affiliation(s). -->
<!-- scope: microscope -->
Linyong Nan, Dragomir Radev, Rui Zhang, Amrit Rau, Abhinand Sivaprasad, Chiachun Hsieh, Xiangru Tang, Aadit Vyas, Neha Verma, Pranav Krishna, Yangxiaokang Liu, Nadia Irwanto, Jessica Pan, Faiaz Rahman, Ahmad Zaidi, Mutethia Mutuma, Yasin Tarabar, Ankit Gupta, Tao Yu, Yi Chern Tan, Xi Victoria Lin, Caiming Xiong, Richard Socher, Nazneen Fatema Rajani

#### Who added the Dataset to GEM?

<!-- info: Who contributed to the data card and adding the dataset to GEM? List the people+affiliations involved in creating this data card and who helped integrate this dataset into GEM. -->
<!-- scope: microscope -->
Miruna Clinciu contributed the original data card and Yacine Jernite wrote the initial data loader. Sebastian Gehrmann migrated the data card and the loader to the new format.


### Dataset Structure

#### Data Fields

<!-- info: List and describe the fields present in the dataset. -->
<!-- scope: telescope -->
-`tripleset`: a list of tuples, each tuple has 3 items
-`subtree_was_extended`: a boolean variable (true or false)
-`annotations`: a list of dict, each with source and text keys.
-`source`: a string mentioning the name of the source table.
-`text`: a sentence string.


#### Reason for Structure

<!-- info: How was the dataset structure determined? -->
<!-- scope: microscope -->
The structure is supposed to be able more complex structures beyond "flat" attribute-value pairs, instead encoding hierarchical relationships.

#### How were labels chosen?

<!-- info: How were the labels chosen? -->
<!-- scope: microscope -->
They are a combination of those from existing datasets and new annotations that take advantage of the hierarchical structure

#### Example Instance

<!-- info: Provide a JSON formatted example of a typical instance in the dataset. -->
<!-- scope: periscope -->
```
 {
    "tripleset": [
      [
        "Ben Mauk",
        "High school",
        "Kenton"
      ],
      [
        "Ben Mauk",
        "College",
        "Wake Forest Cincinnati"
      ]
    ],
    "subtree_was_extended": false,
    "annotations": [
      {
        "source": "WikiTableQuestions_lily",
        "text": "Ben Mauk, who attended Kenton High School, attended Wake Forest Cincinnati for college."
      }
    ]
  }
```

#### Data Splits

<!-- info: Describe and name the splits in the dataset if there are more than one. -->
<!-- scope: periscope -->
|Input Unit | Examples | Vocab Size | Words per SR | Sents per SR | Tables |
| ------------- | ------------- || ------------- || ------------- || ------------- || ------------- |
|Triple Set | 82,191 | 33.2K | 21.6 | 1.5 | 5,623 |

| Train | Dev | Test|
| ------------- | ------------- || ------------- |
| 62,659 | 6,980 | 12,552|


Statistics of DART decomposed by different collection methods. DART exhibits a great deal of topical variety in terms of the number of unique predicates, the number of unique triples, and the vocabulary size. These statistics are computed from DART v1.1.1; the number of unique predicates reported is post-unification (see Section 3.4). SR: Surface Realization.
([details in Table 1 and 2](https://arxiv.org/pdf/2007.02871.pdf)).


#### Splitting Criteria

<!-- info: Describe any criteria for splitting the data, if used. If there are differences between the splits (e.g., if the training annotations are machine-generated and the dev and test ones are created by humans, or if different numbers of annotators contributed to each example), describe them here. -->
<!-- scope: microscope -->
For WebNLG 2017 and Cleaned E2E,  DART use the original data splits. For the new annotation on WikiTableQuestions and WikiSQL, random splitting will make train, dev, and test splits contain similar tables and similar <triple-set, sentence> examples. They are thus split based on Jaccard similarity such that no training examples has a similarity with a test example of over 0.5



## Dataset in GEM

### Rationale for Inclusion in GEM

#### Why is the Dataset in GEM?

<!-- info: What does this dataset contribute toward better generation evaluation and why is it part of GEM? -->
<!-- scope: microscope -->
DART is a large and open-domain structured DAta Record to Text generation corpus with high-quality sentence annotations with each input being a set of entity-relation triples following a tree-structured ontology. 

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
The tree structure is unique among GEM datasets

#### Ability that the Dataset measures

<!-- info: What aspect of model ability can be measured with this dataset? -->
<!-- scope: periscope -->
Reasoning, surface realization


### GEM-Specific Curation

#### Modificatied for GEM?

<!-- info: Has the GEM version of the dataset been modified in any way (data, processing, splits) from the original curated data? -->
<!-- scope: telescope -->
no

#### Additional Splits?

<!-- info: Does GEM provide additional splits to the dataset? -->
<!-- scope: telescope -->
no


### Getting Started with the Task

#### Pointers to Resources

<!-- info: Getting started with in-depth research on the task. Add relevant pointers to resources that researchers can consult when they want to get started digging deeper into the task. -->
<!-- scope: microscope -->
Experimental results on DART shows that BART model as the highest performance among three models with a BLEU score of 37.06. This is attributed to BART’s generalization ability due to pretraining ([Table 4](https://arxiv.org/pdf/2007.02871.pdf)).




## Previous Results

### Previous Results

#### Measured Model Abilities

<!-- info: What aspect of model ability can be measured with this dataset? -->
<!-- scope: telescope -->
Reasoning, surface realization

#### Metrics

<!-- info: What metrics are typically used for this task? -->
<!-- scope: periscope -->
`BLEU`, `MoverScore`, `BERT-Score`, `BLEURT`

#### Proposed Evaluation

<!-- info: List and describe the purpose of the metrics and evaluation methodology (including human evaluation) that the dataset creators used when introducing this task. -->
<!-- scope: microscope -->
The leaderboard uses the combination of BLEU, METEOR, TER, MoverScore, BERTScore, PARENT and BLEURT to overcome the limitations of the n-gram overlap metrics.  
A small scale human annotation of 100 data points was conducted along the dimensions of  (1) fluency - a sentence is natural and grammatical, and (2) semantic faithfulness - a sentence is supported by the input triples.

#### Previous results available?

<!-- info: Are previous results available? -->
<!-- scope: telescope -->
yes

#### Other Evaluation Approaches

<!-- info: What evaluation approaches have others used? -->
<!-- scope: periscope -->
n/a 

#### Relevant Previous Results

<!-- info: What are the most relevant previous results for this task/dataset? -->
<!-- scope: microscope -->
BART currently achieves the best performance according to the leaderboard.



## Dataset Curation

### Original Curation

#### Original Curation Rationale

<!-- info: Original curation rationale -->
<!-- scope: telescope -->
The dataset creators encourage through DART further research in natural language generation from semantic data. DART provides high-quality sentence annotations with each input being a set of entity-relation triples in a tree structure.



#### Communicative Goal

<!-- info: What was the communicative goal? -->
<!-- scope: periscope -->
The speaker is required to produce coherent sentences and construct a trees structured ontology of the column headers.



#### Sourced from Different Sources

<!-- info: Is the dataset aggregated from different data sources? -->
<!-- scope: telescope -->
yes

#### Source Details

<!-- info: List the sources (one per line) -->
<!-- scope: periscope -->
- human annotation on open-domain Wikipedia tables from WikiTableQuestions ([Pasupat and Liang,
2015](https://www.aclweb.org/anthology/P15-1142.pdf)) and WikiSQL ([Zhong et al., 2017](https://arxiv.org/pdf/1709.00103.pdf))
- automatic conversion of questions in WikiSQL to declarative sentences
- incorporation of existing datasets including WebNLG 2017 (Gardent et al., 2017[a](https://www.aclweb.org/anthology/P17-1017.pdf),[b](https://www.aclweb.org/anthology/W17-3518.pdf); [Shimorina and Gardent, 2018](https://www.aclweb.org/anthology/W18-6543.pdf)) and Cleaned E2E ([Novikova et al., 2017b](https://arxiv.org/pdf/1706.09254.pdf); Dušek et al., [2018](https://arxiv.org/pdf/1810.01170.pdf), [2019](https://www.aclweb.org/anthology/W19-8652.pdf))



### Language Data

#### How was Language Data Obtained?

<!-- info: How was the language data obtained? -->
<!-- scope: telescope -->
`Found`, `Created for the dataset`

#### Where was it found?

<!-- info: If found, where from? -->
<!-- scope: telescope -->
`Offline media collection`

#### Creation Process

<!-- info: If created for the dataset, describe the creation process. -->
<!-- scope: microscope -->
Creators proposed a two-stage annotation process for constructing triple set sentence pairs based on a tree-structured ontology of each table. First, internal skilled annotators denote the parent column for each column header. Then, a larger number of annotators provide a sentential description of an automatically-chosen subset of table cells in a row. To form a triple set sentence pair, the highlighted cells can be converted to a connected triple set automatically according to the column ontology for the given table.



#### Language Producers

<!-- info: What further information do we have on the language producers? -->
<!-- scope: microscope -->
No further information about the MTurk workers has been provided.



#### Topics Covered

<!-- info: Does the language in the dataset focus on specific topics? How would you describe them? -->
<!-- scope: periscope -->
The sub-datasets are from Wikipedia, DBPedia, and artificially created restaurant data. 

#### Data Validation

<!-- info: Was the text validated by a different worker or a data curator? -->
<!-- scope: telescope -->
validated by crowdworker

#### Was Data Filtered?

<!-- info: Were text instances selected or filtered? -->
<!-- scope: telescope -->
not filtered


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
no

#### Justification for Using the Data

<!-- info: If not, what is the justification for reusing the data? -->
<!-- scope: microscope -->
The new annotations are based on Wikipedia which is in the public domain and the other two datasets permit reuse (with attribution)


### Private Identifying Information (PII)

#### Contains PII?

<!-- quick -->
<!-- info: Does the source language data likely contain Personal Identifying Information about the data creators or subjects? -->
<!-- scope: telescope -->
no PII

#### Justification for no PII

<!-- info: Provide a justification for selecting `no PII` above. -->
<!-- scope: periscope -->
None of the datasets talk about individuals


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
no

#### Are the Language Producers Representative of the Language?

<!-- info: Does the distribution of language producers in the dataset accurately represent the full distribution of speakers of the language world-wide? If not, how does it differ? -->
<!-- scope: periscope -->
No, the annotators are raters on crowdworking platforms and thus only represent their demographics.



## Considerations for Using the Data

### PII Risks and Liability



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
The dataset may contain some social biases, as the input sentences are based on Wikipedia (WikiTableQuestions, WikiSQL, WebNLG). Studies have shown that the English Wikipedia contains gender biases([Dinan et al., 2020](https://www.aclweb.org/anthology/2020.emnlp-main.23.pdf)), racial biases([Papakyriakopoulos et al., 2020 (https://dl.acm.org/doi/pdf/10.1145/3351095.3372843)) and geographical bias([Livingstone et al., 2010](https://doi.org/10.5204/mcj.315)). [More info](https://en.wikipedia.org/wiki/Racial_bias_on_Wikipedia#cite_note-23).


#### Unsuited Applications

<!-- info: When using a model trained on this dataset in a setting where users or the public may interact with its predictions, what are some pitfalls to look out for? In particular, describe some applications of the general task featured in this dataset that its curation or properties make it less suitable for. -->
<!-- scope: microscope -->
The end-to-end transformer has the lowest performance since the transformer model needs intermediate pipeline planning steps to have higher performance. Similar findings can be found in [Castro Ferreira et al., 2019](https://arxiv.org/pdf/1908.09022.pdf).



