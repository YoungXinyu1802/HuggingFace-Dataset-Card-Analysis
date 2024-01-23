---
annotations_creators:
- expert-generated
language_creators:
- crowdsourced
language:
- en
license:
- apache-2.0
multilinguality:
- monolingual
pretty_name: 'babi_nli'
size_categories:
- 1K<n<10K
source_datasets:
- original
task_categories:
- text-classification
task_ids:
- natural-language-inference
tags:
- logical reasoning
- nli
- natural-language-inference
- reasoning
- logic
---

# bAbi_nli

bAbI tasks recasted as natural language inference;

https://colab.research.google.com/drive/1J_RqDSw9iPxJSBvCJu-VRbjXnrEjKVvr?usp=sharing

```bibtex
@article{weston2015towards,
  title={Towards ai-complete question answering: A set of prerequisite toy tasks},
  author={Weston, Jason and Bordes, Antoine and Chopra, Sumit and Rush, Alexander M and Van Merri{\"e}nboer, Bart and Joulin, Armand and Mikolov, Tomas},
  journal={arXiv preprint arXiv:1502.05698},
  year={2015}
}

@inproceedings{sileo-moens-2022-analysis,
    title = "Analysis and Prediction of {NLP} Models via Task Embeddings",
    author = "Sileo, Damien  and
      Moens, Marie-Francine",
    booktitle = "Proceedings of the Thirteenth Language Resources and Evaluation Conference",
    month = jun,
    year = "2022",
    address = "Marseille, France",
    publisher = "European Language Resources Association",
    url = "https://aclanthology.org/2022.lrec-1.67",
    pages = "633--647",
    abstract = "Task embeddings are low-dimensional representations that are trained to capture task properties. In this paper, we propose MetaEval, a collection of 101 NLP tasks. We fit a single transformer to all MetaEval tasks jointly while conditioning it on learned embeddings. The resulting task embeddings enable a novel analysis of the space of tasks. We then show that task aspects can be mapped to task embeddings for new tasks without using any annotated examples. Predicted embeddings can modulate the encoder for zero-shot inference and outperform a zero-shot baseline on GLUE tasks. The provided multitask setup can function as a benchmark for future transfer learning research.",
}

```