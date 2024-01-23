---
license: cc-by-nc-4.0
---
# Dataset Card for BBBicycles
## Dataset Summary
Bent & Broken Bicycles (BBBicycles) dataset is a benchmark set for the novel task of **damaged object re-identification**, which aims to identify the same object in multiple images even in the presence of breaks, deformations, and missing parts. You can find an interactive preview [here](https://huggingface.co/spaces/GrainsPolito/BBBicyclesPreview).
## Dataset Structure
The final dataset contains:

 - Total of  39,200 image
 - 2,800 unique IDs
 - 20 models
 - 140 IDs for each model

<table border-collapse="collapse">
 <tr>
    <td><b style="font-size:25px">Information for each ID:</b></td>
    <td><b style="font-size:25px">Information for each render:</b></td>
 </tr>
 <tr>
    <td>
        <ul>
            <li>Model</li>
            <li>Type</li>
            <li>Texture type</li>
            <li>Stickers</li>
        </ul>
    </td>
    <td>
        <ul>
            <li>Background</li>
            <li>Viewing Side</li>
            <li>Focal Length</li>
            <li>Presence of dirt</li>
        </ul>
    </td>
 </tr>
</table>

### Citation Information
```
@inproceedings{bbb_2022,
  title={Bent & Broken Bicycles: Leveraging synthetic data for damaged object re-identification},
  author={Luca Piano, Filippo Gabriele Pratticò, Alessandro Sebastian Russo, Lorenzo Lanari, Lia Morra, Fabrizio Lamberti},
  booktitle={2022 IEEE Winter Conference on Applications of Computer Vision (WACV)},
  year={2022},
  organization={IEEE}
}

```

### Credits
The authors gratefully acknowledge the financial support of Reale Mutua Assicurazioni.