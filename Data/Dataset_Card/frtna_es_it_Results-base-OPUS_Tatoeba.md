- Model: [OPUS-MT](https://huggingface.co/Helsinki-NLP/opus-mt-es-it)
- Tested on: [Tatoeba]()
<br>
- Metric: 
  - bleu(tensorflow),
  - sacrebleu(github->mjpost), 
  - google_bleu(nltk), 
  - rouge(google-research),
  - meteor(nltk), 
  - ter(university of Maryland)
<br> 
- Retrieved from: [Huggingface](https://huggingface.co/metrics/) [metrics](https://github.com/huggingface/datasets/blob/master/metrics/) 
- Script used for translation and testing: [https://gitlab.com/hmtkvs/machine_translation/-/tree/production-stable](https://gitlab.com/hmtkvs/machine_translation/-/tree/production-stable)

## Info
## mtdata-OPUS Tatoeba (length=14178, single reference)
**bleu** : 0.5228
<br>
**sacrebleu** : 0.5652
<br>
**google_bleu** : 0.5454
<br>
**rouge-mid** : precision=0.7792, recall=0.7899, f_measure=0.7796
<br>
**meteor** : 0.7557
<br>
**ter** : score=0.3003, num_edits= 24654, ref_length= 82079.0

## OPUS Tatoeba (length = 5000, multi references)
**bleu** : 0.5165
<br>
**sacrebleu** : 0.7098
<br>
**google_bleu** : 0.5397
<br>
**rouge-mid** : precision=0.9965, recall=0.5021, f_measure=0.6665
<br>
**meteor** : 0.3344
<br>
**ter** : score: 0.6703, 'num_edits': 38883, 'ref_length': 58000.0