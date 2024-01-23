---
annotations_creators:
- crowdsourced
language_creators:
- crowdsourced
language:
- ro-RO
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: 'RoITD: Romanian IT Question Answering Dataset'
size_categories:
- unknown
source_datasets:
- original
task_categories:
- question-answering
task_ids:
- extractive-qa
---

## Dataset Summary 

 We introduce a  Romanian IT Dataset (RoITD) resembling SQuAD 1.1.  RoITD consists of 9575 Romanian  QA pairs formulated by crowd workers. QA pairs are based on 5043 articles from Romanian Wikipedia articles describing IT and household products.  Of the total number of questions, 5103 are possible (i.e. the correct answer can be found within the paragraph) and 4472 are not possible (i.e. the given answer is a "plausible answer" and not correct)

## Dataset Structure 


The data structure follows the format of SQuAD, which contains several attributes such as **question**, **id**, **text**, `**answer_start**, **is_impossible** and **context**. The paragraph provided to crowd sourcing workers is stored in the field **context**. This incorporates manually-selected paragraphs from Wikipedia. The field **id** is comprised of a randomly assigned unique identification number for the answer-question pair. Only the numbers "0" and "1" are allowed in the **is_impossible** field. The category "A" is assigned the value "0", indicating that the answer is correct. The value "1" corresponds to the category "U", indicating a plausible answer. The question posed by the source crowd source worker is represented by the field **question**. The field **answer_start** keeps track of the character index marking the beginning of an answer.


