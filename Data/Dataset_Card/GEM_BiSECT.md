---
annotations_creators:
- none
language_creators:
- unknown
language:
- de
- en
- fr
- es
license:
- other
multilinguality:
- unknown
pretty_name: BiSECT
size_categories:
- unknown
source_datasets:
- original
task_categories:
- simplification
task_ids:
- unknown
---

# Dataset Card for GEM/BiSECT

## Dataset Description

- **Homepage:** https://github.com/mounicam/BiSECT
- **Repository:** https://github.com/mounicam/BiSECT/tree/main/bisect
- **Paper:** https://aclanthology.org/2021.emnlp-main.500/
- **Leaderboard:** N/A
- **Point of Contact:** Joongwon Kim, Mounica Maddela, Reno Kriz

### Link to Main Data Card

You can find the main data card on the [GEM Website](https://gem-benchmark.com/data_cards/BiSECT).

### Dataset Summary 

This dataset is composed of 1 million complex sentences with the task to split and simplify them while retaining the full meaning. Compared to other simplification corpora, BiSECT requires more significant edits. BiSECT offers splits in English, German, French, and Spanish.

You can load the dataset via:
```
import datasets
data = datasets.load_dataset('GEM/BiSECT')
```
The data loader can be found [here](https://huggingface.co/datasets/GEM/BiSECT).

#### website
[Link](https://github.com/mounicam/BiSECT)

#### paper
[Link](https://aclanthology.org/2021.emnlp-main.500/)

## Dataset Overview

### Where to find the Data and its Documentation

#### Webpage

<!-- info: What is the webpage for the dataset (if it exists)? -->
<!-- scope: telescope -->
[Link](https://github.com/mounicam/BiSECT)

#### Download

<!-- info: What is the link to where the original dataset is hosted? -->
<!-- scope: telescope -->
[Link](https://github.com/mounicam/BiSECT/tree/main/bisect)

#### Paper

<!-- info: What is the link to the paper describing the dataset (open access preferred)? -->
<!-- scope: telescope -->
[Link](https://aclanthology.org/2021.emnlp-main.500/)

#### BibTex

<!-- info: Provide the BibTex-formatted reference for the dataset. Please use the correct published version (ACL anthology, etc.) instead of google scholar created Bibtex. -->
<!-- scope: microscope -->
```
@inproceedings{kim-etal-2021-bisect,
    title = "{B}i{SECT}: Learning to Split and Rephrase Sentences with Bitexts",
    author = "Kim, Joongwon  and
      Maddela, Mounica  and
      Kriz, Reno  and
      Xu, Wei  and
      Callison-Burch, Chris",
    booktitle = "Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing",
    month = nov,
    year = "2021",
    address = "Online and Punta Cana, Dominican Republic",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.emnlp-main.500",
    pages = "6193--6209"
}
```

#### Contact Name

<!-- quick -->
<!-- info: If known, provide the name of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
Joongwon Kim, Mounica Maddela, Reno Kriz

#### Contact Email

<!-- info: If known, provide the email of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
jkim0118@seas.upenn.edu, mmaddela3@gatech.edu, rkriz1@jh.edu

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
`English`, `German`, `French`, `Spanish, Castilian`

#### License

<!-- quick -->
<!-- info: What is the license of the dataset? -->
<!-- scope: telescope -->
other: Other license

#### Intended Use

<!-- info: What is the intended use of the dataset? -->
<!-- scope: microscope -->
Split and Rephrase.

#### Add. License Info

<!-- info: What is the 'other' license of the dataset? -->
<!-- scope: periscope -->
The dataset is not licensed by itself, and the source OPUS data consists solely of publicly available parallel corpora.

#### Primary Task

<!-- info: What primary task does the dataset support? -->
<!-- scope: telescope -->
Simplification

#### Communicative Goal

<!-- quick -->
<!-- info: Provide a short description of the communicative goal of a model trained for this task on this dataset. -->
<!-- scope: periscope -->
To rewrite a long, complex sentence into shorter, readable, meaning-equivalent sentences.


### Credit



### Dataset Structure

#### Data Fields

<!-- info: List and describe the fields present in the dataset. -->
<!-- scope: telescope -->
- `gem_id` (string): a unique identifier for the instance
- `source_sentence` (string): sentence to be simplified
- `target_sentence` (string)" simplified text that was split and rephrased

#### Example Instance

<!-- info: Provide a JSON formatted example of a typical instance in the dataset. -->
<!-- scope: periscope -->
```
{
   "gem_id": "bisect-train-0",
   "source_sentence": "The report on the visit to Bhutan states that the small community has made the task of coordination less complex and success is manifested in the synchronized programming cycles which now apply to all but one of the agencies ( the World Health Organization ) .",
   "target_sentence": "The report on the visit to Bhutan says that the small community has made the coordination work less complex . Success manifests itself in synchronized programming cycles that now apply to all but one organism ( the World Health Organization ) ."
}
```

#### Data Splits

<!-- info: Describe and name the splits in the dataset if there are more than one. -->
<!-- scope: periscope -->
For the main English BiSECT dataset, the splits are as follows: 1. Train (n=928440) 2. Validation (n=9079) 3. Test (n=583) Additional challenge sets were derived from the data presented in the paper. Please refer to the challenge set sections. The train/validation/test splits for other languages are as follows: German (n=184638/n=864/n=735) Spanish (n=282944/n=3638/n=3081) French (n=491035/n=2400/n=1036)

#### Splitting Criteria

<!-- info: Describe any criteria for splitting the data, if used. If there are differences between the splits (e.g., if the training annotations are machine-generated and the dev and test ones are created by humans, or if different numbers of annotators contributed to each example), describe them here. -->
<!-- scope: microscope -->
While all training data were derived from subsets of the OPUS corpora, different source subsets were used for training v.s., validation and testing. The training set comprised more web crawl data, whereas development and test sets comprised EMEA and EU texts. Details can be found in the BiSECT paper.



## Dataset in GEM

### Rationale for Inclusion in GEM

#### Why is the Dataset in GEM?

<!-- info: What does this dataset contribute toward better generation evaluation and why is it part of GEM? -->
<!-- scope: microscope -->
Understanding long and complex sentences is challenging for both humans and NLP models. The BiSECT dataset helps facilitate more research on Split and Rephrase as a task within itself, as well as how it can benefit downstream NLP applications.

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
BiSECT is the largest available corpora for the Split and Rephrase task. In addition, it has been shown that BiSECT is of higher quality than previous Split and Rephrase corpora and contains a wider variety of splitting operations.

Most previous Split and Rephrase corpora (HSplit-Wiki, Cont-Benchmark, and Wiki-Benchmark) were manually written at a small scale and focused on evaluation, while the one corpus of comparable size, WikiSplit, contains around 25% of pairs contain significant errors. This is because Wikipedia editors are not only trying to split a sentence, but also often simultaneously modifying the sentence for other purposes, which results in changes of the initial meaning.


### GEM-Specific Curation

#### Modificatied for GEM?

<!-- info: Has the GEM version of the dataset been modified in any way (data, processing, splits) from the original curated data? -->
<!-- scope: telescope -->
yes

#### GEM Modifications

<!-- info: What changes have been made to he original dataset? -->
<!-- scope: periscope -->
`data points added`

#### Modification Details

<!-- info: For each of these changes, described them in more details and provided the intended purpose of the modification -->
<!-- scope: microscope -->
The original BiSECT training, validation, and test splits are maintained to ensure a fair comparison. Note that the original BiSECT test set was created by manually selecting 583 high-quality Split and Rephrase instances from 1000 random source-target pairs sampled from the EMEA and JRC-Acquis corpora from OPUS.

As the first challenge set, we include the HSPLIT-Wiki test set, containing 359 pairs. For each complex sentence, there are four reference splits; To ensure replicability, as reference splits, we again follow the BiSECT paper and present only the references from HSplit2-full.

In addition to the two evaluation sets used in the original BiSECT paper, we also introduce a second challenge set. For this, we initially consider all 7,293 pairs from the EMEA and JRC-Acquis corpora. From there, we classify each pair using the classification algorithm from Section 4.2 of the original BiSECT paper. The three classes are as follows:

1. Direct Insertion: when a long sentence l contains two independent clauses and requires only minor changes in order to make a fluent and meaning-preserving split s.
2. Changes near Split, when l contains one independent and one dependent clause, but modifications are restricted to the region where l is split.
3. Changes across Sentences, where major changes are required throughout l in order to create a fluent split s.
We keep only pairs labeled as Type 3, and after filtering out pairs with significant length differences (signaling potential content addition/deletion), we present a second challenge set of 1,798 pairs.

#### Additional Splits?

<!-- info: Does GEM provide additional splits to the dataset? -->
<!-- scope: telescope -->
no


### Getting Started with the Task

#### Pointers to Resources

<!-- info: Getting started with in-depth research on the task. Add relevant pointers to resources that researchers can consult when they want to get started digging deeper into the task. -->
<!-- scope: microscope -->
The dataset can be downloaded from the original repository by the authors.

The original BiSECT paper proposes several transformer-based models that can be used as baselines, which also compares against Copy512, an LSTM-based model and the previous state-of-the-art.

The common metric used for automatic evaluation of Split and Rephrase, and sentence simplification more generally is SARI. The BiSECT paper also evaluates using BERTScore. Note that automatic evaluations tend to not correlate well with human judgments, so a human evaluation for quality is generally expected for publication. The original BiSECT paper provides templates for collecting quality annotations from Amazon Mechanical Turk.



## Previous Results

### Previous Results

#### Measured Model Abilities

<!-- info: What aspect of model ability can be measured with this dataset? -->
<!-- scope: telescope -->
Text comprehension (needed to generate meaning-equivalent output) and notions of complexity (what is more 'readable' in terms of syntactic structure, lexical choice, punctuation).

#### Metrics

<!-- info: What metrics are typically used for this task? -->
<!-- scope: periscope -->
`Other: Other Metrics`, `BERT-Score`

#### Other Metrics

<!-- info: Definitions of other metrics -->
<!-- scope: periscope -->
SARI is a metric used for evaluating automatic text simplification systems. The metric compares the predicted simplified sentences against the reference and the source sentences. It explicitly measures the goodness of words that are added, deleted and kept by the system. 

#### Proposed Evaluation

<!-- info: List and describe the purpose of the metrics and evaluation methodology (including human evaluation) that the dataset creators used when introducing this task. -->
<!-- scope: microscope -->
Existing automatic metrics, such as BLEU (Papineni et al., 2002) and SAMSA (Sulem et al., 2018),
are not optimal for the Split and Rephrase task as
they rely on lexical overlap between the output and
the target (or source) and underestimate the splitting capability of the models that rephrase often. 

As such, the dataset creators focused on BERTScore (Zhang et al., 2020) and SARI (Xu et al., 2016). BERTScore captures meaning preservation and fluency
well (Scialom et al., 2021). SARI can provide three
separate F1/precision scores that explicitly measure the correctness of inserted, kept and deleted
n-grams when compared to both the source and
the target. The authors used an extended version of SARI
that considers lexical paraphrases of the reference. 

#### Previous results available?

<!-- info: Are previous results available? -->
<!-- scope: telescope -->
yes



## Dataset Curation

### Original Curation

#### Original Curation Rationale

<!-- info: Original curation rationale -->
<!-- scope: telescope -->
BiSECT was constructed to satisfy the need of a Split and Rephrase corpus that is both large-scale and high-quality. Most previous Split and Rephrase corpora (HSplit-Wiki, Cont-Benchmark, and Wiki-Benchmark) were manually written at a small scale and focused on evaluation, while the one corpus of comparable size, WikiSplit, contains around 25% of pairs contain significant errors. This is because Wikipedia editors are not only trying to split a sentence, but also often simultaneously modifying the sentence for other purposes, which results in changes of the initial meaning.

#### Communicative Goal

<!-- info: What was the communicative goal? -->
<!-- scope: periscope -->
The goal of Split and Rephrase is to break down longer sentences into multiple shorter sentences, which has downstream applications for many NLP tasks, including machine translation and dependency parsing.

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
`Other`

#### Language Producers

<!-- info: What further information do we have on the language producers? -->
<!-- scope: microscope -->
N/A.

#### Topics Covered

<!-- info: Does the language in the dataset focus on specific topics? How would you describe them? -->
<!-- scope: periscope -->
There is a range of topics spanning domains such as web crawl and government documents (European Parliament, United Nations, EMEA).

#### Data Validation

<!-- info: Was the text validated by a different worker or a data curator? -->
<!-- scope: telescope -->
validated by data curator

#### Data Preprocessing

<!-- info: How was the text data pre-processed? (Enter N/A if the text was not pre-processed) -->
<!-- scope: microscope -->
The construction of the BiSECT corpus relies on leveraging the sentence-level alignments from OPUS), a collection of bilingual parallel corpora over many language pairs. Given a target language A, this work extracts all 1-2 and 2-1 sentence alignments from parallel corpora between A and a set of foreign languages B.

Next, the foreign sentences are translated into English using Google Translate’s Web API service to obtain sentence alignments between a single long sentence and two corresponding split sentences, both in the desired language.

The authors further filtered the data in a hybrid fashion.

#### Was Data Filtered?

<!-- info: Were text instances selected or filtered? -->
<!-- scope: telescope -->
hybrid

#### Filter Criteria

<!-- info: What were the selection criteria? -->
<!-- scope: microscope -->
To remove noise, the authors remove pairs where the single long sentence (l) contains a token with a punctuation after the first two and before the last two alphabetic characters. The authors also removed instances where l contains more than one unconnected component in its dependency tree, generated via SpaCy.


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
Since this data is collected from OPUS, all instances are already in the public domain. 


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
yes

#### Details on how Dataset Addresses the Needs

<!-- info: Describe how this dataset addresses the needs of underserved communities. -->
<!-- scope: microscope -->
The data as provided in GEMv2 is in English, which is a language with abundant existing resources. However, the original paper also provides Split and Rephrase pairs for French, Spanish, and German, while providing a framework for leveraging bilingual corpora from any language pair found within OPUS.


### Discussion of Biases

#### Any Documented Social Biases?

<!-- info: Are there documented social biases in the dataset? Biases in this context are variations in the ways members of different social categories are represented that can have harmful downstream consequences for members of the more disadvantaged group. -->
<!-- scope: telescope -->
no

#### Are the Language Producers Representative of the Language?

<!-- info: Does the distribution of language producers in the dataset accurately represent the full distribution of speakers of the language world-wide? If not, how does it differ? -->
<!-- scope: periscope -->
The language produced in the dataset is limited to what is captured in the used subset of the OPUS corpora, which might not represent the full distribution of speakers from all locations. For example, the corpora used are from a limited set of relatively formal domains, so it is possible that high performance on the BiSECT test set may not transfer to more informal text.



## Considerations for Using the Data

### PII Risks and Liability

#### Potential PII Risk

<!-- info: Considering your answers to the PII part of the Data Curation Section, describe any potential privacy to the data subjects and creators risks when using the dataset. -->
<!-- scope: microscope -->
Since this data is collected from OPUS, all pairs are already in the public domain.


### Licenses

#### Copyright Restrictions on the Dataset

<!-- info: Based on your answers in the Intended Use part of the Data Overview Section, which of the following best describe the copyright and licensing status of the dataset? -->
<!-- scope: periscope -->
`public domain`

#### Copyright Restrictions on the Language Data

<!-- info: Based on your answers in the Language part of the Data Curation Section, which of the following best describe the copyright and licensing status of the underlying language data? -->
<!-- scope: periscope -->
`public domain`


### Known Technical Limitations

#### Technical Limitations

<!-- info: Describe any known technical limitations, such as spurrious correlations, train/test overlap, annotation biases, or mis-annotations, and cite the works that first identified these limitations when possible. -->
<!-- scope: microscope -->
The creation of English BiSECT relies on translating non-English text back to English. While machine translation systems tend to perform well on high-resource languages, there is still a non-negligible chance that there these systems make errors; through a manual evaluation of a subset of BiSECT, it was found that 15% of pairs contained significant errors, while an additional 22% contained minor adequacy/fluency errors. This problem is exacerbated slightly when creating German BiSECT (22% significant errors, 24% minor errors), and these numbers would likely get larger if lower-resource languages were used.


