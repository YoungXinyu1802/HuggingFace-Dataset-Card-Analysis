---
license: cc-by-4.0
pretty_name: QG Annotation
language: en
multilinguality: monolingual
size_categories: <1K
---

# Dataset Card for "lmqg/qg_annotation"

## Dataset Description
- **Repository:** [https://github.com/asahi417/lm-question-generation](https://github.com/asahi417/lm-question-generation)
- **Paper:** [https://arxiv.org/abs/2210.03992](https://arxiv.org/abs/2210.03992)
- **Point of Contact:** [Asahi Ushio](http://asahiushio.com/)

### Dataset Summary
This is the annotated questions generated by different models, used to measure the correlation of automatic metrics against 
human in ["Generative Language Models for Paragraph-Level Question Generation: A Unified Benchmark and Evaluation, EMNLP 2022 main conference"](https://arxiv.org/abs/2210.03992).

### Languages
English (en)

## Dataset Structure
An example of 'train' looks as follows.

```python
{
    "correctness": 1.8,
    "grammaticality": 3.0,
    "understandability": 2.4,
    "prediction": "What trade did the Ming dynasty have a shortage of?",
    "Bleu_4": 0.4961682999359617,
    "METEOR": 0.3572683356086923,
    "ROUGE_L": 0.7272727272727273,
    "BERTScore": 0.9142221808433532,
    "MoverScore": 0.6782580808848975,
    "reference_raw": "What important trade did the Ming Dynasty have with Tibet?",
    "answer_raw": "horse trade",
    "paragraph_raw": "Some scholars note that Tibetan leaders during the Ming frequently engaged in civil war and conducted their own foreign diplomacy with neighboring states such as Nepal. Some scholars underscore the commercial aspect of the Ming-Tibetan relationship, noting the Ming dynasty's shortage of horses for warfare and thus the importance of the horse trade with Tibet. Others argue that the significant religious nature of the relationship of the Ming court with Tibetan lamas is underrepresented in modern scholarship. In hopes of reviving the unique relationship of the earlier Mongol leader Kublai Khan (r. 1260\u20131294) and his spiritual superior Drog\u00f6n Ch\u00f6gyal Phagpa (1235\u20131280) of the Sakya school of Tibetan Buddhism, the Yongle Emperor (r. 1402\u20131424) made a concerted effort to build a secular and religious alliance with Deshin Shekpa (1384\u20131415), the Karmapa of the Karma Kagyu school. However, the Yongle Emperor's attempts were unsuccessful.",
    "sentence_raw": "Some scholars underscore the commercial aspect of the Ming-Tibetan relationship, noting the Ming dynasty's shortage of horses for warfare and thus the importance of the horse trade with Tibet.",
    "reference_norm": "what important trade did the ming dynasty have with tibet ?",
    "model": "T5 Large"
}
```

## Citation Information
```
@inproceedings{ushio-etal-2022-generative,
    title = "{G}enerative {L}anguage {M}odels for {P}aragraph-{L}evel {Q}uestion {G}eneration",
    author = "Ushio, Asahi  and
        Alva-Manchego, Fernando  and
        Camacho-Collados, Jose",
    booktitle = "Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing",
    month = dec,
    year = "2022",
    address = "Abu Dhabi, U.A.E.",
    publisher = "Association for Computational Linguistics",
}
```