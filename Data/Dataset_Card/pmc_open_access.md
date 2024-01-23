---
annotations_creators:
- no-annotation
language_creators:
- expert-generated
language:
- en
license:
- cc0-1.0
- cc-by-4.0
- cc-by-sa-4.0
- cc-by-nd-4.0
- cc-by-nc-4.0
- cc-by-nc-sa-4.0
- cc-by-nc-nd-4.0
- other
- unknown
multilinguality:
- monolingual
size_categories:
- 1M<n<10M
source_datasets:
- original
task_categories:
- text-generation
task_ids:
- language-modeling
pretty_name: PMC Open Access
---

# Dataset Card for PMC Open Access Subset

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

- **Homepage:** https://www.ncbi.nlm.nih.gov/pmc/tools/openftlist/
- **Repository:**
- **Paper:**
- **Leaderboard:**
- **Point of Contact:** [PubMed Central](mailto:pubmedcentral@ncbi.nlm.nih.gov)

### Dataset Summary

The PMC Open Access Subset includes more than 3.4 million journal articles and preprints that are made available under
license terms that allow reuse. Not all articles in PMC are available for text mining and other reuse, many have
copyright protection, however articles in the PMC Open Access Subset are made available under Creative Commons or
similar licenses that generally allow more liberal redistribution and reuse than a traditional copyrighted work. The
PMC Open Access Subset is one part of the PMC Article Datasets.

Within the PMC Open Access Subset, there are three groupings:
- Commercial Use Allowed - CC0, CC BY, CC BY-SA, CC BY-ND licenses
- Non-Commercial Use Only - CC BY-NC, CC BY-NC-SA, CC BY-NC-ND licenses; and
- Other - no machine-readable Creative Commons license, no license, or a custom license.


### Supported Tasks and Leaderboards

- Language modeling

### Languages

English (`en`).

## Dataset Structure

### Data Instances

```
{
  'text': "==== Front\nPLoS BiolPLoS BiolpbioplosbiolPLoS Biology1544-91731545-7885Public Library of Science San Francisco, USA 10.1371/journal.pbio.0000005Research ArticleGenetics/Genomics/Gene TherapyInfectious DiseasesMicrobiologyPlasmodiumThe Transcriptome of the Intraerythrocytic Developmental Cycle of Plasmodium falciparum\n P. falciparum IDC TranscriptomeBozdech Zbynek \n1\nLlinás Manuel \n1\nPulliam Brian Lee \n1\nWong Edith D \n1\nZhu Jingchun \n2\nDeRisi Joseph L joe@derisilab.ucsf.edu\n1\n1Department of Biochemistry and Biophysics, University of California, San FranciscoSan Francisco, CaliforniaUnited States of America2Department of Biological and Medical Informatics, University of California, San FranciscoSan Francisco, CaliforniaUnited States of America10 2003 18 8 2003 18 8 2003 1 1 e512 6 2003 25 7 2003 Copyright: ©2003 Bozdech et al.2003This is an open-access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are properly credited.\nMicroarray Analysis: Genome-Scale Hypothesis Scanning \n\nMonitoring Malaria: Genomic Activity of the Parasite in Human Blood Cells \n\nPlasmodium falciparum is the causative agent of the most burdensome form of human malaria, affecting 200–300 million individuals per year worldwide. The recently sequenced genome of P. falciparum revealed over 5,400 genes, of which 60% encode proteins of unknown function. Insights into the biochemical function and regulation of these genes will provide the foundation for future drug and vaccine development efforts toward eradication of this disease. By analyzing the complete asexual intraerythrocytic developmental cycle (IDC) transcriptome of the HB3 strain of P. falciparum, we demonstrate that at least 60% of the genome is transcriptionally active during this stage. Our data demonstrate that this parasite has evolved an extremely specialized mode of transcriptional regulation that produces a continuous cascade of gene expression, beginning with genes corresponding to general cellular processes, such as protein synthesis, and ending with Plasmodium-specific functionalities, such as genes involved in erythrocyte invasion. The data reveal that genes contiguous along the chromosomes are rarely coregulated, while transcription from the plastid genome is highly coregulated and likely polycistronic. Comparative genomic hybridization between HB3 and the reference genome strain (3D7) was used to distinguish between genes not expressed during the IDC and genes not detected because of possible sequence variations...
  'pmid': '12929205',
  'accession_id': 'PMC176545',
  'license': 'CC BY',
  'last_updated': '2021-01-05 08:21:03',
  'retracted': 'no',
  'citation': 'PLoS Biol. 2003 Oct 18; 1(1):e5'
}
```

### Data Fields

- `text`: Text content.
- `pmid`: PubMed ID.
- `accession_id`: Unique identifier for a sequence record. 
- `license`: License type.
- `last_updated`: Date of last update.
- `retracted`: Whether retracted or not.
- `citation`: Citation reference.

### Data Splits

The dataset is not split.

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

License terms vary. Please refer to the license statement in each article for specific terms of use.

Within the PMC Open Access Subset, there are three groupings based on available license terms:
- Commercial Use Allowed - CC0, CC BY, CC BY-SA, CC BY-ND licenses;
- Non-Commercial Use Only - CC BY-NC, CC BY-NC-SA, CC BY-NC-ND licenses; and
- Other - no machine-readable Creative Commons license, no license, or a custom license.

### Citation Information

[More Information Needed]

### Contributions

Thanks to [@albertvillanova](https://github.com/albertvillanova) for adding this dataset.
