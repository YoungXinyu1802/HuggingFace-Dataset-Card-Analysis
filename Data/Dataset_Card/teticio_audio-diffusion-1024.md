---
annotations_creators: []
language: []
language_creators: []
license: []
multilinguality: []
pretty_name: Mel spectrograms of music
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
Over 20,000 256x256 mel spectrograms of 5 second samples of music from my Spotify liked playlist. The code to convert from audio to spectrogram and vice versa can be found in https://github.com/teticio/audio-diffusion along with scripts to train and run inference using De-noising Diffusion Probabilistic Models.
```
x_res = 1024
y_res = 1024
sample_rate = 44100
n_fft = 2048
hop_length = 512
```