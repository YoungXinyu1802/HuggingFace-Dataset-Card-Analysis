---
license: mit
dataset_info:
  features:
  - name: text_id
    dtype: int64
  - name: text
    dtype: string
  - name: level
    dtype: string
  splits:
  - name: test
    num_bytes: 1276559.048483246
    num_examples: 8321
  - name: train
    num_bytes: 4595060.28364021
    num_examples: 29952
  - name: validation
    num_bytes: 510715.6678765444
    num_examples: 3329
  download_size: 3645953
  dataset_size: 6382335.0
---
## Córpus de Complexidade Textual para Estágios Escolares do Sistema Educacional Brasileiro

O córpus inclui trechos de: livros-textos cuja lista completa é apresentada abaixo, notícias da Seção Para Seu Filho Ler (PSFL) do jornal Zero Hora que apresenta algumas notícias sobre o mesmo córpus do jornal do Zero Hora, mas escritas para crianças de 8 a 11 anos de idade , Exames do SAEB , Livros Digitais do Wikilivros em Português, Exames do Enem dos anos 2015, 2016 e 2017. Todo o material em português foi disponibilizado para avaliar a tarefa de complexidade textual (readability).

Lista completa dos Livros Didáticos e suas fontes originais

Esse corpus faz parte dos recursos de meu doutorado na área de Natural Language Processing, sendo realizado no Núcleo Interinstitucional de Linguística Computacional da USP de São Carlos. Esse trabalho foi orientado pela Profa. Sandra Maria Aluísio.

http://nilc.icmc.usp.br

@inproceedings{mgazzola19,
  title={Predição da Complexidade Textual de Recursos Educacionais Abertos em Português},
  author={Murilo Gazzola, Sidney Evaldo Leal, Sandra Maria Aluisio},
  booktitle={Proceedings of the Brazilian Symposium in Information and Human Language Technology},
  year={2019}
}