---
language: 
- en
license: 
- apache-2.0
task_categories:
- question-answering
pretty_name: 'Battery Device Question Answering Dataset'
---
# Battery Device QA Data

Battery device records, including anode, cathode, and electrolyte.

Examples of the question answering evaluation dataset: 

\{'question': 'What is the cathode?', 'answer': 'Al foil', 'context': 'The blended slurry was then cast onto a clean current collector (Al foil for the cathode and Cu foil for the anode) and dried at 90 °C under vacuum overnight.', 'start index': 645\}


\{'question': 'What is the anode?', 'answer': 'Cu foil', 'context': 'The blended slurry was then cast onto a clean current collector (Al foil for the cathode and Cu foil for the anode) and dried at 90 °C under vacuum overnight. Finally, the obtained electrodes were cut into desired shapes on demand. It should be noted that the electrode mass ratio of cathode/anode is set to about 4, thus achieving the battery balance.', 'start index': 673\}


\{'question': 'What is the cathode?', 'answer': 'SiC/RGO nanocomposite', 'context': 'In conclusion, the SiC/RGO nanocomposite, integrating the synergistic effect of SiC flakes and RGO, was synthesized by an in situ gas–solid fabrication method. Taking advantage of the enhanced photogenerated charge separation, large CO2 adsorption, and numerous exposed active sites, SiC/RGO nanocomposite served as the cathode material for the photo-assisted Li–CO2 battery.', 'start index': 284\}

# Usage
```
from datasets import load_dataset

dataset = load_dataset("batterydata/battery-device-data-qa")
```

# Citation
```
@article{huang2022batterybert,
  title={BatteryBERT: A Pretrained Language Model for Battery Database Enhancement},
  author={Huang, Shu and Cole, Jacqueline M},
  journal={J. Chem. Inf. Model.},
  year={2022},
  doi={10.1021/acs.jcim.2c00035},
  url={DOI:10.1021/acs.jcim.2c00035},
  pages={DOI: 10.1021/acs.jcim.2c00035},
  publisher={ACS Publications}
}
```