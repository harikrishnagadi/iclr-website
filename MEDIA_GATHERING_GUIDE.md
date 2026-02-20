# Media Assets Gathering Guide

**Date**: February 20, 2026
**Purpose**: Guide for downloading and organizing media for HierLoc use case demonstrations

---

## 📥 Media Sources & Licenses

### **Safe Sources (Royalty-Free/Open License)**

#### **Stock Photo Sites**
1. **Unsplash** (CC0 - Public Domain)
   - URL: https://unsplash.com
   - Best for: Street scenes, urban, nature, disasters
   - License: Free for commercial use
   - **Relevant searches**:
     - "street view"
     - "disaster relief"
     - "wildlife camera"
     - "urban planning"
     - "historical buildings"

2. **Pexels** (CC0)
   - URL: https://pexels.com
   - Best for: General purpose, high quality
   - License: Free for commercial use
   - **Relevant searches**:
     - "emergency response"
     - "journalist"
     - "mapping"
     - "conservation"

3. **Pixabay** (CC0)
   - URL: https://pixabay.com
   - Best for: Diverse content
   - License: Free for commercial use
   - **Relevant searches**:
     - "flood damage"
     - "forest fire"
     - "city streets"
     - "insurance"

#### **Creative Commons Licensed**
- **Flickr** (CC BY 2.0 / 3.0): https://www.flickr.com/search/
- **Wikimedia Commons**: https://commons.wikimedia.org/
- **NOAA Image Library** (Public Domain): https://www.noaa.gov/media-library

#### **Documentary/News Footage**
- **BBC Learning Zone**: https://www.bbc.co.uk/bitesize
- **Archive.org (Prelinger Archives)**: https://archive.org/
- **Getty Images Editorial** (Limited free use): https://www.gettyimages.com/

---

## 🎬 Media Needed by Use Case

### **1. Emergency Response & Disaster Management**
**Media Type**: Disaster scene photos, first responder actions
**Download Keywords**:
- "flood damage" site:unsplash.com
- "earthquake aftermath" site:pexels.com
- "rescue operation" site:pixabay.com
**Files Needed**: 2-3 representative images
**Format**: JPG/PNG (1920x1080 or higher)

### **2. News & Journalism**
**Media Type**: News cameras, journalists, breaking news scenes
**Download Keywords**:
- "journalist reporting" site:unsplash.com
- "news camera" site:pexels.com
- "breaking news" site:pixabay.com
**Files Needed**: 2-3 images
**Format**: JPG/PNG

### **3. Wildlife Conservation**
**Media Type**: Wildlife camera traps, forest/nature scenes
**Download Keywords**:
- "wildlife" site:unsplash.com
- "forest conservation" site:pexels.com
- "camera trap" site:wikimedia.org
**Files Needed**: 2-3 images
**Format**: JPG/PNG

### **4. Urban Planning**
**Media Type**: City streets, infrastructure, urban development
**Download Keywords**:
- "city streets" site:unsplash.com
- "urban planning" site:pexels.com
- "infrastructure" site:pixabay.com
**Files Needed**: 2-3 images
**Format**: JPG/PNG

### **5. Historical Research**
**Media Type**: Old buildings, historical locations
**Download Keywords**:
- "historical buildings" site:unsplash.com
- "heritage sites" site:wikimedia.org
- "vintage locations" site:pexels.com
**Files Needed**: 2-3 images
**Format**: JPG/PNG

### **6. Tourism & Travel**
**Media Type**: Scenic locations, tourist destinations
**Download Keywords**:
- "travel destination" site:unsplash.com
- "scenic location" site:pexels.com
- "famous landmark" site:pixabay.com
**Files Needed**: 2-3 images
**Format**: JPG/PNG

### **7. Insurance & Verification**
**Media Type**: Damage assessment, property photos
**Download Keywords**:
- "property damage" site:unsplash.com
- "insurance assessment" site:pexels.com
- "damage verification" site:pixabay.com
**Files Needed**: 2-3 images
**Format**: JPG/PNG

### **8. Agriculture**
**Media Type**: Farm fields, crop monitoring, land use
**Download Keywords**:
- "agriculture field" site:unsplash.com
- "farm land" site:pexels.com
- "crop monitoring" site:pixabay.com
**Files Needed**: 2-3 images
**Format**: JPG/PNG

