---
annotations_creators:
- no-annotation
language_creators:
- crowdsourced
language:
- es
multilinguality:
- monolingual
pretty_name: BIOASQ
size_categories:
- 100K<n<1M
source_datasets:
- Helsinki-NLP/opus-mt-en-es
task_categories:
- sequence-modeling
task_ids:
- language-modeling
---
# BIOASQ 2022 Spanish

This is an automatically translated version of the bioasq dataset, a dataset used for question answering in the biomedical domain.

The translation was performed for the questions, answers and contexts using the [marianMT english-spanish](https://huggingface.co/Helsinki-NLP/opus-mt-en-es) . As the translation process may return answers that are not 100% present in the context, we developed an algorithm based on sentence tokenization and intersection of the words present in the answer and in the portion of the context that we are evaluating, and then extracting the parragraph from the context that matches the answer.

License, distribution and usage conditions of the original dataset apply.

### Contributions
Thanks to [@avacaondata](https://huggingface.co/avacaondata), [@alborotis](https://huggingface.co/alborotis), [@albarji](https://huggingface.co/albarji), [@Dabs](https://huggingface.co/Dabs), [@GuillemGSubies](https://huggingface.co/GuillemGSubies) for adding this dataset.