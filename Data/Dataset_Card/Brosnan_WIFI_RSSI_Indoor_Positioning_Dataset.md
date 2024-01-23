---
license: cc-by-nc-sa-4.0
language_creators:
- expert-generated
pretty_name: WiFi RSSI Indoor Localization
size_categories:
- 100K<n<1M
task_categories:
- tabular-classification
task_ids:
- tabular-single-column-regression
tags:
- wifi
- indoor-positioning
- indoor-localisation
- wifi-rssi
- rssi
- recurrent-neural-networks 
---


# WIFI RSSI Indoor Positioning Dataset

A reliable and comprehensive public WiFi fingerprinting database for researchers to implement and compare the indoor localization’s methods.The database contains RSSI information from 6 APs conducted in different days with the support of autonomous robot.

We use an autonomous robot to collect the WiFi fingerprint data. Our 3-wheel robot has multiple sensors including wheel odometer, an inertial measurement unit (IMU), a LIDAR, sonar sensors and a color and depth (RGB-D) camera. The robot can navigate to a target location to collect WiFi fingerprints automatically. The localization accuracy of the robot is 0.07 m ± 0.02 m. The dimension of the area is 21 m × 16 m. It has three long corridors. There are six APs and five of them provide two distinct MAC address for 2.4- and 5-GHz communications channels, respectively, except for one that only operates on 2.4-GHz frequency. There is one router can provide CSI information.


# Data Format

X Position (m), Y Position (m), RSSI Feature 1 (dBm), RSSI Feature 2 (dBm), RSSI Feature 3 (dBm), RSSI Feature 4 (dBm), ...



