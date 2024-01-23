---
task_categories:
- audio-classification
size_categories:
- 100B<n<1T
---


# VGGSound
VGG-Sound is an audio-visual correspondent dataset consisting of short clips of audio sounds, extracted from videos uploaded to YouTube.


- **Homepage:** https://www.robots.ox.ac.uk/~vgg/data/vggsound/
- **Paper:** https://arxiv.org/abs/2004.14368
- **Github:** https://github.com/hche11/VGGSound

## Analysis

- **310+ classes:** VGG-Sound contains audios spanning a large number of challenging acoustic environments and noise characteristics of real applications.
- **200,000+ videos:** All videos are captured "in the wild" with audio-visual correspondence in the sense that the sound source is visually evident.
- **550+ hours:** VGG-Sound consists of both audio and video. Each segment is 10 seconds long.

![](src/data.png)
 

## Download

We provide a csv file. For each YouTube video, we provide YouTube URLs, time stamps, audio labels and train/test split. Each line in the csv file has columns defined by here.

```
# YouTube ID, start seconds, label, train/test split. 
```

And you can download VGGSound directly from this [repository](https://huggingface.co/datasets/Loie/VGGSound/tree/main).


## License
The VGG-Sound dataset is available to download for commercial/research purposes under a Creative Commons Attribution 4.0 International License. The copyright remains with the original owners of the video. A complete version of the license can be found [here](https://thor.robots.ox.ac.uk/datasets/vggsound/license_vggsound.txt).

## Citation
Please cite the following if you make use of the dataset.
```
@InProceedings{Chen20,
  author       = "Honglie Chen and Weidi Xie and Andrea Vedaldi and Andrew Zisserman",
  title        = "VGGSound: A Large-scale Audio-Visual Dataset",
  booktitle    = "International Conference on Acoustics, Speech, and Signal Processing (ICASSP)",
  year         = "2020",
}
```