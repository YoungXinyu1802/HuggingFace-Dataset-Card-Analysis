---
license: cc-by-4.0
---

## About this dataset
The [CAES](http://galvan.usc.es/caes/) [(Parodi, 2015)](https://www.tandfonline.com/doi/full/10.1080/23247797.2015.1084685?cookieSet=1) dataset, also referred as the “Corpus de Aprendices del Español” (CAES), is a collection of texts created by Spanish L2 learners from Spanish learning centres and universities. These students had different learning levels, different backgrounds (11 native languages) and various levels of experience with the language. We used web scraping techniques to download a portion of the full dataset since its current website only provides content filtered by categories that have to be manually selected. The readability level of each text in CAES follows the [Common European Framework of Reference for Languages (CEFR)](https://www.coe.int/en/web/common-european-framework-reference-languages). The [raw version](https://huggingface.co/datasets/lmvasque/caes/blob/main/caes.raw.csv) of this corpus also contains information about the learners and the type of assignments with which they were assigned to create each text.

We have downloaded this dataset from its original [website](https://galvan.usc.es/caes/search) to make it available to the community. If you use this data, please credit the original author and our work as well (see citations below).

## About the splits
We have uploaded two versions of the CAES corpus:
- **caes.raw.csv**: raw data from the website with no further filtering. It includes information about the learners and the type/topic of their assignments.
- **caes.jsonl**: this data is limited to the text samples, the original levels of readability and our standardised category according to these: simple/complex and basic/intermediate/advanced. You can check for more details about these splits in our [paper](https://drive.google.com/file/d/1KdwvqrjX8MWYRDGBKeHmiR1NCzDcVizo/view?usp=share_link).




## Citation 

If you use our splits in your research, please cite our work: "[A Benchmark for Neural Readability Assessment of Texts in Spanish](https://drive.google.com/file/d/1KdwvqrjX8MWYRDGBKeHmiR1NCzDcVizo/view?usp=share_link)"

```
@inproceedings{vasquez-rodriguez-etal-2022-benchmarking,
    title = "A Benchmark for Neural Readability Assessment of Texts in Spanish",
    author = "V{\'a}squez-Rodr{\'\i}guez, Laura  and
      Cuenca-Jim{\'\e}nez, Pedro-Manuel and
      Morales-Esquivel, Sergio Esteban and
      Alva-Manchego, Fernando",
    booktitle = "Workshop on Text Simplification, Accessibility, and Readability (TSAR-2022), EMNLP 2022",
    month = dec,
    year = "2022",
}
```

We have extracted the CAES corpus from their [website](https://galvan.usc.es/caes/search). If you use this corpus, please also cite their work as follows:
```
@article{Parodi2015,
  author = "Giovanni Parodi",
  title = "Corpus de aprendices de español (CAES)",
  journal = "Journal of Spanish Language Teaching",
  volume = "2",
  number = "2",
  pages = "194-200",
  year  = "2015",
  publisher = "Routledge",
  doi = "10.1080/23247797.2015.1084685",
  URL = "https://doi.org/10.1080/23247797.2015.1084685",
  eprint = "https://doi.org/10.1080/23247797.2015.1084685"
}

```

You can also find more details about the project in our [GitHub](https://github.com/lmvasque/readability-es-benchmark).