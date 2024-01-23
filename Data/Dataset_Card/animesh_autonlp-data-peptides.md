[Deep learning the collisional cross sections of the peptide universe from a million experimental values](https://www.nature.com/articles/s41467-021-21352-8)

[Data](http://proteomecentral.proteomexchange.org/cgi/GetDataset?ID=PXD017703) generated from [MaxQuant](http://coxdocs.org/doku.php?id=maxquant:start) output
```
wget https://ftp.pride.ebi.ac.uk/pride/data/archive/2020/12/PXD017703/HeLa_200ng_Library_MaxQuant.zip
unzip HeLa_200ng_Library_MaxQuant.zip
awk -F '\t' '{print $1,",",$40}' evidence.txt > pepCCS.csv
wc pepCCS.csv
  352111  1056333 12736697 pepCCS.csv
```

[Code](https://github.com/mannlabs/DeepCollisionalCrossSection)
