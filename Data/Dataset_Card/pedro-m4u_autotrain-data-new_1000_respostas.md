---
language:
- pt
task_categories:
- text-classification

---
# AutoTrain Dataset for project: new_1000_respostas

## Dataset Description

This dataset has been automatically processed by AutoTrain for project new_1000_respostas.

### Languages

The BCP-47 code for the dataset's language is pt.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "target": 0,
    "text": " Ol\u00e1, no meu \u00faltimo pedido eu paguei o item errado. Paguei a cerveja long neck, quando o correto \u00e9 a garrafa de 600ml."
  },
  {
    "target": 4,
    "text": " Boa tarde!!! Sou moradora do Citt\u00e0 Imbu\u00ed, hoje 15/01 por volta das 11:50, meu filho tentou comprar uma coca cola e n\u00e3o conseguiu, mas o valor do produto foi debitado. Voc\u00eas podem verificar nas imagens e externar o valor? Desde j\u00e1, agrade\u00e7o. Att, Ana Carla"
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "target": "ClassLabel(names=['Compra Equivocada', 'Cr\u00e9dito n\u00e3o compensado', 'Desativa\u00e7\u00e3o de conta', 'Dificuldade para finalizar a compra', 'Estorno/devolu\u00e7\u00e3o de valor', 'Problemas com destrava', 'Problemas com promo\u00e7\u00f5es', 'Produto danificado/Vencido', 'Produto n\u00e3o encontrado', 'Solicita\u00e7\u00e3o de reposi\u00e7\u00e3o'], id=None)",
  "text": "Value(dtype='string', id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 715 |
| valid        | 182 |
