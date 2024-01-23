---
pretty_name: SRSD-Feynman (Easy)
annotations_creators:
- expert
language_creators:
- expert-generated
language:
- en
license:
- mit
multilinguality:
- monolingual
size_categories:
- 100K<n<1M
source_datasets:
- extended
task_categories:
- symbolic-regression
task_ids: []
---

# Dataset Card for SRSD-Feynman (Easy set)

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

- **Homepage:**
- **Repository:** https://github.com/omron-sinicx/srsd-benchmark
- **Paper:** [Rethinking Symbolic Regression Datasets and Benchmarks for Scientific Discovery](https://arxiv.org/abs/2206.10540)
- **Point of Contact:** [Yoshitaka Ushiku](mailto:yoshitaka.ushiku@sinicx.com)

### Dataset Summary

Our SRSD (Feynman) datasets are designed to discuss the performance of Symbolic Regression for Scientific Discovery.
We carefully reviewed the properties of each formula and its variables in [the Feynman Symbolic Regression Database](https://space.mit.edu/home/tegmark/aifeynman.html) to design reasonably realistic sampling range of values so that our SRSD datasets can be used for evaluating the potential of SRSD such as whether or not an SR method con (re)discover physical laws from such datasets.

This is the ***Easy set*** of our SRSD-Feynman datasets, which consists of the following 30 different physics formulas:

| ID        | Formula                                                                                     |
|-----------|---------------------------------------------------------------------------------------------|
| I.12.1    | \\(F = \mu N_\text{n}\\) |
| I.12.4    | \\(E = \frac{q_1}{4 \pi \epsilon r^2}\\) |
| I.12.5    | \\(F = q_2 E\\) |
| I.14.3    | \\(U = m g z\\) |
| I.14.4    | \\(U = \frac{k_\text{spring} x^2}{2}\\) |
| I.18.12   | \\(\tau = r F \sin\theta\\) |
| I.18.16   | \\(L = m r v \sin\theta\\) |
| I.25.13   | \\(V = \frac{q}{C}\\) |
| I.26.2    | \\(n = \frac{\sin\theta_1}{\sin\theta_2}\\) |
| I.27.6    | \\(f = \frac{1}{\frac{1}{d_1}+\frac{n}{d_2}}\\) |
| I.30.5    | \\(d = \frac{\lambda}{n \sin\theta}\\) |
| I.43.16   | \\(v = \mu q \frac{V}{d}\\) |
| I.47.23   | \\(c = \sqrt{\frac{\gamma P}{\rho}}\\) |
| II.2.42   | \\(J = \kappa (T_2-T_1) \frac{A}{d}\\) |
| II.3.24   | \\(h = \frac{W}{4 \pi r^2}\\) |
| II.4.23   | \\(\phi = \frac{q}{4 \pi \epsilon r}\\) |
| II.8.31   | \\(u = \frac{\epsilon E^2}{2}\\) |
| II.10.9   | \\(E = \frac{\sigma_\text{free}}{\epsilon} \frac{1}{1+\chi}\\) |
| II.13.17  | \\(B = \frac{1}{4 \pi \epsilon c^2} \frac{2 I}{r}\\) |
| II.15.4   | \\(U = -\mu B \cos\theta\\) |
| II.15.5   | \\(U = -p E \cos\theta\\) |
| II.27.16  | \\(S = \epsilon c E^2\\) |
| II.27.18  | \\(u = \epsilon E^2\\) |
| II.34.11  | \\(\omega = g \frac{q B}{2 m}\\) |
| II.34.29b | \\(U = 2 \pi g \mu B \frac{J_z}{h}\\) |
| II.38.3   | \\(F = Y A \frac{\Delta l}{l}\\) |
| II.38.14  | \\(\mu = \frac{Y}{2 (1+\sigma)}\\) |
| III.7.38  | \\(\omega = \frac{4 \pi \mu B}{h}\\) |
| III.12.43 | \\(J = \frac{m h}{2 \pi}\\) |
| III.15.27 | \\(k = \frac{2 \pi}{N b} s\\) |


More details of these datasets such as variables and sampling ranges are provided in [the paper and its supplementary material](https://arxiv.org/abs/2206.10540).  

### Supported Tasks and Leaderboards

Symbolic Regression

## Dataset Structure

### Data Instances

Tabular data + Ground-truth equation per equation

Tabular data: (num_samples, num_variables+1), where the last (rightmost) column indicate output of the target function for given variables.
Note that the number of variables (`num_variables`) varies from equation to equation.
  
Ground-truth equation: *pickled* symbolic representation (equation with symbols in sympy) of the target function.


### Data Fields

For each dataset, we have 
1. train split (txt file, whitespace as a delimiter)
2. val split (txt file, whitespace as a delimiter)
3. test split (txt file, whitespace as a delimiter)
4. true equation (pickle file for sympy object)

### Data Splits

- train: 8,000 samples per equation
- val: 1,000 samples per equation
- test: 1,000 samples per equation

## Dataset Creation

### Curation Rationale

We chose target equations based on [the Feynman Symbolic Regression Database](https://space.mit.edu/home/tegmark/aifeynman.html).

### Annotations

#### Annotation process

We significantly revised the sampling range for each variable from the annotations in the Feynman Symbolic Regression Database.
First, we checked the properties of each variable and treat physical constants (e.g., light speed, gravitational constant) as constants.
Next, variable ranges were defined to correspond to each typical physics experiment to confirm the physical phenomenon for each equation.
In cases where a specific experiment is difficult to be assumed, ranges were set within which the corresponding physical phenomenon can be seen.
Generally, the ranges are set to be sampled on log scales within their orders as 10^2 in order to take both large and small changes in value as the order changes.
Variables such as angles, for which a linear distribution is expected are set to be sampled uniformly.
In addition, variables that take a specific sign were set to be sampled within that range.

#### Who are the annotators?

The main annotators are
- Naoya Chiba (@nchiba)
- Ryo Igarashi (@rigarash)



### Personal and Sensitive Information

N/A

## Considerations for Using the Data

### Social Impact of Dataset

We annotated this dataset, assuming typical physical experiments. The dataset will engage research on symbolic regression for scientific discovery (SRSD) and help researchers discuss the potential of symbolic regression methods towards data-driven scientific discovery.

### Discussion of Biases

Our choices of target equations are based on [the Feynman Symbolic Regression Database](https://space.mit.edu/home/tegmark/aifeynman.html), which are focused on a field of Physics.

### Other Known Limitations

Some variables used in our datasets indicate some numbers (counts), which should be treated as integer.
Due to the capacity of 32-bit integer, however, we treated some of such variables as float e.g., number of molecules (10^{23} - 10^{25})

## Additional Information

### Dataset Curators

The main curators are
- Naoya Chiba (@nchiba)
- Ryo Igarashi (@rigarash)

### Licensing Information

MIT License

### Citation Information

[[Preprint](https://arxiv.org/abs/2206.10540)]  
```bibtex
@article{matsubara2022rethinking,
  title={Rethinking Symbolic Regression Datasets and Benchmarks for Scientific Discovery},
  author={Matsubara, Yoshitomo and Chiba, Naoya and Igarashi, Ryo and Tatsunori, Taniai and Ushiku, Yoshitaka},
  journal={arXiv preprint arXiv:2206.10540},
  year={2022}
}
```

### Contributions

Authors:
- Yoshitomo Matsubara (@yoshitomo-matsubara)
- Naoya Chiba (@nchiba)
- Ryo Igarashi (@rigarash)
- Tatsunori Taniai
- Yoshitaka Ushiku (@yushiku)


