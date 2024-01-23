---
size_categories:
- n<1K
task_categories:
- image-segmentation
task_ids:
- semantic-segmentation
tags:
- teeth-segmentation
- dental-imaging
- medical-imaging
train-eval-index:
- config: plain_text
  task: semantic_segmentation
  task_id: semantic_segmentation
  splits:
    train_split: train
    eval_split: test
  col_mapping:
    image: image
    label: image
---

# Dataset Card for [Dataset Name]

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Homepage:** [https://github.com/SerdarHelli/Segmentation-of-Teeth-in-Panoramic-X-ray-Image-Using-U-Net](https://github.com/SerdarHelli/Segmentation-of-Teeth-in-Panoramic-X-ray-Image-Using-U-Net)
- **Repository:** [https://github.com/SerdarHelli/Segmentation-of-Teeth-in-Panoramic-X-ray-Image-Using-U-Net](https://github.com/SerdarHelli/Segmentation-of-Teeth-in-Panoramic-X-ray-Image-Using-U-Net)
- **Paper:** [Tooth Instance Segmentation on Panoramic Dental Radiographs Using U-Nets and Morphological Processing](https://dergipark.org.tr/tr/pub/dubited/issue/68307/950568) 
- **Leaderboard:**
- **Point of Contact:** S.Serdar Helli

### Dataset Summary

  # Semantic-Segmentation-of-Teeth-in-Panoramic-X-ray-Image
  The aim of this study is automatic semantic segmentation and measurement total length of teeth in one-shot panoramic x-ray image by using deep learning method with U-Net Model and binary image analysis in order to provide diagnostic information for the management of dental disorders, diseases, and conditions. 
  
   [***Github Link***](https://github.com/SerdarHelli/Segmentation-of-Teeth-in-Panoramic-X-ray-Image-Using-U-Net)
  
  
  ***Original Dataset For Only Images***
  DATASET ref - 	H. Abdi, S. Kasaei, and M. Mehdizadeh, “Automatic segmentation of mandible in panoramic x-ray,” J. Med. Imaging, vol. 2, no. 4, p. 44003, 2015
  [Link DATASET for only original images.](https://data.mendeley.com/datasets/hxt48yk462/1)

## Dataset Structure

### Data Instances

An example of 'train' looks as follows.
```
{
    "image": X-ray Image (Image),
    "label": Binary Image Segmentation Map (Image)
    
}
```

## Dataset Creation

### Source Data
  ***Original Dataset For Only Images***
  DATASET ref - 	H. Abdi, S. Kasaei, and M. Mehdizadeh, “Automatic segmentation of mandible in panoramic x-ray,” J. Med. Imaging, vol. 2, no. 4, p. 44003, 2015
  [Link DATASET for only original images.](https://data.mendeley.com/datasets/hxt48yk462/1)


### Annotations

#### Annotation process

The annotation was made manually.

#### Who are the annotators?

S.Serdar Helli


### Other Known Limitations
 The X-Ray Images files associated with this dataset are licensed under a Creative Commons Attribution 4.0 International license.

To Check Out For More Information: 

  ***Original Dataset For Only Images***
  DATASET ref - 	H. Abdi, S. Kasaei, and M. Mehdizadeh, “Automatic segmentation of mandible in panoramic x-ray,” J. Med. Imaging, vol. 2, no. 4, p. 44003, 2015
  [Link DATASET for only original images.](https://data.mendeley.com/datasets/hxt48yk462/1)
## Additional Information

### Citation Information

For Labelling 
```
@article{helli10tooth,
  title={Tooth Instance Segmentation on Panoramic Dental Radiographs Using U-Nets and Morphological Processing},
  author={HELL{\.I}, Serdar and HAMAMCI, Anda{\c{c}}},
  journal={D{\"u}zce {\"U}niversitesi Bilim ve Teknoloji Dergisi},
  volume={10},
  number={1},
  pages={39--50}
}
```

For Original Images 

```

@article{abdi2015automatic,
  title={Automatic segmentation of mandible in panoramic x-ray},
  author={Abdi, Amir Hossein and Kasaei, Shohreh and Mehdizadeh, Mojdeh},
  journal={Journal of Medical Imaging},
  volume={2},
  number={4},
  pages={044003},
  year={2015},
  publisher={SPIE}
}
```

### Contributions

Thanks to [@SerdarHelli](https://github.com/SerdarHelli) for adding this dataset.