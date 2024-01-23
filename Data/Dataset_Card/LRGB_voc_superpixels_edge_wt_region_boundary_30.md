---
task_categories:
- graph-ml
size_categories:
- 1M<n<10M
tags:
- lrgb
---

# `voc_superpixels_edge_wt_region_boundary_30`

### Dataset Summary

|  Dataset | Domain  |  Task | Node Feat. (dim)  | Edge Feat. (dim) | Perf. Metric | 
|---|---|---|---|---|---|
| PascalVOC-SP| Computer Vision | Node Prediction | Pixel + Coord (14) | Edge Weight (1 or 2) | macro F1 |

|  Dataset | # Graphs  |  # Nodes | μ Nodes  | μ Deg. | # Edges | μ Edges | μ Short. Path | μ Diameter 
|---|---:|---:|---:|:---:|---:|---:|---:|---:|
| PascalVOC-SP| 11,355 | 5,443,545 | 479.40 | 5.65 | 30,777,444 | 2,710.48 | 10.74±0.51 | 27.62±2.13 |

## Additional Information

### Dataset Curators

* Vijay Prakash Dwivedi ([vijaydwivedi75](https://github.com/vijaydwivedi75))

### Licensing Information

[Custom License](http://host.robots.ox.ac.uk/pascal/VOC/voc2011/index.html) for Pascal VOC 2011 (respecting Flickr terms of use)

### Citation Information

```
@article{dwivedi2022LRGB,
  title={Long Range Graph Benchmark}, 
  author={Dwivedi, Vijay Prakash and Rampášek, Ladislav and Galkin, Mikhail and Parviz, Ali and Wolf, Guy and Luu, Anh Tuan and Beaini, Dominique},
  journal={arXiv:2206.08164},
  year={2022}
}
```