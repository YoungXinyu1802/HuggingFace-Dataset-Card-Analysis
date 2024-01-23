---
language: 
  - protein sequences
datasets:
- Swissprot
tags: 
- Protein
- PFam
---

Swissprot is a high quality manually annotated protein database. The dataset contains annotations with the functional properties of the proteins. Here we extract proteins with PFam labels.

The dataset is ported from Protinfer: https://github.com/google-research/proteinfer.

The Pfam-labels are extracted and indexed, the mapping is provided in `idx_mapping.json`. Proteins without Pfam tags are removed.
