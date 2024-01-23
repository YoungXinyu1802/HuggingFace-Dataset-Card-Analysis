---
language:
- en
license:
- mit
task_categories:
- question-answering
- summarization
- text-generation
task_ids:
- multiple-choice-qa
- natural-language-inference
configs:
- gov_report
- summ_screen_fd
- qmsum
- qasper
- narrative_qa
- quality
- contract_nli
- squad
- squad_shuffled_distractors
- squad_ordered_distractors
- hotpotqa
- hotpotqa_second_only
tags:
- multi-hop-question-answering
- query-based-summarization
- long-texts
---

## Dataset Description
- **Repository:** [SLED Github repository](https://github.com/Mivg/SLED)
- **Paper:** [Efficient Long-Text Understanding with Short-Text Models
](https://arxiv.org/pdf/2208.00748.pdf)

# Dataset Card for SCROLLS

## Overview
This dataset is based on the [SCROLLS](https://huggingface.co/datasets/tau/scrolls) dataset ([paper](https://arxiv.org/pdf/2201.03533.pdf)), the [SQuAD 1.1](https://huggingface.co/datasets/squad) dataset and the [HotpotQA](https://huggingface.co/datasets/hotpot_qa) dataset.
It doesn't contain any unpblished data, but includes the configuration needed for the [Efficient Long-Text Understanding with Short-Text Models
](https://arxiv.org/pdf/2208.00748.pdf) paper.

## Tasks
The tasks included are:

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

#### SQuAD 1.1 ([Rajpurkar et al., 2016](https://arxiv.org/pdf/1606.05250.pdf)) 
Stanford Question Answering Dataset (SQuAD) is a reading comprehension \
dataset, consisting of questions posed by crowdworkers on a set of Wikipedia \
articles, where the answer to every question is a segment of text, or span, \
from the corresponding reading passage, or the question might be unanswerable.

#### HotpotQA ([Yang et al., 2018](https://arxiv.org/pdf/1809.09600.pdf))  
HotpotQA is a new dataset with 113k Wikipedia-based question-answer pairs with four key features:
(1) the questions require finding and reasoning over multiple supporting documents to answer;
(2) the questions are diverse and not constrained to any pre-existing knowledge bases or knowledge schemas;
(3) we provide sentence-level supporting facts required for reasoning, allowingQA systems to reason with strong supervisionand explain the predictions;
(4) we offer a new type of factoid comparison questions to testQA systems’ ability to extract relevant facts and perform necessary comparison.

## Data Fields

All the datasets in the benchmark are in the same input-output format

- `input`: a `string` feature. The input document.
- `input_prefix`: an optional `string` feature, for the datasets containing prefix (e.g. question)
- `output`: a `string` feature. The target.
- `id`: a `string` feature. Unique per input.
- `pid`: a `string` feature. Unique per input-output pair (can differ from 'id' in NarrativeQA and Qasper, where there is more then one valid target).

The dataset that contain `input_prefix` are:
- SQuAD - the question
- HotpotQA - the question
- qmsum - the query
- qasper  - the question
- narrative_qa - the question
- quality - the question + the four choices
- contract_nli - the hypothesis

## Controlled experiments
To test multiple properties of SLED, we modify SQuAD 1.1 [Rajpurkar et al., 2016](https://arxiv.org/pdf/1606.05250.pdf) 
and HotpotQA [Yang et al., 2018](https://arxiv.org/pdf/1809.09600.pdf) to create a few controlled experiments settings.
Those are accessible via the following configurations:
- squad - Contains the original version of SQuAD 1.1 (question + passage)
- squad_ordered_distractors - For each example, 9 random distrctor passages are concatenated (separated by '\n')
- squad_shuffled_distractors - For each example, 9 random distrctor passages are added (separated by '\n'), and jointly the 10 passages are randomly shuffled
- hotpotqa - A clean version of HotpotQA, where each input contains only the two gold passages (separated by '\n')
- hotpotqa_second_only - In each example, the input contains only the second gold passage

## Citation
If you use this dataset, **please make sure to cite all the original dataset papers as well SCROLLS.** [[bibtex](https://drive.google.com/uc?export=download&id=1IUYIzQD9DPsECw0JWkwk4Ildn8JOMtuU)]
```
@inproceedings{Ivgi2022EfficientLU,
  title={Efficient Long-Text Understanding with Short-Text Models},
  author={Maor Ivgi and Uri Shaham and Jonathan Berant},
  year={2022}
}
```