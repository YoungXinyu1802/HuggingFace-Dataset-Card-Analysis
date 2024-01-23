---
license: cc-by-sa-4.0
task_categories:
- text-classification
language:
- en
pretty_name: Media Bias Identification Benchmark
configs:
  - cognitive-bias
  - fake-news
  - gender-bias
  - hate-speech
  - linguistic-bias
  - political-bias
  - racial-bias
  - text-level-bias
---

# Dataset Card for Media-Bias-Identification-Benchmark

## Table of Contents
- [Dataset Card for Media-Bias-Identification-Benchmark](#dataset-card-for-mbib)
  - [Table of Contents](#table-of-contents)
  - [Dataset Description](#dataset-description)
    - [Dataset Summary](#dataset-summary)
    - [Tasks and Information](#tasks-and-information)
    - [Baseline](#baseline)
    - [Languages](#languages)
  - [Dataset Structure](#dataset-structure)
    - [Data Instances](#data-instances)
      - [cognitive-bias](#cognitive-bias)
    - [Data Fields](#data-fields)
  - [Considerations for Using the Data](#considerations-for-using-the-data)
    - [Social Impact of Dataset](#social-impact-of-dataset)
    - [Discussion of Biases](#discussion-of-biases)
    - [Other Known Limitations](#other-known-limitations)
    - [Citation Information](#citation-information)
    - [Contributions](#contributions)

## Dataset Description

- **Homepage:** https://github.com/Media-Bias-Group/Media-Bias-Identification-Benchmark
- **Repository:** https://github.com/Media-Bias-Group/Media-Bias-Identification-Benchmark
- **Paper:** TODO
- **Point of Contact:** [Martin Wessel](mailto:martin.wessel@uni-konstanz.de)




### Baseline


<table>
        <tr><td><b>Task</b></td><td><b>Model</b></td><td><b>Micro F1</b></td><td><b>Macro F1</b></td></tr>

<td>cognitive-bias</td> <td> ConvBERT/ConvBERT</td> <td>0.7126</td> <td> 0.7664</td></tr>
<td>fake-news</td> <td>Bart/RoBERTa-T</td> <td>0.6811</td> <td> 0.7533</td> </tr>
<td>gender-bias</td> <td> RoBERTa-T/ELECTRA</td> <td>0.8334</td> <td>0.8211</td> </tr>
<td>hate-speech</td> <td>RoBERTA-T/Bart</td> <td>0.8897</td> <td> 0.7310</td> </tr>
<td>linguistic-bias</td> <td> ConvBERT/Bart </td> <td> 0.7044 </td> <td> 0.4995 </td> </tr>
<td>political-bias</td> <td> ConvBERT/ConvBERT </td> <td> 0.7041 </td> <td> 0.7110 </td> </tr>
<td>racial-bias</td> <td> ConvBERT/ELECTRA </td> <td> 0.8772 </td> <td> 0.6170 </td> </tr>
<td>text-leve-bias</td> <td> ConvBERT/ConvBERT </td> <td> 0.7697</td> <td> 0.7532 </td> </tr>
</table>




### Languages

All datasets are in English

## Dataset Structure

### Data Instances

#### cognitive-bias

An example of one training instance looks as follows. 
```json
{
  "text": "A defense bill includes language that would require military hospitals to provide abortions on demand",
  "label": 1
}
```




### Data Fields

- `text`: a sentence from various sources (eg., news articles, twitter, other social media).
- `label`: binary indicator of bias (0 = unbiased, 1 = biased)




## Considerations for Using the Data

### Social Impact of Dataset
We believe that MBIB offers a new common ground
for research in the domain, especially given the rising amount of
(research) attention directed toward media bias





### Citation Information

```
@inproceedings{
    title = {Introducing MBIB - the first Media Bias Identification Benchmark Task and Dataset Collection},
    author = {Wessel, Martin and Spinde, Timo and Horych, Tomáš and Ruas, Terry and Aizawa, Akiko and Gipp, Bela},
    year = {2023},
    note = {[in review]}
}
```
