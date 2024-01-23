---
pretty_name: IRIS Legal Dataset
annotations_creators:
- automated
language_creators:
- found
language:
- pt
license:
- mit
multilinguality:
- monolingual
size_categories:
- 10K>n
source_datasets:
- original
task_categories:
- text-classification
task_ids:
- text-scoring
- semantic-similarity-scoring
---


![INESC-ID](https://www.inesc-id.pt/wp-content/uploads/2019/06/INESC-ID-logo_01.png)
![A Semantic Search System for Supremo Tribunal de Justiça](https://rufimelo99.github.io/SemanticSearchSystemForSTJ/_static/logo.png)

Work developed as part of [Project IRIS](https://www.inesc-id.pt/projects/PR07005/).

Thesis: [A Semantic Search System for Supremo Tribunal de Justiça](https://rufimelo99.github.io/SemanticSearchSystemForSTJ/)

# Portuguese Legal Sentences
Collection of Legal Sentences pairs from the Portuguese Supreme Court of Justice
The goal of this dataset was to be used for Semantic Textual Similarity

- Values from 0-1: random sentences across documents
- Values from 2-4: sentences from the same summary (implying some level of entailment)
- Values from 4-5: sentences pairs generated through OpenAi' text-davinci-003 ("Escreve por outras palavras:\n\Entrada:\n"+originalQuery + "\Saída: \n")



### Contributions
[@rufimelo99](https://github.com/rufimelo99)


If you use this work, please cite:

```bibtex
@inproceedings{MeloSemantic,
	author = {Melo, Rui and Santos, Professor Pedro Alexandre and Dias, Professor Jo{\~ a}o},
	title = {A {Semantic} {Search} {System} for {Supremo} {Tribunal} de {Justi}{\c c}a},
}
```