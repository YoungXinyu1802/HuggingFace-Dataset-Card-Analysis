## ProteinGym benchmarks overview
ProteinGym is an extensive set of Deep Mutational Scanning (DMS) assays curated to enable thorough comparisons of various mutation effect predictors indifferent regimes. It is comprised of two benchmarks: 1) a substitution benchmark which consists of the experimental characterisation of ∼1.5M missense variants across 87 DMS assays 2) an indel benchmark that includes ∼300k mutants across 7 DMS assays.

Each processed file in each benchmark corresponds to a single DMS assay, and contains the following three variables:

1) mutant (str):
- for the substitution benchmark, it describes the set of substitutions to apply on the reference sequence to obtain the mutated sequence (eg., A1P:D2N implies the amino acid 'A' at position 1 should be replaced by 'P', and 'D' at position 2 should be replaced by 'N')
- for the indel benchmark, it corresponds to the full mutated sequence
2) DMS_score (float): corresponds to the experimental measurement in the DMS assay. Across all assays, the higher the DMS_score value, the higher the fitness of the mutated protein
3) DMS_score_bin (int): indicates whether the DMS_score is above the fitness cutoff (1 is fit, 0 is not fit)

Additionally, we provide two reference files (ProteinGym_reference_file_substitutions.csv and ProteinGym_reference_file_indels.csv) that give further details on each assay and contain in particular:
- The UniProt_ID of the corresponding protein, along with taxon and MSA depth category
- The target sequence (target_seq) used in the assay
- Details on how the DMS_score was created from the raw files and how it was binarized


## Reference
If you use ProteinGym in your work, please cite the following paper:
```
Notin, P., Dias, M., Frazer, J., Marchena-Hurtado, J., Gomez, A., Marks, D.S., Gal, Y. (2022). Tranception: Protein Fitness Prediction with Autoregressive Transformers and Inference-time Retrieval. ICML.
```

## Links
- Pre-print: https://arxiv.org/abs/2205.13760
- Code: https://github.com/OATML-Markslab/Tranception