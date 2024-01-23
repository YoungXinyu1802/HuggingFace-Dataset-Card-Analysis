A collection of 38,176 emoji images from Facebook, Google, Apple, WhatsApp, Samsung, [JoyPixels](https://www.joypixels.com/), Twitter, [emojidex](https://www.emojidex.com/), LG, [OpenMoji](https://openmoji.org/), and Microsoft. It includes all the emojis for these apps/platforms as of early 2022.

* Counts: Facebook=3664, Google=3664, Apple=3961, WhatsApp=3519, Samsung=3752, JoyPixels=3538, Twitter=3544, emojidex=2040, LG=3051, OpenMoji=3512, Microsoft=3931.
* Sizes: Facebook=144x144, Google=144x144, Apple=144x144, WhatsApp=144x144, Samsung=108x108, JoyPixels=144x144, Twitter=144x144, emojidex=144x144, LG=136x128, OpenMoji=144x144, Microsoft=144x144.
* The tar files directly contain the image files (they're not inside a parent folder).
* The emoji code points are at the end of the filename, but there are some adjustments needed to parse them into the Unicode character consistently across all sets of emojis in this dataset. Here's some JavaScript code to convert the file name of an emoji image into the actual Unicode emoji character:
```js
let filename = ...;
let fixedFilename = filename.replace(/(no|light|medium|medium-light|medium-dark|dark)-skin-tone/, "").replace(/__/, "_").replace(/--/, "-");
let emoji = String.fromCodePoint(...fixedFilename.split("_")[1].split(".")[0].split("-").map(hex => parseInt(hex, 16)));
```

## Facebook examples:
![Facebook emoji grid](https://i.imgur.com/z0ZCHfO.jpg)

## Google examples:
![Google emoji grid](https://i.imgur.com/yhPVAzN.jpg)

## Apple examples:
![Apple emoji grid](https://i.imgur.com/Y0fUAIA.jpg)

## WhatsApp examples:
![WhatsApp emoji grid](https://i.imgur.com/6kqHLXW.jpg)

## Samsung examples:
![Samsung emoji grid](https://i.imgur.com/rERdop1.jpg)

## JoyPixels examples:
![JoyPixels emoji grid](https://i.imgur.com/nZSYsiN.jpg)

## Twitter examples:
![Twitter emoji grid](https://i.imgur.com/zRxJHfj.jpg)

## emojidex examples:
![emojidex emoji grid](https://i.imgur.com/BQYBu7a.jpg)

## LG examples:
![LG emoji grid](https://i.imgur.com/xv1lQRl.jpg)

## OpenMoji examples:
![OpenMoji emoji grid](https://i.imgur.com/Uk8aRXx.jpg)

## Microsoft examples:
![Microsoft emoji grid](https://i.imgur.com/Z01Tnn9.jpg)