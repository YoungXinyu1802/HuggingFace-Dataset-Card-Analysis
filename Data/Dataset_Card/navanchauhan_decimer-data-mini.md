---
license: openrail
pretty_name: PubChem 68K
size_categories:
- 10K<n<100K
task_categories:
- image-to-text
dataset_info:
  features:
  - name: image
    dtype: image
  - name: smiles
    dtype: string
  - name: selfies
    dtype: string
  splits:
  - name: train
    num_bytes: 1185846198.576
    num_examples: 68996
  - name: test
    num_bytes: 267097779.576
    num_examples: 15499
  - name: validation
    num_bytes: 266912227.912
    num_examples: 15499
  download_size: 1692942822
  dataset_size: 1719856206.064
---

Molecules in this set

* have a molecular weight of fewer than 1500 Daltons,
* not possess counter ions,
* only contain the elements C, H, O, N, P, S, F, Cl, Br, I, Se and B,
* not contain isotopes of Hydrogens (D, T),
* have 3–40 bonds,
* not contain any charged groups including zwitterionic forms,
* only contain implicit hydrogens, except in functional groups,
* have less than 40 SMILES characters,
* no stereochemistry is allowed.

The original dataset from Decimer was imported and randomly sampled. 516x516 sized images were generated using RDKit.

## Reference

> Rajan, Kohulan; Zielesny, Achim; Steinbeck, Christoph (2021): DECIMER 1.0: Deep Learning for Chemical Image Recognition using Transformers. ChemRxiv. Preprint. https://doi.org/10.26434/chemrxiv.14479287.v1