---
annotations_creators:
- expert-generated
language_creators:
- found
license:
- cc-by-4.0
multilinguality:
- af-ZA
- am-ET
- ar-SA
- az-AZ
- bn-BD
- ca-ES
- cy-GB
- da-DK
- de-DE
- el-GR
- en-US
- es-ES
- fa-IR
- fi-FI
- fr-FR
- he-IL
- hi-IN
- hu-HU
- hy-AM
- id-ID
- is-IS
- it-IT
- ja-JP
- jv-ID
- ka-GE
- km-KH
- kn-IN
- ko-KR
- lv-LV
- ml-IN
- mn-MN
- ms-MY
- my-MM
- nb-NO
- nl-NL
- pl-PL
- pt-PT
- ro-RO
- ru-RU
- sl-SL
- sq-AL
- sv-SE
- sw-KE
- ta-IN
- te-IN
- th-TH
- tl-PH
- tr-TR
- ur-PK
- vi-VN
- zh-CN
- zh-TW
size_categories:
- 100K<n<1M
source_datasets:
- original
task_categories:
- text-classification
task_ids:
- intent-classification
- multi-class-classification
paperswithcode_id: massive
pretty_name: MASSIVE
language_bcp47:
- af-ZA
- am-ET
- ar-SA
- az-AZ
- bn-BD
- ca-ES
- cy-GB
- da-DK
- de-DE
- el-GR
- en-US
- es-ES
- fa-IR
- fi-FI
- fr-FR
- he-IL
- hi-IN
- hu-HU
- hy-AM
- id-ID
- is-IS
- it-IT
- ja-JP
- jv-ID
- ka-GE
- km-KH
- kn-IN
- ko-KR
- lv-LV
- ml-IN
- mn-MN
- ms-MY
- my-MM
- nb-NO
- nl-NL
- pl-PL
- pt-PT
- ro-RO
- ru-RU
- sl-SL
- sq-AL
- sv-SE
- sw-KE
- ta-IN
- te-IN
- th-TH
- tl-PH
- tr-TR
- ur-PK
- vi-VN
- zh-CN
- zh-TW
tags:
- natural-language-understanding
---

# MASSIVE 1.1: A 1M-Example Multilingual Natural Language Understanding Dataset with 52 Typologically-Diverse Languages

