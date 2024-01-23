---
license: openrail
task_categories:
- image-segmentation
tags:
- Duckietown
- Lane Following
- Autonomous Driving
pretty_name: Duckietown Multiclass Semantic Segmentation Dataset
size_categories:
- n<1K
---

# Multiclass Semantic Segmentation Duckietown Dataset
A dataset of multiclass semantic segmentation image annotations for the first 250 images of the ["Duckietown Object Detection Dataset"](https://docs.duckietown.org/daffy/AIDO/out/object_detection_dataset.html).

| Raw Image | Segmentated Image |
| --- | --- |
| <img width="915" alt="raw_image" src="https://user-images.githubusercontent.com/42655977/211690204-301193c3-a651-4a3a-bd66-6458cf3a8778.png"> | <img width="915" alt="segmentation_mask" src="https://user-images.githubusercontent.com/42655977/211690212-2c9ca63a-f3ae-4d65-a4e0-ea76b20a616f.png"> |

# Semantic Classes

This dataset defines 8 semantic classes (7 distinct classes + implicit background class):
| Class | XML Label | Description | Color (RGB) |
| --- | --- | --- | --- |
| Ego Lane | `Ego Lane` | The lane the agent is supposed to be driving in (default right-hand traffic assumed) | `[102,255,102]` |
| Opposite Lane | `Opposite Lane` | The lane opposite to the one the agent is supposed to be driving in (default right-hand traffic assumed) | `[245,147,49]` |
| Road End | `Road End` | Perpendicular red indicator found in Duckietown indicating the end of the road or the beginning of an intersection | `[184,61,245]` |
| Intersection | `Intersection` | Road tile with no lane markings that has either 3 (T-intersection) or 4 (X-intersection) adjacent road tiles  | `[50,183,250]` |
| Middle Lane | `Middle Lane` | Broken yellow lane in the middle of the road separating lanes  | `[255,255,0]` |
| Side Lane | `Side Lane` | Solid white lane marking the road boundary  | `[255,255,255]` |
| Background | `Background` | Unclassified | - (implicit class) |

### **Notice**:

(1) The color assignment is purely a suggestion as the color information encoded in the annotation file is not used by the `cvat_preprocessor.py` and can therefore be overwritten by any other mapping. The specified color mapping is mentioned here for explanatory and consistency reasons as this mapping is used in `dataloader.py` (see [Usage](#usage) for more information).

(2) `[Ego Lane, Opposite Lane, Intersection]` are three semantic classes for essentially the same road tiles - the three classes were added to introduce more information for some use cases. Keep in mind, that some semantic segmentation neural network have a hard time learning the difference between these classes, leading to a poor performance on detecting these classes. In such case, treating these three classes as one *"Road"* class helps improving the segmentation performance.

(3) The `Middle Lane` and `Side Lane` classes were added later and thus only the first 125 images were annotated. If you want to use these, use the `segmentation_annotation.xml` annotation file. Otherwise, `segmentation_annotation_old.xml` stores 250 images (including the 125 images from the other annotation file) but without these two classes.

(4) `Background` is a special semantic class as it is not stored in the annotation file. This class is assigned to all pixels that don't have any other class (see `dataloader.py` for a reference solution for that).

# Usage
[](#usage)

Due to the rather large size of the original dataset *(~750MB)*, this repository only contains annotations file stored in `CVAT for Images 1.1` format as well as two python files:
- `cvat_preprocessor.py`: A collection of helper functions to read the annotations file and extract the annotation masks stored as polygons.
- `dataloader.py`: A [_PyTorch_](https://pytorch.org)-specific example implementation of a wrapper-dataset to use with PyTorch machine learning models. 
