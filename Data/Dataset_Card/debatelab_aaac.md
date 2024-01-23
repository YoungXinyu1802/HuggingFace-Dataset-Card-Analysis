---
annotations_creators:
- machine-generated
- expert-generated
language_creators:
- machine-generated
language:
- en
license:
- cc-by-sa-4.0
multilinguality:
- monolingual
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories:
- summarization
- text-retrieval
- text-generation
task_ids:
- parsing
- text-simplification
paperswithcode_id: aaac
pretty_name: Artificial Argument Analysis Corpus
language_bcp47:
- en-US
tags:
- argument-mining
- conditional-text-generation
- structure-prediction
---

# Dataset Card for Artificial Argument Analysis Corpus (AAAC)

## Table of Contents
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
  - [Construction of the Synthetic Data](#construction-of-the-synthetic-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Homepage:** https://debatelab.github.io/journal/deepa2.html
- **Repository:** None
- **Paper:** G. Betz, K. Richardson. *DeepA2: A Modular Framework for Deep Argument Analysis with Pretrained Neural Text2Text Language Models*. https://arxiv.org/abs/2110.01509
- **Leaderboard:** None

### Dataset Summary

DeepA2 is a modular framework for deep argument analysis. DeepA2 datasets contain comprehensive logical reconstructions of informally presented arguments in short argumentative texts. This document describes two synthetic DeepA2 datasets for artificial argument analysis: AAAC01 and AAAC02.

```sh
# clone
git lfs clone https://huggingface.co/datasets/debatelab/aaac
```

```python
import pandas as pd
from datasets import Dataset
# loading train split as pandas df
df = pd.read_json("aaac/aaac01_train.jsonl", lines=True, orient="records")
# creating dataset from pandas df
Dataset.from_pandas(df)
```

### Supported Tasks and Leaderboards

The multi-dimensional datasets can be used to define various text-2-text tasks (see also [Betz and Richardson 2021](https://arxiv.org/abs/2110.01509)), for example:

* Premise extraction,
* Conclusion extraction,
* Logical formalization,
* Logical reconstrcution.


### Languages

English.

## Dataset Structure

### Data Instances

The following histograms (number of dataset records with given property) describe and compare the two datasets AAAC01 (train split, N=16000) and AAAC02 (dev split, N=4000).

|AAAC01 / train split|AAAC02 / dev split|
|-|-|
|![domains](https://huggingface.co/datasets/debatelab/aaac/resolve/main/img/st_domains_aaac01.png) |![domains](https://huggingface.co/datasets/debatelab/aaac/resolve/main/img/st_domains_aaac02.png) |
|![schemes](https://huggingface.co/datasets/debatelab/aaac/resolve/main/img/st_schemes_aaac01.png) |![schemes](https://huggingface.co/datasets/debatelab/aaac/resolve/main/img/st_schemes_aaac02.png) |
|![var](https://huggingface.co/datasets/debatelab/aaac/resolve/main/img/st_sch-vars_aaac01.png) |![domains](https://huggingface.co/datasets/debatelab/aaac/resolve/main/img/st_sch-vars_aaac02.png) |
|![steps](https://huggingface.co/datasets/debatelab/aaac/resolve/main/img/st_steps_aaac01.png) |![steps](https://huggingface.co/datasets/debatelab/aaac/resolve/main/img/st_steps_aaac02.png) |
|![prem](https://huggingface.co/datasets/debatelab/aaac/resolve/main/img/st_prem_aaac01.png) |![prem](https://huggingface.co/datasets/debatelab/aaac/resolve/main/img/st_prem_aaac02.png) |
|![impl prem](https://huggingface.co/datasets/debatelab/aaac/resolve/main/img/st_impl-prem_aaac01.png) |![impl prem](https://huggingface.co/datasets/debatelab/aaac/resolve/main/img/st_impl-prem_aaac02.png) |
|![impl fc](https://huggingface.co/datasets/debatelab/aaac/resolve/main/img/st_impl-fc_aaac01.png) |![impl fc](https://huggingface.co/datasets/debatelab/aaac/resolve/main/img/st_impl-fc_aaac02.png) |
|![dist](https://huggingface.co/datasets/debatelab/aaac/resolve/main/img/st_distr_aaac01.png) |![dist](https://huggingface.co/datasets/debatelab/aaac/resolve/main/img/st_distr_aaac02.png) |


### Data Fields

The following multi-dimensional example record (2-step argument with one implicit premise) illustrates the structure of the AAAC datasets. 


#### argument_source

```
If someone was discovered in 'Moonlight', then they won't play the lead in 'Booksmart',
because being a candidate for the lead in 'Booksmart' is sufficient for not being an
Oscar-Nominee for a role in 'Eighth Grade'. Yet every BAFTA-Nominee for a role in 'The
Shape of Water' is a fan-favourite since 'Moonlight' or a supporting actor in 'Black Panther'.
And if someone is a supporting actor in 'Black Panther', then they could never become the
main actor in 'Booksmart'. Consequently, if someone is a BAFTA-Nominee for a role in
'The Shape of Water', then they are not a candidate for the lead in 'Booksmart'.
```


#### reason_statements

```json
[
    {"text":"being a candidate for the lead in 'Booksmart' is sufficient for 
    not being an Oscar-Nominee for a role in 'Eighth Grade'","starts_at":96,
    "ref_reco":2},
    {"text":"every BAFTA-Nominee for a role in 'The Shape of Water' is a 
    fan-favourite since 'Moonlight' or a supporting actor in 'Black Panther'", 
    "starts_at":221,"ref_reco":4},
    {"text":"if someone is a supporting actor in 'Black Panther', then they 
    could never become the main actor in 'Booksmart'","starts_at":359, 
    "ref_reco":5}
]
```

#### conclusion_statements

```json
[
    {"text":"If someone was discovered in 'Moonlight', then they won't play the 
    lead in 'Booksmart'","starts_at":0,"ref_reco":3},
    {"text":"if someone is a BAFTA-Nominee for a role in 'The Shape of Water', 
    then they are not a candidate for the lead in 'Booksmart'","starts_at":486,
    "ref_reco":6}
]
```

#### distractors

`[]`

#### argdown_reconstruction

```
(1) If someone is a fan-favourite since 'Moonlight', then they are an Oscar-Nominee for a role in 'Eighth Grade'.
(2) If someone is a candidate for the lead in 'Booksmart', then they are not an Oscar-Nominee for a role in 'Eighth Grade'.
--
with hypothetical syllogism {variant: ["negation variant", "transposition"], uses: [1,2]}
--
(3) If someone is beloved for their role in 'Moonlight', then they don't audition in 
'Booksmart'.
(4) If someone is a BAFTA-Nominee for a role in 'The Shape of Water', then they are a fan-favourite since 'Moonlight' or a supporting actor in 'Black Panther'.
(5) If someone is a supporting actor in 'Black Panther', then they don't audition in 
'Booksmart'.
--
with generalized dilemma {variant: ["negation variant"], uses: [3,4,5]}
--
(6) If someone is a BAFTA-Nominee for a role in 'The Shape of Water', then they are not a 
candidate for the lead in 'Booksmart'.
```

#### premises

```json
[
    {"ref_reco":1,"text":"If someone is a fan-favourite since 'Moonlight', then 
    they are an Oscar-Nominee for a role in 'Eighth Grade'.","explicit":false},
    {"ref_reco":2,"text":"If someone is a candidate for the lead in 
    'Booksmart', then they are not an Oscar-Nominee for a role in 'Eighth 
    Grade'.","explicit":true},
    {"ref_reco":4,"text":"If someone is a BAFTA-Nominee for a role in 'The 
    Shape of Water', then they are a fan-favourite since 'Moonlight' or a 
    supporting actor in 'Black Panther'.","explicit":true},
    {"ref_reco":5,"text":"If someone is a supporting actor in 'Black Panther', 
    then they don't audition in 'Booksmart'.","explicit":true}
]
```

#### premises_formalized

```json
[
    {"form":"(x): ${F2}x -> ${F5}x","ref_reco":1},
    {"form":"(x): ${F4}x -> ¬${F5}x","ref_reco":2},
    {"form":"(x): ${F1}x -> (${F2}x v ${F3}x)","ref_reco":4},
    {"form":"(x): ${F3}x -> ¬${F4}x","ref_reco":5}
]
```

#### conclusion

```json 
[{"ref_reco":6,"text":"If someone is a BAFTA-Nominee for a role in 'The Shape 
of Water', then they are not a candidate for the lead in 'Booksmart'.", 
"explicit":true}]
```

#### conclusion_formalized

```json
[{"form":"(x): ${F1}x -> ¬${F4}x","ref_reco":6}]
```

#### intermediary_conclusions

```json
[{"ref_reco":3,"text":"If someone is beloved for their role in 'Moonlight', 
then they don't audition in 'Booksmart'.","explicit":true}]
```

#### intermediary_conclusions_formalized

```json 
[{"form":"(x): ${F2}x -> ¬${F4}x","ref_reco":3}]
```


#### plcd_subs

```json
{
    "F1":"BAFTA-Nominee for a role in 'The Shape of Water'",
    "F2":"fan-favourite since 'Moonlight'",
    "F3":"supporting actor in 'Black Panther'",
    "F4":"candidate for the lead in 'Booksmart'",
    "F5":"Oscar-Nominee for a role in 'Eighth Grade'"
}
```


### Data Splits

Number of instances in the various splits:

| Split | AAAC01 | AAAC02 |
| :---         |     :---:      |     :---:     |
| TRAIN   | 16,000     | 16,000    |
| DEV     | 4,000       | 4,000      |
| TEST     | 4,000       | 4,000      |

To correctly load a specific split, define `data_files` as follows:

```python
>>> data_files = {"train": "aaac01_train.jsonl", "eval": "aaac01_dev.jsonl", "test": "aaac01_test.jsonl"}
>>> dataset = load_dataset("debatelab/aaac", data_files=data_files)
```

## Dataset Creation

### Curation Rationale

Argument analysis refers to the interpretation and logical reconstruction of argumentative texts. Its goal is to make an argument transparent, so as to understand, appreciate and (possibly) criticize it. Argument analysis is a key critical thinking skill.

Here's a first example of an informally presented argument, **Descartes' Cogito**:

> I have convinced myself that there is absolutely nothing in the world, no sky, no earth, no minds, no bodies. Does it now follow that I too do not exist? No: if I convinced myself of something then I certainly existed. But there is a deceiver of supreme power and cunning who is deliberately and constantly deceiving me. In that case I too undoubtedly exist, if he is deceiving me; and let him deceive me as much as he can, he will never bring it about that I am nothing so long as I think that I am something. So after considering everything very thoroughly, I must finally conclude that this proposition, I am, I exist, is necessarily true whenever it is put forward by me or conceived in my mind. (AT 7:25, CSM 2:16f)

And here's a second example, taken from the *Debater's Handbook*, **Pro Censorship**:

> Freedom of speech is never an absolute right but an aspiration. It ceases to be a right when it causes harm to others -- we all recognise the value of, for example, legislating against incitement to racial hatred. Therefore it is not the case that censorship is wrong in principle.

Given such texts, argument analysis aims at answering the following questions:

1. Does the text present an argument?
2. If so, how many?
3. What is the argument supposed to show (conclusion)?
4. What exactly are the premises of the argument?
    * Which statements, explicit in the text, are not relevant for the argument?
    * Which premises are required, but not explicitly stated?
5. Is the argument deductively valid, inductively strong, or simply fallacious?

To answer these questions, argument analysts **interpret** the text by (re-)constructing its argument in a standardized way (typically as a premise-conclusion list) and by making use of logical streamlining and formalization.

A reconstruction of **Pro Censorship** which answers the above questions is:

```argdown
(1) Freedom of speech is never an absolute right but an aspiration.
(2) Censorship is wrong in principle only if freedom of speech is an 
    absolute right.
--with modus tollens--
(3) It is not the case that censorship is wrong in principle
```

There are typically multiple, more or less different interpretations and logical reconstructions of an argumentative text. For instance, there exists an [extensive debate](https://plato.stanford.edu/entries/descartes-epistemology/) about how to interpret **Descartes' Cogito**, and scholars have advanced rival interpretation of the argument. An alternative reconstruction of the much simpler **Pro Censorship** might read:

```argdown
(1) Legislating against incitement to racial hatred is valuable.
(2) Legislating against incitement to racial hatred is an instance of censorship.
(3) If some instance of censorship is valuable, censorship is not wrong in
    principle.
-----
(4) Censorship is not wrong in principle.
(5) Censorship is wrong in principle only if and only if freedom of speech 
    is an absolute right.
-----
(4) Freedom of speech is not an absolute right.
(5) Freedom of speech is an absolute right or an aspiration.
--with disjunctive syllogism--
(6) Freedom of speech is an aspiration.
```

What are the main reasons for this kind of underdetermination?

* **Incompleteness.** Many relevant parts of an argument (statements, their function in the argument, inference rules, argumentative goals) are not stated in its informal presentation. The argument analyst must infer the missing parts.
* **Additional material.** Over and above what is strictly part of the argument, informal presentations contain typically further material: relevant premises are repeated in slightly different ways, further examples are added to illustrate a point, statements are contrasted with views by opponents, etc. etc. It's argument analyst to choice which of the presented material is really part of the argument.
* **Errors.** Authors may err in the presentation of an argument, confounding, e.g., necessary and sufficient conditions in stating a premise. Following the principle of charity, benevolent argument analysts correct such errors and have to choose on of the different ways for how to do so.
* **Linguistic indeterminacy.** One and the same statement can be interpreted -- regarding its logical form -- in different ways.
* **Equivalence.** There are different natural language expressions for one and the same proposition.

AAAC datasets provide logical reconstructions of informal argumentative texts: Each record contains a source text to-be-reconstructed and further fields which describe an internally consistent interpretation of the text, notwithstanding the fact that there might be alternative interpretations of this very text.


### Construction of the Synthetic Data

Argument analysis starts with a text and reconstructs its argument (cf. [Motivation and Background](#curation-rationale)). In constructing our synthetic data, we inverse this direction: We start by sampling a complete argument, construct an informal presentation, and provide further info that describes both logical reconstruction and informal presentation. More specifically, the construction of the data involves the following steps:

1. [Generation of valid symbolic inference schemes](#step-1-generation-of-symbolic-inference-schemes)
2. [Assembling complex ("multi-hop") argument schemes from symbolic inference schemes](#step-2-assembling-complex-multi-hop-argument-schemes-from-symbolic-inference-schemes)
3. [Creation of (precise and informal) natural-language argument](#step-3-creation-of-precise-and-informal-natural-language-argument-schemes)
4. [Substitution of placeholders with domain-specific predicates and names](#step-4-substitution-of-placeholders-with-domain-specific-predicates-and-names)
5. [Creation of the argdown-snippet](#step-5-creation-of-the-argdown-snippet)
7. [Paraphrasing](#step-6-paraphrasing)
6. [Construction of a storyline for the argument source text](#step-7-construction-of-a-storyline-for-the-argument-source-text)
8. [Assembling the argument source text](#step-8-assembling-the-argument-source-text)
9. [Linking the precise reconstruction and the informal argumentative text](#step-9-linking-informal-presentation-and-formal-reconstruction)



#### Step 1: Generation of symbolic inference schemes

We construct the set of available inference schemes by systematically transforming the following 12 base schemes (6 from propositional and another 6 from predicate logic):

* modus ponens: `['Fa -> Gb', 'Fa', 'Gb']`
* chain rule: `['Fa -> Gb', 'Gb -> Hc', 'Fa -> Hc']`
* adjunction: `['Fa', 'Gb', 'Fa & Gb']`
* case analysis: `['Fa v Gb', 'Fa -> Hc', 'Gb -> Hc', 'Hc']`
* disjunctive syllogism: `['Fa v Gb', '¬Fa', 'Gb']`
* biconditional elimination: `['Fa <-> Gb', 'Fa -> Gb']`
* instantiation: `['(x): Fx -> Gx', 'Fa -> Ga']`
* hypothetical syllogism: `['(x): Fx -> Gx', '(x): Gx -> Hx', '(x): Fx -> Hx']`
* generalized biconditional elimination: `['(x): Fx <-> Gx', '(x): Fx -> Gx']`
* generalized adjunction: `['(x): Fx -> Gx', '(x): Fx -> Hx', '(x): Fx -> (Gx & Hx)']`
* generalized dilemma: `['(x): Fx -> (Gx v Hx)', '(x): Gx -> Ix', '(x): Hx -> Ix', '(x): Fx -> Ix']`
* generalized disjunctive syllogism: `['(x): Fx -> (Gx v Hx)', '(x): Fx -> ¬Gx', '(x): Fx -> Hx']`

(Regarding the propositional schemes, we allow for `a`=`b`=`c`.)

Further symbolic inference schemes are generated by applying the following transformations to each of these base schemes:

* *negation*: replace all occurrences of an atomic formula by its negation (for any number of such atomic sentences)
* *transposition*: transpose exactly one (generalized) conditional 
* *dna*: simplify by applying duplex negatio affirmat
* *complex predicates*: replace all occurrences of a given atomic formula by a complex formula consisting in the conjunction or disjunction of two atomic formulas
* *de morgan*: apply de Morgan's rule once

These transformations are applied to the base schemes in the following order:

> **{base_schemes}** > negation_variants > transposition_variants > dna > **{transposition_variants}** > complex_predicates > negation_variants > dna > **{complex_predicates}** > de_morgan > dna > **{de_morgan}**

All transformations, except *dna*, are monotonic, i.e. simply add further schemes to the ones generated in the previous step. Results of bold steps are added to the list of valid inference schemes. Each inference scheme is stored with information about which transformations were used to create it. All in all, this gives us 5542 schemes.


#### Step 2: Assembling complex ("multi-hop") argument schemes from symbolic inference schemes

The complex argument *scheme*, which consists in multiple inferences, is assembled recursively by adding inferences that support premises of previously added inferences, as described by the following pseudocode:

```
argument = []
intermediary_conclusion = []
inference = randomly choose from list of all schemes
add inference to argument  
for i in range(number_of_sub_arguments - 1):
    target = randomly choose a premise which is not an intermediary_conclusion
    inference = randomly choose a scheme whose conclusion is identical with target
    add inference to argument  
    add target to intermediary_conclusion
return argument
```

The complex arguments we create are hence trees, with a root scheme. 

Let's walk through this algorithm by means of an illustrative example and construct a symbolic argument scheme with two sub-arguments. First, we randomly choose some inference scheme (random sampling is controlled by weights that compensate for the fact that the list of schemes mainly contains, for combinatorial reasons, complex inferences), say:

```json
{
  "id": "mp",
  "base_scheme_group": "modus ponens",
  "scheme_variant": ["complex_variant"],
  "scheme": [
      ["${A}${a} -> (${B}${a} & ${C}${a})", 
        {"A": "${F}", "B": "${G}", "C": "${H}", "a": "${a}"}],
      ["${A}${a}", {"A": "${F}", "a": "${a}"}],
      ["${A}${a} & ${B}${a}", {"A": "${G}", "B": "${H}", "a": "${a}"}]
    ],
  "predicate-placeholders": ["F", "G", "H"],
  "entity-placeholders": ["a"]
}
```

Now, the target premise (= intermediary conclusion) of the next subargument is chosen, say: premise 1 of the already added root scheme. We filter the list of schemes for schemes whose conclusion structurally matches the target, i.e. has the form `${A}${a} -> (${B}${a} v ${C}${a})`. From this filtered list of suitable schemes, we randomly choose, for example

```json
{
    "id": "bicelim",
    "base_scheme_group": "biconditional elimination",
    "scheme_variant": [complex_variant],
    "scheme": [
      ["${A}${a} <-> (${B}${a} & ${C}${a})", 
        {"A": "${F}", "B": "${G}", "C": "${H}", "a": "${a}"}],
      ["${A}${a} -> (${B}${a} & ${C}${a})", 
        {"A": "${F}", "B": "${G}", "C": "${H}", "a": "${a}"}]
    ],
    "predicate-placeholders": ["F", "G", "H"],
    "entity-placeholders": []
}
``` 

So, we have generated this 2-step symbolic argument scheme with two premises, one intermediary and one final conclusion:

```
(1) Fa <-> Ga & Ha
--
with biconditional elimination (complex variant) from 1
--
(2) Fa -> Ga & Ha
(3) Fa 
--
with modus ponens (complex variant) from 2,3
--
(4) Ga & Ha
```

General properties of the argument are now determined and can be stored in the dataset (its `domain` is randomly chosen):

```json
"steps":2, // number of inference steps
"n_premises":2,
"base_scheme_groups":[
    "biconditional elimination",
    "modus ponens"
],
"scheme_variants":[
    "complex variant"
],
"domain_id":"consumers_personalcare",
"domain_type":"persons"
```



#### Step 3: Creation of (precise and informal) natural-language argument schemes

In step 3, the *symbolic and formal* complex argument scheme is transformed into a *natural language* argument scheme by replacing symbolic formulas (e.g., `${A}${a} v ${B}${a}`) with suitable natural language sentence schemes (such as, `${a} is a ${A}, and ${a} is a ${B}` or `${a} is a ${A} and a ${B}`).  Natural language sentence schemes which translate symbolic formulas are classified according to whether they are precise, informal, or imprecise. 

For each symbolic formula, there are many (partly automatically, partly manually generated) natural-language sentence scheme which render the formula in more or less precise way. Each of these natural-language "translations" of a symbolic formula is labeled according to whether it presents the logical form in a "precise", "informal", or "imprecise" way. e.g.

|type|form|
|-|-|
|symbolic|`(x): ${A}x -> ${B}x`|
|precise|`If someone is a ${A}, then they are a ${B}.`|
|informal|`Every ${A} is a ${B}.`|
|imprecise|`${A} might be a ${B}.`|

The labels "precise", "informal", "imprecise" are used to control the generation of two natural-language versions of the argument scheme, a **precise** one (for creating the argdown snippet) and an **informal** one (for creating the source text). Moreover, the natural-language "translations" are also chosen in view of the domain (see below) of the to-be-generated argument, specifically in view of whether it is quantified over persons ("everyone", "nobody") or objects ("something, nothing").

So, as a **precise** rendition of our symbolic argument scheme, we may obtain:

```
(1) If, and only if, a is a F, then a is G and a is a H.
--
with biconditional elimination (complex variant) from 1
--
(2) If a is a F, then a is a G and a is a H.
(3) a is a F. 
--
with modus ponens (complex variant) from 3,2
--
(4) a is G and a is a H.
```

Likewise, an **informal** rendition may be:

```
(1) a is a F if a is both a G and a H -- and vice versa.
--
with biconditional elimination (complex variant) from 1
--
(2) a is a G and a H, provided a is a F.
(3) a is a F. 
--
with modus ponens (complex variant) from 3,2
--
(4) a is both a G and a H.
```

#### Step 4: Substitution of placeholders with domain-specific predicates and names

Every argument falls within a domain. A domain provides 

* a list of `subject names` (e.g., Peter, Sarah)
* a list of `object names` (e.g., New York, Lille)
* a list of `binary predicates` (e.g., [subject is an] admirer of [object])

These domains are manually created. 

Replacements for the placeholders are sampled from the corresponding domain. Substitutes for entity placeholders (`a`, `b` etc.) are simply chosen from the list of `subject names`. Substitutes for predicate placeholders (`F`, `G` etc.) are constructed by combining `binary predicates` with `object names`, which yields unary predicates of the form "___ stands in some relation to some object". This combinatorial construction of unary predicates drastically increases the number of replacements available and hence the variety of generated arguments. 

Assuming that we sample our argument from the domain `consumers personal care`, we may choose and construct the following substitutes for placeholders in our argument scheme:


* `F`: regular consumer of Kiss My Face soap
* `G`: regular consumer of Nag Champa soap
* `H`: occasional purchaser of Shield soap
* `a`: Orlando


#### Step 5: Creation of the argdown-snippet

From the **precise rendition** of the natural language argument scheme ([step 3](#step-3-creation-of-precise-and-informal-natural-language-argument-schemes)) and the replacements for its placeholders ([step 4](#step-4-substitution-of-placeholders-with-domain-specific-predicates-and-names)), we construct the `argdown-snippet` by simple substitution and formatting the complex argument in accordance with [argdown syntax](https://argdown.org).

This yields, for our example from above:

```argdown
(1) If, and only if, Orlando is a regular consumer of Kiss My Face soap, 
    then Orlando is a regular consumer of Nag Champa soap and Orlando is 
    a occasional purchaser of Shield soap.
--
with biconditional elimination (complex variant) from 1
--
(2) If Orlando is a regular consumer of Kiss My Face soap, then Orlando 
    is a regular consumer of Nag Champa soap and Orlando is a occasional 
    purchaser of Shield soap.
(3) Orlando is a regular consumer of Kiss My Face soap. 
--
with modus ponens (complex variant) from 3,2
--
(4) Orlando is a regular consumer of Nag Champa soap and Orlando is a 
    occasional purchaser of Shield soap.
```

That's the `argdown_snippet`. By construction of such a synthetic argument (from formal schemes, see [step 2](#step-2-assembling-complex-multi-hop-argument-schemes-from-symbolic-inference-schemes)), we already know its conclusions and their formalization (the value of the field `explicit` will be determined later).

```json
"conclusion":[
    {
        "ref_reco":4,
        "text":"Orlando is a regular consumer of Nag Champa 
            soap and Orlando is a occasional purchaser of 
            Shield soap.",
        "explicit": TBD
    }
],
"conclusion_formalized":[
    {
        "ref_reco":4,
        "form":"(${F2}${a1} & ${F3}${a1})"
    }
],
"intermediary_conclusions":[
    {
        "ref_reco":2,
        "text":"If Orlando is a regular consumer of Kiss My 
            Face soap, then Orlando is a regular consumer of 
            Nag Champa soap and Orlando is a occasional 
            purchaser of Shield soap.",
        "explicit": TBD

    }
]
"intermediary_conclusions_formalized":[
    {
        "ref_reco":2,
        "text":"${F1}${a1} -> (${F2}${a1} & ${F3}${a1})"
    }
],
```

... and the corresponding keys (see [step 4](#step-4-substitution-of-placeholders-with-domain-specific-predicates-and-names))):

```json
"plcd_subs":{
    "a1":"Orlando",
    "F1":"regular consumer of Kiss My Face soap",
    "F2":"regular consumer of Nag Champa soap",
    "F3":"occasional purchaser of Shield soap"
}
```

#### Step 6: Paraphrasing

From the **informal rendition** of the natural language argument scheme ([step 3](#step-3-creation-of-precise-and-informal-natural-language-argument-schemes)) and the replacements for its placeholders ([step 4](#step-4-substitution-of-placeholders-with-domain-specific-predicates-and-names)), we construct an informal argument (argument tree) by substitution.

The statements (premises, conclusions) of the informal argument are individually paraphrased in two steps

1. rule-based and in a domain-specific way, 
2. automatically by means of a specifically fine-tuned T5 model.  

Each domain (see [step 4](#step-4-substitution-of-placeholders-with-domain-specific-predicates-and-names)) provides rules for substituting noun constructs ("is a supporter of X", "is a product made of X") with verb constructs ("supports x", "contains X"). These rules are applied whenever possible.

Next, each sentence is -- with a probability specified by parameter `lm_paraphrasing` -- replaced with an automatically generated paraphrase, using a [T5 model fine-tuned on the Google PAWS dataset](https://huggingface.co/Vamsi/T5_Paraphrase_Paws) and filtering for paraphrases with acceptable _cola_ and sufficiently high _STSB_ value (both as predicted by T5). 

| |AAAC01|AAAC02|
|-|-|-|
|`lm_paraphrasing`|0.2|0.|



#### Step 7: Construction of a storyline for the argument source text

The storyline determines in which order the premises, intermediary conclusions and final conclusions are to be presented in the text paragraph to-be-constructed (`argument-source`). The storyline is constructed from the paraphrased informal complex argument (see [step 6](#step-6-paraphrasing))).

Before determining the order of presentation (storyline), the informal argument tree is pre-processed to account for:

* implicit premises,
* implicit intermediary conclusions, and
* implicit final conclusion,

which is documented in the dataset record as

```json
"presentation_parameters":{
    "resolve_steps":[1],
    "implicit_conclusion":false,
    "implicit_premise":true,
    "...":"..."
}
```

In order to make an intermediary conclusion *C* implicit, the inference to *C* is "resolved" by re-assigning all premisses *from* which *C* is directly inferred *to* the inference to the (final or intermediary) conclusion which *C* supports. 

Original tree:

```
P1 ... Pn
—————————
    C   Q1 ... Qn
    —————————————
          C'
```

Tree with resolved inference and implicit intermediary conclusion:

```
P1 ... Pn Q1 ... Qn
———————————————————
         C'
```

The original argument tree in our example reads:

```
(1)
———
(2) (3)
———————
  (4)
```

This might be pre-processed (by resolving the first inference step and dropping the first premise) to:

```
(3)
———
(4)
```

Given such a pre-processed argument tree, a storyline, which determines the order of presentation, can be constructed by specifying the direction of presentation and a starting point. The **direction** is either 

* forward (premise AND ... AND premise THEREFORE conclusion)
* backward (conclusion SINCE premise AND ... AND premise)

Any conclusion in the pre-processed argument tree may serve as starting point. The storyline is now constructed recursively, as illustrated in Figure~1. Integer labels of the nodes represent the order of presentation, i.e. the storyline. (Note that the starting point is not necessarily the statement which is presented first according to the storyline.) 


![Storyline Construction](https://huggingface.co/datasets/debatelab/aaac/resolve/main/img/storylines1-4.png)



So as to introduce redundancy, the storyline may be post-processed by repeating a premiss that has been stated previously. The likelihood that a single premise is repeated is controlled by the presentation parameters:

```json
"presentation_parameters":{
    "redundancy_frequency":0.1,
}
```

Moreover, **distractors**, i.e. arbitrary statements sampled from the argument's very domain, may be inserted in the storyline. 



#### Step 8: Assembling the argument source text

The `argument-source` is constructed by concatenating the statements of the informal argument ([step 6](#step-6-paraphrasing)) according to the order of the storyline ([step 7](#step-7-construction-of-a-storyline-for-the-argument-source-text)). In principle, each statement is prepended by a conjunction. There are four types of conjunction: 

* THEREFORE: left-to-right inference 
* SINCE: right-to-left inference 
* AND: joins premises with similar inferential role
* MOREOVER: catch all conjunction

Each statement is assigned a specific conjunction type by the storyline.

For every conjunction type, we provide multiple natural-language terms which may figure as conjunctions when concatenating the statements, e.g. "So, necessarily,", "So", "Thus,", "It follows that", "Therefore,", "Consequently,", "Hence,", "In consequence,", "All this entails that", "From this follows that", "We may conclude that" for THEREFORE. The parameter 

```json
"presentation_parameters":{
    "drop_conj_frequency":0.1,
    "...":"..."
}
```

determines the probability that a conjunction is omitted and a statement is concatenated without prepending a conjunction.

With the parameters given above we obtain the following `argument_source` for our example: 

> Orlando is a regular consumer of Nag Champa soap and Orlando is a occasional purchaser of Shield soap, since Orlando is a regular consumer of Kiss My Face soap.


#### Step 9: Linking informal presentation and formal reconstruction

We can identify all statements _in the informal presentation_ (`argument_source`), categorize them according to their argumentative function GIVEN the logical reconstruction and link them to the corresponding statements in the `argdown_snippet`. We distinguish `reason_statement` (AKA REASONS, correspond to premises in the reconstruction) and `conclusion_statement` (AKA CONJECTURES, correspond to conclusion and intermediary conclusion in the reconstruction):

```json
"reason_statements":[ // aka reasons
    {
        "text":"Orlando is a regular consumer of Kiss My Face soap",
        "starts_at":109,
        "ref_reco":3
    }
],
"conclusion_statements":[ // aka conjectures 
    {
        "text":"Orlando is a regular consumer of Nag Champa soap and 
        Orlando is a occasional purchaser of Shield soap",
        "starts_at":0,
        "ref_reco":4
    }
]
```



Moreover, we are now able to classify all premises in the formal reconstruction (`argdown_snippet`) according to whether they are implicit or explicit given the informal presentation:

```json
"premises":[
    {
        "ref_reco":1,
        "text":"If, and only if, Orlando is a regular consumer of Kiss
            My Face soap, then Orlando is a regular consumer of Nag 
            Champa soap and Orlando is a occasional purchaser of 
            Shield soap.",
        "explicit":False
    },
    {
        "ref_reco":3,
        "text":"Orlando is a regular consumer of Kiss My Face soap. ",
        "explicit":True
    }
],
"premises_formalized":[
    {
        "ref_reco":1,
        "form":"${F1}${a1} <-> (${F2}${a1} & ${F3}${a1})"
    },
    {
        "ref_reco":3,
        "form":"${F1}${a1}"
    }
]
```


#### Initial Data Collection and Normalization

N.A.

#### Who are the source language producers?

N.A.

### Annotations

#### Annotation process

N.A.

#### Who are the annotators?

N.A.

### Personal and Sensitive Information

N.A.

## Considerations for Using the Data

### Social Impact of Dataset

None

### Discussion of Biases

None

### Other Known Limitations

See [Betz and Richardson 2021](https://arxiv.org/abs/2110.01509).

## Additional Information

### Dataset Curators

Gregor Betz, Kyle Richardson

### Licensing Information

Creative Commons cc-by-sa-4.0

### Citation Information

```
@misc{betz2021deepa2,
      title={DeepA2: A Modular Framework for Deep Argument Analysis with Pretrained Neural Text2Text Language Models}, 
      author={Gregor Betz and Kyle Richardson},
      year={2021},
      eprint={2110.01509},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

### Contributions

<!--Thanks to [@github-username](https://github.com/<github-username>) for adding this dataset.-->
