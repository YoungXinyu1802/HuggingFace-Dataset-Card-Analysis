---
license: cc
size_categories:
- 1K<n<10K
---

# Dataset Card for Dataset Name

## Dataset Description

- **Homepage:** [Original dataset release](https://figshare.com/articles/dataset/_5_Million_Python_Bash_Programming_Submissions_for_5_Courses_Grades_for_Computer-Based_Exams_over_3_academic_years_/12610958), and the [processed version](https://github.com/GCleuziou/code2aes2vec/tree/master/Datasets)
- **Repository:** [GitHub](https://github.com/dazcona/user2code2vec) [GitHub](https://github.com/dazcona/user2code2vec)
- **Paper:** [Original paper](https://dl.acm.org/doi/10.1145/3303772.3303813) which released the raw data, and the [paper](https://files.eric.ed.gov/fulltext/ED615546.pdf) that repreprocessed it. 

### Dataset Summary

The Dublin programming dataset is a dataset composed of students' submissions to introductory programming assignments at the University of Dublin. 
Students submitted these programs for multiple programming courses over the duration of three academic years. 

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

The assignments were written in Python. 

## Dataset Structure

### Data Instances

Each data instance is the submitted solution from one student (i.e. one user of the original grading system) for one programming assignment. 
The submitted solution might or might not be correct (depending on whether it passes all tests). 

### Data Fields

* submission_id: a unique number identifying the submission
* user: a unique string identifying the (anonymized) student who submitted the solution
* date: the timestamp at which the grading server received the submission
* func_code: the cleaned code submitted
* func_name: the name of the function that had to be implemented
* assingment_id: the unique (string) identifier of the assignment that had to be completed
* academic_year: the starting year of the academic year (e.g. 2015 for the academic year 2015-2016)
* module: the course/module
* test: a humaneval-style string which can be used to execute the submitted solution on the provided test cases
* description: a description of what the function is supposed to achieve
* correct: whether the solution passed all tests or not


## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

This released dataset is a subset of the data preprocessed from 
[Cleuziou et al.](https://files.eric.ed.gov/fulltext/ED615546.pdf), the original data coming from this [source](https://figshare.com/articles/dataset/_5_Million_Python_Bash_Programming_Submissions_for_5_Courses_Grades_for_Computer-Based_Exams_over_3_academic_years_/12610958).


## Considerations for Using the Data

### Other Known Limitations

[More Information Needed]

## Additional Information

### Licensing Information

The original data was released under a [Creative Commons](https://creativecommons.org/licenses/by/4.0/) license.

### Citation Information

```
@inproceedings{azcona2019user2code2vec,
  title={user2code2vec: Embeddings for Profiling Students Based on Distributional Representations of Source Code},
  author={Azcona, David and Arora, Piyush and Hsiao, I-Han and Smeaton, Alan},
  booktitle={Proceedings of the 9th International Learning Analytics & Knowledge Conference (LAK’19)},
  year={2019},
  organization={ACM}
}
```
```
@inproceedings{DBLP:conf/edm/CleuziouF21,
  author    = {Guillaume Cleuziou and
               Fr{\'{e}}d{\'{e}}ric Flouvat},
  editor    = {Sharon I{-}Han Hsiao and
               Shaghayegh (Sherry) Sahebi and
               Fran{\c{c}}ois Bouchet and
               Jill{-}J{\^{e}}nn Vie},
  title     = {Learning student program embeddings using abstract execution traces},
  booktitle = {Proceedings of the 14th International Conference on Educational Data
               Mining, {EDM} 2021, virtual, June 29 - July 2, 2021},
  publisher = {International Educational Data Mining Society},
  year      = {2021},
  timestamp = {Wed, 09 Mar 2022 16:47:22 +0100},
  biburl    = {https://dblp.org/rec/conf/edm/CleuziouF21.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```