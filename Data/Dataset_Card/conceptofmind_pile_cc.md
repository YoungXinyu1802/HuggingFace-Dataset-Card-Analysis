## Pile-CC 
Common Crawl is a collection of website crawls from 2008 onwards, including raw web pages, metadata and text extractions. Due to the raw nature of the dataset, Common Crawl has the advantage of including text from diverse domains, but at the cost of varying quality data. Due to this, use of Common Crawl typically necessitates well-designed extraction and filtering. Our Common Crawl-based dataset, Pile-CC, uses jusText (Endrédy and Novák, 2013) on Web Archive files (raw HTTP responses including page HTML) for extraction, which yields higher quality output than directly using the WET files (extracted plaintext).

## Dataset Description
- Homepage: https://pile.eleuther.ai/
- Repository: https://github.com/EleutherAI/the-pile
- Paper: [The Pile: An 800GB Dataset of Diverse Text for Language Modeling](https://arxiv.org/abs/2101.00027)
- Email: [EleutherAI](mailto:contact@eleuther.ai)

## Citation:
```
@misc{gao2020pile,
      title={The Pile: An 800GB Dataset of Diverse Text for Language Modeling},
      author={Leo Gao and Stella Biderman and Sid Black and Laurence Golding and Travis Hoppe and Charles Foster and Jason Phang and Horace He and Anish Thite and Noa Nabeshima and Shawn Presser and Connor Leahy},
      year={2020},
      eprint={2101.00027},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```