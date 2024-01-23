---
pretty_name: ScandiQA
language:
- da
- sv
- no
license:
- cc-by-sa-4.0
multilinguality:
- multilingual
size_categories:
- 1K<n<10K
source_datasets:
- mkqa
- natural_questions
task_categories:
- question-answering
task_ids:
- extractive-qa
---

# Dataset Card for ScandiQA

## Dataset Description

- **Repository:** <https://github.com/alexandrainst/scandi-qa>
- **Point of Contact:** [Dan Saattrup Nielsen](mailto:dan.nielsen@alexandra.dk)
- **Size of downloaded dataset files:** 69 MB
- **Size of the generated dataset:** 67 MB
- **Total amount of disk used:** 136 MB

### Dataset Summary

ScandiQA is a dataset of questions and answers in the Danish, Norwegian, and Swedish
languages. All samples come from the Natural Questions (NQ) dataset, which is a large
question answering dataset from Google searches. The Scandinavian questions and answers
come from the MKQA dataset, where 10,000 NQ samples were manually translated into,
among others, Danish, Norwegian, and Swedish. However, this did not include a
translated context, hindering the training of extractive question answering models.

We merged the NQ dataset with the MKQA dataset, and extracted contexts as either "long
answers" from the NQ dataset, being the paragraph in which the answer was found, or
otherwise we extract the context by locating the paragraphs which have the largest
cosine similarity to the question, and which contains the desired answer.

Further, many answers in the MKQA dataset were "language normalised": for instance, all
date answers were converted to the format "YYYY-MM-DD", meaning that in most cases
these answers are not appearing in any paragraphs. We solve this by extending the MKQA
answers with plausible "answer candidates", being slight perturbations or translations
of the answer.

With the contexts extracted, we translated these to Danish, Swedish and Norwegian using
the [DeepL translation service](https://www.deepl.com/pro-api?cta=header-pro-api) for
Danish and Swedish, and the [Google Translation
service](https://cloud.google.com/translate/docs/reference/rest/) for Norwegian. After
translation we ensured that the Scandinavian answers do indeed occur in the translated
contexts.

As we are filtering the MKQA samples at both the "merging stage" and the "translation
stage", we are not able to fully convert the 10,000 samples to the Scandinavian
languages, and instead get roughly 8,000 samples per language. These have further been
split into a training, validation and test split, with the latter two containing
roughly 750 samples. The splits have been created in such a way that the proportion of
samples without an answer is roughly the same in each split.


### Supported Tasks and Leaderboards

Training machine learning models for extractive question answering is the intended task
for this dataset. No leaderboard is active at this point.


### Languages

The dataset is available in Danish (`da`), Swedish (`sv`) and Norwegian (`no`).


## Dataset Structure

### Data Instances

- **Size of downloaded dataset files:** 69 MB
- **Size of the generated dataset:** 67 MB
- **Total amount of disk used:** 136 MB

An example from the `train` split of the `da` subset looks as follows.
```
{
    'example_id': 123,
    'question': 'Er dette en test?',
    'answer': 'Dette er en test',
    'answer_start': 0,
    'context': 'Dette er en testkontekst.',
    'answer_en': 'This is a test',
    'answer_start_en': 0,
    'context_en': "This is a test context.",
    'title_en': 'Train test'
}
```

### Data Fields

The data fields are the same among all splits.

- `example_id`: an `int64` feature.
- `question`: a `string` feature.
- `answer`: a `string` feature.
- `answer_start`: an `int64` feature.
- `context`: a `string` feature.
- `answer_en`:  a `string` feature.
- `answer_start_en`: an `int64` feature.
- `context_en`: a `string` feature.
- `title_en`: a `string` feature.

### Data Splits

|   name   | train | validation | test |
|----------|------:|-----------:|-----:|
| da       | 6311  | 749        | 750  |
| sv       | 6299  | 750        | 749  |
| no       | 6314  | 749        | 750  |


## Dataset Creation

### Curation Rationale

The Scandinavian languages does not have any gold standard question answering dataset.
This is not quite gold standard, but the fact both the questions and answers are all
manually translated, it is a solid silver standard dataset.

### Source Data

The original data was collected from the [MKQA](https://github.com/apple/ml-mkqa/) and
[Natural Questions](https://ai.google.com/research/NaturalQuestions) datasets from
Apple and Google, respectively.


## Additional Information

### Dataset Curators

[Dan Saattrup Nielsen](https://saattrupdan.github.io/) from the [The Alexandra
Institute](https://alexandra.dk/) curated this dataset.

### Licensing Information

The dataset is licensed under the [CC BY-SA 4.0
license](https://creativecommons.org/licenses/by-sa/4.0/).
