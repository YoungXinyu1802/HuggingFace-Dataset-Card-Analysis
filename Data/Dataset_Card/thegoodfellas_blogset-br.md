---
license: apache-2.0
language:
- pt
pretty_name: Blogset BR
size_categories:
- 1M<n<10M
---

# Dataset Card for Dataset Name

## Dataset Description

- **Homepage:** https://www.inf.pucrs.br/linatural/wordpress/recursos-e-ferramentas/blogset-br/ 
- **Leaderboard:** Grupo de Processamento da Linguagem Natural da PUC-RS
- **Point of Contact:** Site oficial

### Dataset Summary

Este Dataset foi criado a partir dos dados disponibilizados pelo Grupo de Processamento de Linguagem Natural da PUC-RS. O site oficial pode ser encontrado aqui: https://www.inf.pucrs.br/linatural/wordpress/recursos-e-ferramentas/blogset-br/

### Supported Tasks and Leaderboards

Indicado para treinamento de modelos de linguagem.

### Languages

Português do Brasil

#### Initial Data Collection and Normalization

Informações sobre a criação do Dataset podem ser encontradas aqui: https://www.inf.pucrs.br/linatural/wordpress/recursos-e-ferramentas/blogset-br/

### Licensing Information

Apache V2

### Contributions

Esta página é meramente uma configuração para o formato Huggingface do trabalho realizado pelo equipe PLN da PUC-RS.

### Huggingface format

O código a seguir foi utilizado para a criação do dataset. Decisões quanto a estrutura:

1. Somente a coluna relacionada ao texto foi utilizada (coluna 4).
2. Foi aplicada uma bateria de ajustes visando limpar o texto conforme pode ser observado no código.
3. Procurou-se manter o limite de 512 palavras em cada linha.

Gist: https://gist.github.com/rdemorais/ce2e708af4c07aba47930bc12ed92472
