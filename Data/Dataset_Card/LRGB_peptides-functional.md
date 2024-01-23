---
task_categories:
- graph-ml
size_categories:
- 1M<n<10M
tags:
- lrgb
license: cc-by-nc-4.0
---

# `peptides-functional`

### Dataset Summary

|  Dataset | Domain  |  Task | Node Feat. (dim)  | Edge Feat. (dim) | Perf. Metric | 
|---|---|---|---|---|---|
| Peptides-func | Chemistry | Graph Classification | Atom Encoder (9) | Bond Encoder (3) | AP

|  Dataset | # Graphs  |  # Nodes | μ Nodes  | μ Deg. | # Edges | μ Edges | μ Short. Path | μ Diameter 
|---|---:|---:|---:|:---:|---:|---:|---:|---:|
| Peptides-func | 15,535 | 2,344,859 | 150.94 | 2.04 | 4,773,974 | 307.30 | 20.89±9.79 | 56.99±28.72 |

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