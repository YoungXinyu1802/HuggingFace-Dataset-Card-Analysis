---
license: mit
---
# Reference genome of *Arabidopsis thaliana*

Intended use cases:
- Pre-training of DNA language models.
- Evaluation of DNA language models. Caveat about same chromosome, needed because of small size: TODO

Details:
- Split into 512 base-pair windows.
- Added windows overlapping every 64 base pairs.
- Added reverse complement.

Code to build this dataset: TODO