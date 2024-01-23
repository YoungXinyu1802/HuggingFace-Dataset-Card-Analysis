# BioNLP2021 dataset (Task2)
___

Data fields:
* text (str): source text; Section and Article (train_mul subset only) are separated by &lt;SAS&gt; ; Single Documents  are separated by &lt;DOC&gt; ; Sentences  are separated by &lt;SS&gt;
* summ_abs, summ_ext (str): abstractive and extractive summarization, whose Sentences  are separated by &lt;SS&gt;
* question (str): question, whose Sentences  are separated by &lt;SS&gt;
* key (str): key in the origin dataset (for submitting)