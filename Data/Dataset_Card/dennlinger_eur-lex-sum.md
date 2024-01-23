---
annotations_creators:
- found
- expert-generated
language:
- bg
- hr
- cs
- da
- nl
- en
- et
- fi
- fr
- de
- el
- hu
- ga
- it
- lv
- lt
- mt
- pl
- pt
- ro
- sk
- sl
- es
- sv
language_creators:
- found
- expert-generated
license:
- cc-by-4.0
multilinguality:
- multilingual
pretty_name: eur-lex-sum
size_categories:
- 10K<n<100K
source_datasets:
- original
tags:
- legal
- eur-lex
- expert summary
- parallel corpus
- multilingual
task_categories:
- translation
- summarization
---

# Dataset Card for the EUR-Lex-Sum Dataset

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-instances)
  - [Data Splits](#data-instances)
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

## Dataset Description

- **Homepage:** [Needs More Information]
- **Repository:** https://github.com/achouhan93/eur-lex-sum
- **Paper:** [EUR-Lex-Sum: A Multi-and Cross-lingual Dataset for Long-form Summarization in the Legal Domain](https://arxiv.org/abs/2210.13448)
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [Dennis Aumiller](mailto:aumiller@informatik.uni-heidelberg.de)
### Dataset Summary

The EUR-Lex-Sum dataset is a multilingual resource intended for text summarization in the legal domain.
It is based on human-written summaries of legal acts issued by the European Union.
It distinguishes itself by introducing a smaller set of high-quality human-written samples, each of which have much longer references (and summaries!) than comparable datasets.
Additionally, the underlying legal acts provide a challenging domain-specific application to legal texts, which are so far underrepresented in non-English languages.
For each legal act, the sample can be available in up to 24 languages (the officially recognized languages in the European Union); the validation and test samples consist entirely of samples available in *all* languages, and are aligned across all languages at the paragraph level.

### Supported Tasks and Leaderboards

- `summarization`: The dataset is primarily suitable for summarization tasks, where it can be used as a small-scale training resource. The primary evaluation metric used in the underlying experiments is [ROUGE](https://huggingface.co/metrics/rouge). The EUR-Lex-Sum data is particularly interesting, because traditional lead-based baselines (such as lead-3) do not work well, given the extremely long reference summaries. However, we can provide reasonably good summaries by applying a modified LexRank approach on the paragraph level.
- `cross-lingual-summarization`: Given that samples of the dataset exist across multiple languages, and both the validation and test set are fully aligned across languages, this dataset can further be used as a cross-lingual benchmark. In these scenarios, language pairs (e.g., EN to ES) can be compared against monolingual systems. Suitable baselines include automatic translations of gold summaries, or translations of simple LexRank-generated monolingual summaries.
- `long-form-summarization`: We further note the particular case for *long-form summarization*. In comparison to news-based summarization datasets, this resource provides around 10x longer *summary texts*. This is particularly challenging for transformer-based models, which struggle with limited context lengths.

### Languages

The dataset supports all [official languages of the European Union](https://european-union.europa.eu/principles-countries-history/languages_en). At the time of collection, those were 24 languages:
Bulgarian, Croationa, Czech, Danish, Dutch, English, Estonian, Finnish, French, German, Greek, Hungarian, Irish, Italian, Latvian, Lithuanian, Maltese, Polish, Portuguese, Romanian, Slovak, Slovenian, Spanish, and Swedish.

Both the reference texts, as well as the summaries, are translated from an English original text (this was confirmed by private correspondence with the Publications Office of the European Union). Translations and summaries are written by external (professional) parties, contracted by the EU.

Depending on availability of document summaries in particular languages, we have between 391 (Irish) and 1505 (French) samples available. Over 80% of samples are available in at least 20 languages.

## Dataset Structure

### Data Instances

Data instances contain fairly minimal information. Aside from a unique identifier, corresponding to the Celex ID generated by the EU, two further fields specify the original long-form legal act and its associated summary.
```
{
  "celex_id":  "3A32021R0847",
  "reference": "REGULATION (EU) 2021/847 OF THE EUROPEAN PARLIAMENT AND OF THE COUNCIL\n [...]"
  "summary": "Supporting EU cooperation in the field of taxation: Fiscalis (2021-2027)\n\n [...]"

}
```

### Data Fields

- `celex_id`: The [Celex ID](https://eur-lex.europa.eu/content/tools/eur-lex-celex-infographic-A3.pdf) is a naming convention used for identifying EU-related documents. Among other things, the year of publication and sector codes are embedded in the Celex ID.
- `reference`: This is the full text of a Legal Act published by the EU. 
- `summary`: This field contains the summary associated with the respective Legal Act.

### Data Splits

We provide pre-split training, validation and test splits.
To obtain the validation and test splits, we randomly assigned all samples that are available across all 24 languages into two equally large portions. In total, 375 instances are available in 24 languages, which means we obtain a validation split of 187 samples and 188 test instances.
All remaining instances are assigned to the language-specific training portions, which differ in their exact size.

We particularly ensured that no duplicates exist across the three splits. For this purpose, we ensured that no exactly matching reference *or* summary exists for any sample. Further information on the length distributions (for the English subset) can be found in the paper.

## Dataset Creation

### Curation Rationale

The dataset was curated to provide a resource for under-explored aspects of automatic text summarization research.
In particular, we want to encourage the exploration of abstractive summarization systems that are not limited by the usual 512 token context window, which usually works well for (short) news articles, but fails to generate long-form summaries, or does not even work with longer source texts in the first place.
Also, existing resources primarily focus on a single (and very specialized) domain, namely news article summarization. We wanted to provide a further resource for *legal* summarization, for which many languages do not even have any existing datasets.  
We further noticed that no previous system had utilized the human-written samples from the [EUR-Lex platform](https://eur-lex.europa.eu/homepage.html), which provide an excellent source for training instances suitable for summarization research. We later found out about a resource created in parallel based on EUR-Lex documents, which provides a [monolingual (English) corpus](https://github.com/svea-klaus/Legal-Document-Summarization) constructed in similar fashion. However, we provide a more thorough filtering, and extend the process to the remaining 23 EU languages.

### Source Data

#### Initial Data Collection and Normalization

The data was crawled from the aforementioned EUR-Lex platform. In particular, we only use samples which have *HTML* versions of the texts available, which ensure the alignment across languages, given that translations have to retain the original paragraph structure, which is encoded in HTML elements.
We further filter out samples that do not have associated document summaries available.

One particular design choice has to be expanded upon: For some summaries, *several source documents* are considered as an input by the EU. However, since we construct a single-document summarization corpus, we decided to use the **longest reference document only**. This means we explicitly drop the other reference texts from the corpus.  
One alternative would have been to concatenated all relevant source texts; however, this generally leads to degradation of positional biases in the text, which can be an important learned feature for summarization systems. Our paper details the effect of this decision in terms of n-gram novelty, which we find is affected by the processing choice. 

#### Who are the source language producers?

The language producers are external professionals contracted by the European Union offices. As previously noted, all non-English texts are generated from the respective English document (all summaries are direct translations the English summary, all reference texts are translated from the English reference text).
No further information on the demographic of annotators is provided.

### Annotations

#### Annotation process

The European Union publishes their [annotation guidelines](https://etendering.ted.europa.eu/cft/cft-documents.html?cftId=6490) for summaries, which targets a length between 600-800 words.
No information on the guidelines for translations is known.

#### Who are the annotators?

The language producers are external professionals contracted by the European Union offices.  No further information on the annotators is available.

### Personal and Sensitive Information

The original text was not modified in any way by the authors of this dataset. Explicit mentions of personal names can occur in the dataset, however, we rely on the European Union that no further sensitive information is provided in these documents.

## Considerations for Using the Data

### Social Impact of Dataset

The dataset can be used to provide summarization systems in languages that are previously under-represented. For example, language samples in Irish and Maltese (among others) enable the development and evaluation for these languages.  
A successful cross-lingual system would further enable the creation of automated legal summaries for legal acts, possibly enabling foreigners in European countries to automatically translate similar country-specific legal acts.

Given the limited amount of training data, this dataset is also suitable as a test bed for low-resource approaches, especially in comparsion to strong unsupervised (extractive) summarization systems.
We also note that the summaries are explicitly provided as "not legally binding" by the EU. The implication of left-out details (a necessary evil of summaries) implies the existence of differences between the (legally binding) original legal act.

Risks associated with this dataset also largely stem from the potential application of systems trained on it. Decisions in the legal domain require careful analysis of the full context, and should not be made based on system-generated summaries at this point in time. Known biases of summarization, specifically factual hallucinations, should act as further deterrents.

### Discussion of Biases

Given the availability bias, some of the languages in the dataset are more represented than others. We attempt to mitigate influence on the evaluation by providing validation and test sets of the same size across all languages.
Given that we require the availability of HTML documents, we see a particular temporal bias in our dataset, which features more documents from the years of 1990 onwards, simply due to the increase in EU-related activities, but also the native use of the internet as a data storage.
This could imply a particular focus on more recent topics (e.g., Brexit, renewable eneriges, etc. come to mind).

Finally, due to the source of these documents being the EU, we expect a natural bias towards EU-centric (and therefore Western-centric) content; other nations and continents will be under-represented in the data.

### Other Known Limitations

As previously outlined, we are aware of some summaries relating to multiple (different) legal acts. For these samples, only one (the longest) text will be available in our dataset.

## Additional Information

### Dataset Curators

The web crawler was originally implemented by Ashish Chouhan.
Post-filtering and sample correction was later performed by Dennis Aumiller.
Both were PhD students employed at the Database Systems Research group of Heidelberg University, under the guidance of Prof. Dr. Michael Gertz.

### Licensing Information

Data from the EUR-Lex platform is available under the CC-BY SA 4.0 license. We redistribute the dataset under the same license.

### Citation Information
For the pre-print version, please cite:

```
@article{aumiller-etal-2022-eur,
author = {Aumiller, Dennis and Chouhan, Ashish and Gertz, Michael},
title = {{EUR-Lex-Sum: A Multi- and Cross-lingual Dataset for Long-form Summarization in the Legal Domain}},
journal = {CoRR},
volume = {abs/2210.13448},
eprinttype = {arXiv},
eprint = {2210.13448},
url = {https://arxiv.org/abs/2210.13448}
}
```