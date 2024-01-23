---
annotations_creators:
- expert-generated
language_creators:
- expert-generated
- found
language:
- code
- en
license:
- gpl-3.0
multilinguality:
- translation
size_categories:
- unknown
source_datasets:
- original
task_categories:
- text-generation
task_ids:
- language-modeling
paperswithcode_id: shellcode-ia32
---

# Shellcode_IA32

___Shellcode_IA32___ is a dataset containing _20_ years of shellcodes from a variety of sources is the largest collection of shellcodes in assembly available to date.

This dataset consists of 3,200 examples of instructions in assembly language for _IA-32_ (the 32-bit version of the x86 Intel Architecture) from publicly available security exploits. We collected assembly programs used to generate shellcode from [exploit-db](https://www.exploit-db.com/shellcodes?platform=linux_x86) and from [shell-storm](http://shell-storm.org/shellcode/).
We enriched the dataset by adding examples of assembly programs for the _IA-32_ architecture from popular tutorials and books. This allowed us to understand how different authors and assembly experts comment and, thus, how to deal with the ambiguity of natural language in this specific context. Our dataset consists of 10% of instructions collected from books and guidelines, and the rest from real shellcodes. 

Our focus is on Linux, the most common OS for security-critical network services. Accordingly, we added assembly instructions written with _Netwide Assembler_ (NASM) for Linux.

Each line of _Shellcode\_IA32_ dataset represents a snippet - intent pair. The _snippet_ is a line or a combination of multiple lines of assembly code, built by following the NASM syntax. The _intent_ is a comment in the English language.

Further statistics on the dataset and a set of preliminary experiments performed with a neural machine translation (NMT) model are described in the following paper: [Shellcode_IA32: A Dataset for Automatic Shellcode Generation](https://arxiv.org/abs/2104.13100).


**Note**: This work was done in collaboration with the [DESSERT Lab](http://www.dessert.unina.it/).

The dataset is also hosted on the [DESSERT Lab Github](https://github.com/dessertlab/Shellcode_IA32).


Please consider citing our work: 
```
@inproceedings{liguori-etal-2021-shellcode,
    title = "{S}hellcode{\_}{IA}32: A Dataset for Automatic Shellcode Generation",
    author = "Liguori, Pietro  and
      Al-Hossami, Erfan  and
      Cotroneo, Domenico  and
      Natella, Roberto  and
      Cukic, Bojan  and
      Shaikh, Samira",
    booktitle = "Proceedings of the 1st Workshop on Natural Language Processing for Programming (NLP4Prog 2021)",
    month = aug,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.nlp4prog-1.7",
    doi = "10.18653/v1/2021.nlp4prog-1.7",
    pages = "58--64",
    abstract = "We take the first step to address the task of automatically generating shellcodes, i.e., small pieces of code used as a payload in the exploitation of a software vulnerability, starting from natural language comments. We assemble and release a novel dataset (Shellcode{\_}IA32), consisting of challenging but common assembly instructions with their natural language descriptions. We experiment with standard methods in neural machine translation (NMT) to establish baseline performance levels on this task.",
}
```
