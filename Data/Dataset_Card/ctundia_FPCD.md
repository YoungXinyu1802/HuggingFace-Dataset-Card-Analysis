---
license: cc-by-nc-4.0
---
<b>Dataset Description</b>:-
 MIS Farm Pond Change Detection Dataset  consists of a total of 694 images of size 1024 x 768 pixels at zoom level 18 with a very high resolution up to 1 meter) were collected from Google Earth images. The region of Indian state of Maharashtra was chosen for the dataset. The villages collected have timestamps in months of Jan-April and the minimum year difference is 2 years and the maximum year difference is 9 years, oldest being 2007 and latest being 2021. The types of farm ponds being covered in the dataset are Wet Farm Pond - Lined, Wet Farm Pond - Unlined, Dry Farm Pond - Lined, Dry Farm Pond - Unlined.  The change classes are mainly - Farm Pond Constructed, Farm Pond Demolished, Farm Pond Dried and Farm Pond Wetted. Most of the changes are from the farm pond constructed class showing that there is an increase in farm pond construction across villages in Maharashtra in past 8-9 years. 


<b>T0</b> : Consists of images of time T0 i.e. initial image <br>
<b>T1</b> : Consists of images of time T1 i.e. changed image <br>
<b>task_1</b> : Consists of binary masks of task_1 i.e. Farm Pond Constructed and Farm Pond Demolished <br>
<b>task_2</b> : Consists of binary masks of task_2 i.e. Farm Pond Dried and Farm Pond Wetted <br>
<b>task_3</b> : Consists of binary masks of task_3 i.e. All 4 classes combined:  Farm Pond Constructed, Farm Pond Demolished, Farm Pond Dried and Farm Pond Wetted <br>
 
<b>cd_dataset_train.txt</b> : Contains file_names of train set to be taken from T0, T1 and masks of one of the tasks(task_1, task_2, task_3) <br>
<b>cd_dataset_test.txt</b> : Contains file_names of test set to be taken from T0, T1 and masks of one of the tasks(task_1, task_2, task_3) <br>

<b>object_annotations_train_coco.json</b> : Contains positive images (having annotations) taken from both T0 and T1 in coco format to be used for training - Total 499 <br>
<b>object_annotations_test_coco.json</b> : Contains positive images (having annotations) taken from both T0 and T1 in coco format to be used for testing - Total 92 <br>