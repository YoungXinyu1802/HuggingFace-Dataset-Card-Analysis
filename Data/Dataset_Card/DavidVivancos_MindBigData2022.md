# MindBigData 2022 A Large Dataset of Brain Signals
> Supporting datasets for paper [ arXiv:2212.14746](https://arxiv.org/abs/2212.14746)
> There are 3 Main datasets with subdatasets:
>   
**1.- MindBigData MNIST of Brain Digits**

> based on http://mindbigdata.com/opendb/index.html
> But all datasets splitted to 80% Train 20% Test (also proportional in the 11 classes)
> EEG's Resampled to match original headsets sampling rate
> Included headers.
> and simplified to contain only label  & EEG data as rows named in headers as ChannelName-SampleNum, ie for channel FP1 and MindWave will be  FP1-0 FP1-1 ..... FP1-1023  since there are 1024 samples.
> There are 4 subdatasets:
> 
> For MindWave with 1 EEG Channel and 1024 samples x Channel
> 
> For EPOC1 with 14 EEG Channels and 256 samples x Channel
> 
> For Muse1 with 4 EEG Channels and 440 samples x Channel
> 
> For Insight1 with 5 EEG Channels and 256 samples x Channel
> 
**1.1.- MindBigData MNIST of Brain digits MindWave1**
https://huggingface.co/datasets/DavidVivancos/MindBigData2022_MNIST_MW
> 
**1.2.- MindBigData MNIST of Brain digits EPOC1**
https://huggingface.co/datasets/DavidVivancos/MindBigData2022_MNIST_EP

**1.3.- MindBigData MNIST of Brain digits Muse1**
https://huggingface.co/datasets/DavidVivancos/MindBigData2022_MNIST_MU

**1.4.- MindBigData MNIST of Brain digits Insight1**
https://huggingface.co/datasets/DavidVivancos/MindBigData2022_MNIST_IN

**2.- MindBigData Imagenet of the Brain**

> based on http://mindbigdata.com/opendb/imagenet.html
> But all datasets splitted to 80% Train 20% Test (also proportional in  all the classes)
> EEG's Resampled to match original headsets sampling rate
> Included headers.
> contains label as the ILSVRC2013 category, and a hotencoded name lists, the RGB pixel values of the image seen resampled to 150pixels by 150 pixels  & EEG data as rows named in headers as ChannelName-SampleNum, 
> There are 2 subdatasets:
> 
> One with the Insight 1 EEG signals at 384 samples per channel (5 channels)
> 
> One with the Spectrogram image 64x64px instead of the EEG as described in the paper
> 
 **2.1.- MindBigData Imagenet of the Brain Insight1 EEG**
 https://huggingface.co/datasets/DavidVivancos/MindBigData2022_Imagenet_IN
 
 **2.2.- MindBigData Imagenet of the Brain Insight1 Spectrogram**
 https://huggingface.co/datasets/DavidVivancos/MindBigData2022_Imagenet_IN_Spct

**3.- MindBigData Visual MNIST of Brain Digits**

> based on http://mindbigdata.com/opendb/visualmnist.html
> But all datasets splitted to 80% Train 20% Test (also proportional in the 11 classes)
> Included headers.
> and simplified to contain only label, the original MNIST pixels of the digit seen 28x28pixels  & EEG data as rows named in headers as ChannelName-SampleNum, ie for channel TP9 and Muse2 will be  TP9-0 TP9-1 ..... TP9-511  since there are 512 samples.
> There are 3 subdatasets:
> 
> For Muse2 with 5 EEG Channels, 3 PPG Channels, 3 ACC Channels & 3 GYR Channels and 512 samples x Channel
> 
> For Cap64 with 64 EEG Channels and 400 samples x Channel
>
> For Cap64 with 64 EEG Channels and 400 samples x Channel but with Morlet png images as EEG outputs
> 
**3.1.- MindBigData Visual MNIST of Brain digits Muse2**
https://huggingface.co/datasets/DavidVivancos/MindBigData2022_VisMNIST_MU2

**3.2.- MindBigData Visual MNIST of Brain digits Cap64**
https://huggingface.co/datasets/DavidVivancos/MindBigData2022_VisMNIST_Cap64

**3.3.- MindBigData Visual MNIST of Brain digits Cap64 Morlet**
https://huggingface.co/datasets/DavidVivancos/MindBigData2022_VisMNIST_Cap64_Morlet
