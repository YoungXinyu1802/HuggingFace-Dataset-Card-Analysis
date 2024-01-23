MNIST dataset adapted to a text-based representation.

Modified images to be ~1/4 the original area.
Done by taking a max pool.

This allows testing interpolation quality for Transformer-VAEs.

System is heavily inspired by Matthew Rayfield's work https://youtu.be/Z9K3cwSL6uM

Works by quantising each MNIST pixel into one of 64 characters.
Every sample has an up & down version to encourage the model to learn rotation invarient features.

Use `.array_to_text(` and `.text_to_array(` methods to test your generated data.

Data format:
- text: (16 x 14 tokens, 224 tokens total): Textual representation of MNIST digit, for example:
```
00 down ! ! ! ! ! ! ! ! ! ! ! ! ! !
01 down ! ! ! ! ! ! ! ! ! ! ! ! ! !
02 down ! ! ! ! ! ! % % C L a ^ ! !
03 down ! ! ! - ` ` ` ` ` Y ` Q ! !
04 down ! ! ! % ` ` ` R ^ ! ! ! ! !
05 down ! ! ! ! $ G ` ! ! ! ! ! ! !
06 down ! ! ! ! ! # ` Y < ! ! ! ! !
07 down ! ! ! ! ! ! 5 ` ` F ! ! ! !
08 down ! ! ! ! ! ! ! % ` ` 1 ! ! !
09 down ! ! ! ! ! ! F ` ` ` ! ! ! !
10 down ! ! ! ! 1 ` ` ` ` 4 ! ! ! !
11 down ! ! L ` ` ` ` 5 ! ! ! ! ! !
12 down ! ! ` ` V B ! ! ! ! ! ! ! !
13 down ! ! ! ! ! ! ! ! ! ! ! ! ! !
```
- label: Just a number with the texts matching label.