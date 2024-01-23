---
license: mit
dataset_info:
  features:
  - name: image
    dtype: image
  - name: ocr
    list:
    - name: box
      sequence:
        sequence: float64
    - name: label
      dtype: string
    - name: text
      dtype: string
  splits:
  - name: train
    num_bytes: 267317016.0
    num_examples: 652
  download_size: 217146103
  dataset_size: 267317016.0
---
# Dataset Card for "sroie_document_understanding"

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
- [Dataset Structure](#dataset-structure)
  - [Data Fields](#data-fields)
- [Dataset Creation](#dataset-creation)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
- [Additional Information](#additional-information)
  - [Licensing Information](#licensing-information)
  - [Contributions](#contributions)

## Dataset Description

This dataset is an enriched version of SROIE 2019 dataset with additional labels for line descriptions and line totals for OCR and layout understanding.

## Dataset Structure

```python
DatasetDict({
    train: Dataset({
        features: ['image', 'ocr'],
        num_rows: 652
    })
})
```

### Data Fields

```python
{
    'image': PIL Image object,
    'ocr': [
        #  text box 1
        {
            'box': [[float, float], [float, float], [float, float], [float, float]],
			'label': str,  # "other" | "company" | "address" | "date" | "line_description" | "line_total" | "total"
			'text': str
        },
            ...
        #  text box N
		{
            'box': [[float, float], [float, float], [float, float], [float, float]],
			'label': str,
			'text': str,
        }
    ]
}
```

## Dataset Creation

### Source Data

The dataset was obtained from [ICDAR2019 Competition on Scanned Receipt OCR and Information Extraction](https://rrc.cvc.uab.es/?ch=13)

### Annotations

#### Annotation process

Additional labels to receipt line items were added using open source [labelme](https://github.com/wkentaro/labelme) tool.

#### Who are the annotators?

Arvind Rajan (adding labels to the original text boxes from source)

## Additional Information

### Licensing Information

MIT License 

### Contributions

Thanks to [@arvindrajan92](https://github.com/arvindrajan92) for adding this dataset.