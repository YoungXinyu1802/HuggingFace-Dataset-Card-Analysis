---
task_categories:
- text-classification
- token-classification
- feature-extraction
pretty_name: Movie-Reviews
size_categories:
- 10K<n<100K
---
# IMDB Movie Reviews 

![movie_reivews](images/movie_reviews.jpg)

This is a dataset for binary sentiment classification containing substantially huge data. This dataset contains a set of 50,000 highly polar movie reviews for training models for text classification tasks. 

The dataset is downloaded from 

https://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz

This data is processed and splitted into training and test datasets (0.2% test split). Training dataset contains 40000 reviews and test dataset contains 10000 reviews.

Equal distribution among the labels in both training and test dataset. in training dataset, there are 20000 records for both positive and negative classes. In test dataset, there are 5000 records both the labels.



### Citation Information

```
@InProceedings{maas-EtAl:2011:ACL-HLT2011,
  author    = {Maas, Andrew L.  and  Daly, Raymond E.  and  Pham, Peter T.  and  Huang, Dan  and  Ng, Andrew Y.  and  Potts, Christopher},
  title     = {Learning Word Vectors for Sentiment Analysis},
  booktitle = {Proceedings of the 49th Annual Meeting of the Association for Computational Linguistics: Human Language Technologies},
  month     = {June},
  year      = {2011},
  address   = {Portland, Oregon, USA},
  publisher = {Association for Computational Linguistics},
  pages     = {142--150},
  url       = {http://www.aclweb.org/anthology/P11-1015}
}
```