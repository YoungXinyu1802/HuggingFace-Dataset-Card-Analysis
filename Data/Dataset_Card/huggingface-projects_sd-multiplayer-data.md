To access an image use the following 

Bucket URL: https://d26smi9133w0oo.cloudfront.net/

example:

https://d26smi9133w0oo.cloudfront.net/room-7/1670520485-CZk4C72xBr5wPfTpwDAnG6-7648_7008-a-chicken-breaking-through-a-mirrornnotn.webp

**Bucket URL/key**


SQLite
https://huggingface.co/datasets/huggingface-projects/sd-multiplayer-data/blob/main/rooms_data.db

```bash
sqlite> PRAGMA table_info(rooms_data);
0|id|INTEGER|1||1
1|room_id|TEXT|1||0
2|uuid|TEXT|1||0
3|x|INTEGER|1||0
4|y|INTEGER|1||0
5|prompt|TEXT|1||0
6|time|DATETIME|1||0
7|key|TEXT|1||0

$: sqlite3 rooms_data.db

SELECT * FROM rooms_data WHERE room_id = 'room-40';


```

JSON example
https://huggingface.co/datasets/huggingface-projects/sd-multiplayer-data/blob/main/room-39.json

```json
[
  {
    "id": 160103269,
    "room_id": "room-7",
    "uuid": "CZk4C72xBr5wPfTpwDAnG6",
    "x": 7648,
    "y": 7008,
    "prompt": "7648_7008 a chicken breaking through a mirrornnotn webp",
    "time": "2022-12-08T17:28:06+00:00",
    "key": "room-7/1670520485-CZk4C72xBr5wPfTpwDAnG6-7648_7008-a-chicken-breaking-through-a-mirrornnotn.webp"
  }
]

