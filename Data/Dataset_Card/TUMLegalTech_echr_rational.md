---
license: afl-3.0

annotations_creators:
- expert-generated
language:
- en
language_creators:
- expert-generated
multilinguality:
- monolingual
size_categories:
- 50
---

# Dataset Card for echr_rational

### Dataset Summary
[Deconfounding Legal Judgment Prediction for European Court of Human
Rights Cases Towards Better Alignment with Experts](https://arxiv.org/pdf/2210.13836.pdf)

This work demonstrates that Legal Judgement Prediction systems without expert-informed adjustments can be vulnerable to shallow, distracting surface signals that arise from corpus construction, case distribution, and confounding factors. To mitigate this, we use domain expertise to strategically identify statistically predictive but legally irrelevant information. We adopt adversarial training to prevent the system from relying on it. We evaluate our deconfounded models by employing interpretability techniques and comparing to expert annotations. Quantitative experiments and qualitative analysis show that our deconfounded model consistently aligns better with expert rationales than baselines trained for prediction only. We further contribute a set of reference expert annotations to the validation and testing partitions of an existing benchmark dataset of European Court of Human Rights cases

### Languages
English



# Citation Information

    @article{santosh2022deconfounding,
      title={Deconfounding Legal Judgment Prediction for European Court of Human Rights Cases Towards Better Alignment with Experts},
      author={Santosh, TYS and Xu, Shanshan and Ichim, Oana and Grabmair, Matthias},
      journal={arXiv preprint arXiv:2210.13836},
      year={2022}
    }

