---
license: mit
---

# Dataset Description
Out of **20,577** human proteins (from [UniProt human proteome](https://www.uniprot.org/proteomes/UP000005640)), sequences shorter than 20 amino acids or longer than 512 amino acids were removed, resulting in a set of **12,703** proteins. The uShuffle algorithm ([python pacakge](https://github.com/guma44/ushuffle)) was then used to shuffle these protein sequences while maintaining their doublet distribution. The very few sequences for which uShuffle failed to create a shuffled version were eliminated.
Afterwards, h-CD-HIT algorithm ([web server](http://weizhong-lab.ucsd.edu/cdhit-web-server/cgi-bin/index.cgi)) was used with three subsequent filter stages at pairwise identity cutoffs of 0.9, 0.5 and 0.1, resulting in a total of **11,658** sequences.

# Citation
If you use this dataset, please cite our paper:
```
@article {
	author = {Geffen, Yaron and Ofran, Yanay and Unger, Ron},
	title = {DistilProtBert: A distilled protein language model used to distinguish between real proteins and their randomly shuffled counterparts},
	year = {2022},
	doi = {10.1093/bioinformatics/btac474},
	URL = {https://doi.org/10.1093/bioinformatics/btac474},
	journal = {Bioinformatics}
}
```