---
license: cc-by-4.0
task_categories:
- question-answering
language:
- en
tags:
- Question Answering
- Aviation
- Knowledge Graphs
pretty_name: AviationQA
---
AviationQA is introduced in the paper titled- There is No Big Brother or Small Brother: Knowledge Infusion in Language Models for Link Prediction and Question Answering
https://arxiv.org/abs/2301.04013
The paper is accepted in the main conference of ICON 2022.

We create a synthetic dataset, AviationQA, a set of 1 million factoid QA pairs from 12,000 National Transportation Safety Board (NTSB) reports using templates. These QA pairs contain questions such that answers to them are entities occurring in the AviationKG (Agarwal et al., 2022). AviationQA will be helpful to researchers in finding insights into aircraft accidents and their prevention.

Examples from dataset:

    What was the Aircraft Damage of the accident no. ERA22LA162? Answer: Substantial

    Where was the Destination of the accident no. ERA22LA162?, Answer: Naples, GA (APH)