---
license: mit
---

These word embeddings were computed using the POLAR technique to reproject 'common' word embeddings into roundabout 700 interpretable dimensions of polar opposites (i.e. good/bad). 
I just used their scripts here: 
https://github.com/Sandipan99/POLAR

I applied those on the wikidata5m embeddings, 5 million knowledge graph embeddings (SimplE). 
https://graphvite.io/docs/latest/pretrained_model.html

As the model became too huge, I further filtered it for overlap with fasttext embedding tokens. 
Not all dimensions make sense, this is a work in progress. 
I intend to remove dimensions which turn out to not make sense, when using them. 