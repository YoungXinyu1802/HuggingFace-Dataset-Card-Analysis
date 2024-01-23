---
annotations_creators:
- expert-generated
language:
- en
language_creators:
- found
license:
- cc-by-nc-sa-4.0
multilinguality:
- monolingual
pretty_name: fcc-comments
size_categories:
- 10M<n<100M
source_datasets:
- original
tags:
- notice and comment
- regulation
- government
task_categories:
- text-retrieval
task_ids:
- document-retrieval
---

# Dataset Card for fcc-comments

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

- **Repository: https://github.com/slnader/fcc-comments **
- **Paper: https://doi.org/10.1002/poi3.327 **

### Dataset Summary

Online comment floods during public consultations have posed unique governance challenges for 
regulatory bodies seeking relevant information on proposed regulations. 
How should regulatory bodies separate spam and fake comments from genuine submissions by the public, 
especially when fake comments are designed to imitate ordinary citizens? How can regulatory bodies 
achieve both breadth and depth in their citations to the comment corpus? What is the best way to 
select comments that represent the average submission and comments that supply highly specialized 
information?

`fcc-comments` is an annotated version of the comment corpus from the Federal Communications Commission's 
(FCC) 2017 "Restoring Internet Freedom" proceeding. The source data were downloaded directly from the FCC's Electronic 
Comment Filing System (ECFS) between January and February of 2019 and include raw comment text and metadata on 
comment submissions. The comment data were processed to be in a consistent format
(machine-readable pdf or plain text), and annotated with three types of information: whether the comment was cited in the 
agency's final order, the type of commenter (individual, interest group, business group), and whether the comment was associated with an in-person meeting.

