---
dataset_info:
  features:
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence: int64
  - name: lang
    dtype: string
  splits:
  - name: train
    num_bytes: 319328641
    num_examples: 821600
  - name: validation
    num_bytes: 39434957
    num_examples: 102700
  - name: test
    num_bytes: 39371980
    num_examples: 103206
  download_size: 139847318
  dataset_size: 398135578
task_categories:
- token-classification
language:
- es
- en
- nl
- fr
- it
- ru
- pt
- pl
- de
pretty_name: Wikineural
tags:
- named-entity-recognition
- wikipedia
- machine-generation
---
# Dataset Card for "Babelscape-wikineural-joined"

This dataset is a merged version of [wikineural](https://huggingface.co/datasets/Babelscape/wikineural)

[More Information needed](https://github.com/huggingface/datasets/blob/main/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

<pre><code>
  @inproceedings{tedeschi-etal-2021-wikineural-combined,
    title = "{W}iki{NE}u{R}al: {C}ombined Neural and Knowledge-based Silver Data Creation for Multilingual {NER}",
    author = "Tedeschi, Simone  and
      Maiorca, Valentino  and
      Campolungo, Niccol{\`o}  and
      Cecconi, Francesco  and
      Navigli, Roberto",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2021",
    month = nov,
    year = "2021",
    address = "Punta Cana, Dominican Republic",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.findings-emnlp.215",
    pages = "2521--2533",
    abstract = "Multilingual Named Entity Recognition (NER) is a key intermediate task which is needed in many areas of NLP. In this paper, we address the well-known issue of data scarcity in NER, especially relevant when moving to a multilingual scenario, and go beyond current approaches to the creation of multilingual silver data for the task. We exploit the texts of Wikipedia and introduce a new methodology based on the effective combination of knowledge-based approaches and neural models, together with a novel domain adaptation technique, to produce high-quality training corpora for NER. We evaluate our datasets extensively on standard benchmarks for NER, yielding substantial improvements up to 6 span-based F1-score points over previous state-of-the-art systems for data creation.",
}

</code></pre>