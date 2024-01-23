---
pretty_name: SRSD-Feynman (Hard)
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

# Dataset Card for SRSD-Feynman (Hard set)

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

This is the ***Hard set*** of our SRSD-Feynman datasets, which consists of the following 50 different physics formulas:

| ID        | Formula                                                                                     |
|-----------|---------------------------------------------------------------------------------------------|
| I.6.20    | \\(f = \exp\left(-\frac{\theta^2}{2\sigma^2}\right)/\sqrt{2\pi\sigma^2}\\) |
| I.6.20a   | \\(f = \exp\left(-\frac{\theta^2}{2}\right)/\sqrt{2\pi}\\) |
| I.6.20b   | \\(f = \exp\left(-\frac{\left(\theta-\theta_1\right)^2}{2\sigma^2}\right)/\sqrt{2\pi\sigma}\\) |
| I.9.18    | \\(F = \frac{G m_1 m_2}{(x_2-x_1)^2+(y_2-y_1)^2+(z_2-z_1)^2}\\) |
| I.15.3t   | \\(t_1 = \frac{t-u x/c^2}{\sqrt{1-u^2/c^2}}\\) |
| I.15.3x   | \\(x_1 = \frac{x - u t}{\sqrt{1 - u^2/c^2}}\\) |
| I.29.16   | \\(x = \sqrt{x_1^2+x_2^2 + 2 x_1 x_2 \cos\left(\theta_1-\theta_2\right)}\\) |
| I.30.3    | \\(I = I_0 \frac{\sin^2\left(n \theta/2\right)}{\sin^2\left(\theta/2\right)}\\) |
| I.32.17   | \\(P = \left(\frac{1}{2} \epsilon c E^2\right) \left(\frac{8 \pi r^2}{3}\right) \left(\frac{\omega^4}{\left(\omega^2-\omega_0^2\right)^2}\right)\\) |
| I.34.14   | \\(\omega = \frac{1+v/c}{\sqrt{1-v^2/c^2}} \omega_0\\) |
| I.37.4    | \\(I_{12} = I_1+I_2+2 \sqrt{I_1 I_2} \cos\delta\\) |
| I.39.22   | \\(P = \frac{n k T}{V}\\) |
| I.40.1    | \\(n = n_0 \exp\left(-m g x/ k T\right)\\) |
| I.41.16   | \\(L_\text{rad} = \frac{h}{2 \pi} \frac{\omega^3}{\pi^2 c^2 (\exp(h \omega/2 \pi k T)-1)}\\) |
| I.44.4    | \\(Q = n k T \ln(\frac{V_2}{V_1})\\) |
| I.50.26   | \\(x = K \left(\cos\omega t + \epsilon \cos^2 \omega t\right)\\) |
| II.6.15a  | \\(E = \frac{p}{4 \pi \epsilon} \frac{3 z}{r^5} \sqrt{x^2+y^2}\\) |
| II.6.15b  | \\(E = \frac{p}{4 \pi \epsilon} \frac{3 \cos\theta \sin\theta}{r^3}\\) |
| II.11.17  | \\(n = n_0 \left(1 + \frac{p_0 E \cos\theta}{k T}\right)\\) |
| II.11.20  | \\(P = \frac{n_0 p_0^2 E}{3 k T}\\) |
| II.11.27  | \\(P = \frac{N \alpha}{1-(n \alpha/3)} \epsilon E\\) |
| II.11.28  | \\(\kappa = 1 + \frac{N \alpha}{1-(N \alpha/3)}\\) |
| II.13.23  | \\(\rho = \frac{\rho_0}{\sqrt{1-v^2/c^2}}\\) |
| II.13.34  | \\(j = \frac{\rho_0 v}{\sqrt{1-v^2/c^2}}\\) |
| II.24.17  | \\(k = \sqrt{\omega^2 / c^2 - \pi^2/a^2}\\) |
| II.35.18  | \\(a = \frac{N}{\exp(\mu B/k T)+\exp(-\mu B/k T)}\\) |
| II.35.21  | \\(M = N \mu \tanh\frac{\mu B}{k T}\\) |
| II.36.38  | \\(x = \frac{\mu H}{k T}+\frac{\mu \lambda}{\epsilon c^2 k T} M\\) |
| III.4.33  | \\(E = \frac{h \omega}{2 \pi \left(\exp\left(h \omega/2 \pi k T\right) - 1\right)}\\) |
| III.9.52  | \\(P_{\text{I} \rightarrow \text{II}} = \left(\frac{2 \pi \mu E t}{h}\right)^2 \frac{\sin^2\left(\left(\omega-\omega_0\right) t/2\right)}{\left(\omega-\omega_0\right) t / 2)^2}\\) |
| III.10.19 | \\(E = \mu \sqrt{B_x^2+B_y^2+B_z^2}\\) |
| III.21.20 | \\(J = -\rho \frac{q}{m} A\\) |
| B1        | \\(A = \left(\frac{Z_1 Z_2 \alpha h c}{4 E \sin^2\left(\theta/2\right)}\right)^2\\) |
| B2        | \\(k = \frac{m k_G}{L^2} \left(1+\sqrt{1+\frac{2 E L^2}{m k_G^2}} \cos\left(\theta_1-\theta_2\right)\right)\\) |
| B3        | \\(r = \frac{d (1-\alpha^2)}{1+\alpha \cos(\theta_1-\theta_2)}\\) |
| B4        | \\(v = \sqrt{\frac{2}{m}  \left(E-U-\frac{L^2}{2 m r^2}\right)}\\) |
| B5        | \\(t = \frac{2 \pi d^{3/2}}{\sqrt{G(m_1+m_2)}}\\) |
| B6        | \\(\alpha = \sqrt{1+\frac{2 \epsilon^2 E L^2}{m (Z_1 Z_2 q^2)^2}}\\) |
| B7        | \\(H = \sqrt{\frac{8 \pi G \rho}{3}-\frac{k_\text{f} c^2}{a_\text{f}^2}}\\) |
| B9        | \\(P = -\frac{32}{5} \frac{G^4}{c^5} \frac{(m_1 m_2)^2 (m_1+m_2)}{r^5}\\) |
| B10       | \\(\cos\theta_1 = \frac{\cos\theta_2-v/c}{(1-v/c) \cos\theta_2}\\) |
| B11       | \\(I = I_0 \left(\frac{\sin(\alpha/2)}{\alpha/2} \frac{\sin(N \delta/2)}{\sin(\delta/2)}\right)^2\\) |
| B12       | \\(F = \frac{q}{4 \pi \epsilon y^2} \left(4 \pi \epsilon V_\text{e} d - \frac{q d y^3}{(y^2-d^2)^2}\right)\\) |
| B13       | \\(V_\text{e} = \frac{q}{4 \pi \epsilon \sqrt{r^2+d^2-2 d r \cos\alpha}}\\) |
| B14       | \\(V_\text{e} = E_\text{f} \cos\theta \left(\frac{\alpha-1}{\alpha+2} \frac{d^3}{r^2}-r\right)\\) |
| B15       | \\(\omega_0 = \frac{\sqrt{1-\frac{v^2}{c^2}}}{1+\frac{v}{c} \cos\theta} \omega\\) |
| B16       | \\(E = q V_\text{e} + \sqrt{(p-q A)^2 c^2+m^2 c^4}\\) |
| B17       | \\(E = \frac{1}{2 m} \left(p^2+m^2 \omega^2 x^2 \left(1+\alpha \frac{x}{y}\right)\right)\\) |
| B19       | \\(p_\text{f} = -\frac{1}{8 \pi G} \left(\frac{c^4 k_\text{f}}{a_\text{f}^2}+c^2 H^2 \left(1-2 \alpha\right)\right)\\) |
| B20       | \\(A = \frac{\alpha^2 h^2}{4 \pi m^2 c^2} \left(\frac{\omega_0}{\omega}\right)^2 \left(\frac{\omega_0}{\omega}+\frac{\omega}{\omega_0}-\sin^2\theta\right)\\) |


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


