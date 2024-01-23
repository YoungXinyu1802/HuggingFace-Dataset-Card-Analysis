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
- token-classification
- text-classification
task_ids:
- multi-class-classification
- named-entity-recognition
- parsing
---
# Dataset Card for sd-nlp
## Table of Contents
- [Dataset Card for [EMBO/sd-nlp-non-tokenized]](#dataset-card-for-dataset-name)
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
- **Point of Contact:** thomas.lemberger@embo.org, jorge.abreu@embo.org

### Dataset Summary
This dataset is based on the content of the SourceData (https://sourcedata.embo.org) database, which contains manually annotated figure legends written in English and extracted from scientific papers in the domain of cell and molecular biology (Liechti et al, Nature Methods, 2017, https://doi.org/10.1038/nmeth.4471). 
Unlike the dataset [`sd-nlp`](https://huggingface.co/datasets/EMBO/sd-nlp), pre-tokenized with the `roberta-base` tokenizer, this dataset is not previously tokenized, but just splitted into words. Users can therefore use it to fine-tune other models. 
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
- `DISEASE`: diseases (see limitations)
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
    "words": [
        ".", "Figure", "6", "(", "A", ")", "Cisplatin", "dose", "response", "curves", "of", "(", "i", ")", "MB002", ",", "(", "ii", ")", "Daoy", ",", "and", "(", "iii", ")", "MIC", "in", "the", "absence", "(", "EV", ")", "or", "presence", "of", "SOX9", "by", "Alamar", "blue", ".", "Cells", "were", "pre", "-", "conditioned", "with", "doxycycline", "to", "induce", "expression", "of", "SOX9", "(", "or", "EV", ")", "prior", "to", "treatment", "with", "increasing", "concentrations", "of", "cisplatin", ".", "The", "IC50", "were", "calculated", "following", "5", "(", "MB002", "and", "MIC", ")", "or", "3", "days", "(", "Daoy", ")", "of", "treatment", ".", "Data", "are", "mean", "+", "standard", "deviation", "from", "3", "independent", "repeats", ",", "each", "containing", "5", "technical", "replicates", ".", "(", "B", ")", "Cisplatin", "dose", "response", "curves", "of", "SOX9", "-", "expressing", "(", "i", ")", "Daoy", "and", "(", "ii", ")", "MIC", "in", "the", "absence", "or", "presence", "of", "FBW7\u03b1", ".", "Experiments", "and", "data", "analysis", "were", "performed", "as", "described", "in", "(", "A", ")", "(", "C", ")", "Overall", "survival", "analysis", "of", "mice", "bearing", "Daoy", "or", "Daoy", "-", "expressing", "dox", "-", "inducible", "SOX9", "treated", "with", "cisplatin", ".", "The", "dox", "-", "preconditioned", "cells", "(", "105", "cells", ")", "were", "orthotopically", "xenografted", "to", "Nude", "-", "Foxn1nu", "mice", "and", "left", "for", "1", "week", "to", "prior", "to", "being", "treated", "with", "vehicle", "control", "or", "cisplatin", "(", "2mg", "/", "kg", ")", "intraperitoneally", "for", "every", "other", "day", "for", "a", "total", "of", "6", "doses", ".", "(", "D", ")", "Heat", "map", "of", "the", "row", "-", "wise", "z", "-", "scores", "of", "11", "genes", "associated", "with", "cisplatin", "resistance", "in", "MB002", "expressing", "Sox9", "-", "WT", "or", "Sox9", "-", "T236", "/", "T240A", ".", "Heat", "map", "was", "generated", "using", "the", "GenePattern", "software", ".", "(", "E", ")", "Quantitative", "analysis", "of", "ATP7A", ",", "DUSP2", ",", "and", "TTK", "mRNAs", "in", "MB002", "following", "expression", "of", "SOX9", "-", "WT", "or", "SOX9", "-", "T236", "/", "240A", ".", "Total", "RNA", "were", "collected", "24", "hours", "following", "doxycycline", "treatment", ",", "from", "which", "cDNA", "were", "generated", "for", "qPCR", ".", "Data", "are", "mean", "mRNA", "level", "(", "normalized", "to", "B2M", "transcript", ")", "+", "standard", "deviation", "from", "3", "independent", "experiments", "with", "statistical", "significance", "were", "determined", "by", "Multiple", "comparisons", "2", "-", "way", "ANOVA", "with", "Bonferroni", "'", "s", "post", "-", "test", ".", "(", "F", ")", "Time", "course", "western", "blotting", "of", "HA", "-", "SOX9", ",", "ATP7A", ",", "DUSP2", ",", "ERK1", "/", "2", "pThr202", "/", "Tyr204", "and", "total", "ERK1", "/", "2", "in", "MB002", "cells", "following", "doxycycline", "induction", "of", "either", "EV", ",", "SOX9", "-", "WT", "or", "SOX9", "-", "T236", "/", "240A", ".", "GAPDH", "was", "used", "as", "a", "loading", "control", "."
    ],
    "panel_id": "12345",
    "label_ids": {
        "entity_types": [
            "O", "O", "O", "O", "O", "O", "B-SMALL_MOLECULE", "O", "O", "O", "O", "O", "O", "O", "B-CELL", "O", "O", "O", "O", "B-CELL", "O", "O", "O", "O", "O", "B-CELL", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-GENEPROD", "O", "B-EXP_ASSAY", "I-EXP_ASSAY", "O", "O", "O", "O", "O", "O", "O", "B-SMALL_MOLECULE", "O", "O", "O", "O", "B-GENEPROD", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-SMALL_MOLECULE", "O", "O", "O", "O", "O", "O", "O", "O", "B-CELL", "O", "B-CELL", "O", "O", "O", "O", "O", "B-CELL", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-SMALL_MOLECULE", "O", "O", "O", "O", "B-GENEPROD", "O", "O", "O", "O", "O", "B-CELL", "O", "O", "O", "O", "B-CELL", "O", "O", "O", "O", "O", "O", "B-GENEPROD", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-EXP_ASSAY", "O", "O", "B-ORGANISM", "O", "B-CELL", "O", "B-CELL", "O", "O", "B-SMALL_MOLECULE", "O", "O", "B-GENEPROD", "O", "O", "B-SMALL_MOLECULE", "O", "O", "B-SMALL_MOLECULE", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-ORGANISM", "O", "O", "O", "B-GENEPROD", "B-ORGANISM", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-SMALL_MOLECULE", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-SMALL_MOLECULE", "O", "O", "B-CELL", "O", "B-GENEPROD", "O", "O", "O", "B-GENEPROD", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-GENEPROD", "O", "B-GENEPROD", "O", "O", "B-GENEPROD", "O", "O", "B-CELL", "O", "O", "O", "B-GENEPROD", "O", "O", "O", "B-GENEPROD", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-SMALL_MOLECULE", "O", "O", "O", "O", "O", "O", "O", "O", "B-EXP_ASSAY", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-GENEPROD", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-EXP_ASSAY", "I-EXP_ASSAY", "O", "B-GENEPROD", "O", "B-GENEPROD", "O", "B-GENEPROD", "O", "B-GENEPROD", "O", "B-GENEPROD", "I-GENEPROD", "I-GENEPROD", "O", "O", "O", "O", "O", "B-GENEPROD", "I-GENEPROD", "I-GENEPROD", "O", "B-CELL", "O", "O", "B-SMALL_MOLECULE", "O", "O", "O", "O", "O", "B-GENEPROD", "O", "O", "O", "B-GENEPROD", "O", "O", "O", "O", "O", "B-GENEPROD", "O", "O", "O", "O", "O", "O", "O"
        ],
        "geneprod_roles": [
            "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-CONTROLLED_VAR", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-CONTROLLED_VAR", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-CONTROLLED_VAR", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-CONTROLLED_VAR", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-CONTROLLED_VAR", "O", "O", "O", "B-CONTROLLED_VAR", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-MEASURED_VAR", "O", "B-MEASURED_VAR", "O", "O", "B-MEASURED_VAR", "O", "O", "O", "O", "O", "O", "B-CONTROLLED_VAR", "O", "O", "O", "B-CONTROLLED_VAR", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-MEASURED_VAR", "O", "B-MEASURED_VAR", "O", "B-MEASURED_VAR", "O", "B-MEASURED_VAR", "I-MEASURED_VAR", "I-MEASURED_VAR", "O", "O", "O", "O", "O", "B-MEASURED_VAR", "I-MEASURED_VAR", "I-MEASURED_VAR", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-CONTROLLED_VAR", "O", "O", "O", "B-CONTROLLED_VAR", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"
        ], 
        "boring": [
            "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-BORING", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-BORING", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-BORING", "O", "B-BORING", "O", "O", "B-BORING", "O", "O", "O", "O", "O", "O", "O", "O", "B-BORING", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-BORING", "O", "O", "O", "B-BORING", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-BORING", "O", "O", "B-BORING", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-BORING", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-BORING", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-BORING", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-BORING", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-BORING", "O", "O", "B-BORING", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-BORING", "O", "O", "O", "O", "O", "O", "O"
        ], 
        "panel_start": [
            "O", "O", "O", "B-PANEL_START", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-PANEL_START", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-PANEL_START", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-PANEL_START", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-PANEL_START", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-PANEL_START", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"
        ], 
        "small_mol_roles": ["O", "O", "O", "O", "O", "O", "B-CONTROLLED_VAR", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-CONTROLLED_VAR", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-CONTROLLED_VAR", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-CONTROLLED_VAR", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-CONTROLLED_VAR", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"]
    }
}
```
### Data Fields

- `words`: `list` of `strings` text tokenized into words.
- `panel_id`: ID of the panel to which the example belongs to in the SourceData database.
- `label_ids`:
  - `entity_types`: `list` of `strings` for the IOB2 tags for entity type; possible value in `["O", "I-SMALL_MOLECULE",  "B-SMALL_MOLECULE",  "I-GENEPROD", "B-GENEPROD", "I-SUBCELLULAR", "B-SUBCELLULAR", "I-CELL", "B-CELL", "I-TISSUE", "B-TISSUE", "I-ORGANISM", "B-ORGANISM", "I-EXP_ASSAY", "B-EXP_ASSAY"]`
  - `geneprod_roles`: `list` of `strings` for the IOB2 tags for experimental roles; values in `["O", "I-CONTROLLED_VAR", "B-CONTROLLED_VAR", "I-MEASURED_VAR", "B-MEASURED_VAR"]`
  - `boring`: `list` of `strings` for IOB2 tags for entities unrelated to causal design; values in `["O", "I-BORING", "B-BORING"]`
  - `panel_start`: `list` of `strings` for IOB2 tags `["O", "B-PANEL_START"]`  
  - `small_mol_roles`: `list` of `strings` for IOB2 tags showing whether the entity is the variable being measured or the control variable `["O", "B-CONTROLLED_VAR", "I-CONTROLLED_VAR", "B-MEASURED_VAR", "I-MEASURED_VAR",]`

### Data Splits

- train:
  - features: ['words', 'labels', 'tag_mask', 'panel_id'],
  - num_rows: 50_198
- validation:
  - features: ['words', 'labels', 'tag_mask', 'panel_id'],
  - num_rows: 5_946
- test:
  - features: ['words', 'labels', 'tag_mask', 'panel_id'],
  - num_rows: 6_222

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

The annotation of diseases has been added recently to the dataset. Although they appear, the number is very low and they are not consistently tagged through the entire dataset. 
We recommend to use the diseases by filtering the examples that contain them.

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

Thomas Lemberger, EMBO.
Jorge Abreu Vicente, EMBO

### Licensing Information

CC BY 4.0

### Citation Information

We are currently working on a paper to present the dataset. It is expected to be ready by 2023 spring. In the meantime, the following paper should be cited.

```latex
  @article {Liechti2017,
  	author = {Liechti, Robin and George, Nancy and Götz, Lou and El-Gebali, Sara and Chasapi, Anastasia and Crespo, Isaac and Xenarios, Ioannis and Lemberger, Thomas},
  	title = {SourceData - a semantic platform for curating and searching figures},
  	year = {2017},
    volume = {14},
    number = {11},
  	doi = {10.1038/nmeth.4471},
  	URL = {https://doi.org/10.1038/nmeth.4471},
  	eprint = {https://www.biorxiv.org/content/early/2016/06/20/058529.full.pdf},
  	journal = {Nature Methods}
  }
```


### Contributions

Thanks to [@tlemberger](https://github.com/tlemberger>) and [@drAbreu](https://github.com/drAbreu>) for adding this dataset.
