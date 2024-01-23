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
pretty_name: Corpus tesis de la SCJN 
size_categories:
- unknown
source_datasets:
- original
task_categories: []
task_ids: []
---

# Corpus tesis de la SCJN


En su primera versión contiene textos correspondientes a las tesis de la décima y undécima época publicadas al mes de febrero del 2022 por la SCJN.

## Dataset Structure

### Data Instances

Un ejemplo de 'train' se ve de la siguiente forma:

```
{   
    'id': '3', 
    'text': 'a la luz de las disposiciones del sistema de derechos humanos, los principios tanto de buena fe como de protección de las apariencias constituyen un límite tendente a evitar el dolo para el disfuncional ejercicio de los actos procesales, al cumplir con la función de colmar las inevitables lagunas legales, en tanto que la norma sólo previene abusos comunes, prohibiéndolos en forma enunciativa, porque de considerarlos limitativamente, muchas conductas o declaraciones contrarias a otras precedentes y, por tanto, indebidas, escaparían de la regulación. ambos principios sirven para analizar el caso en el que, en una primera ejecutoria de amparo promovido contra el auto de vinculación a proceso, se declaró irregularmente llevada a cabo una diligencia de reconocimiento de una persona por una fotografía (imputado), al inobservarse las formas procesales, por lo que en cumplimiento con la sentencia, se dictó auto de no vinculación a proceso y, en atención al deber de investigar conforme a los parámetros convencionales, la autoridad practicó una posterior diligencia, esta vez conforme a las disposiciones adjetivas que la rigen; sin embargo, si el defensor se retiró sin firmarla, aduciendo que lo haría posteriormente, sin que así se hubiera logrado, no obstante las gestiones tendientes a ello por la autoridad investigadora, quien pormenorizadamente las detalló en una certificación. actuación que debe ser sometida en cada caso al escrutinio constitucional, considerando que no puede alegar la nulidad quien ha incurrido conscientemente a su producción, porque buscaría aprovecharse de su personal dolo, al provocar daños por medio del uso desviado de medios legales inicialmente legítimos, si se les considera aisladamente. ahora bien, ponderado el caso concreto, se advierte que no obstante alegar en favor de su defenso el propio dolo, se produjeron las consecuencias inherentes a la diligencia en los términos establecidos en la norma, pues incluso consta que intervino activamente en la diligencia; lo que conduce a estimar infundado el agravio expuesto en el sentido de que debe negársele validez, al tender a beneficiar al quejoso del dolo del defensor expresado en retirarse sin firmar, indicando que regresaría a hacerlo, sin que hubiera actuado conforme a esa manifestación precedente, pretendiendo que, de prosperar la falta de formalidad en la segunda diligencia, la cual ahora le es atribuible, afectaría la expectativa creada en otros sujetos de derecho, en la especie, las víctimas, incluso, el exceso en el ejercicio de la acción constitucional alentaría la práctica viciosa de actos cuyos frutos serían aprovechables por quienes los realizan y, por otra parte, tanto las autoridades investigadoras como los tribunales se harían en alguna forma partícipes de ese proceder irregular, si consideraran permitido ese comportamiento sólo porque la ley omitió prohibirlo, incumpliendo las primeras con el deber de investigar la verdad conforme a los parámetros convencionales y, los segundos, al otorgarles credibilidad.'
}
```

### Data Fields

Los campos son los mismos para todos los splits.

- `id`: a `string` feature.
- `text`: a `string` features.

### Data Splits

|  name   |train|validation|test|
|---------|----:|---------:|---:|
|scjn_corpus_tesis|27913|0|0|

## Dataset Creation

### Annotations


### Dataset Curators

Ana Gabriela Palomeque Ortiz, from SCJN - Unidad General de Administración del Conocimiento Jurídico.

### Personal and Sensitive Information

No personal or sensitive information included.

## Considerations for Using the Data

### Other Known Limitations

La información contenida en este dataset es para efectos demostrativos y no representa una fuente oficial de la Suprema Corte de Justicia de la Nación.

## License

<br/>This work is licensed under a <a rel="license" href="https://creativecommons.org/licenses/by-sa/4.0/deed.es">Attribution-ShareAlike 4.0 International License</a>.
