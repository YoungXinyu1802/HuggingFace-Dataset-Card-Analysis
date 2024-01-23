---
annotations_creators:
- no-annotation
language_creators:
- crowdsourced
language:
- da
license:
- cc-by-4.0
multilinguality:
- monolingual
size_categories:
- unknown
source_datasets:
- original
task_categories:
- text-generation
task_ids:
- language-modeling
pretty_name: Danish Gigaword Corpus (no Twitter)
language_bcp47:
- da
- da-bornholm
- da-synnejyl
---

# Dataset Card for [Danish Gigaword (no Twitter)]

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
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

- **Homepage:**
https://gigaword.dk
- **Paper:**
http://www.derczynski.com/papers/dagw.pdf

### Dataset Summary

The Danish Gigaword Corpus contains text spanning several domains and forms. This version does *not* include the sections containing Tweets.

### Supported Tasks and Leaderboards

Pre-training of language models.

### Language

Danish

## Dataset Structure

The dataset contains text from 23 different sources which are thoroughly defined in [Source Data](#source-data). See the [homepage](https://gigaword.dk) or [paper](http://www.derczynski.com/papers/dagw.pdf) for more information. 

### Data Instances

Each entry in the dataset consists of a single text with associated metadata

### Data Fields

An entry in the dataset consists of the following fields:

- `text`(`str`): The content of the document.
- `source` (`str`): The source of the document (see [Source Data](#source-data)).
- `doc_id` (`str`): An unique identifer for each document.
- `LICENSE` (`str`): The license of the document. The licenses vary according to the source. 
- `uri` (`str`): The uri of the document. Not available for all sources.
- `data_built`(`str`): Date the document was built. Not avaialable for all sources. 


### Data Splits

The entire corpus is provided in the `train` split.

## Dataset Creation

### Source Data

Below follows a brief overview of the sources in the corpus along with their individual license.

| Source            | License                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| adl               | Creative Commons Legal Code 1.0 Universal                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| botxt             | Creative Commons Legal Code 1.0 Universal                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| cc                | Creative Commons Legal Code 1.0 Universal                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| danavis           | Creative Commons Legal Code 1.0 Universal                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| dannet            | [dannet license](https://cst.ku.dk/projekter/dannet/license.txt)                                                                                                                                                                                                                                                                                                                                                                                                                    |
| depbank           | Attribution-ShareAlike 4.0 International                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ep                | Creative Commons Legal Code 1.0 Universal                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ft                | Creative Commons Legal Code 1.0 Universal                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| gutenberg         | [gutenberg license](https://www.gutenberg.org/policy/license.html)                                                                                                                                                                                                                                                                                                                                                                                                                  |
| hest              | Creative Commons Legal Code 1.0 Universal                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| jvj               | Attribution-ShareAlike 4.0 International                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| naat              | Creative Commons Legal Code 1.0 Universal                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| opensub           | The data set comes with the same license as the original sources. Please, check the information about the source that is given on http://opus.nlpl.eu/OpenSubtitles-v2018.php                                                                                                                                                                                                                                                                                                       |
| relig             | Creative Commons Legal Code 1.0 Universal                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| retsinformationdk | Danish Copyright law at https://www.retsinformation.dk/forms/r0710.aspx?id=164796 states "§ 9. Love, administrative forskrifter, retsafgørelser og lignende offentlige aktstykker er ikke genstand for ophavsret. Stk. 2. Bestemmelsen i stk. 1 gælder ikke for værker, der fremtræder som selvstændige bidrag i de i stk. 1 nævnte aktstykker. Sådanne værker må dog gengives i forbindelse med aktstykket. Retten til videre udnyttelse afhænger af de i øvrigt gældende regler." |
| retspraksis       | Creative Commons Legal Code 1.0 Universal                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| skat              | Creative Commons Legal Code 1.0 Universal                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| spont             | Creative Commons Legal Code 1.0 Universal                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| synne             | Creative Commons Legal Code 1.0 Universal                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| tv2r              | The owner of this content is TV2 Regionerne, Denmark. Creative Commons Attribution 4.0 International                                                                                                                                                                                                                                                                                                                                                                                |
| wiki              | Creative Commons Legal Code 1.0 Universal                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| wikibooks         | Creative Commons Legal Code 1.0 Universal                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| wikisource        | Creative Commons Legal Code 1.0 Universal                                                                                                                                                                                                                                                                                                                                                                                                                                           |



## Additional Information

### Licensing Information

If you use the data, you MUST acknowledge it. The license is CC-BY 4.0, Creative Commons with Attribution. 


### Citation Information

 Sample attributions:
In a press release:

> Modellen er præ-trænet på et datasæt fra The Danish Gigaword Project (https://gigaword.dk), der er udviklet af forskere fra IT-Universitetet i København
> The model is pre-trained using the Danish Gigaword Corpus (https://gigaword.dk), developed at the IT University of Copenhagen

In academic writing:

```
Derczynski, L., Ciosici, M. R., et al. (2021). The Danish Gigaword Corpus. In Proceedings of the 23rd Nordic Conference on Computational Linguistics (NoDaLiDa 2021).
@inproceedings{dagw,
 title = {{The Danish Gigaword Corpus}},
 author = {Leon Derczynski and Manuel R. Ciosici and Rebekah Baglini and Morten H. Christiansen and Jacob Aarup Dalsgaard and Riccardo Fusaroli and Peter Juel Henrichsen and Rasmus Hvingelby and Andreas Kirkedal and Alex Speed Kjeldsen and Claus Ladefoged and Finn Årup Nielsen and Jens Madsen and Malte Lau Petersen and Jonathan Hvithamar Rystrøm and Daniel Varab},
 year = 2021,
 booktitle = {Proceedings of the 23rd Nordic Conference on Computational Linguistics},
 publisher = {NEALT}
}
```

In a software product, tool, or service:

> Danish Gigaword Corpus: license - homepage

> Denne service er lavet med data fra The Danish Gigaword Corpus

### Contributions

Dataset created by Derczynski et al. (2021)

Derczynski, L., Ciosici, M. R., et al. (2021). The Danish Gigaword Corpus. In Proceedings of the 23rd Nordic Conference on Computational Linguistics (NoDaLiDa 2021).

Thanks to [@HLasse](https://github.com/HLasse) for adding this dataset to the Hugging Face Hub.