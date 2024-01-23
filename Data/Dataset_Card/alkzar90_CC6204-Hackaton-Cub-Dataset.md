---
language:
- en
license:
- apache-2.0
pretty_name: CC6204-Hackaton-CUB200
size_categories:
- 10K<n<15K
source_datasets:
- extended|other
paperswithcode_id: cub-200-2011
task_categories:
- image-classification
- text-classification
task_ids:
- multi-class-image-classification
---

## Dataset Description

- **Homepage:** [CUB 200 2011](http://www.vision.caltech.edu/datasets/cub_200_2011/)
- **Repository:** [Caltech Vision Lab](http://www.vision.caltech.edu/datasets/cub_200_2011/)
- **Paper:** [The Caltech-UCSD Birds-200-2011 Dataset](https://authors.library.caltech.edu/27452/1/CUB_200_2011.pdf)
- **Leaderboard:** [Paperswithcode](https://paperswithcode.com/dataset/cub-200-2011)
- **Point of Contact:** [Catherine Wah](https://scholar.google.com/citations?user=rCDdLUsAAAAJ&hl=en)

  
# CC6204: Hackaton Deep Learning 2022


**Nota:** esta fue un actividad del curso CC6204: Deep Learning, Universidad de Chile, año 2022. Dictado por el profesor Iván Sipiran, material del curso [aquí](https://github.com/ivansipiran/CC6204-Deep-Learning).


En esta actividad intentaremos resolver un problema de clasificación multimodal. En un problema de clasificación multimodal, cada pieza de información viene en diferentes representaciones (imágenes, texto, audios, etc) y la idea es determinar cómo usar esos datos para un problema de clasificación.
En este caso trabajaremos con un dataset que contiene datos sobre especies de pájaros.

## Dataset


### Data Instances

Una muestra del _dataset_ se encuentra a continuación:

```
{'image': <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=334x500 at 0x7F59DE348AF0>,
 'description': 'this bird has a short orange bill, white breast and body and white eyes.\na medium sized bird with a orange bill and a black crown and white eyes\nthis white-breasted bird has a short, squat, orange bill, a black head and wings, and small white eyes above a white stripe.\nthis bird has a white breast, a black head, a short red beak, and webbed feet.\nthis bird is white with black on its neck and has a long, pointy beak.\nthis bird has wings that are black and has a white belly\nthis bird has wings that are black and has a long bill\nthis is a medium sized bird, with a white belly, and a grey head and wings, with a short yellow bill.\nthis bird is white and gray in color, and has a bright orange beak.\nthis bird has a blunt orange beak with mostly black above the neck, the belly is solid white.\n',
 'label': 6,
 'file_name': 'Parakeet_Auklet_0048_795980.jpg'}
```

### Data Fields

Cada instancia de datos tiene los siguientes campos:

- `image`: imagen RGB de un pájaro
- `description`: texto con 10 descripciones del pájaro en la foto, cada descripción esta separado por un salto de linea (i.e. `\n`)
- `label`: un número entero que representa el id de la especie a la que pertenece el pájaro
<details>
  <summary>Id2String</summary>
  ```bash
  1 001.Black_footed_Albatross
  2 002.Laysan_Albatross
  3 003.Sooty_Albatross
  4 004.Groove_billed_Ani
  5 005.Crested_Auklet
  6 006.Least_Auklet
  7 007.Parakeet_Auklet
  8 008.Rhinoceros_Auklet
  9 009.Brewer_Blackbird
  10 010.Red_winged_Blackbird
  11 011.Rusty_Blackbird
  12 012.Yellow_headed_Blackbird
  13 013.Bobolink
  14 014.Indigo_Bunting
  15 015.Lazuli_Bunting
  16 016.Painted_Bunting
  17 017.Cardinal
  18 018.Spotted_Catbird
  19 019.Gray_Catbird
  20 020.Yellow_breasted_Chat
  21 021.Eastern_Towhee
  22 022.Chuck_will_Widow
  23 023.Brandt_Cormorant
  24 024.Red_faced_Cormorant
  25 025.Pelagic_Cormorant
  26 026.Bronzed_Cowbird
  27 027.Shiny_Cowbird
  28 028.Brown_Creeper
  29 029.American_Crow
  30 030.Fish_Crow
  31 031.Black_billed_Cuckoo
  32 032.Mangrove_Cuckoo
  33 033.Yellow_billed_Cuckoo
  34 034.Gray_crowned_Rosy_Finch
  35 035.Purple_Finch
  36 036.Northern_Flicker
  37 037.Acadian_Flycatcher
  38 038.Great_Crested_Flycatcher
  39 039.Least_Flycatcher
  40 040.Olive_sided_Flycatcher
  41 041.Scissor_tailed_Flycatcher
  42 042.Vermilion_Flycatcher
  43 043.Yellow_bellied_Flycatcher
  44 044.Frigatebird
  45 045.Northern_Fulmar
  46 046.Gadwall
  47 047.American_Goldfinch
  48 048.European_Goldfinch
  49 049.Boat_tailed_Grackle
  50 050.Eared_Grebe
  51 051.Horned_Grebe
  52 052.Pied_billed_Grebe
  53 053.Western_Grebe
  54 054.Blue_Grosbeak
  55 055.Evening_Grosbeak
  56 056.Pine_Grosbeak
  57 057.Rose_breasted_Grosbeak
  58 058.Pigeon_Guillemot
  59 059.California_Gull
  60 060.Glaucous_winged_Gull
  61 061.Heermann_Gull
  62 062.Herring_Gull
  63 063.Ivory_Gull
  64 064.Ring_billed_Gull
  65 065.Slaty_backed_Gull
  66 066.Western_Gull
  67 067.Anna_Hummingbird
  68 068.Ruby_throated_Hummingbird
  69 069.Rufous_Hummingbird
  70 070.Green_Violetear
  71 071.Long_tailed_Jaeger
  72 072.Pomarine_Jaeger
  73 073.Blue_Jay
  74 074.Florida_Jay
  75 075.Green_Jay
  76 076.Dark_eyed_Junco
  77 077.Tropical_Kingbird
  78 078.Gray_Kingbird
  79 079.Belted_Kingfisher
  80 080.Green_Kingfisher
  81 081.Pied_Kingfisher
  82 082.Ringed_Kingfisher
  83 083.White_breasted_Kingfisher
  84 084.Red_legged_Kittiwake
  85 085.Horned_Lark
  86 086.Pacific_Loon
  87 087.Mallard
  88 088.Western_Meadowlark
  89 089.Hooded_Merganser
  90 090.Red_breasted_Merganser
  91 091.Mockingbird
  92 092.Nighthawk
  93 093.Clark_Nutcracker
  94 094.White_breasted_Nuthatch
  95 095.Baltimore_Oriole
  96 096.Hooded_Oriole
  97 097.Orchard_Oriole
  98 098.Scott_Oriole
  99 099.Ovenbird
  100 100.Brown_Pelican
  101 101.White_Pelican
  102 102.Western_Wood_Pewee
  103 103.Sayornis
  104 104.American_Pipit
  105 105.Whip_poor_Will
  106 106.Horned_Puffin
  107 107.Common_Raven
  108 108.White_necked_Raven
  109 109.American_Redstart
  110 110.Geococcyx
  111 111.Loggerhead_Shrike
  112 112.Great_Grey_Shrike
  113 113.Baird_Sparrow
  114 114.Black_throated_Sparrow
  115 115.Brewer_Sparrow
  116 116.Chipping_Sparrow
  117 117.Clay_colored_Sparrow
  118 118.House_Sparrow
  119 119.Field_Sparrow
  120 120.Fox_Sparrow
  121 121.Grasshopper_Sparrow
  122 122.Harris_Sparrow
  123 123.Henslow_Sparrow
  124 124.Le_Conte_Sparrow
  125 125.Lincoln_Sparrow
  126 126.Nelson_Sharp_tailed_Sparrow
  127 127.Savannah_Sparrow
  128 128.Seaside_Sparrow
  129 129.Song_Sparrow
  130 130.Tree_Sparrow
  131 131.Vesper_Sparrow
  132 132.White_crowned_Sparrow
  133 133.White_throated_Sparrow
  134 134.Cape_Glossy_Starling
  135 135.Bank_Swallow
  136 136.Barn_Swallow
  137 137.Cliff_Swallow
  138 138.Tree_Swallow
  139 139.Scarlet_Tanager
  140 140.Summer_Tanager
  141 141.Artic_Tern
  142 142.Black_Tern
  143 143.Caspian_Tern
  144 144.Common_Tern
  145 145.Elegant_Tern
  146 146.Forsters_Tern
  147 147.Least_Tern
  148 148.Green_tailed_Towhee
  149 149.Brown_Thrasher
  150 150.Sage_Thrasher
  151 151.Black_capped_Vireo
  152 152.Blue_headed_Vireo
  153 153.Philadelphia_Vireo
  154 154.Red_eyed_Vireo
  155 155.Warbling_Vireo
  156 156.White_eyed_Vireo
  157 157.Yellow_throated_Vireo
  158 158.Bay_breasted_Warbler
  159 159.Black_and_white_Warbler
  160 160.Black_throated_Blue_Warbler
  161 161.Blue_winged_Warbler
  162 162.Canada_Warbler
  163 163.Cape_May_Warbler
  164 164.Cerulean_Warbler
  165 165.Chestnut_sided_Warbler
  166 166.Golden_winged_Warbler
  167 167.Hooded_Warbler
  168 168.Kentucky_Warbler
  169 169.Magnolia_Warbler
  170 170.Mourning_Warbler
  171 171.Myrtle_Warbler
  172 172.Nashville_Warbler
  173 173.Orange_crowned_Warbler
  174 174.Palm_Warbler
  175 175.Pine_Warbler
  176 176.Prairie_Warbler
  177 177.Prothonotary_Warbler
  178 178.Swainson_Warbler
  179 179.Tennessee_Warbler
  180 180.Wilson_Warbler
  181 181.Worm_eating_Warbler
  182 182.Yellow_Warbler
  183 183.Northern_Waterthrush
  184 184.Louisiana_Waterthrush
  185 185.Bohemian_Waxwing
  186 186.Cedar_Waxwing
  187 187.American_Three_toed_Woodpecker
  188 188.Pileated_Woodpecker
  189 189.Red_bellied_Woodpecker
  190 190.Red_cockaded_Woodpecker
  191 191.Red_headed_Woodpecker
  192 192.Downy_Woodpecker
  193 193.Bewick_Wren
  194 194.Cactus_Wren
  195 195.Carolina_Wren
  196 196.House_Wren
  197 197.Marsh_Wren
  198 198.Rock_Wren
  199 199.Winter_Wren
  200 200.Common_Yellowthroat
  ```
</details>
- `file_name`: nombre del archivo que tiene la imagen

### Data Splits
 
|                  |train| test|
|------------------|----:|----:|
|# de observaciones|5994 |5794 |

## Problema

El problema consiste en entrenar un modelo que clasifique instancias del dataset CUB de la mejor manera posible. Algunas preguntas que podrían guiar nuestro desarrollo son:

* Se podrá obtener un buen _performance_ de clasificación solo usando las imágenes del dataset? Este tipo de problema sería el clásico problema de clasificar imágenes.
* Se podrá obtener un buen _performance_ de clasificación solo usando los textos del dataset? Este tipo de problema sería el clásico problema de clasificar texto.
* Se podrá obtener un mejor _performance_ si combino la información en un modelo multimodal? Cómo construyo un modelo multimodal que reciba una imagen y un texto y clasifique la instancia con su respectiva especie? Hint: piense en cómo una red neuronal (la que sea) es simplemente una función que recibe un dato y genera una representación de alto nivel (vector característico) de ese dato. Una red CNN podría hacerse cargo de calcular la representación de una imagen y una red RNN podría hacerse cargo de calcular la representación del texto. Finalmente concateno ambas representaciones y entreno un MLP final que hace la clasificación.

## Experimentación

Como el dataset es grande y los recursos de computación son muy limitados, una estrategia para hacer los experimentos es tomar una muestra más pequeña de datos para ir probando las ideas. Para esta estrategia, éstas son dos ideas válidas:

* Tomar menos instancias por cada clase para el desarrollo y solo dejar el dataset final para hacer el entrenamiento final y la evaluación final con testing.
* Tomar menos clases para el desarrollo inicial y solo dejar el dataset final para hacer el entrenamiento final y la evaluación final con testing.

Ambas estrategias nos permiten lidiar con los recursos limitados que tenemos, pero cuáles son sus ventajas o desventajas? Si usas alguna de estas estrategias, puedes comentar este punto en tu desarrollo final.

## Métrica de Evaluación

La métrica que se debe reportar es el accuracy en conjunto de test.
  
## Citation Information

Sitio web del [_dataset_ CUB200](http://www.vision.caltech.edu/datasets/cub_200_2011/), y reporte técnico [aquí](https://authors.library.caltech.edu/27452/1/CUB_200_2011.pdf).

```
@techreport{WahCUB_200_2011,
	Title = The Caltech-UCSD Birds-200-2011 Dataset,
	Author = {Wah, C. and Branson, S. and Welinder, P. and Perona, P. and Belongie, S.},
	Year = {2011}
	Institution = {California Institute of Technology},
	Number = {CNS-TR-2011-001}
}
```

## Contributions

Creación y adaptación del material de la actividad en un Hugging Face dataset por Cristóbal Alcázar.
