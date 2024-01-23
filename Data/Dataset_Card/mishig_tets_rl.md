## Example dataset card on playing video inside dataset cards

<video loop autoplay controls src="https://huggingface.co/araffin/ppo-LunarLander-v2/resolve/main/replay.mp4"></video>

Since datset cards support html, you can just use html video tag:

```html
<video loop autoplay controls src="https://huggingface.co/araffin/ppo-LunarLander-v2/resolve/main/replay.mp4"></video>
```

note: change the src to your video. You can uplaod the demo video as part of your dataset as well & use it like `https://huggingface.co/{DATASET_OWNER}/{DATASET_NAME}/resolve/main/{VIDEO_PATH}.mp4`