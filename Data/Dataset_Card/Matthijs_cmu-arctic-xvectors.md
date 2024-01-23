---
pretty_name: CMU ARCTIC X-Vectors
task_categories:
- text-to-speech
- audio-to-audio
license: mit
---

# Speaker embeddings extracted from CMU ARCTIC

There is one `.npy` file for each utterance in the dataset, 7931 files in total. The speaker embeddings are 512-element X-vectors.

The [CMU ARCTIC](http://www.festvox.org/cmu_arctic/) dataset divides the utterances among the following speakers:

- bdl (US male)
- slt (US female)
- jmk (Canadian male)
- awb (Scottish male)
- rms (US male)
- clb (US female)
- ksp (Indian male)

The X-vectors were extracted using [this script](https://huggingface.co/mechanicalsea/speecht5-vc/blob/main/manifest/utils/prep_cmu_arctic_spkemb.py), which uses the `speechbrain/spkrec-xvect-voxceleb` model.

Usage:

```python
from datasets import load_dataset
embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")

speaker_embeddings = embeddings_dataset[7306]["xvector"]
speaker_embeddings = torch.tensor(speaker_embeddings).unsqueeze(0)
```
