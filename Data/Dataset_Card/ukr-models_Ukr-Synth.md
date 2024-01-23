---
annotations_creators:
- machine-generated
language_creators:
- found
language:
- uk
license:
- mit
multilinguality:
- monolingual
size_categories:
- 1M<n<10M
task_categories:
- token-classification
task_ids:
- named-entity-recognition
- parsing
- part-of-speech
pretty_name: Ukrainian synthetic dataset in conllu format
---
# Dataset Card for Ukr-Synth

## Dataset Description

### Dataset Summary

Large silver standard Ukrainian corpus annotated with morphology tags, syntax trees and PER, LOC, ORG NER-tags.
Represents a subsample of [Leipzig Corpora Collection for Ukrainian Language](https://wortschatz.uni-leipzig.de/en/download/Ukrainian). The source texts are newspaper texts split into sentences and shuffled. The sentrences are annotated using transformer-based models trained using gold standard Ukrainian language datasets.

### Languages

Ukrainian

## Dataset Structure

### Data Splits

|  name   |train  |validation|
|---------|-------:|---------:|
|conll2003|1000000|      10000|

## Dataset Creation

### Source Data

Leipzig Corpora Collection:

D. Goldhahn, T. Eckart & U. Quasthoff: Building Large Monolingual Dictionaries at the Leipzig Corpora Collection: From 100 to 200 Languages.
In: Proceedings of the 8th International Language Resources and Evaluation (LREC'12), 2012

## Additional Information

### Licensing Information

MIT License

Copyright (c) 2022

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.