---
task_categories:
- text-classification

---
# AutoTrain Dataset for project: provision_classification

## Dataset Descritpion

This dataset has been automatically processed by AutoTrain for project provision_classification.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "text": "Each Partner hereby represents and warrants to the Partnership and each other Partner that (a)\u00a0if such Partner is a corporation, it is duly organized, validly existing, and in good standing under the laws of the jurisdiction of its incorporation and is duly qualified and in good standing as a foreign corporation in the jurisdiction of its principal place of business (if not incorporated therein), (b) if such Partner is a trust, estate or other entity, it is duly formed, validly existing, and (if applicable) in good standing under the laws of the jurisdiction of its formation, and if required by law is duly qualified to do business and (if applicable) in good standing in the jurisdiction of its principal place of business (if not formed therein), (c) such Partner has full corporate, trust, or other applicable right, power and authority to enter into this Agreement and to perform its obligations hereunder and all necessary actions by the board of directors, trustees, beneficiaries, or other Persons necessary for the due authorization, execution, delivery, and performance of this Agreement by such Partner have been duly taken, and such authorization, execution, delivery, and performance do not conflict with any other agreement or arrangement to which such Partner is a party or by which it is bound, and (d)\u00a0such Partner is acquiring its interest in the Partnership for investment purposes and not with a view to distribution thereof.",
    "target": 13
  },
  {
    "text": "This Letter Agreement is binding upon and inures to the benefit of the parties and their respective heirs, executors, administrators, personal representatives, successors, and permitted assigns. This Letter Agreement is personal to you and the availability of you to perform services and the covenants provided by you hereunder have been a material consideration for the Company to enter into this Letter Agreement. Accordingly, you may not assign any of your rights or delegate any of your duties under this Letter Agreement, either voluntarily or by operation of law, without the prior written consent of the Company, which may be given or withheld by the Company in its sole and absolute discretion.",
    "target": 0
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "text": "Value(dtype='string', id=None)",
  "target": "ClassLabel(num_classes=19, names=['Assignment', 'Attorney Fees', 'Bankruptcy', 'Change of Control', 'Compliance with Laws', 'Confidentiality', 'Entire Agreement', 'General Definition', 'Governing Law', 'Indemnification', 'Injunctive Relief', 'Jurisdiction and Venue', 'Liens', 'No Warranties', 'Other', 'Permitted Disclosure', 'Survival', 'Term', 'Termination for Convenience'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 119023 |
| valid        | 13225 |
