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
    num_bytes: 45608.0
    num_examples: 511
  download_size: 18295
  dataset_size: 45608.0
license: gpl-3.0
task_categories:
- text-classification
- reinforcement-learning
tags:
- chess
size_categories:
- n<1K
---
# Dataset Card for "yolochess_deepblue"

Source: https://github.com/niklasf/python-chess/tree/master/data/pgn 

Features:
- fen = Chess board position in [FEN](https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation) format
- move = Move played by a strong human player in this position
- result = Final result of the match
- eco = Opening [ECO](https://en.wikipedia.org/wiki/Encyclopaedia_of_Chess_Openings)-code
  
Deduplicated on (fen, move) pairs.  
  
Samples: 511