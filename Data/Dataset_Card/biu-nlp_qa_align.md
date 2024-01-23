# QA-Align

This dataset contains QA-Alignments --- fine-grained annotations of cross-text content overlap. 
The task input is two sentences from two documents, roughly talking about the same event, along with their QA-SRL annotations 
which capture verbal predicate-argument relations in question-answer format. The output is a cross-sentence alignment between sets of QAs which denote the same information.   

See the paper for details: [QA-Align: Representing Cross-Text Content Overlap by Aligning Question-Answer Propositions, Brook Weiss et. al., EMNLP 2021](https://aclanthology.org/2021.emnlp-main.778/).

The script downloads the data from the original [GitHub repository](https://github.com/DanielaBWeiss/QA-ALIGN). 

### Format

The dataset contains the following important features:
 
* `abs_sent_id_1`, `abs_sent_id_2` - unique sentence ids, unique across all data sources. 
* `text_1`, `text_2`, `prev_text_1`, `prev_text_2` - the two candidate sentences for alignments. The "prev" (previous) sentences are for context (shown to workers and for the model). 
* `qas_1`, `qas_2` - the sets of QASRL QAs for each sentence. For test and dev they were created by workers, while in train, the QASRL parser generated them. 
* `alignments` - the aligned QAs that workers have matched. This is the list of qa-alignments, where a single alignment looks like this:

```json
{'sent1': [{'qa_uuid': '33_1ecbplus~!~8~!~195~!~12~!~charged~!~4082',
    'verb': 'charged',
    'verb_idx': 12,
    'question': 'Who was charged?',
    'answer': 'the two youths',
    'answer_range': '9:11'}],
  'sent2': [{'qa_uuid': '33_8ecbplus~!~3~!~328~!~11~!~accused~!~4876',
    'verb': 'accused',
    'verb_idx': 11,
    'question': 'Who was accused of something?',
    'answer': 'two men',
    'answer_range': '9:10'}]}
```
Where the for each sentence, we save a list of the aligned QAs from that sentence. 

Note that this single alignment may contain multiple QAs for each sentence. While 96% of the data are one-to-one alignments, 4% contain many-to-many alignment (although most of the time it's a 2-to-1).

