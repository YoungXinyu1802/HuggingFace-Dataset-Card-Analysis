# Extracción de datos de Reddit
Se descargaron todos los titulos de los hilos de algunas comunidades en español de Reddit entre marzo del 2017 y enero del 2022: 

| Comunidad                  | N° de hilos |
|----------------------------|-------------|
|AskRedditespanol            | 28072       |
| BOLIVIA                    | 4935        |
| PERU                       | 20735       |
| argentina                  | 214986      |
| chile                      | 69077       |
|espanol                     | 39376       |
| mexico                     | 136984      |
| preguntaleareddit          | 37300       |
| uruguay                    | 55693       |
| vzla                       | 42909       |

# Etiquetas
Luego, se etiquetaron manualmente algunos de los hilos para marcar AMA vs No AMA.
Se etiquetaron 757 hilos (AMA: 290, No AMA: 458), siguiendo una estrategia de query by committee.
En el archivo `etiqueta_ama.csv` se puede revisar esto.

Con estos 757 hilos se ejecuto un algoritmo de label spreading para identificar los hilos AMA restantes, esto dío un total de 3519 hilos.
En el archivo `autoetiquetado_ama.csv` se puede revisar esto. 

Para identificar las profesiones de las personas que crearon los hilos se utilizó la siguiente lista:
https://raw.githubusercontent.com/davoclavo/adigmatangadijolachanga/master/profesiones.txt

Para lograr abarcar todas las posibilidades, se agregaron tanto las versiones que terminaban en "a" como en "o" de todas las profesiones. 

Luego se agruparon las profesiones similares, para lograr un numero similar de hilos por profesión, para lo que se utilizo el siguiente diccionario:

```
sinonimos = {
    'sexologo': 'psicologo',

    'enfermero': 'medico',
    'farmaceutico': 'medico',
    'cirujano': 'medico',
    'doctor': 'medico',

    'radiologo': 'medico',
    
    'dentista': 'odontologo',
    'matron': 'medico',
    'patologo': 'medico',
    'educador': 'profesor',
    'maestro': 'profesor',
    'programador': 'ingeniero',
    'informatico': 'ingeniero',
    'juez': 'abogado',
    'fiscal': 'abogado',
    'oficial': 'abogado',
    'astronomo': 'ciencias',
    'fisico': 'ciencias',
    'ecologo': 'ciencias',
    'filosofo': 'ciencias',
    'biologo': 'ciencias',
    'zoologo': 'ciencias',
    'quimico': 'ciencias',
    'matematico': 'ciencias',
    'meteorologo': 'ciencias',
    'periodista': 'humanidades',
    'dibujante': 'humanidades',
    'fotografo': 'humanidades',
    'traductor': 'humanidades',
    'presidente': 'jefe',
    'gerente': 'jefe'
} 
```

Se descargaron todos los comentarios de los hilos AMA que contenian algunas de estas profesiones y luego se agruparon incluyendo solamente los que contenian algún signo de pregunta y que tuviesen una respuesta del autor del hilo, formando un par de pregunta respuesta.

Finalmente, se mantuvieron todas las profesiones que contenian más de 200 pares de pregunta respuesta, las que incluyen alrededor de 3000 pares pregunta respuesta.
En el archivo `qa_corpus_profesion.csv` se puede revisar esto. 