---
license: apache-2.0
tags:
- flan
- flan 2022
- flan v2
pretty_name: Flan v2
duplicated_from: SirNeural/flan_v2
---

# Fork of [SirNeural/flan_v2](https://huggingface.co/datasets/SirNeural/flan_v2)

just in case it gets deleted. 

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

This current version I've processed is missing a few datasets compared to the main branch of the flan v2 repo:
- cs-en WMT translation task requires manual download and I wasn't able to get the credentials
- q_re_cc dataset preprocessing for the dialog task wasn't working
- 
These are minor hits to the total size of the collection (orders of MB compared to GB) but once those are fixed I will upload a complete version.

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
