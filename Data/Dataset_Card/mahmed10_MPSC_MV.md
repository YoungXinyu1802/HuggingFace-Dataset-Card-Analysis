---
task_categories:
- video-classification
tags:
- Video Acitvity Recognition
---
<h1 style="text-align: center;">MPSC Multi-view Dataset</h1>
<p style='text-align: justify;'> 
  Deep video representation learning has recently attained state-of-the-art performance in video action recognition. However, when used with video clips from varied perspectives, the performance of these models degrades significantly. Existing VAR models frequently simultaneously contain both view information and action attributes, making it difficult to learn a view-invariant representation. Therefore, to study the attribute of multiview representation, we collected a large-scale time synchronous multiview video dataset from 10 subjects in both indoor and outdoor settings performing 10 different actions with three horizontal and vertical viewpoints using a smartphone, an action camera, and a drone camera. We provide the multiview video dataset with various meta-data information to facilitate further research for robust VAR systems.
</p>

### Collecting multiview videos

<p style='text-align: justify;'> 
  In our data collection strategy, we choose regular sensors (smartphone camera), wide-angle sensors (go-pro, action camera), and drone cameras covering front views, side views, and top view positions to receive simultaneous three 2D projections of ten action events. To collect multi-angular and positional projections of the same actions, smartphones (Samsung S8 plus, flat-angle sensor), action cameras (Dragon touch EK700, wide-angle sensor), and a drone (Parrot Anafi, flat-angle sensor) capture the action events simultaneously from different positions in 1080p at 30 FPS. Among the cameras, the smartphone was hand-held and tracked the events. The action camera was placed in a stationary position and captured the events using its wide-view sensor. Both of them were positions approximately 6 feet away from the participants to capture two completely different side-views of the actions from horizontal position. Lastly, the drone captures the events' top view while flying at a low altitude of varying distances from 8 feet to 15 feet. Although we positioned the cameras to capture events from a particular angular position with some occasional movement, it effectively captured an almost complete-view of actions, as the volunteers turn in different directions to perform different actions without any constraints.
</p>

<p style='text-align: justify;'>
  We have selected ten regular micro-actions in our dataset with both static (poses: sitting, standing, lying with face up, lying with face down) and dynamic actions (temporal patterns: walking, push up, waving hand, leg exercise, object carrying, object pick/drop). We hypothesize this would further foundation for complex action recognition since some complex actions require sequentially performing a subset of these micro-actions. In our target actions selection, some actions have only minor differences to distinguish and require contextual knowledge (walking and object carrying, push-ups and lying down, lying with face down and lying with face up, standing and hand waving in standing position). Further, we have collected the background-only data without the human to provide a no-action/human dataset for the identical backgrounds.
</p>

<p style='text-align: justify;'>
  We collect these data [sampled shown in the follwing figure] from 12 volunteer participants with varying traits. The participant performs all ten actions for 30 seconds while being recorded from three-positional cameras simultaneously in each session. The participants provided data multiple times, under different environments with different clothing amassing 30 sessions, yielding approximately ten hours of total video data in a time-controlled and safe setup. 
</p>


![plot](./fig/dataset.png)

<p style='text-align: justify;'>
  Further, the videos are collected under varying realistic lighting conditions; natural lighting, artificial lighting, and a mix of both indoors, and outdoor environments, and multiple realistic backgrounds like walls, doors, windows, grasses, roads, and reflective tiles with varying camera settings like zoom, brightness and contrast filter, relative motions. Environments and lighting conditions are presented in the above figure. We also provide the videos containing only background to avail further research.
</p>

### Data Preprocessing and AI readiness
<p style='text-align: justify;'>
  We align each session's simultaneously recorded videos from the starting time-stamp, and at any given time, all three sensors of any particular session capture their corresponding positional projection of the same event. The alignment allows us to annotate one video file per session for the underlying action in the time duration and receive action annotation for the other two videos, significantly reducing the annotation burden for these multiview videos.
</p>

<p style='text-align: justify;'>
  Besides action information, each video is also tagged with the following meta-information: the subjects' ID, backgrounds environments, lighting conditions, camera specifications, settings (varying zoom, brightness), camera-subject distances, and relative movements, for various research directions. Additionally, other information such as the date, time, and the trial number were also listed for each video. Multiple human volunteers manually annotated video files, and these annotations went through multiple cross-checking. Finally, we prepare the video data in pickle file format for quick loading using python/C++/Matlab libraries.
</p>

### Dataset Statistics

Here we provide the our collected dataset characteristics insight.

<p style='text-align: justify;'>
  <strong> 1) Inter and Intra action variations:</strong> We ensure fine-grain inter and intra-action variation in our dataset by requesting the participants to perform similar actions in freestyle. Further, we take multiple sessions on different dates and times to incorporate inter-personal variation in the dataset. 80% of our participants provided data in multiple sessions. 58% of the participant provides their data from multiple backgrounds. We have 20% of female participants in for multiple sessions. In actions, we have 40% stable pose as action and 60% dynamic simple actions in our collected dataset. Further, 10% of our volunteers are athletes. Moreover, our dataset are relatively balanced with almost equal duration of each actions.
</p>

![plot](./fig/actionvar.png)

<p style='text-align: justify;'>
  <strong> 2) Background Variations:</strong> We considered different realistic backgrounds for our data collection while ensuring safety for the participants. We have 75% data for the indoor laboratory environment. Among that, we have 60% of data with white wall background with regular inventories like computers, bookshelves, doors, and windows, 25% with reflective tiles, sunny windows, and 5% under a messy laboratory background with multiple office tables and carpets. Among the 25% outdoor data, we collected 50% of the outdoor data in green fields and concrete parking spaces. We have about 60% of the data in the artificial lighting, and the rest are in natural sunlight conditions. We also provide the backgrounds without the subjects from the three sensors' viewpoints for reference. 
</p>

![plot](./fig/tdist.png)

<p style='text-align: justify;'>
  <strong>3) Viewpoint and sensor Variations:</strong> We have collected 67% data from the horizontal view and 33% from the top-angular positional viewpoints. Our 67% data are captured by the flat lens from a angular viewpoint, and 33% are captured via the wide angular view from the horizontal position. 40% data are recorded from the stable camera position, and 60% data are captured via moving camera sensors. We have 20% data from the subject-focused zoomed camera lens. Further, the subjects perform the actions while facing away from the sensors 20% of the time.  
</p>

### Acknowledgement
<p style='text-align: justify;'>
  We acknowledge the support of DEVCOM Army Research Laboratory (ARL) and U.S. Army Grant No. W911NF21-20076. 
</p>