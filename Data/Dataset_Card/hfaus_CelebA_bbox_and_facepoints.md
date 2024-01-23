---
size_categories:
- n<1K
---
# CelebA Dataset

CelebA Dataset is a large-scale face attributes dataset with more than 200K celebrity images, each with 40 attribute annotations. The images in this dataset cover large pose variations and background clutter. CelebA has large diversities, large quantities, and rich annotations, including 10,177 number of identities, 202,599 number of face images, and 5 landmark locations, 40 binary attributes annotations per image.

## Usage

It is composed of 3 sets of images:

* Training
* Validation
* Test

## Example

The dataset returns each item as a dictionary with the following fields:

```
{
    "image": image,
    "bbox": [x1, y1, w, h],
    "facial_landmarks": {
       "lefteye": [x1, y1],
       "righteye": [x2, y2],
       "nose": [x3, y3],
       "leftmouth": [x4, y4],
       "rightmouth": [x5, y5]
    }
}
```

## License

CelebA Dataset is licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0).