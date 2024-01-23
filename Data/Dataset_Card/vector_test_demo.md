---
annotaeators:
- found
language_creators:
- found
language:
- cn

---

### Dataset Summary 
Placeholder
You can load the dataset via:
```
import datasets
data = datasets.load_dataset('GEM/wiki_lingua')
```
The data loader can be found [here](https://huggingface.co/datasets/GEM/wiki_lingua).
#### website
None (See Repository)
#### paper
https://www.aclweb.org/anthology/2020.findings-emnlp.360/
#### authors
Faisal Ladhak (Columbia University), Esin Durmus (Stanford University), Claire Cardie (Cornell University), Kathleen McKeown (Columbia University)
## Dataset Overview
### Where to find the Data and its Documentation
#### Webpage
<!-- info: What is the webpage for the dataset (if it exists)? -->
<!-- scope: telescope -->
None (See Repository)
#### Download
<!-- info: What is the link to where the original dataset is hosted? -->
<!-- scope: telescope -->
https://github.com/esdurmus/Wikilingua
#### Paper
<!-- info: What is the link to the paper describing the dataset (open access preferred)? -->
<!-- scope: telescope -->
https://www.aclweb.org/anthology/2020.findings-emnlp.360/
#### BibTex
<!-- info: Provide the BibTex-formatted reference for the dataset. Please use the correct published version (ACL anthology, etc.) instead of google scholar created Bibtex. -->
<!-- scope: microscope -->
@inproceedings{ladhak-etal-2020-wikilingua,
    title = "{W}iki{L}ingua: A New Benchmark Dataset for Cross-Lingual Abstractive Summarization",
    author = "Ladhak, Faisal  and
      Durmus, Esin  and
      Cardie, Claire  and
      McKeown, Kathleen",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.findings-emnlp.360",
    doi = "10.18653/v1/2020.findings-emnlp.360",
    pages = "4034--4048",
    abstract = "We introduce WikiLingua, a large-scale, multilingual dataset for the evaluation of cross-lingual abstractive summarization systems. We extract article and summary pairs in 18 languages from WikiHow, a high quality, collaborative resource of how-to guides on a diverse set of topics written by human authors. We create gold-standard article-summary alignments across languages by aligning the images that are used to describe each how-to step in an article. As a set of baselines for further studies, we evaluate the performance of existing cross-lingual abstractive summarization methods on our dataset. We further propose a method for direct cross-lingual summarization (i.e., without requiring translation at inference time) by leveraging synthetic data and Neural Machine Translation as a pre-training step. Our method significantly outperforms the baseline approaches, while being more cost efficient during inference.",
}
#### Contact Name
<!-- quick -->
<!-- info: If known, provide the name of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
Faisal Ladhak, Esin Durmus
#### Contact Email
<!-- info: If known, provide the email of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
faisal@cs.columbia.edu, esdurmus@stanford.edu
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
#### Covered Dialects
<!-- info: What dialects are covered? Are there multiple dialects per language? -->
<!-- scope: periscope -->
Dataset does not have multiple dialects per language.
#### Covered Languages
<!-- quick -->
<!-- info: What languages/dialects are covered in the dataset? -->
<!-- scope: telescope -->
`English`, `Spanish, Castilian`, `Portuguese`, `French`, `German`, `Russian`, `Italian`, `Indonesian`, `Dutch, Flemish`, `Arabic`, `Chinese`, `Vietnamese`, `Thai`, `Japanese`, `Korean`, `Hindi`, `Czech`, `Turkish`
#### Whose Language?
<!-- info: Whose language is in the dataset? -->
<!-- scope: periscope -->
No information about the user demographic is available.
#### License
<!-- quick -->
<!-- info: What is the license of the dataset? -->
<!-- scope: telescope -->
cc-by-3.0: Creative Commons Attribution 3.0 Unported
#### Intended Use
<!-- info: What is the intended use of the dataset? -->
<!-- scope: microscope -->
The dataset was intended to serve as a large-scale, high-quality benchmark dataset for cross-lingual summarization.
#### Primary Task
<!-- info: What primary task does the dataset support? -->
<!-- scope: telescope -->
Summarization
#### Communicative Goal
<!-- quick -->
<!-- info: Provide a short description of the communicative goal of a model trained for this task on this dataset. -->
<!-- scope: periscope -->
Produce a high quality summary for the given input article.
### Credit
#### Curation Organization Type(s)
<!-- info: In what kind of organization did the dataset curation happen? -->
<!-- scope: telescope -->
`academic`
#### Curation Organization(s)
<!-- info: Name the organization(s). -->
<!-- scope: periscope -->
Columbia University
#### Dataset Creators
<!-- info: Who created the original dataset? List the people involved in collecting the dataset and their affiliation(s). -->
<!-- scope: microscope -->
Faisal Ladhak (Columbia University), Esin Durmus (Stanford University), Claire Cardie (Cornell University), Kathleen McKeown (Columbia University)
#### Who added the Dataset to GEM?
<!-- info: Who contributed to the data card and adding the dataset to GEM? List the people+affiliations involved in creating this data card and who helped integrate this dataset into GEM. -->
<!-- scope: microscope -->
Jenny Chim (Queen Mary University of London), Faisal Ladhak (Columbia University)
### Dataset Structure
#### Data Fields
<!-- info: List and describe the fields present in the dataset. -->
<!-- scope: telescope -->
gem_id -- The id for the data instance.
source_language -- The language of the source article.
target_language -- The language of the target summary.
source -- The source document.


#### Example Instance

<!-- info: Provide a JSON formatted example of a typical instance in the dataset. -->
<!-- scope: periscope -->
{
    "gem_id": "wikilingua_crosslingual-train-12345",
    "gem_parent_id": "wikilingua_crosslingual-train-12345",
    "source_language": "fr",
    "target_language": "de",
    "source": "Document in fr",
    "target": "Summary in de",
}
#### Data Splits

<!-- info: Describe and name the splits in the dataset if there are more than one. -->
<!-- scope: periscope -->
The data is split into train/dev/test. In addition to the full test set, there's also a sampled version of the test set. 

#### Splitting Criteria

<!-- info: Describe any criteria for splitting the data, if used. If there are differences between the splits (e.g., if the training annotations are machine-generated and the dev and test ones are created by humans, or if different numbers of annotators contributed to each example), describe them here. -->
<!-- scope: microscope -->
The data was split to ensure the same document would appear in the same split across languages so as to ensure there's no leakage into the test set.



## Dataset in GEM

### Rationale for Inclusion in GEM

#### Why is the Dataset in GEM?

<!-- info: What does this dataset contribute toward better generation evaluation and why is it part of GEM? -->
<!-- scope: microscope -->
This dataset provides a large-scale, high-quality resource for cross-lingual summarization in 18 languages, increasing the coverage of languages for the GEM summarization task. 

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
XSum covers English news articles, and MLSum covers news articles in German and Spanish. 
In contrast, this dataset has how-to articles in 18 languages, substantially increasing the languages covered. Moreover, it also provides a a different domain than the other two datasets.

#### Ability that the Dataset measures

<!-- info: What aspect of model ability can be measured with this dataset? -->
<!-- scope: periscope -->
The ability to generate quality summaries across multiple languages.


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
Previous version had separate data loaders for each language. In this version, we've created a single monolingual data loader, which contains monolingual data in each of the 18 languages. In addition, we've also created a single cross-lingual data loader across all the language pairs in the dataset.  

#### Additional Splits?

<!-- info: Does GEM provide additional splits to the dataset? -->
<!-- scope: telescope -->
no


### Getting Started with the Task




## Previous Results

### Previous Results

#### Measured Model Abilities

<!-- info: What aspect of model ability can be measured with this dataset? -->
<!-- scope: telescope -->
Ability to summarize content across different languages.

#### Metrics

<!-- info: What metrics are typically used for this task? -->
<!-- scope: periscope -->
`ROUGE`

#### Proposed Evaluation

<!-- info: List and describe the purpose of the metrics and evaluation methodology (including human evaluation) that the dataset creators used when introducing this task. -->
<!-- scope: microscope -->
ROUGE is used to measure content selection by comparing word overlap with reference summaries. In addition, the authors of the dataset also used human evaluation to evaluate content selection and fluency of the systems.

#### Previous results available?

<!-- info: Are previous results available? -->
<!-- scope: telescope -->
no



## Dataset Curation

### Original Curation

#### Original Curation Rationale

<!-- info: Original curation rationale -->
<!-- scope: telescope -->
The dataset was created in order to enable new approaches for cross-lingual and multilingual summarization, which are currently understudied as well as open up inetersting new directions for research in summarization. E.g., exploration of multi-source cross-lingual architectures, i.e. models that can summarize from multiple source languages into a target language, building models that can summarize articles from any language to any other language for a given set of languages.

#### Communicative Goal

<!-- info: What was the communicative goal? -->
<!-- scope: periscope -->
Given an input article, produce a high quality summary of the article in the target language.

#### Sourced from Different Sources

<!-- info: Is the dataset aggregated from different data sources? -->
<!-- scope: telescope -->
no


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
WikiHow, which is an online resource of how-to guides (written and reviewed by human authors) is used as the data source. 

#### Topics Covered

<!-- info: Does the language in the dataset focus on specific topics? How would you describe them? -->
<!-- scope: periscope -->
The articles cover 19 broad categories including health, arts and entertainment, personal care and style, travel, education and communications, etc. The categories cover a broad set of genres and topics.

#### Data Validation

<!-- info: Was the text validated by a different worker or a data curator? -->
<!-- scope: telescope -->
not validated

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
yes

#### Consent Policy Details

<!-- info: What was the consent policy? -->
<!-- scope: microscope -->
(1) Text Content. All text posted by Users to the Service is sub-licensed by wikiHow to other Users under a Creative Commons license as provided herein. The Creative Commons license allows such text content be used freely for non-commercial purposes, so long as it is used and attributed to the original author as specified under the terms of the license. Allowing free republication of our articles helps wikiHow achieve its mission by providing instruction on solving the problems of everyday life to more people for free. In order to support this goal, wikiHow hereby grants each User of the Service a license to all text content that Users contribute to the Service under the terms and conditions of a Creative Commons CC BY-NC-SA 3.0 License. Please be sure to read the terms of the license carefully. You continue to own all right, title, and interest in and to your User Content, and you are free to distribute it as you wish, whether for commercial or non-commercial purposes.

#### Other Consented Downstream Use

<!-- info: What other downstream uses of the data did the original data creators and the data curators consent to? -->
<!-- scope: microscope -->
The data is made freely available under the Creative Commons license, therefore there are no restrictions about downstream uses as long is it's for non-commercial purposes.


### Private Identifying Information (PII)

#### Contains PII?

<!-- quick -->
<!-- info: Does the source language data likely contain Personal Identifying Information about the data creators or subjects? -->
<!-- scope: telescope -->
no PII

#### Justification for no PII

<!-- info: Provide a justification for selecting `no PII` above. -->
<!-- scope: periscope -->
Only the article text and summaries were collected. No user information was retained in the dataset.


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
yes - other datasets featuring the same task


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



## Considerations for Using the Data

### PII Risks and Liability



### Licenses

#### Copyright Restrictions on the Dataset

<!-- info: Based on your answers in the Intended Use part of the Data Overview Section, which of the following best describe the copyright and licensing status of the dataset? -->
<!-- scope: periscope -->
`non-commercial use only`

#### Copyright Restrictions on the Language Data

<!-- info: Based on your answers in the Language part of the Data Curation Section, which of the following best describe the copyright and licensing status of the underlying language data? -->
<!-- scope: periscope -->
`non-commercial use only`


### Known Technical Limitations




