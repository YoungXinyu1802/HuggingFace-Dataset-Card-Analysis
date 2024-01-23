This dataset only consists of linearized underlying data table of charts and their corresponding summaries. 

Model that use this dataset: https://huggingface.co/saadob12/t5_C2T_big
## Created By: 
Kanthara, S., Leong, R. T. K., Lin, X., Masry, A., Thakkar, M., Hoque, E., & Joty, S. (2022). Chart-to-Text: A Large-Scale Benchmark for Chart Summarization. arXiv preprint arXiv:2203.06486.

**Paper**: https://arxiv.org/abs/2203.06486

**Orignal github repo**: https://github.com/vis-nlp/Chart-to-text

# Abstract from the Paper
Charts are commonly used for exploring data
and communicating insights. Generating nat-
ural language summaries from charts can be
very helpful for people in inferring key in-
sights that would otherwise require a lot of
cognitive and perceptual efforts. We present
Chart-to-text, a large-scale benchmark with
two datasets and a total of 44,096 charts cover-
ing a wide range of topics and chart types. We
explain the dataset construction process and
analyze the datasets. We also introduce a num-
ber of state-of-the-art neural models as base-
lines that utilize image captioning and data-to-
text generation techniques to tackle two prob-
lem variations: one assumes the underlying
data table of the chart is available while the
other needs to extract data from chart images.
Our analysis with automatic and human eval-
uation shows that while our best models usu-
ally generate fluent summaries and yield rea-
sonable BLEU scores, they also suffer from
hallucinations and factual errors as well as dif-
ficulties in correctly explaining complex pat-
terns and trends in charts.

### Note
The original paper published two sub-datasets one collected from statista and the other from pew. The dataset upload here is from statista. Images can be downloaded from the github repo mentioned above. 

# Langugage

The data is in english and the summaries are in english. 

# Dataset split
| train | valid  | test |
|:---:|:---:| :---:|
| 24367  | 5222  | 5222 |


**Name of Contributor:** Saad Obaid ul Islam 