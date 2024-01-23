---
language:
- code
---

# Python State Changes

State changes from the execution of single lines of Python code.
All code was taken from Python HackerRank solutions.

Scraped from my dataset of traced HackerRank solutions. https://www.kaggle.com/frasergreenlee/ran-hackerrank-solutions

```json
{"start": "g = 100; i = 1; l = [100, 100, 0, 0, -100, -100]", "code": "g += l[i]", "end": "g = 200; i = 1; l = [100, 100, 0, 0, -100, -100]"}
{"start": "a = 1; b = 2; d = 4; i = 3; j = 2", "code": "i, j = a + (j - b), b + (d - (i - a))", "end": "a = 1; b = 2; d = 4; i = 1; j = 4"}
{"start": "b = 15", "code": "b = b // 2", "end": "b = 7"}
```

## Get an overview of the dataset from seeing the frequency of different ASTs.
👉 https://observablehq.com/@frasergreenlee/python-lines-dataset#chart