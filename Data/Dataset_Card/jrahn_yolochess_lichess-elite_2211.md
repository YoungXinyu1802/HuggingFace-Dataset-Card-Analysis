---
dataset_info:
  features:
  - name: fen
    dtype: string
  - name: move
    dtype: string
  - name: result
    dtype: string
  - name: eco
    dtype: string
  splits:
  - name: train
    num_bytes: 1794337922
    num_examples: 22116598
  download_size: 1044871571
  dataset_size: 1794337922
task_categories:
- text-classification
- reinforcement-learning
license: cc
tags:
- chess
size_categories:
- 10M<n<100M
---
# Dataset Card for "yolochess_lichess-elite_2211"

Source: https://database.nikonoel.fr/ - filtered from https://database.lichess.org for November 2022  

Features:
- fen = Chess board position in [FEN](https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation) format
- move = Move played by a strong human player in this position
- result = Final result of the match
- eco = [ECO](https://en.wikipedia.org/wiki/Encyclopaedia_of_Chess_Openings)-code of the Opening played

Samples: 22.1 million