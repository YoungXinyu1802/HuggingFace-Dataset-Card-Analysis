---
license: apache-2.0
tags:
- flan
- flan 2022
- flan v2
pretty_name: Flan v2
---
# Dataset Card for Flan V2

## Dataset Description

- **Homepage:** https://ai.googleblog.com/2023/02/the-flan-collection-advancing-open.html
- **Repository:** https://github.com/google-research/FLAN/tree/main/flan/v2
- **Paper:** https://arxiv.org/abs/2301.13688
- **Leaderboard:** 
- **Point of Contact:** 

### Dataset Summary

This is a processed version of the Flan V2 dataset.

I'm not affiliated with the creators, I'm just releasing the files in an easier-to-access format after processing.

The authors of the Flan Collection recommend experimenting with different mixing ratio's of tasks to get optimal results downstream.

## Setup Instructions

Here are the steps I followed to get everything working:

### Build AESLC and WinoGrande datasets manually

The repos for these datasets were updated recently and checksums need to be recomputed in TFDS

- `tfds build --dataset aeslc --register_checksums`
- `tfds build --dataset winogrande --register_checksums`

### Fix dataset versions

I've opened a PR [here](https://github.com/google-research/FLAN/pull/20) to get these updated in the upstream FLAN repo, until that gets merged in run these locally to fix any dataset version errors.

- `sed -i 's/glue\/cola:1.0.0/glue\/cola:2.0.0/g' flan/v2/task_configs_v1.py`
- `sed -i 's/gem\/common_gen:1.0.0/gem\/common_gen:1.1.0/g' flan/v2/task_configs_v1.py`
- `sed -i 's/gem\/dart:1.0.0/gem\/dart:1.1.0/g' flan/v2/task_configs_v1.py`
- `sed -i 's/gem\/e2e_nlg:1.0.0/gem\/e2e_nlg:1.1.0/g' flan/v2/task_configs_v1.py`
- `sed -i 's/gem\/web_nlg_en:1.0.0/gem\/web_nlg_en:1.1.0/g' flan/v2/task_configs_v1.py`
- `sed -i 's/gem\/common_gen:1.0.0/gem\/common_gen:1.1.0/g' flan/v2/task_configs_v1.py`
- `sed -i 's/paws_wiki:1.0.0/paws_wiki:1.1.0/g' flan/v2/task_configs_v1.py`
- `sed -i 's/glue\/mrpc:1.0.0/glue\/mrpc:2.0.0/g' flan/v2/task_configs_v1.py`
- `sed -i 's/glue\/qqp:1.0.0/glue\/qqp:2.0.0/g' flan/v2/task_configs_v1.py`
- `sed -i 's/glue\/sst2:1.0.0/glue\/sst2:2.0.0/g' flan/v2/task_configs_v1.py`
- `sed -i 's/glue\/mnli:1.0.0/glue\/mnli:2.0.0/g' flan/v2/task_configs_v1.py`
- `sed -i 's/glue\/qnli:1.0.0/glue\/qnli:2.0.0/g' flan/v2/task_configs_v1.py`
- `sed -i 's/glue\/wnli:1.0.0/glue\/wnli:2.0.0/g' flan/v2/task_configs_v1.py`
- `sed -i 's/glue\/stsb:1.0.0/glue\/stsb:2.0.0/g' flan/v2/task_configs_v1.py`
- `sed -i 's/hellaswag:0.0.1/hellaswag:1.1.0/g' flan/v2/task_configs_v1.py`
- `sed -i 's/xsum:1.0.0/huggingface:xsum/g' flan/v2/task_configs_v1.py`

### Download and install manual steps

Save these to `~/tensorflow_datasets/downloads/manual`. 

- [CzEng (deduped ignoring sections)](https://ufal.mff.cuni.cz/czeng/czeng16pre)
- [Newsroom (extract)](https://lil.nlp.cornell.edu/newsroom/download/index.html)
- [Yandex 1M Corpus](https://translate.yandex.ru/corpus?lang=en)
- [Story Cloze (extract and rename to cloze_test_test__spring2016.csv and cloze_test_val__spring2016.csv)](https://cs.rochester.edu/nlp/)

### Finally, export tasks

```python
import tensorflow as tf
tf.config.set_visible_devices([], 'GPU')
from flan.v2 import constants
from flan.v2 import constants_t0
from flan.v2 import mixtures_utils
from flan.v2 import mixtures
from flan.v2 import tasks
import json
import t5
import seqio
import itertools
from multiprocessing import Pool
seqio.add_global_cache_dirs(constants.CACHE_DIRS)
seqio.set_global_cache_dirs(constants.CACHE_DIRS)

vocab = t5.data.get_default_vocabulary()
def prepare_task(split, shots, opt, task):
    dataset = seqio.get_mixture_or_task(f'palmflan_{task}_{shots}_{opt}').get_dataset(
        split=split,
        num_epochs=1,
        sequence_length={'inputs':4096,'targets':4096}
    )
    print("starting", task, shots, opt, split)
    with open(f'./data/{task}_{shots}_{opt}_{split}.jsonl', 'w') as f:
        for ex in dataset.as_numpy_iterator():
            f.write(
                json.dumps({
                "inputs": vocab.decode(ex["inputs"]),
                "targets": vocab.decode(ex["targets"]),
                "task": task,
            }))
            f.write("\n")
    print("done with", task, shots, opt, split)

# prepare_task("train", "zs", "noopt", "dialog") # use this to export a single task
tasks = itertools.product(["train"], ["zs", "fs"], ["opt", "noopt"], ["dialog", "t0", "niv2", "flan", "cot"])
with Pool(5) as p:
    p.starmap(prepare_task, [(task[0], task[1], task[2], task[3]) for task in tasks])
```

## Dataset Structure

### Data Instances

Flan 2021 (flan), P3 (t0), Super-Natural Instructions (niv2), Chain-of-thought (cot), and Dialog (dialog)

### Data Fields

Instruction data comes in a few formats:
- Few Shot (fs)
- Zero Shot (zs)
- Options Provided in context (i.e. multiple choice pick one) (opt)
- No Options Provided (noopt)

Each combination of the above tasks + formats are saved as a JSONL with following schema `{"input": ..., "target": ..., "task": ...}`

### Data Splits

Everything is saved as a train split
Note: FLAN-fs-opt-train is too big to be uploaded even when gzipped, so its split into 45gb chunks. To combine and recover, run `cat flan_fs_opt_train_*.gz | gunzip -c > flan_fs_opt_train.jsonl`
