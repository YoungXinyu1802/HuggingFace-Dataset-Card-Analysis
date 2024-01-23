---
annotations_creators:
- expert-generated
language_creators:
- expert-generated
language:
- en
license:
- unknown
multilinguality:
- monolingual
size_categories:
- 1K<n<10K
source_datasets:
- original
task_categories:
- question-answering
- summarization
- text-retrieval
pretty_name: slp3ed-iknlp2022
tags:
- question-generation
---

# Dataset Card for IK-NLP-22 Speech and Language Processing

## Table of Contents

- [Dataset Card for IK-NLP-22 Speech and Language Processing](#dataset-card-for-ik-nlp-22-speech-and-language-processing)
  - [Table of Contents](#table-of-contents)
  - [Dataset Description](#dataset-description)
    - [Dataset Summary](#dataset-summary)
    - [Projects](#projects)
    - [Languages](#languages)
  - [Dataset Structure](#dataset-structure)
    - [Data Instances](#data-instances)
      - [Paragraphs Configuration](#paragraphs-configuration)
      - [Questions Configuration](#questions-configuration)
    - [Data Splits](#data-splits)
    - [Dataset Creation](#dataset-creation)
  - [Additional Information](#additional-information)
    - [Dataset Curators](#dataset-curators)
    - [Licensing Information](#licensing-information)
    - [Citation Information](#citation-information)

## Dataset Description

- **Source:** [Stanford](https://web.stanford.edu/~jurafsky/slp3/)
- **Point of Contact:** [Gabriele Sarti](mmailto:ik-nlp-course@rug.nl)

### Dataset Summary

This dataset contains chapters extracted from the Speech and Language Processing book (3ed draft of January 2022) by Jurafsky and Martin via a semi-automatic procedure (see below for additional details). Moreover, a small set of conceptual questions associated with each chapter is provided alongside possible answers.

Only the content of chapters 2 to 11 of the book draft are provided, since these are the ones relevant to the contents of the 2022 edition of the Natural Language Processing course at the Information Science Master's Degree (IK) at the University of Groningen, taught by [Arianna Bisazza](https://research.rug.nl/en/persons/arianna-bisazza) with the assistance of [Gabriele Sarti](https://research.rug.nl/en/persons/gabriele-sarti).

*The Speech and Language Processing book was made freely available by the authors [Dan Jurafsky](http://web.stanford.edu/people/jurafsky/) and [James H. Martin](http://www.cs.colorado.edu/~martin/) on the [Stanford University website](https://web.stanford.edu/~jurafsky/slp3/). The present dataset was created for educational purposes, and is based on the draft of the 3rd edition of the book accessed on December 29th, 2021. All rights of the present contents are attributed to the original authors.*

### Projects

See the course page for a description of possible research directions.

### Languages

The language data of Speech and Language Processing is in English (BCP-47 `en`)

## Dataset Structure

### Data Instances

The dataset contains two configurations: `paragraphs` (default), containing the full set of parsed paragraphs associated to the respective chapter and sections, and `questions`, containing a small subset of example questions matched with the relevant paragraph, and with the answer span extracted.

#### Paragraphs Configuration

The `paragraphs` configuration contains all the paragraphs of the selected book chapters, each associated with the respective chapter, section and subsection. An example from the `train` split of the `paragraphs` config is provided below. The example belongs to section 2.3 but not to a subsection, so the `n_subsection` and `subsection` fields are empty strings.

```json
{
    "n_chapter": "2",
    "chapter": "Regular Expressions",
    "n_section": "2.3",
    "section": "Corpora",
    "n_subsection": "",
    "subsection": "",
    "text": "It's also quite common for speakers or writers to use multiple languages in a single communicative act, a phenomenon called code switching. Code switching (2.2) Por primera vez veo a @username actually being hateful! it was beautiful:)"
}
```

The text is provided as-is, without further preprocessing or tokenization.


#### Questions Configuration

The `questions` configuration contains a small subset of questions, the top retrieved paragraph relevant to the question and the answer spans. An example from the `test` split of the `questions` config is provided below.

 ```json
{
    "chapter": "Regular Expressions",
    "section": "Regular Expressions",
    "subsection": "Basic Regular Expressions",
    "question": "What is the meaning of the Kleene star in Regex?",
    "paragraph": "This language consists of strings with a b, followed by at least two a's, followed by an exclamation point. The set of operators that allows us to say things like \"some number of as\" are based on the asterisk or *, commonly called the Kleene * (gen-Kleene * erally pronounced \"cleany star\"). The Kleene star means \"zero or more occurrences of the immediately previous character or regular expression\". So /a*/ means \"any string of zero or more as\". This will match a or aaaaaa, but it will also match Off Minor since the string Off Minor has zero a's. So the regular expression for matching one or more a is /aa*/, meaning one a followed by zero or more as. More complex patterns can also be repeated. So /[ab]*/ means \"zero or more a's or b's\" (not \"zero or more right square braces\"). This will match strings like aaaa or ababab or bbbb.",
    "answer": "The Kleene star means \"zero or more occurrences of the immediately previous character or regular expression\""
}
 ```

### Data Splits

|       config| train| test|
|------------:|-----:|----:|
|`paragraphs` | 1697 | -   |
|`questions`  | -    | 59  |

### Dataset Creation

The contents of the Speech and Language Processing book PDF were extracted using the [PDF to S2ORC JSON Converter](https://github.com/allenai/s2orc-doc2json) by AllenAI. The texts extracted by the converter were then manually cleaned to remove end-of-chapter exercises and other irrelevant content (e.g. tables, TikZ figures, etc.). Some issues in the parsed content were preserved in the final version to maintain a naturalistic setting for the associated projects, promoting the use of data filtering heuristics for students.

The question-answer pairs were created manually by Gabriele Sarti.

## Additional Information

### Dataset Curators

For problems on this 🤗 Datasets version, please contact us at [ik-nlp-course@rug.nl](mailto:ik-nlp-course@rug.nl).

### Licensing Information

Please refer to the authors' websites for licensing information.

### Citation Information

Please cite the authors if you use these corpora in your work:

```bibtex
@book{slp3ed-iknlp2022,
    author = {Jurafsky, Daniel and Martin, James},
    year = {2021},
    month = {12},
    pages = {1--235, 1--19},
    title = {Speech and Language Processing: An Introduction to Natural Language Processing, Computational Linguistics, and Speech Recognition},
    volume = {3}
}
```