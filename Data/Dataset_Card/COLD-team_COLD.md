---
license: cc-by-sa-4.0
---
## COLD: Complex Offensive Language Dataset

If you use this dataset, please cite the following paper (BibTex below):

Alexis Palmer, Christine Carr, Melissa Robinson, and Jordan Sanders. 2020 (to appear). COLD: Annotation scheme and evaluation data set for complex offensive language in English. *Journal of Linguistics and Computational Linguistics*. 

## Overview of data

The COLD data set is intended for researchers to diagnose and assess their automatic hate speech detection systems. The corpus highlights 4 different types of complex offensive language: slurs, reclaimed slurs, adjective nominalization, distancing, and also non-offensive texts. The corpus contains a set of tweets collected from 3 different data sets: Davidson et al (2017), Waseem and Hovy (2016), and Robinson (2017). The data is annotated by 6 annotators, with each instance being annotated by at least 3 different annotators.  

**COLD-2016** is the data set used for the analyses and experimental results described in the JLCL paper. This version of the data set contains 2016 instances, selected using filters aiming to capture the complex offensive language types listed above.

## Format and annotations

The data are made available here as .tsv files. The format consists of eight columns: four informational and four annotation-related.

### Informational columns:
1. **ID** - information about the original data set and the textual instance's ID from the data set it was extracted from. The ID includes a letter indicating which data set it originates from, followed by a hyphen and the corresponding ID of the instance in the original data set. For example: D-63 means that the instance is from the Davidson et al. (2017) data set, originally with the ID number 63.

2. **Dataset** - a letter indicating from which dataset this instance originates.
3. **Text** - the text of the instance.

### Majority Vote Columns:

For each instance, annotators were asked to answer Yes or No to each of four questions. Theses columns are the majority vote from three annotators (See the paper for much more detailed discussion, as well as distributions, etc.)

1. **Off** Is this text offensive?

2. **Slur** Is there a slur in the text?

3. **Nom** Is there an adjectival nominalization in the text?

4. **Dist** Is there (linguistic) distancing in the text?

### Individual Annotator Columns:
For each instance, annotators were asked to answer Yes or No to each of four questions. Theses columns are the individual response from each annotators (See the paper for much more detailed discussion, as well as distributions, etc.)

1. **Off1/2/3** Is this text offensive?

2. **Slur1/2/3** Is there a slur in the text?

3. **Nom1/2/3** Is there an adjectival nominalization in the text?

4. **Dist1/2/3** Is there (linguistic) distancing in the text?

### Category

1. **Cat** This column is deduced based on the majority votes for OFF/SLUR/NOM/DIST. (See the paper for detailed explination the categories, as well as distributions, etc.) 

## Contact
If you have any questions please contact carrc9953@gmail.com, alexis.palmer@unt.edu, or melissa.robinson@my.unt.edu.

## BibTex

```
@article{cold:2020,
  title = {COLD: Annotation scheme and evaluation data set for complex offensive language in English},
  author = {Palmer, Alexis and Carr, Christine and Robinson, Melissa and Sanders, Jordan}, 
  journal = {Journal of Linguistics and Computational Linguistics, Special Issue},
  year = {2020},
  volume={to appear},
  number={to appear},
  pages = {tbd}
}
```

## References

Davidson, T., Wamsley, D., Macy, M., & Weber, I. (2017). Automated hate speech detection and 
the problem of offensive language. In Eleventh international conference on web and 
social media. <a href="https://aaai.org/ocs/index.php/ICWSM/ICWSM17/paper/view/15665">[the paper]</a>, <a href="https://github.com/t-davidson/hate-speech-and-offensive-language">[the repository]</a>

Robinson, M. (2018). A man needs a female like a fish needs a lobotomy: The role of adjectival 
nominalization in pejorative meaning. Master's thesis, Department of Linguistics, University of North Texas.
<a href="https://digital.library.unt.edu/ark:/67531/metadc1157617/m2/1/high_res_d/ROBINSON-THESIS-2018.pdf">[the thesis]</a>

Waseem, Z., & Hovy, D. (2016). Hateful Symbols or Hateful People? Predictive Features for 
Hate Speech Detection on Twitter. In Proceedings of the NAACL Student Research Workshop. San Diego, California.
<a href="https://www.aclweb.org/anthology/N16-2013/">[the paper]</a>