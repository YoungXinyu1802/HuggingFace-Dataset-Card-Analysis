---
language:
- en
- fr
- ja
- pt
- ru
- zh
---

## XWinograd

Multilingual winograd schema challenge.

### Languages & Samples

- "en": 2325
- "fr": 83
- "jp": 959
- "pt": 263 
- "ru": 315
- "zh": 504

### Dataset creation

Winograd schema challenges come from the XWinograd dataset introduced in Tikhonov et al. As it only contains 16 Chinese schemas, we add 488 Chinese schemas from `clue/cluewsc2020`.

If you only want the original xWinograd Chinese schemas, do:

`load_dataset("Muennighoff/xwinograd", "zh")["test"][0][:16]`

## Additional Information

### Citation Information

```bibtex
@misc{muennighoff2022crosslingual,
      title={Crosslingual Generalization through Multitask Finetuning}, 
      author={Niklas Muennighoff and Thomas Wang and Lintang Sutawika and Adam Roberts and Stella Biderman and Teven Le Scao and M Saiful Bari and Sheng Shen and Zheng-Xin Yong and Hailey Schoelkopf and Xiangru Tang and Dragomir Radev and Alham Fikri Aji and Khalid Almubarak and Samuel Albanie and Zaid Alyafeai and Albert Webson and Edward Raff and Colin Raffel},
      year={2022},
      eprint={2211.01786},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

```bibtex
@misc{tikhonov2021heads,
    title={It's All in the Heads: Using Attention Heads as a Baseline for Cross-Lingual Transfer in Commonsense Reasoning},
    author={Alexey Tikhonov and Max Ryabinin},
    year={2021},
    eprint={2106.12066},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```

### Contributions

Thanks to Jordan Clive, @yongzx & @khalidalt for support on adding Chinese.
