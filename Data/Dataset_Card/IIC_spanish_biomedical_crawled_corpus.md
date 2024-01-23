---
annotations_creators:
- no-annotation
language_creators:
- crowdsourced
language:
- es
multilinguality:
- monolingual
pretty_name: Spanish_Biomedical_Crawled_Corpus
size_categories:
- 1M<n<10M
source_datasets:
- IIC/spanish_biomedical_crawled_corpus
task_categories:
- sequence-modeling
task_ids:
- language-modeling
---
# Spanish_Biomedical_Crawled_Corpus
This is a dataset retrieved directly from [this link](https://zenodo.org/record/5510033#.Ykho3-hByUk), which was originally developed by [BSC](https://temu.bsc.es/). This is a direct copy-paste of the usage, limitations and license of the original dataset:


```
Description

The largest Spanish biomedical and heath corpus to date gathered from a massive Spanish health domain crawler over more than 3,000 URLs were downloaded and preprocessed. The collected data have been preprocessed to produce the CoWeSe (Corpus Web Salud Español) resource, a large-scale and high-quality corpus intended for biomedical and health NLP in Spanish.

Directory structure

CoWeSe.txt: the CoWeSe corpus; an empty line separates each document

License

The corpus is released under this licensing scheme:

- We do not own any of the text from which these data has been extracted and preprocessed to be ready for use for language modeling tasks.

- We license the actual packaging of these data under a CC0 1.0 Universal License

Notice and take down policy

Notice: Should you consider that our data contains material that is owned by you and should therefore not be reproduced here, please:

Clearly identify yourself, with detailed contact data such as an address, telephone number or email address at which you can be contacted.

Clearly identify the copyrighted work claimed to be infringed.

Clearly identify the material that is claimed to be infringing and information reasonably sufficient to allow us to locate

 

Copyright (c) 2021 Text Mining Unit at BSC
```

License, distribution and usage conditions of the original dataset apply.


### Contributions
Thanks to [@avacaondata](https://huggingface.co/avacaondata), [@alborotis](https://huggingface.co/alborotis), [@albarji](https://huggingface.co/albarji), [@Dabs](https://huggingface.co/Dabs), [@GuillemGSubies](https://huggingface.co/GuillemGSubies) for adding this dataset.

### Citation
```
@misc{carrino2021spanish,
      title={Spanish Biomedical Crawled Corpus: A Large, Diverse Dataset for Spanish Biomedical Language Models}, 
      author={Casimiro Pio Carrino and Jordi Armengol-Estapé and Ona de Gibert Bonet and Asier Gutiérrez-Fandiño and Aitor Gonzalez-Agirre and Martin Krallinger and Marta Villegas},
      year={2021},
      eprint={2109.07765},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

[Go to the official paper from the dataset for more information](https://arxiv.org/abs/2109.07765).
