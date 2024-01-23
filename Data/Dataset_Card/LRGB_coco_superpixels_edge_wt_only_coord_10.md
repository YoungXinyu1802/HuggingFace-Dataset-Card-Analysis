---
task_categories:
- graph-ml
size_categories:
- 1M<n<10M
tags:
- lrgb
license: cc-by-4.0
---

# `coco_superpixels_edge_wt_only_coord_10`

### Dataset Summary

|  Dataset | Domain  |  Task | Node Feat. (dim)  | Edge Feat. (dim) | Perf. Metric | 
|---|---|---|---|---|---|
| COCO-SP	| Computer Vision | Node Prediction | Pixel + Coord (14) | Edge Weight (1 or 2) | macro F1 |

|  Dataset | # Graphs  |  # Nodes | μ Nodes  | μ Deg. | # Edges | μ Edges | μ Short. Path | μ Diameter 
|---|---:|---:|---:|:---:|---:|---:|---:|---:|
| COCO-SP | 123,286 | 58,793,216 | 476.88 | 5.65 | 332,091,902 | 2,693.67 | 10.66±0.55 | 27.39±2.14 |

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