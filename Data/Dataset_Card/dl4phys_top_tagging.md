---
license: cc-by-4.0
---
# Dataset Card for Top Quark Tagging

## Table of Contents
- [Dataset Card for Top Quark Tagging](#dataset-card-for-top-quark-tagging)
  - [Table of Contents](#table-of-contents)
  - [Dataset Description](#dataset-description)
    - [Dataset Summary](#dataset-summary)
    - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Dataset Structure](#dataset-structure)
    - [Data Instances](#data-instances)
    - [Data Fields](#data-fields)
    - [Data Splits](#data-splits)
    - [Licensing Information](#licensing-information)
    - [Citation Information](#citation-information)
    - [Contributions](#contributions)

## Dataset Description

- **Homepage:** https://zenodo.org/record/2603256
- **Paper:** https://arxiv.org/abs/1902.09914
- **Point of Contact:** [Gregor Kasieczka](gregor.kasieczka@uni-hamburg.de)

### Dataset Summary

Top Quark Tagging is a dataset of Monte Carlo simulated events produced by proton-proton collisions at the Large Hadron Collider. The top-quark signal and mixed quark-gluon background jets are produced with Pythia8 with its default tune for a center-of-mass energy of 14 TeV. Multiple interactions and pile-up are ignored. The leading 200 jet constituent four-momenta \\( (E, p_x, p_y, p_z) \\) are stored, with zero-padding applied to jets with fewer than 200 constituents.

### Supported Tasks and Leaderboards

- `tabular-classification`: The dataset can be used to train a model for tabular binary classification, which consists in predicting whether an event is produced from a top signal or quark-gluon background. Success on this task is typically measured by achieving a *high* [accuracy](https://huggingface.co/metrics/accuracy) and AUC score.

## Dataset Structure

### Data Instances

Each instance in the dataset consists of the four-momenta of the leading 200 jet constituents, sorted by \\(p_T\\). For jets with fewer than 200 constituents, zero-padding is applied. The four-momenta of the top-quark are also provided, along with a label in the `is_signal_new` column to indicate whether the event stems from a top-quark (1) or QCD background (0). An example instance looks as follows:

```
{'E_0': 474.0711364746094,
 'PX_0': -250.34703063964844,
 'PY_0': -223.65196228027344,
 'PZ_0': -334.73809814453125,
  ...
 'E_199': 0.0,
 'PX_199': 0.0,
 'PY_199': 0.0,
 'PZ_199': 0.0,
 'truthE': 0.0,
 'truthPX': 0.0,
 'truthPY': 0.0,
 'truthPZ': 0.0,
 'ttv': 0,
 'is_signal_new': 0}
```

### Data Fields

The fields in the dataset have the following meaning:

- `E_i`: the energy of jet constituent \\(i\\).
- `PX_i`: the \\(x\\) component of the jet constituent's momentum
- `PY_i`: the \\(y\\) component of the jet constituent's momentum
- `PZ_i`: the \\(z\\) component of the jet constituent's momentum
- `truthE`: the energy of the top-quark
- `truthPX`: the \\(x\\) component of the top quark's momentum
- `truthPY`: the \\(y\\) component of the top quark's momentum
- `truthPZ`: the \\(z\\) component of the top quark's momentum
- `ttv`: a flag that indicates which split (train, validation, or test) that a jet belongs to. Redundant since each split is provided as a separate dataset
- `is_signal_new`: the label for each jet. A 1 indicates a top-quark, while a 0 indicates QCD background.

### Data Splits

|                  |   train | validation |   test |
|------------------|--------:|-----------:|-------:|
| Number of events | 1211000 |     403000 | 404000 |

### Licensing Information

This dataset is released under the [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/legalcode) license.
### Citation Information

```
@dataset{kasieczka_gregor_2019_2603256,
  author       = {Kasieczka, Gregor and
                  Plehn, Tilman and
                  Thompson, Jennifer and
                  Russel, Michael},
  title        = {Top Quark Tagging Reference Dataset},
  month        = mar,
  year         = 2019,
  publisher    = {Zenodo},
  version      = {v0 (2018\_03\_27)},
  doi          = {10.5281/zenodo.2603256},
  url          = {https://doi.org/10.5281/zenodo.2603256}
}
```

### Contributions

Thanks to [@lewtun](https://github.com/lewtun) for adding this dataset.
