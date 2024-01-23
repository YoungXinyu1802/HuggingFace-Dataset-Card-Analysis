---
language:
- en
paperswithcode_id: docvqa
pretty_name: DocVQA - A Dataset for VQA on Document Images
task_ids:
- document-question-answering
---

# DocVQA: A Dataset for VQA on Document Images

The DocVQA dataset can be downloaded from the [challenge page](https://rrc.cvc.uab.es/?ch=17) in RRC portal ("Downloads" tab).


## Dataset Structure

The DocVQA comprises 50, 000 questions framed on 12,767 images. The data is split randomly in an 80−10−10 ratio to train, validation and test splits.
- Train split: 39,463 questions, 10,194 images
- Validation split: 5,349 questions and 1,286 images
- Test split has 5,188 questions and 1,287 images.

## Resources and Additional Information
- More information can be found on the [challenge page](https://rrc.cvc.uab.es/?ch=17) and in the [DocVQA paper](https://arxiv.org/abs/2007.00398).
- Document images are taken from the [UCSF Industry Documents Library](https://www.industrydocuments.ucsf.edu/). It consists of a mix of printed, typewritten and handwritten content. A wide variety of document types appears in this dataset including letters, memos, notes, reports etc.


## Citation Information

```
@InProceedings{mathew2021docvqa,
  author    = {Mathew, Minesh and Karatzas, Dimosthenis and Jawahar, CV},
  title     = {Docvqa: A dataset for vqa on document images},
  booktitle = {Proceedings of the IEEE/CVF winter conference on applications of computer vision},
  year      = {2021},
  pages     = {2200--2209},
}
```