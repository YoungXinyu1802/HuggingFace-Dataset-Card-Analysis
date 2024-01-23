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
- other
task_ids: []
pretty_name: common_gen
tags:
- reasoning
---

# Dataset Card for GEM/common_gen

## Dataset Description

- **Homepage:** https://inklab.usc.edu/CommonGen/
- **Repository:** https://github.com/INK-USC/CommonGen
- **Paper:** https://aclanthology.org/2020.findings-emnlp.165
- **Leaderboard:** https://inklab.usc.edu/CommonGen/leaderboard.html
- **Point of Contact:** Bill Yuchen Lin

### Link to Main Data Card

You can find the main data card on the [GEM Website](https://gem-benchmark.com/data_cards/common_gen).

### Dataset Summary 

CommonGen is an English text generation task to explicitly test machines for the ability of generative commonsense reasoning. Given a set of common concepts, the task is to generate a coherent sentence describing an everyday scenario using these concepts. CommonGen is challenging because it inherently requires 1) relational reasoning using background commonsense knowledge, and 2) compositional generalization ability to work on unseen concept combinations. The dataset, constructed through a combination of crowd-sourcing from AMT and existing caption corpora, consists of 30k concept-sets and 50k sentences in total. Note that the CommonGen test set is private and requires submission to the external leaderboard.

