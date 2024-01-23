---
language:
- es
multilinguality:
- monolingual
size_categories:
- 1K<n<10K
task_categories:
- text2text-generation
- translation
task_ids: []
pretty_name: neutralES
---
# Spanish Gender Neutralization

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/2/29/Gender_equality_symbol_%28clipart%29.png" width="250"/>
</p>

Spanish is a beautiful language and it has many ways of referring to people, neutralizing the genders and using some of the resources inside the language. One would say *Todas las personas asistentes* instead of *Todos los asistentes* and it would end in a more inclusive way for talking about people. This dataset collects a set of manually anotated examples of gendered-to-neutral spanish transformations.

The intended use of this dataset is to train a spanish language model for translating from gendered to neutral, in order to have more inclusive sentences.

### Compiled sources

One of the major challenges was to obtain a valuable dataset that would suit gender inclusion purpose, therefore, when building the dataset, the team opted to dedicate a considerable amount of time to build it from a scratch. You can find here the results.

The data used for the model training has been manually created form a compilation of sources, obtained from a series of guidelines and manuals issued by Spanish Ministry of Health, Social Services and Equality in the matter of the usage of non-sexist language, stipulated in this linked [document](https://www.inmujeres.gob.es/servRecursos/formacion/GuiasLengNoSexista/docs/Guiaslenguajenosexista_.pdf).

**NOTE: Appart from manually anotated samples, this dataset has been further increased by applying data augmentation so a minumin number of training examples are generated.**

* [Guía para un discurso igualitario en la universidad de alicante](https://ieg.ua.es/es/documentos/normativasobreigualdad/guia-para-un-discurso-igualitario-en-la-ua.pdf)

* [Guía UC de Comunicación en Igualdad](<https://web.unican.es/unidades/igualdad/SiteAssets/igualdad/comunicacion-en-igualdad/guia%20comunicacion%20igualdad%20(web).pdf>)

* [Buenas prácticas para el tratamiento del lenguaje en igualdad](https://e-archivo.uc3m.es/handle/10016/22811)

* [Guía del lenguaje no sexista de la Universidad de Castilla-La Mancha](https://unidadigualdad.ugr.es/page/guiialenguajeuniversitarionosexista_universidaddecastillalamancha/!)

* [Guía de Lenguaje Para el Ámbito Educativo](https://www.educacionyfp.gob.es/va/dam/jcr:8ce318fd-c8ff-4ad2-97b4-7318c27d1682/guialenguajeambitoeducativo.pdf)

* [Guía para un uso igualitario y no sexista del lenguaje y dela imagen en la Universidad de Jaén](https://www.ujaen.es/servicios/uigualdad/sites/servicio_uigualdad/files/uploads/Guia_lenguaje_no_sexista.pdf)

* [Guía de uso no sexista del vocabulario español](https://www.um.es/documents/2187255/2187763/guia-leng-no-sexista.pdf/d5b22eb9-b2e4-4f4b-82aa-8a129cdc83e3)

* [Guía para el uso no sexista de la lengua castellana y de imágnes en la UPV/EHV](https://www.ehu.eus/documents/1734204/1884196/Guia_uso_no_sexista_EHU.pdf)

* [Guía de lenguaje no sexista UNED](http://portal.uned.es/pls/portal/docs/PAGE/UNED_MAIN/LAUNIVERSIDAD/VICERRECTORADOS/GERENCIA/OFICINA_IGUALDAD/CONCEPTOS%20BASICOS/GUIA_LENGUAJE.PDF)

* [COMUNICACIÓN AMBIENTAL CON PERSPECTIVA DE GÉNERO](https://cima.cantabria.es/documents/5710649/5729124/COMUNICACI%C3%93N+AMBIENTAL+CON+PERSPECTIVA+DE+G%C3%89NERO.pdf/ccc18730-53e3-35b9-731e-b4c43339254b)

* [Recomendaciones para la utilización de lenguaje no sexista](https://www.csic.es/sites/default/files/guia_para_un_uso_no_sexista_de_la_lengua_adoptada_por_csic2.pdf)

* [Estudio sobre lenguaje y contenido sexista en la Web](https://www.mujeresenred.net/IMG/pdf/Estudio_paginas_web_T-incluye_ok.pdf)

* [Nombra.en.red. En femenino y en masculino](https://www.inmujeres.gob.es/areasTematicas/educacion/publicaciones/serieLenguaje/docs/Nombra_en_red.pdf)

## Team Members
- Fernando Velasco [(fermaat)](https://huggingface.co/fermaat)
- Cibeles Redondo [(CibelesR)](https://huggingface.co/CibelesR)
- Juan Julian Cea [(Juanju)](https://huggingface.co/Juanju)
- Magdalena Kujalowicz [(MacadellaCosta)](https://huggingface.co/MacadellaCosta)
- Javier Blasco [(javiblasco)](https://huggingface.co/javiblasco)

### Enjoy and feel free to collaborate with this dataset 🤗