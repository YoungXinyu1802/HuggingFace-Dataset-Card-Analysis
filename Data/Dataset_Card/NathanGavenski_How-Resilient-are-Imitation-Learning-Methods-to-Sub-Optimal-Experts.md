---
annotations_creators:
- machine-generated
language_creators:
- expert-generated
language: []
license:
- mit
multilinguality: []
size_categories:
- 100B<n<1T
source_datasets:
- original
task_categories:
- other
task_ids: []
pretty_name: How Resilient are Imitation Learning Methods to Sub-Optimal Experts?
tags:
- Imitation Learning
- Expert Trajectories
- Classic Control
---

# How Resilient are Imitation Learning Methods to Sub-Optimal Experts?

## Related Work
Trajectories used in [How Resilient are Imitation Learning Methods to Sub-Optimal Experts?]()
The code that uses this data is on GitHub: https://github.com/NathanGavenski/How-resilient-IL-methods-are

# Structure
These trajectories are formed by using [Stable Baselines](https://stable-baselines.readthedocs.io/en/master/).
Each file is a dictionary of a set of trajectories with the following keys:

* actions: the action in the given timestamp `t`
* obs: current state in the given timestamp `t`
* rewards: reward retrieved after the action in the given timestamp `t`
* episode_returns: The aggregated reward of each episode (each file consists of 5000 runs)
* episode_Starts: Whether that `obs` is the first state of an episode (boolean list)

## Citation Information
```
@inproceedings{gavenski2022how,
  title={How Resilient are Imitation Learning Methods to Sub-Optimal Experts?},
  author={Nathan Gavenski and Juarez Monteiro and Adilson Medronha and Rodrigo Barros},
  booktitle={2022 Brazilian Conference on Intelligent Systems (BRACIS)},
  year={2022},
  organization={IEEE}
}
```

## Contact:
- [Nathan Schneider Gavenski](nathan.gavenski@edu.pucrs.br)
- [Juarez Monteiro](juarez.santos@edu.pucrs.br)
- [Adilson Medronha](adilson.medronha@edu.pucrs.br)
- [Rodrigo C. Barros](rodrigo.barros@pucrs.br)

