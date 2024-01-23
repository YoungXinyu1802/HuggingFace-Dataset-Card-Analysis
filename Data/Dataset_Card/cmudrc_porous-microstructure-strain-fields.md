---
license: cc-by-4.0
language: en
doi: 10.1016/j.dib.2020.106627
viewer: false
---
This dataset contains several microstructure treatments:
1. [`variable_radius.zip`](https://huggingface.co/datasets/cmudrc/porous-microstructure-strain-fields/blob/main/variable_radius.zip)
    - Single split
    - Ten microstructures with defects of variable radii, from 0.01 mm to 0.5 mm.
    - ```data = datasets.load_dataset("cmudrc/porous-microstructure-strain-fields", data_files=['variable_radius.zip'])```
2. [`variable_number.zip`](https://huggingface.co/datasets/cmudrc/porous-microstructure-strain-fields/blob/main/variable_number.zip)
    - Single split
    - Ten microstructures with different numbers of defects, from 20 to 200.
    - ```data = datasets.load_dataset("cmudrc/porous-microstructure-strain-fields", data_files=['variable_number.zip'])```
3. [`circular_defects.zip`](https://huggingface.co/datasets/cmudrc/porous-microstructure-strain-fields/blob/main/circular_defects.zip)
    - Single split (1000 samples)
    - This data contains samples of microstructures with 100 circular porosity defects having their radii uniformly distributed in the range 0.1 – 0.5 mm, and their corresponding strain fields.
    - ```data = datasets.load_dataset("cmudrc/porous-microstructure-strain-fields", data_files=['circular_defects.zip'])```
6. A variety of different defect shapes in smaller datasets:
    - [circle/](https://huggingface.co/datasets/cmudrc/porous-microstructure-strain-fields/tree/main/circle)
      - Train split (500 samples) and test split (50 samples)
      - Circular porosity
      - ```data = datasets.load_dataset("cmudrc/porous-microstructure-strain-fields", data_dir=['circle'])```
    - [crescent/](https://huggingface.co/datasets/cmudrc/porous-microstructure-strain-fields/tree/main/crescent)
      - Train split (500 samples) and test split (50 samples)
      - Crescent-shaped porosity
      - ```data = datasets.load_dataset("cmudrc/porous-microstructure-strain-fields", data_dir=['crescent'])```
    - [ellipse/](https://huggingface.co/datasets/cmudrc/porous-microstructure-strain-fields/tree/main/ellipse)
      - Train split (500 samples) and test split (50 samples)
      - Circular porosity
      - ```data = datasets.load_dataset("cmudrc/porous-microstructure-strain-fields", data_dir=['circle'])```
    - [peanut/](https://huggingface.co/datasets/cmudrc/porous-microstructure-strain-fields/tree/main/peanut)
      - Train split (500 samples) and test split (50 samples)
      - Peanuty porosity
      - ```data = datasets.load_dataset("cmudrc/porous-microstructure-strain-fields", data_dir=['peanut'])```
    - [rectangle/](https://huggingface.co/datasets/cmudrc/porous-microstructure-strain-fields/tree/main/rectangle)
      - Train split (500 samples) and test split (50 samples)
      - Rectangular porosity
      - ```data = datasets.load_dataset("cmudrc/porous-microstructure-strain-fields", data_dir=['rectangle'])```
    - [triangle/](https://huggingface.co/datasets/cmudrc/porous-microstructure-strain-fields/tree/main/triangle)
      - Train split (500 samples) and test split (50 samples)
      - Triangular porosity
      - ```data = datasets.load_dataset("cmudrc/porous-microstructure-strain-fields", data_dir=['triangle'])```