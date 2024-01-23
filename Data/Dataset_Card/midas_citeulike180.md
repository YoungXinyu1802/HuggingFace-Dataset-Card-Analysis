## Dataset Summary

A dataset for benchmarking keyphrase extraction and generation techniques from long document english scientific articles. For more details about the dataset please refer the original paper - [https://aclanthology.org/D09-1137/](https://aclanthology.org/D09-1137/)

Original source of the data - []()


## Dataset Structure


### Data Fields

- **id**: unique identifier of the document.
- **document**: Whitespace separated list of words in the document.
- **doc_bio_tags**: BIO tags for each word in the document. B stands for the beginning of a keyphrase and I stands for inside the keyphrase. O stands for outside the keyphrase and represents the word that isn't a part of the keyphrase at all.
- **extractive_keyphrases**: List of all the present keyphrases.
- **abstractive_keyphrase**: List of all the absent keyphrases.


### Data Splits

|Split| #datapoints  |
|--|--|
| Test | 182 |


## Usage

### Full Dataset

```python
from datasets import load_dataset

# get entire dataset
dataset = load_dataset("midas/citeulike180", "raw")

# sample from the test split
print("Sample from test dataset split")
test_sample = dataset["test"][0]
print("Fields in the sample: ", [key for key in test_sample.keys()])
print("Tokenized Document: ", test_sample["document"])
print("Document BIO Tags: ", test_sample["doc_bio_tags"])
print("Extractive/present Keyphrases: ", test_sample["extractive_keyphrases"])
print("Abstractive/absent Keyphrases: ", test_sample["abstractive_keyphrases"])
print("\n-----------\n")
```
**Output**

```bash
Sample from test data split
Fields in the sample:  ['id', 'document', 'doc_bio_tags', 'extractive_keyphrases', 'abstractive_keyphrases', 'other_metadata']
Tokenized Document:  ['Vol', '450', '|', '8', 'November', '2007', '|', 'doi', ':', '10.1038', '/', 'nature06341', 'ARTICLES', 'Evolution', 'of', 'genes', 'and', 'genomes', 'on', 'the', 'Drosophila', 'phylogeny', 'Drosophila', '12', 'Genomes', 'Consortium', '*', 'Comparative', 'analysis', 'of', 'multiple', 'genomes', 'in', 'a', 'phylogenetic', 'framework', 'dramatically', 'improves', 'the', 'precision', 'and', 'sensitivity', 'of', 'evolutionary', 'inference', ',', 'producing', 'more', 'robust', 'results', 'than', 'single-genome', 'analyses', 'can', 'provide', '.', 'The', 'genomes', 'of', '12', 'Drosophila', 'species', ',', 'ten', 'of', 'which', 'are', 'presented', 'here', 'for', 'the', 'first', 'time', '-LRB-', 'sechellia', ',', 'simulans', ',', 'yakuba', ',', 'erecta', ',', 'ananassae', ',', 'persimilis', ',', 'willistoni', ',', 'mojavensis', ',', 'virilis', 'and', 'grimshawi', '-RRB-', ',', 'illustrate', 'how', 'rates', 'and', 'patterns', 'of', 'sequence', 'divergence', 'across', 'taxa', 'can', 'illuminate', 'evolutionary', 'processes', 'on', 'a', 'genomic', 'scale', '.', 'These', 'genome', 'sequences', 'augment', 'the', 'formidable', 'genetic', 'tools', 'that', 'have', 'made', 'Drosophila', 'melanogaster', 'a', 'pre-eminent', 'model', 'for', 'animal', 'genetics', ',', 'and', 'will', 'further', 'catalyse', 'fundamental', 'research', 'on', 'mechanisms', 'of', 'development', ',', 'cell', 'biology', ',', 'genetics', ',', 'disease', ',', 'neurobiology', ',', 'behaviour', ',', 'physiology', 'and', 'evolution', '.', 'Despite', 'remarkable', 'similarities', 'among', 'these', 'Drosophila', 'species', ',', 'we', 'identified', 'many', 'putatively', 'non-neutral', 'changes', 'in', 'protein-coding', 'genes', ',', 'non-coding', 'RNA', 'genes', ',', 'and', 'cis-regulatory', 'regions', '.', 'These', 'may', 'prove', 'to', 'underlie', 'differences', 'in', 'the', 'ecology', 'and', 'behaviour', 'of', 'these', 'diverse', 'species', '.', 'As', 'one', 'might', 'expect', 'from', 'a', 'genus', 'with', 'species', 'living', 'in', 'deserts', ',', 'in', 'the', 'tropics', ',', 'on', 'chains', 'of', 'volcanic', 'islands', 'and', ',', 'often', ',', 'commensally', 'with', 'humans', ',', 'Drosophila', 'species', 'vary', 'considerably', 'in', 'their', 'morphology', ',', 'ecology', 'and', 'behaviour1', '.', 'Species', 'in', 'this', 'genus', 'span', 'a', 'wide', 'range', 'of', 'global', 'distributions', ':', 'the', '12', 'sequenced', 'species', 'originate', 'from', 'Africa', ',', 'Asia', ',', 'the', 'Americas', 'and', 'the', 'Pacific', 'Islands', ',', 'and', 'also', 'include', 'cosmopolitan', 'species', 'that', 'have', 'colonized', 'the', 'planet', '-LRB-', 'D.', 'melanogaster', 'and', 'D.', 'simulans', '-RRB-', 'as', 'well', 'as', 'closely', 'related', 'species', 'that', 'live', 'on', 'single', 'islands', '-LRB-', 'D.', 'sechellia', '-RRB-', '2', '.', 'A', 'variety', 'of', 'behavioural', 'strategies', 'is', 'also', 'encompassed', 'by', 'the', 'sequenced', 'species', ',', 'ranging', 'in', 'feeding', 'habit', 'from', 'generalist', ',', 'such', 'as', 'D.', 'ananassae', ',', 'to', 'specialist', ',', 'such', 'as', 'D.', 'sechellia', ',', 'which', 'feeds', 'on', 'the', 'fruit', 'of', 'a', 'single', 'plant', 'species', '.', 'Despite', 'this', 'wealth', 'of', 'phenotypic', 'diversity', ',', 'Drosophila', 'species', 'share', 'a', 'distinctive', 'body', 'plan', 'and', 'life', 'cycle', '.', 'Although', 'only', 'D.', 'melanogaster', 'has', 'been', 'extensively', 'characterized', ',', 'it', 'seems', 'that', 'the', 'most', 'important', 'aspects', 'of', 'the', 'cellular', ',', 'molecular', 'and', 'developmental', 'biology', 'of', 'these', 'species', 'are', 'well', 'conserved', '.', 'Thus', ',', 'in', 'addition', 'to', 'providing', 'an', 'extensive', 'resource', 'for', 'the', 'study', 'of', 'the', 'relationship', 'between', 'sequence', 'and', 'phenotypic', 'diversity', ',', 'the', 'genomes', 'of', 'these', 'species', 'provide', 'an', 'excellent', 'model', 'for', 'studying', 'how', 'conserved', 'functions', 'are', 'maintained', 'in', 'the', 'face', 'of', 'sequence', 'divergence', '.', 'These', 'genome', 'sequences', 'provide', 'an', 'unprecedented', 'dataset', 'to', 'contrast', 'genome', 'structure', ',', 'genome', 'content', ',', 'and', 'evolutionary', 'dynamics', 'across', 'the', 'well-defined', 'phylogeny', 'of', 'the', 'sequenced', 'species', '-LRB-', 'Fig.', '1', '-RRB-', '.', 'Genome', 'assembly', ',', 'annotation', 'and', 'alignment', 'Genome', 'sequencing', 'and', 'assembly', '.', 'We', 'used', 'the', 'previously', 'published', 'sequence', 'and', 'updated', 'assemblies', 'for', 'two', 'Drosophila', 'species', ',', 'D.', 'melanogaster3', ',4', '-LRB-', 'release', '4', '-RRB-', 'and', 'D.', 'pseudoobscura5', '-LRB-', 'release', '2', '-RRB-', ',', 'and', 'generated', 'DNA', 'sequence', 'data', 'for', '10', 'additional', 'Drosophila', 'genomes', 'by', 'whole-genome', 'shotgun', 'sequencing6', ',7', '.', 'These', 'species', 'were', 'chosen', 'to', 'span', 'a', 'wide', 'variety', 'of', 'evolutionary', 'distances', ',', 'from', 'closely', 'related', 'pairs', 'such', 'as', 'D.', 'sechellia/D', '.', 'simulans', 'and', 'D.', 'persimilis/D', '.', 'pseudoobscura', 'to', 'the', 'distantly', 'related', 'species', 'of', 'the', 'Drosophila', 'and', 'Sophophora', 'subgenera', '.', 'Whereas', 'the', 'time', 'to', 'the', 'most', 'recent', 'common', 'ancestor', 'of', 'the', 'sequenced', 'species', 'may', 'seem', 'small', 'on', 'an', 'evolutionary', 'timescale', ',', 'the', 'evolutionary', 'divergence', 'spanned', 'by', 'the', 'genus', 'Drosophila', 'exceeds', '*', 'A', 'list', 'of', 'participants', 'and', 'affiliations', 'appears', 'at', 'the', 'end', 'of', 'the', 'paper', '.', 'that', 'of', 'the', 'entire', 'mammalian', 'radiation', 'when', 'generation', 'time', 'is', 'taken', 'into', 'account', ',', 'as', 'discussed', 'further', 'in', 'ref', '.', '8', '.', 'We', 'sequenced', 'seven', 'of', 'the', 'new', 'species', '-LRB-', 'D.', 'yakuba', ',', 'D.', 'erecta', ',', 'D.', 'ananassae', ',', 'D.', 'willistoni', ',', 'D.', 'virilis', ',', 'D.', 'mojavensis', 'and', 'D.', 'grimshawi', '-RRB-', 'to', 'deep', 'coverage', '-LRB-', '8.43', 'to', '11.03', '-RRB-', 'to', 'produce', 'high', 'quality', 'draft', 'sequences', '.', 'We', 'sequenced', 'two', 'species', ',', 'D.', 'sechellia', 'and', 'D.', 'persimilis', ',', 'to', 'intermediate', 'coverage', '-LRB-', '4.93', 'and', '4.13', ',', 'respectively', '-RRB-', 'under', 'the', 'assumption', 'that', 'the', 'availability', 'of', 'a', 'sister', 'species', 'sequenced', 'to', 'high', 'coverage', 'would', 'obviate', 'the', 'need', 'for', 'deep', 'sequencing', 'without', 'sacrificing', 'draft', 'genome', 'quality', '.', 'Finally', ',', 'seven', 'inbred', 'strains', 'of', 'D.', 'simulans', 'were', 'sequenced', 'to', 'low', 'coverage', '-LRB-', '2.93', 'coverage', 'from', 'w501', 'and', ',13', 'coverage', 'of', 'six', 'other', 'strains', '-RRB-', 'to', 'provide', 'population', 'variation', 'data9', '.', 'Further', 'details', 'of', 'the', 'sequencing', 'strategy', 'can', 'be', 'found', 'in', 'Table', '1', ',', 'Supplementary', 'Table', '1', 'and', 'section', '1', 'in', 'Supplementary', 'Information', '.', 'We', 'generated', 'an', 'initial', 'draft', 'assembly', 'for', 'each', 'species', 'using', 'one', 'of', 'three', 'different', 'whole-genome', 'shotgun', 'assembly', 'programs', '-LRB-', 'Table', '1', '-RRB-', '.', 'For', 'D.', 'ananassae', ',', 'D.', 'erecta', ',', 'D.', 'grimshawi', ',', 'D.', 'mojavensis', ',', 'D.', 'virilis', 'and', 'D.', 'willistoni', ',', 'we', 'also', 'generated', 'secondary', 'assemblies', ';', 'reconciliation', 'of', 'these', 'with', 'the', 'primary', 'assemblies', 'resulted', 'in', 'a', '7', '30', '%', 'decrease', 'in', 'the', 'estimated', 'number', 'of', 'misassembled', 'regions', 'and', 'a', '12', '23', '%', 'increase', 'in', 'the', 'N50', 'contig', 'size10', '-LRB-', 'Supplementary', 'Table', '2', '-RRB-', '.', 'For', 'D.', 'yakuba', ',', 'we', 'generated', '52,000', 'targeted', 'reads', 'across', 'low-quality', 'regions', 'and', 'gaps', 'to', 'improve', 'the', 'assembly', '.', 'This', 'doubled', 'the', 'mean', 'contig', 'and', 'scaffold', 'sizes', 'and', 'increased', 'the', 'total', 'fraction', 'of', 'high', 'quality', 'bases', '-LRB-', 'quality', 'score', '-LRB-', 'Q', '-RRB-', '.', '40', '-RRB-', 'from', '96.5', '%', 'to', '98.5', '%', '.', 'We', 'improved', 'the', 'initial', '2.93', 'D.', 'simulans', 'w501', 'whole-genome', 'shotgun', 'assembly', 'by', 'filling', 'assembly', 'gaps', 'with', 'contigs', 'and', 'unplaced', 'reads', 'from', 'the', ',13', 'assemblies', 'of', 'the', 'six', 'other', 'D.', 'simulans', 'strains', ',', 'generating', 'a', '`', 'mosaic', "'", 'assembly', '-LRB-', 'Supplementary', 'Table', '3', '-RRB-', '.', 'This', 'integration', 'markedly', 'improved', 'the', 'D.', 'simulans', 'assembly', ':', 'the', 'N50', 'contig', 'size', 'of', 'the', 'mosaic', 'assembly', ',', 'for', 'instance', ',', 'is', 'more', 'than', 'twice', 'that', 'of', 'the', 'initial', 'w501', 'assembly', '-LRB-', '17']
Document BIO Tags:  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'B', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
Extractive/present Keyphrases:  ['phylogeny', 'drosophila', 'evolution', 'fly', 'genomics']
Abstractive/absent Keyphrases:  ['droso', 'comparative genomics']

-----------
```

### Keyphrase Extraction
```python
from datasets import load_dataset

# get the dataset only for keyphrase extraction
dataset = load_dataset("midas/citeulike180", "extraction")

print("Samples for Keyphrase Extraction")

# sample from the test split
print("Sample from test data split")
test_sample = dataset["test"][0]
print("Fields in the sample: ", [key for key in test_sample.keys()])
print("Tokenized Document: ", test_sample["document"])
print("Document BIO Tags: ", test_sample["doc_bio_tags"])
print("\n-----------\n")
```

### Keyphrase Generation
```python
# get the dataset only for keyphrase generation
dataset = load_dataset("midas/citeulike180", "generation")

print("Samples for Keyphrase Generation")

# sample from the test split
print("Sample from test data split")
test_sample = dataset["test"][0]
print("Fields in the sample: ", [key for key in test_sample.keys()])
print("Tokenized Document: ", test_sample["document"])
print("Extractive/present Keyphrases: ", test_sample["extractive_keyphrases"])
print("Abstractive/absent Keyphrases: ", test_sample["abstractive_keyphrases"])
print("\n-----------\n")
```

## Citation Information
```
@inproceedings{medelyan-etal-2009-human,
    title = "Human-competitive tagging using automatic keyphrase extraction",
    author = "Medelyan, Olena  and
      Frank, Eibe  and
      Witten, Ian H.",
    booktitle = "Proceedings of the 2009 Conference on Empirical Methods in Natural Language Processing",
    month = aug,
    year = "2009",
    address = "Singapore",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/D09-1137",
    pages = "1318--1327",
}

```

## Contributions
Thanks to [@debanjanbhucs](https://github.com/debanjanbhucs), [@dibyaaaaax](https://github.com/dibyaaaaax) and [@ad6398](https://github.com/ad6398) for adding this dataset
