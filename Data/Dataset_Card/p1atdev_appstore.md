---
license: cc0-1.0
---

# AppStore Rankings Dataset

This is a dataset of AppStore rankings, JP and US, each containing 176 json files of ranking chart information including paid and free.


```
2023-01-30
   ├─jp
   | └─... 176 files
   └─us
     ├─Action - Top Free Games.json
     ├─Action - Top Paid Games.json
     ├─Adventure - Top Free Games
     ... 176 files
     └─Word - Top Paid Games.json
```

Example of json file:

```json
{
   "chart": "Action",
   "section": "Top Free Games",
   "apps": [
      {
         "chart": "Action",
         "section": "Top Free Games",
         "rank": "1",
         "id": "431946152",
         "name": "Roblox",
         "dev": "Roblox Corporation",
         "url": "https://apps.apple.com/us/app/roblox/id431946152",
         "icon": {
            "image/png": {
               "320w": "https://is5-ssl.mzstatic.com/image/thumb/Purple113/v4/65/6d/d3/656dd35b-2896-0a9f-043a-b1be8501f7f8/AppIcon-1x_U007emarketing-0-7-0-0-85-220.png/320x0w.png",
               "157w": "https://is5-ssl.mzstatic.com/image/thumb/Purple113/v4/65/6d/d3/656dd35b-2896-0a9f-043a-b1be8501f7f8/AppIcon-1x_U007emarketing-0-7-0-0-85-220.png/157x0w.png",
               "146w": "https://is5-ssl.mzstatic.com/image/thumb/Purple113/v4/65/6d/d3/656dd35b-2896-0a9f-043a-b1be8501f7f8/AppIcon-1x_U007emarketing-0-7-0-0-85-220.png/146x0w.png",
               "640w": "https://is5-ssl.mzstatic.com/image/thumb/Purple113/v4/65/6d/d3/656dd35b-2896-0a9f-043a-b1be8501f7f8/AppIcon-1x_U007emarketing-0-7-0-0-85-220.png/640x0w.png",
               "314w": "https://is5-ssl.mzstatic.com/image/thumb/Purple113/v4/65/6d/d3/656dd35b-2896-0a9f-043a-b1be8501f7f8/AppIcon-1x_U007emarketing-0-7-0-0-85-220.png/314x0w.png",
               "292w": "https://is5-ssl.mzstatic.com/image/thumb/Purple113/v4/65/6d/d3/656dd35b-2896-0a9f-043a-b1be8501f7f8/AppIcon-1x_U007emarketing-0-7-0-0-85-220.png/292x0w.png"
            },
            "image/webp": {
               "320w": "https://is5-ssl.mzstatic.com/image/thumb/Purple113/v4/65/6d/d3/656dd35b-2896-0a9f-043a-b1be8501f7f8/AppIcon-1x_U007emarketing-0-7-0-0-85-220.png/320x0w.webp",
               "157w": "https://is5-ssl.mzstatic.com/image/thumb/Purple113/v4/65/6d/d3/656dd35b-2896-0a9f-043a-b1be8501f7f8/AppIcon-1x_U007emarketing-0-7-0-0-85-220.png/157x0w.webp",
               "146w": "https://is5-ssl.mzstatic.com/image/thumb/Purple113/v4/65/6d/d3/656dd35b-2896-0a9f-043a-b1be8501f7f8/AppIcon-1x_U007emarketing-0-7-0-0-85-220.png/146x0w.webp",
               "640w": "https://is5-ssl.mzstatic.com/image/thumb/Purple113/v4/65/6d/d3/656dd35b-2896-0a9f-043a-b1be8501f7f8/AppIcon-1x_U007emarketing-0-7-0-0-85-220.png/640x0w.webp",
               "314w": "https://is5-ssl.mzstatic.com/image/thumb/Purple113/v4/65/6d/d3/656dd35b-2896-0a9f-043a-b1be8501f7f8/AppIcon-1x_U007emarketing-0-7-0-0-85-220.png/314x0w.webp",
               "292w": "https://is5-ssl.mzstatic.com/image/thumb/Purple113/v4/65/6d/d3/656dd35b-2896-0a9f-043a-b1be8501f7f8/AppIcon-1x_U007emarketing-0-7-0-0-85-220.png/292x0w.webp"
            }
         }
      },
      ...
}
```