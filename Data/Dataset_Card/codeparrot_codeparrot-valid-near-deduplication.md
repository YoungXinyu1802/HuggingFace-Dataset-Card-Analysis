# CodeParrot 🦜 Dataset after near deduplication (validation)

## Dataset Description

A dataset of Python files from Github. We performed near deduplication of this dataset split [codeparrot-clean-train](https://huggingface.co/datasets/codeparrot/codeparrot-clean-valid) from [codeparrot-clean](https://huggingface.co/datasets/codeparrot/codeparrot-clean#codeparrot-%F0%9F%A6%9C-dataset-cleaned). Exact deduplication can miss a fair amount of nearly identical files. We used MinHash with a Jaccard threshold (default=0.85) to create duplicate clusters. Then these clusters are reduced to unique files based on the exact Jaccard similarity. Fore more details, please refer to this [repo](https://github.com/huggingface/transformers/tree/main/examples/research_projects/codeparrot).

