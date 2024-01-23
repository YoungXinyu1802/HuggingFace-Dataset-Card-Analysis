First try data generation for toolformer with retrieval, calculator, and calendar tasks. Don't expect too much magic.

C4 en variant was used to generate this data.

How to parse these:
Each item in the dataset comes with three components:
- file_index: index of c4 en streamed file
- text: complete text input to generation
- x_outputs - list of [score, token index, API call, API return]

token index with gpt-j tokenizer.