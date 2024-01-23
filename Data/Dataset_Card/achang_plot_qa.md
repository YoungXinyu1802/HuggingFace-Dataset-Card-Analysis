---
license: cc
task_categories:
- visual-question-answering
language:
- en
tags:
- plotQA
pretty_name: PlotQA
---

# Dataset Card for PlotQA

## Dataset Description

- **PlotQA from here:** [PlotQA](https://github.com/NiteshMethani/PlotQA)

### Dataset Summary

PlotQA is a VQA dataset with 28.9 million question-answer pairs grounded over 224,377 plots on data from real-world sources and questions based on crowd-sourced question templates.

## Dataset Structure

### Data Fields

List and describe the fields present in the dataset. Mention their data type, and whether they are used as input or output in any of the tasks the dataset currently supports. If the data has span indices, describe their attributes, such as whether they are at the character level or word level, whether they are contiguous or not, etc. If the datasets contains example IDs, state whether they have an inherent meaning, such as a mapping to other datasets or pointing to relationships between data points.

- `image`: PIL image of a plot
- `text`: string of json data 'models'. See notes below.

From [here](https://github.com/NiteshMethani/PlotQA/blob/master/PlotQA_Dataset.md):
'models': It is a list of dictionaries. Depending on the type of the plot (single or 2,3,4-multi), the length of the dictionary can vary from 1 to 4. Each dictionary contains the following keys-
		name: Label corresponding to the datapoint.
		color: Color corresponding to the `name` datapoint.
		bboxes: Bounding boxes corresponding to the `name` datapoints in the plot.
		label: label corresponding to the datapoint which will appear as the legend (same as the `name` field).
		x: x-value of the datapoints.
		y: y-value of the datapoints.


[json2token](https://github.com/clovaai/donut/blob/b317b4bbf1eecec7c62e7666f2097e1e90a6b441/donut/model.py#L495) function was used to convert json to string. 

The new tokens are already loaded in plotQA processor:
```
from transformers import DonutProcessor
processor = DonutProcessor.from_pretrained("[achang/donut-plotqa-trained](https://huggingface.co/achang/donut-plotqa-trained)")
```

### Data Splits

```
validation: Dataset({
    features: ['image', 'text'],
    num_rows: 33650
})
train: Dataset({
    features: ['image', 'text'],
    num_rows: 157070
})
test: Dataset({
    features: ['image', 'text'],
    num_rows: 33657
})
```



## Misc

Dataset Creation, Annotations, Considerations for Using the Data, Social Impact of Dataset, Additional Information, Licensing Information look at [plotQA](https://github.com/NiteshMethani/PlotQA)


### Citation Information

Please cite the following if you use the PlotQA dataset in your work:
```
@InProceedings{Methani_2020_WACV,
author = {Methani, Nitesh and Ganguly, Pritha and Khapra, Mitesh M. and Kumar, Pratyush},
title = {PlotQA: Reasoning over Scientific Plots},
booktitle = {The IEEE Winter Conference on Applications of Computer Vision (WACV)},
month = {March},
year = {2020}
} 
```


