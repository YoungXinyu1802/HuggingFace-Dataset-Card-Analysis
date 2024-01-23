# Overview
This dataset is a subset of the huggingface wikipedia dataset with ~70'000 rows, each about a person on wikipedia.
Each row contains the original wikipedia texts as sentences,
as well as a paraphrased version of each sentence. For both versions full texts with the entity the wikipedia page is about being masked.


# features
- id: the id in the original dataset
- url: the link to the wikipedia page
- title: the title of the wikipedia page
- text: the original wikipedia text
- sentences: text split to sentences
- paraphrased_sentences: text split to sentences, with each sentence paraphrased (e.g. mutated a bit)
- masked_text_original: original text with entity masked in every occurence (<mask> as token)
- masked_entities_original: array of entities masked in masked_text_original
- masked_text_paraphrased: paraphrased text with entity masked in every occurence
- masked_entities_paraphrased: array of entities msked in masked_text_paraphrased

---
annotations_creators:
- no-annotation
- machine-generated
language:
- en
language_creators:
- found
license:
- afl-3.0
multilinguality:
- monolingual
pretty_name: wikipedia persons paraphrased and masked
size_categories:
- 10K<n<100K
source_datasets:
- extended|wikipedia
tags: []
task_categories:
- fill-mask
task_ids:
- slot-filling