## Table of Contents
- [Dataset Card for [Needs More Information]](#dataset-card-for-needs-more-information)
  - [Table of Contents](#table-of-contents)
  - [Dataset Description](#dataset-description)
    - [Dataset Summary](#dataset-summary)
    - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
    - [Languages](#languages)
  - [Dataset Structure](#dataset-structure)
    - [Data Instances](#data-instances)
    - [Data Fields](#data-fields)
    - [Data Splits](#data-splits)
  - [Dataset Creation](#dataset-creation)
    - [Curation Rationale](#curation-rationale)
    - [Source Data](#source-data)
      - [Initial Data Collection and Normalization](#initial-data-collection-and-normalization)
      - [Who are the source language producers?](#who-are-the-source-language-producers)
    - [Personal and Sensitive Information](#personal-and-sensitive-information)
  - [Considerations for Using the Data](#considerations-for-using-the-data)
    - [Other Known Limitations](#other-known-limitations)
  - [Additional Information](#additional-information)
    - [Dataset Curators](#dataset-curators)
    - [Licensing Information](#licensing-information)
    - [No Warranty](#no-warranty)
    - [Citation Information](#citation-information)

## Dataset Description

- **Homepage:** https://github.com/alexa/massive
- **Repository:** https://github.com/alexa/massive
- **Paper:** https://arxiv.org/abs/2204.08582
- **Leaderboard:** https://eval.ai/web/challenges/challenge-page/1697/overview
- **Point of Contact:** [GitHub](https://github.com/alexa/massive/issues)

### Dataset Summary

MASSIVE 1.1 is a parallel dataset of > 1M utterances across 52 languages with annotations for the Natural Language Understanding tasks of intent prediction and slot annotation. Utterances span 60 intents and include 55 slot types. MASSIVE was created by localizing the SLURP dataset, composed of general Intelligent Voice Assistant single-shot interactions.

| Name | Lang  |    Utt/Lang    | Domains | Intents  |  Slots |
|:-------------------------------------------------------------------------------:|:-------:|:--------------:|:-------:|:--------:|:------:|
| MASSIVE 1.1                                                                     | 52      | 19,521         | 18      | 60       | 55     |
| SLURP (Bastianelli et al., 2020)                                                | 1       | 16,521         | 18      | 60       | 55     |
| NLU Evaluation Data (Liu et al., 2019)                                          | 1       | 25,716         | 18      | 54       | 56     |
| Airline Travel Information System (ATIS) (Price, 1990)                          | 1       | 5,871          | 1       | 26       | 129    |
| ATIS with Hindi and Turkish (Upadhyay et al., 2018)                             | 3       | 1,315-5,871    | 1       | 26       | 129    |
| MultiATIS++ (Xu et al., 2020)                                                   | 9       | 1,422-5,897    | 1       | 21-26    | 99-140 |
| Snips (Coucke et al., 2018)                                                     | 1       | 14,484         |  -      | 7        | 53     |
| Snips with French (Saade et al., 2019)                                          | 2       | 4,818          | 2       | 14-15    | 11-12  |
| Task Oriented Parsing (TOP) (Gupta et al., 2018)                                | 1       | 44,873         | 2       | 25       | 36     |
| Multilingual Task-Oriented Semantic Parsing (MTOP) (Li et al., 2021)            | 6       | 15,195-22,288  | 11      | 104-113  | 72-75  |
| Cross-Lingual Multilingual Task Oriented Dialog (Schuster et al., 2019)         | 3       | 5,083-43,323   | 3       | 12       | 11     |
| Microsoft Dialog Challenge (Li et al., 2018)                                    | 1       | 38,276         | 3       | 11       | 29     |
| Fluent Speech Commands (FSC) (Lugosch et al., 2019)                             | 1       | 30,043         |  -      | 31       |  -     |
| Chinese Audio-Textual Spoken Language Understanding (CATSLU) (Zhu et al., 2019) | 1       | 16,258         | 4       |  -       | 94     |

### Supported Tasks and Leaderboards

The dataset can be used to train a model for `natural-language-understanding` (NLU) :

- `intent-classification`
- `multi-class-classification`
- `natural-language-understanding`

### Languages

The MASSIVE 1.1 corpora consists of parallel sentences from 52 languages :

- `Afrikaans - South Africa (af-ZA)`
- `Amharic - Ethiopia (am-ET)`
- `Arabic - Saudi Arabia (ar-SA)`
- `Azeri - Azerbaijan (az-AZ)`
- `Bengali - Bangladesh (bn-BD)`
- `Catalan - Spain (ca-ES)`
- `Chinese - China (zh-CN)`
- `Chinese - Taiwan (zh-TW)`
- `Danish - Denmark (da-DK)`
- `German - Germany (de-DE)`
- `Greek - Greece (el-GR)`
- `English - United States (en-US)`
- `Spanish - Spain (es-ES)`
- `Farsi - Iran (fa-IR)`
- `Finnish - Finland (fi-FI)`
- `French - France (fr-FR)`
- `Hebrew - Israel (he-IL)`
- `Hungarian - Hungary (hu-HU)`
- `Armenian - Armenia (hy-AM)`
- `Indonesian - Indonesia (id-ID)`
- `Icelandic - Iceland (is-IS)`
- `Italian - Italy (it-IT)`
- `Japanese - Japan (ja-JP)`
- `Javanese - Indonesia (jv-ID)`
- `Georgian - Georgia (ka-GE)`
- `Khmer - Cambodia (km-KH)`
- `Korean - Korea (ko-KR)`
- `Latvian - Latvia (lv-LV)`
- `Mongolian - Mongolia (mn-MN)`
- `Malay - Malaysia (ms-MY)`
- `Burmese - Myanmar (my-MM)`
- `Norwegian - Norway (nb-NO)`
- `Dutch - Netherlands (nl-NL)`
- `Polish - Poland (pl-PL)`
- `Portuguese - Portugal (pt-PT)`
- `Romanian - Romania (ro-RO)`
- `Russian - Russia (ru-RU)`
- `Slovanian - Slovania (sl-SL)`
- `Albanian - Albania (sq-AL)`
- `Swedish - Sweden (sv-SE)`
- `Swahili - Kenya (sw-KE)`
- `Hindi - India (hi-IN)`
- `Kannada - India (kn-IN)`
- `Malayalam - India (ml-IN)`
- `Tamil - India (ta-IN)`
- `Telugu - India (te-IN)`
- `Thai - Thailand (th-TH)`
- `Tagalog - Philippines (tl-PH)`
- `Turkish - Turkey (tr-TR)`
- `Urdu - Pakistan (ur-PK)`
- `Vietnamese - Vietnam (vi-VN)`
- `Welsh - United Kingdom (cy-GB)`

## Load the dataset with HuggingFace

```python
from datasets import load_dataset
dataset = load_dataset("AmazonScience/massive", "en-US", split='train')
print(dataset[0])
```

## Dataset Structure

### Data Instances

```json
{
  "id": "0",
  "locale": "fr-FR",
  "partition": "test",
  "scenario": "alarm",
  "intent": "alarm_set",
  "utt": "réveille-moi à cinq heures du matin cette semaine",
  "annot_utt": "réveille-moi à [time : cinq heures du matin] [date : cette semaine]",
  "worker_id": "22",
  "slot_method": [
    { "slot": "time", "method": "translation" },
    { "slot": "date", "method": "translation" }
  ],
  "judgments": [
    {
      "worker_id": "22",
      "intent_score": 1,
      "slots_score": 1,
      "grammar_score": 4,
      "spelling_score": 2,
      "language_identification": "target"
    },
    {
      "worker_id": "8",
      "intent_score": 1,
      "slots_score": 1,
      "grammar_score": 4,
      "spelling_score": 2,
      "language_identification": "target"
    },
    {
      "worker_id": "0",
      "intent_score": 1,
      "slots_score": 1,
      "grammar_score": 4,
      "spelling_score": 2,
      "language_identification": "target"
    }
  ]
}
```

### Data Fields

`id`: maps to the original ID in the [SLURP](https://github.com/pswietojanski/slurp) collection. Mapping back to the SLURP en-US utterance, this utterance served as the basis for this localization.

`locale`: is the language and country code accoring to ISO-639-1 and ISO-3166.

`partition`: is either `train`, `dev`, or `test`, according to the original split in [SLURP](https://github.com/pswietojanski/slurp).

`scenario`: is the general domain, aka "scenario" in SLURP terminology, of an utterance

`intent`: is the specific intent of an utterance within a domain formatted as `{scenario}_{intent}`

`utt`: the raw utterance text without annotations

`annot_utt`: the text from `utt` with slot annotations formatted as `[{label} : {entity}]`

`worker_id`: The obfuscated worker ID from MTurk of the worker completing the localization of the utterance. Worker IDs are specific to a locale and do *not* map across locales.

`slot_method`: for each slot in the utterance, whether that slot was a `translation` (i.e., same expression just in the target language), `localization` (i.e., not the same expression but a different expression was chosen more suitable to the phrase in that locale), or `unchanged` (i.e., the original en-US slot value was copied over without modification).

`judgments`: Each judgment collected for the localized utterance has 6 keys. `worker_id` is the obfuscated worker ID from MTurk of the worker completing the judgment. Worker IDs are specific to a locale and do *not* map across locales, but *are* consistent across the localization tasks and the judgment tasks, e.g., judgment worker ID 32 in the example above may appear as the localization worker ID for the localization of a different de-DE utterance, in which case it would be the same worker.

```plain
intent_score : "Does the sentence match the intent?"
  0: No
  1: Yes
  2: It is a reasonable interpretation of the goal

slots_score : "Do all these terms match the categories in square brackets?"
  0: No
  1: Yes
  2: There are no words in square brackets (utterance without a slot)

grammar_score : "Read the sentence out loud. Ignore any spelling, punctuation, or capitalization errors. Does it sound natural?"
  0: Completely unnatural (nonsensical, cannot be understood at all)
  1: Severe errors (the meaning cannot be understood and doesn't sound natural in your language)
  2: Some errors (the meaning can be understood but it doesn't sound natural in your language)
  3: Good enough (easily understood and sounds almost natural in your language)
  4: Perfect (sounds natural in your language)

spelling_score : "Are all words spelled correctly? Ignore any spelling variances that may be due to differences in dialect. Missing spaces should be marked as a spelling error."
  0: There are more than 2 spelling errors
  1: There are 1-2 spelling errors
  2: All words are spelled correctly

language_identification : "The following sentence contains words in the following languages (check all that apply)"
  1: target
  2: english
  3: other
  4: target & english
  5: target & other
  6: english & other
  7: target & english & other
```

### Data Splits

|Language|Train|Dev|Test|
|:---:|:---:|:---:|:---:|
|af-ZA|11514|2033|2974|
|am-ET|11514|2033|2974|
|ar-SA|11514|2033|2974|
|az-AZ|11514|2033|2974|
|bn-BD|11514|2033|2974|
|ca-ES|11514|2033|2974|
|cy-GB|11514|2033|2974|
|da-DK|11514|2033|2974|
|de-DE|11514|2033|2974|
|el-GR|11514|2033|2974|
|en-US|11514|2033|2974|
|es-ES|11514|2033|2974|
|fa-IR|11514|2033|2974|
|fi-FI|11514|2033|2974|
|fr-FR|11514|2033|2974|
|he-IL|11514|2033|2974|
|hi-IN|11514|2033|2974|
|hu-HU|11514|2033|2974|
|hy-AM|11514|2033|2974|
|id-ID|11514|2033|2974|
|is-IS|11514|2033|2974|
|it-IT|11514|2033|2974|
|ja-JP|11514|2033|2974|
|jv-ID|11514|2033|2974|
|ka-GE|11514|2033|2974|
|km-KH|11514|2033|2974|
|kn-IN|11514|2033|2974|
|ko-KR|11514|2033|2974|
|lv-LV|11514|2033|2974|
|ml-IN|11514|2033|2974|
|mn-MN|11514|2033|2974|
|ms-MY|11514|2033|2974|
|my-MM|11514|2033|2974|
|nb-NO|11514|2033|2974|
|nl-NL|11514|2033|2974|
|pl-PL|11514|2033|2974|
|pt-PT|11514|2033|2974|
|ro-RO|11514|2033|2974|
|ru-RU|11514|2033|2974|
|sl-SL|11514|2033|2974|
|sq-AL|11514|2033|2974|
|sv-SE|11514|2033|2974|
|sw-KE|11514|2033|2974|
|ta-IN|11514|2033|2974|
|te-IN|11514|2033|2974|
|th-TH|11514|2033|2974|
|tl-PH|11514|2033|2974|
|tr-TR|11514|2033|2974|
|ur-PK|11514|2033|2974|
|vi-VN|11514|2033|2974|
|zh-CN|11514|2033|2974|
|zh-TW|11514|2033|2974|


### Personal and Sensitive Information

The corpora is free of personal or sensitive information.

## Additional Information

### Dataset Curators

__MASSIVE__: Jack FitzGerald and Christopher Hench and Charith Peris and Scott Mackie and Kay Rottmann and Ana Sanchez and Aaron Nash and Liam Urbach and Vishesh Kakarala and Richa Singh and Swetha Ranganath and Laurie Crist and Misha Britan and Wouter Leeuwis and Gokhan Tur and Prem Natarajan.

__SLURP__: Bastianelli, Emanuele and Vanzo, Andrea and Swietojanski, Pawel and Rieser, Verena.

__Hugging Face Upload and Integration__: Labrak Yanis (Not affiliated with the original corpus)

### Licensing Information

```plain
Copyright Amazon.com Inc. or its affiliates.

Attribution 4.0 International

=======================================================================

Creative Commons Corporation ("Creative Commons") is not a law firm and
does not provide legal services or legal advice. Distribution of
Creative Commons public licenses does not create a lawyer-client or
other relationship. Creative Commons makes its licenses and related
information available on an "as-is" basis. Creative Commons gives no
warranties regarding its licenses, any material licensed under their
terms and conditions, or any related information. Creative Commons
disclaims all liability for damages resulting from their use to the
fullest extent possible.

Using Creative Commons Public Licenses

Creative Commons public licenses provide a standard set of terms and
conditions that creators and other rights holders may use to share
original works of authorship and other material subject to copyright
and certain other rights specified in the public license below. The
following considerations are for informational purposes only, are not
exhaustive, and do not form part of our licenses.

     Considerations for licensors: Our public licenses are
     intended for use by those authorized to give the public
     permission to use material in ways otherwise restricted by
     copyright and certain other rights. Our licenses are
     irrevocable. Licensors should read and understand the terms
     and conditions of the license they choose before applying it.
     Licensors should also secure all rights necessary before
     applying our licenses so that the public can reuse the
     material as expected. Licensors should clearly mark any
     material not subject to the license. This includes other CC-
     licensed material, or material used under an exception or
     limitation to copyright. More considerations for licensors:
     wiki.creativecommons.org/Considerations_for_licensors

     Considerations for the public: By using one of our public
     licenses, a licensor grants the public permission to use the
     licensed material under specified terms and conditions. If
     the licensor's permission is not necessary for any reason--for
     example, because of any applicable exception or limitation to
     copyright--then that use is not regulated by the license. Our
     licenses grant only permissions under copyright and certain
     other rights that a licensor has authority to grant. Use of
     the licensed material may still be restricted for other
     reasons, including because others have copyright or other
     rights in the material. A licensor may make special requests,
     such as asking that all changes be marked or described.
     Although not required by our licenses, you are encouraged to
     respect those requests where reasonable. More considerations
     for the public:
     wiki.creativecommons.org/Considerations_for_licensees

=======================================================================

Creative Commons Attribution 4.0 International Public License

By exercising the Licensed Rights (defined below), You accept and agree
to be bound by the terms and conditions of this Creative Commons
Attribution 4.0 International Public License ("Public License"). To the
extent this Public License may be interpreted as a contract, You are
granted the Licensed Rights in consideration of Your acceptance of
these terms and conditions, and the Licensor grants You such rights in
consideration of benefits the Licensor receives from making the
Licensed Material available under these terms and conditions.


Section 1 -- Definitions.

  a. Adapted Material means material subject to Copyright and Similar
     Rights that is derived from or based upon the Licensed Material
     and in which the Licensed Material is translated, altered,
     arranged, transformed, or otherwise modified in a manner requiring
     permission under the Copyright and Similar Rights held by the
     Licensor. For purposes of this Public License, where the Licensed
     Material is a musical work, performance, or sound recording,
     Adapted Material is always produced where the Licensed Material is
     synched in timed relation with a moving image.

  b. Adapter's License means the license You apply to Your Copyright
     and Similar Rights in Your contributions to Adapted Material in
     accordance with the terms and conditions of this Public License.

  c. Copyright and Similar Rights means copyright and/or similar rights
     closely related to copyright including, without limitation,
     performance, broadcast, sound recording, and Sui Generis Database
     Rights, without regard to how the rights are labeled or
     categorized. For purposes of this Public License, the rights
     specified in Section 2(b)(1)-(2) are not Copyright and Similar
     Rights.

  d. Effective Technological Measures means those measures that, in the
     absence of proper authority, may not be circumvented under laws
     fulfilling obligations under Article 11 of the WIPO Copyright
     Treaty adopted on December 20, 1996, and/or similar international
     agreements.

  e. Exceptions and Limitations means fair use, fair dealing, and/or
     any other exception or limitation to Copyright and Similar Rights
     that applies to Your use of the Licensed Material.

  f. Licensed Material means the artistic or literary work, database,
     or other material to which the Licensor applied this Public
     License.

  g. Licensed Rights means the rights granted to You subject to the
     terms and conditions of this Public License, which are limited to
     all Copyright and Similar Rights that apply to Your use of the
     Licensed Material and that the Licensor has authority to license.

  h. Licensor means the individual(s) or entity(ies) granting rights
     under this Public License.

  i. Share means to provide material to the public by any means or
     process that requires permission under the Licensed Rights, such
     as reproduction, public display, public performance, distribution,
     dissemination, communication, or importation, and to make material
     available to the public including in ways that members of the
     public may access the material from a place and at a time
     individually chosen by them.

  j. Sui Generis Database Rights means rights other than copyright
     resulting from Directive 96/9/EC of the European Parliament and of
     the Council of 11 March 1996 on the legal protection of databases,
     as amended and/or succeeded, as well as other essentially
     equivalent rights anywhere in the world.

  k. You means the individual or entity exercising the Licensed Rights
     under this Public License. Your has a corresponding meaning.


Section 2 -- Scope.

  a. License grant.

       1. Subject to the terms and conditions of this Public License,
          the Licensor hereby grants You a worldwide, royalty-free,
          non-sublicensable, non-exclusive, irrevocable license to
          exercise the Licensed Rights in the Licensed Material to:

            a. reproduce and Share the Licensed Material, in whole or
               in part; and

            b. produce, reproduce, and Share Adapted Material.

       2. Exceptions and Limitations. For the avoidance of doubt, where
          Exceptions and Limitations apply to Your use, this Public
          License does not apply, and You do not need to comply with
          its terms and conditions.

       3. Term. The term of this Public License is specified in Section
          6(a).

       4. Media and formats; technical modifications allowed. The
          Licensor authorizes You to exercise the Licensed Rights in
          all media and formats whether now known or hereafter created,
          and to make technical modifications necessary to do so. The
          Licensor waives and/or agrees not to assert any right or
          authority to forbid You from making technical modifications
          necessary to exercise the Licensed Rights, including
          technical modifications necessary to circumvent Effective
          Technological Measures. For purposes of this Public License,
          simply making modifications authorized by this Section 2(a)
          (4) never produces Adapted Material.

       5. Downstream recipients.

            a. Offer from the Licensor -- Licensed Material. Every
               recipient of the Licensed Material automatically
               receives an offer from the Licensor to exercise the
               Licensed Rights under the terms and conditions of this
               Public License.

            b. No downstream restrictions. You may not offer or impose
               any additional or different terms or conditions on, or
               apply any Effective Technological Measures to, the
               Licensed Material if doing so restricts exercise of the
               Licensed Rights by any recipient of the Licensed
               Material.

       6. No endorsement. Nothing in this Public License constitutes or
          may be construed as permission to assert or imply that You
          are, or that Your use of the Licensed Material is, connected
          with, or sponsored, endorsed, or granted official status by,
          the Licensor or others designated to receive attribution as
          provided in Section 3(a)(1)(A)(i).

  b. Other rights.

       1. Moral rights, such as the right of integrity, are not
          licensed under this Public License, nor are publicity,
          privacy, and/or other similar personality rights; however, to
          the extent possible, the Licensor waives and/or agrees not to
          assert any such rights held by the Licensor to the limited
          extent necessary to allow You to exercise the Licensed
          Rights, but not otherwise.

       2. Patent and trademark rights are not licensed under this
          Public License.

       3. To the extent possible, the Licensor waives any right to
          collect royalties from You for the exercise of the Licensed
          Rights, whether directly or through a collecting society
          under any voluntary or waivable statutory or compulsory
          licensing scheme. In all other cases the Licensor expressly
          reserves any right to collect such royalties.


Section 3 -- License Conditions.

Your exercise of the Licensed Rights is expressly made subject to the
following conditions.

  a. Attribution.

       1. If You Share the Licensed Material (including in modified
          form), You must:

            a. retain the following if it is supplied by the Licensor
               with the Licensed Material:

                 i. identification of the creator(s) of the Licensed
                    Material and any others designated to receive
                    attribution, in any reasonable manner requested by
                    the Licensor (including by pseudonym if
                    designated);

                ii. a copyright notice;

               iii. a notice that refers to this Public License;

                iv. a notice that refers to the disclaimer of
                    warranties;

                 v. a URI or hyperlink to the Licensed Material to the
                    extent reasonably practicable;

            b. indicate if You modified the Licensed Material and
               retain an indication of any previous modifications; and

            c. indicate the Licensed Material is licensed under this
               Public License, and include the text of, or the URI or
               hyperlink to, this Public License.

       2. You may satisfy the conditions in Section 3(a)(1) in any
          reasonable manner based on the medium, means, and context in
          which You Share the Licensed Material. For example, it may be
          reasonable to satisfy the conditions by providing a URI or
          hyperlink to a resource that includes the required
          information.

       3. If requested by the Licensor, You must remove any of the
          information required by Section 3(a)(1)(A) to the extent
          reasonably practicable.

       4. If You Share Adapted Material You produce, the Adapter's
          License You apply must not prevent recipients of the Adapted
          Material from complying with this Public License.


Section 4 -- Sui Generis Database Rights.

Where the Licensed Rights include Sui Generis Database Rights that
apply to Your use of the Licensed Material:

  a. for the avoidance of doubt, Section 2(a)(1) grants You the right
     to extract, reuse, reproduce, and Share all or a substantial
     portion of the contents of the database;

  b. if You include all or a substantial portion of the database
     contents in a database in which You have Sui Generis Database
     Rights, then the database in which You have Sui Generis Database
     Rights (but not its individual contents) is Adapted Material; and

  c. You must comply with the conditions in Section 3(a) if You Share
     all or a substantial portion of the contents of the database.

For the avoidance of doubt, this Section 4 supplements and does not
replace Your obligations under this Public License where the Licensed
Rights include other Copyright and Similar Rights.


Section 5 -- Disclaimer of Warranties and Limitation of Liability.

  a. UNLESS OTHERWISE SEPARATELY UNDERTAKEN BY THE LICENSOR, TO THE
     EXTENT POSSIBLE, THE LICENSOR OFFERS THE LICENSED MATERIAL AS-IS
     AND AS-AVAILABLE, AND MAKES NO REPRESENTATIONS OR WARRANTIES OF
     ANY KIND CONCERNING THE LICENSED MATERIAL, WHETHER EXPRESS,
     IMPLIED, STATUTORY, OR OTHER. THIS INCLUDES, WITHOUT LIMITATION,
     WARRANTIES OF TITLE, MERCHANTABILITY, FITNESS FOR A PARTICULAR
     PURPOSE, NON-INFRINGEMENT, ABSENCE OF LATENT OR OTHER DEFECTS,
     ACCURACY, OR THE PRESENCE OR ABSENCE OF ERRORS, WHETHER OR NOT
     KNOWN OR DISCOVERABLE. WHERE DISCLAIMERS OF WARRANTIES ARE NOT
     ALLOWED IN FULL OR IN PART, THIS DISCLAIMER MAY NOT APPLY TO YOU.

  b. TO THE EXTENT POSSIBLE, IN NO EVENT WILL THE LICENSOR BE LIABLE
     TO YOU ON ANY LEGAL THEORY (INCLUDING, WITHOUT LIMITATION,
     NEGLIGENCE) OR OTHERWISE FOR ANY DIRECT, SPECIAL, INDIRECT,
     INCIDENTAL, CONSEQUENTIAL, PUNITIVE, EXEMPLARY, OR OTHER LOSSES,
     COSTS, EXPENSES, OR DAMAGES ARISING OUT OF THIS PUBLIC LICENSE OR
     USE OF THE LICENSED MATERIAL, EVEN IF THE LICENSOR HAS BEEN
     ADVISED OF THE POSSIBILITY OF SUCH LOSSES, COSTS, EXPENSES, OR
     DAMAGES. WHERE A LIMITATION OF LIABILITY IS NOT ALLOWED IN FULL OR
     IN PART, THIS LIMITATION MAY NOT APPLY TO YOU.

  c. The disclaimer of warranties and limitation of liability provided
     above shall be interpreted in a manner that, to the extent
     possible, most closely approximates an absolute disclaimer and
     waiver of all liability.


Section 6 -- Term and Termination.

  a. This Public License applies for the term of the Copyright and
     Similar Rights licensed here. However, if You fail to comply with
     this Public License, then Your rights under this Public License
     terminate automatically.

  b. Where Your right to use the Licensed Material has terminated under
     Section 6(a), it reinstates:

       1. automatically as of the date the violation is cured, provided
          it is cured within 30 days of Your discovery of the
          violation; or

       2. upon express reinstatement by the Licensor.

     For the avoidance of doubt, this Section 6(b) does not affect any
     right the Licensor may have to seek remedies for Your violations
     of this Public License.

  c. For the avoidance of doubt, the Licensor may also offer the
     Licensed Material under separate terms or conditions or stop
     distributing the Licensed Material at any time; however, doing so
     will not terminate this Public License.

  d. Sections 1, 5, 6, 7, and 8 survive termination of this Public
     License.


Section 7 -- Other Terms and Conditions.

  a. The Licensor shall not be bound by any additional or different
     terms or conditions communicated by You unless expressly agreed.

  b. Any arrangements, understandings, or agreements regarding the
     Licensed Material not stated herein are separate from and
     independent of the terms and conditions of this Public License.


Section 8 -- Interpretation.

  a. For the avoidance of doubt, this Public License does not, and
     shall not be interpreted to, reduce, limit, restrict, or impose
     conditions on any use of the Licensed Material that could lawfully
     be made without permission under this Public License.

  b. To the extent possible, if any provision of this Public License is
     deemed unenforceable, it shall be automatically reformed to the
     minimum extent necessary to make it enforceable. If the provision
     cannot be reformed, it shall be severed from this Public License
     without affecting the enforceability of the remaining terms and
     conditions.

  c. No term or condition of this Public License will be waived and no
     failure to comply consented to unless expressly agreed to by the
     Licensor.

  d. Nothing in this Public License constitutes or may be interpreted
     as a limitation upon, or waiver of, any privileges and immunities
     that apply to the Licensor or You, including from the legal
     processes of any jurisdiction or authority.


=======================================================================

Creative Commons is not a party to its public licenses.
Notwithstanding, Creative Commons may elect to apply one of its public
licenses to material it publishes and in those instances will be
considered the “Licensor.” The text of the Creative Commons public
licenses is dedicated to the public domain under the CC0 Public Domain
Dedication. Except for the limited purpose of indicating that material
is shared under a Creative Commons public license or as otherwise
permitted by the Creative Commons policies published at
creativecommons.org/policies, Creative Commons does not authorize the
use of the trademark "Creative Commons" or any other trademark or logo
of Creative Commons without its prior written consent including,
without limitation, in connection with any unauthorized modifications
to any of its public licenses or any other arrangements,
understandings, or agreements concerning use of licensed material. For
the avoidance of doubt, this paragraph does not form part of the public
licenses.

Creative Commons may be contacted at creativecommons.org.
```

### Citation Information

Please cite the following papers when using this dataset.

```latex
@misc{fitzgerald2022massive,
      title={MASSIVE: A 1M-Example Multilingual Natural Language Understanding Dataset with 51 Typologically-Diverse Languages},
      author={Jack FitzGerald and Christopher Hench and Charith Peris and Scott Mackie and Kay Rottmann and Ana Sanchez and Aaron Nash and Liam Urbach and Vishesh Kakarala and Richa Singh and Swetha Ranganath and Laurie Crist and Misha Britan and Wouter Leeuwis and Gokhan Tur and Prem Natarajan},
      year={2022},
      eprint={2204.08582},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}

@inproceedings{bastianelli-etal-2020-slurp,
    title = "{SLURP}: A Spoken Language Understanding Resource Package",
    author = "Bastianelli, Emanuele  and
      Vanzo, Andrea  and
      Swietojanski, Pawel  and
      Rieser, Verena",
    booktitle = "Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.emnlp-main.588",
    doi = "10.18653/v1/2020.emnlp-main.588",
    pages = "7252--7262",
    abstract = "Spoken Language Understanding infers semantic meaning directly from audio data, and thus promises to reduce error propagation and misunderstandings in end-user applications. However, publicly available SLU resources are limited. In this paper, we release SLURP, a new SLU package containing the following: (1) A new challenging dataset in English spanning 18 domains, which is substantially bigger and linguistically more diverse than existing datasets; (2) Competitive baselines based on state-of-the-art NLU and ASR systems; (3) A new transparent metric for entity labelling which enables a detailed error analysis for identifying potential areas of improvement. SLURP is available at https://github.com/pswietojanski/slurp."
}
```
