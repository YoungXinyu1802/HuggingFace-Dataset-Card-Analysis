---
language: 
  - protein sequences
datasets:
- Swissprot
tags: 
- Protein
- Enzyme Commission 
---

# Dataset

Swissprot is a high quality manually annotated protein database. The dataset contains annotations with the functional properties of the proteins. Here we extract proteins with Enzyme Commission labels.

The dataset is ported from Protinfer: https://github.com/google-research/proteinfer.

The leaf level EC-labels are extracted and indexed, the mapping is provided in `idx_mapping.json`. Proteins without leaf-level-EC tags are removed.


## Example
The protein Q87BZ2 have the following EC tags.

    EC:2.-.-.-    (Transferases)
    EC:2.7.-.-    (Transferring phosphorus-containing groups)
    EC:2.7.1.-    (Phosphotransferases with an alcohol group as acceptor)
    EC:2.7.1.30   (Glycerol kinase)

We only extract the leaf level labels, here EC:2.7.1.30, corresponding to glycerol kinase.


