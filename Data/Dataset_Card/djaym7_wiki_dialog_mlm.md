---
license: apache-2.0
---
Wiki_dialog dataset with Inpainting (MLM) on dialog. Section 2.1 in paper : https://arxiv.org/abs/2205.09073
https://huggingface.co/datasets/djaym7/wiki_dialog


Access using 
dataset = datasets.load_dataset('djaym7/wiki_dialog_mlm','OQ', beam_runner='DirectRunner')