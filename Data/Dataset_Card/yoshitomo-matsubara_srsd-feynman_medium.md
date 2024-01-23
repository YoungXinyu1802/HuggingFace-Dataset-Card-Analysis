---
pretty_name: SRSD-Feynman (Medium)
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

# Dataset Card for SRSD-Feynman (Medium set)

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

This is the ***Medium set*** of our SRSD-Feynman datasets, which consists of the following 40 different physics formulas:

| ID        | Formula                                                                                     |
|-----------|---------------------------------------------------------------------------------------------|
| I.8.14    | \\(d = \sqrt{(x_2-x_1)^2+(y_2-y_1)^2}\\) |
| I.10.7    | \\(m = \frac{m_0}{\sqrt{1-\frac{v^2}{c^2}}}\\) |
| I.11.19   | \\(A = x_1 y_1+x_2 y_2+x_3 y_3\\) |
| I.12.2    | \\(F = \frac{q_1 q_2}{4 \pi \epsilon r^2}\\) |
| I.12.11   | \\(F = q \left(E + B v \sin\left(\theta\right)\right)\\) |
| I.13.4    | \\(K = \frac{1}{2} m (v^2 + u^2 + w^2)\\) |
| I.13.12   | \\(U = G m_1 m_2 \left(\frac{1}{r_2}-\frac{1}{r_1}\right)\\) |
| I.15.10   | \\(p = \frac{m_0 v}{\sqrt{1-v^2/c^2}}\\) |
| I.16.6    | \\(v_1 = \frac{u+v}{1+u v/c^2}\\) |
| I.18.4    | \\(r = \frac{m_1 r_1+m_2 r_2}{m_1+m_2}\\) |
| I.24.6    | \\(E = \frac{1}{4} m (\omega^2+\omega_0^2) x^2\\) |
| I.29.4    | \\(k = \frac{\omega}{c}\\) |
| I.32.5    | \\(P = \frac{q^2 a^2}{6 \pi \epsilon c^3}\\) |
| I.34.8    | \\(\omega = \frac{q v B}{p}\\) |
| I.34.10   | \\(\omega = \frac{\omega_0}{1-v/c}\\) |
| I.34.27   | \\(W = \frac{h}{2 \pi} \omega\\) |
| I.38.12   | \\(r = 4 \pi \epsilon \frac{\left(h/\left(2 \pi\right)\right)^2}{m q^2}\\) |
| I.39.10   | \\(U = \frac{3}{2} P V\\) |
| I.39.11   | \\(U = \frac{P V}{\gamma-1}\\) |
| I.43.31   | \\(D = \mu k T\\) |
| I.43.43   | \\(\kappa = \frac{1}{\gamma - 1} \frac{k v}{\sigma_c}\\) |
| I.48.2    | \\(E = \frac{m c^2}{\sqrt{1-v^2/c^2}}\\) |
| II.6.11   | \\(\phi = \frac{1}{4 \pi \epsilon} \frac{p \cos\theta}{r^2}\\) |
| II.8.7    | \\(U = \frac{3}{5}  \frac{Q^2}{4 \pi \epsilon a}\\) |
| II.11.3   | \\(x = \frac{q E}{m (\omega_0^2-\omega^2)}\\) |
| II.21.32  | \\(\phi = \frac{q}{4 \pi \epsilon r (1-v/c)}\\) |
| II.34.2   | \\(\mu = \frac{q v r}{2}\\) |
| II.34.2a  | \\(I = \frac{q v}{2 \pi r}\\) |
| II.34.29a | \\(\mu = \frac{q h}{4 \pi m}\\) |
| II.37.1   | \\(E = \mu (1+\chi) B\\) |
| III.4.32  | \\(n = \frac{1}{\exp(h \omega/2 \pi k T) - 1}\\) |
| III.8.54  | \\(|C|^2 = \sin^2 \frac{2 \pi A t}{h}\\) |
| III.13.18 | \\(v = \frac{4 \pi A b^2}{h} k\\) |
| III.14.14 | \\(I = I_0 \left(\exp\left(q \Delta V/\kappa T\right)-1\right)\\) |
| III.15.12 | \\(E = 2 A (1-\cos k d)\\) |
| III.15.14 | \\(m = \frac{h^2}{8 \pi^2 A b^2}\\) |
| III.17.37 | \\(f = \beta (1+\alpha \cos\theta)\\) |
| III.19.51 | \\(E = -\frac{m q^4}{2 (4 \pi \epsilon)^2 (h/(2 \pi))^2 n^2}\\) |
| B8        | \\(U = \frac{E}{1+\frac{E}{m c^2} (1-\cos\theta)}\\) |
| B18       | \\(\rho = \frac{3}{8 \pi G} \left(\frac{c^2 k_\text{f}}{a_\text{f}^2}+H^2\right)\\) |


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


