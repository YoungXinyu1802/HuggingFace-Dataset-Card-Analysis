---
license: mit
language:
- en
---

# hand.json

3,000 image data about "Hand" retrieved from Unsplash.

# portrait.json

10,000 image data about "Portrait" retrieved from Unsplash.

# pose.json

10,000 image data about "Pose" retrieved from Unsplash.

# Tool

- [unsplash-wizard](https://github.com/p1atdev/unsplash-wizard)

```typescript
deno task build
./unsplash download ./hand.json -o ./hand --color --relatedTags --likes 50
```

# Type Definition

```typescript
interface Photo {
  id: string
  color: string
  description: string | null
  alt_description: string | null
  tags: string[]
  likes: number
  urls: {
    raw: string
    full: string
    regular: string
    small: string
    thumb: string
    small_s3: string
  }
  width: number
  height: number
  related_tags: string[]
  location: {
      name: string | null
      city: string | null
      country: string | null
      position: {
          latitude: number | null
          longitude: number | null
      }
  }
  exif: {
      make: string | null
      model: string | null
      exposure_time: string | null
      aperture: string | null
      focal_length: string | null
      iso: number | null
  }
  views: number
  downloads: number
}
```