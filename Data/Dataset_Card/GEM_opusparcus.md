---
annotations_creators:
- expert-created
language_creators:
- unknown
language:
- de
- en
- fi
- fr
- ru
- sv
license:
- cc-by-nc-4.0
multilinguality:
- unknown
size_categories:
- unknown
source_datasets:
- original
task_categories:
- other
task_ids: []
pretty_name: opusparcus
tags:
- paraphrasing
---

# Dataset Card for GEM/opusparcus

## Dataset Description

- **Homepage:** http://urn.fi/urn:nbn:fi:lb-2018021221
- **Repository:** http://urn.fi/urn:nbn:fi:lb-2018021221
- **Paper:** http://www.lrec-conf.org/proceedings/lrec2018/pdf/131.pdf
- **Leaderboard:** N/A
- **Point of Contact:** Mathias Creutz

### Link to Main Data Card

You can find the main data card on the [GEM Website](https://gem-benchmark.com/data_cards/opusparcus).

### Dataset Summary 

Opusparcus is a paraphrase corpus for six European language: German, English, Finnish, French, Russian, and Swedish. The paraphrases consist of subtitles from movies and TV shows.

You can load the dataset via:
```
import datasets
data = datasets.load_dataset('GEM/opusparcus')
```
The data loader can be found [here](https://huggingface.co/datasets/GEM/opusparcus).

#### website
[Website](http://urn.fi/urn:nbn:fi:lb-2018021221)

#### paper
[LREC](http://www.lrec-conf.org/proceedings/lrec2018/pdf/131.pdf)

## Dataset Overview

### Where to find the Data and its Documentation

#### Webpage

<!-- info: What is the webpage for the dataset (if it exists)? -->
<!-- scope: telescope -->
[Website](http://urn.fi/urn:nbn:fi:lb-2018021221)

#### Download

<!-- info: What is the link to where the original dataset is hosted? -->
<!-- scope: telescope -->
[Website](http://urn.fi/urn:nbn:fi:lb-2018021221)

#### Paper

<!-- info: What is the link to the paper describing the dataset (open access preferred)? -->
<!-- scope: telescope -->
[LREC](http://www.lrec-conf.org/proceedings/lrec2018/pdf/131.pdf)

#### BibTex

<!-- info: Provide the BibTex-formatted reference for the dataset. Please use the correct published version (ACL anthology, etc.) instead of google scholar created Bibtex. -->
<!-- scope: microscope -->
```
@InProceedings{creutz:lrec2018,
  title = {Open Subtitles Paraphrase Corpus for Six Languages},
  author={Mathias Creutz},
  booktitle={Proceedings of the 11th edition of the Language Resources and Evaluation Conference (LREC 2018)},
  year={2018},
  month = {May 7-12},
  address = {Miyazaki, Japan},
  editor = {Nicoletta Calzolari (Conference chair) and Khalid Choukri and Christopher Cieri and Thierry Declerck and Sara Goggi and Koiti Hasida and Hitoshi Isahara and Bente Maegaard and Joseph Mariani and Hélène Mazo and Asuncion Moreno and Jan Odijk and Stelios Piperidis and Takenobu Tokunaga},
  publisher = {European Language Resources Association (ELRA)},
  isbn = {979-10-95546-00-9},
  language = {english},
  url={http://www.lrec-conf.org/proceedings/lrec2018/pdf/131.pdf}
```

#### Contact Name

<!-- quick -->
<!-- info: If known, provide the name of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
Mathias Creutz

#### Contact Email

<!-- info: If known, provide the email of at least one person the reader can contact for questions about the dataset. -->
<!-- scope: periscope -->
firstname dot lastname at helsinki dot fi

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
`German`, `English`, `Finnish`, `French`, `Russian`, `Swedish`

#### Whose Language?

<!-- info: Whose language is in the dataset? -->
<!-- scope: periscope -->
Opusparcus is a paraphrase corpus for six European language: German, English, Finnish, French, Russian, and Swedish. The paraphrases consist of subtitles from movies and TV shows.

The data in Opusparcus has been extracted from [OpenSubtitles2016](http://opus.nlpl.eu/OpenSubtitles2016.php), which is in turn based on data from [OpenSubtitles](http://www.opensubtitles.org/).

#### License

<!-- quick -->
<!-- info: What is the license of the dataset? -->
<!-- scope: telescope -->
cc-by-nc-4.0: Creative Commons Attribution Non Commercial 4.0 International

#### Intended Use

<!-- info: What is the intended use of the dataset? -->
<!-- scope: microscope -->
Opusparcus is a sentential paraphrase corpus for multiple languages containing colloquial language.

#### Primary Task

<!-- info: What primary task does the dataset support? -->
<!-- scope: telescope -->
Paraphrasing

#### Communicative Goal

<!-- quick -->
<!-- info: Provide a short description of the communicative goal of a model trained for this task on this dataset. -->
<!-- scope: periscope -->
Models can be trained, e.g., for paraphrase detection and generation, that is, determining whether two given sentences mean the same thing or generating new paraphrases for a given sentence. 


### Credit

#### Who added the Dataset to GEM?

<!-- info: Who contributed to the data card and adding the dataset to GEM? List the people+affiliations involved in creating this data card and who helped integrate this dataset into GEM. -->
<!-- scope: microscope -->
Mathias Creutz (University of Helsinki)


### Dataset Structure

#### Data Fields

<!-- info: List and describe the fields present in the dataset. -->
<!-- scope: telescope -->
- `sent1`: a tokenized sentence
- `sent2`: another tokenized sentence, which is potentially a paraphrase of `sent1`.
- `annot_score`: a value between 1.0 and 4.0 indicating how good an example of paraphrases `sent1` and `sent2` are. (For the training sets, the value is 0.0, which indicates that no manual annotation has taken place.)
- `lang`: language of this dataset
- `gem_id`: unique identifier of this entry

All fields are strings except `annot_score`, which is a float.

#### Reason for Structure

<!-- info: How was the dataset structure determined? -->
<!-- scope: microscope -->
For each target language, the Opusparcus data have been partitioned into three types of data sets: training, validation and test sets. The training sets are large, consisting of millions of sentence pairs, and have been compiled automatically, with the help of probabilistic ranking functions. The development and test sets consist of sentence pairs that have been annotated manually; each set contains approximately 1000 sentence pairs that have been verified to be acceptable paraphrases by two independent annotators.

When you download Opusparcus, you must always indicate the language you want to retrieve, for instance:

```
data = load_dataset("GEM/opusparcus", lang="de")
```

The above command will download the validation and test sets for German. If additionally, you want to retrieve training data, you need to specify the level of quality you desire, such as "French, with 90% quality of the training data":

```
data = load_dataset("GEM/opusparcus", lang="fr", quality=90)
```

The entries in the training sets have been ranked automatically by how likely they are paraphrases, best first, worst last. The quality parameter indicates the estimated proportion (in percent) of true
paraphrases in the training set. Allowed quality values range between 60 and 100, in increments of 5 (60, 65, 70, ..., 100). A value of 60 means that 60% of the sentence pairs in the training set are estimated to be true paraphrases (and the remaining 40% are not). A higher value produces a smaller but cleaner set. The smaller sets are subsets of the larger sets, such that the `quality=95` set is a subset of `quality=90`, which is a subset of `quality=85`, and so on.

The default `quality` value, if omitted, is 100. This matches no training data at all, which can be convenient, if you are only interested in the validation and test sets, which are considerably
smaller, but manually annotated.

Note that an alternative to typing the parameter values explicitly, you can use configuration names instead. The following commands are equivalent to the ones above:

```
data = load_dataset("GEM/opusparcus", "de.100")
data = load_dataset("GEM/opusparcus", "fr.90")
```

#### How were labels chosen?

<!-- info: How were the labels chosen? -->
<!-- scope: microscope -->
Annotators have used the following scores to label sentence pairs in the test and validation sets:

4: Good example of paraphrases (Dark green button in the annotation tool): The two sentences can be used in the same situation and essentially "mean the same thing".

3: Mostly good example of paraphrases (Light green button in the annotation tool): It is acceptable to think that the two sentences refer to the same thing, although one sentence might be more specific
than the other one, or there are differences in style, such as polite form versus familiar form.

2: Mostly bad example of paraphrases (Yellow button in the annotation tool): There is some connection between the sentences that explains why they occur together, but one would not really consider them to mean the same thing.

1: Bad example of paraphrases (Red button in the annotation tool): There is no obvious connection. The sentences mean different things.

If the two annotators fully agreed on the category, the value in the `annot_score` field is 4.0, 3.0, 2.0 or 1.0.  If the two annotators chose adjacent categories, the value in this field will be 3.5, 2.5 or
1.5.  For instance, a value of 2.5 means that one annotator gave a score of 3 ("mostly good"), indicating a possible paraphrase pair, whereas the other annotator scored this as a 2 ("mostly bad"), that is, unlikely to be a paraphrase pair.  If the annotators disagreed by more than one category, the sentence pair was discarded and won't show up in the datasets.

The training sets were not annotated manually. This is indicated by
the value 0.0 in the `annot_score` field.

For an assessment of of inter-annotator agreement, see Aulamo et al. (2019). [Annotation of subtitle paraphrases using a new web tool.](http://ceur-ws.org/Vol-2364/3_paper.pdf) In *Proceedings of the
Digital Humanities in the Nordic Countries 4th Conference*, Copenhagen, Denmark.

#### Example Instance

<!-- info: Provide a JSON formatted example of a typical instance in the dataset. -->
<!-- scope: periscope -->
```
{'annot_score': 4.0, 'gem_id': 'gem-opusparcus-test-1587', 'lang': 'en', 'sent1': "I haven 't been contacted by anybody .", 'sent2': "Nobody 's contacted me ."}
```

#### Data Splits

<!-- info: Describe and name the splits in the dataset if there are more than one. -->
<!-- scope: periscope -->
The data is split into training, validation and test sets. The validation and test sets come in two versions, the regular validation and test sets and the full sets, called validation.full and test.full. The full sets contain all sentence pairs successfully annotated by the annotators, including the sentence pairs that were rejected as paraphrases. The annotation scores of the full sets thus range between 1.0 and 4.0. The regular validation and test sets only contain sentence pairs that qualify as paraphrases, scored between 3.0 and 4.0 by the annotators.

The number of sentence pairs in the data splits are as follows for each of the languages. The range between the smallest (`quality=95`) and largest (`quality=60`) train configuration have been shown.

|       | train         | valid | test | valid.full | test.full |
| ----- | ------        | ----- | ---- | ---------- | --------- |
| de    | 0.59M .. 13M  |  1013 | 1047 |       1582 |      1586 |
| en    |  1.0M .. 35M  |  1015 |  982 |       1455 |      1445 |
| fi    | 0.48M .. 8.9M |   963 |  958 |       1760 |      1749 |
| fr    | 0.94M .. 22M  |   997 | 1007 |       1630 |      1674 |
| ru    | 0.15M .. 15M  |  1020 | 1068 |       1854 |      1855 |
| sv    | 0.24M .. 4.5M |   984 |  947 |       1887 |      1901 |

As a concrete example, loading the English data requesting 95% quality of the train split produces the following:

```
>>> data = load_dataset("GEM/opusparcus", lang="en", quality=95)

>>> data
DatasetDict({
    test: Dataset({
        features: ['lang', 'sent1', 'sent2', 'annot_score', 'gem_id'],
        num_rows: 982
    })
    validation: Dataset({
        features: ['lang', 'sent1', 'sent2', 'annot_score', 'gem_id'],
        num_rows: 1015
    })
    test.full: Dataset({
        features: ['lang', 'sent1', 'sent2', 'annot_score', 'gem_id'],
        num_rows: 1445
    })
    validation.full: Dataset({
        features: ['lang', 'sent1', 'sent2', 'annot_score', 'gem_id'],
        num_rows: 1455
    })
    train: Dataset({
        features: ['lang', 'sent1', 'sent2', 'annot_score', 'gem_id'],
        num_rows: 1000000
    })
})

>>> data["test"][0]
{'annot_score': 4.0, 'gem_id': 'gem-opusparcus-test-1587', 'lang': 'en', 'sent1': "I haven 't been contacted by anybody .", 'sent2': "Nobody 's contacted me ."}

>>> data["validation"][2]
{'annot_score': 3.0, 'gem_id': 'gem-opusparcus-validation-1586', 'lang': 'en', 'sent1': 'No promises , okay ?', 'sent2': "I 'm not promising anything ."}

>>> data["train"][1000]
{'annot_score': 0.0, 'gem_id': 'gem-opusparcus-train-12501001', 'lang': 'en', 'sent1': 'Am I beautiful ?', 'sent2': 'Am I pretty ?'}

#### Splitting Criteria

<!-- info: Describe any criteria for splitting the data, if used. If there are differences between the splits (e.g., if the training annotations are machine-generated and the dev and test ones are created by humans, or if different numbers of annotators contributed to each example), describe them here. -->
<!-- scope: microscope -->
The validation and test sets have been annotated manually, but the training sets have been produced using automatic scoring and come in different size configurations depending on the desired quality level. (See above descriptions and examples for more details.)

Please note that previous work suggests that a larger and noisier training set is better than a
smaller and clean set. See Sjöblom et al. (2018). [Paraphrase Detection on Noisy Subtitles in Six
Languages](http://noisy-text.github.io/2018/pdf/W-NUT20189.pdf). In *Proceedings of the 2018 EMNLP Workshop W-NUT: The 4th Workshop on Noisy User-generated Text*, and Vahtola et al. (2021). [Coping with Noisy Training Data Labels in Paraphrase Detection](https://aclanthology.org/2021.wnut-1.32/). In *Proceedings of the 7th Workshop on Noisy User-generated Text*.




## Dataset in GEM

### Rationale for Inclusion in GEM

#### Why is the Dataset in GEM?

<!-- info: What does this dataset contribute toward better generation evaluation and why is it part of GEM? -->
<!-- scope: microscope -->
Opusparcus provides examples of sentences that mean the same thing or have very similar meaning. Sentences are available in six languages and the style is colloquial language.

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
There is another data set containing manually labeled Finnish paraphrases.

#### Ability that the Dataset measures

<!-- info: What aspect of model ability can be measured with this dataset? -->
<!-- scope: periscope -->
Sentence meaning


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
Training sets have been prepared for each the "quality levels" 60% – 95%.

In the original release, this task was left to the user of the data.

#### Additional Splits?

<!-- info: Does GEM provide additional splits to the dataset? -->
<!-- scope: telescope -->
yes

#### Split Information

<!-- info: Describe how the new splits were created -->
<!-- scope: periscope -->
There are two versions of the validations and test sets: the regular sets which only contain positive examples of paraphrases and the full sets containing all examples.

#### Split Motivation

<!-- info: What aspects of the model's generation capacities were the splits created to test? -->
<!-- scope: periscope -->
In the original release, only the full validation and test sets were supplied. The "regular sets" have been added in order to make it easier to test on true parapahrases only. 


### Getting Started with the Task

#### Pointers to Resources

<!-- info: Getting started with in-depth research on the task. Add relevant pointers to resources that researchers can consult when they want to get started digging deeper into the task. -->
<!-- scope: microscope -->
Creutz (2018). [Open Subtitles Paraphrase Corpus for Six Languages](http://www.lrec-conf.org/proceedings/lrec2018/pdf/131.pdf), Proceedings of the 11th edition of the Language Resources and Evaluation Conference (LREC 2018).

Sjöblom et al. (2018). [Paraphrase Detection on Noisy Subtitles in Six Languages](http://noisy-text.github.io/2018/pdf/W-NUT20189.pdf). In Proceedings of the 2018 EMNLP Workshop W-NUT: The 4th Workshop on Noisy User-generated Text.

Aulamo et al. (2019). [Annotation of subtitle paraphrases using a new web tool.](http://ceur-ws.org/Vol-2364/3_paper.pdf) In Proceedings of the Digital Humanities in the Nordic Countries 4th Conference.

Sjöblom et al. (2020). [Paraphrase Generation and Evaluation on Colloquial-Style Sentences](https://aclanthology.org/2020.lrec-1.224/), Proceedings of the 12th Language Resources and Evaluation Conference (LREC). 

Vahtola et al. (2021). [Coping with Noisy Training Data Labels in Paraphrase Detection](https://aclanthology.org/2021.wnut-1.32/). In Proceedings of the 7th Workshop on Noisy User-generated Text.




## Previous Results

### Previous Results

#### Measured Model Abilities

<!-- info: What aspect of model ability can be measured with this dataset? -->
<!-- scope: telescope -->
Sentence meaning

In a scenario of paraphrase detection, the model determines whether two given sentences carry approximately the same meaning.

In a scenario of paraphrase generation, the model generates a potential paraphrase of a given sentence.

#### Metrics

<!-- info: What metrics are typically used for this task? -->
<!-- scope: periscope -->
`BLEU`, `BERT-Score`, `Other: Other Metrics`

#### Other Metrics

<!-- info: Definitions of other metrics -->
<!-- scope: periscope -->
PINC

#### Proposed Evaluation

<!-- info: List and describe the purpose of the metrics and evaluation methodology (including human evaluation) that the dataset creators used when introducing this task. -->
<!-- scope: microscope -->
The metrics mentioned above can be used to assess how well a generated paraphrase corresponds to a given reference sentence. The PINC score additionally assesses how different the surface forms are.

#### Previous results available?

<!-- info: Are previous results available? -->
<!-- scope: telescope -->
yes

#### Other Evaluation Approaches

<!-- info: What evaluation approaches have others used? -->
<!-- scope: periscope -->
See publications on using Opusparcus

#### Relevant Previous Results

<!-- info: What are the most relevant previous results for this task/dataset? -->
<!-- scope: microscope -->
Sjöblom et al. (2020). [Paraphrase Generation and Evaluation on Colloquial-Style Sentences](https://aclanthology.org/2020.lrec-1.224/), Proceedings of the 12th Language Resources and Evaluation Conference (LREC).



## Dataset Curation

### Original Curation

#### Original Curation Rationale

<!-- info: Original curation rationale -->
<!-- scope: telescope -->
Opusparcus was created in order to produce a *sentential* paraphrase corpus for multiple languages containing *colloquial* language (as opposed to news or religious text, for instance).

#### Communicative Goal

<!-- info: What was the communicative goal? -->
<!-- scope: periscope -->
Opusparcus provides labeled examples of pairs of sentences that have similar (or dissimilar) meanings.

#### Sourced from Different Sources

<!-- info: Is the dataset aggregated from different data sources? -->
<!-- scope: telescope -->
no


### Language Data

#### How was Language Data Obtained?

<!-- info: How was the language data obtained? -->
<!-- scope: telescope -->
`Crowdsourced`

#### Where was it crowdsourced?

<!-- info: If crowdsourced, where from? -->
<!-- scope: periscope -->
`Other crowdworker platform`

#### Language Producers

<!-- info: What further information do we have on the language producers? -->
<!-- scope: microscope -->
The data in Opusparcus has been extracted from [OpenSubtitles2016](http://opus.nlpl.eu/OpenSubtitles2016.php), which is in turn based on data from [OpenSubtitles.org](http://www.opensubtitles.org/).

The texts consists of subtitles that have been produced using crowdsourcing.

#### Topics Covered

<!-- info: Does the language in the dataset focus on specific topics? How would you describe them? -->
<!-- scope: periscope -->
The language is representative of movies and TV shows. Domains covered include comedy, drama, relationships, suspense, etc.

#### Data Validation

<!-- info: Was the text validated by a different worker or a data curator? -->
<!-- scope: telescope -->
validated by data curator

#### Data Preprocessing

<!-- info: How was the text data pre-processed? (Enter N/A if the text was not pre-processed) -->
<!-- scope: microscope -->
Sentence and word tokenization was performed.

#### Was Data Filtered?

<!-- info: Were text instances selected or filtered? -->
<!-- scope: telescope -->
algorithmically

#### Filter Criteria

<!-- info: What were the selection criteria? -->
<!-- scope: microscope -->
The sentence pairs in the training sets were ordered automatically based on the estimated likelihood that the sentences were paraphrases, most likely paraphrases on the top, and least likely paraphrases on the bottom.

The validation and test sets were checked and annotated manually, but the sentence pairs selected for annotation had to be different enough in terms of minimum edit distance (Levenshtein distance). This ensured that annotators would not spend their time annotating pairs of more or less identical sentences.


### Structured Annotations

#### Additional Annotations?

<!-- quick -->
<!-- info: Does the dataset have additional annotations for each instance? -->
<!-- scope: telescope -->
expert created

#### Number of Raters

<!-- info: What is the number of raters -->
<!-- scope: telescope -->
11<n<50

#### Rater Qualifications

<!-- info: Describe the qualifications required of an annotator. -->
<!-- scope: periscope -->
Students and staff at the University of Helsinki (native or very proficient speakers of the target languages)

#### Raters per Training Example

<!-- info: How many annotators saw each training example? -->
<!-- scope: periscope -->
0

#### Raters per Test Example

<!-- info: How many annotators saw each test example? -->
<!-- scope: periscope -->
2

#### Annotation Service?

<!-- info: Was an annotation service used? -->
<!-- scope: telescope -->
no

#### Annotation Values

<!-- info: Purpose and values for each annotation -->
<!-- scope: microscope -->
The development and test sets consist of sentence pairs that have been annotated manually; each set contains approximately 1000 sentence pairs that have been verified to be acceptable paraphrases by two independent annotators.

The `annot_score` field reflects the judgments made by the annotators. If the annnotators fully agreed on the category (4.0: dark green, 3.0: light green, 2.0: yellow, 1.0: red), the value of `annot_score` is 4.0, 3.0, 2.0 or 1.0.  If the annotators chose adjacent categories, the value in this field will be 3.5, 2.5 or 1.5.  For instance, a value of 2.5 means that one annotator gave a score of 3 ("mostly good"), indicating a possible paraphrase pair, whereas the other annotator scored this as a 2 ("mostly bad"), that is, unlikely to be a paraphrase pair.  If the annotators disagreed by more than one category, the sentence pair was discarded and won't show up in the datasets.

Annotators could also reject a sentence pair as being corrupted data.

#### Any Quality Control?

<!-- info: Quality control measures? -->
<!-- scope: telescope -->
validated by another rater

#### Quality Control Details

<!-- info: Describe the quality control measures that were taken. -->
<!-- scope: microscope -->
If the annotators disagreed by more than one category, the sentence pair was discarded and is not part of the final dataset.


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
no


### Discussion of Biases

#### Any Documented Social Biases?

<!-- info: Are there documented social biases in the dataset? Biases in this context are variations in the ways members of different social categories are represented that can have harmful downstream consequences for members of the more disadvantaged group. -->
<!-- scope: telescope -->
no

#### Are the Language Producers Representative of the Language?

<!-- info: Does the distribution of language producers in the dataset accurately represent the full distribution of speakers of the language world-wide? If not, how does it differ? -->
<!-- scope: periscope -->
What social bias there may be in the subtitles in this dataset has not been studied.



## Considerations for Using the Data

### PII Risks and Liability

#### Potential PII Risk

<!-- info: Considering your answers to the PII part of the Data Curation Section, describe any potential privacy to the data subjects and creators risks when using the dataset. -->
<!-- scope: microscope -->
The data only contains subtitles of publicly available movies and TV shows.


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

#### Technical Limitations

<!-- info: Describe any known technical limitations, such as spurrious correlations, train/test overlap, annotation biases, or mis-annotations, and cite the works that first identified these limitations when possible. -->
<!-- scope: microscope -->
Some subtitles contain typos that are caused by inaccurate OCR.

#### Unsuited Applications

<!-- info: When using a model trained on this dataset in a setting where users or the public may interact with its predictions, what are some pitfalls to look out for? In particular, describe some applications of the general task featured in this dataset that its curation or properties make it less suitable for. -->
<!-- scope: microscope -->
The models might memorize individual subtitles of existing movies and TV shows, but there is no context across sentence boundaries in the data.

#### Discouraged Use Cases

<!-- info: What are some discouraged use cases of a model trained to maximize the proposed metrics on this dataset? In particular, think about settings where decisions made by a model that performs reasonably well on the metric my still have strong negative consequences for user or members of the public. -->
<!-- scope: microscope -->
A general issue with paraphrasing is that very small modifications in the surface form might produce valid paraphrases, which are however rather uninteresting. It is more valuable to produce paraphrases with clearly different surface realizations (e.g., measured using minimum edit distance).


