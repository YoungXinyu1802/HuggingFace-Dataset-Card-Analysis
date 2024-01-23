# Dataset Card for mlquestions

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
- [Additional Information](#additional-information)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)

## Dataset Description

- **Homepage:** https://github.com/McGill-NLP/MLQuestions
- **Repository:** https://github.com/McGill-NLP/MLQuestions
- **Paper:** https://aclanthology.org/2021.emnlp-main.566.pdf
- **Leaderboard:** [Needs More Information]
- **Point of Contact:** [Devang Kulshreshtha](mailto:devang.kulshreshtha@mila.quebec)

### Dataset Summary

The MLQuestions dataset consists of questions from Google search queries and passages from Wikipedia pages related to Machine learning domain . The dataset was created to support research in domain adaptation of question generation and passage retrieval models. 

### Languages

The text in the dataset is in English

## Dataset Structure

### Data Instances

We release development and test sets where a typical data point comprises a passage denoted by `input_text` label and a question, with a `target_text` label. 

An example from the MLQuestions test set looks as follows:

{
    'input_text': 'Bayesian learning uses Bayes' theorem to determine the conditional probability of a hypotheses given some evidence or observations.'
    'target_text': 'What is Bayesian learning in machine learning'
}

We also provide unsupervised questions and passages in two separate files - 'passages_unaligned.csv' and 'questions_unaligned.csv' with labels `input_text` and `target_text` respectively.

## Additional Information

### Licensing Information

https://github.com/McGill-NLP/MLQuestions/blob/main/LICENSE.md

### Citation Information

If you find this useful in your research, please consider citing:

    @inproceedings{kulshreshtha-etal-2021-back,
        title = "Back-Training excels Self-Training at Unsupervised Domain Adaptation of Question Generation and Passage Retrieval",
        author = "Kulshreshtha, Devang  and
          Belfer, Robert  and
          Serban, Iulian Vlad  and
          Reddy, Siva",
        booktitle = "Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing",
        month = nov,
        year = "2021",
        address = "Online and Punta Cana, Dominican Republic",
        publisher = "Association for Computational Linguistics",
        url = "https://aclanthology.org/2021.emnlp-main.566",
        pages = "7064--7078",
        abstract = "In this work, we introduce back-training, an alternative to self-training for unsupervised domain adaptation (UDA). While self-training generates synthetic training data where natural inputs are aligned with noisy outputs, back-training results in natural outputs aligned with noisy inputs. This significantly reduces the gap between target domain and synthetic data distribution, and reduces model overfitting to source domain. We run UDA experiments on question generation and passage retrieval from the Natural Questions domain to machine learning and biomedical domains. We find that back-training vastly outperforms self-training by a mean improvement of 7.8 BLEU-4 points on generation, and 17.6{\%} top-20 retrieval accuracy across both domains. We further propose consistency filters to remove low-quality synthetic data before training. We also release a new domain-adaptation dataset - MLQuestions containing 35K unaligned questions, 50K unaligned passages, and 3K aligned question-passage pairs.",
    }