Dataset of single lines of Python code taken from the [CodeSearchNet](https://github.com/github/CodeSearchNet) dataset.

Context

This dataset allows checking the validity of Variational-Autoencoder latent spaces by testing what percentage of random/intermediate latent points can be greedily decoded into valid Python code.

Content

Each row has a parsable line of source code.
{'text': '{python source code line}'}

Most lines are < 100 characters while all are under 125 characters.

Contains 2.6 million lines.

All code is in parsable into a python3 ast.
