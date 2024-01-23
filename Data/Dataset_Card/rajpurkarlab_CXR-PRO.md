CXR-PRO contains the following files:

```
.
├── cxr.h5
├── mimic_train_impressions.csv
└── mimic_test_impressions.csv
```

The contents of each file are outlined below:

`cxr.h5`: The subset of MIMIC-CXR chest radiographs used for MIMIC-PRO, saved in Hierarchical Data Format (HDF).
`mimic_train_impressions.csv`: A compilation of the impressions section of each radiology report in the MIMIC-PRO dataset, with references to priors removed. Additional fields include `dicom_id`, `study_id`, and `subject_id` (which refer users to the chest radiograph associated with a given impressions section).
`mimic_test_impressions.csv`: The expert-edited test set, as described in the Methods section of MIMIC-PRO's documentation on PhysioNet.
