This dataset contains images from iNaturalist of butterflies (superfamily Papilionoidea) with at least one fave. Check the descriptions - some images have a licence like CC-BY-NC and can't be used for commercial purposes. 

The list of observations was exported from iNaturalist after a query similar to https://www.inaturalist.org/observations?place_id=any&popular&taxon_id=47224

The images were downloaded with img2dataset and uploaded to the huggingface hub by @johnowhitaker using this colab notebook: https://colab.research.google.com/drive/14qwFV_G4dh6evizzqHP08qDUAHtzfuiW?usp=sharing

The goal is to have a dataset of butterflies in different poses and settings, to use for GAN training and to compare with datasets built with museum collections of pinned specimens (which tend to be much cleaner and have more consistency of pose etc)

I'm not familiar with the nuances of creative commons licencing but you may wish to filter out images which are no-derivatices (CC-...-ND) when training a GAN or creating new images. 