---
annotations_creators:
- expert-generated
- crowdsourced
language:
- en
language_creators:
- crowdsourced
- expert-generated
license:
- mit
multilinguality:
- monolingual
paperswithcode_id: winobias
pretty_name: panda
size_categories:
- 100K<n<1M
source_datasets:
- original
tags:
- fairness
- nlp
- demographic
- diverse
- gender
- non-binary
- race
- age
task_categories:
- token-classification
task_ids: []
---

# Dataset Card for PANDA

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

- **Repository:** https://github.com/facebookresearch/ResponsibleNLP/
- **Paper:** https://arxiv.org/abs/2205.12586
- **Point of Contact:** rebeccaqian@meta.com, ccross@meta.com, douwe@huggingface.co, adinawilliams@meta.com

### Dataset Summary

PANDA (Perturbation Augmentation NLP DAtaset) consists of approximately 100K pairs of crowdsourced human-perturbed text snippets (original, perturbed). Annotators were given selected terms and target demographic attributes, and instructed to rewrite text snippets along three demographic axes: gender, race and age, while preserving semantic meaning. Text snippets were sourced from a range of text corpora (BookCorpus, Wikipedia, ANLI, MNLI, SST, SQuAD). PANDA can be used for training a learned perturber that can rewrite text with control. PANDA can also be used to evaluate the demographic robustness of language models.

### Languages

English

## Dataset Structure

### Data Instances

- Size of training data: 198.6 MB
- Size of validation data: 22.2 MB

Examples of data instances:
```
{
  "original": "the moment the girl mentions the subject she will be yours .",
  "selected_word": "girl",
  "target_attribute": "man",
  "perturbed": "the moment the boy mentions the subject he will be yours.\n\n"
}
{
  "original": "are like magic tricks, says the New York Times ' Michael Kimmelman. <SEP> Michael Kimmelman has never likened anything to a magic trick.",
  "selected_word": "Michael",
  "target_attribute": "woman",
  "perturbed": "are like magic tricks, says the New York Times' Michelle Kimmelman. <SEP> Michelle Kimmelman has never likened anything to a magic trick."
}
{
  "original": "lilly ann looked at him asking herself how he cold not know .",
  "selected_word": "he",
  "target_attribute": "non-binary",
  "perturbed": "Lilly Ann looked at them, asking herself how they could not know."
}
```

Examples with <SEP> tokens are the result of concatenation of text fields in source datasets, such as the premise and hypothesis of NLI datasets.

### Data Fields

- `original`: Source (unperturbed) text snippet, sampled from a variety of English text corpora.
- `selected_word`: Demographic term that needs to be perturbed.
- `target_attribute`: Target demographic category.
- `perturbed`: Perturbed text snippet, which is the source text rewritten to alter the selected word along the specified target demographic attribute. For example, if the selected word is "Lily" and target is "man", all references to "Lily" (eg. pronouns) in the source text are altered to refer to a man. Note that some examples may be unchanged, either due to the lack of demographic information, or ambiguity of the task; given the subjective nature of identifying demographic terms and attributes, we allow some room for interpretation provided the rewrite does not perpetuate harmful social biases.

### Data Splits

- `train`: 94966
- `valid`: 10551

## Dataset Creation

### Curation Rationale

We constructed PANDA to create and release the first large scale dataset of demographic text perturbations. This enables the training of the first neural perturber model, which outperforms heuristic approaches. 

### Source Data

#### Initial Data Collection and Normalization

We employed 524 crowdworkers to create PANDA examples over the span of several months. Annotators were tasked with rewriting text snippets sourced from popular English text corpora. For more information on the task UI and methodology, see our paper *Perturbation Augmentation for Fairer NLP*.

### Annotations

#### Annotation process

PANDA was collected in a 3 stage annotation process:
1. Span identification: Annotators select demographic terms in source text samples.
2. Attribute identification: Identified demographic terms are annotated for gender/race/age attributes, such as "man", "Asian", "old" etc.
3. Rewrite text: Annotators rewrite text by modifying the selected entity to reflect the target demographic attribute. Annotators are encouraged to create minimal edits, eg. "George" -> "Georgina".

The annotation process is explained in more detail in our paper.

#### Who are the annotators?

PANDA was annotated by English speaking Amazon Mechanical Turk workers. We included a voluntary demographic survey along with annotation tasks that did not contribute to pay. For a breakdown of annotators' demographic identities, see our paper.

### Personal and Sensitive Information

PANDA does not contain identifying information about annotators.

## Considerations for Using the Data

### Social Impact of Dataset

By releasing the first large scale dataset of demographic text rewrites, we hope to enable exciting future work in fairness in NLP toward more scalable, automated approaches to reducing biases in datasets and language models.

Furthermore, PANDA aims to be diverse in text domain and demographic representation. PANDA includes a large proportion of non-binary gender annotations, which are underrepresented in existing text corpora and prior fairness datasets. Text examples vary in length, with examples spanning single sentences and long Wikipedia passages, and are sourced from a variety of text corpora that can be used to train a domain agnostic perturber.


### Discussion of Biases

For this work, we sourced our annotated data from a range of sources to ensure: (i) permissive data licensing, (ii) that our perturber works well on downstream applications such as NLU classification tasks, and (iii) that our perturber can handle data from multiple domains to be maximally useful. However, we acknowledge that there may be other existing biases in PANDA as a result of our data sourcing choices. For example, it is possible that data sources like BookWiki primarily contain topics of interest to people with a certain amount of influence and educational access, people from the so-called “Western world”, etc. Other topics that might be interesting and relevant to others may be missing or only present in limited quantities. The present approach can only weaken associations inherited from the data sources we use, but in future work, we would love to explore the efficacy of our approach on text from other sources that contain a wider range of topics and text domain differences.

### Other Known Limitations

Our augmentation process can sometimes create nonexistent versions of real people, such as discussing an English King Victor (not a historical figure), as opposed to a Queen Victoria (a historical figure). We embrace the counterfactuality of many of our perturbations, but the lack of guaranteed factuality means that our approach may not be well-suited to all NLP tasks. For example, it might not be suitable for augmenting misinformation detection datasets, because peoples’ names, genders, and other demographic information should not be changed.

## Additional Information

### Dataset Curators

Rebecca Qian, Candace Ross, Jude Fernandes, Douwe Kiela and Adina Williams.

### Licensing Information

PANDA is released under the MIT license.

### Citation Information

https://arxiv.org/abs/2205.12586

### Contributions

Thanks to [@Rebecca-Qian](https://github.com/Rebecca-Qian) for adding this dataset.