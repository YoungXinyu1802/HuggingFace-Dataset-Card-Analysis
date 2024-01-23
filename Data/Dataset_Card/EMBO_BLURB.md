---
annotations_creators:
- expert-generated
language_creators:
- expert-generated
language:
- en
license: apache-2.0
multilinguality:
- monolingual
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories:
- question-answering
- token-classification
- sentence-similarity
- text-classification
task_ids:
- closed-domain-qa
- named-entity-recognition
- parsing
- semantic-similarity-scoring
- text-scoring
- topic-classification
pretty_name: BLURB (Biomedical Language Understanding and Reasoning Benchmark.)
---

# Dataset Card for BLURB

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Homepage:** https://microsoft.github.io/BLURB/index.html
- **Paper:** [Domain-Specific Language Model Pretraining for Biomedical Natural Language Processing](https://arxiv.org/pdf/2007.15779.pdf)
- **Leaderboard:** https://microsoft.github.io/BLURB/leaderboard.html
- **Point of Contact:**

### Dataset Summary

BLURB is a collection of resources for biomedical natural language processing. In general domains, such as newswire and the Web, comprehensive benchmarks and leaderboards such as GLUE have greatly accelerated progress in open-domain NLP. In biomedicine, however, such resources are ostensibly scarce. In the past, there have been a plethora of shared tasks in biomedical NLP, such as BioCreative, BioNLP Shared Tasks, SemEval, and BioASQ, to name just a few. These efforts have played a significant role in fueling interest and progress by the research community, but they typically focus on individual tasks. The advent of neural language models, such as BERT provides a unifying foundation to leverage transfer learning from unlabeled text to support a wide range of NLP applications. To accelerate progress in biomedical pretraining strategies and task-specific methods, it is thus imperative to create a broad-coverage benchmark encompassing diverse biomedical tasks.

Inspired by prior efforts toward this direction (e.g., BLUE), we have created BLURB (short for Biomedical Language Understanding and Reasoning Benchmark). BLURB comprises of a comprehensive benchmark for PubMed-based biomedical NLP applications, as well as a leaderboard for tracking progress by the community. BLURB includes thirteen publicly available datasets in six diverse tasks. To avoid placing undue emphasis on tasks with many available datasets, such as named entity recognition (NER), BLURB reports the macro average across all tasks as the main score. The BLURB leaderboard is model-agnostic. Any system capable of producing the test predictions using the same training and development data can participate. The main goal of BLURB is to lower the entry barrier in biomedical NLP and help accelerate progress in this vitally important field for positive societal and human impact.


#### BC5-chem
The corpus consists of three separate sets of 
articles with diseases, chemicals and their relations annotated. 
The training (500 articles) and development (500 articles) sets 
were released to task participants in advance to support text-mining 
method development. The test set (500 articles) was used for final 
system performance evaluation.
                  
- **Homepage:** https://biocreative.bioinformatics.udel.edu/resources/corpora/biocreative-v-cdr-corpus 
- **Repository:** [NER GitHub repo by @GamalC](https://github.com/cambridgeltl/MTL-Bioinformatics-2016/raw/master/data/)
- **Paper:** [BioCreative V CDR task corpus: a resource for chemical disease relation extraction](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4860626/)

#### BC5-disease
The corpus consists of three separate sets of 
articles with diseases, chemicals and their relations annotated. 
The training (500 articles) and development (500 articles) sets 
were released to task participants in advance to support text-mining 
method development. The test set (500 articles) was used for final 
system performance evaluation.
                  
- **Homepage:** https://biocreative.bioinformatics.udel.edu/resources/corpora/biocreative-v-cdr-corpus 
- **Repository:** [NER GitHub repo by @GamalC](https://github.com/cambridgeltl/MTL-Bioinformatics-2016/raw/master/data/)
- **Paper:** [BioCreative V CDR task corpus: a resource for chemical disease relation extraction](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4860626/)

#### BC2GM 
The BioCreative II Gene Mention task.
The training corpus for the current task consists mainly of 
the training and testing corpora (text collections) from the 
BCI task, and the testing corpus for the current task 
consists of an additional 5,000 sentences that were held 
'in reserve' from the previous task.
In the current corpus, tokenization is not provided; 
instead participants are asked to identify a gene mention 
in a sentence by giving its start and end characters. 
As before, the training set consists of a set of sentences, 
and for each sentence a set of gene mentions 
(GENE annotations).
- **Homepage:** https://biocreative.bioinformatics.udel.edu/tasks/biocreative-ii/task-1a-gene-mention-tagging/
- **Repository:** [NER GitHub repo by @GamalC](https://github.com/cambridgeltl/MTL-Bioinformatics-2016/raw/master/data/)
- **Paper:** [verview of BioCreative II gene mention recognition](https://link.springer.com/article/10.1186/gb-2008-9-s2-s2)

#### NCBI Disease

The NCBI disease corpus is fully annotated at the mention 
  and concept level to serve as a research resource for the biomedical natural 
  language processing community.
      Corpus Characteristics
      ----------------------
      * 793 PubMed abstracts
      * 6,892 disease mentions
      * 790 unique disease concepts
      * Medical Subject Headings (MeSH®)
      * Online Mendelian Inheritance in Man (OMIM®)
      * 91% of the mentions map to a single disease concept
        **divided into training, developing and testing sets.
      Corpus Annotation
      * Fourteen annotators
      * Two-annotators per document (randomly paired)
      * Three annotation phases
      * Checked for corpus-wide consistency of annotations                    
- **Homepage:** https://www.ncbi.nlm.nih.gov/CBBresearch/Dogan/DISEASE/
- **Repository:** [NER GitHub repo by @GamalC](https://github.com/cambridgeltl/MTL-Bioinformatics-2016/raw/master/data/)
- **Paper:** [NCBI disease corpus: a resource for disease name recognition and concept normalization](https://pubmed.ncbi.nlm.nih.gov/24393765/)

#### JNLPBA
The BioNLP / JNLPBA Shared Task 2004 involves the identification 
and classification of technical terms referring to concepts of interest to 
biologists in the domain of molecular biology. The task was organized by GENIA 
Project based on the annotations of the GENIA Term corpus (version 3.02). 
Corpus format: The JNLPBA corpus is distributed in IOB format, with each line 
containing a single token and its tag, separated by a tab character. 
Sentences are separated by blank lines.
- **Homepage: ** http://www.geniaproject.org/shared-tasks/bionlp-jnlpba-shared-task-2004
- **Repository:** [NER GitHub repo by @GamalC](https://github.com/cambridgeltl/MTL-Bioinformatics-2016/raw/master/data/)
- **Paper: ** [Introduction to the Bio-entity Recognition Task at JNLPBA](https://aclanthology.org/W04-1213)

#### EBM PICO
- **Homepage:**
- **Repository:**
- **Paper:**
- **Leaderboard:**

#### ChemProt
- **Homepage:**
- **Repository:**
- **Paper:**

#### DDI
- **Homepage:**
- **Repository:**
- **Paper:**

#### GAD
- **Homepage:**
- **Repository:**
- **Paper:**

#### BIOSSES 

BIOSSES is a benchmark dataset for biomedical sentence similarity estimation. The dataset comprises 100 sentence pairs, in which each sentence was selected from the [TAC (Text Analysis Conference) Biomedical Summarization Track Training Dataset](https://tac.nist.gov/2014/BiomedSumm/) containing articles from the biomedical domain. The sentence pairs in BIOSSES were selected from citing sentences, i.e. sentences that have a citation to a reference article. 
The sentence pairs were evaluated by five different human experts that judged their similarity and gave scores ranging from 0 (no relation) to 4 (equivalent). In the original paper the mean of the scores assigned by the five human annotators was taken as the gold standard. The Pearson correlation between the gold standard scores and the scores estimated by the models was used as the evaluation metric. The strength of correlation can be assessed by the general guideline proposed by Evans (1996) as follows:
- very strong: 0.80–1.00
- strong: 0.60–0.79
- moderate: 0.40–0.59
- weak: 0.20–0.39
- very weak: 0.00–0.19

- **Homepage:** https://tabilab.cmpe.boun.edu.tr/BIOSSES/DataSet.html
- **Repository:** https://github.com/gizemsogancioglu/biosses
- **Paper:** [BIOSSES: a semantic sentence similarity estimation system for the biomedical domain](https://academic.oup.com/bioinformatics/article/33/14/i49/3953954)
- **Point of Contact:** [Gizem Soğancıoğlu](gizemsogancioglu@gmail.com) and [Arzucan Özgür](gizemsogancioglu@gmail.com)

#### HoC
- **Homepage:**
- **Repository:**
- **Paper:**
- **Leaderboard:**
- **Point of Contact:**


#### PubMedQA

We introduce PubMedQA, a novel biomedical question answering (QA) dataset collected from PubMed abstracts. The task of PubMedQA is to answer research questions with yes/no/maybe (e.g.: Do preoperative statins reduce atrial fibrillation after coronary artery bypass grafting?) using the corresponding abstracts. PubMedQA has 1k expert-annotated, 61.2k unlabeled and 211.3k artificially generated QA instances. Each PubMedQA instance is composed of (1) a question which is either an existing research article title or derived from one, (2) a context which is the corresponding abstract without its conclusion, (3) a long answer, which is the conclusion of the abstract and, presumably, answers the research question, and (4) a yes/no/maybe answer which summarizes the conclusion. PubMedQA is the first QA dataset where reasoning over biomedical research texts, especially their quantitative contents, is required to answer the questions. Our best performing model, multi-phase fine-tuning of BioBERT with long answer bag-of-word statistics as additional supervision, achieves 68.1% accuracy, compared to single human performance of 78.0% accuracy and majority-baseline of 55.2% accuracy, leaving much room for improvement. PubMedQA is publicly available at this https URL.

- **Homepage:** https://pubmedqa.github.io/
- **Repository:** https://github.com/pubmedqa/pubmedqa
- **Paper:** [PubMedQA: A Dataset for Biomedical Research Question Answering](https://arxiv.org/pdf/1909.06146.pdf)
- **Leaderboard:** [Question answering](https://pubmedqa.github.io/)
- **Point of Contact:**

#### BioASQ

Task 7b will use benchmark datasets containing training and test biomedical questions, in English, along with gold standard (reference) answers. The participants will have to respond to each test question with relevant concepts (from designated terminologies and ontologies), relevant articles (in English, from designated article repositories), relevant snippets (from the relevant articles), relevant RDF triples (from designated ontologies), exact answers (e.g., named entities in the case of factoid questions) and 'ideal' answers (English paragraph-sized summaries). 2747 training questions (that were used as dry-run or test questions in previous year) are already available, along with their gold standard answers (relevant concepts, articles, snippets, exact answers, summaries).

- **Homepage:** http://bioasq.org/
- **Repository:** http://participants-area.bioasq.org/datasets/
- **Paper:** [Automatic semantic classification of scientific literature according to the hallmarks of cancer](https://academic.oup.com/bioinformatics/article/32/3/432/1743783?login=false)

### Supported Tasks and Leaderboards

|  **Dataset** |         **Task**        | **Train** | **Dev** | **Test** | **Evaluation Metrics** | **Added** |
|:------------:|:-----------------------:|:---------:|:-------:|:--------:|:----------------------:|-----------|
|   BC5-chem   |           NER           |    5203   |   5347  |   5385   |     F1 entity-level    |    **Yes**    |
|  BC5-disease |           NER           |    4182   |   4244  |   4424   |     F1 entity-level    |    **Yes**    |
| NCBI-disease |           NER           |    5134   |   787   |    960   |     F1 entity-level    |    **Yes**    |
|     BC2GM    |           NER           |   15197   |   3061  |   6325   |     F1 entity-level    |    **Yes**    |
|    JNLPBA    |           NER           |   46750   |   4551  |   8662   |     F1 entity-level    |    **Yes**    |
|   EBM PICO   |           PICO          |   339167  |  85321  |   16364  |   Macro F1 word-level  |     No    |
|   ChemProt   |   Relation Extraction   |   18035   |  11268  |   15745  |        Micro F1        |     No    |
|      DDI     |   Relation Extraction   |   25296   |   2496  |   5716   |        Micro F1        |     No    |
|      GAD     |   Relation Extraction   |    4261   |   535   |    534   |        Micro F1        |     No    |
|    BIOSSES   |   Sentence Similarity   |     64    |    16   |    20    |         Pearson        |     **Yes**   |
|      HoC     | Document Classification |    1295   |   186   |    371   |    Average Micro F1    |     No    |
|   PubMedQA   |    Question Answering   |    450    |    50   |    500   |        Accuracy        |     **Yes**   |
|    BioASQ    |    Question Answering   |    670    |    75   |    140   |        Accuracy        |     No    |

Datasets used in the BLURB biomedical NLP benchmark. The Train, Dev, and test splits might not be exactly identical to those proposed in BLURB.
This is something to be checked.

### Languages

English from biomedical texts

## Dataset Structure

### Data Instances

* **NER**
  ```json
  {
    'id': 0,
    'tokens': [ "DPP6", "as", "a", "candidate", "gene", "for", "neuroleptic", "-", "induced", "tardive", "dyskinesia", "." ]
    'ner_tags': [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
  }
  ```
* **PICO**
  ```json
  {
    'TBD'
  }
  ```
* **Relation Extraction**
  ```json
  {
    'TBD'
  }
  ```

* **Sentence Similarity**
  
  ```json
  {'sentence 1': 'Here, looking for agents that could specifically kill KRAS mutant cells, they found that knockdown of GATA2 was synthetically lethal with KRAS mutation'
   'sentence 2': 'Not surprisingly, GATA2 knockdown in KRAS mutant cells resulted in a striking reduction of active GTP-bound RHO proteins, including the downstream ROCK kinase'
   'score': 2.2}
  ```
  
* **Document Classification**
  ```json
  {
    'TBD'
  }
  ```
* **Question Answering**

  * PubMedQA
  ```json
    {'context': {'contexts': ['Programmed cell death (PCD) is the regulated death of cells within an organism. The lace plant (Aponogeton madagascariensis) produces perforations in its leaves through PCD. The leaves of the plant consist of a latticework of longitudinal and transverse veins enclosing areoles. PCD occurs in the cells at the center of these areoles and progresses outwards, stopping approximately five cells from the vasculature. The role of mitochondria during PCD has been recognized in animals; however, it has been less studied during PCD in plants.',
       'The following paper elucidates the role of mitochondrial dynamics during developmentally regulated PCD in vivo in A. madagascariensis. A single areole within a window stage leaf (PCD is occurring) was divided into three areas based on the progression of PCD; cells that will not undergo PCD (NPCD), cells in early stages of PCD (EPCD), and cells in late stages of PCD (LPCD). Window stage leaves were stained with the mitochondrial dye MitoTracker Red CMXRos and examined. Mitochondrial dynamics were delineated into four categories (M1-M4) based on characteristics including distribution, motility, and membrane potential (ΔΨm). A TUNEL assay showed fragmented nDNA in a gradient over these mitochondrial stages. Chloroplasts and transvacuolar strands were also examined using live cell imaging. The possible importance of mitochondrial permeability transition pore (PTP) formation during PCD was indirectly examined via in vivo cyclosporine A (CsA) treatment. This treatment resulted in lace plant leaves with a significantly lower number of perforations compared to controls, and that displayed mitochondrial dynamics similar to that of non-PCD cells.'],
      'labels': ['BACKGROUND', 'RESULTS'],
      'meshes': ['Alismataceae',
       'Apoptosis',
       'Cell Differentiation',
       'Mitochondria',
       'Plant Leaves'],
      'reasoning_free_pred': ['y', 'e', 's'],
      'reasoning_required_pred': ['y', 'e', 's']},
     'final_decision': 'yes',
     'long_answer': 'Results depicted mitochondrial dynamics in vivo as PCD progresses within the lace plant, and highlight the correlation of this organelle with other organelles during developmental PCD. To the best of our knowledge, this is the first report of mitochondria and chloroplasts moving on transvacuolar strands to form a ring structure surrounding the nucleus during developmental PCD. Also, for the first time, we have shown the feasibility for the use of CsA in a whole plant system. Overall, our findings implicate the mitochondria as playing a critical and early role in developmentally regulated PCD in the lace plant.',
     'pubid': 21645374,
     'question': 'Do mitochondria play a role in remodelling lace plant leaves during programmed cell death?'}
  ```


### Data Fields

* **NER**
  * `id`: string
  * `ner_tags`: Sequence[ClassLabel]
  * `tokens`: Sequence[String]
* **PICO**
  * To be added
* **Relation Extraction**
  * To be added
* **Sentence Similarity**
  * `sentence 1`: string
  * `sentence 2`: string
  * `score`: float ranging from 0 (no relation) to 4 (equivalent)
* **Document Classification**
  * To be added
* **Question Answering**
  * PubMedQA
    * `pubid`: integer
    * `question`: string
    * `context`: sequence of strings [`contexts`, `labels`, `meshes`, `reasoning_required_pred`, `reasoning_free_pred`]
    * `long_answer`: string
    * `final_decision`: string

### Data Splits

Shown in the table of supported tasks.

## Dataset Creation

### Curation Rationale

* BC5-chem
* BC5-disease
* BC2GM 
* JNLPBA
* EBM PICO
* ChemProt
* DDI
* GAD
* BIOSSES
* HoC
* PubMedQA
* BioASQ

### Source Data

[More Information Needed]

### Annotations

All the datasets have been obtained and annotated by experts in the biomedical domain. Check the different citations for further details.

#### Annotation process

* BC5-chem
* BC5-disease
* BC2GM 
* JNLPBA
* EBM PICO
* ChemProt
* DDI
* GAD
* BIOSSES - The sentence pairs were evaluated by five different human experts that judged their similarity and gave scores ranging from 0 (no relation) to 4 (equivalent). The score range was described based on the guidelines of SemEval 2012 Task 6 on STS (Agirre et al., 2012). Besides the annotation instructions, example sentences from the biomedical literature were provided to the annotators for each of the similarity degrees. 
* HoC
* PubMedQA
* BioASQ

### Dataset Curators

All the datasets have been obtained and annotated by experts in thebiomedical domain. Check the different citations for further details.

### Licensing Information

* BC5-chem
* BC5-disease
* BC2GM 
* JNLPBA
* EBM PICO
* ChemProt
* DDI
* GAD
* BIOSSES - BIOSSES is made available under the terms of [The GNU Common Public License v.3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).
* HoC
* PubMedQA - MIT License Copyright (c) 2019 pubmedqa
* BioASQ

### Citation Information

* BC5-chem & BC5-disease
 ```latex
 @article{article,
            author = {Li, Jiao and Sun, Yueping and Johnson, Robin and Sciaky, Daniela and Wei, Chih-Hsuan and Leaman, Robert and Davis, Allan Peter and Mattingly, Carolyn and Wiegers, Thomas and lu, Zhiyong},
            year = {2016},
            month = {05},
            pages = {baw068},
            title = {BioCreative V CDR task corpus: a resource for chemical disease relation extraction},
            volume = {2016},
            journal = {Database},
            doi = {10.1093/database/baw068}
            }
  ```
* BC2GM 
 ```latex
  @article{article,
              author = {Smith, Larry and Tanabe, Lorraine and Ando, Rie and Kuo, Cheng-Ju and Chung, I-Fang and Hsu, Chun-Nan and Lin, Yu-Shi and Klinger, Roman and Friedrich, Christoph and Ganchev, Kuzman and Torii, Manabu and Liu, Hongfang and Haddow, Barry and Struble, Craig and Povinelli, Richard and Vlachos, Andreas and Baumgartner Jr, William and Hunter, Lawrence and Carpenter, Bob and Wilbur, W.},
              year = {2008},
              month = {09},
              pages = {S2},
              title = {Overview of BioCreative II gene mention recognition},
              volume = {9 Suppl 2},
              journal = {Genome biology},
              doi = {10.1186/gb-2008-9-s2-s2}
              }
 ```
* JNLPBA
 ```latex
    @inproceedings{collier-kim-2004-introduction,
                title = "Introduction to the Bio-entity Recognition Task at {JNLPBA}",
                author = "Collier, Nigel  and
                  Kim, Jin-Dong",
                booktitle = "Proceedings of the International Joint Workshop on Natural Language Processing in Biomedicine and its Applications ({NLPBA}/{B}io{NLP})",
                month = aug # " 28th and 29th",
                year = "2004",
                address = "Geneva, Switzerland",
                publisher = "COLING",
                url = "https://aclanthology.org/W04-1213",
                pages = "73--78",
                }
     ```
* NCBI Disiease
 ```latex
    @article{10.5555/2772763.2772800,
                author = {Dogan, Rezarta Islamaj and Leaman, Robert and Lu, Zhiyong},
                title = {NCBI Disease Corpus},
                year = {2014},
                issue_date = {February 2014},
                publisher = {Elsevier Science},
                address = {San Diego, CA, USA},
                volume = {47},
                number = {C},
                issn = {1532-0464},
                abstract = {Graphical abstractDisplay Omitted NCBI disease corpus is built as a gold-standard resource for disease recognition.793 PubMed abstracts are annotated with disease mentions and concepts (MeSH/OMIM).14 Annotators produced high consistency level and inter-annotator agreement.Normalization benchmark results demonstrate the utility of the corpus.The corpus is publicly available to the community. Information encoded in natural language in biomedical literature publications is only useful if efficient and reliable ways of accessing and analyzing that information are available. Natural language processing and text mining tools are therefore essential for extracting valuable information, however, the development of powerful, highly effective tools to automatically detect central biomedical concepts such as diseases is conditional on the availability of annotated corpora.This paper presents the disease name and concept annotations of the NCBI disease corpus, a collection of 793 PubMed abstracts fully annotated at the mention and concept level to serve as a research resource for the biomedical natural language processing community. Each PubMed abstract was manually annotated by two annotators with disease mentions and their corresponding concepts in Medical Subject Headings (MeSH ) or Online Mendelian Inheritance in Man (OMIM ). Manual curation was performed using PubTator, which allowed the use of pre-annotations as a pre-step to manual annotations. Fourteen annotators were randomly paired and differing annotations were discussed for reaching a consensus in two annotation phases. In this setting, a high inter-annotator agreement was observed. Finally, all results were checked against annotations of the rest of the corpus to assure corpus-wide consistency.The public release of the NCBI disease corpus contains 6892 disease mentions, which are mapped to 790 unique disease concepts. Of these, 88% link to a MeSH identifier, while the rest contain an OMIM identifier. We were able to link 91% of the mentions to a single disease concept, while the rest are described as a combination of concepts. In order to help researchers use the corpus to design and test disease identification methods, we have prepared the corpus as training, testing and development sets. To demonstrate its utility, we conducted a benchmarking experiment where we compared three different knowledge-based disease normalization methods with a best performance in F-measure of 63.7%. These results show that the NCBI disease corpus has the potential to significantly improve the state-of-the-art in disease name recognition and normalization research, by providing a high-quality gold standard thus enabling the development of machine-learning based approaches for such tasks.The NCBI disease corpus, guidelines and other associated resources are available at: http://www.ncbi.nlm.nih.gov/CBBresearch/Dogan/DISEASE/.},
                journal = {J. of Biomedical Informatics},
                month = {feb},
                pages = {1–10},
                numpages = {10}}
     ```
* EBM PICO
* ChemProt
* DDI
* GAD
* BIOSSES 
 ```latex
    @article{souganciouglu2017biosses,
          title={BIOSSES: a semantic sentence similarity estimation system for the biomedical domain},
          author={So{\u{g}}anc{\i}o{\u{g}}lu, Gizem and {\"O}zt{\"u}rk, Hakime and {\"O}zg{\"u}r, Arzucan},
          journal={Bioinformatics},
          volume={33},
          number={14},
          pages={i49--i58},
          year={2017},
          publisher={Oxford University Press}
        }

   ```
* HoC
* PubMedQA 
 ```latex
  @inproceedings{jin2019pubmedqa,
                          title={PubMedQA: A Dataset for Biomedical Research Question Answering},
                          author={Jin, Qiao and Dhingra, Bhuwan and Liu, Zhengping and Cohen, William and Lu, Xinghua},
                          booktitle={Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)},
                          pages={2567--2577},
                          year={2019}
                        }
   ```

* BioASQ
 ```latex
    @article{10.1093/bioinformatics/btv585,
        author = {Baker, Simon and Silins, Ilona and Guo, Yufan and Ali, Imran and Högberg, Johan and Stenius, Ulla and Korhonen, Anna},
        title = "{Automatic semantic classification of scientific literature according to the hallmarks of cancer}",
        journal = {Bioinformatics},
        volume = {32},
        number = {3},
        pages = {432-440},
        year = {2015},
        month = {10},
        abstract = "{Motivation: The hallmarks of cancer have become highly influential in cancer research. They reduce the complexity of cancer into 10 principles (e.g. resisting cell death and sustaining proliferative signaling) that explain the biological capabilities acquired during the development of human tumors. Since new research depends crucially on existing knowledge, technology for semantic classification of scientific literature according to the hallmarks of cancer could greatly support literature review, knowledge discovery and applications in cancer research.Results: We present the first step toward the development of such technology. We introduce a corpus of 1499 PubMed abstracts annotated according to the scientific evidence they provide for the 10 currently known hallmarks of cancer. We use this corpus to train a system that classifies PubMed literature according to the hallmarks. The system uses supervised machine learning and rich features largely based on biomedical text mining. We report good performance in both intrinsic and extrinsic evaluations, demonstrating both the accuracy of the methodology and its potential in supporting practical cancer research. We discuss how this approach could be developed and applied further in the future.Availability and implementation: The corpus of hallmark-annotated PubMed abstracts and the software for classification are available at: http://www.cl.cam.ac.uk/∼sb895/HoC.html .Contact:simon.baker@cl.cam.ac.uk}",
        issn = {1367-4803},
        doi = {10.1093/bioinformatics/btv585},
        url = {https://doi.org/10.1093/bioinformatics/btv585},
        eprint = {https://academic.oup.com/bioinformatics/article-pdf/32/3/432/19568147/btv585.pdf},
    }  
 ```

### Contributions
* This dataset has been uploaded and generated by Dr. Jorge Abreu Vicente.
* Thanks to [@GamalC](https://github.com/GamalC) for uploading the NER datasets to GitHub, from where I got them.
* I am not part of the team that generated BLURB. This dataset is intended to help researchers to usethe BLURB benchmarking for NLP in Biomedical NLP.
* Thanks to [@bwang482](https://github.com/bwang482) for uploading the [BIOSSES dataset](https://github.com/bwang482/datasets/tree/master/datasets/biosses). We forked the [BIOSSES 🤗 dataset](https://huggingface.co/datasets/biosses) to add it to this BLURB benchmark.
* Thank you to [@tuner007](https://github.com/tuner007) for adding this dataset to the 🤗 hub