---
license: mit
---

# Dataset Card for JetClass

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

- **Homepage:**
- **Repository:** https://github.com/jet-universe/particle_transformer
- **Paper:** https://arxiv.org/abs/2202.03772
- **Leaderboard:**
- **Point of Contact:** [Huilin Qu](mailto:huilin.qu@cern.ch)

### Dataset Summary

JetClass is a large and comprehensive dataset to advance deep learning for jet tagging. The dataset consists of 100 million jets for training, with 10 different types of jets.  The jets in this dataset generally fall into two categories:

* The background jets are initiated by light quarks or gluons (q/g) and are ubiquitously produced at the
LHC.
* The signal jets are those arising either from the top quarks (t), or from the W, Z or Higgs (H) bosons. For top quarks and Higgs bosons, we further consider their different decay modes as separate types, because the resulting jets have rather distinct characteristics and are often tagged individually.

Jets in this dataset are simulated with standard Monte Carlo event generators used by LHC experiments. The production and decay of the top quarks and the W, Z and Higgs bosons are generated with MADGRAPH5_aMC@NLO. We use PYTHIA to evolve the produced particles, i.e., performing parton showering and hadronization, and produce the final outgoing particles. To be close to realistic jets  reconstructed at the ATLAS or CMS experiment, detector effects are simulated with DELPHES using the CMS detector configuration provided in DELPHES. In addition, the impact parameters of electrically charged particles are smeared to match the resolution of the CMS tracking detector . Jets are clustered from DELPHES E-Flow objects with the anti-kT algorithm using a distance
parameter R = 0.8. Only jets with transverse momentum in 500–1000 GeV and pseudorapidity |η| < 2 are considered. For signal jets, only the “high-quality” ones that fully contain the decay products of initial particles are included.

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

[More Information Needed]

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

[More Information Needed]

### Citation Information

If you use the JetClass dataset, please cite:

```
@article{Qu:2022mxj,
    author = "Qu, Huilin and Li, Congqiao and Qian, Sitian",
    title = "{Particle Transformer for Jet Tagging}",
    eprint = "2202.03772",
    archivePrefix = "arXiv",
    primaryClass = "hep-ph",
    month = "2",
    year = "2022"
}
```

### Contributions

Thanks to [@lewtun](https://github.com/lewtun) for adding this dataset.
