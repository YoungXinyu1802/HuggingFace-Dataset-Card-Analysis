---
annotations_creators:
- crowdsourced
language_creators:
- crowdsourced
language:
- en
license:
- mit
multilinguality:
- monolingual
pretty_name: sufficient_facts
size_categories:
- 1K<n<10K
source_datasets:
- extended|fever
- extended|hover
- extended|fever_gold_evidence
task_categories:
- text-classification
task_ids:
- fact-checking
---

# Dataset Card for sufficient_facts

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Homepage:** https://github.com/copenlu/sufficient_facts
- **Repository:** https://github.com/copenlu/sufficient_facts
- **Paper:** Will be uploaded soon...
- **Leaderboard:**
- **Point of Contact:** https://apepa.github.io/

### Dataset Summary

This is the dataset SufficientFacts, introduced in the paper "Fact Checking with Insufficient Evidence", accepted at the TACL journal in 2022. 

Automating the fact checking (FC) process relies on information obtained from external sources. In this work, we posit that it is crucial for FC models to make veracity predictions only when there is sufficient evidence and otherwise indicate when it is not enough. To this end, we are the first to study what information FC models consider sufficient by introducing a novel task and advancing it with three main contributions. First, we conduct an in-depth empirical analysis of the task with a new fluency-preserving method for omitting information from the evidence at the constituent and sentence level. We identify when models consider the remaining evidence (in)sufficient for FC, based on three trained models with different Transformer architectures and three FC datasets. Second, we ask annotators whether the omitted evidence was important for FC, resulting in a novel diagnostic dataset, **SufficientFacts**, for FC with omitted evidence. We find that models are least successful in detecting missing evidence when adverbial modifiers are omitted (21% accuracy), whereas it is easiest for omitted date modifiers (63% accuracy). Finally, we propose a novel data augmentation strategy for contrastive self-learning of missing evidence by employing the proposed omission method combined with tri-training. It improves performance for Evidence Sufficiency Prediction by up to 17.8 F1 score, which in turn improves FC performance by up to 2.6 F1 score.


### Languages

English

## Dataset Structure

The dataset consists of three files, each for one of the datasets -- FEVER, HoVer, and VitaminC.
Each file consists of json lines of the format:

```json
{
    "claim": "Unison (Celine Dion album) was originally released by Atlantic Records.", 
    "evidence": [
        [
            "Unison (Celine Dion album)", 
            "The album was originally released on 2 April 1990 ."
        ]
    ],
    "label_before": "REFUTES", 
    "label_after": "NOT ENOUGH", 
    "agreement": "agree_ei", 
    "type": "PP", 
    "removed": ["by Columbia Records"], 
    "text_orig": "[[Unison (Celine Dion album)]] The album was originally released on 2 April 1990 <span style=\"color:red;\">by Columbia Records</span> ."
}
```

### Data Instances

* FEVER: 600 consituent-level, 400 sentence-level; 
* HoVer - 600 consituent-level, 400 sentence-level; 
* VitaminC - 600 consituent-level.

### Data Fields

* `claim` - the claim that is being verified
* `evidence` - the augmented evidence for the claim, i.e. the evidence with some removed information
* `label_before` - the original label for the claim-evidence pair, before information was removed from the evidence
* `label_after` - the label for the augmented claim-evidence pair, after information was removed from the evidence, as annotated by crowd-source workers
* `type` - type of the information removed from the evidence. The types are fine-grained and their mapping to the general types -- 7 constituent and 1 sentence type can be found in [types.json](types.json) file.
* `removed` - the text of the removed information from the evidence
* `text_orig` - the original text of the evidence, as presented to crowd-source workers, the text of the removed information is inside `<span style=\"color:red;\"></span>` tags.

### Data Splits

|   name   |test_fever|test_hover|test_vitaminc|
|----------|-------:|-----:|-------:|
|test|   1000|  1000|   600|


Augmented from the test splits of the corresponding datasets.

### Annotations

#### Annotation process

The workers were provided with the following task description:

For each evidence text, some facts have been removed (marked in <span style="color:red;">red</span>). 
You should annotate whether, <b>given the remaining facts in the evidence text, the evidence is still enough for verifying the claim.</b> <br></br>
<ul>
    <li>You should select <i><b>'ENOUGH -- IRRELEVANT'</b></i>, if the <b>remaining information is still <i>enough</i></b> for verifying the claim because the <b>removed information is irrelevant</b> for identifying the evidence as SUPPORTS or REFUTES. See examples 1 and 2.</li>
    <li>You should select <i><b>'ENOUGH -- REPEATED'</b></i>, if the <b>remaining information is still <i>enough</i></b> for verifying the claim because the <b>removed information is relevant but is also present (repeated) in the remaining (not red) text.</b> See example 3.</li>
    <li>You should select <i><b>'NOT ENOUGH'</b></i> -- when <b>1) the removed information is <i>relevant</i></b> for verifying the claim <b> AND 2) it is <i>not present (repeated)</i> in the remaining text.</b> See examples 4, 5, and 6.</li>
    <!--<li>You should select <i><b>'CHANGED INFO'</b></i> in the rare cases when the remaining evidence has <b>changed the support for the claim</b></li>-->
</ul>   

<b>Note: You should not incorporate your own knowledge or beliefs! You should rely only on the evidence provided for the claim.</b> 

The annotators were then given example instance annotations.
Finally, annotators were asked to complete a qualification test in order to be allowed to annotate instances for the task. 
The resulting inter-annotator agreement for SufficientFacts is 0.81 Fleiss'k from three annotators.

#### Who are the annotators?

The annotations were performed by workers at Amazon Mechanical Turk.

## Additional Information

### Licensing Information

MIT

### Citation Information
```
@article{10.1162/tacl_a_00486,
    author = {Atanasova, Pepa and Simonsen, Jakob Grue and Lioma, Christina and Augenstein, Isabelle},
    title = "{Fact Checking with Insufficient Evidence}",
    journal = {Transactions of the Association for Computational Linguistics},
    volume = {10},
    pages = {746-763},
    year = {2022},
    month = {07},
    abstract = "{Automating the fact checking (FC) process relies on information obtained from external sources. In this work, we posit that it is crucial for FC models to make veracity predictions only when there is sufficient evidence and otherwise indicate when it is not enough. To this end, we are the first to study what information FC models consider sufficient by introducing a novel task and advancing it with three main contributions. First, we conduct an in-depth empirical analysis of the task with a new fluency-preserving method for omitting information from the evidence at the constituent and sentence level. We identify when models consider the remaining evidence (in)sufficient for FC, based on three trained models with different Transformer architectures and three FC datasets. Second, we ask annotators whether the omitted evidence was important for FC, resulting in a novel diagnostic dataset, SufficientFacts1, for FC with omitted evidence. We find that models are least successful in detecting missing evidence when adverbial modifiers are omitted (21\\% accuracy), whereas it is easiest for omitted date modifiers (63\\% accuracy). Finally, we propose a novel data augmentation strategy for contrastive self-learning of missing evidence by employing the proposed omission method combined with tri-training. It improves performance for Evidence Sufficiency Prediction by up to 17.8 F1 score, which in turn improves FC performance by up to 2.6 F1 score.}",
    issn = {2307-387X},
    doi = {10.1162/tacl_a_00486},
    url = {https://doi.org/10.1162/tacl\_a\_00486},
    eprint = {https://direct.mit.edu/tacl/article-pdf/doi/10.1162/tacl\_a\_00486/2037141/tacl\_a\_00486.pdf},
}
```
### Contributions

Thanks to [@apepa](https://github.com/apepa) for adding this dataset.