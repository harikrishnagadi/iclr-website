# HierLoc Use Cases - Integration Plan

**Date**: February 20, 2026
**Status**: Ready for Implementation
**Scope**: Add comprehensive use cases section to video

---

## 📋 Overview

This document outlines how to integrate real-world use cases into the HierLoc explainer video, demonstrating practical applications and impact.

---

## 🎬 Two Implementation Options

### **Option 1: Dedicated Scene 6 (Recommended)**
**Create a new Scene 6 focused entirely on use cases**
- Duration: ~45-60 seconds
- Visual: Gallery of images + text overlays
- Narration: Explain top 3-5 use cases with examples
- Format: Matching style of existing 5 scenes

**Advantages**:
✅ Complete coverage of all use cases
✅ Professional presentation
✅ Matches video style consistency
✅ Can be extended easily

### **Option 2: Integrated into Scene 5**
**Add use cases to end of Scene 5 (Results)**
- Duration: +30-40 seconds to Scene 5
- Visual: Brief use case examples
- Narration: Quick overview of applications
- Format: Quick montage style

**Advantages**:
✅ Faster to produce
✅ Shorter overall video
✅ Natural conclusion to the video

---

## 📊 Recommended Use Cases (Top 5 for Video)

### **For ~45 second Scene 6:**

1. **Emergency Response** (8 seconds)
   - Hook: "First responders need answers fast"
   - Visual: Disaster scene photo
   - Impact: Saves lives through rapid location identification

2. **News & Journalism** (8 seconds)
   - Hook: "Fighting misinformation at scale"
   - Visual: Journalist/breaking news photo
   - Impact: Verify breaking news location automatically

3. **Wildlife Conservation** (8 seconds)
   - Hook: "Monitor endangered species without manual effort"
   - Visual: Wildlife/forest camera trap photo
   - Impact: Automated ecosystem monitoring

4. **Urban Planning** (8 seconds)
   - Hook: "Map cities comprehensively"
   - Visual: Urban street/city planning photo
   - Impact: Better infrastructure decisions

5. **Climate & Environment** (9 seconds)
   - Hook: "Track environmental changes globally"
   - Visual: Forest/environmental damage photo
   - Impact: Real-time climate monitoring

**Plus closing statement** (4 seconds):
"These are just the beginning. HierLoc makes visual understanding practical at planetary scale."

---

## 🎨 Scene 6 Structure (Recommended Implementation)

### **Format: Image Gallery with Text Overlays**

```
Timeline:
[0:00-0:02] Title: "Real-World Impact"
[0:02-0:10] Emergency Response case
[0:10-0:18] News & Journalism case
[0:18-0:26] Wildlife Conservation case
[0:26-0:34] Urban Planning case
[0:34-0:43] Climate & Environment case
[0:43-0:45] Closing statement
```