The release also includes query-term and document-term matrices to facilitate keyword searches on the comment corpus. 
An example of how these can be used with the bm25 algorithm can be found 
[here](https://github.com/slnader/fcc-comments/blob/main/process_comments/1_score_comments.py).

## Dataset Structure

FCC relational database (fcc.pgsql): The core components of the database include a table for submission metadata, 
a table for attachment metadata, a table for filer metadata, and a table that contains comment text if submitted in express format. 
In addition to these core tables, there are several derived tables specific to the analyses in the paper, 
including which submissions and attachments were cited in the final order, which submissions were associated with in-person meetings, 
and which submissions were associated with interest groups. Full documentation of the tables can be found in fcc_database.md.

Attachments (attachments.tar.gz): Attachments to submissions that could be converted to text via OCR and saved in machine-readable pdf format. 
The filenames are formatted as [submission_id]_[document_id].pdf, where submission_id and document_id are keys in the relational database.

Search datasets (search.tar.gz): Objects to facilitate prototyping of search algorithms on the comment corpus. Contains the following elements:

| Filename      | description |
| ----------- | ----------- |
query_dtm.pickle | Query-term matrix (79x3986) in sparse csr format (rows are queries, columns are bigram keyword counts).
query_text.pickle | Dictionary keyed by the paragraph number in the FCC’s Notice of Proposed Rulemaking. Values are the text of the query containing a call for comments. |
search_dtms_express.pickle | Document-term matrix for express comments (3800691x3986) in sparse csr format (rows are comment pages, columns are bigram keyword counts). |
search_index_express.pickle | Pandas dataframe containing unique id and total term length for express comments. |
search_dtms.pickle | Document-term matrix for standard comment attachments (44655x3986) in sparse csr format (rows are comment pages, columns are bigram keyword counts). |
search_index.pickle | Pandas dataframe containing unique id and total term length for standard comment attachments. |

### Data Fields

The following tables are available in fcc.pgsql:

- comments: plain text comments associated with submissions

| column      | type | description |
| ----------- | ----------- | ----------- |
| comment_id      | character varying(64)       | unique id for plain text comment |
comment_text | text | raw text of plain text comment
row_id | integer | row sequence for plain text comments

- submissions: metadata for submissions

| column      | type | description |
| ----------- | ----------- | ----------- |
submission_id   | character varying(20)  | unique id for submission
submission_type | character varying(100) | type of submission (e.g., comment, reply, statement)
express_comment | numeric                | 1 if express comment
date_received   | date                   | date submission was received
contact_email   | character varying(255) | submitter email address
city            | character varying(255) | submitter city
address_line_1  | character varying(255) | submitter address line 1
address_line_2  | character varying(255) | submitter address line 2
state           | character varying(255) | submitter state
zip_code        | character varying(50)  | submitter zip
comment_id      | character varying(64)  | unique id for plain text comment

- filers: names of filers associated with submissions

| column      | type | description |
| ----------- | ----------- | ----------- |
submission_id | character varying(20)  | unique id for submission
filer_name    | character varying(250) | name of filer associated with submission

- documents: attachments associated with submissions

| column      | type | description |
| ----------- | ----------- | ----------- |
submission_id   | character varying(20) | unique id for submission
document_name   | text                  | filename of attachment
download_status | numeric               | status of attachment download
document_id     | character varying(64) | unique id for attachment
file_extension  | character varying(4)  | file extension for attachment

- filers_cited: citations from final order

| column      | type | description |
| ----------- | ----------- | ----------- |
point           | numeric                | paragraph number in final order
filer_name      | character varying(250) | name of cited filer
submission_type | character varying(12)  | type of submission as indicated in final order
page_numbers    | text[]                 | cited page numbers
cite_id         | integer                | unique id for citation
filer_id        | character varying(250) | id for cited filer

- docs_cited: attachments associated with cited submissions

| column      | type | description |
| ----------- | ----------- | ----------- |
cite_id       | numeric               | unique id for citation
submission_id | character varying(20) | unique id for submission
document_id   | character varying(64) | unique id for attachment


- near_duplicates: lookup table for comment near-duplicates

| column      | type | description |
| ----------- | ----------- | ----------- |
target_document_id    | unique id for target document
duplicate_document_id | unique id for duplicate of target document

- exact_duplicates: lookup table for comment exact duplicates

| column      | type | description |
| ----------- | ----------- | ----------- |
target_document_id    | character varying(100) | unique id for target document
duplicate_document_id | character varying(100) | unique id for duplicate of target document   

- in_person_exparte: submissions associated with ex parte meeting

| column      | type | description |
| ----------- | ----------- | ----------- |
submission_id   | character varying(20) | unique id for submission

- interest_groups: submissions associated with interest groups

| column      | type | description |
| ----------- | ----------- | ----------- |
submission_id | character varying(20) | unique id for submission
business      | numeric | 1 if business group, 0 otherwise


## Dataset Creation

### Curation Rationale

The data were curated to perform information retrieval and summarization tasks as documented in https://doi.org/10.1002/poi3.327. 

### Source Data

#### Initial Data Collection and Normalization

The data for this study come from the FCC's Electronic Comment Filing System (ECFS) system, accessed between January and February of 2019. 
I converted the API responses into a normalized, relational database containing information on 23,951,967 submissions.
23,938,686 "express" submissions contained a single plain text comment submitted directly through the comment form. 
13,821 "standard" submissions contained one or more comment documents submitted as attachments in various file formats. 
While the FCC permitted any file format for attachments, I only consider documents attached in pdf, plain text, rich text, 
and Microsoft Word file formats, and I drop submitted documents that were simply copies of the FCC’s official documents (e.g., the NPRM itself). 
Using standard OCR software, I attempted to convert all attachments into plain text and saved them as machine-readable pdfs. 

#### Who are the source language producers?

All submitters of public comments during the public comment period (but see note on fake comments in considerations).

### Annotations

#### Annotation process

- Citations: I consider citations from the main text of the FCC's final rule. I did not include citations to
  supporting documents not available through ECFS (e.g., court decisions), nor did I include citations
  to submissions from prior FCC proceedings. The direct citations to filed submissions are included
  in a series of 1,186 footnotes. The FCC’s citation format typically followed a relatively standard
  pattern: the name of the filer (e.g., Verizon), a description of the document (e.g., Comment), and
  at times a page number. I extracted citations from the text using regular expressions. Based on a
  random sample of paragraphs from the final order, the regular expressions identified 98% of eligible citations, 
  while successfully excluding all non-citation text. In total, this produced 1,886 unique citations.
  I then identified which of the comments were cited. First, I identified all documents from the cited filer 
  that had enough pages to contain the page number cited (if provided), and, where applicable, whose filename 
  contained the moniker from the FCC’s citation (e.g., "Reply"). The majority of citations matched to only one 
  possible comment submitted, and I identified the re- maining cited comments through manual review of the citations. 
  In this way, I was able to tag documents associated with all but three citations. When the same cited document was 
  submitted under multiple separate submissions, I tagged all versions of the document as being cited.

- Commenter type: Comments are labeled as mass comments if 10 or more duplicate or near-duplicate copies were
  submitted by individual commenters. Near-duplicates were defined as comments with non-zero identical information scores.
  To identify the type of commenter for non-mass comments, I take advantage of the fact that the vast majority of organized
  groups preferred standard submissions over express submissions. Any non-mass comment submitted as an express comment was
  coded as coming from an individual. To distinguish between individuals and organizations that used standard submissions,
  I use a first name and surname database from the names dataset Python package to characterize filer names as belonging to
  individuals or organizations. I also use the domain of the submitter’s email address to re-categorize comments as coming
  from organizations if they were submitted on behalf of organizations by an individual. Government officials were identified by
  their .gov email addresses. I manually review this procedure for mischaracterizations. After obtaining a list of organization
  names, I manually code each one as belonging to a business group or a non-business group. Government officials writing in
  their official capacity were categorized as a non-business group.

- In-person meetings: To identify which commenters held in-person meetings with the agency, I collect all comments labeled
  as an ex-parte submission in the EFCS. I manually review these submissions for mention of an in-person meeting. I label
  a commenter as having held an in-person meeting if they submitted at least one ex-parte document that mentioned an in-person meeting.

#### Who are the annotators?

Annotations are a combination of automated and manual review done by the author.

### Personal and Sensitive Information

This dataset may contain personal and sensitive information, as there were no restrictions on what commenters could submit to 
the agency. This dataset also contains numerous examples of profanity and spam. These comments represent what the FCC decided was 
appropriate to share publicly on their own website.

## Considerations for Using the Data

### Discussion of Biases

This proceeding was famous for the large number of "fake" comments (comments impersonating ordinary citizens) submitted to the 
agency (see [this report](https://ag.ny.gov/sites/default/files/oag-fakecommentsreport.pdf) by the NY AG for more information).
As such, this comment corpus contains a mix of computer-generated and natural language, and there is currently no way to reliably separate 
mass comments submitted with the approval of the commenter and those submitted on behalf of the commenter without their knowledge.

## Additional Information

### Licensing Information

CreativeCommons Attribution-NonCommercial-ShareAlike 4.0 International.

### Citation Information

```
@article{handan2022,
  title={Do fake online comments pose a threat to regulatory policymaking? Evidence from Internet regulation in the United States},
  author={Handan-Nader, Cassandra},
  journal={Policy \& Internet},
  year={2022}
}
```