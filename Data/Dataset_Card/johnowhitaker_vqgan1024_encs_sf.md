Images from CC12M encoded with VQGAN f16 1024

Script to continue prep is included in the repo if you want more than the ~1.5M images I did here.

VQGAN model:
```
!curl -L 'https://heibox.uni-heidelberg.de/d/8088892a516d4e3baf92/files/?p=%2Fckpts%2Flast.ckpt&dl=1' > vqgan_im1024.ckpt
!curl -L 'https://heibox.uni-heidelberg.de/d/8088892a516d4e3baf92/files/?p=%2Fconfigs%2Fmodel.yaml&dl=1' > vqgan_im1024.yaml 
```

Try it out: TODO