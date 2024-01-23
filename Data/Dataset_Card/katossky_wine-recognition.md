---
annotations_creators:
- no-annotation
language: []
language_creators:
- expert-generated
license:
- unknown
pretty_name: Wine Recognition Dataset
size_categories:
- n<1K
source_datasets:
- original
task_categories:
- tabular-classification
task_ids:
- tabular-multi-class-classification
---

# Dataset Card for Wine Recognition dataset

## Dataset Description

- **Homepage:** https://archive.ics.uci.edu/ml/datasets/wine
- **Papers:**
    1. S. Aeberhard, D. Coomans and O. de Vel,
        Comparison of Classifiers in High Dimensional Settings,
        Tech. Rep. no. 92-02, (1992), Dept. of Computer Science and Dept. of
        Mathematics and Statistics, James Cook University of North Queensland.
    2. S. Aeberhard, D. Coomans and O. de Vel,
        "THE CLASSIFICATION PERFORMANCE OF RDA"
        Tech. Rep. no. 92-01, (1992), Dept. of Computer Science and Dept. of
        Mathematics and Statistics, James Cook University of North Queensland.
- **Point of Contact:** stefan'@'coral.cs.jcu.edu.au

### Dataset Summary

These data are the results of a chemical analysis of wines grown in the same region in Italy but derived from three different cultivars. The analysis determined the quantities of 13 constituents found in each of the three types of wines. In a classification context, this is a well posed problem with "well behaved" class structures. A good data set for first testing of a new classifier, but not very challenging.

### Supported Tasks and Leaderboards

Classification (cultivar) from continuous variables (all other variables)

## Dataset Structure

### Data Instances

178 wines

### Data Fields

1. Wine category (cultivar)
2. Alcohol
3. Malic acid
4. Ash
5. Alcalinity of ash
6. Magnesium
7. Total phenols
8. Flavanoids
9. Nonflavanoid phenols
10. Proanthocyanins
11. Color intensity
12. Hue
13. OD280/OD315 of diluted wines
14. Proline

### Data Splits

None

## Dataset Creation

### Source Data

https://archive.ics.uci.edu/ml/datasets/wine

#### Initial Data Collection and Normalization

Original Owners:

Forina, M. et al, PARVUS -
An Extendible Package for Data Exploration, Classification and Correlation.
Institute of Pharmaceutical and Food Analysis and Technologies, Via Brigata Salerno,
16147 Genoa, Italy.

## Additional Information

### Dataset Curators

Stefan Aeberhard

### Licensing Information

No information found on the original website