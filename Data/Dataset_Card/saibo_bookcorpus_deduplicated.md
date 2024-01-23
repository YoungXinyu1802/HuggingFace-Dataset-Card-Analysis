---
dataset_info:
  features:
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2867856394
    num_examples: 38832894
  download_size: 1794567875
  dataset_size: 2867856394
---
# Dataset Card for "bookcorpus_deduplicated"

## Dataset Summary
This is a deduplicated version of the original [Book Corpus dataset](https://huggingface.co/datasets/bookcorpus).
The Book Corpus (Zhu et al., 2015), which was used to train popular models such as BERT, has a substantial amount of exact-duplicate documents according to [Bandy and Vincent (2021)](https://arxiv.org/abs/2105.05241)
[Bandy and Vincent (2021)](https://arxiv.org/abs/2105.05241) find that thousands of books in BookCorpus are duplicated, with only 7,185 unique books out of 11,038 total.

Effect of deduplication
- Num of lines: 38832894 VS 74004228 
- Dataset size: 2.91GB VS 4.63GB

The duplicate text has been droped and only the first appearance is kept. 
The order of text appearance is kept.

## Why deduplicate?
Deduplication of training data has showed various advantages, including:
- require fewer training steps to achieve the same or better accuracy
- train models that emit memorized text ten times less frequently
- reduce carbon emission and energy consumption

cf [Deduplicating Training Data Makes Language Models Better](https://arxiv.org/abs/2107.06499)


## Deduplication script
```python
import pandas as pd
from datasets import load_dataset

dataset = load_dataset("bookcorpus")["train"]["text"]
df = pd.Dataframe({"text":dataset})

# drop duplicates(exact match)
df_filtered = df["text"].drop_duplicates()

df_filtered.to_csv("bookcorpus_filtered.csv","index"=False,"header"=False)
new_dataset = load_dataset("text",data_files={"train":"bookcorpus_filtered.csv"})
```
The running time is short, less than several minutes.
More sophicated deduplication algorithms can be applied to improve the performance, such as https://github.com/google-research/deduplicate-text-datasets

## Reference
```bib
@misc{https://doi.org/10.48550/arxiv.2105.05241,
  doi = {10.48550/ARXIV.2105.05241},
  url = {https://arxiv.org/abs/2105.05241},
  author = {Bandy, Jack and Vincent, Nicholas},
  keywords = {Computation and Language (cs.CL), Computers and Society (cs.CY), Machine Learning (cs.LG), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {Addressing "Documentation Debt" in Machine Learning Research: A Retrospective Datasheet for BookCorpus},
  publisher = {arXiv},
  year = {2021},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```

```bib
@misc{https://doi.org/10.48550/arxiv.2107.06499,
  doi = {10.48550/ARXIV.2107.06499},
  url = {https://arxiv.org/abs/2107.06499},
  author = {Lee, Katherine and Ippolito, Daphne and Nystrom, Andrew and Zhang, Chiyuan and Eck, Douglas and Callison-Burch, Chris and Carlini, Nicholas},
  keywords = {Computation and Language (cs.CL), Machine Learning (cs.LG), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {Deduplicating Training Data Makes Language Models Better},
  publisher = {arXiv},
  year = {2021},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```

```bib
@misc{https://doi.org/10.48550/arxiv.2209.00099,
  doi = {10.48550/ARXIV.2209.00099},
  url = {https://arxiv.org/abs/2209.00099},
  author = {Treviso, Marcos and Ji, Tianchu and Lee, Ji-Ung and van Aken, Betty and Cao, Qingqing and Ciosici, Manuel R. and Hassid, Michael and Heafield, Kenneth and Hooker, Sara and Martins, Pedro H. and Martins, André F. T. and Milder, Peter and Raffel, Colin and Simpson, Edwin and Slonim, Noam and Balasubramanian, Niranjan and Derczynski, Leon and Schwartz, Roy},
  keywords = {Computation and Language (cs.CL), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {Efficient Methods for Natural Language Processing: A Survey},
  publisher = {arXiv},
  year = {2022},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```

[More Information needed](https://github.com/huggingface/datasets/blob/main/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)