---
annotations_creators:
- expert-generated
language_creators:
- expert-generated
- machine-generated
language:
- ru
license:
- afl-3.0
multilinguality:
- monolingual
pretty_name: 'The Pages of Early Soviet Performance (PESP) uses machine learning to
  generate multiple datasets of early-Soviet illustrated periodicals related to the
  performing arts. By using computer vision techniques and training a YOLO (You Only
  Look Once) real-time object detection model, we are producing textual and image
  data that will facilitate new avenues of research about Soviet culture during the
  first decades after the October Revolution (1917-1932).


  Our starting point is Princeton University Library''s Digital PUL (DPUL) where ten
  titles - totaling 526 issues and approximately 26,000 pages - of Soviet performance
  journals have been digitized and can be freely viewed online. Journals are a diverse
  and complex genre: taken together, this collection contains hundreds of thousands
  of articles, poems, editorial commentary, advertisements as well as images, illustrations
  and graphic art. Today, researchers can browse the journals and view and download
  high-quality page images on DPUL.'
size_categories: []
source_datasets:
- original
task_categories:
- other
task_ids: []
---

# Pages of Early Soviet Performance (PESP)

This dataset was created as part of the [Pages of Early Soviet Performance](https://cdh.princeton.edu/projects/pages-early-soviet-performance/) project at Princeton and provides text and image research data from a previously scanned [collection of illustrated periodicals](https://dpul.princeton.edu/slavic/catalog?f%5Breadonly_collections_ssim%5D%5B%5D=Russian+Illustrated+Periodicals) held by Princeton University's Slavic Collections. The project was a partnership with ITMO University in Saint Petersburg. Our work focused on document segmentation and the prediction of image, text, title, and mixedtext regions in the document images.  The mixedtext category refers to segments where the typeface and text layout are mixed with other visual elements such as graphics, photographs, and illustrations. This category identifies sections that present problems for OCR and also highlights the experimental use of text, images, and other elements in the documents.

For each of the ten journals of interest in Princeton's digital collections (DPUL), we started with the IIIF manifest URI.  With these manifests, we downloaded each of the 24,000 document images.  The URI for each of the images is included in the dataset and a full list is available in `IIIF_URIs.json`.

## Authors 
Natalia Ermolaev, Thomas Keenan, Katherine Reischl, Andrew Janco, Quinn Dombrowski, Antonina Puchkovskaia, Alexander Jacobson, Anastasiia Mamonova, Michael Galperin and Vladislav Tretyak

## Journal manifests
-  [Эрмитаж](https://figgy.princeton.edu/concern/scanned_resources/6b561fbb-ba28-4afb-91d2-d77b8728d7d9/manifest?manifest=https://figgy.princeton.edu/concern/scanned_resources/6b561fbb-ba28-4afb-91d2-d77b8728d7d9/manifest)
- [Вестник искусств](https://figgy.princeton.edu/concern/scanned_resources/ad256b35-9ad0-4f75-bf83-3bad1a7c6018/manifest?manifest=https://figgy.princeton.edu/concern/scanned_resources/ad256b35-9ad0-4f75-bf83-3bad1a7c6018/manifest)
- [Советский театр](https://figgy.princeton.edu/concern/scanned_resources/f33993bb-a041-40a1-b11f-f660da825583/manifest?manifest=https://figgy.princeton.edu/concern/scanned_resources/f33993bb-a041-40a1-b11f-f660da825583/manifest)
- [Рабис](https://figgy.princeton.edu/concern/scanned_resources/01f4236f-0a2f-473c-946f-d9bbec12f8ea/manifest?manifest=https://figgy.princeton.edu/concern/scanned_resources/01f4236f-0a2f-473c-946f-d9bbec12f8ea/manifest)
- [Даёшь](https://figgy.princeton.edu/concern/scanned_resources/e036a5da-97a8-4041-ad62-a57af44359e2/manifest?manifest=https://figgy.princeton.edu/concern/scanned_resources/e036a5da-97a8-4041-ad62-a57af44359e2/manifest)
- [Персимфанс](https://figgy.princeton.edu/concern/scanned_resources/af43d19a-3659-4dd0-a0fc-4c74ce521ad6/manifest?manifest=https://figgy.princeton.edu/concern/scanned_resources/af43d19a-3659-4dd0-a0fc-4c74ce521ad6/manifest)
- [Тридцать дней](https://figgy.princeton.edu/concern/scanned_resources/d2d488af-2980-4554-a9ef-aacbaf463ec8/manifest?manifest=https://figgy.princeton.edu/concern/scanned_resources/d2d488af-2980-4554-a9ef-aacbaf463ec8/manifest)
- [За пролетарское искусство](https://figgy.princeton.edu/concern/scanned_resources/38f89d57-8e64-4033-97d6-b925c407584a/manifest?manifest=https://figgy.princeton.edu/concern/scanned_resources/38f89d57-8e64-4033-97d6-b925c407584a/manifest)
- [Бригада художников](https://figgy.princeton.edu/concern/scanned_resources/66d00a87-5ea9-439a-a909-95d697401a2b/manifest?manifest=https://figgy.princeton.edu/concern/scanned_resources/66d00a87-5ea9-439a-a909-95d697401a2b/manifest)
- [Зрелища](https://figgy.princeton.edu/concern/scanned_resources/1af8b322-a0b1-46af-8541-5c3054af8098/manifest?manifest=https://figgy.princeton.edu/concern/scanned_resources/1af8b322-a0b1-46af-8541-5c3054af8098/manifest)


## Model 

Using [makesense.ai](https://www.makesense.ai/) and a custom active learning application called ["Mayakovsky"](https://github.com/CDH-ITMO-Periodicals-Project/mayakovsky) we generated training data for a [YOLOv5 model](https://docs.ultralytics.com/tutorials/train-custom-datasets/).  The model was fine-tuned on the new labels and predictions were generated for all images in the collection. 

## OCR 

Using the model's predictions for image, title, text and mixedtext segments, we cropped the image using the bounding boxes and ran OCR on each document segment using Tesseract, Google Vision, and ABBYY FineReader.  Given that the output of these various OCR engines can be difficult to compare, the document segments give a common denominator for comparison of OCR outputs.  Having three variations of the extracted text can be useful for experiments with OCR post-correction.

## Dataset 

The dataset contains an entry for each image with the following fields: 
- filename: the image name (ex. 'Советский театр_1932 No. 4_16') with journal name, year, issue, page.
- dpul: the URL for the image's journal in Digital Princeton University Library
- journal: the journal name
- year: the year of the journal issue
- issue: the issue for the image
- URI: the IIIF URI used to fetch the image from Princeton's IIIF server 
- yolo: the raw model prediction (ex '3 0.1655 0.501396 0.311'), in Yolo's normalized xywh format (object-class x y width height). The labels are 'image'=0, 'mixedtext'=1, 'title'=2, 'textblock'=3.
- yolo_predictions: a List with a dictionary for each of the model's predictions with fields for: 
  - label: the predicted label
  - x: the x-value location of the center point of the prediction 
  - y: the y-value location of the center point of  the prediction
  - w: the total width of the prediction's bounding box 
  - h: the total height of the prediction's bounding box
  - abbyy_text: the text extracted from the predicted document segment using ABBY FineReader. Note that due to costs, only about 800 images have this data
  - tesseract_text: the text extracted from the predicted document segment using Tesseract.
  - vision_text: the text extracted from the predicted document segment using Google Vision.
  - vision_labels: entities recognized by Google Vision in image blocks and separated by | (ex. Boating|Boat|Printmaking) 

# Useage 

```python
from datasets import load_dataset

dataset = load_dataset('ajanco/pesp')
for item in dataset['train']:
    for prediction in item['yolo_predictions']:
        print(prediction)
    
```