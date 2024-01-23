---
language:
- ms
---
# Unsupervised malay speakers from youtube videos

10492 unique speakers with at least 75 hours of voice activities. Steps to reproduce at https://github.com/huseinzol05/malaya-speech/blob/master/data/youtube/process-youtube.ipynb

## how-to

1. Download and extract [processed-youtube.tar.gz](processed-youtube.tar.gz), each processed videos saved as pickle, `{video_name}.pkl`.

2. Each pickle file got,

```python
[{'wav_data': '/home/husein/ssd2/processed-youtube-v2/"Abam_peluk_saya_lama_atas_pentas_akhir_MLM"-_Ali_Puteh_menangis_imbau_saat_manis_dengan_arwah_abang-_MdgGr7VD7w/0.mp3',
  'timestamp': datetime.datetime(2023, 3, 2, 18, 45, 45, 778042),
  'asr_model': ('kenapa tak mahu bangun kau abang',
   [0.5325799628135358],
   [309, 9, 399, 633, 108, 252]),
  'classification_model': (array([ 3.02432757e-03, -3.64390127e-02,  2.93319039e-02, -2.84599233e-02,
          -5.04244901e-02,  6.03185333e-02,  7.04260264e-03,  7.36895157e-03,
           2.41034012e-02, -3.31214964e-02, -1.61228217e-02, -1.92081463e-02,
          -1.77928973e-02,  1.05488757e-02,  5.11314301e-03,  2.08497643e-02,
           2.80407351e-02, -1.34683009e-02,  1.10213496e-02, -5.76948654e-03,
           2.11171638e-02, -3.10498872e-03,  1.60899870e-02, -2.22061612e-02,
          -3.09270490e-02,  1.03673469e-02,  2.29822248e-02,  5.44358939e-02,
          -9.44061391e-03,  3.24469656e-02, -1.40673192e-02,  6.55731931e-03,
           1.94134321e-02,  2.31755860e-02, -8.62774719e-03, -3.72681394e-03,
          -3.17485556e-02, -1.12474747e-02,  1.65595114e-02,  2.31244415e-02,
           3.28784771e-02,  8.52510054e-03, -6.41896739e-04,  3.13562714e-03,
          -3.15982029e-02,  1.72785181e-03,  1.58039071e-02, -9.93900001e-03,
           2.03248486e-02, -2.98949536e-02,  3.53759155e-02,  3.06809470e-02,
          -3.68881435e-03, -3.98267582e-02, -2.07101982e-02,  2.51877047e-02,
          -2.51530181e-03,  1.06034977e-02,  1.24978041e-02,  2.35916697e-03,
           1.31300613e-02, -1.62451845e-02, -2.09861826e-02,  3.17490734e-02,
          -1.18532358e-02,  4.25735563e-02,  4.17908467e-02,  1.21251179e-03,
          -3.85571155e-03, -9.50544327e-03, -7.37808086e-03,  2.63940021e-02,
           1.09219365e-02,  3.05683501e-02, -4.08848785e-02, -1.71920974e-02,
          -1.46033484e-02, -3.29053291e-05,  3.84788848e-02, -7.86552951e-03,
           1.01251132e-03,  2.72140447e-02,  2.52339337e-02,  3.39004360e-02,
          -1.38184745e-02,  2.60320995e-02, -1.01425601e-02, -1.16012329e-02,
           4.30319924e-03, -1.01203052e-02, -4.66396799e-03, -2.64480542e-02,
           3.44322808e-02, -4.64622118e-03,  1.06053520e-02,  1.37923108e-02,
          -2.05409434e-03, -1.19995829e-02,  2.10450366e-02, -2.87155900e-03,
          -1.39515549e-02, -1.51185887e-02,  2.29053162e-02, -1.78178120e-02,
           1.95855577e-03,  2.37271357e-02,  2.80657201e-03, -6.08753460e-03,
          -2.01220363e-02,  3.22612897e-02,  1.82474777e-02,  5.31493872e-02,
          -7.08705634e-02,  2.76431069e-03,  1.03597697e-02, -3.53837833e-02,
           1.38167264e-02, -5.91275143e-03,  1.84398554e-02,  6.05177172e-02,
           1.14565976e-02,  1.56977493e-02, -1.82731878e-02, -4.58574407e-02,
          -1.08330613e-02, -1.16500622e-02, -1.19803764e-04,  6.48374185e-02,
          -1.21538760e-03, -5.41793741e-02,  1.38867721e-02,  3.52845751e-02,
          -2.08288375e-02,  1.03750750e-02, -2.17110049e-02,  2.29265504e-02,
          -1.21381739e-02, -1.47071329e-03, -4.36875001e-02, -2.25690063e-02,
          -4.16939743e-02, -8.39853752e-03, -2.06098761e-02,  2.30504461e-02,
           3.48615423e-02, -4.18495797e-02, -2.41985917e-03, -3.18994140e-03,
           1.22078639e-02, -9.50168632e-03, -1.97298196e-03,  1.30731370e-02,
           2.07234323e-02,  1.08521534e-02,  2.30542179e-02, -2.54045837e-02,
           1.45645533e-02, -1.08493539e-02, -1.30415503e-02,  3.29123251e-02,
           3.46204527e-02,  2.58748885e-04, -1.28235819e-03, -1.32823242e-02,
           5.47284493e-03, -2.62062326e-02,  2.31803600e-02, -2.04505119e-02,
           2.32407395e-02,  2.12946888e-02, -1.28869051e-02, -6.81399694e-03,
           5.68802692e-02,  4.31004271e-04,  1.67261921e-02,  2.93559525e-02,
           1.32581135e-02, -9.03073605e-03, -9.38207190e-03,  1.74718127e-02,
           1.72506981e-02,  5.02267219e-02, -1.32851647e-02,  5.07321544e-02,
          -1.87530685e-02,  4.18599546e-02,  1.50075918e-02, -2.61102356e-02,
          -1.59594957e-02,  1.36823149e-03, -9.64679196e-03,  1.71130225e-02],
         dtype=float32),
   'speaker 0')}]
```

