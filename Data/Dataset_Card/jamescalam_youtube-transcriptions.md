---
annotations_creators:
- no-annotation
language:
- en
language_creators:
- found
license:
- afl-3.0
multilinguality:
- monolingual
pretty_name: Youtube Transcriptions
size_categories:
- 10K<n<100K
source_datasets:
- original
tags:
- youtube
- technical
- speech to text
- speech
- video
- video search
- audio
- audio search
task_categories:
- conversational
- question-answering
- text-retrieval
- visual-question-answering
task_ids:
- open-domain-qa
- extractive-qa
- document-retrieval
- visual-question-answering
---

The YouTube transcriptions dataset contains technical tutorials (currently from [James Briggs](https://www.youtube.com/c/jamesbriggs), [Daniel Bourke](https://www.youtube.com/channel/UCr8O8l5cCX85Oem1d18EezQ), and [AI Coffee Break](https://www.youtube.com/c/aicoffeebreak)) transcribed using [OpenAI's Whisper](https://huggingface.co/openai/whisper-large) (large). Each row represents roughly a sentence-length chunk of text alongside the video URL and timestamp.

Note that each item in the dataset contains just a short chunk of text. For most use cases you will likely need to merge multiple rows to create more substantial chunks of text, if you need to do that, this code snippet will help:

```python
from datasets import load_dataset

# first download the dataset
data = load_dataset(
    'jamescalam/youtube-transcriptions',
    split='train'
)

new_data = []  # this will store adjusted data

window = 6  # number of sentences to combine
stride = 3  # number of sentences to 'stride' over, used to create overlap

for i in range(0, len(data), stride):
    i_end = min(len(data)-1, i+window)
    if data[i]['title'] != data[i_end]['title']:
        # in this case we skip this entry as we have start/end of two videos
        continue
    # create larger text chunk
    text = ' '.join(data[i:i_end]['text'])
    # add to adjusted data list
    new_data.append({
        'start': data[i]['start'],
        'end': data[i_end]['end'],
        'title': data[i]['title'],
        'text': text,
        'id': data[i]['id'],
        'url': data[i]['url'],
        'published': data[i]['published']
    })
```