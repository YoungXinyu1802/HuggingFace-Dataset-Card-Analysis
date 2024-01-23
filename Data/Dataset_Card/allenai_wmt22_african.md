# Dataset Card for allenai/wmt22_african

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

- **Homepage:** https://www.statmt.org/wmt22/large-scale-multilingual-translation-task.html
- **Repository:** [Needs More Information]
- **Paper:** [Needs More Information]
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [Needs More Information]

### Dataset Summary

This dataset was created based on [metadata](https://github.com/facebookresearch/LASER/tree/main/data/wmt22_african) for mined bitext released by Meta AI.  It contains bitext for 248 pairs for the African languages that are part of the [2022 WMT Shared Task on Large Scale Machine Translation Evaluation for African Languages](https://www.statmt.org/wmt22/large-scale-multilingual-translation-task.html).

#### How to use the data

There are two ways to access the data:

* Via the Hugging Face Python datasets library 

```
from datasets import load_dataset
dataset = load_dataset("allenai/wmt22_african")
```

* Clone the git repo
```
git lfs install
git clone https://huggingface.co/datasets/allenai/wmt22_african
```


### Supported Tasks and Leaderboards

This dataset is one of resources allowed under the Constrained Track for the [2022 WMT Shared Task on Large Scale Machine Translation Evaluation for African Languages](https://www.statmt.org/wmt22/large-scale-multilingual-translation-task.html).

### Languages

#### Focus languages

| Language | Code |
| -------- | ---- |
| Afrikaans | afr |
| Amharic | amh |
| Chichewa | nya |
| Nigerian Fulfulde | fuv |
| Hausa | hau |
| Igbo | ibo |
| Kamba | kam |
| Kinyarwanda | kin |
| Lingala | lin |
| Luganda | lug |
| Luo | luo |
| Northern Sotho | nso |
| Oroma | orm |
| Shona | sna |
| Somali | som |
| Swahili | swh |
| Swati | ssw |
| Tswana | tsn | 
| Umbundu | umb |
| Wolof | wol |
| Xhosa | xho |
| Xitsonga | tso |
| Yoruba | yor |
| Zulu | zul |

Colonial linguae francae: English - eng, French - fra

## Dataset Structure

The dataset contains gzipped tab delimited text files for each direction.  Each text file contains lines with parallel sentences.

### Data Instances

The dataset contains 248 language pairs.

Sentence counts for each pair can be found [here](https://huggingface.co/datasets/allenai/wmt22_african/blob/main/sentence_counts.txt).

### Data Fields

Every instance for a language pair contains the following fields: 'translation' (containing sentence pairs), 'laser_score', 'source_sentence_lid', 'target_sentence_lid', where 'lid' is language classification probability.

Example:
```
{
'translation': 
    {
        'afr': 'In Mei 2007, in ooreenstemming met die spesifikasies van die Java Gemeenskapproses, het Sun Java tegnologie geherlisensieer onder die GNU General Public License.', 
        'eng': 'As of May 2007, in compliance with the specifications of the Java Community Process, Sun relicensed most of its Java technologies under the GNU General Public License.'
    }, 
'laser_score': 1.0717015266418457, 
'source_sentence_lid': 0.9996600151062012, 
'target_sentence_lid': 0.9972000122070312
}
```
### Data Splits

The data is not split into train, dev, and test.

## Dataset Creation

### Curation Rationale

Parallel sentences from monolingual data in Common Crawl and ParaCrawl were identified via [Language-Agnostic Sentence Representation (LASER)](https://github.com/facebookresearch/LASER) encoders.

### Source Data

#### Initial Data Collection and Normalization

Monolingual data was obtained from Common Crawl and ParaCrawl.

#### Who are the source language producers?

Contributors to web text in Common Crawl and ParaCrawl.

### Annotations

#### Annotation process

The data was not human annotated. The metadata used to create the dataset can be found here: https://github.com/facebookresearch/LASER/tree/main/data/wmt22_african

#### Who are the annotators?

The data was not human annotated.  Parallel text from Common Crawl and Para Crawl monolingual data were identified automatically via [LASER](https://github.com/facebookresearch/LASER) encoders. 

### Personal and Sensitive Information

[Needs More Information]

## Considerations for Using the Data

### Social Impact of Dataset

This dataset provides data for training machine learning systems for many languages that have low resources available for NLP.

### Discussion of Biases

Biases in the data have not been studied.

### Other Known Limitations

[Needs More Information]

## Additional Information

### Dataset Curators

[Needs More Information]

### Licensing Information

The dataset is released under the terms of [ODC-BY](https://opendatacommons.org/licenses/by/1-0/). By using this, you are also bound by the Internet Archive [Terms of Use](https://archive.org/about/terms.php) in respect of the content contained in the dataset.

### Citation Information

NLLB Team et al, No Language Left Behind: Scaling Human-Centered Machine Translation, Arxiv, 2022.

### Contributions

We thank the AllenNLP team at AI2 for hosting and releasing this data, including [Akshita Bhagia](https://akshitab.github.io/) (for engineering efforts to create the huggingface dataset), and [Jesse Dodge](https://jessedodge.github.io/) (for organizing the connection).
