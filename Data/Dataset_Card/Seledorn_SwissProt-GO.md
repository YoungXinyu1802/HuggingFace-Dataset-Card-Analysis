---
language: 
  - protein sequences
datasets:
- Swissprot
tags: 
- Protein
- Gene Ontology
- GO
---

Swissprot is a high quality manually annotated protein database. The dataset contains annotations with the functional properties of the proteins. Here we extract proteins with Gene Ontology labels.

The dataset is ported from Protinfer: https://github.com/google-research/proteinfer.

The GO-labels are extracted and indexed, the mapping is provided in `idx_mapping.json`. Proteins without GO tags are removed.
