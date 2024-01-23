---
license: cc-by-nc-sa-4.0

language:
- lb
- de
- fr
- en
- pt

---
#### This custom multilingual-multispeaker TTS speech corpus contains 12.800 balanced samples with audio files (wav format sampled with 16000 Hz) and related transcriptions (csv format with two columns) from 18 speakers. The dataset has been assembled from the following sources:

* [VCTK](https://datashare.ed.ac.uk/handle/10283/3443) : 428 + 426 + 426 english male samples (p259, p274, p286) (CC BY 4.0) 
* [LJSpeech](https://keithito.com/LJ-Speech-Dataset/) : 1280 english female samples (public domain)
* [m-ailabs](https://www.caito.de/2019/01/03/the-m-ailabs-speech-dataset/) : 1280 french male samples (public free licence)
* [SIWIS](https://datashare.ed.ac.uk/handle/10283/2353) : 1024 french female samples (CC BY 4.0) 
* [Rhasspy](https://github.com/rhasspy/dataset-voice-kerstin) : 1082 german female samples (CC0 1.0)
* [Thorsten](https://www.thorsten-voice.de) : 1280 german male samples (CC0)
* [TTS-Portuguese-Corpus](https://github.com/Edresson/TTS-Portuguese-Corpus) : 2560 portuguese male samples (CC BY 4.0) 
* [Marylux](https://github.com/marytts/marylux-data) : 663 luxembourgish & 198 german & 256 french female samples  (CC BY-NC-SA 4.0) 
* [uni.lu](http://engelmann.uni.lu/dictee/index.php) : 409 luxembourgish female & 231 luxembourgish male samples (© uni.lu)
* [rtl.lu](https://www.rtl.lu/meenung/commentaire) : 1257 luxembourgish male samples (© RTL-CLT-UFA)
* Charel : 11 luxembourgish boy samples from my grandchild

#### The dataset has been manually checked and the transcriptions have been expanded and eventually corrected to comply with the audio files. The data structure is equivalent to the mailabs format. The folder nesting is shown below:

```  
mailabs
   language-1
      by_book
         female 
            speaker-1
               wavs/ folder
               metadata.csv
               metadata-train.csv
               metadata-eval.csv
            speaker-2
               wavs/ folder
               metadata.csv
               metadata-train.csv
               metadata-eval.csv
            ...
         male
            speaker-1   
               wavs/ folder
               metadata.csv
               metadata-train.csv
               metadata-eval.csv
            speaker-2
               wavs/ folder
               metadata.csv
               metadata-train.csv
               metadata-eval.csv
            ...               
   language-2
      by_book
         ...
   language-3
      by_book
         ...
   ...                                  
```  

#### Thanks to [RTL](https://www.rtl.lu/) and to the [University of Luxembourg](https://wwwen.uni.lu/) for permission to use and share selected copyrighted data.