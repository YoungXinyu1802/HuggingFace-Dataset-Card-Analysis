---
language:
- es
pretty_name: contextualized_hate_speech
task_categories:
- text-classification
tags:
- hate_speech
size_categories:
- 10K<n<100K
---
# Contextualized Hate Speech: A dataset of comments in news outlets on Twitter

## Dataset Description

- **Homepage:** 
- **Repository:** 
- **Paper**: ["Assessing the impact of contextual information in hate speech detection"](https://arxiv.org/abs/2210.00465), Juan Manuel Pérez, Franco Luque, Demian Zayat, Martín Kondratzky, Agustín Moro, Pablo Serrati, Joaquín Zajac, Paula Miguel, Natalia Debandi, Agustín Gravano, Viviana Cotik
- **Point of Contact**: jmperez (at) dc uba ar

### Dataset Summary
![Graphical representation of the dataset](Dataset%20graph.png)
This dataset is a collection of tweets that were posted in response to news articles from five specific Argentinean news outlets: Clarín, Infobae, La Nación, Perfil and Crónica, during the COVID-19 pandemic. The comments were analyzed for hate speech across eight different characteristics: against women, racist content, class hatred, against LGBTQ+ individuals, against physical appearance, against people with disabilities, against criminals, and for political reasons. All the data is in Spanish.

Each comments is labeled with the following variables



| Label      | Description                                                             |
| :--------- | :---------------------------------------------------------------------- |
| HATEFUL    | Contains hate speech (HS)?                                              |
| CALLS      | If it is hateful, is this message calling to (possibly violent) action? |
| WOMEN      | Is this against women?                                                  |
| LGBTI      | Is this against LGBTI people?                                           |
| RACISM     | Is this a racist message?                                               |
| CLASS      | Is this a classist message?                                             |
| POLITICS   | Is this HS due to political ideology?                                   |
| DISABLED   | Is this HS against disabled people?                                     |
| APPEARANCE | Is this HS against people due to their appearance? (e.g. fatshaming)    |
| CRIMINAL   | Is this HS against criminals or people in conflict with law?            |



There is an extra label `CALLS`, which represents whether a comment is a call to violent action or not.
### Citation Information

```bibtex
@article{perez2022assessing,
  title={Assessing the impact of contextual information in hate speech detection},
  author={P{\'e}rez, Juan Manuel and Luque, Franco and Zayat, Demian and Kondratzky, Mart{\'\i}n and Moro, Agust{\'\i}n and Serrati, Pablo and Zajac, Joaqu{\'\i}n and Miguel, Paula and Debandi, Natalia and Gravano, Agust{\'\i}n and others},
  journal={arXiv preprint arXiv:2210.00465},
  year={2022}
}
```

### Contributions

[More Information Needed]