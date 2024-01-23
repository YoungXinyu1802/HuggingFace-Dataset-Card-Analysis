---
annotations_creators:
- none
language_creators:
- unknown
language:
- en
license:
- cc-by-4.0
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
pretty_name: cochrane-simplification
---

# Dataset Card for GEM/cochrane-simplification

## Dataset Description

- **Homepage:** https://github.com/AshOlogn/Paragraph-level-Simplification-of-Medical-Texts
- **Repository:** https://github.com/AshOlogn/Paragraph-level-Simplification-of-Medical-Texts
- **Paper:** https://aclanthology.org/2021.naacl-main.395/
- **Leaderboard:** N/A
- **Point of Contact:** Ashwin Devaraj

### Link to Main Data Card

You can find the main data card on the [GEM Website](https://gem-benchmark.com/data_cards/cochrane-simplification).

### Dataset Summary 

Cochrane is an English dataset for paragraph-level simplification of medical texts. Cochrane is a database of systematic reviews of clinical questions, many of which have summaries in plain English targeting readers without a university education. The dataset comprises about 4,500 of such pairs. 

You can load the dataset via:
```
import datasets
data = datasets.load_dataset('GEM/cochrane-simplification')
```
The data loader can be found [here](https://huggingface.co/datasets/GEM/cochrane-simplification).

#### website
[Link](https://github.com/AshOlogn/Paragraph-level-Simplification-of-Medical-Texts)

#### paper
[Link](https://aclanthology.org/2021.naacl-main.395/)

#### authors
Ashwin Devaraj (The University of Texas at Austin), Iain J. Marshall (King's College London), Byron C. Wallace (Northeastern University), Junyi Jessy Li (The University of Texas at Austin)

## Dataset Overview

### Where to find the Data and its Documentation

#### Webpage

<!-- info: What is the webpage for the dataset (if it exists)? -->
<!-- scope: telescope -->
[Link](https://github.com/AshOlogn/Paragraph-level-Simplification-of-Medical-Texts)

#### Download

<!-- info: What is the link to where the original dataset is hosted? -->
<!-- scope: telescope -->
[Link](https://github.com/AshOlogn/Paragraph-level-Simplification-of-Medical-Texts)

#### Paper

<!-- info: What is the link to the paper describing the dataset (open access preferred)? -->
<!-- scope: telescope -->
[Link](https://aclanthology.org/2021.naacl-main.395/)

#### BibTex

<!-- info: Provide the BibTex-formatted reference for the dataset. Please use the correct published version (ACL anthology, etc.) instead of google scholar created Bibtex. -->
<!-- scope: microscope -->
```
@inproceedings{devaraj-etal-2021-paragraph,
    title = "Paragraph-level Simplification of Medical Texts",
    author = "Devaraj, Ashwin  and
      Marshall, Iain  and
      Wallace, Byron  and
      Li, Junyi Jessy",
    booktitle = "Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies",
    month = jun,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.naacl-main.395",
    doi = "10.18653/v1/2021.naacl-main.395",
    pages = "4972--4984",
}
```

#### Contact Name

<!-- quick -->
<!-- info: If known, provide the name of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
Ashwin Devaraj

#### Contact Email

<!-- info: If known, provide the email of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
ashwin.devaraj@utexas.edu

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
cc-by-4.0: Creative Commons Attribution 4.0 International

#### Intended Use

<!-- info: What is the intended use of the dataset? -->
<!-- scope: microscope -->
The intended use of this dataset is to train models that simplify medical text at the paragraph level so that it may be more accessible to the lay reader.

#### Primary Task

<!-- info: What primary task does the dataset support? -->
<!-- scope: telescope -->
Simplification

#### Communicative Goal

<!-- quick -->
<!-- info: Provide a short description of the communicative goal of a model trained for this task on this dataset. -->
<!-- scope: periscope -->
A model trained on this dataset can be used to simplify medical texts to make them more accessible to readers without medical expertise.


### Credit

#### Curation Organization Type(s)

<!-- info: In what kind of organization did the dataset curation happen? -->
<!-- scope: telescope -->
`academic`

#### Curation Organization(s)

<!-- info: Name the organization(s). -->
<!-- scope: periscope -->
The University of Texas at Austin, King's College London, Northeastern University

#### Dataset Creators

<!-- info: Who created the original dataset? List the people involved in collecting the dataset and their affiliation(s). -->
<!-- scope: microscope -->
Ashwin Devaraj (The University of Texas at Austin), Iain J. Marshall (King's College London), Byron C. Wallace (Northeastern University), Junyi Jessy Li (The University of Texas at Austin)

#### Funding

<!-- info: Who funded the data creation? -->
<!-- scope: microscope -->
National Institutes of Health (NIH) grant R01-LM012086, National Science Foundation (NSF) grant IIS-1850153, Texas Advanced Computing Center (TACC) computational resources

#### Who added the Dataset to GEM?

<!-- info: Who contributed to the data card and adding the dataset to GEM? List the people+affiliations involved in creating this data card and who helped integrate this dataset into GEM. -->
<!-- scope: microscope -->
Ashwin Devaraj (The University of Texas at Austin)


### Dataset Structure

#### Data Fields

<!-- info: List and describe the fields present in the dataset. -->
<!-- scope: telescope -->
- `gem_id`: string, a unique identifier for the example
- `doi`: string, DOI identifier for the Cochrane review from which the example was generated
- `source`: string, an excerpt from an abstract of a Cochrane review
- `target`: string, an excerpt from the plain-language summary of a Cochrane review that roughly aligns with the source text

#### Example Instance

<!-- info: Provide a JSON formatted example of a typical instance in the dataset. -->
<!-- scope: periscope -->
```
{
    "gem_id": "gem-cochrane-simplification-train-766",
    "doi": "10.1002/14651858.CD002173.pub2",
    "source": "Of 3500 titles retrieved from the literature, 24 papers reporting on 23 studies could be included in the review. The studies were published between 1970 and 1997 and together included 1026 participants. Most were cross-over studies. Few studies provided sufficient information to judge the concealment of allocation. Four studies provided results for the percentage of symptom-free days. Pooling the results did not reveal a statistically significant difference between sodium cromoglycate and placebo. For the other pooled outcomes, most of the symptom-related outcomes and bronchodilator use showed statistically significant results, but treatment effects were small. Considering the confidence intervals of the outcome measures, a clinically relevant effect of sodium cromoglycate cannot be excluded. The funnel plot showed an under-representation of small studies with negative results, suggesting publication bias. There is insufficient evidence to be sure about the efficacy of sodium cromoglycate over placebo. Publication bias is likely to have overestimated the beneficial effects of sodium cromoglycate as maintenance therapy in childhood asthma.",
    "target": "In this review we aimed to determine whether there is evidence for the effectiveness of inhaled sodium cromoglycate as maintenance treatment in children with chronic asthma. Most of the studies were carried out in small groups of patients. Furthermore, we suspect that not all studies undertaken have been published. The results show that there is insufficient evidence to be sure about the beneficial effect of sodium cromoglycate compared to placebo. However, for several outcome measures the results favoured sodium cromoglycate."
}
```

#### Data Splits

<!-- info: Describe and name the splits in the dataset if there are more than one. -->
<!-- scope: periscope -->
- `train`: 3568 examples
- `validation`: 411 examples
- `test`: 480 examples



## Dataset in GEM

### Rationale for Inclusion in GEM

#### Why is the Dataset in GEM?

<!-- info: What does this dataset contribute toward better generation evaluation and why is it part of GEM? -->
<!-- scope: microscope -->
This dataset is the first paragraph-level simplification dataset published (as prior work had primarily focused on simplifying individual sentences). Furthermore, this dataset is in the medical domain, which is an especially useful domain for text simplification.

#### Similar Datasets

<!-- info: Do other datasets for the high level task exist? -->
<!-- scope: telescope -->
no

#### Ability that the Dataset measures

<!-- info: What aspect of model ability can be measured with this dataset? -->
<!-- scope: periscope -->
This dataset measures the ability for a model to simplify paragraphs of medical text through the omission non-salient information and simplification of medical jargon.


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




## Previous Results

### Previous Results

#### Measured Model Abilities

<!-- info: What aspect of model ability can be measured with this dataset? -->
<!-- scope: telescope -->
This dataset measures the ability for a model to simplify paragraphs of medical text through the omission non-salient information and simplification of medical jargon.

#### Metrics

<!-- info: What metrics are typically used for this task? -->
<!-- scope: periscope -->
`Other: Other Metrics`, `BLEU`

#### Other Metrics

<!-- info: Definitions of other metrics -->
<!-- scope: periscope -->
SARI  measures the quality of text simplification


#### Previous results available?

<!-- info: Are previous results available? -->
<!-- scope: telescope -->
yes

#### Relevant Previous Results

<!-- info: What are the most relevant previous results for this task/dataset? -->
<!-- scope: microscope -->
The paper which introduced this dataset trained BART models (pretrained on XSum) with unlikelihood training to produce  simplification models achieving maximum SARI and BLEU scores of 40 and 43 respectively.



## Dataset Curation

### Original Curation

#### Sourced from Different Sources

<!-- info: Is the dataset aggregated from different data sources? -->
<!-- scope: telescope -->
no


### Language Data

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
no


### Private Identifying Information (PII)

#### Contains PII?

<!-- quick -->
<!-- info: Does the source language data likely contain Personal Identifying Information about the data creators or subjects? -->
<!-- scope: telescope -->
yes/very likely

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
This dataset can be used to simplify medical texts that may otherwise be inaccessible to those without medical training.


### Discussion of Biases

#### Any Documented Social Biases?

<!-- info: Are there documented social biases in the dataset? Biases in this context are variations in the ways members of different social categories are represented that can have harmful downstream consequences for members of the more disadvantaged group. -->
<!-- scope: telescope -->
unsure

#### Are the Language Producers Representative of the Language?

<!-- info: Does the distribution of language producers in the dataset accurately represent the full distribution of speakers of the language world-wide? If not, how does it differ? -->
<!-- scope: periscope -->
The dataset was generated from abstracts and plain-language summaries of medical literature reviews that were written by medical professionals and thus does was not generated by people representative of the entire English-speaking population.



## Considerations for Using the Data

### PII Risks and Liability



### Licenses



### Known Technical Limitations

#### Technical Limitations

<!-- info: Describe any known technical limitations, such as spurrious correlations, train/test overlap, annotation biases, or mis-annotations, and cite the works that first identified these limitations when possible. -->
<!-- scope: microscope -->
The main limitation of this dataset is that the information alignment between the abstract and plain-language summary is often rough, so the plain-language summary may contain information that isn't found in the abstract. Furthermore, the plain-language targets often contain formulaic statements like "this evidence is current to [month][year]" not found in the abstracts. Another limitation is that some plain-language summaries do not simplify the technical abstracts very much and still contain medical jargon. 

#### Unsuited Applications

<!-- info: When using a model trained on this dataset in a setting where users or the public may interact with its predictions, what are some pitfalls to look out for? In particular, describe some applications of the general task featured in this dataset that its curation or properties make it less suitable for. -->
<!-- scope: microscope -->
The main pitfall to look out for is errors in factuality. Simplification work so far has not placed a strong emphasis on the logical fidelity of model generations with the input text, and the paper introducing this dataset does not explore modeling techniques to combat this.  These kinds of errors are especially pernicious in the medical domain, and the models introduced in the paper do occasionally alter entities like disease and medication names.


