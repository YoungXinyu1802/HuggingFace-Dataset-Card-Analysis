# Dataset Summary

**mRobust** is a multilingual version of the [TREC 2004 Robust passage ranking dataset](https://trec.nist.gov/data/robust/04.guidelines.html).
For more information, checkout our papers:
  <!-- * [**mRobust: A Multilingual Version of the MS MARCO Passage Ranking Dataset**](https://arxiv.org/abs/2108.13897)
  * [**A cost-benefit analysis of cross-lingual transfer methods**](https://arxiv.org/abs/2105.06813) -->


The current version is composed 10 languages: Chinese, French, German, Indonesian, Italian, Portuguese, Russian, Spanish, Dutch and Vietnamese.


### Supported languages

| Language name | Language code |
|---------------|---------------|
| English		| english		|
| Chinese		| chinese		|
| French		| french		|
| German		| german		|
| Indonesian	| indonesian	|
| Italian		| italian		|
| Portuguese	| portuguese	|
| Russian		| russian		|
| Spanish		| spanish		|
| Dutch         | dutch         |
| Vietnamese    | vietnamese    |


# Dataset Structure

You can load mRobust dataset by choosing a specific language. We include the translated collections of documents and queries.

#### Queries

```python
>>> dataset = load_dataset('unicamp-dl/mrobust', 'queries-spanish')
>>> dataset['queries'][1]
{'id': '302', 'text': '¿Está controlada la enfermedad de la poliomielitis (polio) en el mundo?'}
```

#### Collection

```python
>>> dataset = load_dataset('unicamp-dl/mrobust', 'collection-portuguese')
>>> dataset['collection'][5]
{'id': 'FT931-16660', 'text': '930105 FT 05 JAN 93 / Cenelec: Correção O endereço do Cenelec, Comitê Europeu de Normalização Eletrotécnica, estava incorreto na edição de ontem. É Rue de Stassart 35, B-1050, Bruxelas, Tel (322) 519 6871. CEN, Comitê Europeu de Normalização, está localizado na Rue de Stassart 36, B-1050, Bruxelas, Tel 519 6811.'}
```


# Citation Information
```
@misc{https://doi.org/10.48550/arxiv.2209.13738,
  doi = {10.48550/ARXIV.2209.13738},
  url = {https://arxiv.org/abs/2209.13738},
  author = {Jeronymo, Vitor and Nascimento, Mauricio and Lotufo, Roberto and Nogueira, Rodrigo},
  title = {mRobust04: A Multilingual Version of the TREC Robust 2004 Benchmark},
  publisher = {arXiv},
  year = {2022},
  copyright = {Creative Commons Attribution 4.0 International}
}

```
