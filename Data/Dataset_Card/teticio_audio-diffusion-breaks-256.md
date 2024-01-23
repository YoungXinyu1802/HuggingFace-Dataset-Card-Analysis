---
annotations_creators: []
language: []
language_creators: []
license: []
multilinguality: []
pretty_name: Mel spectrograms of sampled music
size_categories:
- 10K<n<100K
source_datasets: []
tags:
- audio
- spectrograms
task_categories:
- image-to-image
task_ids: []
---
30,000 256x256 mel spectrograms of 5 second samples that have been used in music, sourced from [WhoSampled](https://whosampled.com) and [YouTube](https://youtube.com). The code to convert from audio to spectrogram and vice versa can be found in https://github.com/teticio/audio-diffusion along with scripts to train and run inference using De-noising Diffusion Probabilistic Models.

```
x_res = 256
y_res = 256
sample_rate = 22050
n_fft = 2048
hop_length = 512
```