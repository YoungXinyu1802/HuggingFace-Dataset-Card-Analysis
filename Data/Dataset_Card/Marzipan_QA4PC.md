## QA4PC Dataset (paper: Cross-Policy Compliance Detection via Question Answering)


### Train Sets
To create training set or entailment and QA tasks, download the ShARC data from here: https://sharc-data.github.io/data.html. After that, run the script from _create_train_from_sharc.py_, by providing the path to the ShARC train and development sets.

### Evaluation Sets

#### Entailment Data
The following files contain the data for the entailment task. This includes the policy + questions, a scenario and an answer (_Yes, No, Maybe_). Each datapoint also contain the information from the ShARC dataset such as tree_id and source_url.
- __dev_entailment_qa4pc.json__
- __test_entailment_qa4pc.json__

#### QA Data
The following files contain the data for the QA task.
- __dev_sc_qa4pc.json__
- __test_sc_qa4pc.json__

The following file contains the expression tree data for the dev and test sets. Each tree includes a policy, a set of questions and a logical expression.
- __trees_dev_test_qa4pc.json__
