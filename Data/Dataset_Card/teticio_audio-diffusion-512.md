---
dataset_info:
  features:
  - name: image
    dtype: image
  - name: audio_file
    dtype: string
  - name: slice
    dtype: int16
  splits:
  - name: train
    num_bytes: 1903861364.293
    num_examples: 10663
  download_size: 1903696036
  dataset_size: 1903861364.293
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
x_res = 256
y_res = 256
sample_rate = 22050
n_fft = 2048
hop_length = 512
```