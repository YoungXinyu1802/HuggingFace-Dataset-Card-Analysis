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


# Digital Peter

The Peter dataset can be used for reading texts from the manuscripts written by Peter the Great. The dataset annotation contain end-to-end markup for training detection and OCR models, as well as an end-to-end model for reading text from pages.

Paper is available at http://arxiv.org/abs/2103.09354 

## Description

Digital Peter is an educational task with a historical slant created on the basis of several AI technologies (Computer Vision, NLP, and knowledge graphs). The task was prepared jointly with the Saint Petersburg Institute of History (N.P.Lihachov mansion) of Russian Academy of Sciences, Federal Archival Agency of Russia and Russian State Archive of Ancient Acts.

A detailed description of the problem (with an immersion in the problem) can be found in [detailed_description_of_the_task_en.pdf](https://github.com/sberbank-ai/digital_peter_aij2020/blob/master/desc/detailed_description_of_the_task_en.pdf)

The dataset consists of 662 full page images and 9696 annotated text files. There are 265788 symbols and approximately 50998 words.

## Annotation format

The annotation is in COCO format. The `annotation.json` should have the following dictionaries:

- `annotation["categories"]` - a list of dicts with a categories info (categotiy names and indexes).
- `annotation["images"]` - a list of dictionaries with a description of images, each dictionary must contain fields:
   - `file_name` - name of the image file.
   - `id` for image id.
- `annotation["annotations"]` - a list of dictioraties with a murkup information. Each dictionary stores a description for one polygon from the dataset, and must contain the following fields:
   - `image_id` - the index of the image on which the polygon is located.
   - `category_id` - the polygon’s category index.
   - ```attributes``` - dict with some additional annotatioin information. In the `translation` subdict you can find text translation for the line.
   - `segmentation` - the coordinates of the polygon, a list of numbers - which are coordinate pairs x and y.

## Competition

We held a competition based on Digital Peter dataset.
Here is github [link](https://github.com/sberbank-ai/digital_peter_aij2020). Here is competition [page](https://ods.ai/tracks/aij2020) (need to register).