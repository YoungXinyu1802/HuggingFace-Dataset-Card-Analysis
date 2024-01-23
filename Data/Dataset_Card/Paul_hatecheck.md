---
annotations_creators:
- crowdsourced
language_creators:
- expert-generated
language:
- en
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: HateCheck
size_categories:
- 1K<n<10K
source_datasets:
- original
task_categories:
- text-classification
task_ids:
- hate-speech-detection
---

# Dataset Card for HateCheck

## Dataset Description

HateCheck is a suite of functional test for hate speech detection models. 
The dataset contains 3,728 validated test cases in 29 functional tests.
19 functional tests correspond to distinct types of hate. The other 11 functional tests cover challenging types of non-hate.
This allows for targeted diagnostic insights into model performance.

In our ACL paper, we found critical weaknesses in all commercial and academic hate speech detection model that we tested with HateCheck. 
Please refer to the paper (linked below) for results and further discussion, as well as further information on the dataset and a full data statement.

- **Paper:** Röttger et al. (2021) - HateCheck: Functional Tests for Hate Speech Detection Model. https://aclanthology.org/2021.acl-long.4/ or https://arxiv.org/abs/2012.15606
- **Repository:** https://github.com/paul-rottger/hatecheck-data
- **Point of Contact:** paul.rottger@oii.ox.ac.uk


## Dataset Structure

"test.csv" contains all 3,728 validated test cases. Each test case (row) has the following attributes:

**functionality**
The shorthand for the functionality tested by the test case.

**case_id**
The unique ID of the test case (assigned to each of the 3,901 cases we initially generated)

**test_case**
The text of the test case.

**label_gold**
The gold standard label (hateful/non-hateful) of the test case. All test cases within a given functionality have the same gold standard label.

**target_ident**
Where applicable, the protected group targeted or referenced by the test case. We cover seven protected groups in the test suite: women, trans people, gay people, black people, disabled people, Muslims and immigrants.

**direction**
For hateful cases, the binary secondary label indicating whether they are *directed* at an individual as part of a protected group or aimed at the group in *general*.

**focus_words**
Where applicable, the key word or phrase in a given test case (e.g. "cut their throats").

**focus_lemma**
Where applicable, the corresponding lemma (e.g. "cut sb. throat").

**ref_case_id**
For hateful cases, where applicable, the ID of the simpler hateful case which was perturbed to generate them.
For non-hateful cases, where applicable, the ID of the hateful case which is contrasted.

**ref_templ_id**
The equivalent, but for template IDs.

**templ_id**
The unique ID of the template from which the test case was generated (assigned to each of the 866 cases and templates from which we generated the 3,901 initial cases).


## Citation Information

When using HateCheck, please cite our ACL paper:

@inproceedings{rottger-etal-2021-hatecheck,
    title = "{H}ate{C}heck: Functional Tests for Hate Speech Detection Models",
    author = {R{\"o}ttger, Paul  and
      Vidgen, Bertie  and
      Nguyen, Dong  and
      Waseem, Zeerak  and
      Margetts, Helen  and
      Pierrehumbert, Janet},
    booktitle = "Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)",
    month = aug,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.acl-long.4",
    doi = "10.18653/v1/2021.acl-long.4",
    pages = "41--58",
    abstract = "Detecting online hate is a difficult task that even state-of-the-art models struggle with. Typically, hate speech detection models are evaluated by measuring their performance on held-out test data using metrics such as accuracy and F1 score. However, this approach makes it difficult to identify specific model weak points. It also risks overestimating generalisable model performance due to increasingly well-evidenced systematic gaps and biases in hate speech datasets. To enable more targeted diagnostic insights, we introduce HateCheck, a suite of functional tests for hate speech detection models. We specify 29 model functionalities motivated by a review of previous research and a series of interviews with civil society stakeholders. We craft test cases for each functionality and validate their quality through a structured annotation process. To illustrate HateCheck{'}s utility, we test near-state-of-the-art transformer models as well as two popular commercial models, revealing critical model weaknesses.",
}



