# Title 
EntSUM: A Data Set for Entity-Centric Extractive Summarization

# Author list
Mounica Maddela*, Mayank Kulkarni*, Daniel Preotiuc-Pietro

# Description
Controllable summarization aims to provide summaries that take into account user-specified aspects and preferences to better assist them with their information need, as opposed to the standard summarization setup which build a single generic summary of a document. We introduce a human-annotated data set EntSUM for controllable summarization with a focus on named entities as the aspects to control. We conduct an extensive quantitative analysis to motivate the task of entity-centric summarization and show that existing methods for controllable summarization fail to generate entity-centric summaries. We propose extensions to state-of-the-art summarization approaches that achieve substantially better results on our data set. Our analysis and results show the challenging nature of this task and of the proposed data set.
As a part of this zip file, we release the EntSum dataset on which the evaluations are performed. There are three json files, namely, one summary annotation, two summary annotations and a combination of both. Each file contains the document ID from the NYT corpus, the sentence IDs, the summary(s), the salient sentences and summary sentence corresponding to the sentence IDs. Obtaining the source text can be done by downloading the original NYT corpus and mapping the document IDs. The annotation process and pre-processing details are described extensively in the research paper.

# Language
English

# Keywords
Natural Language Processing, Summarization, Abstractive Summarization, Extractive Summarization

# Related identifiers 
NYT – is the source that this data set is derived from - https://doi.org/10.35111/77ba-9x74, License (LDC) https://catalog.ldc.upenn.edu/LDC2008T19

# Citation
```
@inproceedings{maddela-etal-2022-entsum,
    title = "{E}nt{SUM}: A Data Set for Entity-Centric Extractive Summarization",
    author = "Maddela, Mounica  and
      Kulkarni, Mayank  and
      Preotiuc-Pietro, Daniel",
    booktitle = "Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = may,
    year = "2022",
    address = "Dublin, Ireland",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.acl-long.237",
    pages = "3355--3366",
    abstract = "Controllable summarization aims to provide summaries that take into account user-specified aspects and preferences to better assist them with their information need, as opposed to the standard summarization setup which build a single generic summary of a document.We introduce a human-annotated data set EntSUM for controllable summarization with a focus on named entities as the aspects to control.We conduct an extensive quantitative analysis to motivate the task of entity-centric summarization and show that existing methods for controllable summarization fail to generate entity-centric summaries. We propose extensions to state-of-the-art summarization approaches that achieve substantially better results on our data set. Our analysis and results show the challenging nature of this task and of the proposed data set.",
}
```