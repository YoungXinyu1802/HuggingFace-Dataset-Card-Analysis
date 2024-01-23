---
annotations_creators:
- unknown
language_creators:
- unknown
license: unknown
size_categories:
- n<1K
source_datasets:
- unknown
task_categories:
- audio-classification
task_ids: []
tags:
- audio-slot-filling
---

# TAU Spatial Room Impulse Response Database (TAU-SRIR DB)

## Important

**This is a copy from the Zenodo Original one**

## Description

[Audio Research Group / Tampere University](https://webpages.tuni.fi/arg/)

AUTHORS

**Tampere University**

- Archontis Politis ([contact](mailto:archontis.politis@tuni.fi), [profile](https://scholar.google.fi/citations?user=DuCqB3sAAAAJ&hl=en))
- Sharath Adavanne ([contact](mailto:sharath.adavanne@tuni.fi), [profile](https://www.aane.in))
- Tuomas Virtanen ([contact](mailto:tuomas.virtanen@tuni.fi), [profile](https://homepages.tuni.fi/tuomas.virtanen/))

**Data Collection 2019-2020**

- Archontis Politis
- Aapo Hakala
- Ali Gohar

**Data Collection 2017-2018**

- Sharath Adavanne
- Aapo Hakala
- Eemi Fagerlund
- Aino Koskimies

The **TAU Spatial Room Impulse Response Database (TAU-SRIR DB)** database contains spatial room impulse responses (SRIRs) captured in various spaces of Tampere University (TAU), Finland, for a fixed receiver position and multiple source positions per room, along with separate recordings of spatial ambient noise captured at the same recording point. The dataset is intended for emulation of spatial multichannel recordings for evaluation and/or training of multichannel processing algorithms in realistic reverberant conditions and over multiple rooms. The major distinct properties of the database compared to other databases of room impulse responses are:

- Capturing in a high resolution multichannel format (32 channels) from which multiple more limited application-specific formats can be derived (e.g. tetrahedral array, circular array, first-order Ambisonics, higher-order Ambisonics, binaural).
- Extraction of densely spaced SRIRs along measurement trajectories, allowing emulation of moving source scenarios.
- Multiple source distances, azimuths, and elevations from the receiver per room, allowing emulation of complex configurations for multi-source methods.
- Multiple rooms, allowing evaluation of methods at various acoustic conditions, and training of methods with the aim of generalization on different rooms.

The RIRs were collected by staff of TAU between 12/2017 - 06/2018, and between 11/2019 - 1/2020. The data collection received funding from the European Research Council, grant agreement [637422 EVERYSOUND](https://cordis.europa.eu/project/id/637422).
[![ERC](https://erc.europa.eu/sites/default/files/content/erc_banner-horizontal.jpg "ERC")](https://erc.europa.eu/)

> **NOTE**: This database is a work-in-progress. We intend to publish additional rooms, additional formats, and potentially higher-fidelity versions of the captured responses in the near future, as new versions of the database in this repository.

## Report and reference

A compact description of the dataset, recording setup, recording procedure, and extraction can be found in:

>Politis., Archontis, Adavanne, Sharath, & Virtanen, Tuomas (2020). **A Dataset of Reverberant Spatial Sound Scenes with Moving Sources for Sound Event Localization and Detection**. In _Proceedings of the Detection and Classification of Acoustic Scenes and Events 2020 Workshop (DCASE2020)_, Tokyo, Japan.

available [here](https://dcase.community/documents/workshop2020/proceedings/DCASE2020Workshop_Politis_88.pdf). A more detailed report specifically focusing on the dataset collection and properties will follow.

## Aim

The dataset can be used for generating multichannel or monophonic mixtures for testing or training of methods under realistic reverberation conditions, related to e.g. multichannel speech enhancement, acoustic scene analysis, and machine listening, among others. It is especially suitable for the follow application scenarios:

- monophonic and multichannal reverberant single- or multi-source speech in multi-room reverberant conditions,
- monophonic and multichannel polyphonic sound events in multi-room reverberant conditions,
- single-source and multi-source localization in multi-room reverberant conditions, in static or dynamic scenarios,
- single-source and multi-source tracking in multi-room reverberant conditions, in static or dynamic scenarios,
- sound event localization and detection in multi-room reverberant conditions, in static or dynamic scenarios.

## Specifications

The SRIRs were captured using an [Eigenmike](https://mhacoustics.com/products) spherical microphone array. A [Genelec G Three loudspeaker](https://www.genelec.com/g-three) was used to playback a maximum length sequence (MLS) around the Eigenmike. The SRIRs were obtained in the STFT domain using a least-squares regression between the known measurement signal (MLS) and far-field recording independently at each frequency. In this version of the dataset the SRIRs and ambient noise are downsampled to 24kHz for compactness.

The currently published SRIR set was recorded at nine different indoor locations inside the Tampere University campus at Hervanta, Finland. Additionally, 30 minutes of ambient noise recordings were collected at the same locations with the IR recording setup unchanged. SRIR directions and distances differ with the room. Possible azimuths span the whole range of $\phi\in[-180,180)$, while the elevations span approximately a range between $\theta\in[-45,45]$ degrees. The currently shared measured spaces are as follows:

1. Large open space in underground bomb shelter, with plastic-coated floor and rock walls. Ventilation noise.
2. Large open gym space. Ambience of people using weights and gym equipment in adjacent rooms. 
3. Small classroom (PB132) with group work tables and carpet flooring. Ventilation noise. 
4. Meeting room (PC226) with hard floor and partially glass walls. Ventilation noise. 
5. Lecture hall (SA203) with inclined floor and rows of desks. Ventilation noise. 
6. Small classroom (SC203) with group work tables and carpet flooring. Ventilation noise. 
7. Large classroom (SE203) with hard floor and rows of desks. Ventilation noise. 
8. Lecture hall (TB103) with inclined floor and rows of desks. Ventilation noise. 
9. Meeting room (TC352) with hard floor and partially glass walls. Ventilation noise. 

The measurement trajectories were organized in groups, with each group being specified by a circular or linear trace at the floor at a certain distance (range) from the z-axis of the microphone. For circular trajectories two ranges were measured, a _close_ and a _far_ one, except room TC352, where the same range was measured twice, but with different furniture configuration and open or closed doors. For linear trajectories also two ranges were measured, _close_ and _far_, but with linear paths at either side of the array, resulting in 4 unique trajectory groups, with the exception of room SA203 where 3 ranges were measurd resulting on 6 trajectory groups. Linear trajectory groups are always parallel to each other, in the same room.

Each trajectory group had multiple measurement trajectories, following the same floor path, but with the source at different heights. 
The SRIRs are extracted from the noise recordings of the slowly moving source across those trajectories, at an angular spacing of approximately every 1 degree from the microphone. This extraction scheme instead of extracting SRIRs at equally spaced points along the path (e.g. every 20cm) was found more practical for synthesis purposes, making emulation of moving sources at an approximately constant angular speed easier.

The following table summarizes the above properties for the currently available rooms:

|   | Room name                 | Room type                     | Traj. type | # ranges   | # trajectory groups | # heights/group   | # trajectories (total) | # RIRs/DOAs |
|---|--------------------------|----------------------------|------------|-------------|-----------------------|---------------------|------------------------|-------------|
| 1 | Bomb shelter              | Complex/semi-open     | Circular    | 2               | 2                             | 9                           | 18                             | 6480        |
| 2 | Gym                            | Rectangular/large         | Circular    | 2              | 2                              | 9                           | 18                             | 6480        |
| 3 | PB132 Meeting room | Rectangular/small         | Circular    | 2              | 2                              | 9                           | 18                             | 6480        |
| 4 | PC226 Meeting room | Rectangular/small         | Circular    | 2              | 2                              | 9                           | 18                             | 6480        |
| 5 | SA203 Lecture hall     | Trapezoidal/large           | Linear      | 3              | 6                              | 3                           | 18                             | 1594        |
| 6 | SC203 Classroom      | Rectangular/medium     | Linear      | 2              | 4                              | 5                           | 20                             | 1592        |
| 7 | SE203 Classroom      | Rectangular/large          | Linear       | 2             | 4                              | 4                            | 16                            | 1760        |
| 8 | TB103 Classroom      | Trapezoidal/large           | Linear       | 2             | 4                              | 3                            | 12                            | 1184        |
| 9 | TC352 Meeting room | Rectangular/small         | Circular     | 1             | 2                              | 9                            | 18                            | 6480        |

More details on the trajectory geometries can be found in the database info file (`measinfo.mat`).

## Recording formats

The array response of the two recording formats can be considered known. The following theoretical spatial responses (steering vectors) modeling the two formats describe the directional response of each channel to a source incident from direction-of-arrival (DOA) given by azimuth angle $\phi$ and elevation angle $\theta$.

**For the first-order ambisonics (FOA):**

\begin{eqnarray}
H_1(\phi, \theta, f) &=& 1 \\
H_2(\phi, \theta, f) &=& \sin(\phi) * \cos(\theta) \\
H_3(\phi, \theta, f) &=& \sin(\theta) \\
H_4(\phi, \theta, f) &=& \cos(\phi) * \cos(\theta)
\end{eqnarray}

The (FOA) format is obtained by converting the 32-channel microphone array signals by means of encoding filters based on anechoic measurements of the Eigenmike array response. Note that in the formulas above the encoding format is assumed frequency-independent, something that holds true up to around 9kHz with the specific microphone array, while the actual encoded responses start to deviate gradually at higher frequencies from the ideal ones provided above. Routines that can compute the matrix of encoding filters for spherical and general arrays, based on theoretical array models or measurements, can be found [here](https://github.com/polarch/Spherical-Array-Processing).

**For the tetrahedral microphone array (MIC):**

The four microphone have the following positions, in spherical coordinates $(\phi, \theta, r)$:

\begin{eqnarray} 
M1: &\quad(&45^\circ, &&35^\circ, &4.2\mathrm{cm})\nonumber\\
M2: &\quad(&-45^\circ, &-&35^\circ, &4.2\mathrm{cm})\nonumber\\
M3: &\quad(&135^\circ, &-&35^\circ, &4.2\mathrm{cm})\nonumber\\
M4: &\quad(&-135^\circ, &&35^\circ, &4.2\mathrm{cm})\nonumber
\end{eqnarray}

Since the microphones are mounted on an acoustically-hard spherical baffle, an analytical expression for the directional array response is given by the expansion:
\begin{equation}
H_m(\phi_m, \theta_m, \phi, \theta, \omega) = \frac{1}{(\omega R/c)^2}\sum_{n=0}^{30} \frac{i^{n-1}}{h_n'^{(2)}(\omega R/c)}(2n+1)P_n(\cos(\gamma_m))
\end{equation}

where $m$ is the channel number, $(\phi_m, \theta_m)$ are the specific microphone's azimuth and elevation position, $\omega = 2\pi f$ is the angular frequency, $R = 0.042$m is the array radius, $c = 343$m/s is the speed of sound, $\cos(\gamma_m)$ is the cosine angle between the microphone and the DOA, and $P_n$ is the unnormalized Legendre polynomial of degree $n$, and $h_n'^{(2)}$ is the derivative with respect to the argument of a spherical Hankel function of the second kind. The expansion is limited to 30 terms which provides negligible modeling error up to 20kHz. Example routines that can generate directional frequency and impulse array responses based on the above formula can be found [here](https://github.com/polarch/Array-Response-Simulator).

## Reference directions-of-arrival

For each extracted RIR across a measurement trajectory there is a direction-of-arrival (DOA) associated with it, which can be used as the reference direction for sound source spatialized using this RIR, for training or evaluation purposes. The DOAs were determined acoustically from the extracted RIRs, by windowing the direct sound part and applying a broadband version of the MUSIC localization algorithm on the windowed multichannel signal.

The DOAs are provided as Cartesian components [x, y, z] of unit length vectors. 

## Scene generator

A set of routines is shared, here termed scene generator, that can spatialize a bank of sound samples using the SRIRs and noise recordings of this library, to emulate scenes for the two target formats. The code is the same as the one used to generate the [**TAU-NIGENS Spatial Sound Events 2021**](https://doi.org/10.5281/zenodo.5476980) dataset, and has been ported to Python from the original version written in Matlab.

The generator can be found [**here**](https://github.com/danielkrause/DCASE2022-data-generator), along with more details on its use. 

The generator at the moment is set to work with the [NIGENS](https://zenodo.org/record/2535878) sound event sample database, and the [FSD50K](https://zenodo.org/record/4060432) sound event database, but additional sample banks can be added with small modifications.

The dataset together with the generator has been used by the authors in the following public challenges:

- [DCASE 2019 Challenge Task 3](https://dcase.community/challenge2019/task-sound-event-localization-and-detection), to generate the **TAU Spatial Sound Events 2019** dataset ([development](https://doi.org/10.5281/zenodo.2599196)/[evaluation](https://doi.org/10.5281/zenodo.3377088))
- [DCASE 2020 Challenge Task 3](https://dcase.community/challenge2020/task-sound-event-localization-and-detection), to generate the [**TAU-NIGENS Spatial Sound Events 2020**](https://doi.org/10.5281/zenodo.4064792) dataset
- [DCASE2021 Challenge Task 3](https://dcase.community/challenge2021/task-sound-event-localization-and-detection), to generate the [**TAU-NIGENS Spatial Sound Events 2021**](https://doi.org/10.5281/zenodo.5476980) dataset
- [DCASE2022 Challenge Task 3](https://dcase.community/challenge2022/task-sound-event-localization-and-detection), to generate additional [SELD synthetic mixtures for training the task baseline](https://doi.org/10.5281/zenodo.6406873)

> **NOTE**: The current version of the generator is work-in-progress, with some code being quite "rough". If something does not work as intended or it is not clear what certain parts do, please contact [daniel.krause@tuni.fi](mailto:daniel.krause@tuni.fi), or [archontis.politis@tuni.fi](mailto:archontis.politis@tuni.fi).

## Dataset structure

The dataset contains a folder of the SRIRs (`TAU-SRIR_DB`), with all the SRIRs per room in a single _mat_ file, e.g. `rirs_09_tb103.mat`.   The specific room had 4 trajectory groups measured at 3 different heights, hence the mat file contains an `rirs` array of 4x3 structures, each with the fields `mic` and `foa`. Selecting e.g. the 2nd trajectory and 3rd height with `rirs(2,3)` returns `mic` and `foa` fields with an array of size `[7200x4x114]` on each. The array contains the SRIRs for the specific format, and it is arranged as `[samples x channels x DOAs]`, meaning that 300msec long (7200samples@24kHz) 4 channel RIRs are extracted at 114 positions along that specific trajectory.

The file `rirdata.mat` contains some general information such as sample rate, format specifications, and most importantly the DOAs of every extracted SRIR. Those can be found in the `rirdata.room` field, which is an array of 9 structures itself, one per room. Checking for example `rirdata.room(8)` returns the name of the specific room (_tb103_), the year the measurements were done, the numbers of SRIRs extracted for each trajectory, and finally the DOAs of the extracted SRIRs. The DOAs of a certain trajectory can be retrieved as e.g. `rirdata.room(8).rirs(2,3).doa_xyz` which returns an array of size `[114x3]`. These are the DOAs of the 114 SRIRs retrieved in the previous step for the 2nd trajectory, 3rd source height, of room `TB103`.

The file `measinfo.mat` contains measurement and recording information in each room. Those details are the name of each room, its dimensions for rectangular or trapezoidal shapes, start and end positions for the linear trajectories, or distances from center for the circular ones, the source heights for each trajectory group, the target formats, the trajectory type,  the recording device, the A-weighted ambient sound pressure level, and the maximum and minimum A-weighted sound pressure level of the measurement noise signal. Coordinates are defined with respect to the origina being at the base of the microphone. Based on the information included in the  `measinfo.mat`, one can plot a 3D arrangement of the trajectories around the microphone, even though keep in mind that these would be the ideal circular or linear intended trajectories, while the actual DOAs obtained from acoustic analysis have some deviations around those ideal paths.

Finally, the dataset contains a folder of spatial ambient noise recordings (`TAU-SNoise_DB`), with one subfolder per room having two audio recordings fo the spatial ambience, one for each format, FOA or MIC.  The recordings vary in length between rooms, ranging from about 20 mins to 30 mins. Users of the dataset can segment these recordings and add them to spatialized sound samples at desired SNRs, or mix different segments to augment the recordings to additional ambience than the original recording time. Such a use case is demonstrated in the scene generator examples.

## Download

The files `TAU-SRIR_DB.z01`, ..., `TAU-SRIR_DB.zip` contain the SRIRs and measurement info files.
The files `TAU-SNoise_DB.z01`, ..., `TAU-SNoise_DB.zip` contain the ambient noise recordings.

Download the zip files and use your preferred compression tool to unzip these split zip files. To extract a split zip archive (named as zip, z01, z02, ...), you could use, for example, the following syntax in Linux or OSX terminal:

Combine the split archive to a single archive:
>zip -s 0 split.zip --out single.zip

Extract the single archive using unzip:
>unzip single.zip

# License

The database is published under a custom **open non-commercial with attribution** license. It can be found in the `LICENSE.txt` file that accompanies the data.

