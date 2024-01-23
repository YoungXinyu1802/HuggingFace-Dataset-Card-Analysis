---
language:
- en
task_categories:
- question-answering
- summarization
- text-generation
task_ids:
- multiple-choice-qa
- natural-language-inference
paperswithcode_id: scrolls
configs:
- gov_report
- summ_screen_fd
- qmsum
- qasper
- narrative_qa
- quality
- contract_nli
tags:
- query-based-summarization
- long-texts
---

## Dataset Description

- **Homepage:** [SCROLLS](https://www.scrolls-benchmark.com/)
- **Repository:** [SCROLLS Github repository](https://github.com/tau-nlp/scrolls)
- **Paper:** [SCROLLS: Standardized CompaRison Over Long Language Sequences
](https://arxiv.org/pdf/2201.03533.pdf)
- **Leaderboard:** [Leaderboard](https://www.scrolls-benchmark.com/leaderboard)
- **Point of Contact:** [scrolls-benchmark-contact@googlegroups.com](scrolls-benchmark-contact@googlegroups.com)

# Dataset Card for SCROLLS

## Overview
SCROLLS is a suite of datasets that require synthesizing information over long texts. The benchmark includes seven natural language tasks across multiple domains, including summarization, question answering, and natural language inference.

## Leaderboard
The SCROLLS benchmark leaderboard can be found [here](https://www.scrolls-benchmark.com/leaderboard).

## Tasks
SCROLLS comprises the following tasks:

#### GovReport ([Huang et al., 2021](https://arxiv.org/pdf/2104.02112.pdf))
GovReport is a summarization dataset of reports addressing various national policy issues published by the 
Congressional Research Service and the U.S. Government Accountability Office, where each document is paired with a hand-written executive summary.
The reports and their summaries are longer than their equivalents in other popular long-document summarization datasets; 
for example, GovReport's documents are approximately 1.5 and 2.5 times longer than the documents in Arxiv and PubMed, respectively.

#### SummScreenFD ([Chen  et al., 2021](https://arxiv.org/pdf/2104.07091.pdf))
SummScreenFD is a summarization dataset in the domain of TV shows (e.g. Friends, Game of Thrones).
Given a transcript of a specific episode, the goal is to produce the episode's recap.
The original dataset is divided into two complementary subsets, based on the source of its community contributed transcripts. 
For SCROLLS, we use the ForeverDreaming (FD) subset, as it incorporates 88 different shows, 
making it a more diverse alternative to the TV MegaSite (TMS) subset, which has only 10 shows. 
Community-authored recaps for the ForeverDreaming transcripts were collected from English Wikipedia and TVMaze.

#### QMSum ([Zhong et al., 2021](https://arxiv.org/pdf/2104.05938.pdf))
QMSum is a query-based summarization dataset, consisting of 232 meetings transcripts from multiple domains. 
The corpus covers academic group meetings at the International Computer Science Institute and their summaries, industrial product meetings for designing a remote control, 
and committee meetings of the Welsh and Canadian Parliaments, dealing with a variety of public policy issues.
Annotators were tasked with writing queries about the broad contents of the meetings, as well as specific questions about certain topics or decisions, 
while ensuring that the relevant text for answering each query spans at least 200 words or 10 turns.

#### NarrativeQA ([Kočiský et al., 2021](https://arxiv.org/pdf/1712.07040.pdf))
NarrativeQA (Kočiský et al., 2021) is an established question answering dataset over entire books from Project Gutenberg and movie scripts from different websites.
Annotators were given summaries of the books and scripts obtained from Wikipedia, and asked to generate question-answer pairs, 
resulting in about 30 questions and answers for each of the 1,567 books and scripts.
They were encouraged to use their own words rather then copying, and avoid asking yes/no questions or ones about the cast.
Each question was then answered by an additional annotator, providing each question with two reference answers (unless both answers are identical).

#### Qasper ([Dasigi et al., 2021](https://arxiv.org/pdf/2105.03011.pdf))
Qasper is a question answering dataset over NLP papers filtered from the Semantic Scholar Open Research Corpus (S2ORC).
Questions were written by NLP practitioners after reading only the title and abstract of the papers, 
while another set of NLP practitioners annotated the answers given the entire document.
Qasper contains abstractive, extractive, and yes/no questions, as well as unanswerable ones.

#### QuALITY ([Pang et al., 2021](https://arxiv.org/pdf/2112.08608.pdf))
QuALITY is a multiple-choice question answering dataset over articles and stories sourced from Project Gutenberg, 
the Open American National Corpus, and more.
Experienced writers wrote questions and distractors, and were incentivized to write answerable, unambiguous questions such that in order to correctly answer them, 
human annotators must read large portions of the given document. 
Reference answers were then calculated using the majority vote between of the annotators and writer's answers.
To measure the difficulty of their questions, Pang et al. conducted a speed validation process, 
where another set of annotators were asked to answer questions given only a short period of time to skim through the document.
As a result, 50% of the questions in QuALITY are labeled as hard, i.e. the majority of the annotators in the speed validation setting chose the wrong answer.

#### ContractNLI ([Koreeda and Manning, 2021](https://arxiv.org/pdf/2110.01799.pdf))
Contract NLI is a natural language inference dataset in the legal domain.
Given a non-disclosure agreement (the premise), the task is to predict whether a particular legal statement (the hypothesis) is entailed, not entailed (neutral), or cannot be entailed (contradiction) from the contract.
The NDAs were manually picked after simple filtering from the Electronic Data Gathering, Analysis, and Retrieval system (EDGAR) and Google.
The dataset contains a total of 607 contracts and 17 unique hypotheses, which were combined to produce the dataset's 10,319 examples.

## Data Fields

All the datasets in the benchmark are in the same input-output format

- `input`: a `string` feature. The input document.
- `output`: a `string` feature. The target.
- `id`: a `string` feature. Unique per input.
- `pid`: a `string` feature. Unique per input-output pair (can differ from 'id' in NarrativeQA and Qasper, where there is more then one valid target).

## Citation
If you use the SCROLLS data, **please make sure to cite all of the original dataset papers.** [[bibtex](https://scrolls-tau.s3.us-east-2.amazonaws.com/scrolls_datasets.bib)]
```
@inproceedings{shaham-etal-2022-scrolls,
    title = "{SCROLLS}: Standardized {C}ompa{R}ison Over Long Language Sequences",
    author = "Shaham, Uri  and
      Segal, Elad  and
      Ivgi, Maor  and
      Efrat, Avia  and
      Yoran, Ori  and
      Haviv, Adi  and
      Gupta, Ankit  and
      Xiong, Wenhan  and
      Geva, Mor  and
      Berant, Jonathan  and
      Levy, Omer",
    booktitle = "Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing",
    month = dec,
    year = "2022",
    address = "Abu Dhabi, United Arab Emirates",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.emnlp-main.823",
    pages = "12007--12021",
}
```