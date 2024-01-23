---
annotations_creators:
- automatically-created
language_creators:
- unknown
language:
- en
- de
license:
- cc-by-4.0
multilinguality:
- unknown
size_categories:
- unknown
source_datasets:
- original
task_categories:
- table-to-text
task_ids: []
pretty_name: RotoWire_English-German
tags:
- data-to-text
---

# Dataset Card for GEM/RotoWire_English-German

## Dataset Description

- **Homepage:** https://sites.google.com/view/wngt19/dgt-task
- **Repository:** https://github.com/neulab/dgt
- **Paper:** https://www.aclweb.org/anthology/D19-5601/
- **Leaderboard:** N/A
- **Point of Contact:** Hiroaki Hayashi

### Link to Main Data Card

You can find the main data card on the [GEM Website](https://gem-benchmark.com/data_cards/RotoWire_English-German).

### Dataset Summary 

This dataset is a data-to-text dataset in the basketball domain. The input are tables in a fixed format with statistics about a game (in English) and the target is a German translation of the originally English description. The translations were done by professional translators with basketball experience. The dataset can be used to evaluate the cross-lingual data-to-text capabilities of a model with complex inputs. 

You can load the dataset via:
```
import datasets
data = datasets.load_dataset('GEM/RotoWire_English-German')
```
The data loader can be found [here](https://huggingface.co/datasets/GEM/RotoWire_English-German).

#### website
[Website](https://sites.google.com/view/wngt19/dgt-task)

#### paper
[ACL Anthology](https://www.aclweb.org/anthology/D19-5601/)

#### authors
Graham Neubig (Carnegie Mellon University), Hiroaki Hayashi (Carnegie Mellon University)

## Dataset Overview

### Where to find the Data and its Documentation

#### Webpage

<!-- info: What is the webpage for the dataset (if it exists)? -->
<!-- scope: telescope -->
[Website](https://sites.google.com/view/wngt19/dgt-task)

#### Download

<!-- info: What is the link to where the original dataset is hosted? -->
<!-- scope: telescope -->
[Github](https://github.com/neulab/dgt)

#### Paper

<!-- info: What is the link to the paper describing the dataset (open access preferred)? -->
<!-- scope: telescope -->
[ACL Anthology](https://www.aclweb.org/anthology/D19-5601/)

#### BibTex

<!-- info: Provide the BibTex-formatted reference for the dataset. Please use the correct published version (ACL anthology, etc.) instead of google scholar created Bibtex. -->
<!-- scope: microscope -->
```
@inproceedings{hayashi-etal-2019-findings,
    title = "Findings of the Third Workshop on Neural Generation and Translation",
    author = "Hayashi, Hiroaki  and
      Oda, Yusuke  and
      Birch, Alexandra  and
      Konstas, Ioannis  and
      Finch, Andrew  and
      Luong, Minh-Thang  and
      Neubig, Graham  and
      Sudoh, Katsuhito",
    booktitle = "Proceedings of the 3rd Workshop on Neural Generation and Translation",
    month = nov,
    year = "2019",
    address = "Hong Kong",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/D19-5601",
    doi = "10.18653/v1/D19-5601",
    pages = "1--14",
    abstract = "This document describes the findings of the Third Workshop on Neural Generation and Translation, held in concert with the annual conference of the Empirical Methods in Natural Language Processing (EMNLP 2019). First, we summarize the research trends of papers presented in the proceedings. Second, we describe the results of the two shared tasks 1) efficient neural machine translation (NMT) where participants were tasked with creating NMT systems that are both accurate and efficient, and 2) document generation and translation (DGT) where participants were tasked with developing systems that generate summaries from structured data, potentially with assistance from text in another language.",
}
```

#### Contact Name

<!-- quick -->
<!-- info: If known, provide the name of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
Hiroaki Hayashi

#### Contact Email

<!-- info: If known, provide the email of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
hiroakih@andrew.cmu.edu

#### Has a Leaderboard?

<!-- info: Does the dataset have an active leaderboard? -->
<!-- scope: telescope -->
no


### Languages and Intended Use

#### Multilingual?

<!-- quick -->
<!-- info: Is the dataset multilingual? -->
<!-- scope: telescope -->
yes

#### Covered Languages

<!-- quick -->
<!-- info: What languages/dialects are covered in the dataset? -->
<!-- scope: telescope -->
`English`, `German`

#### License

<!-- quick -->
<!-- info: What is the license of the dataset? -->
<!-- scope: telescope -->
cc-by-4.0: Creative Commons Attribution 4.0 International

#### Intended Use

<!-- info: What is the intended use of the dataset? -->
<!-- scope: microscope -->
Foster the research on document-level generation technology and contrast the methods for different types of inputs.

#### Primary Task

<!-- info: What primary task does the dataset support? -->
<!-- scope: telescope -->
Data-to-Text

#### Communicative Goal

<!-- quick -->
<!-- info: Provide a short description of the communicative goal of a model trained for this task on this dataset. -->
<!-- scope: periscope -->
Describe a basketball game given its box score table (and possibly a summary in a foreign language).


### Credit

#### Curation Organization Type(s)

<!-- info: In what kind of organization did the dataset curation happen? -->
<!-- scope: telescope -->
`academic`

#### Curation Organization(s)

<!-- info: Name the organization(s). -->
<!-- scope: periscope -->
Carnegie Mellon University

#### Dataset Creators

<!-- info: Who created the original dataset? List the people involved in collecting the dataset and their affiliation(s). -->
<!-- scope: microscope -->
Graham Neubig (Carnegie Mellon University), Hiroaki Hayashi (Carnegie Mellon University)

#### Funding

<!-- info: Who funded the data creation? -->
<!-- scope: microscope -->
Graham Neubig

#### Who added the Dataset to GEM?

<!-- info: Who contributed to the data card and adding the dataset to GEM? List the people+affiliations involved in creating this data card and who helped integrate this dataset into GEM. -->
<!-- scope: microscope -->
Hiroaki Hayashi (Carnegie Mellon University)


### Dataset Structure

#### Data Fields

<!-- info: List and describe the fields present in the dataset. -->
<!-- scope: telescope -->
- `id` (`string`): The identifier from the original dataset.
- `gem_id` (`string`): The identifier from GEMv2.
- `day` (`string`): Date of the game (Format: `MM_DD_YY`)
- `home_name` (`string`): Home team name.
- `home_city` (`string`): Home team city name.
- `vis_name` (`string`): Visiting (Away) team name.
- `vis_city` (`string`): Visiting team (Away) city name.
- `home_line` (`Dict[str, str]`): Home team statistics (e.g., team free throw percentage).
- `vis_line` (`Dict[str, str]`): Visiting team statistics (e.g., team free throw percentage).
- `box_score` (`Dict[str, Dict[str, str]]`): Box score table. (Stat_name to [player ID to stat_value].)
- `summary_en` (`List[string]`): Tokenized target summary in English.
- `sentence_end_index_en` (`List[int]`): Sentence end indices for `summary_en`.
- `summary_de` (`List[string]`): Tokenized target summary in German.
- `sentence_end_index_de` (`List[int]`): ): Sentence end indices for `summary_de`.
- (Unused) `detok_summary_org` (`string`): Original summary provided by RotoWire dataset.
- (Unused) `summary` (`List[string]`): Tokenized summary of `detok_summary_org`.
- (Unused) `detok_summary` (`string`): Detokenized (with organizer's detokenizer) summary of `summary`.


#### Reason for Structure

<!-- info: How was the dataset structure determined? -->
<!-- scope: microscope -->
- Structured data are directly imported from the original RotoWire dataset.
- Textual data (English, German) are associated to each sample.

#### Example Instance

<!-- info: Provide a JSON formatted example of a typical instance in the dataset. -->
<!-- scope: periscope -->
```
{
  'id': '11_02_16-Jazz-Mavericks-TheUtahJazzdefeatedthe',
  'gem_id': 'GEM-RotoWire_English-German-train-0'
  'day': '11_02_16',
  'home_city': 'Utah',
  'home_name': 'Jazz',
  'vis_city': 'Dallas',
  'vis_name': 'Mavericks',
  'home_line': {
    'TEAM-FT_PCT': '58', ...
  },
  'vis_line': {
    'TEAM-FT_PCT': '80', ...
  },
  'box_score': {
    'PLAYER_NAME': {
      '0': 'Harrison Barnes', ...
  }, ...
  'summary_en': ['The', 'Utah', 'Jazz', 'defeated', 'the', 'Dallas', 'Mavericks', ...],
  'sentence_end_index_en': [16, 52, 100, 137, 177, 215, 241, 256, 288],
  'summary_de': ['Die', 'Utah', 'Jazz', 'besiegten', 'am', 'Mittwoch', 'in', 'der', ...],
  'sentence_end_index_de': [19, 57, 107, 134, 170, 203, 229, 239, 266],
  'detok_summary_org': "The Utah Jazz defeated the Dallas Mavericks 97 - 81 ...",
  'detok_summary': "The Utah Jazz defeated the Dallas Mavericks 97-81 ...",
  'summary': ['The', 'Utah', 'Jazz', 'defeated', 'the', 'Dallas', 'Mavericks', ...],
}
```

#### Data Splits

<!-- info: Describe and name the splits in the dataset if there are more than one. -->
<!-- scope: periscope -->
- Train
- Validation
- Test

#### Splitting Criteria

<!-- info: Describe any criteria for splitting the data, if used. If there are differences between the splits (e.g., if the training annotations are machine-generated and the dev and test ones are created by humans, or if different numbers of annotators contributed to each example), describe them here. -->
<!-- scope: microscope -->
- English summaries are provided sentence-by-sentence to professional German translators with basketball knowledge to obtain sentence-level German translations.
- Split criteria follows the original RotoWire dataset.

#### 

<!-- info: What does an outlier of the dataset in terms of length/perplexity/embedding look like? -->
<!-- scope: microscope -->
- The (English) summary length in the training set varies from 145 to 650 words, with an average of 323 words.



## Dataset in GEM

### Rationale for Inclusion in GEM

#### Why is the Dataset in GEM?

<!-- info: What does this dataset contribute toward better generation evaluation and why is it part of GEM? -->
<!-- scope: microscope -->
The use of two modalities (data, foreign text) to generate a document-level text summary.

#### Similar Datasets

<!-- info: Do other datasets for the high level task exist? -->
<!-- scope: telescope -->
yes

#### Unique Language Coverage

<!-- info: Does this dataset cover other languages than other datasets for the same task? -->
<!-- scope: periscope -->
yes

#### Difference from other GEM datasets

<!-- info: What else sets this dataset apart from other similar datasets in GEM? -->
<!-- scope: microscope -->
The potential use of two modalities (data, foreign text) as input.

#### Ability that the Dataset measures

<!-- info: What aspect of model ability can be measured with this dataset? -->
<!-- scope: periscope -->
- Translation
- Data-to-text verbalization
- Aggregation of the two above.


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
- Added GEM ID in each sample.
- Normalize the number of players in each sample with "N/A" for consistent data loading.

#### Additional Splits?

<!-- info: Does GEM provide additional splits to the dataset? -->
<!-- scope: telescope -->
no


### Getting Started with the Task

#### Pointers to Resources

<!-- info: Getting started with in-depth research on the task. Add relevant pointers to resources that researchers can consult when they want to get started digging deeper into the task. -->
<!-- scope: microscope -->
- [Challenges in Data-to-Document Generation](https://aclanthology.org/D17-1239)
- [Data-to-Text Generation with Content Selection and Planning](https://ojs.aaai.org//index.php/AAAI/article/view/4668)
- [Findings of the Third Workshop on Neural Generation and Translation](https://aclanthology.org/D19-5601)

#### Technical Terms

<!-- info: Technical terms used in this card and the dataset and their definitions -->
<!-- scope: microscope -->
- Data-to-text
- Neural machine translation (NMT)
- Document-level generation and translation (DGT) 



## Previous Results

### Previous Results

#### Measured Model Abilities

<!-- info: What aspect of model ability can be measured with this dataset? -->
<!-- scope: telescope -->
- Textual accuracy towards the gold-standard summary.
- Content faithfulness to the input structured data.

#### Metrics

<!-- info: What metrics are typically used for this task? -->
<!-- scope: periscope -->
`BLEU`, `ROUGE`, `Other: Other Metrics`

#### Other Metrics

<!-- info: Definitions of other metrics -->
<!-- scope: periscope -->
Model-based measures proposed by (Wiseman et al., 2017):
- Relation Generation
- Content Selection
- Content Ordering

#### Proposed Evaluation

<!-- info: List and describe the purpose of the metrics and evaluation methodology (including human evaluation) that the dataset creators used when introducing this task. -->
<!-- scope: microscope -->
To evaluate the fidelity of the generated content to the input data.

#### Previous results available?

<!-- info: Are previous results available? -->
<!-- scope: telescope -->
yes

#### Other Evaluation Approaches

<!-- info: What evaluation approaches have others used? -->
<!-- scope: periscope -->
N/A.

#### Relevant Previous Results

<!-- info: What are the most relevant previous results for this task/dataset? -->
<!-- scope: microscope -->
See Table 2 to 7 of (https://aclanthology.org/D19-5601) for previous results for this dataset.



## Dataset Curation

### Original Curation

#### Original Curation Rationale

<!-- info: Original curation rationale -->
<!-- scope: telescope -->
A random subset of RotoWire dataset was chosen for German translation annotation.

#### Communicative Goal

<!-- info: What was the communicative goal? -->
<!-- scope: periscope -->
Foster the research on document-level generation technology and contrast the methods for different types of inputs.

#### Sourced from Different Sources

<!-- info: Is the dataset aggregated from different data sources? -->
<!-- scope: telescope -->
yes

#### Source Details

<!-- info: List the sources (one per line) -->
<!-- scope: periscope -->
RotoWire


### Language Data

#### How was Language Data Obtained?

<!-- info: How was the language data obtained? -->
<!-- scope: telescope -->
`Created for the dataset`

#### Creation Process

<!-- info: If created for the dataset, describe the creation process. -->
<!-- scope: microscope -->
Professional German language translators were hired to translate basketball summaries from a subset of RotoWire dataset.

#### Language Producers

<!-- info: What further information do we have on the language producers? -->
<!-- scope: microscope -->
Translators are familiar with basketball terminology.

#### Topics Covered

<!-- info: Does the language in the dataset focus on specific topics? How would you describe them? -->
<!-- scope: periscope -->
Basketball (NBA) game summaries.

#### Data Validation

<!-- info: Was the text validated by a different worker or a data curator? -->
<!-- scope: telescope -->
validated by data curator

#### Data Preprocessing

<!-- info: How was the text data pre-processed? (Enter N/A if the text was not pre-processed) -->
<!-- scope: microscope -->
Sentence-level translations were aligned back to the original English summary sentences.

#### Was Data Filtered?

<!-- info: Were text instances selected or filtered? -->
<!-- scope: telescope -->
not filtered


### Structured Annotations

#### Additional Annotations?

<!-- quick -->
<!-- info: Does the dataset have additional annotations for each instance? -->
<!-- scope: telescope -->
automatically created

#### Annotation Service?

<!-- info: Was an annotation service used? -->
<!-- scope: telescope -->
no

#### Annotation Values

<!-- info: Purpose and values for each annotation -->
<!-- scope: microscope -->
Sentence-end indices for the tokenized summaries. Sentence boundaries can help users accurately identify aligned sentences in both languages, as well as allowing an accurate evaluation that involves sentence boundaries (ROUGE-L).

#### Any Quality Control?

<!-- info: Quality control measures? -->
<!-- scope: telescope -->
validated through automated script

#### Quality Control Details

<!-- info: Describe the quality control measures that were taken. -->
<!-- scope: microscope -->
Token and number overlaps between pairs of aligned sentences are measured.


### Consent

#### Any Consent Policy?

<!-- info: Was there a consent policy involved when gathering the data? -->
<!-- scope: telescope -->
no

#### Justification for Using the Data

<!-- info: If not, what is the justification for reusing the data? -->
<!-- scope: microscope -->
Reusing by citing the original papers:
- Sam Wiseman, Stuart M. Shieber, Alexander M. Rush:
Challenges in Data-to-Document Generation. EMNLP 2017.
- Hiroaki Hayashi, Yusuke Oda, Alexandra Birch, Ioannis Konstas, Andrew Finch, Minh-Thang Luong, Graham Neubig, Katsuhito Sudoh. Findings of the Third Workshop on Neural Generation and Translation. WNGT 2019.


### Private Identifying Information (PII)

#### Contains PII?

<!-- quick -->
<!-- info: Does the source language data likely contain Personal Identifying Information about the data creators or subjects? -->
<!-- scope: telescope -->
unlikely

#### Categories of PII

<!-- info: What categories of PII are present or suspected in the data? -->
<!-- scope: periscope -->
`generic PII`

#### Any PII Identification?

<!-- info: Did the curators use any automatic/manual method to identify PII in the dataset? -->
<!-- scope: periscope -->
no identification


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
- English text in this dataset is from Rotowire, originally written by writers at Rotowire.com that are likely US-based.
- German text is produced by professional translators proficient in both English and German.



## Considerations for Using the Data

### PII Risks and Liability

#### Potential PII Risk

<!-- info: Considering your answers to the PII part of the Data Curation Section, describe any potential privacy to the data subjects and creators risks when using the dataset. -->
<!-- scope: microscope -->
- Structured data contain real National Basketball Association player and organization names.


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
Potential overlap of box score tables between splits. This was extensively studied and pointed out by [1].

[1]: Thomson, Craig, Ehud Reiter, and Somayajulu Sripada. "SportSett: Basketball-A robust and maintainable data-set for Natural Language Generation." Proceedings of the Workshop on Intelligent Information Processing and Natural Language Generation. 2020.

#### Unsuited Applications

<!-- info: When using a model trained on this dataset in a setting where users or the public may interact with its predictions, what are some pitfalls to look out for? In particular, describe some applications of the general task featured in this dataset that its curation or properties make it less suitable for. -->
<!-- scope: microscope -->
Users may interact with a trained model to learn about a NBA game in a textual manner. On generated texts, they may observe factual errors that contradicts the actual data that the model conditions on.
Factual errors include wrong statistics of a player (e.g., 3PT), non-existent injury information.

#### Discouraged Use Cases

<!-- info: What are some discouraged use cases of a model trained to maximize the proposed metrics on this dataset? In particular, think about settings where decisions made by a model that performs reasonably well on the metric my still have strong negative consequences for user or members of the public. -->
<!-- scope: microscope -->
Publishing the generated text as is. Even if the model achieves high scores on the evaluation metrics, there is a risk of factual errors mentioned above.


