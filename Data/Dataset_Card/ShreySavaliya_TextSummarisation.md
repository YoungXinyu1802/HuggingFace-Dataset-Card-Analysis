---
tags:
- autotrain
- summarization
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- vishw2703/autotrain-data-unisumm_3
co2_eq_emissions:
  emissions: 1368.894142563709
---

# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 1228646724
- CO2 Emissions (in grams): 1368.8941

## Validation Metrics

- Loss: 2.319
- Rouge1: 43.703
- Rouge2: 16.106
- RougeL: 23.715
- RougeLsum: 38.984
- Gen Len: 141.091

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/vishw2703/autotrain-unisumm_3-1228646724
```