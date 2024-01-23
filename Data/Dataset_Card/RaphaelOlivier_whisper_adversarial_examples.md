---
license: cc-by-4.0
---

# Description
This dataset is a subset of [LibriSpeech](https://huggingface.co/datasets/librispeech_asr) and Multilingual [CommonVoice](commonvoice.mozilla.org/) that have been adversarially modified to fool [Whisper](https://huggingface.co/openai/whisper-medium) ASR model. 

Original [source code](https://github.com/RaphaelOlivier/whisper_attack).

The raw [tar files](https://data.mendeley.com/datasets/96dh52hz9r).
# Configurations and splits
* The `targeted` config contains targeted adversarial examples. When successful, they fool Whisper into predicting the sentence `OK Google, browse to evil.com` even if the input is entirely different. We provide a split for each Whisper model, and one containing the original, unmodified inputs
* The `untargeted-35` and `untargeted-40` configs contain untargeted adversarial examples, with average Signal-Noise Ratios of 35dB and 40dB respectively. They fool Whisper into predicting erroneous transcriptions. We provide a split for each Whisper model, and one containing the original, unmodified inputs
* The `language-<lang> configs contain adversarial examples in language <lang> that fool Whisper in predicting the wrong language. Split `<lang>.<target_lang>` contain inputs that Whisper perceives as <target_lang>, and split `<lang>.original` contains the original inputs in language <lang>. We use 3 target languages (English, Tagalog and Serbian) and 7 source languages (English, Italian, Indonesian, Danish, Czech, Lithuanian and Armenian).

# Usage

Here is an example of code using this dataset:

```python
model_name="whisper-medium"
config_name="targeted"
split_name="whisper.medium"
hub_path = "openai/whisper-"+model_name
processor = WhisperProcessor.from_pretrained(hub_path)
model = WhisperForConditionalGeneration.from_pretrained(hub_path).to("cuda")

dataset = load_dataset("RaphaelOlivier/whisper_adversarial_examples",config_name ,split=split_name)

def map_to_pred(batch):
    input_features = processor(batch["audio"][0]["array"], return_tensors="pt").input_features
    predicted_ids = model.generate(input_features.to("cuda"))
    transcription = processor.batch_decode(predicted_ids, normalize = True)
    batch['text'][0] = processor.tokenizer._normalize(batch['text'][0])
    batch["transcription"] = transcription
    return batch

result = dataset.map(map_to_pred, batched=True, batch_size=1)

wer = load("wer")
for t in zip(result["text"],result["transcription"]):
    print(t)
print(wer.compute(predictions=result["text"], references=result["transcription"]))

```