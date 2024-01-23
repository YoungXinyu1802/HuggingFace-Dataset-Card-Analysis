---
license: apache-2.0
pretty_name: D4RL-gym
---
# Dataset Card for D4RL-gym
## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)
## Dataset Description
- **Homepage:** https://sites.google.com/view/d4rl/home/
- **Repository:** https://github.com/rail-berkeley/d4rl* 
- **Paper:** D4RL: Datasets for Deep Data-Driven Reinforcement Learning https://arxiv.org/abs/2004.07219

### Dataset Summary
D4RL is an open-source benchmark for offline reinforcement learning. It provides standardized environments and datasets for training and benchmarking algorithms. 
We host here a subset of the dataset, used for the training of Decision Transformers : https://github.com/kzl/decision-transformer
There is only a training set for this dataset, as evaluation is undertaken by interacting with a simulator.

## Dataset Structure
### Data Instances
A data point comprises tuples of sequences of (observations, actions, reward, dones):
```
{
    "observations":datasets.Array2D(),
    "actions":datasets.Array2D(),
    "rewards":datasets.Array2D(),
    "dones":datasets.Array2D(),

}
```
### Data Fields
- `observations`: An Array2D containing 1000 observations from a trajectory of an evaluated agent.
- `actions`: An Array2D containing 1000 actions from a trajectory of an evaluated agent.
- `rewards`: An Array2D containing 1000 rewards from a trajectory of an evaluated agent.
- `dones`: An Array2D containing 1000 terminal state flags from a trajectory of an evaluated agent.

### Data Splits
There is only a training set for this dataset, as evaluation is undertaken by interacting with a simulator.

## Additional Information
### Dataset Curators
Justin Fu, Aviral Kumar, Ofir Nachum, George Tucker, Sergey Levine
### Licensing Information
MIT Licence
### Citation Information
```
@misc{fu2021d4rl,
      title={D4RL: Datasets for Deep Data-Driven Reinforcement Learning}, 
      author={Justin Fu and Aviral Kumar and Ofir Nachum and George Tucker and Sergey Levine},
      year={2021},
      eprint={2004.07219},
      archivePrefix={arXiv},
      primaryClass={cs.LG}
}
```
### Contributions
Thanks to [@edbeeching](https://github.com/edbeeching) for adding this dataset.