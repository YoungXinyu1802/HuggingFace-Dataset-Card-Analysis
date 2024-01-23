**Stats about bigcode dataset:**

* Permissive licenses only :


 |Language |Raw (only exact dedup)  | Near dedup | Near dedup + content filters| Near dedup + more near-dedup (1)|Near dedup + comments filter (1)| Near dedup + more near-dedup + comments(1)|
|-------|--------|-------|--------|--------|--------|--------|
|Python | 200 GB| [80 GB](https://huggingface.co/datasets/bigcode/the-stack-dedup-pjj/tree/v1.1.a1) | [75.61 GB](https://huggingface.co/datasets/bigcode/the-stack-pjjs-no-pii-filtered) | [61.97 GB](https://huggingface.co/datasets/bigcode/stack-dedup-alt-filter-no-pii) | [65 GB](https://huggingface.co/datasets/bigcode/the-stack-comments-filter) | (?) less than 60 |
|Java | 266 GB |112 GB |110 GB | 88 GB | 92 GB |(?) less than 80 |
|JavaScript | 496 GB | 166 GB |83 GB| 65 GB | 75 GB |(?) less than 60|
|C | 255 GB | 75 GB |73 GB (2)| - | - |-|
|C++ | 215 GB | 65 GB |61 GB (2)|- | - |-|

* Non permissive data, the number are higher than the  e.g 240GB of python I mentionned (it was on old dump)
|Language |Raw (only exact dedup)  | Near dedup |
|-------|--------|-------|
| Python (3)| 737 GB | - |
|Java | 1.3 TB | - |
|JavaScript | 5.8 TB | -|
|C | 1.64 TB | - |
|C++ | 644 GB | - |

(1) all these runs have content filtering, notice that it removes a lot of data from JavaScript (you could try filtering with less strict thresholds, the [script](https://github.com/bigcode-project/bigcode-dataset/tree/main/preprocessing) is very easy to run)

(2) I don't have the data but I found these numbers from an old run on the forst version of The Stack (it uses the same content filtering thresholds as for python, java and js)

(3) this went through content filters