---
annotations_creators:
- expert-generated
language:
- en
language_creators:
- found
license:
- cc-by-nc-4.0
multilinguality:
- monolingual
paperswithcode_id: citeworth
pretty_name: CiteWorth
size_categories:
- 1M<n<10M
source_datasets:
- extended|s2orc
tags:
- citation detection
- citation
- science
- scholarly documents
- bio
- medicine
- computer science
- citeworthiness
task_categories:
- text-classification
task_ids: []
---

# Dataset Card for CiteWorth

## Dataset Description

- **Repo** https://github.com/copenlu/cite-worth
- **Paper** https://aclanthology.org/2021.findings-acl.157.pdf

### Dataset Summary

Scientific document understanding is challenging as the data is highly domain specific and diverse. However, datasets for tasks with scientific text require expensive manual annotation and tend to be small and limited to only one or a few fields. At the same time, scientific documents contain many potential training signals, such as citations, which can be used to build large labelled datasets. Given this, we present an in-depth study of cite-worthiness detection in English, where a sentence is labelled for whether or not it cites an external source. To accomplish this, we introduce CiteWorth, a large, contextualized, rigorously cleaned labelled dataset for cite-worthiness detection built from a massive corpus of extracted plain-text scientific documents. We show that CiteWorth is high-quality, challenging, and suitable for studying problems such as domain adaptation. Our best performing cite-worthiness detection model is a paragraph-level contextualized sentence labelling model based on Longformer, exhibiting a 5 F1 point improvement over SciBERT which considers only individual sentences. Finally, we demonstrate that language model fine-tuning with cite-worthiness as a secondary task leads to improved performance on downstream scientific document understanding tasks.

## Dataset Structure

The data is structured as follows
 - `paper_id`: The S2ORC paper ID where the paragraph comes from
 - `section_idx`: An index into the section array in the original S2ORC data
 - `file_index`: The volume in the S2ORC dataset that the paper belongs to
 - `file_offset`: Byte offset to the start of the paper json in the S2ORC paper PDF file
 - `mag_field_of_study`: The field of study to which a paper belongs (an array, but each paper belongs to a single field)
 - `original_text`: The original text of the paragraph
 - `section_title`: Title of the section to which the paragraph belongs
 - `samples`: An array containing dicts of the cleaned sentences for the paragraph, in order. The fields for each dict are as follows
   - `text`: The cleaned text for the sentence
   - `label`: Label for the sentence, either `check-worthy` for cite-worthy sentences or `non-check-worthy` non-cite-worthy sentences
   - `original_text`: The original sentence text
   - `ref_ids`: List of the reference IDs in the S2ORC dataset for papers cited in this sentence
   - `citation_text`: List of all citation text in this sentence

## Dataset Creation

The data is derived from the [S2ORC dataset](https://github.com/allenai/s2orc), specifically the 20200705v1 release of the data. It is licensed under the [CC By-NC 2.0](https://creativecommons.org/licenses/by-nc/2.0/) license. For details on the dataset creation process, see section 3 of our [paper](https://aclanthology.org/2021.findings-acl.157.pdf)
.

## Citing
Please use the following citation when referencing this work or using the data:

```
@inproceedings{wright2021citeworth,
    title={{CiteWorth: Cite-Worthiness Detection for Improved Scientific Document Understanding}},
    author={Dustin Wright and Isabelle Augenstein},
    booktitle = {Findings of ACL-IJCNLP},
    publisher = {Association for Computational Linguistics},
    year = 2021
}
```