---
license: mit
---

# ProofNet

## Dataset Description

- **Repository:** [zhangir-azerbayev/ProofNet](https://github.com/zhangir-azerbayev/ProofNet)
- **Paper:** [ProofNet](https://mathai2022.github.io/papers/20.pdf)
- **Point of Contact:** [Zhangir Azerbayev](https://zhangir-azerbayev.github.io/)

### Dataset Summary
ProofNet is a benchmark for autoformalization and formal proving of undergraduate-level mathematics. The ProofNet benchmarks consists of 371 examples, each consisting of a formal theorem statement in Lean 3, a natural language theorem statement, and a natural language proof. The problems are primarily drawn from popular undergraduate pure mathematics textbooks and cover topics such as real and complex analysis, linear algebra, abstract algebra, and topology. We intend for ProofNet to be a challenging benchmark that will drive progress in autoformalization and automatic theorem proving.

**Citation**:
```bibtex
@misc{azerbayev2023proofnet,
      title={ProofNet: Autoformalizing and Formally Proving Undergraduate-Level Mathematics}, 
      author={Zhangir Azerbayev and Bartosz Piotrowski and Hailey Schoelkopf and Edward W. Ayers and Dragomir Radev and Jeremy Avigad},
      year={2023},
      eprint={2302.12433},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
### Leaderboard
**Statement Autoformalization**
| Model                              | Typecheck Rate | Accuracy |
| ---------------------------------- | -------------- | -------- |
| Davinci-code-002 (prompt retrieval)| 45.2           | 16.1     |
| Davinci-code-002 (in-context learning) | 23.7       | 13.4     |
| proofGPT-1.3B                      | 10.7           | 3.2      |

**Statement Informalization**
| Model                              | Accuracy |
| ---------------------------------- | -------- |
| Code-davinci-002 (in-context learning)| 62.3    |
| proofGPT-6.7B (in-context learning) | 6.5      |
| proofGPT-1.3B (in-context learning) | 4.3      |

### Data Fields

- `id`: Unique string identifier for the problem.
- `nl_statement`: Natural language theorem statement.
- `nl_proof`: Natural language proof, in LaTeX. Depends on `amsthm, amsmath, amssymb` packages.
- `formal_statement`: Formal theorem statement in Lean 3.
- `src_header`: File header including imports, namespaces, and locales required for the formal statement. Note that local import of [common.lean](https://github.com/zhangir-azerbayev/ProofNet/blob/main/benchmark/benchmark_to_publish/formal/common.lean), which has to be manually downloaded and place in the same directory as your `.lean` file containing the formal statement. 

### Authors
Zhangir Azerbayev, Bartosz Piotrowski, Jeremy Avigad