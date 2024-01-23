---
license: cc
language:
- vi
- en
task_categories:
- text-generation
- fill-mask
task_ids:
- language-modeling
- masked-language-modeling
paperswithcode_id: pubmed
dataset_info:
  features:
  - name: en
    dtype: string
  - name: vi
    dtype: string
  splits:
  - name: pubmed22
    num_bytes: 44360028980
    num_examples: 20087006
  download_size: 23041004247
  dataset_size: 44360028980
---

# Dataset Summary
20M Vietnamese PubMed biomedical abstracts translated by the [state-of-the-art English-Vietnamese Translation project](https://arxiv.org/abs/2210.05610). The data has been used as unlabeled dataset for [pretraining a Vietnamese Biomedical-domain Transformer model](https://arxiv.org/abs/2210.05598).

![image](https://user-images.githubusercontent.com/44376091/200204462-4d559113-5bdf-4cc5-9e88-70abe82babba.png)

image source: [Enriching Biomedical Knowledge for Vietnamese Low-resource Language Through Large-Scale Translation](https://arxiv.org/abs/2210.05598)


# Language
- English: Original biomedical abstracts from [Pubmed](https://www.nlm.nih.gov/databases/download/pubmed_medline_faq.html)
- Vietnamese: Synthetic abstract translated by a [state-of-the-art English-Vietnamese Translation project](https://arxiv.org/abs/2210.05610)

# Dataset Structure
- The English sequences are 
- The Vietnamese sequences are 


# Source Data - Initial Data Collection and Normalization
https://www.nlm.nih.gov/databases/download/pubmed_medline_faq.html

# Licensing Information
[Courtesy of the U.S. National Library of Medicine.](https://www.nlm.nih.gov/databases/download/terms_and_conditions.html)

# Citation
```
@misc{mtet,
  doi = {10.48550/ARXIV.2210.05610},
  url = {https://arxiv.org/abs/2210.05610},
  author = {Ngo, Chinh and Trinh, Trieu H. and Phan, Long and Tran, Hieu and Dang, Tai and Nguyen, Hieu and Nguyen, Minh and Luong, Minh-Thang},
  keywords = {Computation and Language (cs.CL), Artificial Intelligence (cs.AI), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {MTet: Multi-domain Translation for English and Vietnamese},
  publisher = {arXiv},
  year = {2022},
  copyright = {Creative Commons Attribution 4.0 International}
}
```

```
@misc{vipubmed,
  doi = {10.48550/ARXIV.2210.05598},
  url = {https://arxiv.org/abs/2210.05598},
  author = {Phan, Long and Dang, Tai and Tran, Hieu and Phan, Vy and Chau, Lam D. and Trinh, Trieu H.},
  keywords = {Computation and Language (cs.CL), Artificial Intelligence (cs.AI), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {Enriching Biomedical Knowledge for Vietnamese Low-resource Language Through Large-Scale Translation},
  publisher = {arXiv},
  year = {2022},
  copyright = {Creative Commons Attribution 4.0 International}
}
```