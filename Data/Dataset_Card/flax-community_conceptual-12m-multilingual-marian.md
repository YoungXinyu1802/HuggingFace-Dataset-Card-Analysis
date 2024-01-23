This dataset is created from subset of [Conceptual Captions](https://ai.google.com/research/ConceptualCaptions/). The original dataset has 12M captions but this dataset has around 10M image, caption pairs in different languages with 2.5M unique images. This dataset has captions translated from English to Spanish, German, French using language specific English to [Marian](https://huggingface.co/Helsinki-NLP) models. Data distribution is following:

`train_file_marian_final.tsv`: 10010625 captions (2502656 captions of English, German, Spanish, French each)
<br /> 
`val_file_marian_final.tsv`: 110592 captions (27648 captions of English, German, Spanish, French each)