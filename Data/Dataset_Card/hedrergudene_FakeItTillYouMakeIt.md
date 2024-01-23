# Introduction

Face Synthetics dataset is a collection of diverse synthetic face images with ground truth labels.

It was introduced in our paper Fake It Till You Make It: Face analysis in the wild using synthetic data alone.

Our dataset contains:

100,000 images of faces at 512 x 512 pixel resolution
70 standard facial landmark annotations
per-pixel semantic class anotations
It can be used to train machine learning systems for face-related tasks such as landmark localization and face parsing, showing that synthetic data can both match real data in accuracy as well as open up new approaches where manual labelling would be impossible.

Some images also include hands and off-center distractor faces in addition to primary faces centered in the image.

The Face Synthetics dataset can be used for non-commercial research, and is licensed under the license found in LICENSE.txt.

# Dataset Layout
The Face Synthetics dataset is a single .zip file containing color images, segmentation images, and 2D landmark coordinates in a text file.
```markdown
dataset.zip
|
|- {frame_id}.png         # Rendered image of a face
|- {frame_id}_seg.pmg     # Segmentation image
|- {frame_id}_ldmks.txt   # Landmark annotations for 70 facial landmarks (x,y)
```

# Download
A small subset of the original dataset can be found here; in order to train models in the entire dataset, please refer to [Microsoft original repo](https://github.com/microsoft/FaceSynthetics).