- all mp3 files postprocessing using https://malaya-speech.readthedocs.io/en/latest/load-noise-reduction.html and https://malaya-speech.readthedocs.io/en/latest/load-speech-enhancement.html
- `wav_data` is directory of the audio, prune the path to proper extracted directory.
- `asr_model` is predicted using the best model that we have, `conformer-medium`, returned `(text, probability, subwords)`, https://malaya-speech.readthedocs.io/en/latest/load-stt-transducer-model-pt.html
- `classification_model` is predicted using NEMO TITANET Large speaker verification model, https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nemo/models/titanet_large, with streaming speaker similarity, https://malaya-speech.readthedocs.io/en/latest/huggingface-repository.html

3. Group by similar speakers using pagerank method (scipy.sparse.linalg.gmres),

- 90% similar, from 10492 unique speakers become 6085 unique speakers, https://github.com/huseinzol05/malaya-speech/blob/master/data/youtube/mapping-youtube-speakers-90.json 
- 85% similar, from 10492 unique speakers become 4312 unique speakers, https://github.com/huseinzol05/malaya-speech/blob/master/data/youtube/mapping-youtube-speakers-85.json
- 80% similar, from 10492 unique speakers become 2912 unique speakers, https://github.com/huseinzol05/malaya-speech/blob/master/data/youtube/mapping-youtube-speakers-80.json

Speaker name defined as,

```python
import os
import pickle

pkl = 'filename.pkl'
with open(pkl, 'rb') as fopen:
  data = pickle.load(fopen)

filename = os.path.split(pkl)[1].replace('.pkl', '')
for result in data:
  speaker_name = f'{filename}-{speaker}'
  actual_speaker = unique_speakers[speaker_name]
```

Check example at https://github.com/huseinzol05/malaya-speech/blob/master/data/youtube/calculate-lengths-80.ipynb