MNIST dataset adapted to a text-based representation.

This allows testing interpolation quality for Transformer-VAEs.

System is heavily inspired by Matthew Rayfield's work https://youtu.be/Z9K3cwSL6uM

Works by quantising each MNIST pixel into one of 64 characters.
Every sample has an up & down version to encourage the model to learn rotation invarient features.

Use `.array_to_text(` and `.text_to_array(` methods to test your generated data.

Data format:
- text: (30 x 28 tokens, 840 tokens total): Textual representation of MNIST digit, for example:
```
00 down ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !
01 down ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !
02 down ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !
03 down ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !
04 down ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !
05 down ! ! ! ! ! ! ! ! ! ! ! ! ! % % % @ C L ' J a ^ @ ! ! ! !
06 down ! ! ! ! ! ! ! ! ( * 8 G K ` ` ` ` ` Y L ` ] Q 1 ! ! ! !
07 down ! ! ! ! ! ! ! - \ ` ` ` ` ` ` ` ` _ 8 5 5 / * ! ! ! ! !
08 down ! ! ! ! ! ! ! % W ` ` ` ` ` R N ^ ] ! ! ! ! ! ! ! ! ! !
09 down ! ! ! ! ! ! ! ! 5 H ; ` ` T # ! + G ! ! ! ! ! ! ! ! ! !
10 down ! ! ! ! ! ! ! ! ! $ ! G ` 7 ! ! ! ! ! ! ! ! ! ! ! ! ! !
11 down ! ! ! ! ! ! ! ! ! ! ! C ` P ! ! ! ! ! ! ! ! ! ! ! ! ! !
12 down ! ! ! ! ! ! ! ! ! ! ! # P ` 2 ! ! ! ! ! ! ! ! ! ! ! ! !
13 down ! ! ! ! ! ! ! ! ! ! ! ! ) ] Y I < ! ! ! ! ! ! ! ! ! ! !
14 down ! ! ! ! ! ! ! ! ! ! ! ! ! 5 ] ` ` > ' ! ! ! ! ! ! ! ! !
15 down ! ! ! ! ! ! ! ! ! ! ! ! ! ! , O ` ` F ' ! ! ! ! ! ! ! !
16 down ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! % 8 ` ` O ! ! ! ! ! ! ! !
17 down ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! _ ` _ 1 ! ! ! ! ! ! !
18 down ! ! ! ! ! ! ! ! ! ! ! ! ! ! , A N ` ` T ! ! ! ! ! ! ! !
19 down ! ! ! ! ! ! ! ! ! ! ! ! * F Z ` ` ` _ N ! ! ! ! ! ! ! !
20 down ! ! ! ! ! ! ! ! ! ! ' = X ` ` ` ` S 4 ! ! ! ! ! ! ! ! !
21 down ! ! ! ! ! ! ! ! & 1 V ` ` ` ` R 5 ! ! ! ! ! ! ! ! ! ! !
22 down ! ! ! ! ! ! % K W ` ` ` ` Q 5 # ! ! ! ! ! ! ! ! ! ! ! !
23 down ! ! ! ! . L Y ` ` ` ` ^ B # ! ! ! ! ! ! ! ! ! ! ! ! ! !
24 down ! ! ! ! C ` ` ` V B B % ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !
25 down ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !
26 down ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !
27 down ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !
```
- label: Just a number with the texts matching label.