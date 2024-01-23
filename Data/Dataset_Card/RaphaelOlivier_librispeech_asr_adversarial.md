# Description
This dataset is a subset of [https://huggingface.co/datasets/librispeech_asr](LibriSpeech) that has been adversarially modified. It is designed to fool ASR models into predicting a target of our choosing instead of the correct output.

## Splits
The dataset contains several splits. Each split consists of the same utterances, modified with different types and amount of noise. 3 noises have been used:
* Adversarial noise of radius 0.04 (`adv_0.04` split) 
* Adversarial noise of radius 0.015 (`adv_0.015` split) 
* Adversarial noise of radius 0.015 combined with Room Impulse Response (RIR) noise (`adv_0.015_RIR` split) 

In addition we provide the original inputs (`natural` split)

For each split we actually provide two text keys: `true_text` which is the original LibriSpeech label, i.e. the sentence one can actually hear when listening to the audio; and `target_text`, which is the target sentence of our adversarial attack. An ASR model that this dataset fools would get a low WER on `target_text` and a high WER on `true_text`. An ASR model robust to this dataset would get the opposite. 

## Usage
You should evaluate your model on this dataset as you would evaluate it on LibriSpeech. Here is an example with Wav2Vec2


```python
from datasets import load_dataset
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import torch
from jiwer import wer


librispeech_adv_eval = load_dataset("RaphaelOlivier/librispeech_asr_adversarial", "adv", split="adv_0.15_adv_txt")

model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h").to("cuda")
processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")

def map_to_pred(batch):
    input_values = processor(batch["audio"]["array"], return_tensors="pt", padding="longest").input_values
    with torch.no_grad():
        logits = model(input_values.to("cuda")).logits

    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.batch_decode(predicted_ids)
    batch["transcription"] = transcription
    return batch

result = librispeech_adv_eval.map(map_to_pred, batched=True, batch_size=1, remove_columns=["audio"])

print("WER on correct labels:", wer(result["true_text"], result["transcription"]))
print("WER on attack targets:", wer(result["target_text"], result["transcription"]))
```

*Result (WER)*:

| "0.015 target_text" | "0.015 true_text" | "0.04 target_text" | "0.04 true_text"
|---|---|---|---|
| 58.2 | 108 | 49.5 | 108 |

