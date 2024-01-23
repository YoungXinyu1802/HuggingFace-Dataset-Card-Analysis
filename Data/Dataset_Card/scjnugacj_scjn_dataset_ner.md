---
annotations_creators:
- expert-generated
language_creators:
- other
language:
- es
license:
- cc-by-sa-4.0
multilinguality:
- monolingual
pretty_name: Corpus SCJN NER
size_categories:
- unknown
source_datasets:
- original
task_categories:
- Token Classification
task_ids:
- NER
---

# Corpus SCJN NER, para el reconocimiento de entidades nombradas


En su primera versión contiene etiquetas para identificar leyes y tratados internacionales de los que el Estado Mexicano es parte.

## Dataset Structure

### Data Instances

Un ejemplo de 'train' se ve de la siguiente forma:

```
{   
    'id': '3', 
    'ner_tags': [0,  0,  0,  0,  0,  1,  2,  2,  2,  2,  2,  2,  2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], 
    'tokens': ['el',  'artículo',  '15',  'de',  'la',  'ley',  'general',  'de',  'títulos',  'y',  'operaciones',  'de',  'crédito',  'exige',  'que',  'se',  'satisfagan',  'las',  'expresiones',  'omitidas',  'en',  'el',  'título',  ',',  'antes',  'de',  'la',  'presentación',  'de',  'éste',  'para',  'su',  'aceptación',  'o',  'para',  'su',  'pago',  '.',  'aunque',  'varios',  'autores',  'estiman',  'que',  'el',  'tenedor',  'puede',  'completar',  'los',  'requisitos',  'faltantes',  'a',  'la',  'cambial',  ',',  'en',  'cualquier',  'instante',  'anterior',  'a',  'su',  'vencimiento',  ',',  'este',  'criterio',  'no',  'es',  'aplicable',  'frente',  'a',  'la',  'disposición',  'terminante',  'de',  'la',  'ley',  'mexicana',  ';',  'y',  'si',  'nuestro',  'legislador',  'hubiera',  'aceptado',  'la',  'posibilidad',  'de',  'llenar',  'los',  'requisitos',  'en',  'cualquier',  'momento',  ',',  'hasta',  'antes',  'de',  'la',  'presentación',  'del',  'documento',  'para',  ',',  'el',  'pago',  ',',  'no',  'habría',  'hablado',  'de',  'la',  'presentación',  'para',  'la',  'aceptación',  ';',  'máxime',  ',',  'que',  'mientras',  'todas',  'las',  'letras',  'de',  'cambio',  'son',  'susceptibles',  'de',  'pago',  ',',  'no',  'todas',  'lo',  'son',  'de',  'aceptación',  '.',  'la',  'cambial',  'en',  'blanco',  'bien',  'puede',  'existir',  'y',  'circular',  'antes',  'de',  'que',  'sea',  'presentada',  'para',  'su',  'aceptación',  ';',  'pero',  'cuando',  'ya',  'el',  'tenedor',  'va',  'a',  'hacer',  'valer',  'sus',  'derechos',  '(',  'y',  'la',  'presentación',  'para',  'la',  'aceptación',  'es',  'el',  'ejercicio',  'de',  'uno',  'de',  'ellos',  ')',  ',',  'debe',  'llenar',  'los',  'extremos',  'necesarios',  'y',  'presentar',  'un',  'documento',  'completo',  '.',  'cuando',  'el',  'girado',  ',',  'al',  'aceptar',  'la',  'letra',  ',',  'se',  'muestra',  'conforme',  'en',  'que',  'después',  'se',  'llene',  'la',  'expresión',  'de',  'su',  'importe',  ',',  'ello',  'no',  'le',  'reporta',  'perjuicio',  ',',  'si',  'el',  'beneficiario',  'lo',  'hace',  'dentro',  'de',  'los',  'límites',  'convenidos',  ';',  'más',  'si',  'éste',  'se',  'excede',  'en',  'la',  'expresión',  'de',  'la',  'cantidad',  'convenida',  ',',  'el',  'girado',  'sí',  'recibe',  'perjuicio',  'considerable',  ',',  'ya',  'que',  'a',  'pesar',  'de',  'que',  'pueda',  'válidamente',  'oponer',  'las',  'excepciones',  'de',  'dolo',  'y',  'plus',  'petitio',  'correspondientes',  ',',  'frente',  'al',  'beneficiario',  'que',  'violó',  'lo',  'pactado',  ',',  'no',  'podrá',  'hacerlo',  'si',  'el',  'tenedor',  'es',  'un',  'tercero',  'que',  'de',  'buena',  'fe',  'adquirió',  'el',  'documento',  ',',  'ignorando',  'las',  'circunstancias',  'precedentes',  ';',  'en',  'cambio',  ',',  'si',  'de',  'acuerdo',  'con',  'lo',  'preceptuado',  'por',  'nuestra',  'ley',  ',',  'falta',  'el',  'título',  'de',  'crédito',  ',',  'pues',  'el',  'documento',  'cuyos',  'requisitos',  'omitidos',  'no',  'se',  'satisficieron',  'oportunamente',  ',',  'no',  'produce',  'efectos',  'como',  'tal',  '(',  'artículo',  '14',  'de',  'la',  'ley',  'de',  'la',  'materia',  ')',  ',',  'ésta',  'será',  'excepción',  'que',  ',',  'demostrada',  ',',  'puede',  'ser',  'oponible',  'a',  'cualquier',  'tenedor',  ',',  'es',  'decir',  ',',  'ya',  'no',  'será',  'una',  'excepción',  'personal',  ',',  'sino',  'una',  'excepción',  'real',  '.']
}
```

### Data Fields

Los campos son los mismos para todos los splits.

- `id`: a `string` feature.
- `tokens`: a `list` of `string` features.
- `ner_tags`: a `list` of classification labels (`int`). Full tagset with indices:
```python
{'O': 0, 'B-LEY': 1, 'I-LEY': 2, 'B-TRAT_INTL': 3, 'I-TRAT_INTL': 4}
```

### Data Splits

|  name   |train|validation|test|
|---------|----:|---------:|---:|
|SCJNNER|1396|345|0|

## Dataset Creation

### Annotations

|  annotations|train|validation|test|
|---------|----:|---------:|---:|
|LEY|1084|329|0|
|TRAT_INTL|935|161|0|

### Dataset Curators

Ana Gabriela Palomeque Ortiz, from SCJN - Unidad General de Administración del Conocimiento Jurídico.

### Personal and Sensitive Information

No personal or sensitive information included.

## Considerations for Using the Data

### Other Known Limitations

La información contenida en este dataset es para efectos demostrativos y no representa una fuente oficial de la Suprema Corte de Justicia de la Nación.

## License

<br/>This work is licensed under a <a rel="license" href="https://creativecommons.org/licenses/by-sa/4.0/deed.es">Attribution-ShareAlike 4.0 International License</a>.
