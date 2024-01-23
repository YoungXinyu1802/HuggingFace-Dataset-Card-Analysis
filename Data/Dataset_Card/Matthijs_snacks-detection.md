---
pretty_name: Snacks (Detection)
task_categories:
- object-detection
- computer-vision
license: cc-by-4.0
---

# Dataset Card for Snacks (Detection)

## Dataset Summary

This is a dataset of 20 different types of snack foods that accompanies the book [Machine Learning by Tutorials](https://www.raywenderlich.com/books/machine-learning-by-tutorials/v2.0).

The images were taken from the [Google Open Images dataset](https://storage.googleapis.com/openimages/web/index.html), release 2017_11. 

## Dataset Structure

Included in the **data** folder are three CSV files with bounding box annotations for the images in the dataset, although not all images have annotations and some images have multiple annotations. 

The columns in the CSV files are: 

- `image_id`: the filename of the image without the .jpg extension
- `x_min, x_max, y_min, y_max`: normalized bounding box coordinates, i.e. in the range [0, 1]
- `class_name`: the class that belongs to the bounding box
- `folder`: the class that belongs to the image as a whole, which is also the name of the folder that contains the image

The class names are:

```nohighlight
apple
banana
cake
candy
carrot
cookie
doughnut
grape
hot dog
ice cream
juice
muffin
orange
pineapple
popcorn
pretzel
salad
strawberry
waffle
watermelon
```

**Note:** The image files are not part of this repo but [can be found here](https://huggingface.co/datasets/Matthijs/snacks).

### Data Splits

Train, Test, Validation

## Licensing Information

Just like the images from Google Open Images, the snacks dataset is licensed under the terms of the Creative Commons license. 

The images are listed as having a [CC BY 2.0](https://creativecommons.org/licenses/by/2.0/) license. 

The annotations are licensed by Google Inc. under a [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) license. 
