# Scene 2 - Quick Implementation Guide

## Critical Fixes (3 changes needed)

### FIX #1: Grid Cell Visibility (Line 152-161)

**BEFORE:**
```python
# Line 152-161 in scene2_problem.py
cell = Rectangle(
    width=cell_width * 0.92,
    height=cell_height * 0.92,
    color="#000000",          # ✗ Black on black = invisible
    stroke_width=0.3,
    fill_opacity=0.2,         # ✗ Too transparent
    stroke_opacity=0.4        # ✗ Too faint
)
```

**AFTER:**
```python
cell = Rectangle(
    width=cell_width * 0.92,
    height=cell_height * 0.92,
    color=COLORS["accent"],   # ✓ Gold (#e8a838)
    stroke_width=0.5,         # ✓ Thicker
    fill_opacity=0.25,        # ✓ More visible
    stroke_opacity=0.6        # ✓ Better contrast
)
```

**Impact:** Grid becomes clearly visible on dark background. Critical for Classification sequence clarity.

---

### FIX #2: Diffusion Dots Color (Line 313-318)

**BEFORE:**
```python
# Line 313-318 in scene2_problem.py
dot = Dot(
    point=[x_random, y_random, 0],
    radius=0.04,              # ✗ Very small
    color="#000000",          # ✗ Black on black
    fill_opacity=0.7
)
```

**AFTER:**
```python
dot = Dot(
    point=[x_random, y_random, 0],
    radius=0.05,              # ✓ Slightly larger
    color=COLORS["accent"],   # ✓ Gold for visibility
    fill_opacity=0.8          # ✓ More opaque
)
```

**Impact:** Animated dots become visible and easier to track during motion sequence.

---

### FIX #3: Retrieval Highlight Duration (Line 517-522)

**BEFORE:**
```python
# Line 517-522 in scene2_problem.py
self.play(
    FadeIn(highlight_circle, run_time=0.1)    # ✗ Too fast at 1080p
)
self.play(
    FadeOut(highlight_circle, run_time=0.08)  # ✗ Too fast
)
```

**AFTER:**
```python
self.play(
    FadeIn(highlight_circle, run_time=0.15)   # ✓ Better visibility
)
self.play(
    FadeOut(highlight_circle, run_time=0.12)  # ✓ Smoother fade
)
```

**Impact:** Highlight effects are more visible and readable at 1080p resolution.

---

## High Priority Fixes (4 optional improvements)

### FIX #4: Method Box Labels Font Size (Line 234)
```python
# Change from 26 to 28
label = create_sans_body(
    method_name,
    font_size=28,    # Was 26
    color=color
)
```

### FIX #5: Divider Title Font Size (Line 201)
```python
# Change from 48 to 50
divider_title = create_sans_body(
    "Three Approaches to Geolocation",
    font_size=50,    # Was 48
    color=COLORS["accent"]
)
```

### FIX #6: Add Wait Time After Grid Fade (Line 166)
```python
# Change from 0.5 to 0.8
self.play(FadeIn(clf_visual, run_time=1.0))
self.wait(0.8)    # Was 0.5 - gives viewers time to register
```

### FIX #7: Progress Dot Color Consistency (Line 63)
```python
# Change from gold_light to accent for consistency with Scene 1
dot = Dot(
    point=[x_pos, 3.2, 0],
    radius=0.07,
    color=COLORS["accent"] if i == 1 else COLORS["text_muted"],  # Was gold_light
    fill_opacity=1.0 if i == 1 else 0.4
)
```

---

## Testing Checklist

After making changes, verify:

- [ ] Grid cells in Classification are clearly visible with distinct gold color
- [ ] Diffusion dots animate smoothly and are easy to see
- [ ] Highlight circles in Retrieval persist long enough to be noticed
- [ ] All font sizes appear balanced and readable on 1920×1080 display
- [ ] Progress dots use consistent accent color throughout video
- [ ] Overall video maintains visual consistency with Scene 1

---

## File Locations

**Main file:** `/Volumes/SSD/iclr-website/manim_video/scenes/scene2_problem.py`
**Config file:** `/Volumes/SSD/iclr-website/manim_video/config.py`
**Color reference:** See COLORS dictionary in config.py

---

## Re-render Command

After making fixes:

```bash
cd /Volumes/SSD/iclr-website/manim_video
manim -pqh scenes/scene2_problem.py Scene2Problem
```

Expected output: `output/videos/scene2_problem/1080p60/Scene2Problem.mp4`
