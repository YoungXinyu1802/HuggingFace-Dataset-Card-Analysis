---
license: openrail++
task_categories:
- text-to-image
language:
- en
- ja
size_categories:
- 1K<n<10K
---

# VRoid Image Dataset Lite

This is a dataset to train text-to-image or other models without any copyright issue.
All materials used in this dataset are CC0 or properly licensed.

This dataset is also used to train [Mitsua Diffusion One](https://huggingface.co/Mitsua/mitsua-diffusion-one), which is a latent text-to-image diffusion model, whose VAE and U-Net are trained from scratch using only public domain/CC0 or copyright images with permission for use. 

Various parameters such as camera angle, pose, skin color and facial expression were randomly set and the images were output.

## Dataset License
[Creative Open-Rail++-M License](https://huggingface.co/stabilityai/stable-diffusion-2/blob/main/LICENSE-MODEL)

This model is open access and available to all, with a CreativeML OpenRAIL++-M license further specifying rights and usage. The CreativeML OpenRAIL++-M License specifies:

1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL++-M to all your users (please read the license entirely and carefully) [Please read the full license here](https://huggingface.co/stabilityai/stable-diffusion-2/blob/main/LICENSE-MODEL)


## Materials used in this dataset and their licenses
### VRoid Models
- VRM models used in this dataset are all CC0.
- These models are made by VRoid Project
  - [HairSample_Male](https://vroid.pixiv.help/hc/en-us/articles/4402614652569-Do-VRoid-Studio-s-sample-models-come-with-conditions-of-use-)
  - [HairSample_Female](https://vroid.pixiv.help/hc/en-us/articles/4402614652569-Do-VRoid-Studio-s-sample-models-come-with-conditions-of-use-)
  - [AvatarSample-D](https://vroid.pixiv.help/hc/en-us/articles/360012381793-AvatarSample-D)
  - [AvatarSample-E](https://vroid.pixiv.help/hc/en-us/articles/360014900273-AvatarSample-E)
  - [AvatarSample-F](https://vroid.pixiv.help/hc/en-us/articles/360014900113-AvatarSample-F)
  - [AvatarSample-G](https://vroid.pixiv.help/hc/en-us/articles/360014900233-AvatarSample-G)
  - [Sakurada Fumiriya](https://vroid.pixiv.help/hc/en-us/articles/360014788554-Sakurada-Fumiriya)
  - [Sendagaya Shino](https://vroid.pixiv.help/hc/en-us/articles/360013482714-Sendagaya-Shino)
- These models are made by pastelskies
  - [015](https://hub.vroid.com/characters/1636202188966335207/models/6893459099891579554)
  - [009](https://hub.vroid.com/characters/2472286065213980612/models/9151142999439416702)
  - [008](https://hub.vroid.com/characters/601931587119584437/models/3857812504036458003)
- These models are made by yomox9
  - [Qi](https://hub.vroid.com/characters/2048759159111415425/models/6905433332368675090)
- These models are made by くつした
  - [【CC0】オリジナルアバター「少女A」【Cluster想定】](https://hub.vroid.com/characters/5271108759876567944/models/9069514665234246177)
- These models are made by ろーてく
  - [【CC0】オリジナルアバター「シャペル」【VRChat想定】](https://lowteq.booth.pm/items/1349366)


### Pose and motions
- Our original poses.
- Free edition pose subset in [Unity Humanoid AnimationClip - PoseCollection](https://necocoya.booth.pm/items/1634088) made by かんな久＠ねここや様 (❗❗**NOT CC0**❗❗)
  - We have obtained permission directly from the author for training or distributing the AI model.
  - This dataset uses only a subset of the "Free edition (ポーズ詰め合わせ（無料版）in Japanese)", which is allowed to use for AI training.
  - We have confirmed directly from the author that an exact equivalent license is not necesserily needed to distribute the trained model or to generate images.
  - Therefore, to avoid harmful content generation, the Creative Open Rail++-M license is applied to this dataset, and an equivalent or more restrictive license must be applied to its derivatives.

### Shader
- MToon (MIT) with some modification by dev team.

### Other Textures for Skybox / Ground
- [Poly Haven](https://polyhaven.com/) (CC0)
- [ambientCG](https://ambientcg.com/) (CC0)


## Metadata Description
The final caption is not provided in this dataset, but you can create complete caption from metadata.

### Color Shifting
Color shift is used to create more diverse images. It is applied to skin/hair/eye/cloth/accesories independently.
- Parameter xyz = (H_Shift, S_Factor, V_Factor)
- New Color HSV = (H + H_Shift, S * S_Factor, V * V_Factor)

### Metadata Items
- vrm_name : VRoid model name
- clip_name : Pose Clip Number
- camera_profile
- facial_expression
- lighting
- lighting_color
- outline
- shade_toony
- skin_profile
- looking_label
- camera_position : 3D position in meter
- camera_rotation : Pitch/Yaw/Roll in degree
- camera_fov : in degree
- hair_color_shift : HSV color shift of hair
- eye_color_shift : HSV color shift of eye
- color_shift : HSV color shift of cloth and accesories
- ground_plane_material
- left_hand_sign
- right_hand_sign
- skybox


## Full Dataset
This is a subset of full dataset consisting of approx. 600k images.

Full dataset would be available upon request only for non-commercial research purposes. 

You will need to provide 1 TB of online storage so that we could upload the data set or send us an empty 1 TB physical hard drive to our office located in Tokyo Japan.

Contact : info [at] elanmitsua.com

## Developed by
- Abstract Engine dev team
- Special Thanks to Mitsua Contributors

- VRoid is a trademark or registered trademark of Pixiv inc. in Japan and other regions.