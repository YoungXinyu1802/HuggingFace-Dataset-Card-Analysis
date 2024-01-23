---
library_name: gia
tags:
- deep-reinforcement-learning
- reinforcement-learning
- gia
- multi-task
- multi-modal
- imitation-learning
- offline-reinforcement-learning
---

An imitation learning environment for the door-open-v2 environment, sample for the policy door-open-v2 

This environment was created as part of the Generally Intelligent Agents project gia: https://github.com/huggingface/gia 




## Load dataset

First, clone it with

```sh
git clone https://huggingface.co/datasets/qgallouedec/prj_gia_dataset_metaworld_door_open_v2_1111
```

Then, load it with

```python
import numpy as np
dataset = np.load("prj_gia_dataset_metaworld_door_open_v2_1111/dataset.npy", allow_pickle=True).item()
print(dataset.keys())  # dict_keys(['observations', 'actions', 'dones', 'rewards'])
```

    