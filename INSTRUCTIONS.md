# HierLoc Video Project - Instructions for Future Agents

## 🎯 Project Overview

This is a comprehensive video production pipeline for creating an award-winning explainer video for **HierLoc: Hyperbolic Entity Embeddings for Hierarchical Visual Geolocation**.

**Paper**: Gadi et al., ICLR 2025
**Task**: Create a 3-5 minute 3Blue1Brown-style explainer video
**Status**: Active development (Scene rewrites in progress)

---

## 📚 Background: What is HierLoc?

### The Problem
**Visual Geolocation**: Given an image, predict where it was taken (country, region, city)

**Current Challenge**:
- Naive methods require comparing against 5M+ images
- O(N) search complexity = expensive, slow
- Doesn't leverage that geography is inherently hierarchical

### The Solution: HierLoc
Instead of matching images to images, match images to **geographic entities** in **hyperbolic space**:

1. **Encode** images into embeddings
2. **Map** to geographic entities (countries, regions, subregions, cities)
3. **Use hierarchy** for efficient search: Country → Region → City
4. **Hyperbolic geometry** naturally captures hierarchy (exponential volume growth)

### Key Results
- **19.5%** reduction in mean geodesic error
- **+8.8%** country accuracy improvement
- **+43.2%** subregion accuracy improvement
- **95% fewer** embeddings needed (240K vs 5M+)
- **Sub-linear** search complexity

**Key Insight**: Hyperbolic geometry is the right tool for hierarchical data.

---

## 📁 Project Structure

```
/Volumes/SSD/iclr-website/
├── manim_video/                          # Main video project directory
│   ├── scenes/                           # Scene implementation files
│   │   ├── scene1_hook.py               # Opening question & title
│   │   ├── scene2_problem.py            # Why naive methods fail
│   │   ├── scene3_insight.py            # Geographic hierarchy concept
│   │   ├── scene4_solution.py           # HierLoc approach
│   │   └── scene5_results.py            # Results & impact
│   ├── config.py                         # Colors, fonts, configuration
│   ├── utils.py                          # Helper functions
│   ├── render.sh                         # Rendering script
│   ├── output/                           # Rendered videos and temporary files
│   ├── audio/                            # Narration audio files (to be created)
│   └── README.md                         # Project-specific README
│
├── static/
│   ├── images/
│   │   ├── streetview/                   # Street view images for scenes
│   │   │   ├── Paris_00131_*.jpg
│   │   │   ├── Russia_00019_*.jpg
│   │   │   ├── 482314949_*.jpg
│   │   │   └── 0b_5a_*.jpg
│   │   └── [other paper figures]
│   └── paper.pdf                         # Original research paper
│
├── Documentation/
│   ├── INSTRUCTIONS.md                   # THIS FILE - Project background
│   ├── CHANGELOG.md                      # Version history and changes
│   ├── SCENE_SPECIFICATIONS.md           # Detailed scene requirements
│   ├── STYLE_GUIDE.md                    # Design system & guidelines
│   └── NARRATION_SCRIPT.md               # Final narration script
│
└── [ARCHIVE - Old docs to clean up]
    ├── HIERLOC_VIDEO_PLAN.md            # ⚠️ OLD - see SCENE_SPECIFICATIONS.md
    ├── HIERLOC_VIDEO_POSTPRODUCTION.md  # ⚠️ OLD - post-production guide
    ├── hierloc_narration_script.md       # ⚠️ OLD - outdated narration
    └── [other old files]
```

---

## 🎬 Scene Overview & Design Requirements

### Scene 1: Hook (20-24 seconds)
**Purpose**: Pose the central question and grab attention

**Visual Elements**:
- Clean title: "HierLoc" (modern sans serif)
- Subtitle: "Where Are You?"
- Progressive text reveals: "Can you guess?", "Without landmarks?", "How would a computer solve this?"