### **Visual Style**
- Stack images horizontally or in a grid
- Fade in/out transitions (1 second each)
- Text overlay with case name and impact
- Use accent color (#e8a838) for text
- Maintain consistency with existing scenes

### **Narration Timing**
- 8-10 seconds per use case
- 100-130 words per use case
- Clear, conversational tone
- Emphasize the problem + HierLoc solution

---

## 📥 Media Gathering Steps

### **Phase 1: Prepare Directories**
```bash
mkdir -p /Volumes/SSD/iclr-website/static/images/usecases/{emergency_response,news_journalism,wildlife_conservation,urban_planning,climate_environment}
```

### **Phase 2: Download Images**
Use the media gathering guide to download 3-4 representative images per use case from:
- Unsplash.com (primary)
- Pexels.com (secondary)
- Pixabay.com (tertiary)

**Search terms by use case**:
- Emergency: "flood damage", "disaster relief", "rescue"
- News: "journalist", "breaking news", "camera"
- Wildlife: "wildlife camera trap", "forest conservation", "endangered species"
- Urban: "city streets", "urban planning", "infrastructure"
- Climate: "forest fire", "environmental damage", "deforestation"

### **Phase 3: Optimize Images**
- Resize to 1920x1080
- Compress to <500KB each
- Verify quality (no blur, clear subject)

### **Phase 4: Create Attribution Document**
Document all sources in `MEDIA_ATTRIBUTIONS.md` with:
- Image filename
- Photographer/creator name
- Source website
- License type (CC0, CC BY, etc.)

---

## 🎬 Creating Scene 6 (Technical Steps)

### **Step 1: Create Scene File**
Create `/Volumes/SSD/iclr-website/manim_video/scenes/scene6_usecases.py`

### **Step 2: Implementation Template**
```python
from manim import *
from config import COLORS, FONTS, setup_manim_config
from layout import ObjectPositioner

setup_manim_config(quality="high_quality")

class Scene6UseCases(Scene):
    def construct(self):
        self.camera.background_color = COLORS["bg"]

        # Header and progress dots
        # (Copy from other scenes, update to dot 6)

        # Title
        title = Text("Real-World Impact",
                    font=FONTS["sans"],
                    font_size=48,
                    color=COLORS["accent"])

        # Load and position use case images
        # Create image gallery layout
        # Add text overlays
        # Add narration sync points
```

### **Step 3: Image Positioning Strategy**
**Option A: Grid Layout** (3×2)
```
[Emergency]    [News]         [Wildlife]
[Urban]        [Climate]      [Closing]
```

**Option B: Horizontal Stack** (Sequential)
```
[Emergency] → [News] → [Wildlife] → [Urban] → [Climate] → [Closing]
```

**Option C: Carousel** (One at a time, fade in/out)
```
[Image fades in] → [Text overlay] → [Fade out] → [Next image]
```

Recommendation: **Option C (Carousel)** - Matches existing scene style

---

## 📝 Narration Script Template

Each use case follows this structure:
```
Hook (1 sentence - problem intro)
"[Hook about the challenge]"

Explanation (2-3 sentences - why it matters)
"[Explain the scale and importance]"

HierLoc Solution (1 sentence - how it helps)
"[With HierLoc, we can...]"
```

**Example - Emergency Response**:
```
"When disaster strikes, first responders have minutes to act.
A photo from the scene—but where is it? In the old world,
finding the location could take hours. With HierLoc,
seconds. That's lives saved."
```

---

## 🎤 Recording Narration for Scene 6

Use the existing AUDIO_RECORDING_GUIDE.md specifications:
- Sample Rate: 48 kHz
- Bit Depth: 24-bit
- Format: WAV (lossless)
- Peak levels: -3dB to -6dB

Duration: ~45 seconds of narration

---

## 🚀 Implementation Timeline

| Phase | Task | Duration | Status |
|-------|------|----------|--------|
| **Phase 1** | Gather media from Unsplash/Pexels/Pixabay | 1-2 hours | 📋 Ready |
| **Phase 2** | Optimize and organize images | 30 minutes | 📋 Ready |
| **Phase 3** | Write Scene 6 code (Manim) | 1-2 hours | 📋 Planning |
| **Phase 4** | Record narration (45 seconds) | 30 minutes | 📋 Ready |
| **Phase 5** | Test and refine Scene 6 render | 1 hour | 📋 Planning |
| **Phase 6** | Render final Scene 6 video | 15-20 minutes | 📋 Planning |

**Total Timeline**: ~6-8 hours

---

## ✅ Completion Checklist

**Media Gathering**
- [ ] Create use cases directories
- [ ] Download 3-4 images per use case (15-20 total)
- [ ] Resize to 1920x1080
- [ ] Compress images (<500KB each)
- [ ] Create MEDIA_ATTRIBUTIONS.md

**Scene Development**
- [ ] Write Scene 6 Manim code
- [ ] Implement image gallery layout
- [ ] Add text overlays
- [ ] Set up narration sync points
- [ ] Test rendering locally

**Narration**
- [ ] Write narration script (500-600 words)
- [ ] Record audio (45 seconds)
- [ ] Trim and normalize audio
- [ ] Save as WAV format (48kHz, 24-bit)

**Final Assembly**
- [ ] Render Scene 6 final video
- [ ] Verify all sync points
- [ ] Test full 6-scene sequence
- [ ] Create final master video with audio

---

## 📞 Related Documents

- `HIERLOC_USECASES.md` - Detailed use cases and impact
- `MEDIA_GATHERING_GUIDE.md` - Guide for downloading media
- `AUDIO_RECORDING_GUIDE.md` - Audio recording specifications
- `LAYOUT_SYSTEM_GUIDE.md` - Text positioning system
- `SCENE_SPECIFICATIONS.md` - Visual style guidelines

---

## 🎯 Key Objectives

By adding this section, the video will:
✅ Demonstrate real-world relevance
✅ Show practical impact beyond academic interest
✅ Connect research to society
✅ Make the problem relatable and urgent
✅ Provide concrete examples viewers understand

This transforms the video from "here's a cool technique" to "here's why it matters."

