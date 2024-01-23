---
pretty_name: XML-parsed PMC
task_categories:
- text-classification
- summarization
- other
annotations_creators:
- no-annotation
language_creators:
- expert-generated
language:
- en
size_categories:
- 1M<n<10M
source_datasets:
- original
license:
- cc0-1.0
- cc-by-4.0
- cc-by-sa-4.0
- cc-by-nc-4.0
- cc-by-nd-4.0
- cc-by-nc-nd-4.0
- cc-by-nc-sa-4.0
- unknown
- other
multilinguality:
- monolingual
task_ids: []
tags:
- research papers
- biology
- medecine
---

# Dataset Card for PMC Open Access XML

## Table of Contents
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

## Dataset Description

- **Homepage:** https://www.ncbi.nlm.nih.gov/pmc/tools/openftlist/
- **Repository:** [Needs More Information]
- **Paper:** [Needs More Information]
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [Needs More Information]

### Dataset Summary

The XML Open Access includes more than 3.4 million journal articles and preprints that are made available under
license terms that allow reuse. 
Not all articles in PMC are available for text mining and other reuse, many have copyright protection, however articles
in the PMC Open Access Subset are made available under Creative Commons or similar licenses that generally allow more
liberal redistribution and reuse than a traditional copyrighted work. 
The PMC Open Access Subset is one part of the PMC Article Datasets

This version takes XML version as source, benefiting from the structured text
to split the articles in parts, naming the introduction, methods, results,
discussion and conclusion, and reference with keywords in the text to external or internal
resources (articles, figures, tables, formulas, boxed-text, quotes, code, footnotes, chemicals, graphics, medias).

The dataset was initially created with relation-extraction tasks in mind, between the references in text and the content of the
references (e.g. for PMID, by joining the refered article abstract from the pubmed dataset), but aims in a larger extent to provide
a corpus of pre-annotated text for other tasks (e.g. figure caption to graphic, glossary definition detection, summarization).

### Supported Tasks and Leaderboards

[Needs More Information]

### Languages

[Needs More Information]

## Dataset Structure

### Data Fields

- "accession_id": The PMC ID of the article
- "pmid":         The PubMed ID of the article
- "introduction": List of \<title\> and \<p\> elements in \<body\>, sharing their root with a \<title\> containing "introduction" or "background".
- "methods":      Same as introduction with "method" keyword.
- "results":      Same as introduction with "result" keyword.
- "discussion":   Same as introduction with "discussion" keyword.
- "conclusion":   Same as introduction with "conclusion" keyword. 
- "front":        List of \<title\> and \<p\> elements in \<front\> after everything else has been searched.
- "body":         List of \<title\> and \<p\> elements in \<body\> after everything else has been searched.
- "back":         List of \<title\> and \<p\> elements in \<back\> after everything else has been searched.
- "figure":       List of \<fig\> elements of the article.
- "table":        List of \<table-wrap\> and \<array\> elements of the article.
- "formula":      List of \<disp-formula\> and \<inline-formula\> elements of the article.
- "box":          List of \<boxed-text\> elements of the article.
- "code":         List of \<code\> elements of the article.
- "quote":        List of \<disp-quote\> and \<speech\> elements of the article.
- "chemical":     List of \<chem-struct-wrap\> elements of the article.
- "supplementary": List of \<supplementary-material\> and \<inline-supplementary-material\> elements of the article.
- "footnote":      List of \<fn-group\> and \<table-wrap-foot\> elements of the article.
- "graphic":       List of \<graphic\> and \<inline-graphic\> elements of the article.
- "media":         List of \<media\> and \<inline-media\> elements of the article.
- "glossary": Glossary if found in the XML
- "unknown_references": JSON of a dictionnary of each "tag":"text" for the reference that did not indicate a PMID
- "n_references": Total number of references and unknown references
- "license": The licence of the article
- "retracted": If the article was retracted or not
- "last_updated": Last update of the article
- "citation": Citation of the article
- "package_file": path to the folder containing the graphics and media files of the article (to append to the base URL: ftp.ncbi.nlm.nih.gov/pub/pmc/)

In text, the references are in the form ##KEYWORD##IDX_REF##OLD_TEXT##, with keywords (REF, UREF, FIG, TAB, FORMU, BOX, CODE, QUOTE, CHEM, SUPPL, FOOTN, GRAPH, MEDIA) referencing respectively to "pubmed articles" (external), "unknown_references", "figure", "table", "formula", "box", "code", "quote", "chem", "supplementary", "footnote", "graphic" and "media".
### Data Splits

[Needs More Information]

## Dataset Creation

### Curation Rationale

Internal references (figures, tables, ...) were found using specific tags. Deciding on those tags was done by testing and by looking in the documentation
for the different kind of possible usage.
Then, to split the article into introduction, methods, results, discussion and conclusion, specific keywords in titles were used. Because there are no rules
in this xml to tag those sections, finding the keyword seemed like the most reliable approach to do so. A drawback is that many section do not have those 
keywords in the titles but could be assimilated to those. However, the huge diversity in the titles makes it harder to label such sections. This could be the
work of further versions of this dataset.

### Source Data

#### Initial Data Collection and Normalization

Data was obtained from:
- ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/oa_noncomm/xml/
- ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/oa_comm/xml/
- ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/oa_other/xml/

Additional content for individual articles (graphics, media) can be obtained from:
- ftp.ncbi.nlm.nih.gov/pub/pmc + "package_file"

#### Who are the source language producers?

[Needs More Information]

### Annotations

#### Annotation process

[Needs More Information]

#### Who are the annotators?

[Needs More Information]

### Personal and Sensitive Information

[Needs More Information]

## Considerations for Using the Data

### Social Impact of Dataset

[Needs More Information]

### Discussion of Biases

The articles XML are similar accross collections. This means that if a certain collection handles the structure in unusual ways, the whole collection might not be as
well annotated than others. This concerns all the sections (intro, methods, ...), the external references (pmids) and the internal references (tables, figures, ...).
To illustrate that, references are sometime given as a range (e.g. 10-15). In that case, only reference 10 and 15 are linked. This could potentially be handled in a
future version.

### Other Known Limitations

[Needs More Information]

### Preprocessing recommendations

- Filter out empty contents.
- Remove unwanted references from the text, and replace either by the "references_text" or by the reference content itself.
- Unescape HTML special characters: `import html; html.unescape(my_text)`
- Remove superfluous line break in text.
- Remove XML tags (\<italic\>, \<sup\>, \<sub\>, ...), replace by special tokens? 
- Join the items of the contents' lists.

## Additional Information

### Dataset Curators

[Needs More Information]

### Licensing Information

https://www.ncbi.nlm.nih.gov/pmc/about/copyright/

Within the PMC Open Access Subset, there are three groupings:

Commercial Use Allowed - CC0, CC BY, CC BY-SA, CC BY-ND licenses
Non-Commercial Use Only - CC BY-NC, CC BY-NC-SA, CC BY-NC-ND licenses; and
Other - no machine-readable Creative Commons license, no license, or a custom license.

### Citation Information

[Needs More Information]