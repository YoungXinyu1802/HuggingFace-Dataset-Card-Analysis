---
{}

---
# AutoTrain Dataset for project: sample-diabetes-predict

## Dataset Descritpion

This dataset has been automatically processed by AutoTrain for project sample-diabetes-predict.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "target": 0,
    "feat_HighBP": 0.0,
    "feat_HighChol": 0.0,
    "feat_CholCheck": 1.0,
    "feat_BMI": 34.0,
    "feat_Smoker": 1.0,
    "feat_Stroke": 0.0,
    "feat_HeartDiseaseorAttack": 0.0,
    "feat_PhysActivity": 1.0,
    "feat_Fruits": 1.0,
    "feat_Veggies": 1.0,
    "feat_HvyAlcoholConsump": 0.0,
    "feat_AnyHealthcare": 1.0,
    "feat_NoDocbcCost": 0.0,
    "feat_GenHlth": 3.0,
    "feat_MentHlth": 0.0,
    "feat_PhysHlth": 0.0,
    "feat_DiffWalk": 0.0,
    "feat_Sex": 0.0,
    "feat_Age": 6.0,
    "feat_Education": 6.0,
    "feat_Income": 7.0
  },
  {
    "target": 1,
    "feat_HighBP": 0.0,
    "feat_HighChol": 0.0,
    "feat_CholCheck": 1.0,
    "feat_BMI": 46.0,
    "feat_Smoker": 1.0,
    "feat_Stroke": 0.0,
    "feat_HeartDiseaseorAttack": 0.0,
    "feat_PhysActivity": 1.0,
    "feat_Fruits": 1.0,
    "feat_Veggies": 1.0,
    "feat_HvyAlcoholConsump": 0.0,
    "feat_AnyHealthcare": 1.0,
    "feat_NoDocbcCost": 0.0,
    "feat_GenHlth": 2.0,
    "feat_MentHlth": 1.0,
    "feat_PhysHlth": 0.0,
    "feat_DiffWalk": 0.0,
    "feat_Sex": 1.0,
    "feat_Age": 10.0,
    "feat_Education": 6.0,
    "feat_Income": 5.0
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "target": "ClassLabel(num_classes=2, names=['0.0', '1.0'], id=None)",
  "feat_HighBP": "Value(dtype='float64', id=None)",
  "feat_HighChol": "Value(dtype='float64', id=None)",
  "feat_CholCheck": "Value(dtype='float64', id=None)",
  "feat_BMI": "Value(dtype='float64', id=None)",
  "feat_Smoker": "Value(dtype='float64', id=None)",
  "feat_Stroke": "Value(dtype='float64', id=None)",
  "feat_HeartDiseaseorAttack": "Value(dtype='float64', id=None)",
  "feat_PhysActivity": "Value(dtype='float64', id=None)",
  "feat_Fruits": "Value(dtype='float64', id=None)",
  "feat_Veggies": "Value(dtype='float64', id=None)",
  "feat_HvyAlcoholConsump": "Value(dtype='float64', id=None)",
  "feat_AnyHealthcare": "Value(dtype='float64', id=None)",
  "feat_NoDocbcCost": "Value(dtype='float64', id=None)",
  "feat_GenHlth": "Value(dtype='float64', id=None)",
  "feat_MentHlth": "Value(dtype='float64', id=None)",
  "feat_PhysHlth": "Value(dtype='float64', id=None)",
  "feat_DiffWalk": "Value(dtype='float64', id=None)",
  "feat_Sex": "Value(dtype='float64', id=None)",
  "feat_Age": "Value(dtype='float64', id=None)",
  "feat_Education": "Value(dtype='float64', id=None)",
  "feat_Income": "Value(dtype='float64', id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 56552 |
| valid        | 14140 |
