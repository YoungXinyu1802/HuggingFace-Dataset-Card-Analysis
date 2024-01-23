---
license: cc0-1.0
---

This dataset was created using [this tool](https://github.com/p1atdev/pinterest-wizard).

# concept_art.json

589 images about "Concept Art" from **Pinterest searches** 🤗.

# double_exposure.json

597 images about "Double Exposure" from **Pinterest searches** 🤗.

# vaporwave.json

599 images about "Vaporwave" from **Pinterest searches** 🤗.

# typography.json

633 images about "Typography" from **Pinterest searches** 🤗.

# portrait.json

573 images about "Portrait" from **Pinterest searches** 🤗.

# selfie.json

584 images about "自撮り　女の子" from **Pinterest searches** 🤗.

# Type

```ts
interface Pinterest {
  url: string    // pinterest page url
  alt: string    // description of the image (not so accurate everytime)
  src: string    // image url
  tags: string[] // related tags
}
```