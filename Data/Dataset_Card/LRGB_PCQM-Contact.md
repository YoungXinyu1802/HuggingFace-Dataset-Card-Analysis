---
task_categories:
- graph-ml
size_categories:
- 1M<n<10M
tags:
- lrgb
license: cc-by-4.0
---

# `peptides-functional`

### Dataset Summary

|  Dataset | Domain  |  Task | Node Feat. (dim)  | Edge Feat. (dim) | Perf. Metric | 
|---|---|---|---|---|---|
| PCQM-Contact | Quantum Chemistry | Link Prediction | Atom Encoder (9) | Bond Encoder (3) | Hits@K, MRR

|  Dataset | # Graphs  |  # Nodes | μ Nodes  | μ Deg. | # Edges | μ Edges | μ Short. Path | μ Diameter 
|---|---:|---:|---:|:---:|---:|---:|---:|---:|
| PCQM-Contact | 529,434 | 15,955,687 | 30.14 | 2.03 | 32,341,644 | 61.09 |4.63±0.63 | 9.86±1.79 |

## Additional Information

### Dataset Curators

* Vijay Prakash Dwivedi ([vijaydwivedi75](https://github.com/vijaydwivedi75))

### Citation Information

```
@article{dwivedi2022LRGB,
  title={Long Range Graph Benchmark}, 
  author={Dwivedi, Vijay Prakash and Rampášek, Ladislav and Galkin, Mikhail and Parviz, Ali and Wolf, Guy and Luu, Anh Tuan and Beaini, Dominique},
  journal={arXiv:2206.08164},
  year={2022}
}
```