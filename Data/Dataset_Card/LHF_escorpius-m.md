---
license: cc-by-nc-nd-4.0
language:
- af
- ar
- bn
- ca
- cs
- da
- de
- el
- eu
- fa
- fi
- fr
- gl
- hi
- hr
- it
- ja
- ko
- mt
- nl
- no
- oc
- pa
- pl
- pt
- ro
- sl
- sr
- sv
- tr
- uk
- ur
multilinguality:
- multilingual
size_categories:
- 100B<n<1T
source_datasets:
- original
task_categories:
  - text-generation
  - fill-mask
task_ids:
  - language-modeling
  - masked-language-modeling
---


# esCorpius Multilingual
In the recent years, Transformer-based models have lead to significant advances in language modelling for natural language processing. However, they require a vast amount of data to be (pre-)trained and there is a lack of corpora in languages other than English. Recently, several initiatives have presented multilingual datasets obtained from automatic web crawling. However, they present important shortcomings for languages different from English, as they are either too small, or present a low quality derived from sub-optimal cleaning and deduplication. In this repository, we introduce esCorpius-m, a multilingual crawling corpus obtained from near 1 Pb of Common Crawl data. It is the most extensive corpus in some of the languages covered with this level of quality in the extraction, purification and deduplication of web textual content. Our data curation process involves a novel highly parallel cleaning pipeline and encompasses a series of deduplication mechanisms that together ensure the integrity of both document and paragraph boundaries. Additionally, we maintain both the source web page URL and the WARC shard origin URL in order to complain with EU regulations. esCorpius-m has been released under CC BY-NC-ND 4.0 license.


## Other corpora
- esCorpius-mr multilingual *raw* corpus (not deduplicated): https://huggingface.co/datasets/LHF/escorpius-mr
- esCorpius original *Spanish only* corpus (deduplicated): https://huggingface.co/datasets/LHF/escorpius

## Citation
Link to paper: https://www.isca-speech.org/archive/pdfs/iberspeech_2022/gutierrezfandino22_iberspeech.pdf / https://arxiv.org/abs/2206.15147

Cite this work:
```
@inproceedings{gutierrezfandino22_iberspeech,
  author={Asier Gutiérrez-Fandiño and David Pérez-Fernández and Jordi Armengol-Estapé and David Griol and Zoraida Callejas},
  title={{esCorpius: A Massive Spanish Crawling Corpus}},
  keywords = {Computation and Language (cs.CL), Artificial Intelligence (cs.AI), FOS: Computer and information sciences, FOS: Computer and information sciences},
  year=2022,
  booktitle={Proc. IberSPEECH 2022},
  pages={126--130},
  doi={10.21437/IberSPEECH.2022-26}
}
```
## Disclaimer
We did not perform any kind of filtering and/or censorship to the corpus. We expect users to do so applying their own methods. We are not liable for any misuse of the corpus.
