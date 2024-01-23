# Dataset Summary

**mMARCO** is a multilingual version of the [MS MARCO passage ranking dataset](https://microsoft.github.io/msmarco/).
For more information, checkout our papers:
  * [**mMARCO: A Multilingual Version of the MS MARCO Passage Ranking Dataset**](https://arxiv.org/abs/2108.13897)
  * [**A cost-benefit analysis of cross-lingual transfer methods**](https://arxiv.org/abs/2105.06813)


The first (deprecated) version comprises 8 languages: Chinese, French, German, Indonesian, Italian, Portuguese, Russian and Spanish. The current version included translations for Japanese, Dutch, Vietnamese, Hindi and Arabic. The current version is composed of 14 languages (including the original English version).


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
| Arabic        | arabic        |
| Dutch         | dutch         |
| Hindi         | hindi         |
| Japanese      | japanese      |
| Vietnamese    | vietnamese    |


# Dataset Structure

You can load mMARCO dataset by choosing a specific language. We include training triples (query, positive and negative example), the translated collections of documents and queries.


#### Training triples

```python
>>> dataset = load_dataset('unicamp-dl/mmarco', 'english')
>>> dataset['train'][1]
{'query': 'what fruit is native to australia', 'positive': 'Passiflora herbertiana. A rare passion fruit native to Australia. Fruits are green-skinned, white fleshed, with an unknown edible rating. Some sources list the fruit as edible, sweet and tasty, while others list the fruits as being bitter and inedible.assiflora herbertiana. A rare passion fruit native to Australia. Fruits are green-skinned, white fleshed, with an unknown edible rating. Some sources list the fruit as edible, sweet and tasty, while others list the fruits as being bitter and inedible.', 'negative': 'The kola nut is the fruit of the kola tree, a genus (Cola) of trees that are native to the tropical rainforests of Africa.'}
```

#### Queries

```python
>>> dataset = load_dataset('unicamp-dl/mmarco', 'queries-spanish')
>>> dataset['train'][1]
{'id': 634306, 'text': '¿Qué significa Chattel en el historial de crédito'}
```

#### Collection

```python
>>> dataset = load_dataset('unicamp-dl/mmarco', 'collection-portuguese')
>>> dataset['collection'][100]
{'id': 100, 'text': 'Antonín Dvorák (1841-1904) Antonin Dvorak era filho de açougueiro, mas ele não seguiu o negócio de seu pai. Enquanto ajudava seu pai a meio tempo, estudou música e se formou na Escola de Órgãos de Praga em 1859.'}
```


# Citation Information
```
@misc{bonifacio2021mmarco,
      title={mMARCO: A Multilingual Version of MS MARCO Passage Ranking Dataset}, 
      author={Luiz Henrique Bonifacio and Vitor Jeronymo and Hugo Queiroz Abonizio and Israel Campiotti and Marzieh Fadaee and  and Roberto Lotufo and Rodrigo Nogueira},
      year={2021},
      eprint={2108.13897},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
