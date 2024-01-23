---
{}

---
# AutoTrain Dataset for project: Engage

## Dataset Descritpion

This dataset has been automatically processed by AutoTrain for project Engage.

### Languages

The BCP-47 code for the dataset's language is unk.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "feat_km_driven": 0.0296548632976001,
    "feat_seats": 0.4166666666666666,
    "feat_how_old": 0.1923076923076923,
    "feat_EngineCC": 0.5218120805369127,
    "feat_mileage_conv": 0.3666666666666666,
    "feat_torque_conv": 0.3509308849783218,
    "feat_max_power_conv": 0.2374727668845316,
    "feat_Automatic": 0.0,
    "feat_Manual": 1.0,
    "feat_First Owner": 1.0,
    "feat_Fourth & Above Owner": 0.0,
    "feat_Second Owner": 0.0,
    "feat_Test Drive Car": 0.0,
    "feat_Third Owner": 0.0,
    "feat_Dealer": 0.0,
    "feat_Individual": 1.0,
    "feat_Trustmark Dealer": 0.0,
    "feat_CNG": 0.0,
    "feat_Diesel": 1.0,
    "feat_LPG": 0.0,
    "feat_Petrol": 0.0,
    "target": 715000.0
  },
  {
    "feat_km_driven": 0.0338913328611081,
    "feat_seats": 0.2499999999999999,
    "feat_how_old": 0.4615384615384616,
    "feat_EngineCC": 0.0577181208053691,
    "feat_mileage_conv": 0.469047619047619,
    "feat_torque_conv": 0.0729405763835756,
    "feat_max_power_conv": 0.0367647058823529,
    "feat_Automatic": 0.0,
    "feat_Manual": 1.0,
    "feat_First Owner": 0.0,
    "feat_Fourth & Above Owner": 0.0,
    "feat_Second Owner": 1.0,
    "feat_Test Drive Car": 0.0,
    "feat_Third Owner": 0.0,
    "feat_Dealer": 0.0,
    "feat_Individual": 1.0,
    "feat_Trustmark Dealer": 0.0,
    "feat_CNG": 0.0,
    "feat_Diesel": 0.0,
    "feat_LPG": 0.0,
    "feat_Petrol": 1.0,
    "target": 110000.0
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "feat_km_driven": "Value(dtype='float64', id=None)",
  "feat_seats": "Value(dtype='float64', id=None)",
  "feat_how_old": "Value(dtype='float64', id=None)",
  "feat_EngineCC": "Value(dtype='float64', id=None)",
  "feat_mileage_conv": "Value(dtype='float64', id=None)",
  "feat_torque_conv": "Value(dtype='float64', id=None)",
  "feat_max_power_conv": "Value(dtype='float64', id=None)",
  "feat_Automatic": "Value(dtype='float64', id=None)",
  "feat_Manual": "Value(dtype='float64', id=None)",
  "feat_First Owner": "Value(dtype='float64', id=None)",
  "feat_Fourth & Above Owner": "Value(dtype='float64', id=None)",
  "feat_Second Owner": "Value(dtype='float64', id=None)",
  "feat_Test Drive Car": "Value(dtype='float64', id=None)",
  "feat_Third Owner": "Value(dtype='float64', id=None)",
  "feat_Dealer": "Value(dtype='float64', id=None)",
  "feat_Individual": "Value(dtype='float64', id=None)",
  "feat_Trustmark Dealer": "Value(dtype='float64', id=None)",
  "feat_CNG": "Value(dtype='float64', id=None)",
  "feat_Diesel": "Value(dtype='float64', id=None)",
  "feat_LPG": "Value(dtype='float64', id=None)",
  "feat_Petrol": "Value(dtype='float64', id=None)",
  "target": "Value(dtype='float32', id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 7115 |
| valid        | 791 |
