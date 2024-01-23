---
license: apache-2.0
---
https://github.com/entangledloops/slidingpuzzle/

Each JSON file contains a list of board and solution pairs. These are the optimal solutions as found through Breadth-First Search.
For example, here is a random snapshot from inside `examples_3x3.json`:
```
...
[[[8, 4, 5], [3, 7, 1], [0, 2, 6]], [2, 7, 3, 8, 4, 3, 8, 2, 7, 8, 1, 5, 3, 1, 2, 4, 1, 2, 5, 6]], 
[[[8, 4, 5], [3, 7, 1], [2, 6, 0]], [6, 7, 3, 8, 4, 3, 8, 2, 7, 8, 1, 5, 3, 1, 2, 4, 1, 2, 5, 6]], 
[[[8, 4, 5], [2, 3, 1], [7, 6, 0]], [6, 7, 2, 8, 4, 3, 8, 2, 7, 8, 1, 5, 3, 1, 2, 4, 1, 2, 5, 6]],
...
```
The first example represents the following board,
```
8 4 5
3 7 1
  2 6
```
where 0 indicates the blank. The solution is to first move the 2, then 7, 3, 8, etc.
The final solved board state would be:
```
1 2 3
4 5 6
7 8
```
To use the data, it can be parsed:
```python
import json
with open("examples_3x3.json", "rt") as fp:
    db = json.load(fp)

board, solution = db[0]  # inspect first example
print(board, solution)    
```