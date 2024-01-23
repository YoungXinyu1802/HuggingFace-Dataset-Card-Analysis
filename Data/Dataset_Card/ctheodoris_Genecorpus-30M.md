# Dataset Card for Genecorpus-30M

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks](#supported-tasks)
  - [Species](#species)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
<!--- 
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)
--->

## Dataset Description

<!--- **Paper:**
--->
- **Point of Contact:** christina.theodoris@gladstone.ucsf.edu

### Dataset Summary

We assembled a large-scale pretraining corpus, Genecorpus-30M, comprised of ~30 million human single cell transcriptomes from a broad range of tissues from publicly available data. This corpus was used for pretraining [Geneformer](https://huggingface.co/ctheodoris/Geneformer), a pretrained transformer model that enables context-aware predictions in settings with limited data in network biology.

### Supported Tasks

This corpus was used for pretraining [Geneformer](https://huggingface.co/ctheodoris/Geneformer) and is compatible with pretraining or fine-tuning Geneformer or similar models.

### Species

Homo sapiens

## Dataset Structure

### Data Instances

Genecorpus-30M is provided as tokenized data in the Huggingface Datasets structure, which is based on the Apache Arrow format. Each example within the dataset is composed of the rank value encoding for a single cell within the corpus. Rank value encodings provide a nonparametric representation of each single cell’s transcriptome, ranking genes by their expression within that cell normalized by their expression across the entire Genecorpus-30M. This method takes advantage of the many observations of each gene’s expression across Genecorpus-30M to prioritize genes that distinguish cell state. Specifically, this method will deprioritize ubiquitously highly-expressed housekeeping genes by normalizing them to a lower rank. Conversely, genes such as transcription factors that may be lowly expressed when they are expressed but highly distinguish cell state will move to a higher rank within the encoding. Furthermore, this rank-based approach may be more robust against technical artifacts that may systematically bias the absolute transcript counts value while the overall relative ranking of genes within each cell remains more stable.

To accomplish this, we first calculated the nonzero median value of expression of each detected gene across all cells from the entire Genecorpus-30M. We aggregated the transcript count distribution for each gene, normalizing the gene transcript counts in each cell by the total transcript count of that cell to account for varying sequencing depth. We then normalized the genes in each single cell transcriptome by that gene’s non-zero median value of expression across Genecorpus-30M and ordered the genes by the rank of their normalized expression in that specific cell. Of note, we opted to use the nonzero median value of expression rather than include zeros in the distribution so as not to weight the value by tissue representation within Genecorpus-30M, assuming that a representative range of transcript values would be observed within the cells in which each gene was detected.

The rank value encodings for each single cell transcriptome were then tokenized based on a total vocabulary of 25,424 protein-coding or miRNA genes detected within Geneformer-30M. The token dictionary mapping each token ID to special tokens (<pad> and <mask>) or Ensembl IDs for each gene is included within the repository as a pickle file (token_dictionary.pickle).

### Data Fields

- `input_ids`: rank value encoding for an example cell
- `lengths`: length of rank value encoding for that example cell

### Data Splits

The dataset does not contain any predefined splits.

## Dataset Creation

### Curation Rationale

Mapping the gene regulatory networks that drive disease progression enables screening for molecules that correct the network by normalizing core regulatory elements, rather than targeting peripheral downstream effectors that may not be disease modifying. However, mapping the gene network architecture requires large amounts of transcriptomic data to learn the connections between genes, which impedes network-correcting drug discovery in settings with limited data, including rare diseases and diseases affecting clinically inaccessible tissues. Although data remains limited in these settings, recent advances in sequencing technologies have driven a rapid expansion in the amount of transcriptomic data available from human tissues more broadly. Furthermore, single cell technologies have facilitated the observation of transcriptomic states without averaging genes’ expression across multiple cells, potentially providing more precise data for inference of network interactions, especially in diseases driven by dysregulation of multiple cell types. Recently, the concept of transfer learning has revolutionized fields such as natural language understanding and computer vision by leveraging deep learning models pretrained on large-scale general datasets that can then be fine-tuned towards a vast array of downstream tasks with limited task-specific data that would be insufficient to yield meaningful predictions when used in isolation. We therefore assembled Genecorpus-30M to allow the large-scale pretraining of [Geneformer](https://huggingface.co/ctheodoris/Geneformer), a pretrained transformer model that enables context-aware predictions in settings with limited data in network biology.

### Source Data

#### Initial Data Collection and Normalization

Source data included 29.9 million (29,900,531) human single cell transcriptomes from a broad range of tissues from 561 publicly available datasets from original studies cited in the Extended Methods of Theodoris et al. 2022. Datasets were filtered to retain cells with total read counts within three standard deviations of the mean within that dataset and mitochondrial reads within three standard deviations of the mean within that dataset. Ensembl-annotated protein-coding and miRNA genes were used for downstream analysis. Cells with less than seven detected Ensembl-annotated protein-coding or miRNA genes were excluded as the 15% masking used for the pretraining learning objective would not reliably mask a gene in cells with fewer detected genes. Ultimately, 27.4 million (27,406,217) cells passed the defined quality filters. Cells were then represented as rank value encodings as discussed above in [Data Instances](#data-instances).

#### Who are the source data producers?

Publicly available datasets containing raw counts were collected from National Center for Biotechnology Information (NCBI) Gene Expression Omnibus (GEO), NCBI Sequence Read Archive (SRA), Human Cell Atlas, European Molecular Biology Laboratory-European Bioinformatics Institute (EMBL-EBI) Single Cell Expression Atlas, Broad Institute Single Cell Portal, Brotman Baty Institute (BBI)-Allen Single Cell Atlases, Tumor Immune Single-cell Hub (TISCH) (excluding malignant cells), Panglao Database, 10x Genomics, University of California, Santa Cruz Cell Browser, European Genome-phenome Archive, Synapse, Riken, Zenodo, National Institutes of Health (NIH) Figshare Archive, NCBI dbGap, Refine.bio, China National GeneBank Sequence Archive, Mendeley Data, and individual communication with authors of the original studies as cited in the Extended Methods of Theodoris et al. 2022.

### Annotations

#### Annotation process

Geneformer-30M does not contain annotations.

#### Who are the annotators?

N/A

### Personal and Sensitive Information

There is no personal or sensitive information included in the dataset. The dataset is composed of rank value encodings, so there are no traceable sequencing reads included.

## Considerations for Using the Data

### Social Impact of Dataset

Genecorpus-30M enabled the large-scale pretraining of [Geneformer](https://huggingface.co/ctheodoris/Geneformer), a pretrained transformer model that enables context-aware predictions in settings with limited data in network biology. Within our publication, we demonstrated that during pretraining, Geneformer gained a fundamental understanding of network dynamics, encoding network hierarchy in the model’s attention weights in a completely self-supervised manner. Fine-tuning Geneformer towards a diverse panel of downstream tasks relevant to chromatin and network dynamics using limited task-specific data demonstrated that Geneformer consistently boosted predictive accuracy. Applied to disease modeling with limited patient data, Geneformer identified candidate therapeutic targets for cardiomyopathy. Overall, Geneformer represents an invaluable pretrained model from which fine-tuning towards a broad range of downstream applications can be pursued to accelerate discovery of key network regulators and candidate therapeutic targets.

### Discussion of Biases

We excluded cells with high mutational burdens (e.g. malignant cells and immortalized cell lines) that could lead to substantial network rewiring without companion genome sequencing to facilitate interpretation. We only included droplet-based sequencing platforms to assure expression value unit comparability. Although we assembled the dataset to represent as diverse a set of human tissues and cell types as possible, particular tissues and cell types are not represented due to unavailability of public data at the time of dataset assembly. In our manuscript, we demonstrated that pretraining with larger and more diverse corpuses consistently improved Geneformer’s predictive power, consistent with observations that large-scale pretraining allows training of deeper models that ultimately have greater predictive potential in fields including NLU, computer vision, and mathematical problem-solving. Additionally, exposure to hundreds of experimental datasets during pretraining also appeared to promote robustness to batch-dependent technical artifacts and individual variability that commonly impact single cell analyses in biology. These findings suggest that as the amount of publicly available transcriptomic data continues to expand, future models pretrained on even larger-scale corpuses may open opportunities to achieve meaningful predictions in even more elusive tasks with increasingly limited task-specific data.

### Other Known Limitations

Genecorpus-30M was intended to be used for self-supervised pretraining. To achieve the best possible predictions in downstream tasks, Geneformer should be fine-tuned with labeled datasets relevant to the task at hand.

## Additional Information

### Dataset Curators

Christina Theodoris, MD, PhD

<!--- ### Licensing Information

[More Information Needed]

### Citation Information

[More Information Needed]

### Contributions

Thanks to [@github-username](https://github.com/<github-username>) for adding this dataset.
--->
