---
annotations_creators:
- crowdsourced
language_creators:
- expert-generated
language:
- fr
license:
- cc-by-4.0
multilinguality:
- monolingual
pretty_name: French HateCheck
size_categories:
- 1K<n<10K
source_datasets:
- original
task_categories:
- text-classification
task_ids:
- hate-speech-detection
---
# Dataset Card for Multilingual HateCheck
## Dataset Description

Multilingual HateCheck (MHC) is a suite of functional tests for hate speech detection models in 10 different languages: Arabic, Dutch, French, German, Hindi, Italian, Mandarin, Polish, Portuguese and Spanish.
For each language, there are 25+ functional tests that correspond to distinct types of hate and challenging non-hate.
This allows for targeted diagnostic insights into model performance.

For more details, please refer to our paper about MHC, published at the 2022 Workshop on Online Abuse and Harms (WOAH) at NAACL 2022. If you are using MHC, please cite our work!
- **Paper:** Röttger et al. (2022) - Multilingual HateCheck: Functional Tests for Multilingual Hate Speech Detection Models. https://arxiv.org/abs/2206.09917
- **Repository:** https://github.com/rewire-online/multilingual-hatecheck
- **Point of Contact:** paul@rewire.online

## Dataset Structure

The csv format mostly matches the original HateCheck data, with some adjustments for specific languages.

**mhc_case_id**
The test case ID that is unique to each test case across languages (e.g., "mandarin-1305")

**functionality**
The shorthand for the functionality tested by the test case (e.g, "target_obj_nh"). The same functionalities are tested in all languages, except for Mandarin and Arabic, where non-Latin script required adapting the tests for spelling variations.

**test_case**
The test case text.

**label_gold**
The gold standard label ("hateful" or "non-hateful") of the test case. All test cases within a given functionality have the same gold standard label.

**target_ident**
Where applicable, the protected group that is targeted or referenced in the test case. All HateChecks cover seven target groups, but their composition varies across languages.

**ref_case_id**
For hateful cases, where applicable, the ID of the hateful case which was perturbed to generate this test case. For non-hateful cases, where applicable, the ID of the hateful case which is contrasted by this test case.

**ref_templ_id**
The equivalent to ref_case_id, but for template IDs.

**templ_id**
The ID of the template from which the test case was generated.

**case_templ**
The template from which the test case was generated (where applicable).

**gender_male** and **gender_female**
For gender-inflected languages (French, Spanish, Portuguese, Hindi, Arabic, Italian, Polish, German), only for cases where gender inflection is relevant, separate entries for gender_male and gender_female replace case_templ.

**label_annotated**
A list of labels given by the three annotators who reviewed the test case (e.g., "['hateful', 'hateful', 'hateful']").

**label_annotated_maj**
The majority vote of the three annotators (e.g., "hateful"). In some cases this differs from the gold label given by our language experts.

**disagreement_in_case**
True if label_annotated_maj does not match label_gold for the entry.

**disagreement_in_template**
True if the test case is generated from an IDENT template and there is at least one case with disagreement_in_case generated from the same template. This can be used to exclude entire templates from MHC.