---
annotations_creators:
- expert-generated
language_creators:
- found
language:
- en
license:
- gpl-3.0
multilinguality:
- monolingual
size_categories:
- n<1K
source_datasets:
- original
task_categories:
- text-classification
task_ids:
- text-scoring
- semantic-similarity-scoring
paperswithcode_id: biosses
pretty_name: BIOSSES
dataset_info:
  features:
  - name: sentence1
    dtype: string
  - name: sentence2
    dtype: string
  - name: score
    dtype: float32
  splits:
  - name: train
    num_bytes: 32783
    num_examples: 100
  download_size: 36324
  dataset_size: 32783
---

# Dataset Card for BIOSSES

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
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

- **Homepage:** https://tabilab.cmpe.boun.edu.tr/BIOSSES/DataSet.html
- **Repository:** https://github.com/gizemsogancioglu/biosses
- **Paper:** [BIOSSES: a semantic sentence similarity estimation system for the biomedical domain](https://academic.oup.com/bioinformatics/article/33/14/i49/3953954)
- **Point of Contact:** [Gizem Soğancıoğlu](gizemsogancioglu@gmail.com) and [Arzucan Özgür](gizemsogancioglu@gmail.com)

### Dataset Summary

BIOSSES is a benchmark dataset for biomedical sentence similarity estimation. The dataset comprises 100 sentence pairs, in which each sentence was selected from the [TAC (Text Analysis Conference) Biomedical Summarization Track Training Dataset](https://tac.nist.gov/2014/BiomedSumm/) containing articles from the biomedical domain. The sentence pairs in BIOSSES were selected from citing sentences, i.e. sentences that have a citation to a reference article. 

The sentence pairs were evaluated by five different human experts that judged their similarity and gave scores ranging from 0 (no relation) to 4 (equivalent). In the original paper the mean of the scores assigned by the five human annotators was taken as the gold standard. The Pearson correlation between the gold standard scores and the scores estimated by the models was used as the evaluation metric. The strength of correlation can be assessed by the general guideline proposed by Evans (1996) as follows:

- very strong: 0.80–1.00
- strong: 0.60–0.79
- moderate: 0.40–0.59
- weak: 0.20–0.39
- very weak: 0.00–0.19

### Data Splits (From BLUE Benchmark)

|name|Train|Dev|Test|
|:--:|:--:|:--:|:--:|
|biosses|64|16|20|

### Supported Tasks and Leaderboards

Biomedical Semantic Similarity Scoring.

### Languages

English.

## Dataset Structure

### Data Instances

For each instance, there are two sentences (i.e. sentence 1 and 2), and its corresponding similarity score (the mean of the scores assigned by the five human annotators).

```json
{
    "id": "0",
    "sentence1": "Centrosomes increase both in size and in microtubule-nucleating capacity just before mitotic entry.", 
    "sentence2": "Functional studies showed that, when introduced into cell lines, miR-146a was found to promote cell proliferation in cervical cancer cells, which suggests that miR-146a works as an oncogenic miRNA in these cancers.",
    "score": 0.0
}
```

### Data Fields

- `sentence 1`: string
- `sentence 2`: string
- `score`: float ranging from 0 (no relation) to 4 (equivalent)

## Dataset Creation

### Curation Rationale

### Source Data

The [TAC (Text Analysis Conference) Biomedical Summarization Track Training Dataset](https://tac.nist.gov/2014/BiomedSumm/).

### Annotations

#### Annotation process

The sentence pairs were evaluated by five different human experts that judged their similarity and gave scores ranging from 0 (no relation) to 4 (equivalent). The score range was described based on the guidelines of SemEval 2012 Task 6 on STS (Agirre et al., 2012). Besides the annotation instructions, example sentences from the biomedical literature were provided to the annotators for each of the similarity degrees.

The table below shows the Pearson correlation of the scores of each annotator with respect to the average scores of the remaining four annotators. It is observed that there is strong association among the scores of the annotators. The lowest correlations are 0.902, which can be considered as an upper bound for an algorithmic measure evaluated on this dataset.

|           |Correlation r  |
|----------:|--------------:|
|Annotator A|         	0.952|
|Annotator B|         	0.958|
|Annotator C|         	0.917|
|Annotator D|         	0.902|
|Annotator E|         	0.941|

## Additional Information

### Dataset Curators

- Gizem Soğancıoğlu, gizemsogancioglu@gmail.com 
- Hakime Öztürk, hakime.ozturk@boun.edu.tr
- Arzucan Özgür, gizemsogancioglu@gmail.com
Bogazici University, Istanbul, Turkey

### Licensing Information

BIOSSES is made available under the terms of [The GNU Common Public License v.3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).

### Citation Information

```bibtex
@article{10.1093/bioinformatics/btx238,
    author = {Soğancıoğlu, Gizem and Öztürk, Hakime and Özgür, Arzucan},
    title = "{BIOSSES: a semantic sentence similarity estimation system for the biomedical domain}",
    journal = {Bioinformatics},
    volume = {33},
    number = {14},
    pages = {i49-i58},
    year = {2017},
    month = {07},
    abstract = "{The amount of information available in textual format is rapidly increasing in the biomedical domain. Therefore, natural language processing (NLP) applications are becoming increasingly important to facilitate the retrieval and analysis of these data. Computing the semantic similarity between sentences is an important component in many NLP tasks including text retrieval and summarization. A number of approaches have been proposed for semantic sentence similarity estimation for generic English. However, our experiments showed that such approaches do not effectively cover biomedical knowledge and produce poor results for biomedical text.We propose several approaches for sentence-level semantic similarity computation in the biomedical domain, including string similarity measures and measures based on the distributed vector representations of sentences learned in an unsupervised manner from a large biomedical corpus. In addition, ontology-based approaches are presented that utilize general and domain-specific ontologies. Finally, a supervised regression based model is developed that effectively combines the different similarity computation metrics. A benchmark data set consisting of 100 sentence pairs from the biomedical literature is manually annotated by five human experts and used for evaluating the proposed methods.The experiments showed that the supervised semantic sentence similarity computation approach obtained the best performance (0.836 correlation with gold standard human annotations) and improved over the state-of-the-art domain-independent systems up to 42.6\\% in terms of the Pearson correlation metric.A web-based system for biomedical semantic sentence similarity computation, the source code, and the annotated benchmark data set are available at: http://tabilab.cmpe.boun.edu.tr/BIOSSES/.}",
    issn = {1367-4803},
    doi = {10.1093/bioinformatics/btx238},
    url = {https://doi.org/10.1093/bioinformatics/btx238},
    eprint = {https://academic.oup.com/bioinformatics/article-pdf/33/14/i49/25157316/btx238.pdf},
}
```

### Contributions

Thanks to [@qanastek](https://github.com/qanastek) for adding this dataset.
