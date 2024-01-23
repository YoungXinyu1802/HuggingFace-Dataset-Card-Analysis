---
# For reference on model card metadata, see the spec: https://github.com/huggingface/hub-docs/blob/main/datasetcard.md?plain=1
# Doc / guide: https://huggingface.co/docs/hub/datasets-cards
{}
---

# Dataset Card for Med-EASi

## Dataset Description
 
- **Repository:https://github.com/Chandrayee/CTRL-SIMP** 
- **Paper:https://arxiv.org/pdf/2302.09155.pdf**  
- **Point of Contact:Chandrayee Basu** 

### Dataset Summary

Med-EASi (Medical dataset for Elaborative and Abstractive Simplification), a uniquely crowdsourced and finely annotated dataset for supervised simplification of short medical
texts. It contains 1979 expert-simple text pairs in medical domain, spanning a total of 4478 UMLS concepts across all text pairs. The dataset is annotated with four textual transformations:
replacement, elaboration, insertion and deletion.

### Supported Tasks 

The dataset can be used for direct generation of simplified medical text or generation of simplified text along with controllability over individual transformations. Please refer to the paper for more information.

### Languages

English

## Dataset Structure

- **train.csv: 1397 text pairs (5.19 MB)**
- **validation.csv: 197 text pairs (1.5 MB)**
- **test.csv: 300 text pairs (1.19 MB)**

We also provide several metrics per data point including Levenstein similarity, SentenceBERT embedding cosine similarity, compression ratio, Flesch Kincaid readability grade, 
automated readability index for each of the expert and simple text, and UMLS concepts in each of them.

### Data Instances

```
Expert: Some patients have weight loss, rarely enough to become underweight. Anemia, glossitis, angular stomatitis, and aphthous ulcers are usually seen in these patients.
Simple: Some people are undernourished, have mild weight loss and anemia, or have mouth sores and an inflamed tongue.
Annotated: Some <elab>patients<by>people are undernourished,</elab> have <elab>weight loss<by>mild weight loss</elab><del>, rarely enough to become underweight.</del> <rep>Anemia, glossitis, angular stomatitis, and aphthous ulcers<by>and anemia, or have mouth sores and an inflamed tongue</rep><del>usually seen in these patients</del>.
```
### Data Fields

```
Expert
Simple
Annotation
sim (Levenstein Similarity)
sentence_sim (SentenceBERT embedding cosine similarity)
compression
expert_fk_grade
expert_ari	
layman_fk_grade	
layman_ari	
umls_expert	
umls_layman	
expert_terms	
layman_terms	
idx (original data index before shuffling, redundant)
```


### Data Splits

75 % train, 10 % validation and 15 % test

## Dataset Creation

This dataset is created by annotating 1500 SIMPWIKI data points (Van den Bercken, Sips, and Lofi 2019) and all of MSD (Cao et al. 2020) data points. We used expert-layman-AI collaboration for annotation. 

### Personal and Sensitive Information

There is no personal or sensitive information in this dataset.

## Considerations for Using the Data

### Discussion of Biases

The dataset contains biomedical and clinical short texts. 

### Other Known Limitations

The expert and simple texts in the original datasets were extracted and aligned using automated methods that have their own limitations.

### Citation Information
```
@article{basu2023med,
  title={Med-EASi: Finely Annotated Dataset and Models for Controllable Simplification of Medical Texts},
  author={Basu, Chandrayee and Vasu, Rosni and Yasunaga, Michihiro and Yang, Qian},
  journal={arXiv preprint arXiv:2302.09155},
  year={2023}
}
```