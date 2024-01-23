# Egyptian hieroglyphs 𓂀
## _Hieroglyphs image dataset along with Language Model !_

![code](https://i.ibb.co/WtGgxkz/Screenshot-2022-07-12-214648-transformed.png)

## Features

- This dataset is build from the hieroglyphs found in 10 different pictures from the book "The Pyramid of Unas" (Alexandre Piankoff, 1955). We therefore urge you to have access to this book before using the dataset.
- The ten different pictures used throughout this dataset are: 3,5,7,9,20,21,22,23,39,41 (numbers represent the numbers used in the book "The pyramid of Unas".
- Each hieroglyph is manually annotated and labelled according the Gardiner Sign List. The images are stored with their label and number in their name.

```sh
totalImages = 4210 (of which 179 are labelled as UNKNOWN)
totalClasses = 171 (excluding the UNKNOWN class)
```

> NOTE: The labelling may not be 100% correct.
> This is out of my knowledge as an Egyptian
> The hieroglyphs that I was unable to identify are labelled as "UNKNOWN".

&emsp;
## Process

Aside from the manual annotation, we used a text-detection method to extract the hieroglyphs automatically. The results are shown in `Dataset/Automated/`
The labels on automatic detected images are based on a comparison with the manual detection, and are labelled according the the Pascal VOC overlap criteria (50% overlap).

The x/y position of each hieroglyph is stored in the Location-folder. Each file in this folder contains the exact position of all (raw) annotated hieroglyphs in their corresponding picture. 
Example: "030000_S29.png,71,27,105,104," from Dataset/Manual/Locations/3.txt:
  - image = Dataset/Manual/Raw/3/030000_D35.png
  - Picture number = 3 	(Dataset/Pictures/egyptianTexts3.jpg)
  - index number = 0
  - Gardiner label = D35
  - top-left position = 71,27
  - bottom-right position = 105,104		(such that width = (105-71) = 34, and the height is (104-27) = 77)

Included in this dataset are some tools to create the language model.
in `Dataset/LanguageModel/JSESH_EgyptianTexts/` are the Egyptian texts from the JSesh database. Jsesh is an open source program, used to write hieroglyphs [Jsesh](http://jsesh.qenherkhopeshef.org/). The texts are written in a mixture of Gardiner labels and transliteration. Each text can be opened by Jsesh to view the hieroglyphs.

Furthermore, a lexicon is included in `Dataset/LanguageModel/Lexicon.txt`. Originally from [OpenGlyp](http://sourceforge.net/projects/openglyph/), but with added word-occurrence based on the EgyptianTexts. Each time a word is encoutered in the text, the word-occurrence is increased by 1 divided by the amount of other possible words that can be made with the surrounding hieroglyphs.

The lexicon is organised as follows: each line contains a word, that is made up by a number of hieroglyphs. Other information such as the translation, transliteration and word-occurrence is also stored. Each element is separated by a semicolon.
`Example: D36,N35,D7,;an;beautiful;0.333333;`
  - The 3 hieroglyphs used to write this word: D36,N35,D7,
  - transliteration: an
  - English translation: beautiful
  - word-occurrence: 0.333333

nGrams are included in this dataset as well, under Dataset/LanguageModel/nGrams.txt
Each line in this file contains an nGram (either uni-gram, bi-gram or tri-gram) accompanied by their occurrence. 
`Example: G17,N29,G1,;9;`
  - Hieroglyphs used to write this tri-gram: G17,N29,G1
  - number of occurrences in the EgyptianTexts database: 9

## Structure

The dataset is organised as follows:

Dataset/
|---Pictures/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Contains 10 pictures from the book "The Pyramid of Unas", which are used throughout this dataset`

  |---Manual/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Contains the manually annotated images of hieroglyphs`
    |------Locations/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Contains the location-files that hold the x/y position of each`
    |------hieroglyph.
    |------Preprocessed/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Contains the pre-processed images`
    |------Raw/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Contains the raw, un-pre-processed, images of hieroglyphs`
	
  |---Automated/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Contains the result of the automatic hieroglpyh detection`
    |------Locations/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Contains the location-files that hold the x/y position of each `
    |------hieroglyph.
    |------Preprocessed/`Contains the pre-processed images`
    |------Raw/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Contains the raw, un-pre-processed, images of hieroglyphs`

  |---ExampleSet7/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`An example of how the test and train set can be separated.`
    |------test/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Simply contains all pre-processed images from picture #7`
    |------train/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Contains all the hieroglyphs images from other pictures.`

  |---Language Model/
    |------JSESH_EgyptianTexts/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Contains the EgyptianTexts database of JSesh, which is a program used to write hieroglyphs` [JSesh link](http://jsesh.qenherkhopeshef.org/).
    |------Lexicon.txt
    |------nGrams.txt


## License

GPL - non commercial use

**What are you waiting for? Make some ✨Magic ✨!**