---
annotations_creators:
- hired_annotators
language_creators:
- found
language:
- pl
license:
- cc-by-nc-sa-4.0
multilinguality:
- monolingual
size_categories:
- 10<n<10K
task_categories:
- token-classification
task_ids:
- named-entity-recognition
- part-of-speech
pretty_name: Polish-Abusive-Clauses
---

# PAC - Polish Abusive Clauses Dataset

''I have read and agree to the terms and conditions'' is one of the biggest lies on the Internet. Consumers rarely read the contracts they are required to accept. We conclude agreements over the Internet daily. But do we know the content of these agreements? Do we check potential unfair statements? On the Internet, we probably skip most of the Terms and Conditions. However, we must remember that we have concluded many more contracts. Imagine that we want to buy a house, a car, send our kids to the nursery, open a bank account, or many more. In all these situations, you will need to conclude the contract, but there is a high probability that you will not read the entire agreement with proper understanding. European consumer law aims to prevent businesses from using so-called ''unfair contractual terms'' in their unilaterally drafted contracts, requiring consumers to accept.

Our dataset treats ''unfair contractual term'' as the equivalent of an abusive clause. It could be defined as a clause that is unilaterally imposed by one of the contract's parties, unequally affecting the other, or creating a situation of imbalance between the duties and rights of the parties.

On the EU and at the national such as the Polish levels, agencies cannot check possible agreements by hand. Hence, we took the first step to evaluate the possibility of accelerating this process. We created a dataset and machine learning models to automate potentially abusive clauses detection partially. Consumer protection organizations and agencies can use these resources to make their work more eﬀective and eﬃcient. Moreover, consumers can automatically analyze contracts and understand what they agree upon.

## Tasks (input, output and metrics)

Abusive Clauses Detection

**Input** ('*text'* column): text of agreement 

**Output** ('*label'* column): binary label (`BEZPIECZNE_POSTANOWIENIE_UMOWNE`: correct agreement statement, `KLAUZULA_ABUZYWNA`: abusive clause)

**Domain**: legal agreement

**Measurements**: Accuracy, F1 Macro

**Example***:* 

Input: *`Wszelka korespondencja wysyłana przez Pożyczkodawcę na adres zamieszkania podany w umowie oraz na e-mail zostaje uznana za skutecznie doręczoną. Zmiana adresu e-mail oraz adresu zamieszkania musi być dostarczona do Pożyczkodawcy osobiście`* 

Input (translated by DeepL): *`All correspondence sent by the Lender to the residential address provided in the agreement and to the e-mail address shall be deemed effectively delivered. Change of e-mail address and residential address must be delivered to the Lender in person`*

Output: `KLAUZULA_ABUZYWNA` (abusive clause)

## Data splits

| Subset      | Cardinality (sentences) |
| ----------- | ----------------------: |
| train       | 4284                    |
| dev         | 1519                    |
| test        | 3453                    |

## Class distribution

`BEZPIECZNE_POSTANOWIENIE_UMOWNE` - means correct agreement statement.

`KLAUZULA_ABUZYWNA` informs us about abusive clause.

| Class                           |   train |          dev |   test |
|:--------------------------------|--------:|-------------:|-------:|
| BEZPIECZNE_POSTANOWIENIE_UMOWNE |  0.5458 |       0.3002 | 0.6756 |
| KLAUZULA_ABUZYWNA               |  0.4542 |       0.6998 | 0.3244 |

## License

[Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

## Citation

TBD
