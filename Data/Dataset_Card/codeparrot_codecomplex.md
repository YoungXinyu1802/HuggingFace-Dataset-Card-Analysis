---
annotations_creators: []
language_creators:
- expert-generated
language:
- code
license:
- apache-2.0
multilinguality:
- monolingual
size_categories:
- unknown
source_datasets: []
task_categories:
- text-generation
task_ids:
- language-modeling
pretty_name: CodeComplex
---

# CodeComplex Dataset

## Dataset Description
[CodeComplex](https://github.com/yonsei-toc/CodeComple) consists of 4,200 Java codes submitted to programming competitions by human programmers and their complexity labels annotated by a group of algorithm experts.

### How to use it

 You can load and iterate through the dataset with the following two lines of code:

```python
from datasets import load_dataset

ds = load_dataset("codeparrot/codecomplex", split="train")
print(next(iter(ds)))
```

## Data Structure
```
DatasetDict({
    train: Dataset({
        features: ['src', 'complexity', 'problem', 'from'],
        num_rows: 4517
    })
})
```

### Data Instances

```python
{'src': 'import java.io.*;\nimport java.math.BigInteger;\nimport java.util.InputMismatchException;...',
 'complexity': 'quadratic',
 'problem': '1179_B. Tolik and His Uncle',
 'from': 'CODEFORCES'}
```

### Data Fields

* src: a string feature, representing the source code in Java.
* complexity: a string feature, giving program complexity.
* problem: a string of the feature, representing the problem name.
* from: a string feature, representing the source of the problem.

complexity filed has 7 classes, where each class has around 500 codes each. The seven classes are constant, linear, quadratic, cubic, log(n), nlog(n) and NP-hard.
### Data Splits

The dataset only contains a train split.

## Dataset Creation
The authors first collected problem and solution codes in Java from CodeForces and they were inspected by experienced human annotators to label each code by their time complexity. After the labelling, they used different programming experts to verify the class of each data that the human annotators assigned. 

## Citation Information
```
@article{JeonBHHK22,
    author  = {Mingi Jeon and Seung-Yeop Baik and Joonghyuk Hahn and Yo-Sub Han and Sang-Ki Ko},
    title   = {{Deep Learning-based Code Complexity Prediction}},
    year    = {2022},
}
```