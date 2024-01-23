---
license:
- bsd-3-clause
train-eval-index:
- config: kmfoda--booksum
  task: summarization
  task_id: summarization
  splits:
    eval_split: test
  col_mapping:
    chapter: text
    summary_text: target
---

# BOOKSUM: A Collection of Datasets for Long-form Narrative Summarization
Authors: [Wojciech Kryściński](https://twitter.com/iam_wkr), [Nazneen Rajani](https://twitter.com/nazneenrajani), [Divyansh Agarwal](https://twitter.com/jigsaw2212), [Caiming Xiong](https://twitter.com/caimingxiong), [Dragomir Radev](http://www.cs.yale.edu/homes/radev/)

## Introduction
The majority of available text summarization datasets include short-form source documents that lack long-range causal and temporal dependencies, and often contain strong layout and stylistic biases. 
While relevant, such datasets will offer limited challenges for future generations of text summarization systems.
We address these issues by introducing BookSum, a collection of datasets for long-form narrative summarization.
Our dataset covers source documents from the literature domain, such as novels, plays and stories, and includes highly abstractive, human written summaries on three levels of granularity of increasing difficulty: paragraph-, chapter-, and book-level.
The domain and structure of our dataset poses a unique set of challenges for summarization systems, which include: processing very long documents, non-trivial causal and temporal dependencies, and rich discourse structures.
To facilitate future work, we trained and evaluated multiple extractive and abstractive summarization models as baselines for our dataset.

## Links

- [paper](https://arxiv.org/abs/2105.08209) by SalesForce Research
- [GitHub repo](https://github.com/salesforce/booksum)

<p align="center"><img src="misc/book_sumv4.png"></p>
 
## Table of Contents

1. [Citation](#citation)
2. [Legal Note](#legal-note)
3. [License](#license)


## Citation
```
@article{kryscinski2021booksum,
      title={BookSum: A Collection of Datasets for Long-form Narrative Summarization}, 
      author={Wojciech Kry{\'s}ci{\'n}ski and Nazneen Rajani and Divyansh Agarwal and Caiming Xiong and Dragomir Radev},
      year={2021},
      eprint={2105.08209},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

## Legal Note
By downloading or using the resources, including any code or scripts, shared in this code
repository, you hereby agree to the following terms, and your use of the resources is conditioned
on and subject to these terms.
1. You may only use the scripts shared in this code repository for research purposes. You
may not use or allow others to use the scripts for any other purposes and other uses are
expressly prohibited.
2. You will comply with all terms and conditions, and are responsible for obtaining all
rights, related to the services you access and the data you collect.
3. We do not make any representations or warranties whatsoever regarding the sources from
which data is collected. Furthermore, we are not liable for any damage, loss or expense of
any kind arising from or relating to your use of the resources shared in this code
repository or the data collected, regardless of whether such liability is based in tort,
contract or otherwise.

## License
The code is released under the **BSD-3 License** (see `LICENSE.txt` for details).