---
{}

---
# AutoTrain Dataset for project: enzydg

## Dataset Description

This dataset has been automatically processed by AutoTrain for project enzydg.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "id": 155,
    "feat_compound_iso_smiles": "CC1(C2CC(=O)C1(C(=O)C2)C)C",
    "feat_target_sequence": "MKQLATPFQEYSQKYENIRLERDGGVLLVTVHTEGKSLVWTSTAHDELAYCFHDIACDRENKVVILTGTGPSFCNEIDFTSFNLGTPHDWDEIIFEGQRLLNNLLSIEVPVIAAVNGPVTNAPEIPVMSDIVLAAESATFQDGPHFPSGIVPGDGAHVVWPHVLGSNRGRYFLLTGQELDARTALDYGAVNEVLSEQELLPRAWELARGIAEKPLLARRYARKVLTRQLRRVMEADLSLGLAHEALAAIDLGMESEQ",
    "target": 13.621903419494629
  },
  {
    "id": 180,
    "feat_compound_iso_smiles": "C1=CC(=CC=C1C2=COC3=C(C2=O)C=CC(=C3)O[C@H]4[C@@H]([C@H]([C@@H]([C@H](O4)CO)O)O)O)O",
    "feat_target_sequence": "MAFPAGFGWAAATAAYQVEGGWDADGKGPCVWDTFTHQGGERVFKNQTGDVACGSYTLWEEDLKCIKQLGLTHYRFSLSWSRLLPDGTTGFINQKGIDYYNKIIDDLLKNGVTPIVTLYHFDLPQTLEDQGGWLSEAIIESFDKYAQFCFSTFGDRVKQWITINEANVLSVMSYDLGMFPPGIPHFGTGGYQAAHNLIKAHARSWHSYDSLFRKKQKGMVSLSLFAVWLEPADPNSVSDQEAAKRAITFHLDLFAKPIFIDGDYPEVVKSQIASMSQKQGYPSSRLPEFTEEEKKMIKGTADFFAVQYYTTRLIKYQENKKGELGILQDAEIEFFPDPSWKNVDAIYVVPWGVCKLLKYIKDTYNNPVIYITENGFPQSDPAPLDDTQRWEYFRQTFQELFKAIQLDKVNLQVYCAWSLLDNFEWNQGYSSRFGLFHVDFEDPARPRVPYTSAKEYAKIIRNNGLEAHL",
    "target": 17.67270851135254
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "id": "Value(dtype='int64', id=None)",
  "feat_compound_iso_smiles": "Value(dtype='string', id=None)",
  "feat_target_sequence": "Value(dtype='string', id=None)",
  "target": "Value(dtype='float32', id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 160 |
| valid        | 44 |
