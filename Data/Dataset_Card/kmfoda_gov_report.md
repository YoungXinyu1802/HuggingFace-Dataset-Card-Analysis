---
dataset_info:
  features:
  - name: source
    dtype: string
  - name: target
    dtype: string
  splits:
  - name: test
    num_bytes: 55710125
    num_examples: 972
  - name: train
    num_bytes: 976584268
    num_examples: 17519
  - name: validation
    num_bytes: 57315603
    num_examples: 973
  download_size: 528419980
  dataset_size: 1089609996
---
# Dataset Card for "gov_report"

## GOV_REPORT
A dataset "consisting of about 19.5k U.S. government reports with expert-written ab- stractive summaries.3 GOVREPORT has two impor- tant features: (1) It contains significantly longer documents (9.4k words) and summaries (553 words) than existing datasets, such as PubMed and arXiv (Cohan et al., 2018) (2) Salient content is spread throughout the documents, as opposed
to cases where summary-worthy words are
more heavily concentrated in specific parts of the
document. These properties make GOVREPORT an
important benchmark for producing long document
summaries with multiple paragraphs. 

## Links

- [Paper](https://aclanthology.org/2021.naacl-main.112.pdf)
- [GitHub repo](http://cloud.datacrunch.io)
- [GDrive Folder](https://drive.google.com/drive/folders/128KyqPTwZ0Si9RV_IX-md2dcHeRTUHkr)

## Citation
```
@article{kryscinski2021booksum,
      title={BookSum: A Collection of Datasets for Long-form Narrative Summarization}, 
      author={Wojciech Kry{\'s}ci{\'n}ski and Nazneen Rajani and Divyansh Agarwal and Caiming Xiong and Dragomir Radev},
      year={2021},
      eprint={2105.08209},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

## License
Licensing info TBD. [Issue raised](https://github.com/luyang-huang96/LongDocSum/issues/7) in main repo to get info on the license from the original authors.