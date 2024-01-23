---
license: apache-2.0
---

## advABSA

An adversarial aspect-based sentiment analysis (ABSA) benchmark, dubbed [*adv*ABSA](https://arxiv.org/pdf/2207.08099.pdf) for both aspect-based sentiment classification (SC) and opinion extraction (OE).

### *adv*ABSA (Adversarial ABSA Benchmark)

In response to the concerning robustness issue of ABSA, [Arts](https://aclanthology.org/2020.emnlp-main.292.pdf) is proposed, which contains datasets crafted only for adversarial evaluaiton on SC but not for OE. So we additionally craft datasets for adversarial evaluaiton on OE following their track. These gathered datasets form *adv*ABSA. That is, *adv*ABSA can be decomposed to two parts, where the first part is Arts-\[domain\]-SC reused from Arts and the second part is Arts-\[domain\]-OE newly produced by us.

### *std*ABSA (Standard ABSA Benchmark)

In addition, we also provide *std*ABSA containing datasets from SemEval14 for standard evaluation, namely Sem14-\[domain\]-SC and Sem14-\[domain\]-OE. So corresponding performance drops can be measured properly.

### Citation

If you find *adv*ABSA useful, please kindly star this repositary and cite our paper as follows:

```bibtex
@inproceedings{ma-etal-2022-aspect, 
    title = "Aspect-specific Context Modeling for Aspect-based Sentiment Analysis", 
    author = "Ma, Fang and Zhang, Chen and Zhang, Bo and Song, Dawei",
    booktitle = "NLPCC", 
    month = "sep", year = "2022", 
    address = "Guilin, China", 
    url = "https://arxiv.org/pdf/2207.08099.pdf",
}
```

### Credits

The benchmark is mainly processed by [Fang Ma](https://github.com/BD-MF).