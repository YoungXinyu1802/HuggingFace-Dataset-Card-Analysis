---
license: cc-by-nc-sa-4.0
---

# ECHR Cases

The original data from [Chalkidis et al.](https://arxiv.org/abs/1906.02059), sourced from [archive.org](https://archive.org/details/ECHR-ACL2019).

## Preprocessing

* Order is shuffled
* Fact numbers preceeding each fact are removed (using the python regex `^[0-9]+\. `), as some cases didn't have fact numbers to begin with
* Everything else is the same
