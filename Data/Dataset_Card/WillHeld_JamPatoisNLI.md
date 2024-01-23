---
dataset_info:
  features:
  - name: Number
    dtype: int64
  - name: premise
    dtype: string
  - name: hypothesis
    dtype: string
  - name: label
    dtype:
      class_label:
        names:
          '0': entailment
          '1': neutral
          '2': contradiction
  splits:
  - name: train
    num_bytes: 32336
    num_examples: 250
  - name: val
    num_bytes: 27515
    num_examples: 200
  - name: test
    num_bytes: 27342
    num_examples: 200
  download_size: 67207
  dataset_size: 87193
---

This  data comes from "JamPatoisNLI: A Jamaican Patois Natural Language Inference Dataset" by Ruth-Ann Armstrong, John Hewitt, Christopher Manning. Please cite the original work if you make use of this data:                                                                                                                                                                                  
                                                                                                                                                                                                                   
```                                                                                                                                                                                                                
@article{DBLP:journals/corr/abs-2212-03419,
  author    = {Ruth{-}Ann Armstrong and
               John Hewitt and
               Christopher D. Manning},
  title     = {JamPatoisNLI: {A} Jamaican Patois Natural Language Inference Dataset},
  journal   = {CoRR},
  volume    = {abs/2212.03419},
  year      = {2022},
  url       = {https://doi.org/10.48550/arXiv.2212.03419},
  doi       = {10.48550/arXiv.2212.03419},
  eprinttype = {arXiv},
  eprint    = {2212.03419},
  timestamp = {Mon, 02 Jan 2023 15:09:55 +0100},
  biburl    = {https://dblp.org/rec/journals/corr/abs-2212-03419.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}                                                                                                                                                                                                                 
```  