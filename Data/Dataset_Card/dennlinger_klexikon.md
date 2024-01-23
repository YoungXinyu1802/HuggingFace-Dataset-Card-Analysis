---
annotations_creators:
- found
- expert-generated
language_creators:
- found
- machine-generated
language:
- de
license:
- cc-by-sa-4.0
multilinguality:
- monolingual
size_categories:
- 1K<n<10K
source_datasets:
- original
task_categories:
- summarization
- text2text-generation
task_ids:
- text-simplification
paperswithcode_id: klexikon
pretty_name: Klexikon
tags:
- conditional-text-generation
- simplification
- document-level
---

# Dataset Card for the Klexikon Dataset

## Table of Contents
- [Version History](#version-history)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-instances)
  - [Data Splits](#data-instances)
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
  

## Version History

- **v0.3** (2022-09-01): Removing some five samples from the dataset due to duplication conflicts with other samples.
- **v0.2** (2022-02-28): Updated the files to no longer contain empty sections and removing otherwise empty lines at the end of files. Also removing lines with some sort of coordinate.
- **v0.1** (2022-01-19): Initial data release on Huggingface datasets.

## Dataset Description

- **Homepage:** [N/A]
- **Repository:** [Klexikon repository](https://github.com/dennlinger/klexikon)
- **Paper:** [Klexikon: A German Dataset for Joint Summarization and Simplification](https://arxiv.org/abs/2201.07198)
- **Leaderboard:** [N/A]
- **Point of Contact:** [Dennis Aumiller](mailto:dennis.aumiller@gmail.com)

### Dataset Summary

The Klexikon dataset is a German resource of document-aligned texts between German Wikipedia and the children's lexicon "Klexikon". The dataset was created for the purpose of joint text simplification and summarization, and contains almost 2900 aligned article pairs.
Notably, the children's articles use a simpler language than the original Wikipedia articles; this is in addition to a clear length discrepancy between the source (Wikipedia) and target (Klexikon) domain.

### Supported Tasks and Leaderboards

- `summarization`: The dataset can be used to train a model for summarization. In particular, it poses a harder challenge than some of the commonly used datasets (CNN/DailyMail), which tend to suffer from positional biases in the source text. This makes it very easy to generate high (ROUGE) scoring solutions, by simply taking the leading 3 sentences. Our dataset provides a more challenging extraction task, combined with the additional difficulty of finding lexically appropriate simplifications.
- `simplification`: While not currently supported by the HF task board, text simplification is concerned with the appropriate representation of a text for disadvantaged readers (e.g., children, language learners, dyslexic,...).

For scoring, we ran preliminary experiments based on [ROUGE](https://huggingface.co/metrics/rouge), however, we want to cautiously point out that ROUGE is incapable of accurately depicting simplification appropriateness.
We combined this with looking at Flesch readability scores, as implemented by [textstat](https://github.com/shivam5992/textstat).
Note that simplification metrics such as [SARI](https://huggingface.co/metrics/sari) are not applicable here, since they require sentence alignments, which we do not provide.

### Languages

The associated BCP-47 code is `de-DE`.

The text of the articles is in German. Klexikon articles are further undergoing a simple form of peer-review before publication, and aim to simplify language for 8-13 year old children. This means that the general expected text difficulty for Klexikon articles is lower than Wikipedia's entries.

## Dataset Structure

### Data Instances

One datapoint represents the Wikipedia text (`wiki_text`), as well as the Klexikon text (`klexikon_text`).
Sentences are separated by newlines for both datasets, and section headings are indicated by leading `==` (or `===` for subheadings, `====` for sub-subheading, etc.).
Further, it includes the `wiki_url` and `klexikon_url`, pointing to the respective source texts. Note that the original articles were extracted in April 2021, so re-crawling the texts yourself will likely change some content.
Lastly, we include a unique identifier `u_id` as well as the page title `title` of the Klexikon page.

Sample (abridged texts for clarity):
```
{
    "u_id": 0,
    "title": "ABBA",
    "wiki_url": "https://de.wikipedia.org/wiki/ABBA",
    "klexikon_url": "https://klexikon.zum.de/wiki/ABBA",
    "wiki_sentences": [
      "ABBA ist eine schwedische Popgruppe, die aus den damaligen Paaren Agnetha Fältskog und Björn Ulvaeus sowie Benny Andersson und Anni-Frid Lyngstad besteht und sich 1972 in Stockholm formierte.",
      "Sie gehört mit rund 400 Millionen verkauften Tonträgern zu den erfolgreichsten Bands der Musikgeschichte.",
      "Bis in die 1970er Jahre hatte es keine andere Band aus Schweden oder Skandinavien gegeben, der vergleichbare Erfolge gelungen waren.",
      "Trotz amerikanischer und britischer Dominanz im Musikgeschäft gelang der Band ein internationaler Durchbruch.",
      "Sie hat die Geschichte der Popmusik mitgeprägt.",
      "Zu ihren bekanntesten Songs zählen Mamma Mia, Dancing Queen und The Winner Takes It All.",
      "1982 beendeten die Gruppenmitglieder aufgrund privater Differenzen ihre musikalische Zusammenarbeit.",
      "Seit 2016 arbeiten die vier Musiker wieder zusammen an neuer Musik, die 2021 erscheinen soll.",
    ],
    "klexikon_sentences": [
      "ABBA war eine Musikgruppe aus Schweden.",
      "Ihre Musikrichtung war die Popmusik.",
      "Der Name entstand aus den Anfangsbuchstaben der Vornamen der Mitglieder, Agnetha, Björn, Benny und Anni-Frid.",
      "Benny Andersson und Björn Ulvaeus, die beiden Männer, schrieben die Lieder und spielten Klavier und Gitarre.",
      "Anni-Frid Lyngstad und Agnetha Fältskog sangen."
    ]
  },
```

### Data Fields

* `u_id` (`int`): A unique identifier for each document pair in the dataset. 0-2349 are reserved for training data, 2350-2623 for testing, and 2364-2897 for validation.
* `title` (`str`): Title of the Klexikon page for this sample.
* `wiki_url` (`str`): URL of the associated Wikipedia article. Notably, this is non-trivial, since we potentially have disambiguated pages, where the Wikipedia title is not exactly the same as the Klexikon one.
* `klexikon_url` (`str`): URL of the Klexikon article.
* `wiki_text` (`List[str]`): List of sentences of the Wikipedia article. We prepare a pre-split document with spacy's sentence splitting (model: `de_core_news_md`). Additionally, please note that we do not include page contents outside of `<p>` tags, which excludes lists, captions and images.
* `klexikon_text` (`List[str]`): List of sentences of the Klexikon article. We apply the same processing as for the Wikipedia texts.

### Data Splits

We provide a stratified split of the dataset, based on the length of the respective Wiki article/Klexikon article pair (according to number of sentences).
The x-axis represents the length of the Wikipedia article, and the y-axis the length of the Klexikon article.
We segment the coordinate systems into rectangles of shape `(100, 10)`, and randomly sample a split of 80/10/10 for training/validation/test from each rectangle to ensure stratification. In case of rectangles with less than 10 entries, we put all samples into training.

The final splits have the following size:
* 2350 samples for training
* 274 samples for validation
* 274 samples for testing

## Dataset Creation

### Curation Rationale

As previously described, the Klexikon resource was created as an attempt to bridge the two fields of text summarization and text simplification. Previous datasets suffer from either one or more of the following shortcomings:

* They primarily focus on input/output pairs of similar lengths, which does not reflect longer-form texts.
* Data exists primarily for English, and other languages are notoriously understudied.
* Alignments exist for sentence-level, but not document-level.

This dataset serves as a starting point to investigate the feasibility of end-to-end simplification systems for longer input documents.

### Source Data

#### Initial Data Collection and Normalization

Data was collected from [Klexikon](klexikon.zum.de), and afterwards aligned with corresponding texts from [German Wikipedia](de.wikipedia.org).
Specifically, the collection process was performed in April 2021, and 3145 articles could be extracted from Klexikon back then. Afterwards, we semi-automatically align the articles with Wikipedia, by looking up articles with the same title.
For articles that do not exactly match, we manually review their content, and decide to match to an appropriate substitute if the content can be matched by at least 66% of the Klexikon paragraphs.
Similarly, we proceed to manually review disambiguation pages on Wikipedia.

We extract only full-text content, excluding figures, captions, and list elements from the final text corpus, and only retain articles for which the respective Wikipedia document consists of at least 15 paragraphs after pre-processing.

#### Who are the source language producers?

The language producers are contributors to Klexikon and Wikipedia. No demographic information was available from the data sources.

### Annotations

#### Annotation process

Annotations were performed by manually reviewing the URLs of the ambiguous article pairs. No annotation platforms or existing tools were used in the process.
Otherwise, articles were matched based on the exact title.

#### Who are the annotators?

The manually aligned articles were reviewed by the dataset author (Dennis Aumiller).

### Personal and Sensitive Information

Since Klexikon and Wikipedia are public encyclopedias, no further personal or sensitive information is included. We did not investigate to what extent information about public figures is included in the dataset.

## Considerations for Using the Data

### Social Impact of Dataset

Accessibility on the web is still a big issue, particularly for disadvantaged readers.
This dataset has the potential to strengthen text simplification systems, which can improve the situation.
In terms of language coverage, this dataset also has a beneficial impact on the availability of German data.

Potential negative biases include the problems of automatically aligned articles. The alignments may never be 100% perfect, and can therefore cause mis-aligned articles (or associations), despite the best of our intentions.

### Discussion of Biases

We have not tested whether any particular bias towards a specific article *type* (i.e., "person", "city", etc.) exists.
Similarly, we attempted to present an unbiased (stratified) split for validation and test set, but given that we only cover around 2900 articles, it is possible that these articles represent a particular focal lense on the overall distribution of lexical content.

### Other Known Limitations

Since the articles were written independently of each other, it is not guaranteed that there exists an exact coverage of each sentence in the simplified article, which could also stem from the fact that sometimes Wikipedia pages have separate article pages for aspects (e.g., the city of "Aarhus" has a separate page for its art museum (ARoS). However, Klexikon lists content and description for ARoS on the page of the city itself.

## Additional Information

### Dataset Curators

The dataset was curated only by the author of this dataset, Dennis Aumiller.

### Licensing Information

Klexikon and Wikipedia make their textual contents available under the CC BY-SA license, which will be inherited for this dataset.

### Citation Information

If you use our dataset or associated code, please cite our paper:

```
@inproceedings{aumiller-gertz-2022-klexikon,
    title = "Klexikon: A {G}erman Dataset for Joint Summarization and Simplification",
    author = "Aumiller, Dennis  and
      Gertz, Michael",
    booktitle = "Proceedings of the Thirteenth Language Resources and Evaluation Conference",
    month = jun,
    year = "2022",
    address = "Marseille, France",
    publisher = "European Language Resources Association",
    url = "https://aclanthology.org/2022.lrec-1.288",
    pages = "2693--2701"
}
```
