---
language: de
license: other
---

# Inclusive words in German 🏳️‍🌈 🇩🇪

Pairs of words and phrases in exclusive language and alternative words and phrases in inclusive language.

Inclusivity aims to comprehend all [dimensions of diversity](https://www.charta-der-vielfalt.de/en/understanding-diversity/diversity-dimensions/) (age, ethnic background and nationality, gender and gender identity, physical and mental abilities, religion and worldview, sexual orientation, social background, and more); but currently focuses almost exclusively on **gender inclusion**, since gender exclusion is very dominant in German language.

## Dataset structure

**Train/test split:** There is no train/test split, just a "train" dataset.

- **`exclusive`**: Exclusive words and phrases in the singular. For the dimension of gender, these are certain words and phrases in the grammatical masculine. Note that the grammatical masculine is only exclusive if it is used in a _generic_ sense: "Die Doktoren" may be accurately used to describe three male doctors, but the same phrase is exclusive when it intends to refer to a group that also (potentially) includes women and nonbinary people. The relation between exclusive and inclusive phrases is n-to-n: An exclusive phrase may occur in multiple rows with various inclusive phrases associated, and vice versa.

- **`inclusive`**: Corresponding inclusive word or phrase that can replace the exclusive phrase. It may be applicable only in a certain context and not in others. Usually in the singular; where `number` is plural, it may be either in the singular or plural. The relation between exclusive and inclusive phrases is n-to-n: An inclusive phrase may occur in multiple rows with various exclusive phrases associated, and vice versa.

- **`applicable`**: One of `in_singular`, `in_plural`, or `always`. Specifies the grammatical number that the inclusive phrase must be found in such that it can be replaced by the inclusive phrase given in this entry.

  - _Special case:_ Some singular words (such as "Management" as a replacement for "Manager") occur in two rows, once with the attribute `always`, once with the attribute `plural`. The first means that "Manager"(singular) can be replaced with "Management" (singular) and "Manager" (plural) can be replaced with "Managements" (plural); the second means that "Manager" (plural) can (also) be replaced with "Management" (singular).

- **`gender_of_inclusive`**: Whether the inclusive phrase is semantically `neutral` or `female`. If it is female, it is not by itself inclusive but has to be combined with the male phrase (and potentially a character such as the gender star for representing nonbinary persons) to form a neutral phrase. (Since the male phrase is already given by the `exclusive` column, it is not repeated in the `inclusive` column due to potentially questionable ideological beliefs about data normalization.)

- **`source`**: The origin of the entry.

  - _geschicktgendern_: The entry has been copied from the _Genderwörterbuch_ by _Geschickt Gendern_. These entries are under a CC-BY-NC-SA 4.0 International License (c) Johanna Usinger, [geschicktgendern.de](https://geschicktgendern.de/).

  - _dereko_: The entry has been extracted from the German reference corpus [DeReKo](https://www.ids-mannheim.de/en/digspra/corpus-linguistics/projects/corpus-development/). Since these are single words only, copyright does not apply and the entries are under the CC-0 license.

  - _diversifix_: Entries added by ourselves or our community, also under the CC-0 license.

## Bias

The entries from the `dereko` source have been extracted according to their frequency in the corpus. This means, for example, that there are words referring to people from larger countries but not from some smaller countries; or, more accurately, countries that are considered important from the perspective of German-speaking journalism are more prevalent in the dataset.

## License

Mixed license. All data is open, but a part of it only noncommercially. See the description for the `source` column above for details.

## See also

- [Other data sources on inclusive German.](https://github.com/tech4germany/bam-inclusify/blob/main/doc/data.md)
- [retext-equality](https://github.com/retextjs/retext-equality) 🏳️‍🌈 🇬🇧