**Key Points**:
- Minimal, elegant design
- High contrast on dark background (#0a0a0f)
- Gold accents (#e8a838) for emphasis
- NO background pattern/clutter

**Coordinates & Readability**:
- Title: Centered at Y=2.5, font size 96
- Subtitle: Below title at Y=1.8
- Questions: Centered at Y=-2.0, font size 40
- All text uses Helvetica Neue or Inter (modern sans serif)

---

### Scene 2: The Problem (35-40 seconds)
**Purpose**: Show why traditional methods fail at scale

**Visual Elements**:
- Organized grid of dots (12x12) representing images
- Center dot highlighted in gold = test image
- 8 arrows radiating outward = search process
- 3 problem labels: "Slow", "Memory-intensive", "No structure"
- Label: "5M+ images"

**Key Narrative**:
- "Modern methods compare against millions of images"
- "Each comparison is expensive and memory-intensive"
- "The system doesn't understand that geography has structure"

**Coordinates**:
- Dot grid: Centered at [0, 0.5, 0], 12×12 grid with 0.35 spacing
- Test dot: Center [0, 0.5, 0] with radius 0.12
- Arrows: 8 evenly spaced at 45° intervals, length 1.5
- Problem labels: TOP-LEFT, TOP-RIGHT, BOTTOM-CENTER

---

### Scene 3: The Insight (38-42 seconds)
**Purpose**: Reveal that geography is hierarchical + hyperbolic geometry solution

**Visual Elements - Part A (Nesting)**:
- Nested rectangles showing: Paris ⊂ France ⊂ Europe ⊂ Earth
- Clean hierarchy visualization with gold highlighting

**Visual Elements - Part B (Tree)**:
- Tree structure: Earth → 5 continents → countries → regions
- Progressive reveal with connecting lines
- "Exponential branching" label

**Visual Elements - Part C (Problem)**:
- Label: "In Euclidean space: cities get cramped"

**Visual Elements - Part D (Solution)**:
- Poincaré disk (circle with radius 1.2)
- Label: "Hyperbolic space: exponential room"

**Key Insight**: Hyperbolic geometry has exponential volume growth = perfect for hierarchy

---

### Scene 4: The Solution (65-75 seconds)
**Purpose**: Show how HierLoc works step-by-step

**Visual Elements - Image Encoding**:
- Image placeholder (left): Rectangle 1.8×1.4 at [-3.5, 1.0, 0]
- Arrow pointing right
- Embedding vector (center): Rectangle 1.2×1.2 at [-0.4, 1.0, 0]

**Visual Elements - Entity Space**:
- Title: "Entity Space" at [3.0, 2.2, 0]
- Hierarchical dots: 3 at top (countries), 2 below (cities)
- Connecting lines showing hierarchy

**Visual Elements - Matching**:
- Gold arrow: Image → Entity space
- Gold glow around matched entity
- Label: "Match"

**Visual Elements - Metrics**:
- Left column: "Traditional" | "5M+ embeddings" | "O(N) search"
- Right column: "HierLoc" | "240K entities" | "Sub-linear search"
- Highlight: "95% fewer embeddings"

---

### Scene 5: Results (40-45 seconds)
**Purpose**: Show concrete results and celebrate the breakthrough

**Visual Elements - Metrics**:
- Metric 1: "Mean Geodesic Error ↓ 19.5%" (gold color)
- Metric 2: "Country Accuracy +8.8%"
- Metric 3: "City Accuracy +43.2%"

**Visual Elements - Why It Matters**:
- "⚡ Sub-linear search"
- "💾 95% fewer embeddings"
- "🔍 Interpretable paths"

**Visual Elements - Final Message**:
- "Hyperbolic geometry is the right tool for hierarchy"

**Visual Elements - CTA**:
- "Learn more" (call to action)

---

## 🎨 Design System

### Colors (From Website)
```
Background:      #0a0a0f  (ink/dark cosmos)
Primary Accent:  #e8a838  (geodesic gold)
Light Gold:      #f5cc7a  (highlights)
Text Primary:    #e8e4da  (cream/off-white)
Text Muted:      #8c8a84  (secondary text)
Surface:         #14141e  (panels, containers)
```

### Typography
- **Titles**: Helvetica Neue Bold (modern sans serif)
- **Body**: Helvetica Neue (modern sans serif)
- **Emphasis**: Helvetica Neue with gold color
- **Code/Numbers**: Menlo (monospace)

**Font Sizes**:
- Major titles: 64-96
- Scene titles: 56-64
- Body text: 24-40
- Labels: 18-28
- Small text: 14-20

### Animation Principles
- **Easing**: Cubic ease-in-out for smooth, professional feel
- **Duration**: Fast reveals (0.4-0.8s), slower explanations (1.0-2.0s)
- **Pacing**:
  - Hook: Fast and punchy
  - Problem: Slower, let scale sink in
  - Insight: Building excitement
  - Solution: Confident and clear
  - Results: Triumphant and celebratory

---

## 🔧 Technical Setup

### Requirements
- Python 3.8+
- Manim Community Edition v0.19.2+
- FFmpeg (for audio sync and video composition)
- Fonts: Helvetica Neue, Menlo (available on macOS)

### Quick Start
```bash
cd /Volumes/SSD/iclr-website/manim_video

# Render a single scene
./render.sh scene1

# Render all scenes
./render.sh all

# Output videos: output/videos/scene[N]_*/1080p60/Scene[N]*.mp4
```

### Quality Settings
- **Low**: 480p, 15fps (testing)
- **Medium**: 720p, 30fps (preview)
- **High (default)**: 1080p, 60fps (production)

---

## ✍️ Narration Guidelines

### Recording Requirements
- Sample rate: 48 kHz
- Bit depth: 24-bit
- Format: WAV (lossless)
- Peak levels: -6dB to -3dB (headroom)
- Noise floor: Essentially silent

### Tone & Pacing
- **Scene 1-2**: Curious, building tension ("Let's think about something fascinating...")
- **Scene 3**: Excited, "aha moment" ("But wait, there's elegance here...")
- **Scene 4**: Confident, satisfied ("Here's the elegant solution...")
- **Scene 5**: Triumphant, visionary ("This shows something bigger...")

### Coordinate Timing
Each scene has specific animation timings - narration must sync with:
- Scene 1: ~24s total (title 1s, questions ~3s each)
- Scene 2: ~36s total (grid appears, arrows fan, labels)
- Scene 3: ~39s total (nesting 2s, tree 1.5s, conclusion)
- Scene 4: ~70s total (image 2s, entity space 2s, matching 1s, metrics 2s)
- Scene 5: ~45s total (metrics 1.5s, advantages 1.5s, conclusion 2s)

---

## 📋 Checklist for Future Modifications

### Before Making Changes
- [ ] Read this entire INSTRUCTIONS.md
- [ ] Review SCENE_SPECIFICATIONS.md for detailed requirements
- [ ] Check STYLE_GUIDE.md for design constraints
- [ ] Review latest CHANGELOG.md to understand history

### When Modifying Scenes
- [ ] **Coordinates**: Always plan coordinates carefully (scene is 8 units wide, 4.5 tall)
- [ ] **Readability**: Test text on dark background at actual size
- [ ] **Alignment**: All elements should align intentionally
- [ ] **Color**: Use only colors from COLORS dict
- [ ] **Fonts**: Use only Helvetica Neue (sans), Menlo (mono)
- [ ] **Animations**: Use smooth easing, appropriate durations
- [ ] **Geometry**: Every shape should have purpose

### After Making Changes
- [ ] Run `./render.sh scene[N]` to test
- [ ] Check video for readability issues
- [ ] Verify colors match design system
- [ ] Update CHANGELOG.md with changes
- [ ] Commit with clear message referencing CHANGELOG.md

---

## 🚨 Common Pitfalls to Avoid

### ❌ Readability Issues
- Text too small on dark background
- Text overlapping with animations
- Color contrast too low (use #e8e4da for primary text)

### ❌ Geometry Issues
- Elements misaligned or off-center
- Proportions wrong (squares look like rectangles)
- Spacing inconsistent
- Random positioning (everything should align to grid)

### ❌ Animation Issues
- Animations too fast (viewers can't follow)
- Abrupt cuts instead of smooth transitions
- Objects teleporting instead of moving smoothly

### ❌ Font Issues
- Using DM fonts (old design)
- Mixed fonts in same scene
- Inconsistent sizing

### ❌ Narrative Issues
- Not following the paper's actual methodology
- Oversimplifying to point of inaccuracy
- Missing key insights (hyperbolic geometry, hierarchical search)

---

## 📞 Key Files Reference

| File | Purpose |
|------|---------|
| `config.py` | Colors, fonts, rendering config |
| `utils.py` | Helper functions for text, colors |
| `render.sh` | Build script - DO NOT MODIFY WITHOUT REASON |
| `CHANGELOG.md` | Track all modifications |
| `SCENE_SPECIFICATIONS.md` | Detailed scene requirements |
| `STYLE_GUIDE.md` | Design system constraints |
| `paper.pdf` | Original research (READ THIS) |

---

## 🎓 Learning Resources

**Understanding HierLoc**:
- Read: `/Volumes/SSD/iclr-website/paper.pdf` (pages 1-5 minimum)
- Key concepts: Hyperbolic geometry, hierarchical entities, contrastive learning

**Understanding Manim**:
- Documentation: https://docs.manim.community/
- Key classes: Scene, Mobject, Text, Rectangle, Circle, Arrow, VGroup
- This project uses **Manim Community Edition** (not ManimGL)

**3Blue1Brown Style**:
- Progressive revelation: Show problem → solution → impact
- Visual metaphors: Make abstract concepts visual
- Smooth easing: Never jarring animations
- Color as meaning: Use gold for key insights

---

## 🔄 Update Process

When updating this file or creating new documentation:

1. Make changes to appropriate `.md` file
2. Update CHANGELOG.md with date and summary
3. Commit with message: "docs: [description]"
4. Run `./render.sh all` to verify no breaks
5. Test on different screen sizes/devices

---

**Last Updated**: February 20, 2026
**Status**: Active Development
**Next Phase**: Award-winning script rewrite + modern fonts

