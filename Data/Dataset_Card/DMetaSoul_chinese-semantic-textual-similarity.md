---
license: apache-2.0
---

为了对 like-BERT 预训练模型进行 fine-tune 调优和评测以得到更好的文本表征模，对业界开源的语义相似（STS）、自然语言推理（NLI）、问题匹配（QMC）以及相关性等数据集进行了搜集整理，具体介绍如下：

| 类型           | 数据集                                                       | 简介                                                         | 规模                                               |
| -------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | -------------------------------------------------- |
| **通用领域**   | [OCNLI](https://www.cluebenchmarks.com/introduce.html)       | 原生中文自然语言推理数据集，是第一个非翻译的、使用原生汉语的大型中文自然语言推理数据集。OCNLI为中文语言理解基准测评（CLUE）的一部分。 | **Train**:  50437, **Dev**: 2950                   |
|                | [CMNLI](https://github.com/pluto-junzeng/CNSD)               | 翻译自英文自然语言推理数据集 XNLI 和 MNLI，曾经是中文语言理解基准测评（CLUE）的一部分，现在被 OCNLI 取代。 | **Train**: 391783, **Dev**: 12241                  |
|                | [CSNLI](https://github.com/pluto-junzeng/CNSD)               | 翻译自英文自然语言推理数据集 SNLI。                          | **Train**: 545833, **Dev**: 9314, **Test**: 9176   |
|                | [STS-B-Chinese](https://github.com/pluto-junzeng/CNSD)       | 翻译自英文语义相似数据集 STSbenchmark。                      | **Train**: 5231, **Dev**: 1458, **Test**: 1361     |
|                | [PAWS-X](https://www.luge.ai/#/luge/dataDetail?id=16)        | 释义（含义）匹配数据集，特点是具有高度重叠词汇，重点考察模型对句法结构的理解能力。 | **Train**: 49401, **Dev**: 2000, **Test**: 2000    |
|                | [PKU-Paraphrase-Bank](https://github.com/pkucoli/PKU-Paraphrase-Bank/) | 中文语句复述数据集，也即一句话换种方式描述但语义保持一致。   | 共509832个语句对                                   |
| **问题匹配**   | [LCQMC](https://www.luge.ai/#/luge/dataDetail?id=14)         | 百度知道领域的中文问题匹配大规模数据集，该数据集从百度知道不同领域的用户问题中抽取构建数据。 | **Train**: 238766, **Dev**: 8802, **Test**: 12500  |
|                | [BQCorpus](https://www.luge.ai/#/luge/dataDetail?id=15)      | 银行金融领域的问题匹配数据，包括了从一年的线上银行系统日志里抽取的问题pair对，是目前最大的银行领域问题匹配数据。 | **Train**: 100000, **Dev**: 10000, **Test**: 10000 |
|                | [AFQMC](https://www.cluebenchmarks.com/introduce.html)       | 蚂蚁金服真实金融业务场景中的问题匹配数据集（已脱敏），是中文语言理解基准测评（CLUE）的一部分。 | **Train**: 34334, **Dev**: 4316                    |
|                | [DuQM](https://www.luge.ai/#/luge/dataDetail?id=27)          | 问题匹配评测数据集（label没有公开），属于百度大规模阅读理解数据集（DuReader）的[一部分](https://github.com/baidu/DuReader/tree/master/DuQM)。 | 共50000个语句对                                    |
| **对话和搜索** | [BUSTM: OPPO-xiaobu](https://www.luge.ai/#/luge/dataDetail?id=28) | 通过对闲聊、智能客服、影音娱乐、信息查询等多领域真实用户交互语料进行用户信息脱敏、相似度筛选处理得到，该对话匹配（Dialogue Short Text Matching）数据集主要特点是文本较短、非常口语化、存在文本高度相似而语义不同的难例。 | **Train**: 167173, **Dev**: 10000                  |
|                | [QBQTC](https://github.com/CLUEbenchmark/QBQTC)              | QQ浏览器搜索相关性数据集（QBQTC,QQ Browser Query Title Corpus），是QQ浏览器搜索引擎目前针对大搜场景构建的一个融合了相关性、权威性、内容质量、 时效性等维度标注的学习排序（LTR）数据集，广泛应用在搜索引擎业务场景中。（相关性的含义：0，相关程度差；1，有一定相关性；2，非常相关。） | **Train**: 180000, **Dev**: 20000, **Test**: 5000  |

*以上数据集主要收集整理自[CLUE](https://www.cluebenchmarks.com/introduce.html)（中文语言理解基准评测数据集）、[SimCLUE](https://github.com/CLUEbenchmark/SimCLUE) (整合许多开源文本相似数据集)、[百度千言](https://www.luge.ai/#/)的文本相似度等数据集。*

根据以上收集的数据集构建如下**评测 benchmark**：

| Name                   | Size  | Type          |
| ---------------------- | ----- | ------------- |
| **Chinese-STS-B-dev**  | 1458  | label=0.0~1.0 |
| **Chinese-STS-B-test** | 1361  | label=0.0~1.0 |
| **afqmc-dev**          | 4316  | label=0,1     |
| **lcqmc-dev**          | 8802  | label=0,1     |
| **bqcorpus-dev**       | 10000 | label=0,1     |
| **pawsx_dev**          | 2000  | label=0,1     |
| **oppo-xiaobu-dev**    | 10000 | label=0,1     |

*TODO：目前收集的数据集不论是数量还是多样性都需要进一步扩充以更真实的反映表征模型的效果*
