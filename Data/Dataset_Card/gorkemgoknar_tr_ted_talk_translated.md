---
language:
- tr
thumbnail:
tags:
- dataset
- turkish
- ted-multi
- cleaned

license: apache-2.0
datasets:
- ted-multi

---

# Turkish Ted talk translations 
# Created from ted-multi dataset

adding processing steps here if you want another language


```python
#using Turkish as target
target_lang="tr"  # change to your target lang


from datasets import load_dataset
#ted-multi is a multiple language translated dataset
#fits for our case , not to big and curated but need a simple processing

dataset = load_dataset("ted_multi")
dataset.cleanup_cache_files()

#original from patrick's
#chars_to_ignore_regex = '[,?.!\-\;\:\"“%‘”�—’…–]'  # change to the ignored characters of your fine-tuned model

#will use cahya/wav2vec2-base-turkish-artificial-cv
#checking inside model repository to find which chars removed (no run.sh)
chars_to_ignore_regex = '[\,\?\.\!\-\;\:\"\“\‘\”\'\`…\’»«]'


import re

def extract_target_lang_entries(batch):
  #specific mapping for ted_multi dataset
  #need to find index of language in each translation as it can shift
  try:
    target_index_for_lang= batch["translations"]["language"].index(target_lang) 
  except ValueError:
    #target not in list empty it for later processing
    batch["text"] = None 
    return batch 

  #index_translation_pairs = zip(batch, target_index_for_batch)
  text= batch["translations"]["translation"][target_index_for_lang] 
  batch["text"] = re.sub(chars_to_ignore_regex, "", text.lower())
  return batch


#this dataset has additional columns need to say it
cols_to_remove =  ['translations', 'talk_name']
dataset = dataset.map(extract_target_lang_entries, remove_columns=cols_to_remove)


#on preocessing we tagged None for empty ones
dataset_cleaned = dataset.filter(lambda x: x['text'] is not None)
dataset_cleaned

from huggingface_hub import notebook_login

notebook_login()

dataset_cleaned.push_to_hub(f"{target_lang}_ted_talk_translated")

```