---
annotations_creators:
- expert-generated
language:
- en
- it
- fr
- ar
- de
- hi
- pt
- ru
- es
language_creators:
- expert-generated
license:
- cc-by-sa-3.0
multilinguality:
- translation
pretty_name: mt_geneval
size_categories:
- 1K<n<10K
source_datasets:
- original
tags:
- gender
- constrained mt
task_categories:
- translation
task_ids: []
---

# Dataset Card for MT-GenEval

## Table of Contents

- [Dataset Card for MT-GenEval](#dataset-card-for-mt-geneval)
  - [Table of Contents](#table-of-contents)
  - [Dataset Description](#dataset-description)
    - [Dataset Summary](#dataset-summary)
    - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
      - [Machine Translation](#machine-translation)
    - [Languages](#languages)
  - [Dataset Structure](#dataset-structure)
    - [Data Instances](#data-instances)
    - [Data Splits](#data-splits)
    - [Dataset Creation](#dataset-creation)
  - [Additional Information](#additional-information)
    - [Dataset Curators](#dataset-curators)
    - [Licensing Information](#licensing-information)
    - [Citation Information](#citation-information)

## Dataset Description

- **Repository:** [Github](https://github.com/amazon-science/machine-translation-gender-eval)
- **Paper:** [EMNLP 2022](https://arxiv.org/abs/2211.01355)
- **Point of Contact:** [Anna Currey](mailto:ancurrey@amazon.com)

### Dataset Summary

The MT-GenEval benchmark evaluates gender translation accuracy on English -> {Arabic, French, German, Hindi, Italian, Portuguese, Russian, Spanish}. The dataset contains individual sentences with annotations on the gendered target words, and contrastive original-invertend translations with additional preceding context.

**Disclaimer**: *The MT-GenEval benchmark was released in the EMNLP 2022 paper [MT-GenEval: A Counterfactual and Contextual Dataset for Evaluating Gender Accuracy in Machine Translation](https://arxiv.org/abs/2211.01355) by Anna Currey, Maria Nadejde, Raghavendra Pappagari, Mia Mayer, Stanislas Lauly, Xing Niu, Benjamin Hsu, and Georgiana Dinu and is hosted through Github by the [Amazon Science](https://github.com/amazon-science?type=source) organization. The dataset is licensed under a [Creative Commons Attribution-ShareAlike 3.0 Unported License](https://creativecommons.org/licenses/by-sa/3.0/).*

### Supported Tasks and Leaderboards
#### Machine Translation
Refer to the [original paper](https://arxiv.org/abs/2211.01355) for additional details on gender accuracy evaluation with MT-GenEval.
### Languages
The dataset contains source English sentences extracted from Wikipedia translated into the following languages: Arabic (`ar`), French (`fr`), German (`de`), Hindi (`hi`), Italian (`it`), Portuguese (`pt`), Russian (`ru`), and Spanish (`es`).
## Dataset Structure
### Data Instances

The dataset contains two configuration types, `sentences` and `context`, mirroring the original repository structure, with source and target language specified in the configuration name (e.g. `sentences_en_ar`, `context_en_it`) The `sentences` configurations contains masculine and feminine versions of individual sentences with gendered word annotations. Here is an example entry of the `sentences_en_it` split (all `sentences_en_XX` splits have the same structure):

```json
{
{
  "orig_id": 0,
  "source_feminine": "Pagratidis quickly recanted her confession, claiming she was psychologically pressured and beaten, and until the moment of her execution, she remained firm in her innocence.",
  "reference_feminine": "Pagratidis subito ritrattò la sua confessione, affermando che era aveva subito pressioni psicologiche e era stata picchiata, e fino al momento della sua esecuzione, rimase ferma sulla sua innocenza.",
  "source_masculine": "Pagratidis quickly recanted his confession, claiming he was psychologically pressured and beaten, and until the moment of his execution, he remained firm in his innocence.",
  "reference_masculine": "Pagratidis subito ritrattò la sua confessione, affermando che era aveva subito pressioni psicologiche e era stato picchiato, e fino al momento della sua esecuzione, rimase fermo sulla sua innocenza.",
  "source_feminine_annotated": "Pagratidis quickly recanted <F>her</F> confession, claiming <F>she</F> was psychologically pressured and beaten, and until the moment of <F>her</F> execution, <F>she</F> remained firm in <F>her</F> innocence.",
  "reference_feminine_annotated": "Pagratidis subito ritrattò la sua confessione, affermando che era aveva subito pressioni psicologiche e era <F>stata picchiata</F>, e fino al momento della sua esecuzione, rimase <F>ferma</F> sulla sua innocenza.",
  "source_masculine_annotated": "Pagratidis quickly recanted <M>his</M> confession, claiming <M>he</M> was psychologically pressured and beaten, and until the moment of <M>his</M> execution, <M>he</M> remained firm in <M>his</M> innocence.",
  "reference_masculine_annotated": "Pagratidis subito ritrattò la sua confessione, affermando che era aveva subito pressioni psicologiche e era <M>stato picchiato</M>, e fino al momento della sua esecuzione, rimase <M>fermo</M> sulla sua innocenza.",
  "source_feminine_keywords": "her;she;her;she;her",
  "reference_feminine_keywords": "stata picchiata;ferma",
  "source_masculine_keywords": "his;he;his;he;his",
  "reference_masculine_keywords": "stato picchiato;fermo",
}
}
```

The `context` configuration contains instead different English sources related to stereotypical professional roles with additional preceding context and contrastive original-inverted translations. Here is an example entry of the `context_en_it` split (all `context_en_XX` splits have the same structure):

```json
{
  "orig_id": 0,
  "context": "Pierpont told of entering and holding up the bank and then fleeing to Fort Wayne, where the loot was divided between him and three others.",
  "source": "However, Pierpont stated that Skeer was the planner of the robbery.",
  "reference_original": "Comunque, Pierpont disse che Skeer era il pianificatore della rapina.",
  "reference_flipped": "Comunque, Pierpont disse che Skeer era la pianificatrice della rapina."
}
```

### Data Splits

All `sentences_en_XX` configurations have 1200 examples in the `train` split and 300 in the `test` split. For the `context_en_XX` configurations, the number of example depends on the language pair:

| Configuration   | # Train    | # Test  |
| :-----------:   | :--------: | :-----: |
| `context_en_ar` |    792     |  1100   |
| `context_en_fr` |    477     |  1099   |
| `context_en_de` |    598     |  1100   |
| `context_en_hi` |    397     |  1098   |
| `context_en_it` |    465     |  1904   |
| `context_en_pt` |    574     |  1089   |
| `context_en_ru` |    583     |  1100   |
| `context_en_es` |    534     |  1096   |

### Dataset Creation

From the original paper:

>In developing MT-GenEval, our goal was to create a realistic, gender-balanced dataset that naturally incorporates a diverse range of gender phenomena. To this end, we extracted English source sentences from Wikipedia as the basis for our dataset. We automatically pre-selected relevant sentences using EN gender-referring words based on the list provided by [Zhao et al. (2018)](https://doi.org/10.18653/v1/N18-2003).

Please refer to the original article [MT-GenEval: A Counterfactual and Contextual Dataset for Evaluating Gender Accuracy in Machine Translation](https://arxiv.org/abs/2211.01355) for additional information on dataset creation.

## Additional Information
### Dataset Curators

The original authors of MT-GenEval are the curators of the original dataset. For problems or updates on this 🤗 Datasets version, please contact [gabriele.sarti996@gmail.com](mailto:gabriele.sarti996@gmail.com).

### Licensing Information

The dataset is licensed under the [Creative Commons Attribution-ShareAlike 3.0 International License](https://creativecommons.org/licenses/by-sa/3.0/).

### Citation Information
Please cite the authors if you use these corpora in your work.

```bibtex
@inproceedings{currey-etal-2022-mtgeneval,
    title = "{MT-GenEval}: {A} Counterfactual and Contextual Dataset for Evaluating Gender Accuracy in Machine Translation",
    author = "Currey, Anna  and
      Nadejde, Maria  and
      Pappagari, Raghavendra  and
      Mayer, Mia  and
      Lauly, Stanislas,  and
      Niu, Xing  and
      Hsu, Benjamin  and
      Dinu, Georgiana",
    booktitle = "Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing",
    month = dec,
    year = "2022",
    publisher = "Association for Computational Linguistics",
    url = "https://arxiv.org/abs/2211.01355",
}
```