---
annotations_creators:
- unknown
language_creators:
- unknown
language:
- en
license:
- cc-by-nc-4.0
multilinguality:
- unknown
size_categories:
- unknown
source_datasets:
- original
task_categories:
- table-to-text
task_ids: []
pretty_name: web_nlg
tags:
- data-to-text
---

# Dataset Card for GEM/web_nlg

## Dataset Description

- **Homepage:** https://webnlg-challenge.loria.fr/
- **Repository:** https://gitlab.com/shimorina/webnlg-dataset
- **Paper:** http://www.aclweb.org/anthology/P17-1017, [WebNLG Challenge 2017 Report
- **Leaderboard:** https://beng.dice-research.org/gerbil/
- **Point of Contact:** [Needs More Information]

### Link to Main Data Card

You can find the main data card on the [GEM Website](https://gem-benchmark.com/data_cards/web_nlg).

### Dataset Summary 

WebNLG is a bi-lingual dataset (English, Russian) of parallel DBpedia triple sets and short texts that cover about 450 different DBpedia properties. The WebNLG data was originally created to promote the development of RDF verbalisers able to generate short text and to handle micro-planning (i.e., sentence segmentation and ordering, referring expression generation, aggregation); the goal of the task is to generate texts starting from 1 to 7 input triples which have entities in common (so the input is actually a connected Knowledge Graph). The dataset contains about 17,000 triple sets and 45,000 crowdsourced texts in English, and 7,000 triples sets and 19,000 crowdsourced texts in Russian. A challenging test set section with entities and/or properties that have not been seen at training time is available.

You can load the dataset via:
```
import datasets
data = datasets.load_dataset('GEM/web_nlg')
```
The data loader can be found [here](https://huggingface.co/datasets/GEM/web_nlg).

#### website
[Website](https://webnlg-challenge.loria.fr/)

#### paper
[First Dataset Release](http://www.aclweb.org/anthology/P17-1017), [WebNLG Challenge 2017 Report](https://www.aclweb.org/anthology/W17-3518/), [WebNLG Challenge 2020 Report](https://webnlg-challenge.loria.fr/files/2020.webnlg-papers.7.pdf)

#### authors
The principle curator of the dataset is Anastasia Shimorina (Université de Lorraine / LORIA, France). Throughout the WebNLG releases, several people contributed to their construction: Claire Gardent (CNRS / LORIA, France), Shashi Narayan (Google, UK), Laura Perez-Beltrachini (University of Edinburgh, UK), Elena Khasanova, and Thiago Castro Ferreira (Federal University of Minas Gerais, Brazil).

## Dataset Overview

### Where to find the Data and its Documentation

#### Webpage

<!-- info: What is the webpage for the dataset (if it exists)? -->
<!-- scope: telescope -->
[Website](https://webnlg-challenge.loria.fr/)

#### Download

<!-- info: What is the link to where the original dataset is hosted? -->
<!-- scope: telescope -->
[Gitlab](https://gitlab.com/shimorina/webnlg-dataset)

#### Paper

<!-- info: What is the link to the paper describing the dataset (open access preferred)? -->
<!-- scope: telescope -->
[First Dataset Release](http://www.aclweb.org/anthology/P17-1017), [WebNLG Challenge 2017 Report](https://www.aclweb.org/anthology/W17-3518/), [WebNLG Challenge 2020 Report](https://webnlg-challenge.loria.fr/files/2020.webnlg-papers.7.pdf)

#### BibTex

<!-- info: Provide the BibTex-formatted reference for the dataset. Please use the correct published version (ACL anthology, etc.) instead of google scholar created Bibtex. -->
<!-- scope: microscope -->
Initial release of the dataset:
```
@inproceedings{gardent2017creating,
  author = 	"Gardent, Claire
		and Shimorina, Anastasia
		and Narayan, Shashi
		and Perez-Beltrachini, Laura",
  title = 	"Creating Training Corpora for NLG Micro-Planners",
  booktitle = 	"Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
  year = 	"2017",
  publisher = 	"Association for Computational Linguistics",
  pages = 	"179--188",
  location = 	"Vancouver, Canada",
  doi = 	"10.18653/v1/P17-1017",
  url = 	"http://www.aclweb.org/anthology/P17-1017"
}
```

The latest version 3.0:
```
@inproceedings{castro-ferreira20:bilin-bi-direc-webnl-shared,
  title={The 2020 Bilingual, Bi-Directional WebNLG+ Shared Task Overview and Evaluation Results (WebNLG+ 2020)},
  author={Castro Ferreira, Thiago and
                  Gardent, Claire and
		  Ilinykh, Nikolai and
		  van der Lee, Chris and
		  Mille, Simon and
		  Moussallem, Diego and
		  Shimorina, Anastasia},
  booktitle = {Proceedings of the 3rd WebNLG Workshop on Natural Language Generation from the Semantic Web (WebNLG+ 2020)},
    pages = "55--76",
  year = 	 2020,
  address = 	 {Dublin, Ireland (Virtual)},
  publisher = {Association for Computational Linguistics}}
```

#### Contact Email

<!-- info: If known, provide the email of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
webnlg-challenge@inria.fr

#### Has a Leaderboard?

<!-- info: Does the dataset have an active leaderboard? -->
<!-- scope: telescope -->
yes

#### Leaderboard Link

<!-- info: Provide a link to the leaderboard. -->
<!-- scope: periscope -->
[Website](https://beng.dice-research.org/gerbil/)

#### Leaderboard Details

<!-- info: Briefly describe how the leaderboard evaluates models. -->
<!-- scope: microscope -->
The model outputs are evaluated against the crowdsourced references; the leaderboard reports BLEU-4, METEOR, chrF++, TER, BERTScore and BLEURT scores.


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
`Russian`, `English`

#### License

<!-- quick -->
<!-- info: What is the license of the dataset? -->
<!-- scope: telescope -->
cc-by-nc-4.0: Creative Commons Attribution Non Commercial 4.0 International

#### Intended Use

<!-- info: What is the intended use of the dataset? -->
<!-- scope: microscope -->
The WebNLG dataset was created to promote the development (_i_) of RDF verbalisers and (_ii_) of microplanners able to handle a wide range of linguistic constructions. The dataset aims at covering knowledge in different domains ("categories"). The same properties and entities can appear in several categories.


#### Primary Task

<!-- info: What primary task does the dataset support? -->
<!-- scope: telescope -->
Data-to-Text

#### Communicative Goal

<!-- quick -->
<!-- info: Provide a short description of the communicative goal of a model trained for this task on this dataset. -->
<!-- scope: periscope -->
A model should verbalize all and only the provided input triples in natural language.


### Credit

#### Curation Organization Type(s)

<!-- info: In what kind of organization did the dataset curation happen? -->
<!-- scope: telescope -->
`academic`

#### Curation Organization(s)

<!-- info: Name the organization(s). -->
<!-- scope: periscope -->
Université de Lorraine / LORIA, France, CNRS / LORIA, France, University of Edinburgh, UK, Federal University of Minas Gerais, Brazil

#### Dataset Creators

<!-- info: Who created the original dataset? List the people involved in collecting the dataset and their affiliation(s). -->
<!-- scope: microscope -->
The principle curator of the dataset is Anastasia Shimorina (Université de Lorraine / LORIA, France). Throughout the WebNLG releases, several people contributed to their construction: Claire Gardent (CNRS / LORIA, France), Shashi Narayan (Google, UK), Laura Perez-Beltrachini (University of Edinburgh, UK), Elena Khasanova, and Thiago Castro Ferreira (Federal University of Minas Gerais, Brazil).

#### Funding

<!-- info: Who funded the data creation? -->
<!-- scope: microscope -->
The dataset construction was funded by the French National Research Agency (ANR).

#### Who added the Dataset to GEM?

<!-- info: Who contributed to the data card and adding the dataset to GEM? List the people+affiliations involved in creating this data card and who helped integrate this dataset into GEM. -->
<!-- scope: microscope -->
Simon Mille and Sebastian Gehrmann added the dataset and wrote the data card.


### Dataset Structure

#### Data Fields

<!-- info: List and describe the fields present in the dataset. -->
<!-- scope: telescope -->
See [official documentation](https://webnlg-challenge.loria.fr/docs/).


`entry`: a data instance of the benchmark. Each entry has five attributes: a DBpedia category (`category`), entry ID (`eid`), shape, shape type, and triple set size (`size`).
	
- `shape`: a string representation of the RDF tree with nested parentheses where `X` is a node (see [Newick tree format](https://en.wikipedia.org/wiki/Newick_format)).

- `shape_type`: a type of the tree shape. We [identify](https://www.aclweb.org/anthology/C16-1141.pdf) three types of tree shapes:
    * `chain` (the object of one triple is the subject of the other);
    * `sibling` (triples with a shared subject);
    * `mixed` (both `chain` and `sibling` types present).
- `eid`: an entry ID. It is unique only within a category and a size.
- `category`: a DBpedia category (Astronaut, City, MusicalWork, Politician, etc.).
- `size`: the number of RDF triples in a set. Ranges from 1 to 7.

Each `entry` has three fields: `originaltripleset`, `modifiedtripleset`, and `lexs`.

`originaltripleset`: a set of RDF triples as extracted from [DBpedia](https://wiki.dbpedia.org/). Each set of RDF triples is a tree. Triples have the subject-predicate-object structure.

`modifiedtripleset`: a set of RDF triples as presented to crowdworkers (for more details on modifications, see below).

Original and modified triples serve different purposes: the original triples — to link data to a knowledge base (DBpedia), whereas the modified triples — to ensure consistency and homogeneity throughout the data. To train models, the modified triples should be used.

`lexs` (shortened for lexicalisations): a natural language text verbalising the triples. Each lexicalisation has two attributes: a comment (`comment`), and a lexicalisation ID (`lid`). By default, comments have the value `good`, except rare cases when they were manually marked as `toFix`. That was done during the corpus creation, when it was seen that a lexicalisation did not exactly match a triple set.

Russian data has additional optional fields comparing to English:

`<dbpedialinks>`: RDF triples extracted from DBpedia between English and Russian entities by means of the property `sameAs`.

`<links>`: RDF triples created manually for some entities to serve as pointers to translators. There are two types of them:

   * with `sameAs` (`Spaniards | sameAs | испанцы`)
    
   * with `includes` (`Tomatoes, guanciale, cheese, olive oil | includes | гуанчиале`). Those were mostly created for string literals to translate some parts of them.

Lexicalisations in the Russian WebNLG have a new parameter `lang` (values: `en`, `ru`) because original English texts were kept in the Russian version (see the example above).


#### Example Instance

<!-- info: Provide a JSON formatted example of a typical instance in the dataset. -->
<!-- scope: periscope -->

```
{
"entry": {
	"category": "Company",
	"size": "4",
	"shape": "(X (X) (X) (X) (X))",
	"shape_type": "sibling",
	"eid": "Id21",
	"lexs": [
	    {
		"comment": "good",
		"lex": "Trane, which was founded on January 1st 1913 in La Crosse, Wisconsin, is based in Ireland. It has 29,000 employees.",
		"lid": "Id1"
	    }
	],
	"modifiedtripleset": [
	    {
		"subject": "Trane",
		"property": "foundingDate",
		"object": "1913-01-01"
	    },
	    {
		"subject": "Trane",
		"property": "location",
		"object": "Ireland"
	    },
	    {
		"subject": "Trane",
		"property": "foundationPlace",
		"object": "La_Crosse,_Wisconsin"
	    },
	    {
		"subject": "Trane",
		"property": "numberOfEmployees",
		"object": "29000"
	    }

	],
	"originaltriplesets": {
	    "originaltripleset": [
		    {
			"subject": "Trane",
			"property": "foundingDate",
			"object": "1913-01-01"
		    },
		    {
			"subject": "Trane",
			"property": "location",
			"object": "Ireland"
		    },
		    {
			"subject": "Trane",
			"property": "foundationPlace",
			"object": "La_Crosse,_Wisconsin"
		    },
		    {
			"subject": "Trane",
			"property": "numberOfEmployees",
			"object": "29000"
		    }
	    ]
	}

	}
}
```

The XML-formatted example is [here](https://webnlg-challenge.loria.fr/docs/#example).


#### Data Splits

<!-- info: Describe and name the splits in the dataset if there are more than one. -->
<!-- scope: periscope -->


|  English (v3.0) | Train  | Dev   | Test  |
|-----------------|--------|-------|-------|
| **triple sets** | 13,211 | 1,667 | 1,779 |
| **texts**       | 35,426 | 4,464 | 5,150 |
|**properties**   | 372    | 290   | 220   |


|  Russian (v3.0) | Train  | Dev   | Test  |
|-----------------|--------|-------|-------|
| **triple sets** | 5,573  | 790   | 1,102 |
| **texts**       | 14,239 | 2,026 | 2,780 |
|**properties**   | 226    | 115   | 192   |



## Dataset in GEM

### Rationale for Inclusion in GEM

#### Why is the Dataset in GEM?

<!-- info: What does this dataset contribute toward better generation evaluation and why is it part of GEM? -->
<!-- scope: microscope -->
Due to the constrained generation task, this dataset can be used to evaluate very specific and narrow generation capabilities. 

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
The RDF-triple format is unique to WebNLG.

#### Ability that the Dataset measures

<!-- info: What aspect of model ability can be measured with this dataset? -->
<!-- scope: periscope -->
surface realization


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
No changes to the main content of the dataset. The [version 3.0](https://gitlab.com/shimorina/webnlg-dataset/-/tree/master/release_v3.0) of the dataset is used.


#### Additional Splits?

<!-- info: Does GEM provide additional splits to the dataset? -->
<!-- scope: telescope -->
yes

#### Split Information

<!-- info: Describe how the new splits were created -->
<!-- scope: periscope -->
23 special test sets for WebNLG were added to the GEM evaluation suite, 12 for English and 11 for Russian.
For both languages, we created subsets of the training and development sets of ~500 randomly selected inputs each. The inputs were sampled proportionally from each category.

Two types of transformations have been applied to WebNLG: (i) input scrambling (English and Russian) and (ii) numerical value replacements (English); in both cases, a subset of about 500 inputs was randomly selected. For (i), the order of the triples was randomly reassigned (each triple kept the same Subject-Property-Object internal order). For (ii), the change was performed respecting the format of the current cardinal value (e.g., alpha, integer, or floating-point) and replacing it with a new random value. The new number is lower-bounded between zero and upper bounded to be within to the highest power of 10 unit for the given value (e.g., replacing 54 would result in a random value between 0-100). Floating values maintain the degree of precision.

For both languages, we did identify different subsets of the test set that we could compare to each other so that we would have a better understanding of the results. There are currently 8 selections that we have made:

Selection 1 (size): input length. This selection corresponds to the number of predicates in the input. By comparing inputs of different lengths, we can see to what extent NLG systems are able to handle different input sizes.  The table below provides the relevant frequencies. Please be aware that comparing selections with fewer than 100 items may result in unreliable comparisons.

| Input length   | Frequency English | Frequency Russian |
|----------------|-------------------|-------------------|
|              1 |               369 |               254 |
|              2 |               349 |               200 |
|              3 |               350 |               214 |
|              4 |               305 |               214 |
|              5 |               213 |               159 |
|              6 |               114 |                32 |
|              7 |                79 |                29 |


Selection 2 (frequency): seen/unseen single predicates. This selection corresponds to the inputs with only one predicate. We compare which predicates are seen/unseen in the training data. The table below provides the relevant frequencies. Note that the comparison is only valid for English. Not for Russian, since there is only one example of unseen single predicates.

| _ in training | Frequency English | Frequency Russian |
|---------------|-------------------|-------------------|
| Seen          |               297 |               253 |
| Unseen        |                72 |                 1 |


Selection 3 (frequency): seen/unseen combinations of predicates. This selection checks for all combinations of predicates whether that combination has been seen in the training data. For example: if the combination of predicates A and B is seen, that means that there is an input in the training data consisting of two triples, where one triple uses predicate A and the other uses predicate B. If the combination is unseen, then the converse is true. The table below provides the relevant frequencies.

| _ in training | Frequency English | Frequency Russian |
|---------------|-------------------|-------------------|
| unseen        |              1295 |               354 |
| seen          |               115 |               494 |


Selection 4 (frequency): seen/unseen arguments. This selection checks for all input whether or not all arg1s and arg2s in the input have been seen during the training phase. For this selection, *Seen* is the default. Only if all arg1 instances for a particular input are unseen, do we count the arg1s of the input as unseen. The same holds for arg2. So "seen" here really means that at least some of the arg1s or arg2s are seen in the input. The table below provides the relevant frequencies. Note that the comparison is only valid for English. Not for Russian, since there are very few examples of unseen combinations of predicates.

| Arguments seen in training? | Frequency English | Frequency Russian |
|-----------------------------|-------------------|-------------------|
| both_seen                   |               518 |              1075 |
| both_unseen                 |              1177 |                 4 |
| arg1_unseen                 |                56 |                19 |
| arg2_unseen                 |                28 |                 4 |

Selection 5 (shape): repeated subjects. For this selection, the subsets are based on the times a subject is repeated in the input; it only takes into account the maximum number of times a subject is repeated, that is, if in one input a subject appears 3 times and a different subject 2 times, this input will be in the "3_subjects_same' split. Unique_subjects means all subjects are different. 

| Max num. of repeated subjects | Frequency English | Frequency Russian |
|-------------------------------|-------------------|-------------------|
| unique_subjects               |               453 |               339 |
| 2_subjects_same               |               414 |               316 |
| 3_subjects_same               |               382 |               217 |
| 4_subjects_same               |               251 |               143 |
| 5_subjects_same               |               158 |                56 |
| 6_subjects_same               |                80 |                19 |
| 7_subjects_same               |                41 |                12 |

Selection 6 (shape): repeated objects. Same as for subjects above, but for objects. There are much less cases of repeated objects, so there are only two categories for this selection, unique_objects and some_objects_repeated; for the latter, we have up to 3 coreferring objects in English, and XXX in Russian.

| Max num. of repeated objects | Frequency English | Frequency Russian |
|------------------------------|-------------------|-------------------|
| unique_objects               |              1654 |              1099 |
| some_objects_same            |               125 |                 3 |

Selection 7 (shape): repeated properties. Same as for objects above, but for properties; up to two properties can be the same in English, up to XXX in Russian.

| Max num. of repeated properties | Frequency English | Frequency Russian |
|---------------------------------|-------------------|-------------------|
| unique_properties               |              1510 |               986 |
| some_properties_same            |               269 |               116 |

Selection 8 (shape): entities that appear both as subject and object. For this selection, we grouped together the inputs in which no entity is found as both subject and object, and on the other side inputs in which one or more entity/ies appear both as subject and as object. We found up to two such entities per input in English, and up to XXX in Russian.

| Max num. of objects and subjects in common | Frequency English | Frequency Russian |
|--------------------------------------------|-------------------|-------------------|
| unique_properties                          |              1322 |               642 |
| some_properties_same                       |               457 |               460 |

#### Split Motivation

<!-- info: What aspects of the model's generation capacities were the splits created to test? -->
<!-- scope: periscope -->
Robustness


### Getting Started with the Task

#### Pointers to Resources

<!-- info: Getting started with in-depth research on the task. Add relevant pointers to resources that researchers can consult when they want to get started digging deeper into the task. -->
<!-- scope: microscope -->
Dataset construction: [main dataset paper](https://www.aclweb.org/anthology/P17-1017/), [RDF triple extraction](https://www.aclweb.org/anthology/C16-1141/), [Russian translation](https://www.aclweb.org/anthology/W19-3706/)

WebNLG Challenge 2017: [webpage](https://webnlg-challenge.loria.fr/challenge_2017/), [paper](https://www.aclweb.org/anthology/W17-3518/)

WebNLG Challenge 2020: [webpage](https://webnlg-challenge.loria.fr/challenge_2020/), [paper](https://webnlg-challenge.loria.fr/files/2020.webnlg-papers.7.pdf)

Enriched version of WebNLG: [repository](https://github.com/ThiagoCF05/webnlg), [paper](https://www.aclweb.org/anthology/W18-6521/)

Related research papers: [webpage](https://webnlg-challenge.loria.fr/research/)




## Previous Results

### Previous Results

#### Proposed Evaluation

<!-- info: List and describe the purpose of the metrics and evaluation methodology (including human evaluation) that the dataset creators used when introducing this task. -->
<!-- scope: microscope -->
For both languages, the participating systems are automatically evaluated in a multi-reference scenario. Each English hypothesis is compared to a maximum of 5 references, and each Russian one to a maximum of 7 references. On average, English data has 2.89 references per test instance, and Russian data has 2.52 references per instance. 

In a human evaluation, example are uniformly sampled across size of triple sets and the following dimensions are assessed (on MTurk and Yandex.Toloka):

1. Data Coverage: Does the text include descriptions of all predicates presented in the data?
2. Relevance: Does the text describe only such predicates (with related subjects and objects), which are found in the data?
3. Correctness: When describing predicates which are found in the data, does the text mention correct the objects and adequately introduces the subject for this specific predicate?
4. Text Structure: Is the text grammatical, well-structured, written in acceptable English language?
5. Fluency: Is it possible to say that the text progresses naturally, forms a coherent whole and it is easy to understand the text?

For additional information like the instructions, we refer to the original paper.


#### Previous results available?

<!-- info: Are previous results available? -->
<!-- scope: telescope -->
yes

#### Other Evaluation Approaches

<!-- info: What evaluation approaches have others used? -->
<!-- scope: periscope -->
We evaluated a wide range of models as part of the GEM benchmark.

#### Relevant Previous Results

<!-- info: What are the most relevant previous results for this task/dataset? -->
<!-- scope: microscope -->
Results can be found on the [GEM website](https://gem-benchmark.com/results).



## Broader Social Context

### Previous Work on the Social Impact of the Dataset

#### Usage of Models based on the Data

<!-- info: Are you aware of cases where models trained on the task featured in this dataset ore related tasks have been used in automated systems? -->
<!-- scope: telescope -->
yes - related tasks

#### Social Impact Observations

<!-- info: Did any of these previous uses result in observations about the social impact of the systems? In particular, has there been work outlining the risks and limitations of the system? Provide links and descriptions here. -->
<!-- scope: microscope -->
We do not foresee any negative social impact in particular from this dataset or task.

Positive outlooks: Being able to generate good quality text from RDF data would permit, e.g., making this data more accessible to lay users, enriching existing text with information drawn from knowledge bases such as DBpedia or describing, comparing and relating entities present in these knowledge bases.



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
This dataset is created using DBpedia RDF triples which naturally exhibit biases that have been found to exist in Wikipedia such as some forms of, e.g., gender bias.

The choice of [entities](https://gitlab.com/shimorina/webnlg-dataset/-/blob/master/supplementary/entities_dict.json), described by RDF trees, was not controlled. As such, they may contain gender biases; for instance, all the astronauts described by RDF triples are male. Hence, in texts, pronouns _he/him/his_ occur more often. Similarly, entities can be related to the Western culture more often than to other cultures.


#### Are the Language Producers Representative of the Language?

<!-- info: Does the distribution of language producers in the dataset accurately represent the full distribution of speakers of the language world-wide? If not, how does it differ? -->
<!-- scope: periscope -->
In English, the dataset is limited to the language that crowdraters speak. In Russian, the language is heavily biased by the translationese of the translation system that is post-edited. 



## Considerations for Using the Data

### PII Risks and Liability

#### Potential PII Risk

<!-- info: Considering your answers to the PII part of the Data Curation Section, describe any potential privacy to the data subjects and creators risks when using the dataset. -->
<!-- scope: microscope -->
There is no PII in this dataset.


### Licenses

#### Copyright Restrictions on the Dataset

<!-- info: Based on your answers in the Intended Use part of the Data Overview Section, which of the following best describe the copyright and licensing status of the dataset? -->
<!-- scope: periscope -->
`non-commercial use only`

#### Copyright Restrictions on the Language Data

<!-- info: Based on your answers in the Language part of the Data Curation Section, which of the following best describe the copyright and licensing status of the underlying language data? -->
<!-- scope: periscope -->
`public domain`


### Known Technical Limitations

#### Technical Limitations

<!-- info: Describe any known technical limitations, such as spurrious correlations, train/test overlap, annotation biases, or mis-annotations, and cite the works that first identified these limitations when possible. -->
<!-- scope: microscope -->
The quality of the crowdsourced references is limited, in particular in terms of fluency/naturalness of the collected texts.

Russian data was machine-translated and then post-edited by crowdworkers, so some examples may still exhibit issues related to bad translations.


#### Unsuited Applications

<!-- info: When using a model trained on this dataset in a setting where users or the public may interact with its predictions, what are some pitfalls to look out for? In particular, describe some applications of the general task featured in this dataset that its curation or properties make it less suitable for. -->
<!-- scope: microscope -->
Only a limited number of domains are covered in this dataset. As a result, it cannot be used as a general-purpose realizer. 


