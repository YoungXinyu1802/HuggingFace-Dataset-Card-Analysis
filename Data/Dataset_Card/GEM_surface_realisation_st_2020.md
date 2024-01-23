---
annotations_creators:
- none
language_creators:
- unknown
language:
- ar
- zh
- en
- fr
- hi
- id
- ja
- ko
- pt
- ru
- es
license:
- cc-by-2.5
multilinguality:
- unknown
size_categories:
- unknown
source_datasets:
- original
task_categories:
- table-to-text
task_ids: []
pretty_name: surface_realisation_st_2020
tags:
- data-to-text
---

# Dataset Card for GEM/surface_realisation_st_2020

## Dataset Description

- **Homepage:** http://taln.upf.edu/pages/msr2020-ws/SRST.html#data
- **Repository:** https://sites.google.com/site/genchalrepository/surface-realisation/sr-20-multilingual
- **Paper:** https://aclanthology.org/2020.msr-1.1/
- **Leaderboard:** N/A
- **Point of Contact:** Simon Mille

### Link to Main Data Card

You can find the main data card on the [GEM Website](https://gem-benchmark.com/data_cards/surface_realisation_st_2020).

### Dataset Summary 

This dataset was used as part of the multilingual surface realization shared task in which a model gets full or partial universal dependency structures and has to reconstruct the natural language. This dataset support 11 languages. 

You can load the dataset via:
```
import datasets
data = datasets.load_dataset('GEM/surface_realisation_st_2020')
```
The data loader can be found [here](https://huggingface.co/datasets/GEM/surface_realisation_st_2020).

#### website
[Website](http://taln.upf.edu/pages/msr2020-ws/SRST.html#data)

#### paper
[ACL Anthology](https://aclanthology.org/2020.msr-1.1/)

#### authors
Simon Mille (Pompeu Fabra University); Leo Wanner (Pompeu Fabra University); Anya Belz (Brighton University); Bernd Bohnet (Google Inc.); Thiago Castro Ferreira (Federal University of Minas Gerais); Yvette Graham (ADAPT/Trinity College Dublin)

## Dataset Overview

### Where to find the Data and its Documentation

#### Webpage

<!-- info: What is the webpage for the dataset (if it exists)? -->
<!-- scope: telescope -->
[Website](http://taln.upf.edu/pages/msr2020-ws/SRST.html#data)

#### Download

<!-- info: What is the link to where the original dataset is hosted? -->
<!-- scope: telescope -->
[Website](https://sites.google.com/site/genchalrepository/surface-realisation/sr-20-multilingual)

#### Paper

<!-- info: What is the link to the paper describing the dataset (open access preferred)? -->
<!-- scope: telescope -->
[ACL Anthology](https://aclanthology.org/2020.msr-1.1/)

#### BibTex

<!-- info: Provide the BibTex-formatted reference for the dataset. Please use the correct published version (ACL anthology, etc.) instead of google scholar created Bibtex. -->
<!-- scope: microscope -->
```
@inproceedings{mille-etal-2020-third,
    title = "The Third Multilingual Surface Realisation Shared Task ({SR}{'}20): Overview and Evaluation Results",
    author = "Mille, Simon  and
      Belz, Anya  and
      Bohnet, Bernd  and
      Castro Ferreira, Thiago  and
      Graham, Yvette  and
      Wanner, Leo",
    booktitle = "Proceedings of the Third Workshop on Multilingual Surface Realisation",
    month = dec,
    year = "2020",
    address = "Barcelona, Spain (Online)",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.msr-1.1",
    pages = "1--20",
    abstract = "This paper presents results from the Third Shared Task on Multilingual Surface Realisation (SR{'}20) which was organised as part of the COLING{'}20 Workshop on Multilingual Surface Realisation. As in SR{'}18 and SR{'}19, the shared task comprised two tracks: (1) a Shallow Track where the inputs were full UD structures with word order information removed and tokens lemmatised; and (2) a Deep Track where additionally, functional words and morphological information were removed. Moreover, each track had two subtracks: (a) restricted-resource, where only the data provided or approved as part of a track could be used for training models, and (b) open-resource, where any data could be used. The Shallow Track was offered in 11 languages, whereas the Deep Track in 3 ones. Systems were evaluated using both automatic metrics and direct assessment by human evaluators in terms of Readability and Meaning Similarity to reference outputs. We present the evaluation results, along with descriptions of the SR{'}19 tracks, data and evaluation methods, as well as brief summaries of the participating systems. For full descriptions of the participating systems, please see the separate system reports elsewhere in this volume.",
}
```

#### Contact Name

<!-- quick -->
<!-- info: If known, provide the name of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
Simon Mille

#### Contact Email

<!-- info: If known, provide the email of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
sfmille@gmail.com

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
No multiple dialects.

#### Covered Languages

<!-- quick -->
<!-- info: What languages/dialects are covered in the dataset? -->
<!-- scope: telescope -->
`Arabic`, `Chinese`, `English`, `French`, `Hindi`, `Indonesian`, `Japanese`, `Korean`, `Portuguese`, `Russian`, `Spanish, Castilian`

#### Whose Language?

<!-- info: Whose language is in the dataset? -->
<!-- scope: periscope -->
Unknown

#### License

<!-- quick -->
<!-- info: What is the license of the dataset? -->
<!-- scope: telescope -->
cc-by-2.5: Creative Commons Attribution 2.5 Generic

#### Intended Use

<!-- info: What is the intended use of the dataset? -->
<!-- scope: microscope -->
The dataset is intended to be used for training models to solve several NLG subtasks, such as function word introduction, morphological agreement resolution, word order determination and inflection generation.

Comment about the license: the dataset has multiple licences, since each original dataset has their own type of licence. All datasets but one are CC-BY and subclasses of it, the other one is GPL (French Sequoia).

#### Primary Task

<!-- info: What primary task does the dataset support? -->
<!-- scope: telescope -->
Data-to-Text

#### Communicative Goal

<!-- quick -->
<!-- info: Provide a short description of the communicative goal of a model trained for this task on this dataset. -->
<!-- scope: periscope -->
The models are able to introduce surface features (syntax, morphology, topology) from more or less abstract inputs in different, the most abstract being predicate-argument structures. The datasets cover a large variety of domains (news, blogs, forums, wikipedia pages, etc.).


### Credit

#### Curation Organization Type(s)

<!-- info: In what kind of organization did the dataset curation happen? -->
<!-- scope: telescope -->
`industry`, `academic`

#### Curation Organization(s)

<!-- info: Name the organization(s). -->
<!-- scope: periscope -->
Pompeu Fabra University, Google Inc., University of Brighton, Federal University of Minas Gerais, ADAPT/Trinity College Dublin

#### Dataset Creators

<!-- info: Who created the original dataset? List the people involved in collecting the dataset and their affiliation(s). -->
<!-- scope: microscope -->
Simon Mille (Pompeu Fabra University); Leo Wanner (Pompeu Fabra University); Anya Belz (Brighton University); Bernd Bohnet (Google Inc.); Thiago Castro Ferreira (Federal University of Minas Gerais); Yvette Graham (ADAPT/Trinity College Dublin)

#### Funding

<!-- info: Who funded the data creation? -->
<!-- scope: microscope -->
Mostly EU funds via H2020 projects 

#### Who added the Dataset to GEM?

<!-- info: Who contributed to the data card and adding the dataset to GEM? List the people+affiliations involved in creating this data card and who helped integrate this dataset into GEM. -->
<!-- scope: microscope -->
Simon Mille (Pompeu Fabra University)


### Dataset Structure

#### Data Fields

<!-- info: List and describe the fields present in the dataset. -->
<!-- scope: telescope -->
`input` (string): this field contains an input tree in CoNLL-U format; the CoNLL-U format is a one-word-per-line format with the following tab-separated 10 columns (see [here](http://universaldependencies.org/format.html)):  [1] Position, [2] Lemma, [3] Wordform, [4] Part of Speech, [5] Fine-grained Part of Speech (if available), [6] Features (FEATS), [7] governor, [8] dependency relation, [9] additional dependency information, and [10] metadata. For the surface task, the input is a Universal Dependency tree of a given language in which the word order was scrambled and the surface forms removed (only lemmas are available); for the deep task, the input is a tree derived from the surface input, with predicate-argument relations between content words only (function words were removed) and without any morphological agreement information.

`target_tokenized` (string): this field contains the target sentence to generate, in which every non-initial and non-final token is surrounded by two spaces. This output is usually used for automatic evaluations.

`target` (string): this field contains the detokenised target sentence to generate. This output is usually used for human evaluations.

`gem_id` (string): a unique ID.

`sentence_id` (string): the original ID of a sentence in the UD dataset.

#### Reason for Structure

<!-- info: How was the dataset structure determined? -->
<!-- scope: microscope -->
The structure of the input (CoNLL-U) was chosen according to the standards in parsing, and because the original UD datasets were provided in this format.

#### How were labels chosen?

<!-- info: How were the labels chosen? -->
<!-- scope: microscope -->
The input labels for the surface track are the original labels in the UD treebanks; see [here](https://universaldependencies.org/u/dep/index.html) for the dependencies, [here](https://universaldependencies.org/u/feat/index.html) for the features, and [here](https://universaldependencies.org/u/pos/index.html) for the PoS tags.

The input labels for the deep track are a subset of the PoS tags and features of the surface track, and for the relations, universal predicate-argument relations augmented with a few specific relations to capture coordinations and named entity relations for instance.

#### Example Instance

<!-- info: Provide a JSON formatted example of a typical instance in the dataset. -->
<!-- scope: periscope -->
```
{"input": "1\tGoogle\t_\tPROPN\tNNP\tNumber=Sing\t5\tnsubj\t_\t_\n2\t\t_\tPUNCT\t.\tlin=+1\t5\tpunct\t_\t_\n3\tinto\t_\tADP\tIN\t_\t6\tcase\t_\t_\n4\tif\t_\tSCONJ\tIN\t_\t5\tmark\t_\t_\n5\tmorph\t_\tVERB\tVBD\tMood=Ind|Tense=Past|VerbForm=Fin\t7\tadvcl\t_\t_\n6\tGoogleOS\t_\tPROPN\tNNP\tNumber=Sing\t5\tobl\t_\t_\n7\twhat\t_\tPRON\tWP\tPronType=Int\t0\troot\t_\t_", "target_tokenized": "What if Google Morphed Into GoogleOS ?", "target": "What if Google Morphed Into GoogleOS?", "gem_id": "GEM-surface_realisation_st_2020-T1-test-en_ewt-ud-test-0", "sentence_id": ""}
```

#### Data Splits

<!-- info: Describe and name the splits in the dataset if there are more than one. -->
<!-- scope: periscope -->
There are 119 splits in the dataset:

- 29 training sets, which correspond to 20 UD datasets (11 languages), 9 of which have both surface and deep inputs (3 languages);
- 29 development set which correspond to the 29 training sets above;
- 29 test sets for the data described above;
- 4 out-of-domain test sets,  3 surface inputs and 1 deep one (3 languages for which PUD out-of-domain datasets were available);
- 9 automatically parsed in-domain test sets, 6 surface inputs and 3 deep inputs (6 languages for which good UD parsers were available);
- 9 automatically parsed out-of-domain test sets, 6 surface inputs and 3 deep inputs (6 languages for which we were able to create clean Wikipedia text and that had a good UD parser).

#### Splitting Criteria

<!-- info: Describe any criteria for splitting the data, if used. If there are differences between the splits (e.g., if the training annotations are machine-generated and the dev and test ones are created by humans, or if different numbers of annotators contributed to each example), describe them here. -->
<!-- scope: microscope -->
Described above for more clarity.

#### 

<!-- info: What does an outlier of the dataset in terms of length/perplexity/embedding look like? -->
<!-- scope: microscope -->
An outlier would usually be an input that corresponds to a very long sentence (e.g. 159 words in English, when the average number of words per sentence is around 25).



## Dataset in GEM

### Rationale for Inclusion in GEM

#### Why is the Dataset in GEM?

<!-- info: What does this dataset contribute toward better generation evaluation and why is it part of GEM? -->
<!-- scope: microscope -->
The datset includes languages from different families and some languages not often used in NLG (e.g. Arabic, Indonesian, Korean, Hindi). It proposes two tasks, which can be tackled both separately and in one shot, with different levels of difficulty: the most superficial task (T1) consits in ordering and inflecting some trees, and the deeper task (T2) includes extra tasks such as defining the syntactic structure and introducing function words and morphological agreement information. Both tasks can allow for developing modules for pipeline NLG architectures. T1 is rather straightforward to evaluate: BLEU works quite well for some languages since all the words are present in the input and few word orders only can be possible for a syntactic tree. But T2 is more challenging to evaluate, since more outputs are correct given one particular input.

There is a large variety of sizes in the datasets, both clean and noisy data, parallel data in different languages, and many already available system outputs to use as baselines.

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
This is possibly the only dataset that starts the generation process from predicate-argument structures and from syntactic structures. It also has parallel datasets in a few languages (coming from the PUD parallel annotations).

#### Ability that the Dataset measures

<!-- info: What aspect of model ability can be measured with this dataset? -->
<!-- scope: periscope -->
Syntacticisation, functional word introduction, word order resolution, agreement resolution, morphological inflection


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
[Website](http://taln.upf.edu/pages/msr2020-ws/SRST.html)

#### Technical Terms

<!-- info: Technical terms used in this card and the dataset and their definitions -->
<!-- scope: microscope -->
Syntacticisation: prediction of the syntactic 



## Previous Results

### Previous Results

#### Measured Model Abilities

<!-- info: What aspect of model ability can be measured with this dataset? -->
<!-- scope: telescope -->
Syntacticisation, functional word introduction, word order resolution, morphological agreement resolution, morphological inflection

#### Metrics

<!-- info: What metrics are typically used for this task? -->
<!-- scope: periscope -->
`BLEU`, `BERT-Score`, `Other: Other Metrics`

#### Other Metrics

<!-- info: Definitions of other metrics -->
<!-- scope: periscope -->
NIST: n-gram similarity metric weighted in favour of less frequent n-grams which are taken to be more informative.

Normalised edit distance (DIST): inverse, normalised, character-based string-edit distance that starts by computing the minimum number of character inserts, deletes and substitutions (all at cost 1) required to turn the system output into the (single) reference text.

#### Proposed Evaluation

<!-- info: List and describe the purpose of the metrics and evaluation methodology (including human evaluation) that the dataset creators used when introducing this task. -->
<!-- scope: microscope -->
BLEU, NIST, BERTScore and DIST simply aim at calculating in different ways the similarity between a predicted and a reference sentence.

Two additional criteria have been used for human evaluation, Readability and Meaning SImilarity.  The statement to be  assessed in the Readability evaluation was: "The text reads well and is free from grammatical errors and awkward constructions.". The corresponding statement in the Meaning Similarity evaluation, in which system outputs (‘the black text’) were compared to reference sentences (‘the gray text’), was: "The meaning of the gray text is adequately expressed by the black text."


#### Previous results available?

<!-- info: Are previous results available? -->
<!-- scope: telescope -->
yes

#### Other Evaluation Approaches

<!-- info: What evaluation approaches have others used? -->
<!-- scope: periscope -->
Same as above.

#### Relevant Previous Results

<!-- info: What are the most relevant previous results for this task/dataset? -->
<!-- scope: microscope -->
- [Fast and Accurate Non-Projective Dependency Tree Linearization](https://aclanthology.org/2020.acl-main.134/)
- [Shape of Synth to Come: Why We Should Use Synthetic Data for English Surface Realization](https://aclanthology.org/2020.acl-main.665/)



## Dataset Curation

### Original Curation

#### Original Curation Rationale

<!-- info: Original curation rationale -->
<!-- scope: telescope -->
The datasets were created in the context of the Surface Realisation Shared Task series.

#### Communicative Goal

<!-- info: What was the communicative goal? -->
<!-- scope: periscope -->
The dataset's objective was to allow for training systems to perform tasks related to surface realisation (introduction of function words, syntacticisation, resolution of morphological agreements, word order resolution, inflection generation.

#### Sourced from Different Sources

<!-- info: Is the dataset aggregated from different data sources? -->
<!-- scope: telescope -->
yes

#### Source Details

<!-- info: List the sources (one per line) -->
<!-- scope: periscope -->
Each of the 20 used UD datasets comes from various sources, all listed on the individual page of each UD treeebank (https://universaldependencies.org/).

Additional test sets were created for the task, and were obtained from Wikipedia pages for 6 languages.


### Language Data

#### How was Language Data Obtained?

<!-- info: How was the language data obtained? -->
<!-- scope: telescope -->
`Found`

#### Where was it found?

<!-- info: If found, where from? -->
<!-- scope: telescope -->
`Multiple websites`

#### Language Producers

<!-- info: What further information do we have on the language producers? -->
<!-- scope: microscope -->
There are numerous sources of language in the multiple datasets.

#### Topics Covered

<!-- info: Does the language in the dataset focus on specific topics? How would you describe them? -->
<!-- scope: periscope -->
There is a large variety of topics in the multiple datasets.

#### Data Validation

<!-- info: Was the text validated by a different worker or a data curator? -->
<!-- scope: telescope -->
not validated

#### Data Preprocessing

<!-- info: How was the text data pre-processed? (Enter N/A if the text was not pre-processed) -->
<!-- scope: microscope -->
The text data was detokenised so as to create references for automatic evaluations (several languages don't use spaces to separate words, and running metrics like BLEU would not make sense without separating all the tokens in a sentence).

#### Was Data Filtered?

<!-- info: Were text instances selected or filtered? -->
<!-- scope: telescope -->
hybrid

#### Filter Criteria

<!-- info: What were the selection criteria? -->
<!-- scope: microscope -->
For the Wikipedia test created for the shared task, extensive filtering was applied to achieve reasonably good text quality. Sentences that include special characters, contain unusual tokens (e.g. ISBN), or have unbalanced quotation marks or brackets were skipped. Furthermore, only sentences with more than 5 tokens and shorter than 50 tokens were selected. After the initial filtering, quite a few malformed sentences remained. In order to remove those, the sentences were scored with BERT and
only the top half scored sentences were kept. Finally, via manual inspection, patterns and expressions were identified to
further reduce the number of malformed sentences.


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
The Universal Dependency data had been previously used for shared tasks on parsing, so it made sense to reuse it for generation.


### Private Identifying Information (PII)

#### Contains PII?

<!-- quick -->
<!-- info: Does the source language data likely contain Personal Identifying Information about the data creators or subjects? -->
<!-- scope: telescope -->
unlikely

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
yes

#### Details on how Dataset Addresses the Needs

<!-- info: Describe how this dataset addresses the needs of underserved communities. -->
<!-- scope: microscope -->
Thanks to the original work of the UD dataset creators, the surface realisation dataset addresses a few languages which are possibly under-served in NLG: e.g. Arabic, Hindi, Indonesian, Korean.


### Discussion of Biases

#### Any Documented Social Biases?

<!-- info: Are there documented social biases in the dataset? Biases in this context are variations in the ways members of different social categories are represented that can have harmful downstream consequences for members of the more disadvantaged group. -->
<!-- scope: telescope -->
no

#### Are the Language Producers Representative of the Language?

<!-- info: Does the distribution of language producers in the dataset accurately represent the full distribution of speakers of the language world-wide? If not, how does it differ? -->
<!-- scope: periscope -->
It is very likely that the distribution of language producers is not fully represented in the datasets of each language.



## Considerations for Using the Data

### PII Risks and Liability

#### Potential PII Risk

<!-- info: Considering your answers to the PII part of the Data Curation Section, describe any potential privacy to the data subjects and creators risks when using the dataset. -->
<!-- scope: microscope -->
No risks foreseen.


### Licenses

#### Copyright Restrictions on the Dataset

<!-- info: Based on your answers in the Intended Use part of the Data Overview Section, which of the following best describe the copyright and licensing status of the dataset? -->
<!-- scope: periscope -->
`multiple licenses`, `open license - commercial use allowed`

#### Copyright Restrictions on the Language Data

<!-- info: Based on your answers in the Language part of the Data Curation Section, which of the following best describe the copyright and licensing status of the underlying language data? -->
<!-- scope: periscope -->
`multiple licenses`, `open license - commercial use allowed`


### Known Technical Limitations

#### Technical Limitations

<!-- info: Describe any known technical limitations, such as spurrious correlations, train/test overlap, annotation biases, or mis-annotations, and cite the works that first identified these limitations when possible. -->
<!-- scope: microscope -->
The deep track inputs (predicate-argument structures) are not of perfect quality, they were derived automatically from gold or predicted syntactic parses using handcrafted grammars.

#### Unsuited Applications

<!-- info: When using a model trained on this dataset in a setting where users or the public may interact with its predictions, what are some pitfalls to look out for? In particular, describe some applications of the general task featured in this dataset that its curation or properties make it less suitable for. -->
<!-- scope: microscope -->
The datasets are probably not fitted to train tools to produce "unusual" languages (e.g. poetry, kid writing etc.). 

#### Discouraged Use Cases

<!-- info: What are some discouraged use cases of a model trained to maximize the proposed metrics on this dataset? In particular, think about settings where decisions made by a model that performs reasonably well on the metric my still have strong negative consequences for user or members of the public. -->
<!-- scope: microscope -->
To be thought of :)


