---
license: mit
task_categories:
- text-generation
pretty_name: ABC CC
size_categories:
- 100K<n<1M
---

## Dataset Summary

The dataset used to train and evaluate [TunesFormer](https://huggingface.co/sander-wood/tunesformer) is collected from two sources: [The Session](https://thesession.org) and [ABCnotation.com](https://abcnotation.com). The Session is a community website focused on Irish traditional music, while ABCnotation.com is a website that provides a standard for folk and traditional music notation in the form of ASCII text files. The combined dataset consists of 285,449 ABC tunes, with 99\% (282,595) of the tunes used as the training set and the remaining 1\% (2854) used as the evaluation set.

Control codes are symbols that are added to the ABC notation representation to indicate the desired musical form of the generated melodies. We add the following control codes to each ABC tune in the dataset through an automated process to indicate its musical form:

- Number of Bars (NB): controls the number of bars in a section of the melody. For example, users could specify that they want a section to contain 8 bars, and TunesFormer would generate a section that fits within that structure. It counts on the bar symbol ***|***.
- Number of Sections (NS): controls the number of sections in the entire melody. This can be used to create a sense of structure and coherence within the melody, as different sections can be used to create musical themes or motifs. It counts on several symbols that are commonly used in ABC notation and can be used to represent section boundaries: ***\[|***, ***||***, ***|\]***, ***|:***, ***::***, and ***:|***.
- Edit Distance Similarity (EDS): controls the similarity level between the current section and a previous section in the melody. 

To ensure consistency and standardization among the ABC tunes in the dataset, we first converted them all into MusicXML format and then re-converted them back into ABC notation. In order to focus solely on the musical content, we removed any natural language elements (such as titles, composers, and lyrics) and unnecessary information (such as reference numbers and sources).