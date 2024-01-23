---
dataset_info:
  features:
  - name: transcription
    dtype: string
  - name: audio
    dtype:
      audio:
        sampling_rate: 16000
  splits:
  - name: train
    num_bytes: 1947609729.4653895
    num_examples: 6169
  - name: test
    num_bytes: 864278563.4406104
    num_examples: 2645
  download_size: 2705520657
  dataset_size: 2811888292.906
license: apache-2.0
---
## Dataset audio info
- 16000 Hz 16 bit
- wav
- mono
- Russian speech
## Dataset instance structure
{'audio': {'path': '/path/to/wav.wav',
  'array': array([wav numpy array]), dtype=float32),
  'sampling_rate': 16000},
 'transcription': 'транскрипция'}
## Citation

@Misc{Voxforge.org,
  author = {Voxforge.org},
  title = {Free Speech... Recognition (Linux, Windows and Mac) - voxforge.org},
  howpublished = {\url{[http://www.voxforge.org/]}},
  note = {accessed 01/21/2023}
}

## Source
http://www.voxforge.org/ru/downloads