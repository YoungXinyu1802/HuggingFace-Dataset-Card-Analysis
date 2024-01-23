#NQ-retrieval

This is a nicely formatted version of the [Natural Questions](https://ai.google.com/research/NaturalQuestions/) dataset, formatted to train and evaluate retrieval systems.

Each row contains the following entries:
- **question**: Original question send for Google Search Engine
- **title**: Title of Wikipedia article
- **candidates**: A list with the passages from the original Wikipedia HTML document
- **passage_types**: Types (text, table, list) of the candidate passages
- **long_answers**: IDs which candidate passages where selected as relevant from annotators. Might be empty if no relevant passage has been identified
- **document_url**