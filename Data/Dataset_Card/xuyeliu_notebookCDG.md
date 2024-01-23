# notebookCDG

This dataset designed for a recent published paper([HAConvGNN: Hierarchical Attention Based Convolutional Graph Neural Network for Code Documentation Generation in Jupyter Notebooks](https://arxiv.org/abs/2104.01002)) EMNLP'21 Finding. 

You can directly use dataset_notebook.pkl to run the code from the [github repository](https://github.com/xuyeliu/HAConvGNN)

In the repository, we split ground truth documentation split into coms.train, coms.val, and coms.test subsets, following a 8:1:1 ratio. ast_nodes.pkl and ast_edges.pkl are the graph input in this dataset. code.seq is the code sequence input in this dataset. You can also based on the id distribution to split graph and code sequence subsets. 

Inspired by [Wang et al. 2021](https://dl.acm.org/doi/abs/10.1145/3411763.3451617), we decided to utilize the top-voted and well-documented Kaggle notebooks to construct the notebookCDG dataset 

We collected the top 10% highly-voted notebooks from the top 20 popular competitions on Kaggle (e.g. Titanic). We checked the data policy of each of the 20 competitions, none of them has copyright issues. We also contacted the Kaggle administrators to make sure our data collection complies with the platform’s policy.  

In total, we collected 3,944 notebooks as raw data. After data preprocessing, the final dataset contains 2,476 notebooks out of the 3,944 notebooks from the raw data. It has 28,625 code–documentation pairs. The overall code-to-markdown ratio is 2.2195

## Bibliographic Citations

Our work is published at [EMNLP'21 Finding](https://arxiv.org/abs/2104.01002). You can cite: 

```
@misc{liu2021haconvgnn,
      title={HAConvGNN: Hierarchical Attention Based Convolutional Graph Neural Network for Code Documentation Generation in Jupyter Notebooks}, 
      author={Xuye Liu and Dakuo Wang and April Wang and Yufang Hou and Lingfei Wu},
      year={2021},
      eprint={2104.01002},
      archivePrefix={arXiv},
      primaryClass={cs.SE}
}
```

