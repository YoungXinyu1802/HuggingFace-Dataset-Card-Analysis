---
annotations_creators:
- other
- clicks
language_creators:
- other
language:
- en-US
license:
- apache-2.0
multilinguality:
- monolingual
pretty_name: tripclick-training
size_categories:
- unknown
source_datasets: [tripclick]
task_categories:
- text-retrieval
task_ids:
- document-retrieval
---

# TripClick Baselines with Improved Training Data

*Establishing Strong Baselines for TripClick Health Retrieval* Sebastian Hofstätter, Sophia Althammer, Mete Sertkan and Allan Hanbury

https://arxiv.org/abs/2201.00365

**tl;dr** We create strong re-ranking and dense retrieval baselines (BERT<sub>CAT</sub>, BERT<sub>DOT</sub>, ColBERT, and TK) for TripClick (health ad-hoc retrieval). We improve the – originally too noisy – training data with a simple negative sampling policy. We achieve large gains over BM25 in the re-ranking and retrieval setting on TripClick, which were not achieved with the original baselines. We publish the improved training files for everyone to use.

If you have any questions, suggestions, or want to collaborate please don't hesitate to get in contact with us via [Twitter](https://twitter.com/s_hofstaetter) or mail to s.hofstaetter@tuwien.ac.at

**Please cite our work as:**
````
@misc{hofstaetter2022tripclick,
      title={Establishing Strong Baselines for TripClick Health Retrieval}, 
      author={Sebastian Hofst{\"a}tter and Sophia Althammer and Mete Sertkan and Allan Hanbury},
      year={2022},
      eprint={2201.00365},
      archivePrefix={arXiv},
      primaryClass={cs.IR}
}
````

## Published Training Files

We publish the improved training files without the text content instead using the ids from TripClick (with permission from the TripClick owners); for the text content please get the full TripClick dataset from [the TripClick Github page](https://github.com/tripdatabase/tripclick). 

Our training file **improved_tripclick_train_triple-ids.tsv** has the format ``query_id pos_passage_id neg_passage_id`` (with tab separation).

----

For more information on how to use the training files see: https://github.com/sebastian-hofstaetter/tripclick