You can load the dataset via:
```
import datasets
data = datasets.load_dataset('GEM/common_gen')
```
The data loader can be found [here](https://huggingface.co/datasets/GEM/common_gen).

#### website
[link](https://inklab.usc.edu/CommonGen/)

#### paper
[Link](https://aclanthology.org/2020.findings-emnlp.165)

#### authors
Bill Yuchen Lin (USC), Wangchunshu Zhou (USC), Ming Shen (USC), Pei Zhou (USC), Chandra Bhagavatula (AllenAI), Yejin Choi (AllenAI + UW), Xiang Ren (USC)

## Dataset Overview

### Where to find the Data and its Documentation

#### Webpage

<!-- info: What is the webpage for the dataset (if it exists)? -->
<!-- scope: telescope -->
[link](https://inklab.usc.edu/CommonGen/)

#### Download

<!-- info: What is the link to where the original dataset is hosted? -->
<!-- scope: telescope -->
[Link](https://github.com/INK-USC/CommonGen)

#### Paper

<!-- info: What is the link to the paper describing the dataset (open access preferred)? -->
<!-- scope: telescope -->
[Link](https://aclanthology.org/2020.findings-emnlp.165)

#### BibTex

<!-- info: Provide the BibTex-formatted reference for the dataset. Please use the correct published version (ACL anthology, etc.) instead of google scholar created Bibtex. -->
<!-- scope: microscope -->
```
@inproceedings{lin-etal-2020-commongen,
    title = "{C}ommon{G}en: A Constrained Text Generation Challenge for Generative Commonsense Reasoning",
    author = "Lin, Bill Yuchen  and
      Zhou, Wangchunshu  and
      Shen, Ming  and
      Zhou, Pei  and
      Bhagavatula, Chandra  and
      Choi, Yejin  and
      Ren, Xiang",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.findings-emnlp.165",
    pages = "1823--1840",
}
```

#### Contact Name

<!-- quick -->
<!-- info: If known, provide the name of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
Bill Yuchen Lin

#### Contact Email

<!-- info: If known, provide the email of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
yuchen.lin@usc.edu

#### Has a Leaderboard?

<!-- info: Does the dataset have an active leaderboard? -->
<!-- scope: telescope -->
yes

#### Leaderboard Link

<!-- info: Provide a link to the leaderboard. -->
<!-- scope: periscope -->
[Link](https://inklab.usc.edu/CommonGen/leaderboard.html)

#### Leaderboard Details

<!-- info: Briefly describe how the leaderboard evaluates models. -->
<!-- scope: microscope -->
The model outputs are evaluated against the crowdsourced references, and ranked by SPICE score. The leaderboard also reports BLEU-4 and CIDEr scores.


### Languages and Intended Use

#### Multilingual?

<!-- quick -->
<!-- info: Is the dataset multilingual? -->
<!-- scope: telescope -->
no

#### Covered Dialects

<!-- info: What dialects are covered? Are there multiple dialects per language? -->
<!-- scope: periscope -->
No information is provided on regional restrictions and we thus assume that the covered dialects are those spoken by raters on Mechanical Turk. 

#### Covered Languages

<!-- quick -->
<!-- info: What languages/dialects are covered in the dataset? -->
<!-- scope: telescope -->
`English`

#### Whose Language?

<!-- info: Whose language is in the dataset? -->
<!-- scope: periscope -->
The concepts were extracted from multiple English image captioning datasets and the data was collected via Amazon Mechanical Turk. No information on regional restrictions is provided. 

#### License

<!-- quick -->
<!-- info: What is the license of the dataset? -->
<!-- scope: telescope -->
mit: MIT License

#### Intended Use

<!-- info: What is the intended use of the dataset? -->
<!-- scope: microscope -->
CommonGen is a constrained text generation task, associated with a benchmark dataset, to explicitly test machines for the ability of generative commonsense reasoning. 

#### Primary Task

<!-- info: What primary task does the dataset support? -->
<!-- scope: telescope -->
Reasoning

#### Communicative Goal

<!-- quick -->
<!-- info: Provide a short description of the communicative goal of a model trained for this task on this dataset. -->
<!-- scope: periscope -->
The speaker is required to produce a *coherent* sentence which mentions all of the source concepts, and which describes a *likely* situation that could be captured in a picture or video.



### Credit

#### Curation Organization Type(s)

<!-- info: In what kind of organization did the dataset curation happen? -->
<!-- scope: telescope -->
`academic`, `independent`

#### Curation Organization(s)

<!-- info: Name the organization(s). -->
<!-- scope: periscope -->
The dataset was curated by a joint team of researchers from the University of Southern California and Allen Institute for Artificial Intelligence.

#### Dataset Creators

<!-- info: Who created the original dataset? List the people involved in collecting the dataset and their affiliation(s). -->
<!-- scope: microscope -->
Bill Yuchen Lin (USC), Wangchunshu Zhou (USC), Ming Shen (USC), Pei Zhou (USC), Chandra Bhagavatula (AllenAI), Yejin Choi (AllenAI + UW), Xiang Ren (USC)

#### Funding

<!-- info: Who funded the data creation? -->
<!-- scope: microscope -->
The research is based upon work supported in part by the Office of the Director of National Intelligence (ODNI), Intelligence Advanced Research Projects Activity (IARPA), the DARPA MCS program, and NSF SMA 18-29268.

#### Who added the Dataset to GEM?

<!-- info: Who contributed to the data card and adding the dataset to GEM? List the people+affiliations involved in creating this data card and who helped integrate this dataset into GEM. -->
<!-- scope: microscope -->
Yacine Jernite created the initial data card. It was later extended by Simon Mille. Sebastian Gehrmann migrated it to the GEMv2 format. 


### Dataset Structure

#### Data Fields

<!-- info: List and describe the fields present in the dataset. -->
<!-- scope: telescope -->
A data instance has the following fields:

- `concepts`: a `list` of  `string` values denoting the concept the system should write about. Has 3 to 5 items, constitutes the `input` of the task.
- `target`: a sentence `string` mentioning all of the above mentioned `concepts`. Constitutes the desired `output` of the task.


#### Example Instance

<!-- info: Provide a JSON formatted example of a typical instance in the dataset. -->
<!-- scope: periscope -->
```
[
  {
    "concepts": ['ski', 'mountain', 'skier'],
    "target": 'Skier skis down the mountain',
  },
  {
    "concepts": ['ski', 'mountain', 'skier'],
    "target": 'Three skiers are skiing on a snowy mountain.',
  },
]
```

#### Data Splits

<!-- info: Describe and name the splits in the dataset if there are more than one. -->
<!-- scope: periscope -->
Each example in the dataset consists of a set of 3 to 5 concepts denoted by a single noun, verb, or adjective (the input), and a sentence using these concepts (the output). The dataset provides several such sentences for each such concept.

|                           | Train  | Dev   | Test  |
|---------------------------|--------|-------|-------|
| **Total concept-sets**    | 32,651 | 993   | 1,497 |
| **Total sentences**       | 67,389 | 4,018 | 6,042 |
|**Average sentence length**| 10.54  | 11.55 | 13.34 |



#### Splitting Criteria

<!-- info: Describe any criteria for splitting the data, if used. If there are differences between the splits (e.g., if the training annotations are machine-generated and the dev and test ones are created by humans, or if different numbers of annotators contributed to each example), describe them here. -->
<!-- scope: microscope -->
The dev and test set were created by sampling sets of concepts of size 4 or 5 (and as many of size 3 for the dev set) present in the source captioning datasets and having crowd-workers write reference sentences using these concepts.

Conversely, the training set has more concept sets of size 3 than of size 4 and 5, and uses the original captions from the source datasets as references.

The authors also ensured that the training, dev and test set have different combinations of unique concepts to ensure compositionality (details in [Table 1](https://arxiv.org/pdf/1911.03705v3.pdf)).



## Dataset in GEM

### Rationale for Inclusion in GEM

#### Why is the Dataset in GEM?

<!-- info: What does this dataset contribute toward better generation evaluation and why is it part of GEM? -->
<!-- scope: microscope -->
CommonGen is a medium sized corpus with a unique reasoning challenge and interesting evaluation possibilities.


#### Similar Datasets

<!-- info: Do other datasets for the high level task exist? -->
<!-- scope: telescope -->
no

#### Ability that the Dataset measures

<!-- info: What aspect of model ability can be measured with this dataset? -->
<!-- scope: periscope -->
Commonsense reasoning


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
4 challenge sets for CommenGen were added to the GEM evaluation suite.


#### Additional Splits?

<!-- info: Does GEM provide additional splits to the dataset? -->
<!-- scope: telescope -->
yes

#### Split Information

<!-- info: Describe how the new splits were created -->
<!-- scope: periscope -->
1. Data Shift

We created subsets of the training and development sets of ~500 randomly selected inputs each.

2. Transformations

We applied input scrambling on a subset of 500 randomly selected test instances; the order of the concepts was randomly reassigned.

3. Subpopulations

We created a subpopulation based on input length, taking into account the number of concepts the input test structures. By comparing inputs of different lengths, we can see to what extent systems are able to handle different input sizes

| Concept number | Frequency English |
|----------------|-------------------|
| 4              |               747 |
| 5              |               750 |




#### Split Motivation

<!-- info: What aspects of the model's generation capacities were the splits created to test? -->
<!-- scope: periscope -->
Generalization and Robustness


### Getting Started with the Task

#### Pointers to Resources

<!-- info: Getting started with in-depth research on the task. Add relevant pointers to resources that researchers can consult when they want to get started digging deeper into the task. -->
<!-- scope: microscope -->
- Two variants of [BART](https://arxiv.org/abs/1910.13461), [Knowledge Graph augemnted-BART](https://arxiv.org/abs/2009.12677) and [Enhanced Knowledge Injection Model for Commonsense Generation](https://arxiv.org/abs/2012.00366), hold the top two spots on the leaderboard, followed by a fine-tuned [T5 model](https://arxiv.org/abs/1910.10683).
- The following script shows how to download and load the data, fine-tune, and evaluate a model using the ROUGE, BLEU, and METEOR metrics: [GEM sample script](https://github.com/GEM-benchmark/GEM-baseline-models/blob/main/examples/GEM-common_gen.ipynb).




## Previous Results

### Previous Results

#### Measured Model Abilities

<!-- info: What aspect of model ability can be measured with this dataset? -->
<!-- scope: telescope -->
Commonsense Reasoning

#### Metrics

<!-- info: What metrics are typically used for this task? -->
<!-- scope: periscope -->
`Other: Other Metrics`, `BLEU`, `ROUGE`, `METEOR`

#### Other Metrics

<!-- info: Definitions of other metrics -->
<!-- scope: periscope -->
- SPICE: An evaluation metric for image captioning that is defined over scene graphs
- CIDEr: An n-gram overlap metric based on cosine similarity between the TF-IDF weighted ngram counts


#### Proposed Evaluation

<!-- info: List and describe the purpose of the metrics and evaluation methodology (including human evaluation) that the dataset creators used when introducing this task. -->
<!-- scope: microscope -->
The main metrics are captioning metrics since the original concept lists were extracted from captioning datasets. A human subject study with five graduate students was conducted and they were asked to rank the "commonsense plausibility" of two models at a time. 

#### Previous results available?

<!-- info: Are previous results available? -->
<!-- scope: telescope -->
yes

#### Other Evaluation Approaches

<!-- info: What evaluation approaches have others used? -->
<!-- scope: periscope -->
The currently best performing model KFCNet (https://aclanthology.org/2021.findings-emnlp.249/) uses the same automatic evaluation but does not conduct any human evaluation. 

#### Relevant Previous Results

<!-- info: What are the most relevant previous results for this task/dataset? -->
<!-- scope: microscope -->
The most relevant results can be seen on the [leaderboard](https://inklab.usc.edu/CommonGen/leaderboard.html)



## Dataset Curation

### Original Curation

#### Original Curation Rationale

<!-- info: Original curation rationale -->
<!-- scope: telescope -->
The dataset creators selected sets of concepts that appeared in image and video captions (as identified by a POS tagger) to ensure that a likely real-world scenario including the set could be imagined and constructed. Section 3.1 of the [paper](https://arxiv.org/pdf/1911.03705v3.pdf) describes a sampling scheme which encourages diversity of sets while selecting common concepts.


#### Communicative Goal

<!-- info: What was the communicative goal? -->
<!-- scope: periscope -->
The speaker is required to produce a *coherent* sentence which mentions all of the source concepts, and which describes a *likely* situation that could be captured in a picture or video.


#### Sourced from Different Sources

<!-- info: Is the dataset aggregated from different data sources? -->
<!-- scope: telescope -->
yes

#### Source Details

<!-- info: List the sources (one per line) -->
<!-- scope: periscope -->
  - [Flickr30k](https://www.mitpressjournals.org/doi/abs/10.1162/tacl_a_00166)
  - [MSCOCO](https://link.springer.com/chapter/10.1007/978-3-319-10602-1_48)
  - [Conceptual Captions](https://www.aclweb.org/anthology/P18-1238/)
- Video captioning datasets:
  - [LSMDC](https://link.springer.com/article/10.1007/s11263-016-0987-1)
  - [ActivityNet](https://openaccess.thecvf.com/content_iccv_2017/html/Krishna_Dense-Captioning_Events_in_ICCV_2017_paper.html)
  - [VaTeX](https://openaccess.thecvf.com/content_ICCV_2019/html/Wang_VaTeX_A_Large-Scale_High-Quality_Multilingual_Dataset_for_Video-and-Language_Research_ICCV_2019_paper.html)



### Language Data

#### How was Language Data Obtained?

<!-- info: How was the language data obtained? -->
<!-- scope: telescope -->
`Crowdsourced`

#### Where was it crowdsourced?

<!-- info: If crowdsourced, where from? -->
<!-- scope: periscope -->
`Amazon Mechanical Turk`

#### Language Producers

<!-- info: What further information do we have on the language producers? -->
<!-- scope: microscope -->
The training data consists of concept sets and captions for the source datasets. The concept sets are the sets of labels of the images or videos, selected with a heuristic to maximize diversity while ensuring that they represent likely scenarios.

The dev and test set sentences were created by Amazon Mechanical Turk crowd workers. The workers were shown an example generation and a set of 4 or 5 concept names along with their part-of-speech and asked to write:
1. One sentence mentioning all of the concepts
2. A rationale explaining how the sentence connects the concept

A screenshot of the interface is provided in Figure 7 of the [Appendix](https://arxiv.org/pdf/1911.03705v3.pdf).


#### Topics Covered

<!-- info: Does the language in the dataset focus on specific topics? How would you describe them? -->
<!-- scope: periscope -->
Information was not provided.

#### Data Validation

<!-- info: Was the text validated by a different worker or a data curator? -->
<!-- scope: telescope -->
validated by data curator

#### Was Data Filtered?

<!-- info: Were text instances selected or filtered? -->
<!-- scope: telescope -->
algorithmically

#### Filter Criteria

<!-- info: What were the selection criteria? -->
<!-- scope: microscope -->
During the data collection, workers who provided rationales that were too short, failed to have good coverage of the input in their sentences, or workers whose output had a high perplexity under a GPT-2 model were disqualified from the pool and replaced with newcomers.



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
The data was sourced from Mechanical Turk which means that raters were aware that their annotations may be publicly released for research purposes.  


### Private Identifying Information (PII)

#### Contains PII?

<!-- quick -->
<!-- info: Does the source language data likely contain Personal Identifying Information about the data creators or subjects? -->
<!-- scope: telescope -->
no PII

#### Justification for no PII

<!-- info: Provide a justification for selecting `no PII` above. -->
<!-- scope: periscope -->
The concepts are restricted to verbs, adjectives, and common nouns, and no personal information is given in the captions.



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
The dataset is created using data from image captioning systems and might inherit some of the social biases represented therein (see e.g. [Tang et al. 2020](https://arxiv.org/abs/2006.08315)).

Another related concern is the exposure bias introduced by the initial selection of pictures and video, which are likely to over-represent situations that are common in the US at the expense of other parts of the world (Flickr, for example, is a US-based company founded in Canada). For more discussion of the potential impacts of exposure bias, see e.g. [The Social Impact of Natural Language Processing](https://www.aclweb.org/anthology/P16-2096.pdf).





## Considerations for Using the Data

### PII Risks and Liability

#### Potential PII Risk

<!-- info: Considering your answers to the PII part of the Data Curation Section, describe any potential privacy to the data subjects and creators risks when using the dataset. -->
<!-- scope: microscope -->
The concepts are restricted to verbs, adjectives, and common nouns, and no personal information is given in the captions.



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
The dataset is in English, a language with an abundance of existing resources.

The use of GPT-2 to validate development ant test sentences [might be cause for similar concern](https://www.aclweb.org/anthology/D19-1339.pdf), but we do note that the authors only use the model to discount very high perplexity sequences which is less likely to surface those biases.

The language in the development and test set is crowdsourced, which means that it was written by workers whose main goal was speed. This is likely to impact the quality and variety of the targets. The population of crowdsource workers is also not identically distributed as the the base population of the locations the workers come from, which may lead to different representation of situations or underlying expectations of what these situations are.


#### Unsuited Applications

<!-- info: When using a model trained on this dataset in a setting where users or the public may interact with its predictions, what are some pitfalls to look out for? In particular, describe some applications of the general task featured in this dataset that its curation or properties make it less suitable for. -->
<!-- scope: microscope -->
Due to the overrepresentation of US-situations, the system may not work for users across the world. Moreover, only limited information on the dataset quality are provided and the system may fail as a result of unknown issues.

#### Discouraged Use Cases

<!-- info: What are some discouraged use cases of a model trained to maximize the proposed metrics on this dataset? In particular, think about settings where decisions made by a model that performs reasonably well on the metric my still have strong negative consequences for user or members of the public. -->
<!-- scope: microscope -->
Any system needs to be evaluated on a broader set of unseen concepts then provided in the dataset. Since the references for the test set are private, it is not known how well findings generalize beyond the collection methodology. 


