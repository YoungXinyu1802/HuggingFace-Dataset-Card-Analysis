---
language:
- ru
license:
- mit
source_datasets:
- original
task_categories:
- image-segmentation
- object-detection
task_ids: []
tags:
- optical-character-recognition
- text-detection
- ocr
---


# School Notebooks Dataset

The images of school notebooks with handwritten notes in Russian.

The dataset annotation contain end-to-end markup for training detection and OCR models, as well as an end-to-end model for reading text from pages.

## Annotation format

The annotation is in COCO format. The `annotation.json` should have the following dictionaries:

- `annotation["categories"]` - a list of dicts with a categories info (categotiy names and indexes).
- `annotation["images"]` - a list of dictionaries with a description of images, each dictionary must contain fields:
   - `file_name` - name of the image file.
   - `id` for image id.
- `annotation["annotations"]` - a list of dictioraties with a murkup information. Each dictionary stores a description for one polygon from the dataset, and must contain the following fields:
   - `image_id` - the index of the image on which the polygon is located.
   - `category_id` - the polygon’s category index.
   - `attributes` - dict with some additional annotation information. In the `translation` subdict you can find text translation for the line.
   - `segmentation` - the coordinates of the polygon, a list of numbers - which are coordinate pairs x and y.