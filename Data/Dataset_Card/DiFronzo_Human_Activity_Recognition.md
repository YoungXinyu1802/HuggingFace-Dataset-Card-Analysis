Human Activity Recognition (HAR) using smartphones dataset. Classifying the type of movement amongst five categories:
- WALKING,
- WALKING_UPSTAIRS,
- WALKING_DOWNSTAIRS,
- SITTING,
- STANDING

The experiments have been carried out with a group of 16 volunteers within an age bracket of 19-26 years. Each person performed five activities (WALKING, WALKING_UPSTAIRS, WALKING_DOWNSTAIRS, SITTING, STANDING) wearing a smartphone (Samsung Galaxy S8) in the pucket. Using its embedded accelerometer and gyroscope, we captured 3-axial linear acceleration and 3-axial angular velocity at a constant rate of 50Hz. The experiments have been video-recorded to label the data manually. 

```bash
'raw_data/labels.txt': include all the activity labels available for the dataset (1 per row).
   Column 1: experiment number ID,
   Column 2: user number ID,
   Column 3: activity number ID
   Column 4: Label start point (in number of signal log samples (recorded at 50Hz))
   Column 5: Label end point (in number of signal log samples)

activity_type:
 1 WALKING
 2 WALKING_UPSTAIRS
 3 WALKING_DOWNSTAIRS
 4 SITTING
 5 STANDING
```
Repository: [DiFronzo/LSTM-for-Human-Activity-Recognition-classification](https://github.com/DiFronzo/LSTM-for-Human-Activity-Recognition-classification)