### **9. Social Media**
**Media Type**: Instagram-style photos, user-generated content
**Download Keywords**:
- "social media photo" site:unsplash.com
- "user content" site:pexels.com
- "community sharing" site:pixabay.com
**Files Needed**: 2-3 images
**Format**: JPG/PNG

### **10. Security & Law Enforcement**
**Media Type**: Crime scenes (non-graphic), evidence, investigations
**Download Keywords**:
- "police investigation" site:unsplash.com
- "evidence" site:pexels.com
- "security" site:pixabay.com
**Files Needed**: 2-3 images
**Format**: JPG/PNG

---

## 📋 Download Workflow

### **Step 1: Search and Select**
```bash
# Recommended: Use Firefox/Chrome to search these sites
# Search term example: "flood damage" + site:unsplash.com
# Select images that clearly show the use case
# Download at highest quality available
```

### **Step 2: Organize Files**
```
/Volumes/SSD/iclr-website/static/images/usecases/
├── emergency_response/
│   ├── disaster_1.jpg
│   ├── disaster_2.jpg
│   └── rescue.jpg
├── news_journalism/
│   ├── journalist_1.jpg
│   ├── journalist_2.jpg
│   └── camera.jpg
├── wildlife_conservation/
│   ├── forest.jpg
│   ├── wildlife.jpg
│   └── habitat.jpg
├── urban_planning/
├── historical_research/
├── tourism/
├── insurance/
├── agriculture/
├── social_media/
└── security/
```

### **Step 3: Optimize Images**
```bash
# Using ImageMagick (install if needed: brew install imagemagick)
convert input.jpg -resize 1920x1080 -quality 85 output.jpg

# Or use ffmpeg
ffmpeg -i input.jpg -vf scale=1920:1080 output.jpg
```

### **Step 4: Create Attribution File**
Create `MEDIA_ATTRIBUTIONS.md` with source and license info:
```markdown
# Media Attributions

## Emergency Response Images
- disaster_1.jpg: Photo by [Author] on Unsplash (CC0)
- disaster_2.jpg: Photo by [Author] on Pexels (CC0)
- rescue.jpg: Photo by [Author] on Pixabay (CC0)

[Continue for all images...]
```

---

## ⚖️ License Compliance

### **Important Guidelines**
1. **Always download from reputable sources**
   - Unsplash, Pexels, Pixabay are safe
   - Check license before downloading
   - Keep attribution files

2. **Document sources**
   - Save original filename
   - Record photographer name
   - Store URL or download source

3. **For commercial use**
   - Use CC0 (public domain) when possible
   - Use CC BY (with attribution) if needed
   - Avoid CC BY-SA (viral license)
   - Avoid restricted commercial licenses

4. **Create CREDITS section**
   - List all images used
   - Include photographer names
   - Include license type
   - Add to video description

---

## 🎯 Quick Download Script

```bash
#!/bin/bash
# Quick download of example images from Unsplash API

# Set up directories
mkdir -p /Volumes/SSD/iclr-website/static/images/usecases/{emergency_response,news_journalism,wildlife_conservation,urban_planning,historical_research,tourism,insurance,agriculture,social_media,security}

# Note: Unsplash API requires registration, but allows direct downloads
# For now, recommend manual download from unsplash.com with keywords:
echo "Use these search terms on unsplash.com:"
echo "emergency response → download to ./emergency_response/"
echo "journalism → download to ./news_journalism/"
echo "wildlife → download to ./wildlife_conservation/"
echo "city streets → download to ./urban_planning/"
echo "historical buildings → download to ./historical_research/"
echo "travel destination → download to ./tourism/"
echo "damage assessment → download to ./insurance/"
echo "agriculture field → download to ./agriculture/"
echo "social media → download to ./social_media/"
echo "police investigation → download to ./security/"
```

---

## ✅ Validation Checklist

- [ ] All images are CC0 or properly licensed
- [ ] Image dimensions are 1920x1080 or higher
- [ ] File sizes are optimized (< 500KB each)
- [ ] All sources documented in MEDIA_ATTRIBUTIONS.md
- [ ] Folder structure organized by use case
- [ ] Image quality verified (no blur, clear subject)
- [ ] Relevant to use case (not generic stock photos)

---

## 📝 Notes

- **Total images needed**: ~30 (3 per use case × 10 use cases)
- **Estimated storage**: ~15-20MB
- **Time to gather**: ~1-2 hours
- **Recommended approach**: Download manually while watching use case descriptions

