---
annotations_creators: []
language_creators:
- crowdsourced
- expert-generated
- machine-generated
- found
- other
language:
- asm-IN
- ben-IN
- brx-IN
- guj-IN
- hin-IN
- kan-IN
- kas-IN
- kok-IN
- mai-IN
- mal-IN
- mar-IN
- mni-IN
- nep-IN
- ori-IN
- pan-IN
- san-IN
- sid-IN
- tam-IN
- tel-IN
- urd-IN
license:
- cc-by-nc-4.0
multilinguality:
- multilingual
pretty_name: Aksharantar
size_categories: []
source_datasets:
- original
task_categories:
- text-generation
task_ids: []
---

# Dataset Card for Aksharantar

## Table of Contents
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

- **Homepage:** https://indicnlp.ai4bharat.org/indic-xlit/
- **Repository:** https://github.com/AI4Bharat/IndicXlit/
- **Paper:** [Aksharantar: Towards building open transliteration tools for the next billion users](https://arxiv.org/abs/2205.03018)
- **Leaderboard:**
- **Point of Contact:**

### Dataset Summary

Aksharantar is the largest publicly available transliteration dataset for 20 Indic languages. The corpus has 26M Indic language-English transliteration pairs.

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

| <!-- -->  	 | <!-- --> 	  | <!-- --> 	   | <!-- -->	     | <!-- -->       | <!-- -->      |
| -------------- | -------------- | -------------- | --------------- | -------------- | ------------- |
| Assamese (asm) | Hindi (hin) 	  | Maithili (mai) | Marathi (mar)   | Punjabi (pan)  | Tamil (tam)   |
| Bengali (ben)  | Kannada (kan)  | Malayalam (mal)| Nepali (nep)    | Sanskrit (san) | Telugu (tel)  | 
| Bodo(brx)      | Kashmiri (kas) | Manipuri (mni) | Oriya (ori)     | Sindhi (snd)   | Urdu (urd)    |
| Gujarati (guj) | Konkani (kok)  | 


## Dataset Structure


### Data Instances

```
A random sample from Hindi (hin) Train dataset.

{
'unique_identifier': 'hin1241393', 
'native word': 'स्वाभिमानिक', 
'english word': 'swabhimanik', 
'source': 'IndicCorp', 
'score': -0.1028788579
}

```

### Data Fields

- `unique_identifier` (string): 3-letter language code followed by a unique number in each set (Train, Test, Val).
- `native word` (string): A word in Indic language.
- `english word` (string): Transliteration of native word in English (Romanised word).
- `source` (string): Source of the data.
- `score` (num): Character level log probability of indic word given roman word by IndicXlit (model). Pairs with average threshold of the 0.35 are considered.

  For created data sources, depending on the destination/sampling method of a pair in a language, it will be one of:
  - Dakshina Dataset
  - IndicCorp 
  - Samanantar
  - Wikidata
  - Existing sources
  - Named Entities Indian (AK-NEI)
  - Named Entities Foreign (AK-NEF)
  - Data from Uniform Sampling method. (Ak-Uni)
  - Data from Most Frequent words sampling method. (Ak-Freq)
  
  
  
  
### Data Splits

| Subset | asm-en | ben-en | brx-en | guj-en | hin-en | kan-en | kas-en | kok-en | mai-en | mal-en | mni-en | mar-en | nep-en | ori-en | pan-en | san-en | sid-en | tam-en | tel-en | urd-en |
|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|
| Training | 179K | 1231K | 36K | 1143K | 1299K | 2907K | 47K | 613K | 283K | 4101K | 10K | 1453K | 2397K | 346K | 515K | 1813K | 60K | 3231K | 2430K | 699K |
| Validation | 4K | 11K | 3K | 12K | 6K | 7K | 4K | 4K | 4K | 8K | 3K | 8K | 3K | 3K | 9K | 3K | 8K | 9K | 8K | 12K |
| Test | 5531 | 5009 | 4136 | 7768 | 5693 | 6396 | 7707 | 5093 | 5512 | 6911 | 4925 | 6573 | 4133 | 4256 | 4316 | 5334 | - | 4682 | 4567 | 4463 |


## Dataset Creation

Information in the paper. [Aksharantar: Towards building open transliteration tools for the next billion users](https://arxiv.org/abs/2205.03018)

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

Information in the paper. [Aksharantar: Towards building open transliteration tools for the next billion users](https://arxiv.org/abs/2205.03018)

#### Who are the source language producers?

[More Information Needed]

### Annotations

Information in the paper. [Aksharantar: Towards building open transliteration tools for the next billion users](https://arxiv.org/abs/2205.03018)

#### Annotation process

Information in the paper. [Aksharantar: Towards building open transliteration tools for the next billion users](https://arxiv.org/abs/2205.03018)

#### Who are the annotators?

Information in the paper. [Aksharantar: Towards building open transliteration tools for the next billion users](https://arxiv.org/abs/2205.03018)

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

<!-- <a rel="license" float="left" href="http://creativecommons.org/publicdomain/zero/1.0/">
  <img src="https://licensebuttons.net/p/zero/1.0/88x31.png" style="border-style: none;" alt="CC0" width="100" />
  <img src="https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by.png" style="border-style: none;" alt="CC-BY" width="100" href="http://creativecommons.org/publicdomain/zero/1.0/"/>
</a>
<br/> -->


This data is released under the following licensing scheme:

- Manually collected data: Released under CC-BY license. 
- Mined dataset (from Samanantar and IndicCorp): Released under CC0 license. 
- Existing sources: Released under CC0 license. 

**CC-BY License**

<a rel="license" float="left" href="https://creativecommons.org/about/cclicenses/">
  <img src="https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by.png" style="border-style: none;" alt="CC-BY" width="100"/>
</a>

<br>
<br>
<!-- 
and the Aksharantar benchmark and all manually transliterated data under the [Creative Commons CC-BY license (“no rights reserved”)](https://creativecommons.org/licenses/by/4.0/). -->


**CC0 License Statement**

<a rel="license" float="left" href="https://creativecommons.org/about/cclicenses/">
  <img src="https://licensebuttons.net/p/zero/1.0/88x31.png" style="border-style: none;" alt="CC0" width="100"/>
</a>

<br>
<br>

- We do not own any of the text from which this data has been extracted.
- We license the actual packaging of the mined data under the [Creative Commons CC0 license (“no rights reserved”)](http://creativecommons.org/publicdomain/zero/1.0).
- To the extent possible under law, <a rel="dct:publisher" href="https://indicnlp.ai4bharat.org/aksharantar/"> <span property="dct:title">AI4Bharat</span></a> has waived all copyright and related or neighboring rights to <span property="dct:title">Aksharantar</span> manually collected data and existing sources.
- This work is published from: India.

### Citation Information

```
@misc{madhani2022aksharantar,
      title={Aksharantar: Towards Building Open Transliteration Tools for the Next Billion Users}, 
      author={Yash Madhani and Sushane Parthan and Priyanka Bedekar and Ruchi Khapra and Anoop Kunchukuttan and Pratyush Kumar and Mitesh Shantadevi Khapra},
      year={2022},
      eprint={},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

### Contributions

