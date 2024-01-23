This a subset of "ceyda/smithsonian_butterflies" dataset with additional processing done to train the "ceyda/butterfly_gan" model.

The preprocessing includes:
- Adding "sim_score" to images with CLIP model using "pretty butterfly","one butterfly","butterfly with open wings","colorful butterfly" 
- Removing butterflies with the same name(species)
- Limiting only to the top 1000 images
- Removing the background (doing another sim_scoring after bg removal did visually worse so didn't do it)
- Detecting contours 
- Cropping to the bounding box of the contour with the largest area
- Converting back to RGB
