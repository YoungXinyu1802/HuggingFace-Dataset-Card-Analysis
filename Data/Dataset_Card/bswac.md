---
annotations_creators:
- no-annotation
language_creators:
- found
language:
- bs
license:
- cc-by-sa-3.0
multilinguality:
- monolingual
size_categories:
- 100M<n<1B
source_datasets:
- original
task_categories:
- text-generation
- fill-mask
task_ids:
- language-modeling
- masked-language-modeling
paperswithcode_id: null
pretty_name: BsWac
dataset_info:
  features:
  - name: sentence
    dtype: string
  config_name: bswac
  splits:
  - name: train
    num_bytes: 9156258478
    num_examples: 354581267
  download_size: 1988514951
  dataset_size: 9156258478
---

# Dataset Card for BsWac

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

- **Homepage:** http://nlp.ffzg.hr/resources/corpora/bswac/
- **Repository:** https://www.clarin.si/repository/xmlui/handle/11356/1062
- **Paper:** http://nlp.ffzg.hr/data/publications/nljubesi/ljubesic14-bs.pdf
- **Leaderboard:**
- **Point of Contact:** [Nikola Ljubešič](mailto:nikola.ljubesic@ffzg.hr)

### Dataset Summary

The Bosnian web corpus bsWaC was built by crawling the .ba top-level domain in 2014. The corpus was near-deduplicated on paragraph level, normalised via diacritic restoration, morphosyntactically annotated and lemmatised. The corpus is shuffled by paragraphs. Each paragraph contains metadata on the URL, domain and language identification (Bosnian vs. Croatian vs. Serbian).
### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

Dataset is monolingual in Bosnian language.

## Dataset Structure

### Data Instances

[More Information Needed]

### Data Fields

[More Information Needed]

### Data Splits

[More Information Needed]

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

[More Information Needed]

### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

[More Information Needed]

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

[More Information Needed]

### Licensing Information

Dataset is under the [CC-BY-SA 3.0](http://creativecommons.org/licenses/by-sa/3.0/) license.

### Citation Information

```
  @misc{11356/1062,
 title = {Bosnian web corpus {bsWaC} 1.1},
 author = {Ljube{\v s}i{\'c}, Nikola and Klubi{\v c}ka, Filip},
 url = {http://hdl.handle.net/11356/1062},
 note = {Slovenian language resource repository {CLARIN}.{SI}},
 copyright = {Creative Commons - Attribution-{ShareAlike} 4.0 International ({CC} {BY}-{SA} 4.0)},
 year = {2016} }
```

### Contributions

Thanks to [@IvanZidov](https://github.com/IvanZidov) for adding this dataset.