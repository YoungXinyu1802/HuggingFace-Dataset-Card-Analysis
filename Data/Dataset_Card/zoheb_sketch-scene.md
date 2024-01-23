---
license: cc-by-nc-sa-4.0
language:
- en
language_creators:
- machine-generated
multilinguality:
- monolingual
pretty_name: 'Sketch Scene Descriptions'
size_categories:
- n<10K
source_datasets:
- FS-COCO
tags: []
task_categories:
- text-to-image
task_ids: []
---

# Dataset Card for Sketch Scene Descriptions

_Dataset used to train [Sketch Scene text to image model]()_

We advance sketch research to scenes with the first dataset of freehand scene sketches, FS-COCO. With practical applications in mind, we collect sketches that convey well scene content but can be sketched within a few minutes by a person with any sketching skills. Our dataset comprises around 10,000 freehand scene vector sketches with per-point space-time information by 100 non-expert individuals, offering both object- and scene-level abstraction. Each sketch is augmented with its text description.

For each row, the dataset contains `image` and `text` keys. `image` is a varying size PIL jpeg, and `text` is the accompanying text caption. Only a train split is provided.


## Citation

If you use this dataset, please cite it as:

```
@inproceedings{fscoco,
    title={FS-COCO: Towards Understanding of Freehand Sketches of Common Objects in Context.}
    author={Chowdhury, Pinaki Nath and Sain, Aneeshan and Bhunia, Ayan Kumar and Xiang, Tao and Gryaditskaya, Yulia and Song, Yi-Zhe},
    booktitle={ECCV},
    year={2022}
}
```