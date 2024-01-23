---
annotations_creators:
- none
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
pretty_name: conversational_weather
tags:
- data-to-text
---

# Dataset Card for GEM/conversational_weather

## Dataset Description

- **Homepage:** [Needs More Information]
- **Repository:** https://github.com/facebookresearch/TreeNLG
- **Paper:** https://aclanthology.org/P19-1080
- **Leaderboard:** N/A
- **Point of Contact:** Kartikeya Upasani

### Link to Main Data Card

You can find the main data card on the [GEM Website](https://gem-benchmark.com/data_cards/conversational_weather).

### Dataset Summary 

The purpose of this dataset is to assess how well a model can learn a template-like structure in a very low data setting. The task here is to produce a response to a weather-related query. The reply is further specified through the data attributes and discourse structure in the input. The output contains both the lexicalized text and discourse markers for attributes (e.g., `_ARG_TEMP_ 34`). 

You can load the dataset via:
```
import datasets
data = datasets.load_dataset('GEM/conversational_weather')
```
The data loader can be found [here](https://huggingface.co/datasets/GEM/conversational_weather).

#### paper
[ACL Anthology](https://aclanthology.org/P19-1080)

#### authors
Anusha Balakrishnan, Jinfeng Rao, Kartikeya Upasani, Michael White, Rajen Subba (Facebook Conversational AI)

## Dataset Overview

### Where to find the Data and its Documentation

#### Download

<!-- info: What is the link to where the original dataset is hosted? -->
<!-- scope: telescope -->
[Github](https://github.com/facebookresearch/TreeNLG)

#### Paper

<!-- info: What is the link to the paper describing the dataset (open access preferred)? -->
<!-- scope: telescope -->
[ACL Anthology](https://aclanthology.org/P19-1080)

#### BibTex

<!-- info: Provide the BibTex-formatted reference for the dataset. Please use the correct published version (ACL anthology, etc.) instead of google scholar created Bibtex. -->
<!-- scope: microscope -->
```
@inproceedings{balakrishnan-etal-2019-constrained,
  title = "Constrained Decoding for Neural {NLG} from Compositional Representations in Task-Oriented Dialogue",
  author = "Balakrishnan, Anusha  and
    Rao, Jinfeng  and
    Upasani, Kartikeya  and
    White, Michael  and
    Subba, Rajen",
  booktitle = "Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics",
  month = jul,
  year = "2019",
  address = "Florence, Italy",
  publisher = "Association for Computational Linguistics",
  url = "https://www.aclweb.org/anthology/P19-1080",
  doi = "10.18653/v1/P19-1080",
  pages = "831--844"
}
```

#### Contact Name

<!-- quick -->
<!-- info: If known, provide the name of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
Kartikeya Upasani

#### Contact Email

<!-- info: If known, provide the email of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
kart@fb.com

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

#### License

<!-- quick -->
<!-- info: What is the license of the dataset? -->
<!-- scope: telescope -->
cc-by-nc-4.0: Creative Commons Attribution Non Commercial 4.0 International

#### Intended Use

<!-- info: What is the intended use of the dataset? -->
<!-- scope: microscope -->
This dataset is intended to help develop conversational agents that exhibit human-like properties such as matching the framing of the response with the query or contrasting relevant data attributes.

#### Primary Task

<!-- info: What primary task does the dataset support? -->
<!-- scope: telescope -->
Data-to-Text

#### Communicative Goal

<!-- quick -->
<!-- info: Provide a short description of the communicative goal of a model trained for this task on this dataset. -->
<!-- scope: periscope -->
Producing a text that is a response to a weather query as per the discourse structure and data attributes specified in the input meaning representation.


### Credit

#### Curation Organization Type(s)

<!-- info: In what kind of organization did the dataset curation happen? -->
<!-- scope: telescope -->
`industry`

#### Curation Organization(s)

<!-- info: Name the organization(s). -->
<!-- scope: periscope -->
Facebook

#### Dataset Creators

<!-- info: Who created the original dataset? List the people involved in collecting the dataset and their affiliation(s). -->
<!-- scope: microscope -->
Anusha Balakrishnan, Jinfeng Rao, Kartikeya Upasani, Michael White, Rajen Subba (Facebook Conversational AI)

#### Funding

<!-- info: Who funded the data creation? -->
<!-- scope: microscope -->
Facebook

#### Who added the Dataset to GEM?

<!-- info: Who contributed to the data card and adding the dataset to GEM? List the people+affiliations involved in creating this data card and who helped integrate this dataset into GEM. -->
<!-- scope: microscope -->
Vipul Raheja (Grammarly)


### Dataset Structure

#### Data Fields

<!-- info: List and describe the fields present in the dataset. -->
<!-- scope: telescope -->
- `gem_id`: (string): GEM-formatted row id
- `id`: (string): Row id in the original data
- `user_query`: (string): Natural language weather query from humans
- `tree_str_mr`: (string): Synthetically-added user context (datetime and location) in the form of a tree-structured MR
- `response`: (string): A tree-structured annotation of the response.


#### Example Instance

<!-- info: Provide a JSON formatted example of a typical instance in the dataset. -->
<!-- scope: periscope -->
```
{'gem_id': 'weather-train-11',
'id': '1108963',
 'synthetic_user_context': '[__DG_INFORM__ [__ARG_TASK__ get_forecast ] '
                           '[__ARG_TEMP__ 37 ] [__ARG_TEMP_UNIT__ fahrenheit ] '
                           '[__ARG_CLOUD_COVERAGE__ partly cloudy ] '
                           '[__ARG_DATE_TIME__ [__ARG_COLLOQUIAL__ currently ] '
                           '] [__ARG_LOCATION__ [__ARG_CITY__ Oakland ] '
                           '[__ARG_COUNTRY__ United States ] [__ARG_REGION__ '
                           'California ] ] ] [__DG_INFORM__ [__ARG_TASK__ '
                           'get_forecast ] [__ARG_TEMP_SUMMARY__ mid 40s ] '
                           '[__ARG_DATE_TIME_RANGE__ [__ARG_COLLOQUIAL__ This '
                           'afternoon ] ] [__ARG_LOCATION__ [__ARG_CITY__ '
                           'Oakland ] [__ARG_COUNTRY__ United States ] '
                           '[__ARG_REGION__ California ] ] ] [__DG_INFORM__ '
                           '[__ARG_TASK__ get_forecast ] '
                           '[__ARG_CLOUD_COVERAGE__ mostly sunny ] '
                           '[__ARG_DATE_TIME_RANGE__ [__ARG_COLLOQUIAL__ This '
                           'afternoon ] ] [__ARG_LOCATION__ [__ARG_CITY__ '
                           'Oakland ] [__ARG_COUNTRY__ United States ] '
                           '[__ARG_REGION__ California ] ] ]',
 'tree_str_mr': "[__DG_INFORM__ It's [__ARG_DATE_TIME__ [__ARG_COLLOQUIAL__ "
                'currently ] ] [__ARG_CLOUD_COVERAGE__ partly cloudy ] and '
                '[__ARG_TEMP__ __ARG_TEMP__ ] [__ARG_TEMP_UNIT__ '
                '__ARG_TEMP_UNIT__ ] [__ARG_LOCATION__ in [__ARG_CITY__ '
                '__ARG_CITY__ ] , [__ARG_REGION__ __ARG_REGION__ ] , '
                '[__ARG_COUNTRY__ __ARG_COUNTRY__ ] ] . ] [__DG_INFORM__ '
                '[__ARG_DATE_TIME_RANGE__ [__ARG_COLLOQUIAL__ This afternoon ] '
                "] , it'll be [__ARG_CLOUD_COVERAGE__ mostly sunny ] ] "
                '[__DG_INFORM__ with temperatures in the [__ARG_TEMP_SUMMARY__ '
                'mid <number>  ] ]',
 'user_query': 'Show weather forecast for Oakland, CA. '}
```

#### Data Splits

<!-- info: Describe and name the splits in the dataset if there are more than one. -->
<!-- scope: periscope -->
- Standard Splits: Train/Validation/Test
- Additional Split: Disc_Test (a more challenging subset of the test set that contains discourse relations) 

#### Splitting Criteria

<!-- info: Describe any criteria for splitting the data, if used. If there are differences between the splits (e.g., if the training annotations are machine-generated and the dev and test ones are created by humans, or if different numbers of annotators contributed to each example), describe them here. -->
<!-- scope: microscope -->
The test set contains 3,121 examples, of which 1.1K (35%) have unique MRs that have never been seen in the training set.

#### 

<!-- info: What does an outlier of the dataset in terms of length/perplexity/embedding look like? -->
<!-- scope: microscope -->
```
{'gem_id': 'weather-train-13333', 'data_id': '1260610', 'user_query': 'Sundown', 'tree_str_mr': '[__DG_INFORM__ [__ARG_TASK__ get_weather_attribute ] [__ARG_SUNSET_TIME_DATE_TIME__ [__ARG_TIME__ 05:04 PM ] ] ]', 'response': '[__DG_INFORM__ The sun will go down at [__ARG_SUNSET_TIME_DATE_TIME__ [__ARG_TIME__ __ARG_TIME__ ] ] ]'}
```



## Dataset in GEM

### Rationale for Inclusion in GEM

#### Why is the Dataset in GEM?

<!-- info: What does this dataset contribute toward better generation evaluation and why is it part of GEM? -->
<!-- scope: microscope -->
The dataset was curated to develop a weather bot that exhibits human-like properties such as matching the framing of the response with the query or contrasting relevant data attributes. 

The dataset offers rich tree-based meaning representations that offer fine-grained control over the response, e.g. by specifying which two attributes are to be contrasted.  The natural language input queries are also provided to model the coherence of the response based on the input.  The output response is annotated with the input meaning components using special bracketing tokens, which enables developing new techniques such as constrained decoding to improve quality of output responses

#### Similar Datasets

<!-- info: Do other datasets for the high level task exist? -->
<!-- scope: telescope -->
no

#### Ability that the Dataset measures

<!-- info: What aspect of model ability can be measured with this dataset? -->
<!-- scope: periscope -->
Adequately expressing CONTRAST and JUSTIFY discourse relations with appropriate grouping of arguments; adequately generalizing to many combinations of arguments.


### GEM-Specific Curation

#### Modificatied for GEM?

<!-- info: Has the GEM version of the dataset been modified in any way (data, processing, splits) from the original curated data? -->
<!-- scope: telescope -->
yes

#### GEM Modifications

<!-- info: What changes have been made to he original dataset? -->
<!-- scope: periscope -->
`data points removed`

#### Modification Details

<!-- info: For each of these changes, described them in more details and provided the intended purpose of the modification -->
<!-- scope: microscope -->
The original repo contained a challenge set disc_test.tsv, which is a subset of the test set consisting of discourse relations (CONTRAST and JUSTIFY) , but also contained JOIN relations.
This discrepancy has been rectified in the GEM version. The rectified version has been added in the `challenge_sets` 

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
Adequately expressing CONTRAST and JUSTIFY discourse relations with appropriate grouping of arguments; adequately generalizing to many combinations of arguments.

#### Metrics

<!-- info: What metrics are typically used for this task? -->
<!-- scope: periscope -->
`BLEU`, `Other: Other Metrics`

#### Other Metrics

<!-- info: Definitions of other metrics -->
<!-- scope: periscope -->
Tree accuracy:  It measures whether the tree structure in the prediction matches that of the input MR exactly (modulo repeated arguments that need only appear once).

#### Proposed Evaluation

<!-- info: List and describe the purpose of the metrics and evaluation methodology (including human evaluation) that the dataset creators used when introducing this task. -->
<!-- scope: microscope -->
Automatic metrics are evaluated on the raw model predictions (which have de-lexicalized fields):
* Tree accuracy: Measures whether the tree structure in the prediction matches that of the input MR exactly. 
* BLEU-4: A word overlap metric commonly used for evaluating NLG systems.

Authors also performed human evaluation studies by asking annotators to evaluate the quality of responses produced by different models. Annotators provided binary ratings on the following dimensions:
• Grammaticality: Measures fluency of the responses. 
• Correctness: Measures semantic correctness of the responses.

#### Previous results available?

<!-- info: Are previous results available? -->
<!-- scope: telescope -->
no



## Dataset Curation

### Original Curation

#### Original Curation Rationale

<!-- info: Original curation rationale -->
<!-- scope: telescope -->
The dataset was curated to develop a weather bot that exhibits human-like properties such as matching the framing of the response with the query or contrasting relevant data attributes. To achieve this, the dataset contains rich tree-structured meaning representations that are specified using several data arguments and discourse acts, the input natural language queries, and annotations for the responses. 

#### Communicative Goal

<!-- info: What was the communicative goal? -->
<!-- scope: periscope -->
Producing a text that is a response to a weather query as per the discourse structure and data attributes specified in the input meaning representation.

#### Sourced from Different Sources

<!-- info: Is the dataset aggregated from different data sources? -->
<!-- scope: telescope -->
no


### Language Data

#### How was Language Data Obtained?

<!-- info: How was the language data obtained? -->
<!-- scope: telescope -->
`Crowdsourced`, `Machine-generated`

#### Where was it crowdsourced?

<!-- info: If crowdsourced, where from? -->
<!-- scope: periscope -->
`Other crowdworker platform`

#### Topics Covered

<!-- info: Does the language in the dataset focus on specific topics? How would you describe them? -->
<!-- scope: periscope -->
The dataset is focused on the weather domain:  Weather was the first successful case of NLG put into production back in the 80s (Reiter & Dale, 1997). This domain offers significant complexity for NLG. Weather forecast summaries in particular can be very long, and require reasoning over several disjoint pieces of information.

#### Data Validation

<!-- info: Was the text validated by a different worker or a data curator? -->
<!-- scope: telescope -->
validated by crowdworker

#### Data Preprocessing

<!-- info: How was the text data pre-processed? (Enter N/A if the text was not pre-processed) -->
<!-- scope: microscope -->
Please refer to Appendix D of the original paper for details.

#### Was Data Filtered?

<!-- info: Were text instances selected or filtered? -->
<!-- scope: telescope -->
hybrid

#### Filter Criteria

<!-- info: What were the selection criteria? -->
<!-- scope: microscope -->
Please refer to Appendix C of the original paper for details.


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
Annotation was done as work for hire and contains no PII.


### Private Identifying Information (PII)

#### Contains PII?

<!-- quick -->
<!-- info: Does the source language data likely contain Personal Identifying Information about the data creators or subjects? -->
<!-- scope: telescope -->
no PII

#### Justification for no PII

<!-- info: Provide a justification for selecting `no PII` above. -->
<!-- scope: periscope -->
Data is simulated and not specific to annotator.


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
unsure

#### Are the Language Producers Representative of the Language?

<!-- info: Does the distribution of language producers in the dataset accurately represent the full distribution of speakers of the language world-wide? If not, how does it differ? -->
<!-- scope: periscope -->
Grammatical evaluations performed with the data to date have used norms from informal Standard American English. These prescriptive notions of grammaticality potentially serve to perpetuate systemic power imbalances as they’re conveyed by language. 

Since the data only contains informal Standard American English, its use to train a model may not be appropriate depending on the potential use case.



## Considerations for Using the Data

### PII Risks and Liability

#### Potential PII Risk

<!-- info: Considering your answers to the PII part of the Data Curation Section, describe any potential privacy to the data subjects and creators risks when using the dataset. -->
<!-- scope: microscope -->
Annotation was done as work for hire and contains no PII. Annotated data is simulated and not specific to annotator.



### Licenses



### Known Technical Limitations

#### Unsuited Applications

<!-- info: When using a model trained on this dataset in a setting where users or the public may interact with its predictions, what are some pitfalls to look out for? In particular, describe some applications of the general task featured in this dataset that its curation or properties make it less suitable for. -->
<!-- scope: microscope -->
An imperfect model used to convey actual weather data could mislead users about weather conditions?


