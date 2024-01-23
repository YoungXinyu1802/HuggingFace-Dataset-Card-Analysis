---
task_categories:
- text-classification

---
# AutoNLP Dataset for project: alberti-stanzas-finetuning

## Table of content
- [Dataset Description](#dataset-description)
    - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)

## Dataset Descritpion

This dataset has been automatically processed by AutoNLP for project alberti-stanzas-finetuning.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "text": "No es la ciudad inmunda \nquien empuja las velas. Tampoco el coraz\u00f3n, \nprimitiva caba\u00f1a del deseo, \nse aventura por islas encendidas \nen donde el mar oculta sus ruinas, \nalgas de Baudelaire, espumas y silencios. \nEs la necesidad, la solitaria \nnecesidad de un hombre, \nquien nos lleva a cubierta, \nquien nos hace temblar, vivir en cuerpos \nque resisten la voz de las sirenas, \namarrados en proa, \ncon el tim\u00f3n gimiendo entre las manos.",
    "target": 40
  },
  {
    "text": "Ni mueve m\u00e1s ligera,\nni m\u00e1s igual divide por derecha\nel aire, y fiel carrera,\no la traciana flecha\no la bola tudesca un fuego hecha.",
    "target": 11
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "target": "ClassLabel(num_classes=46, names=['0', '1', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '2', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '3', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '4', '40', '41', '42', '43', '44', '45', '5', '6', '7', '8', '9'], names_file=None, id=None)",
  "text": "Value(dtype='string', id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 4004 |
| valid        | 1001 |
