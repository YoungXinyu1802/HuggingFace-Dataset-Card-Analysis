# AirDrums Data
This dataset contains all data needed for training

`2d_images` contains raw unsegmented image data for 2-dimensional dataset. filenames are representative of timestamp

`3d_images` contains raw unsegmented image data (paired) for 3-dimensional dataset. filenames are representative of timestamp and camera angle

images from both of the previous sets are to be segmented and converted to a coordinate and direction

`2d_imu` contains IMU data for training in 2-dimensional space (xy) with segmented images from above

`3d_imu` contains IMU data for training in 3-dimensional space(xyz) with segmented images from above and front (xy and yz planes)


---
language: 
- en

tags:
- sensor
- location

datasets:
- 2d_images
- 3d_images
- 2d_imu
- 3d_imu
---

