---
annotations_creators: []
language:
- en
language_creators: []
license:
- cc0-1.0
multilinguality:
- monolingual
pretty_name: 'DBpedia'
size_categories:
- 1M<n<10M
source_datasets: []
tags: []
task_categories:
- text-classification
task_ids:
- topic-classification
---

About Dataset

DBpedia (from "DB" for "database") is a project aiming to extract structured content from the information created in Wikipedia.
This is an extract of the data (after cleaning, kernel included) that provides taxonomic, hierarchical categories ("classes") for 342,782 wikipedia articles. There are 3 levels, with 9, 70 and 219 classes respectively.
A version of this dataset is a popular baseline for NLP/text classification tasks. This version of the dataset is much tougher, especially if the L2/L3 levels are used as the targets.

This is an excellent benchmark for hierarchical multiclass/multilabel text classification.
Some example approaches are included as code snippets.
Content

DBPedia dataset with multiple levels of hierarchy/classes, as a multiclass dataset.
Original DBPedia ontology (triplets data): https://wiki.dbpedia.org/develop/datasets
Listing of the class tree/taxonomy: http://mappings.dbpedia.org/server/ontology/classes/
Acknowledgements

Thanks to the Wikimedia foundation for creating Wikipedia, DBPedia and associated open-data goodness!

Thanks to my colleagues at Sparkbeyond (https://www.sparkbeyond.com) for pointing me towards the taxonomical version of this dataset (as opposed to the classic 14 class version)
Inspiration

    Try different NLP models.
    See also https://www.kaggle.com/datasets/danofer/dbpedia-classes
    Compare to the SOTA in Text Classification on DBpedia - https://paperswithcode.com/sota/text-classification-on-dbpedia