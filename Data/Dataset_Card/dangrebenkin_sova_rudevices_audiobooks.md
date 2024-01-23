---
license: apache-2.0
dataset_info:
  features:
  - name: audio
    dtype:
      audio:
        sampling_rate: 16000
  - name: transcription
    dtype: string
  splits:
  - name: train
    num_bytes: 29311788948.030003
    num_examples: 182835
  - name: test
    num_bytes: 3181370673.15
    num_examples: 20315
  download_size: 29701298876
  dataset_size: 32493159621.180004
---
## Dataset instance structure
{'audio': {'path': '/path/to/wav.wav',
  'array': array([wav numpy array]), dtype=float32),
  'sampling_rate': 16000},
 'transcription': 'транскрипция'}
## Dataset audio info
- 16000 Hz
- wav
- mono
- Russian speech from audiobooks
## Citation
@misc{sova2021rudevices,
  author = {Zubarev, Egor and Moskalets, Timofey and SOVA.ai},
  title = {SOVA RuDevices Dataset: free public STT/ASR dataset with manually annotated live speech},
  publisher = {GitHub},
  journal = {GitHub repository},
  year = {2021},
  howpublished = {\url{https://github.com/sovaai/sova-dataset}},
}