---
task_categories:
- conditional-text-generation

---
# AutoNLP Dataset for project: Scientific_Title_Generator

## Table of content
- [Dataset Description](#dataset-description)
    - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)

## Dataset Descritpion

This dataset has been automatically processed by AutoNLP for project Scientific_Title_Generator.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "target": "Unification of Fusion Theories, Rules, Filters, Image Fusion and Target\n  Tracking Methods (UFT)",
    "text": "  The author has pledged in various papers, conference or seminar\npresentations, and scientific grant applications (between 2004-2015) for the\nunification of fusion theories, combinations of fusion rules, image fusion\nprocedures, filter algorithms, and target tracking methods for more accurate\napplications to our real world problems - since neither fusion theory nor\nfusion rule fully satisfy all needed applications. For each particular\napplication, one selects the most appropriate fusion space and fusion model,\nthen the fusion rules, and the algorithms of implementation. He has worked in\nthe Unification of the Fusion Theories (UFT), which looks like a cooking\nrecipe, better one could say like a logical chart for a computer programmer,\nbut one does not see another method to comprise/unify all things. The\nunification scenario presented herein, which is now in an incipient form,\nshould periodically be updated incorporating new discoveries from the fusion\nand engineering research.\n"
  },
  {
    "target": "Investigation of Variances in Belief Networks",
    "text": "  The belief network is a well-known graphical structure for representing\nindependences in a joint probability distribution. The methods, which perform\nprobabilistic inference in belief networks, often treat the conditional\nprobabilities which are stored in the network as certain values. However, if\none takes either a subjectivistic or a limiting frequency approach to\nprobability, one can never be certain of probability values. An algorithm\nshould not only be capable of reporting the probabilities of the alternatives\nof remaining nodes when other nodes are instantiated; it should also be capable\nof reporting the uncertainty in these probabilities relative to the uncertainty\nin the probabilities which are stored in the network. In this paper a method\nfor determining the variances in inferred probabilities is obtained under the\nassumption that a posterior distribution on the uncertainty variables can be\napproximated by the prior distribution. It is shown that this assumption is\nplausible if their is a reasonable amount of confidence in the probabilities\nwhich are stored in the network. Furthermore in this paper, a surprising upper\nbound for the prior variances in the probabilities of the alternatives of all\nnodes is obtained in the case where the probability distributions of the\nprobabilities of the alternatives are beta distributions. It is shown that the\nprior variance in the probability at an alternative of a node is bounded above\nby the largest variance in an element of the conditional probability\ndistribution for that node.\n"
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "target": "Value(dtype='string', id=None)",
  "text": "Value(dtype='string', id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 5784 |
| valid        | 1446 |
