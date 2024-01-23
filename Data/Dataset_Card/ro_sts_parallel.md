---
annotations_creators:
- crowdsourced
language_creators:
- crowdsourced
language:
- en
- ro
license:
- cc-by-4.0
multilinguality:
- multilingual
size_categories:
- 10K<n<100K
source_datasets:
- extended|other-sts-b
task_categories:
- translation
task_ids: []
paperswithcode_id: null
pretty_name: RO-STS-Parallel
dataset_info:
- config_name: ro_sts_parallel
  features:
  - name: translation
    dtype:
      translation:
        languages:
        - ro
        - en
  splits:
  - name: train
    num_bytes: 1563909
    num_examples: 11499
  - name: validation
    num_bytes: 443787
    num_examples: 3001
  - name: test
    num_bytes: 347590
    num_examples: 2759
  download_size: 2251694
  dataset_size: 2355286
- config_name: rosts-parallel-en-ro
  features:
  - name: translation
    dtype:
      translation:
        languages:
        - en
        - ro
  splits:
  - name: train
    num_bytes: 1563909
    num_examples: 11499
  - name: validation
    num_bytes: 443787
    num_examples: 3001
  - name: test
    num_bytes: 347590
    num_examples: 2759
  download_size: 2251694
  dataset_size: 2355286
---

# Dataset Card for RO-STS-Parallel

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

- **Homepage:** [GitHub](https://github.com/dumitrescustefan/RO-STS)
- **Repository:** [GitHub](https://github.com/dumitrescustefan/RO-STS)
- **Paper:** [Needs More Information]
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [email](dumitrescu.stefan@gmail.com)

### Dataset Summary

We present RO-STS-Parallel - a Parallel Romanian-English dataset obtained by translating the [STS English dataset](https://ixa2.si.ehu.eus/stswiki/index.php/STSbenchmark) dataset into Romanian. It contains 17256 sentences in Romanian and English.

### Supported Tasks and Leaderboards

[Needs More Information]

### Languages

The text dataset is in Romanian and English (`ro`, `en`)

## Dataset Structure

### Data Instances

An example looks like this:

```
{
  'translation': {
    'ro': 'Problema e si mai simpla.',
    'en': 'The problem is simpler than that.'
    }
}
```

### Data Fields

- translation:
  - ro: text in Romanian
  - en: text in English

### Data Splits

The train/validation/test split contain 11,498/3,000/2,758 sentence pairs.

## Dataset Creation

### Curation Rationale

### Source Data

#### Initial Data Collection and Normalization

*To construct the dataset, we first obtained automatic translations using Google's translation engine. These were then manually checked, corrected, and cross-validated by human volunteers. *

#### Who are the source language producers?

[Needs More Information]

### Annotations

#### Annotation process

#### Who are the annotators?

### Personal and Sensitive Information

[Needs More Information]

## Considerations for Using the Data

### Social Impact of Dataset

[Needs More Information]

### Discussion of Biases

[Needs More Information]

### Other Known Limitations

[Needs More Information]

## Additional Information

### Dataset Curators

[Needs More Information]

### Licensing Information

CC BY-SA 4.0 License

### Citation Information

```
@inproceedings{dumitrescu2021liro,
  title={Liro: Benchmark and leaderboard for romanian language tasks},
  author={Dumitrescu, Stefan Daniel and Rebeja, Petru and Lorincz, Beata and Gaman, Mihaela and Avram, Andrei and Ilie, Mihai and Pruteanu, Andrei and Stan, Adriana and Rosia, Lorena and Iacobescu, Cristina and others},
  booktitle={Thirty-fifth Conference on Neural Information Processing Systems Datasets and Benchmarks Track (Round 1)},
  year={2021}
}
```

### Contributions

Thanks to [@lorinczb](https://github.com/lorinczb) for adding this dataset.