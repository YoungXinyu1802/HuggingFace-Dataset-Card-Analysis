---
annotations_creators:
- expert-generated
language_creators:
- expert-generated
language:
- en
license:
- cc-by-4.0
multilinguality:
- monolingual
size_categories:
- 10K<n<100K
source_datasets: []
task_categories:
  - text-classification
  - structure-prediction
  - text-classification
task_ids:
  - multi-class-classification
  - named-entity-recognition
  - parsing
---

# Dataset Card for sd-nlp

## Table of Contents
- [Dataset Card for [Dataset Name]](#dataset-card-for-dataset-name)
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
    - [Annotations](#annotations)
      - [Annotation process](#annotation-process)
      - [Who are the annotators?](#who-are-the-annotators)
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

- **Homepage:** https://sourcedata.embo.org
- **Repository:** https://github.com/source-data/soda-roberta
- **Paper:**
- **Leaderboard:**
- **Point of Contact:** thomas.lemberger@embo.org

### Dataset Summary

This dataset is based on the content of the SourceData (https://sourcedata.embo.org) database, which contains manually annotated figure legends written in English and extracted from scientific papers in the domain of cell and molecular biology (Liechti et al, Nature Methods, 2017, https://doi.org/10.1038/nmeth.4471). 

The dataset is pre-tokenized with the `roberta-base` tokenizer. 

Additional details at https://github.com/source-data/soda-roberta

### Supported Tasks and Leaderboards

Tags are provided as [IOB2-style tags](https://en.wikipedia.org/wiki/Inside%E2%80%93outside%E2%80%93beginning_(tagging)).

`PANELIZATION`: figure captions (or figure legends) are usually composed of segments that each refer to one of several 'panels' of the full figure. Panels tend to represent results obtained with a coherent method and depicts data points that can be meaningfully compared to each other. `PANELIZATION` provide the start (B-PANEL_START) of these segments and allow to train for recogntion of the boundary between consecutive panel lengends.

`NER`: biological and chemical entities are labeled. Specifically the following entities are tagged:
- `SMALL_MOLECULE`: small molecules
- `GENEPROD`: gene products (genes and proteins)
- `SUBCELLULAR`: subcellular components
- `CELL`: cell types and cell lines.
- `TISSUE`: tissues and organs
- `ORGANISM`: species
- `EXP_ASSAY`: experimental assays

`ROLES`: the role of entities with regard to the causal hypotheses tested in the reported results. The tags are:
- `CONTROLLED_VAR`: entities that are associated with experimental variables and that subjected to controlled and targeted perturbations.
- `MEASURED_VAR`: entities that are associated with the variables measured and the object of the measurements.

`BORING`: entities are marked with the tag `BORING` when they are more of descriptive value and not directly associated with causal hypotheses ('boring' is not an ideal choice of word, but it is short...). Typically, these entities are so-called 'reporter' geneproducts, entities used as common baseline across samples, or specify the context of the experiment (cellular system, species, etc...).


### Languages

The text in the dataset is English.

## Dataset Structure

### Data Instances

```json
{
    "tokens": [
        "<s>", "Figure", "\u01205", ".", "\u0120Figure", "\u01205", ".", "A", "\u0120ER", "p", "57", "fl", "ox", "/", "fl", "ox", "\u0120mice", "\u0120were", "\u0120crossed", "\u0120with", "\u0120Nest", "in", "\u0120Cre", "\u0120trans", "genic", "\u0120mice", "\u0120to", "\u0120generate", "\u0120nervous", "\u0120system", "\u0120specific", "\u0120ER", "p", "57", "\u0120deficient", "\u0120animals", ".", "\u0120The", "\u0120levels", "\u0120of", "\u0120ER", "p", "57", "\u0120protein", "\u0120in", "\u0120the", "\u0120spinal", "\u0120cord", "\u0120were", "\u0120monitored", "\u0120by", "\u0120Western", "\u0120blot", ".", "\u0120ER", "p", "57", "WT", "\u0120(", "n", "=", "4", "),", "\u0120ER", "p", "57", "N", "es", "+", "/-", "\u0120(", "n", "=", "5", ")", "\u0120and", "\u0120ER", "p", "57", "N", "es", "-", "/-", "\u0120(", "n", "=", "4", ")", "\u0120mice", ".", "\u0120H", "SP", "90", "\u0120levels", "\u0120were", "\u0120determined", "\u0120as", "\u0120a", "\u0120loading", "\u0120control", ".", "\u0120Right", "\u0120panel", ":", "\u0120Quant", "ification", "\u0120of", "\u0120ER", "p", "57", "\u0120levels", "\u0120was", "\u0120performed", "\u0120relative", "\u0120to", "\u0120H", "sp", "90", "\u0120levels", ".", "\u0120B", "\u0120Body", "\u0120weight", "\u0120measurements", "\u0120were", "\u0120performed", "\u0120for", "\u0120indicated", "\u0120time", "\u0120points", "\u0120in", "\u0120ER", "p", "57", "WT", "\u0120(", "n", "=", "50", "),", "\u0120ER", "p", "57", "N", "es", "+", "/-", "\u0120(", "n", "=", "32", ")", "\u0120and", "\u0120ER", "p", "57", "N", "es", "-", "/-", "\u0120(", "n", "=", "19", ")", "\u0120mice", ".", "\u0120C", "\u0120Rot", "ar", "od", "\u0120performance", "\u0120was", "\u0120performed", "\u0120ER", "p", "57", "WT", "\u0120(", "n", "=", "20", "),", "\u0120ER", "p", "57", "N", "es", "+", "/-", "\u0120(", "n", "=", "15", ")", "\u0120and", "\u0120ER", "p", "57", "N", "es", "-", "/-", "\u0120(", "n", "=", "8", ")", "\u0120mice", ".", "\u0120D", "\u0120H", "anging", "\u0120test", "\u0120performance", "\u0120was", "\u0120assessed", "\u0120in", "\u0120ER", "p", "57", "WT", "\u0120(", "n", "=", "41", "),", "\u0120ER", "p", "57", "N", "es", "+", "/-", "\u0120(", "n", "=", "32", ")", "\u0120and", "\u0120ER", "p", "57", "N", "es", "-", "/-", "\u0120(", "n", "=", "12", ")", "\u0120mice", ".", "\u0120E", "\u0120Kaplan", "-", "Me", "ier", "\u0120survival", "\u0120curve", "\u0120for", "\u0120ER", "p", "57", "N", "es", "-", "/-", "\u0120mice", "\u0120(", "N", "\u0120=", "\u012019", ")", "\u0120that", "\u0120prematurely", "\u0120died", "\u0120or", "\u0120had", "\u0120to", "\u0120be", "\u0120sacrificed", "\u0120because", "\u0120of", "\u0120health", "\u0120reasons", "\u0120between", "\u0120the", "\u0120ages", "\u012022", "\u0120and", "\u012073", "\u0120days", ".", "\u0120Mean", "\u0120survival", "\u0120of", "\u0120this", "\u0120sub", "group", "\u0120of", "\u0120animals", "\u0120was", "\u012057", "\u0120days", ".", "\u0120ER", "p", "57", "WT", "\u0120(", "n", "=", "50", ")", "\u0120and", "\u0120ER", "p", "57", "N", "es", "+", "/-", "\u0120(", "n", "=", "32", ")", "\u0120mice", "\u0120are", "\u0120shown", "\u0120as", "\u0120a", "\u0120reference", ".", "\u0120F", "\u0120Hist", "ological", "\u0120analysis", "\u0120of", "\u0120Ne", "u", "N", "\u0120and", "\u0120GF", "AP", "\u0120st", "aining", "\u0120was", "\u0120performed", "\u0120in", "\u0120spinal", "\u0120cord", "\u0120tissue", "\u0120from", "\u0120ER", "p", "57", "WT", "\u0120and", "\u0120ER", "p", "57", "N", "es", "-", "/-", "\u0120mice", "\u0120in", "\u0120three", "\u0120animals", "\u0120per", "\u0120group", "\u0120using", "\u0120indirect", "\u0120immun", "of", "lu", "orescence", ".", "\u0120The", "\u0120nucleus", "\u0120was", "\u0120stained", "\u0120with", "\u0120H", "oe", "ch", "st", ".", "\u0120Representative", "\u0120images", "\u0120from", "\u0120one", "\u0120mouse", "\u0120per", "\u0120group", "\u0120are", "\u0120shown", ".", "\u0120Scale", "\u0120bar", ":", "\u012050", "\u0120\u00ce\u00bc", "m", ".", "\u0120G", "\u0120St", "ere", "ological", "\u0120analysis", "\u0120of", "\u0120the", "\u0120spinal", "\u0120cord", "\u0120from", "\u0120ER", "p", "57", "WT", "\u0120(", "n", "\u0120=", "\u01204", "),", "\u0120ER", "p", "57", "N", "es", "+", "/-", "\u0120(", "n", "\u0120=", "\u01204", ")", "\u0120and", "\u0120ER", "p", "57", "N", "es", "-", "/-", "\u0120(", "n", "\u0120=", "\u01204", ")", "\u0120mice", ".", "\u0120Alternate", "\u0120series", "\u0120of", "\u0120sections", "\u0120from", "\u0120the", "\u0120spinal", "\u0120cord", "\u0120of", "\u0120the", "\u0120mice", "\u0120were", "\u0120either", "\u0120stained", "\u0120for", "\u0120N", "iss", "l", "\u0120(", "top", "\u0120row", "\u0120images", ")", "\u0120or", "\u0120processed", "\u0120for", "\u0120immun", "oh", "ist", "ochemistry", "\u0120for", "\u0120the", "\u0120ch", "olin", "ergic", "\u0120cell", "\u0120marker", "\u0120Ch", "oline", "\u0120Ac", "et", "yl", "\u0120Transfer", "ase", "\u0120(", "Ch", "AT", ",", "\u0120bottom", "\u0120row", "\u0120images", ").", "\u0120The", "\u0120nucle", "oli", "\u0120of", "\u0120the", "</s>"
    ],
    "input_ids": [
        0, 40683, 195, 4, 17965, 195, 4, 250, 13895, 642, 4390, 4825, 4325, 73, 4825, 4325, 15540, 58, 7344, 19, 12786, 179, 12022, 6214, 44131, 15540, 7, 5368, 7464, 467, 2167, 13895, 642, 4390, 38396, 3122, 4, 20, 1389, 9, 13895, 642, 4390, 8276, 11, 5, 21431, 13051, 58, 14316, 30, 2027, 39144, 4, 13895, 642, 4390, 25982, 36, 282, 5214, 306, 238, 13895, 642, 4390, 487, 293, 2744, 40398, 36, 282, 5214, 245, 43, 8, 13895, 642, 4390, 487, 293, 12, 40398, 36, 282, 5214, 306, 43, 15540, 4, 289, 4186, 3248, 1389, 58, 3030, 25, 10, 16761, 797, 4, 5143, 2798, 35, 28256, 5000, 9, 13895, 642, 4390, 1389, 21, 3744, 5407, 7, 289, 4182, 3248, 1389, 4, 163, 13048, 2408, 19851, 58, 3744, 13, 4658, 86, 332, 11, 13895, 642, 4390, 25982, 36, 282, 5214, 1096, 238, 13895, 642, 4390, 487, 293, 2744, 40398, 36, 282, 5214, 2881, 43, 8, 13895, 642, 4390, 487, 293, 12, 40398, 36, 282, 5214, 1646, 43, 15540, 4, 230, 9104, 271, 1630, 819, 21, 3744, 13895, 642, 4390, 25982, 36, 282, 5214, 844, 238, 13895, 642, 4390, 487, 293, 2744, 40398, 36, 282, 5214, 996, 43, 8, 13895, 642, 4390, 487, 293, 12, 40398, 36, 282, 5214, 398, 43, 15540, 4, 211, 289, 23786, 1296, 819, 21, 11852, 11, 13895, 642, 4390, 25982, 36, 282, 5214, 4006, 238, 13895, 642, 4390, 487, 293, 2744, 40398, 36, 282, 5214, 2881, 43, 8, 13895, 642, 4390, 487, 293, 12, 40398, 36, 282, 5214, 1092, 43, 15540, 4, 381, 25353, 12, 5096, 906, 7967, 9158, 13, 13895, 642, 4390, 487, 293, 12, 40398, 15540, 36, 487, 5457, 753, 43, 14, 30088, 962, 50, 56, 7, 28, 26936, 142, 9, 474, 2188, 227, 5, 4864, 820, 8, 6521, 360, 4, 30750, 7967, 9, 42, 2849, 13839, 9, 3122, 21, 4981, 360, 4, 13895, 642, 4390, 25982, 36, 282, 5214, 1096, 43, 8, 13895, 642, 4390, 487, 293, 2744, 40398, 36, 282, 5214, 2881, 43, 15540, 32, 2343, 25, 10, 5135, 4, 274, 31862, 9779, 1966, 9, 3864, 257, 487, 8, 32727, 591, 1690, 8173, 21, 3744, 11, 21431, 13051, 11576, 31, 13895, 642, 4390, 25982, 8, 13895, 642, 4390, 487, 293, 12, 40398, 15540, 11, 130, 3122, 228, 333, 634, 18677, 13998, 1116, 6487, 45094, 4, 20, 38531, 21, 31789, 19, 289, 3540, 611, 620, 4, 10308, 3156, 31, 65, 18292, 228, 333, 32, 2343, 4, 33256, 2003, 35, 654, 46911, 119, 4, 272, 312, 2816, 9779, 1966, 9, 5, 21431, 13051, 31, 13895, 642, 4390, 25982, 36, 282, 5457, 204, 238, 13895, 642, 4390, 487, 293, 2744, 40398, 36, 282, 5457, 204, 43, 8, 13895, 642, 4390, 487, 293, 12, 40398, 36, 282, 5457, 204, 43, 15540, 4, 43510, 651, 9, 9042, 31, 5, 21431, 13051, 9, 5, 15540, 58, 1169, 31789, 13, 234, 3006, 462, 36, 8766, 3236, 3156, 43, 50, 12069, 13, 13998, 2678, 661, 39917, 13, 5, 1855, 21716, 44858, 3551, 17540, 732, 18675, 6208, 594, 4360, 18853, 3175, 36, 4771, 2571, 6, 2576, 3236, 3156, 322, 20, 38898, 6483, 9, 5, 2
    ], 
    "label_ids": {
        "entity_types": [
            "O", "O", "O", "O", "O", "O", "O", "O", "B-GENEPROD", "I-GENEPROD", "I-GENEPROD", "O", "O", "O", "O", "O", "B-ORGANISM", "O", "O", "O", "B-GENEPROD", "I-GENEPROD", "B-GENEPROD", "O", "O", "B-ORGANISM", "O", "O", "O", "O", "O", "B-GENEPROD", "I-GENEPROD", "I-GENEPROD", "O", "O", "O", "O", "O", "O", "B-GENEPROD", "I-GENEPROD", "I-GENEPROD", "O", "O", "O", "B-TISSUE", "I-TISSUE", "O", "O", "O", "B-EXP_ASSAY", "I-EXP_ASSAY", "O", "B-GENEPROD", "I-GENEPROD", "I-GENEPROD", "O", "O", "O", "O", "O", "O", "B-GENEPROD", "I-GENEPROD", "I-GENEPROD", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-GENEPROD", "I-GENEPROD", "I-GENEPROD", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-ORGANISM", "O", "B-GENEPROD", "I-GENEPROD", "I-GENEPROD", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-GENEPROD", "I-GENEPROD", "I-GENEPROD", "O", "O", "O", "O", "O", "B-GENEPROD", "I-GENEPROD", "I-GENEPROD", "O", "O", "O", "B-EXP_ASSAY", "I-EXP_ASSAY", "I-EXP_ASSAY", "O", "O", "O", "O", "O", "O", "O", "B-GENEPROD", "I-GENEPROD", "I-GENEPROD", "O", "O", "O", "O", "O", "O", "B-GENEPROD", "I-GENEPROD", "I-GENEPROD", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-GENEPROD", "I-GENEPROD", "I-GENEPROD", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-ORGANISM", "O", "O", "O", "O", "O", "O", "O", "O", "B-GENEPROD", "I-GENEPROD", "I-GENEPROD", "O", "O", "O", "O", "O", "O", "B-GENEPROD", "I-GENEPROD", "I-GENEPROD", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-GENEPROD", "I-GENEPROD", "I-GENEPROD", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-ORGANISM", "O", "O", "B-EXP_ASSAY", "I-EXP_ASSAY", "I-EXP_ASSAY", "O", "O", "O", "O", "B-GENEPROD", "I-GENEPROD", "I-GENEPROD", "O", "O", "O", "O", "O", "O", "B-GENEPROD", "I-GENEPROD", "I-GENEPROD", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-GENEPROD", "I-GENEPROD", "I-GENEPROD", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-ORGANISM", "O", "O", "O", "O", "O", "O", "B-EXP_ASSAY", "O", "O", "B-GENEPROD", "I-GENEPROD", "I-GENEPROD", "O", "O", "O", "O", "B-ORGANISM", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-EXP_ASSAY", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-GENEPROD", "I-GENEPROD", "I-GENEPROD", "O", "O", "O", "O", "O", "O", "O", "B-GENEPROD", "I-GENEPROD", "I-GENEPROD", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-ORGANISM", "O", "O", "O", "O", "O", "O", "O", "B-EXP_ASSAY", "I-EXP_ASSAY", "I-EXP_ASSAY", "O", "B-GENEPROD", "I-GENEPROD", "I-GENEPROD", "O", "B-GENEPROD", "I-GENEPROD", "O", "O", "O", "O", "O", "B-TISSUE", "I-TISSUE", "O", "O", "B-GENEPROD", "I-GENEPROD", "I-GENEPROD", "O", "O", "B-GENEPROD", "I-GENEPROD", "I-GENEPROD", "O", "O", "O", "O", "B-ORGANISM", "O", "O", "O", "O", "O", "O", "B-EXP_ASSAY", "I-EXP_ASSAY", "I-EXP_ASSAY", "I-EXP_ASSAY", "I-EXP_ASSAY", "O", "O", "B-SUBCELLULAR", "O", "O", "O", "B-EXP_ASSAY", "I-EXP_ASSAY", "I-EXP_ASSAY", "I-EXP_ASSAY", "O", "O", "O", "O", "O", "B-ORGANISM", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-EXP_ASSAY", "I-EXP_ASSAY", "I-EXP_ASSAY", "I-EXP_ASSAY", "O", "O", "B-TISSUE", "I-TISSUE", "O", "B-GENEPROD", "I-GENEPROD", "I-GENEPROD", "O", "O", "O", "O", "O", "O", "B-GENEPROD", "I-GENEPROD", "I-GENEPROD", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-GENEPROD", "I-GENEPROD", "I-GENEPROD", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-ORGANISM", "O", "O", "O", "O", "O", "O", "O", "B-TISSUE", "I-TISSUE", "O", "O", "B-ORGANISM", "O", "O", "O", "O", "B-SUBCELLULAR", "I-SUBCELLULAR", "I-SUBCELLULAR", "O", "O", "O", "O", "O", "O", "O", "O", "B-EXP_ASSAY", "I-EXP_ASSAY", "I-EXP_ASSAY", "I-EXP_ASSAY", "O", "O", "O", "O", "O", "O", "O", "B-GENEPROD", "I-GENEPROD", "I-GENEPROD", "I-GENEPROD", "I-GENEPROD", "I-GENEPROD", "I-GENEPROD", "O", "B-GENEPROD", "I-GENEPROD", "O", "O", "O", "O", "O", "O", "B-SUBCELLULAR", "I-SUBCELLULAR", "O", "O", "O"
        ],
        "geneprod_roles": [
            "O", "O", "O", "O", "O", "O", "O", "O", "B-CONTROLLED_VAR", "I-CONTROLLED_VAR", "I-CONTROLLED_VAR", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-CONTROLLED_VAR", "I-CONTROLLED_VAR", "I-CONTROLLED_VAR", "O", "O", "O", "O", "O", "O", "B-CONTROLLED_VAR", "I-CONTROLLED_VAR", "I-CONTROLLED_VAR", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-CONTROLLED_VAR", "I-CONTROLLED_VAR", "I-CONTROLLED_VAR", "O", "O", "O", "O", "O", "O", "B-CONTROLLED_VAR", "I-CONTROLLED_VAR", "I-CONTROLLED_VAR", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-CONTROLLED_VAR", "I-CONTROLLED_VAR", "I-CONTROLLED_VAR", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-MEASURED_VAR", "I-MEASURED_VAR", "I-MEASURED_VAR", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-CONTROLLED_VAR", "I-CONTROLLED_VAR", "I-CONTROLLED_VAR", "O", "O", "O", "O", "O", "O", "B-CONTROLLED_VAR", "I-CONTROLLED_VAR", "I-CONTROLLED_VAR", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-CONTROLLED_VAR", "I-CONTROLLED_VAR", "I-CONTROLLED_VAR", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-CONTROLLED_VAR", "I-CONTROLLED_VAR", "I-CONTROLLED_VAR", "O", "O", "O", "O", "O", "O", "B-CONTROLLED_VAR", "I-CONTROLLED_VAR", "I-CONTROLLED_VAR", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-CONTROLLED_VAR", "I-CONTROLLED_VAR", "I-CONTROLLED_VAR", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-CONTROLLED_VAR", "I-CONTROLLED_VAR", "I-CONTROLLED_VAR", "O", "O", "O", "O", "O", "O", "B-CONTROLLED_VAR", "I-CONTROLLED_VAR", "I-CONTROLLED_VAR", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-CONTROLLED_VAR", "I-CONTROLLED_VAR", "I-CONTROLLED_VAR", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-CONTROLLED_VAR", "I-CONTROLLED_VAR", "I-CONTROLLED_VAR", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-CONTROLLED_VAR", "I-CONTROLLED_VAR", "I-CONTROLLED_VAR", "O", "O", "O", "O", "O", "O", "O", "B-CONTROLLED_VAR", "I-CONTROLLED_VAR", "I-CONTROLLED_VAR", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-MEASURED_VAR", "I-MEASURED_VAR", "I-MEASURED_VAR", "O", "B-MEASURED_VAR", "I-MEASURED_VAR", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-CONTROLLED_VAR", "I-CONTROLLED_VAR", "I-CONTROLLED_VAR", "O", "O", "B-CONTROLLED_VAR", "I-CONTROLLED_VAR", "I-CONTROLLED_VAR", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-CONTROLLED_VAR", "I-CONTROLLED_VAR", "I-CONTROLLED_VAR", "O", "O", "O", "O", "O", "O", "B-CONTROLLED_VAR", "I-CONTROLLED_VAR", "I-CONTROLLED_VAR", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-CONTROLLED_VAR", "I-CONTROLLED_VAR", "I-CONTROLLED_VAR", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-MEASURED_VAR", "I-MEASURED_VAR", "I-MEASURED_VAR", "I-MEASURED_VAR", "I-MEASURED_VAR", "I-MEASURED_VAR", "I-MEASURED_VAR", "O", "B-MEASURED_VAR", "I-MEASURED_VAR", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"
        ], 
        "boring": [
            "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-BORING", "O", "O", "O", "B-BORING", "I-BORING", "B-BORING", "O", "O", "B-BORING", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-BORING", "I-BORING", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-BORING", "O", "B-BORING", "I-BORING", "I-BORING", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-BORING", "I-BORING", "I-BORING", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-BORING", "I-BORING", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-BORING", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-BORING", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-BORING", "I-BORING", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-BORING", "O", "O", "O", "O", "O", "O", "O", "B-BORING", "I-BORING", "O", "O", "B-BORING", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"
        ], 
        "panel_start": [
            "O", "O", "O", "O", "O", "O", "O", "B-PANEL_START", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-PANEL_START", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-PANEL_START", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-PANEL_START", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-PANEL_START", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-PANEL_START", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"
        ]
    }
}
```

### Data Fields

- `input_ids`: token id in `roberta-base` tokenizers' vocabulary provided as a`list` of `int` 
- `label_ids`:
  - `entity_types`: `list` of `strings` for the IOB2 tags for entity type; possible value in `["O", "I-SMALL_MOLECULE",  "B-SMALL_MOLECULE",  "I-GENEPROD", "B-GENEPROD", "I-SUBCELLULAR", "B-SUBCELLULAR", "I-CELL", "B-CELL", "I-TISSUE", "B-TISSUE", "I-ORGANISM", "B-ORGANISM", "I-EXP_ASSAY", "B-EXP_ASSAY"]`
  - `geneprod_roles`: `list` of `strings` for the IOB2 tags for experimental roles; values in `["O", "I-CONTROLLED_VAR", "B-CONTROLLED_VAR", "I-MEASURED_VAR", "B-MEASURED_VAR"]`
  - `boring`: `list` of `strings` for IOB2 tags for entities unrelated to causal design; values in `["O", "I-BORING", "B-BORING"]`
  - `panel_start`: `list` of `strings` for IOB2 tags `["O", "B-PANEL_START"]`

### Data Splits

- train:
  - features: ['input_ids', 'labels', 'tag_mask'],
  - num_rows: 48_771
- test:
  - features: ['input_ids', 'labels', 'tag_mask'],
  - num_rows: 13_801
- validation:
  - features: ['input_ids', 'labels', 'tag_mask'],
  - num_rows: 7_178

## Dataset Creation

### Curation Rationale

The dataset was built to train models for the automatic extraction of a knowledge graph based from the scientific literature. The dataset can be used to train models for text segmentation, named entity recognition and semantic role labeling. 

### Source Data

#### Initial Data Collection and Normalization

Figure legends were annotated according to the SourceData framework described in Liechti et al 2017 (Nature Methods, 2017, https://doi.org/10.1038/nmeth.4471). The curation tool at https://curation.sourcedata.io was used to segment figure legends into panel legends, tag enities, assign experiemental roles and normalize with standard identifiers (not available in this dataset). The source data was downloaded from the SourceData API (https://api.sourcedata.io) on 21 Jan 2021.

#### Who are the source language producers?

The examples are extracted from the figure legends from scientific papers in cell and molecular biology. 

### Annotations

#### Annotation process

The annotations were produced manually with expert curators from the SourceData project (https://sourcedata.embo.org)

#### Who are the annotators?

Curators of the SourceData project.

### Personal and Sensitive Information

None known.

## Considerations for Using the Data

### Social Impact of Dataset

Not applicable.

### Discussion of Biases

The examples are heavily biased towards cell and molecular biology and are enriched in examples from papers published in EMBO Press journals (https://embopress.org)

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

Thomas Lemberger, EMBO.

### Licensing Information

CC BY 4.0

### Citation Information

[More Information Needed]

### Contributions

Thanks to [@tlemberger](https://github.com/tlemberger>) for adding this dataset.
