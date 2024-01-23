---
license: afl-3.0

annotations_creators:
- expert-generated
language:
- cn
language_creators:
- expert-generated
multilinguality:
- monolingual
size_categories:
- 1K<n<10K
---

# Dataset Card for CANLI


### Dataset Summary
[CANLI: The Chinese Causative-Passive Homonymy Disambiguation: an Adversarial Dataset for NLI and a Probing Task](http://www.lrec-conf.org/proceedings/lrec2022/pdf/2022.lrec-1.460.pdf)

The disambiguation of causative-passive homonymy (CPH) is potentially tricky for machines, as the causative and the passive
are not distinguished by the sentences syntactic structure. By transforming CPH disambiguation to a challenging natural
language inference (NLI) task, we present the first Chinese Adversarial NLI challenge set (CANLI). We show that the pretrained
transformer model RoBERTa, fine-tuned on an existing large-scale Chinese NLI benchmark dataset, performs poorly on CANLI.
We also employ Word Sense Disambiguation as a probing task to investigate to what extent the CPH feature is captured in
the models internal representation. We find that the models performance on CANLI does not correspond to its internal
representation of CPH, which is the crucial linguistic ability central to the CANLI dataset. 

### Languages
Chinese Mandarin

# Citation Information

    @inproceedings{xu-markert-2022-chinese,
    title = "The {C}hinese Causative-Passive Homonymy Disambiguation: an adversarial Dataset for {NLI} and a Probing Task",
    author = "Xu, Shanshan  and Markert, Katja",
    booktitle = "Proceedings of the Thirteenth Language Resources and Evaluation Conference",
    month = jun,
    year = "2022",
    address = "Marseille, France",
    publisher = "European Language Resources Association",
    url = "https://aclanthology.org/2022.lrec-1.460",
    pages = "4316--4323",
} 
        