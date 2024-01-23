---
annotations_creators:
- machine-generated
- expert-generated
language_creators:
- found
language:
- en
size_categories:
- 1K<n<10K
source_datasets:
- original
task_categories:
- text-classification
task_ids:
- multi-class-classification
pretty_name: HoC
language_bcp47:
- en-US
---

# HoC : Hallmarks of Cancer Corpus

## Table of Contents
- [Dataset Card for [Needs More Information]](#dataset-card-for-needs-more-information)
  - [Table of Contents](#table-of-contents)
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
      - [Initial Data Collection and Normalization](#initial-data-collection-and-normalization)
      - [Who are the source language producers?](#who-are-the-source-language-producers)
    - [Personal and Sensitive Information](#personal-and-sensitive-information)
  - [Considerations for Using the Data](#considerations-for-using-the-data)
    - [Other Known Limitations](#other-known-limitations)
  - [Additional Information](#additional-information)
    - [Dataset Curators](#dataset-curators)
    - [Licensing Information](#licensing-information)
    - [No Warranty](#no-warranty)
    - [Citation Information](#citation-information)

## Dataset Description

- **Homepage:** https://s-baker.net/resource/hoc/
- **Repository:** https://github.com/sb895/Hallmarks-of-Cancer
- **Paper:** https://academic.oup.com/bioinformatics/article/32/3/432/1743783
- **Leaderboard:** https://paperswithcode.com/dataset/hoc-1
- **Point of Contact:** [Yanis Labrak](mailto:yanis.labrak@univ-avignon.fr)

### Dataset Summary

The Hallmarks of Cancer Corpus for text classification

The Hallmarks of Cancer (HOC) Corpus consists of 1852 PubMed publication abstracts manually annotated by experts according to a taxonomy. The taxonomy consists of 37 classes in a hierarchy. Zero or more class labels are assigned to each sentence in the corpus. The labels are found under the "labels" directory, while the tokenized text can be found under "text" directory. The filenames are the corresponding PubMed IDs (PMID).

In addition to the HOC corpus, we also have the [Cancer Hallmarks Analytics Tool](http://chat.lionproject.net/) which classifes all of PubMed according to the HoC taxonomy.

### Supported Tasks and Leaderboards

The dataset can be used to train a model for `multi-class-classification`.

### Languages

The corpora consists of PubMed article only in english:

- `English - United States (en-US)`

## Load the dataset with HuggingFace

```python
from datasets import load_dataset
dataset = load_dataset("qanastek/HoC")
validation = dataset["validation"]
print("First element of the validation set : ", validation[0])
```

## Dataset Structure

### Data Instances

```json
{
  "document_id": "12634122_5",
  "text": "Genes that were overexpressed in OM3 included oncogenes , cell cycle regulators , and those involved in signal transduction , whereas genes for DNA repair enzymes and inhibitors of transformation and metastasis were suppressed .",
  "label": [9, 5, 0, 6]
}
```

### Data Fields

`document_id`: Unique identifier of the document.

`text`: Raw text of the PubMed abstracts.

`label`: One of the 10 currently known hallmarks of cancer.

|                   Hallmark                  |                 Search term                 |
|:-------------------------------------------:|:-------------------------------------------:|
| 1. Sustaining proliferative signaling (PS)  |        Proliferation Receptor Cancer        |
|                                             |           'Growth factor' Cancer            |
|                                             |             'Cell cycle' Cancer             |
|     2. Evading growth suppressors (GS)      |             'Cell cycle' Cancer             |
|                                             |            'Contact inhibition'             |
|        3. Resisting cell death (CD)         |              Apoptosis Cancer               |
|                                             |               Necrosis Cancer               |
|                                             |              Autophagy Cancer               |
|  4. Enabling replicative immortality (RI)   |              Senescence Cancer              |
|                                             |           Immortalization Cancer            |
|        5. Inducing angiogenesis (A)         |             Angiogenesis Cancer             |
|                                             |             'Angiogenic factor'             |
|  6. Activating invasion & metastasis (IM)   |         Metastasis Invasion Cancer          |
|    7. Genome instability & mutation (GI)    |               Mutation Cancer               |
|                                             |             'DNA repair' Cancer             |
|                                             |               Adducts Cancer                |
|                                             |           'Strand breaks' Cancer            |
|                                             |             'DNA damage' Cancer             |
|    8. Tumor-promoting inflammation (TPI)    |             Inflammation Cancer             |
|                                             |          'Oxidative stress' Cancer          |
|                                             |    Inflammation 'Immune response' Cancer    |
|  9. Deregulating cellular energetics (CE)   | Glycolysis Cancer; 'Warburg effect' Cancer  |
|    10. Avoiding immune destruction (ID)     |           'Immune system' Cancer            |
|                                             |          Immunosuppression Cancer           |

### Data Splits

Distribution of data for the 10 hallmarks:

| **Hallmark** | **No. abstracts** | **No. sentences** |
|:------------:|:-----------------:|:-----------------:|
|    1. PS     |        462        |        993        |
|    2. GS     |        242        |        468        |
|    3. CD     |        430        |        883        |
|    4. RI     |        115        |        295        |
|     5. A     |        143        |        357        |
|    6. IM     |        291        |        667        |
|    7. GI     |        333        |        771        |
|    8. TPI    |        194        |        437        |
|    9. CE     |        105        |        213        |
|    10. ID    |        108        |        226        |

## Dataset Creation

### Source Data

#### Who are the source language producers?

The corpus has been produced and uploaded by Baker Simon and Silins Ilona and Guo Yufan and Ali Imran and Hogberg Johan and Stenius Ulla and Korhonen Anna.

### Personal and Sensitive Information

The corpora is free of personal or sensitive information.

## Additional Information

### Dataset Curators

__HoC__: Baker Simon and Silins Ilona and Guo Yufan and Ali Imran and Hogberg Johan and Stenius Ulla and Korhonen Anna

__Hugging Face__: Labrak Yanis (Not affiliated with the original corpus)

### Licensing Information

```plain
GNU General Public License v3.0
```

```plain
Permissions
- Commercial use
- Modification
- Distribution
- Patent use
- Private use
Limitations
- Liability
- Warranty
Conditions
- License and copyright notice
- State changes
- Disclose source
- Same license
```

### Citation Information

We would very much appreciate it if you cite our publications:

[Automatic semantic classification of scientific literature according to the hallmarks of cancer](https://academic.oup.com/bioinformatics/article/32/3/432/1743783)

```bibtex
@article{baker2015automatic,
  title={Automatic semantic classification of scientific literature according to the hallmarks of cancer},
  author={Baker, Simon and Silins, Ilona and Guo, Yufan and Ali, Imran and H{\"o}gberg, Johan and Stenius, Ulla and Korhonen, Anna},
  journal={Bioinformatics},
  volume={32},
  number={3},
  pages={432--440},
  year={2015},
  publisher={Oxford University Press}
}
```

[Cancer Hallmarks Analytics Tool (CHAT): a text mining approach to organize and evaluate scientific literature on cancer](https://www.repository.cam.ac.uk/bitstream/handle/1810/265268/btx454.pdf?sequence=8&isAllowed=y)

```bibtex
@article{baker2017cancer,
  title={Cancer Hallmarks Analytics Tool (CHAT): a text mining approach to organize and evaluate scientific literature on cancer},
  author={Baker, Simon and Ali, Imran and Silins, Ilona and Pyysalo, Sampo and Guo, Yufan and H{\"o}gberg, Johan and Stenius, Ulla and Korhonen, Anna},
  journal={Bioinformatics},
  volume={33},
  number={24},
  pages={3973--3981},
  year={2017},
  publisher={Oxford University Press}
}
```

[Cancer hallmark text classification using convolutional neural networks](https://www.repository.cam.ac.uk/bitstream/handle/1810/270037/BIOTXTM2016.pdf?sequence=1&isAllowed=y)

```bibtex
@article{baker2017cancer,
  title={Cancer hallmark text classification using convolutional neural networks},
  author={Baker, Simon and Korhonen, Anna-Leena and Pyysalo, Sampo},
  year={2016}
}
```

[Initializing neural networks for hierarchical multi-label text classification](http://www.aclweb.org/anthology/W17-2339)

```bibtex
@article{baker2017initializing,
  title={Initializing neural networks for hierarchical multi-label text classification},
  author={Baker, Simon and Korhonen, Anna},
  journal={BioNLP 2017},
  pages={307--315},
  year={2017}
}
```
