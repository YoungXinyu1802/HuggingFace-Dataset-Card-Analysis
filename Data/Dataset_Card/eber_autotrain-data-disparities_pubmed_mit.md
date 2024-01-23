---
language:
- en
task_categories:
- text-classification

---
# AutoTrain Dataset for project: disparities_pubmed_mit

## Dataset Description

This dataset has been automatically processed by AutoTrain for project disparities_pubmed_mit.

### Languages

The BCP-47 code for the dataset's language is en.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "text": "IDH1-R132H acts as a tumor suppressor in glioma via epigenetic up-regulation of the DNA damage response. Patients with glioma whose tumors carry a mutation in isocitrate dehydrogenase 1 (IDH1(R132H)) are younger at diagnosis and live longer. IDH1 mutations co-occur with other molecular lesions, such as 1p/19q codeletion, inactivating mutations in the tumor suppressor protein 53 (TP53) gene, and loss-of-function mutations in alpha thalassemia/mental retardation syndrome X-linked gene (ATRX). All adult low-grade gliomas (LGGs) harboring ATRX loss also express the IDH1(R132H) mutation. The current molecular classification of LGGs is based, partly, on the distribution of these mutations. We developed a genetically engineered mouse model harboring IDH1(R132H), TP53 and ATRX inactivating mutations, and activated NRAS G12V. Previously, we established that ATRX deficiency, in the context of wild-type IDH1, induces genomic instability, impairs nonhomologous end-joining DNA repair, and increases sensitivity to DNA-damaging therapies. In this study, using our mouse model and primary patient-derived glioma cultures with IDH1 mutations, we investigated the function of IDH1(R132H) in the context of TP53 and ATRX loss. We discovered that IDH1(R132H) expression in the genetic context of ATRX and TP53 gene inactivation (i) increases median survival in the absence of treatment, (ii) enhances DNA damage response (DDR) via epigenetic up-regulation of the ataxia-telangiectasia-mutated (ATM) signaling pathway, and (iii) elicits tumor radioresistance. Accordingly, pharmacological inhibition of ATM or checkpoint kinases 1 and 2, essential kinases in the DDR, restored the tumors' radiosensitivity. Translation of these findings to patients with IDH1(132H) glioma harboring TP53 and ATRX loss could improve the therapeutic efficacy of radiotherapy and, consequently, patient survival.",
    "target": 0
  },
  {
    "text": "Activation of prolyl hydroxylase-2 for stabilization of mitochondrial stress along with simultaneous downregulation of HIF-1\u00ce\u00b1/FASN in ER\u00c2\u00a0+\u00c2\u00a0breast cancer subtype. The present study was undertaken to inquest the chemical activation of prolyl hydroxylase-2 for the curtailment of hypoxia-inducible factor-1\u00ce\u00b1 and fatty acid synthase. It was well documented that hypoxia-inducible factor-1\u00ce\u00b1 and fatty acid synthase were overexpressed in mammary gland carcinomas. After screening a battery of compounds, BBAP-2 was retrieved as a potential prolyl hydroxylase-2 activator and validates its activity using ER\u00c2\u00a0+\u00c2\u00a0MCF-7 cell line and n-methyl-n-nitrosourea-induced rat in vivo model, respectively. BBAP-2 was palpable for the morphological characteristics of apoptosis along with changes in the mitochondrial intergrity as visualized by acridine orange/ethidium bromide and JC-1 staining against ER\u00c2\u00a0+\u00c2\u00a0MCF-7 cells. BBAP-2 also arrest the cell cycle of ER\u00c2\u00a0+\u00c2\u00a0MCF-7 cells at G2/M phase. Afterward, BBAP-2 has scrutinized against n-methyl-n-nitrosourea-induced mammary gland carcinoma in albino Wistar rats. BBAP-2 restored the morphological architecture when screened through carmine staining, haematoxylin and eosin staining, and scanning electron microscopy. BBAP-2 also delineated the markers of oxidative stress favourably. The immunoblotting and mRNA expression analysis validated that BBAP-2 has a potentialty activate the prolyl hydroxylase-2 with sequential downregulating effect on hypoxia-inducible factor-1\u00ce\u00b1 and its downstream checkpoint. BBAP-2 also fostered apoptosis through mitochondrial-mediated death pathway. The present study elaborates the chemical activation of prolyl hydroxylase-2 by which the increased expression of HIF-1\u00ce\u00b1 and FASN can be reduced in mammary gland carcinoma.",
    "target": 0
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "text": "Value(dtype='string', id=None)",
  "target": "ClassLabel(num_classes=2, names=['0', '1'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 807 |
| valid        | 203 |
