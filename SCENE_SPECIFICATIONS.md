# HierLoc Video - Scene Specifications

**Version**: 0.3.0 (Award-winning redesign)
**Last Updated**: February 20, 2026
**Status**: Rendering in progress

Complete pixel-perfect specifications for each scene, including coordinates, timing, and technical requirements.

---

## Scene 1: HOOK - Visual Geolocation Challenge

**Duration**: ~24 seconds
**Purpose**: Pose the central mystery

### Visual Specification

| Element | Type | Position | Size | Color | Notes |
|---------|------|----------|------|-------|-------|
| Title | Text | [0, 3.0, 0] | 100pt | #e8e4da | "HierLoc" - Futura |
| Title Accent | Text | [0, 3.0, 0] | 100pt | #e8a838 | Last 3 chars "Loc" |
| Subtitle | Text | Below title | 42pt | #8c8a84 | "Visual Geolocation" |
| Image 1 | ImageMobject | [0, 0.5, 0] | Height 3.0 | N/A | Street view photo |
| Q1 Text | Text | [0, -2.5, 0] | 32pt | #e8e4da | Multi-line |
| Image 2 | ImageMobject | [0, 0.5, 0] | Height 3.0 | N/A | Different location |
| Q2 Text | Text | [0, -2.5, 0] | 32pt | #e8e4da | Multi-line |
| Challenge Line 1 | Text | [0, -2.5, 0] | 40pt | #e8e4da | "How would a" |
| Challenge Line 2 | Text | [0, -2.7, 0] | 40pt | #e8a838 | "computer" |
| Challenge Line 3 | Text | [0, -2.9, 0] | 40pt | #e8e4da | "solve this?" |

### Timing Breakdown
- 0-1.0s: Title fade in
- 1.0-2.5s: Subtitle appears
- 2.5-6.0s: Image 1 + Question 1
- 6.0-9.5s: Image 2 + Question 2
- 9.5-15.0s: Challenge question sequence
- 15.0-24.0s: Fade out transition

### Key Requirements
- ✅ Images must be accessible from `/static/images/streetview/`
- ✅ Text centered for symmetry
- ✅ Gold accent only on "Loc" in title
- ✅ Smooth fade transitions between images
- ✅ 3-line challenge question with careful line breaks

---

## Scene 2: THE PROBLEM - Scale Failure

**Duration**: ~36 seconds
**Purpose**: Show O(N) complexity and why naive methods fail

### Visual Specification

| Element | Type | Position | Size | Color | Notes |
|---------|------|----------|------|-------|-------|
| Title | Text | Top, UP buff=0.5 | 64pt | #e8e4da | "The Problem" |
| Dot Grid | VGroup(Dot×196) | [0, 0.3, 0] | 14×14 grid, sp=0.32 | #8c8a84 | Represents 5M images |
| Scale Label | Text | [0, -2.8, 0] | 28pt | #e8a838 | "5,000,000+ Images" |
| Test Dot | Dot | [0.05, 0.3, 0] | radius 0.15 | #e8a838 | Query image |
| Glow Circle | Circle | [0.05, 0.3, 0] | radius 0.3 | #f5cc7a | Glow effect |
| Test Label | Text | Above glow | 24pt | #f5cc7a | "Your image" |
| Arrows | Arrow×12 | Radiating from center | 2.2 length | #e8a838 | Search pattern |
| Problem 1 Title | Text | [-2.8, 2.2, 0] | 26pt | #e8a838 | "Slow" |
| Problem 1 Desc | Text | [-2.8, 1.9, 0] | 18pt | #8c8a84 | "O(N) comparisons" |
| Problem 2 Title | Text | [2.8, 2.2, 0] | 26pt | #e8a838 | "Memory" |
| Problem 2 Desc | Text | [2.8, 1.9, 0] | 18pt | #8c8a84 | "5M+ embeddings" |
| Problem 3 Title | Text | [0, -2.2, 0] | 26pt | #e8a838 | "No Structure" |
| Problem 3 Desc | Text | [0, -2.5, 0] | 18pt | #8c8a84 | "Geography ignored" |
| Impact Text | Text | [0, -3.5, 0] | 36pt | #e8a838 | "This doesn't scale." |

### Timing Breakdown
- 0-1.0s: Title fade in
- 1.5-8.0s: Grid appears, scale label
- 8.0-11.0s: Test dot highlight + label
- 11.0-15.0s: Arrows fan out (12 in bursts of 3)
- 15.0-21.0s: Problem labels appear
- 21.0-28.0s: Impact statement
- 28.0-36.0s: Fade out transition

### Key Requirements
- ✅ Grid must be 14×14 (196 dots) with spacing 0.32
- ✅ Test dot centered at grid origin
- ✅ 12 arrows evenly spaced at 30° intervals
- ✅ Problem labels at TOP-LEFT, TOP-RIGHT, BOTTOM-CENTER
- ✅ Smooth cubic easing for all fades
- ✅ Glow effect around test dot (2D circle)

---

## Scene 3: THE INSIGHT - Hierarchical Structure

**Duration**: ~39 seconds
**Purpose**: Reveal geographic hierarchy + hyperbolic geometry

### Visual Specification

| Element | Type | Position | Size | Color | Notes |
|---------|------|----------|------|-------|-------|
| Title | Text | Top, UP buff=0.5 | 64pt | #e8e4da | "The Insight" |
| City Box | Rectangle | [0, 1.0, 0] | 2.0×0.6 | #e8a838 stroke | Paris layer |
| City Label | Text | Center of box | 28pt | #e8a838 | "Paris" |
| Region Box | Rectangle | [0, 1.0, 0] | 3.2×1.2 | #e8a838 stroke | Île-de-France |
| Region Label | Text | Above box | 22pt | #f5cc7a | "Île-de-France" |
| Country Box | Rectangle | [0, 1.0, 0] | 4.4×1.8 | #e8a838 stroke | France |
| Country Label | Text | Above box | 20pt | #f5cc7a | "France" |
| Continent Box | Rectangle | [0, 1.0, 0] | 5.6×2.6 | #e8a838 stroke | Europe |
| Continent Label | Text | Above box | 18pt | #f5cc7a | "Europe" |
| Problem Text | Text | [0, -2.3, 0] | 28pt | #8c8a84 | Euclidean problem |
| Poincaré Disk | Circle | [0, 0.8, 0] | radius 1.4 | #e8a838 stroke | Hyperbolic space |
| Solution Title | Text | [0, 2.4, 0] | 32pt | #e8a838 | "Hyperbolic Space" |
| Solution Desc | Text | [0, -2.2, 0] | 24pt | #f5cc7a | Growth description |

### Timing Breakdown
- 0-1.0s: Title fade in
- 1.5-13.0s: Nested boxes (City → Region → Country → Continent) with labels
- 13.0-22.0s: Problem statement appears
- 22.0-35.0s: Poincaré disk introduction + description
- 35.0-39.0s: Fade out transition

### Key Requirements
- ✅ Nested rectangles centered at origin
- ✅ Boxes created in order: smallest to largest
- ✅ Labels positioned ABOVE each box (not inside)
- ✅ Clean stroke appearance, minimal fill
- ✅ Poincaré disk is simple circle (represents hyperbolic space)
- ✅ Gold is primary accent color throughout

---

## Scene 4: THE SOLUTION - HierLoc Architecture

**Duration**: ~70 seconds
**Purpose**: Show the complete pipeline

### Visual Specification

| Component | Type | Position | Size | Color |
|-----------|------|----------|------|-------|
| Title | Text | Top | 64pt | #e8e4da |
| **IMAGE ENCODING PHASE** | | | | |
| Image Box | Rectangle | [-3.0, 1.2, 0] | 2.0×1.6 | #e8a838 stroke |
| Image Label | Text | Center | 20pt | #e8a838 |
| Arrow 1 | Arrow | [-2.0, 1.2, 0] → [-0.8, 1.2, 0] | 1.2 length | #e8a838 |
| Encode Label | Text | Above arrow | 16pt | #e8a838 |
| **EMBEDDING PHASE** | | | | |
| Embedding Box | Rectangle | [0.2, 1.2, 0] | 1.4×1.4 | #e8a838 stroke |
| Embedding Label | Text | Center | 18pt | #e8a838 |
| Arrow 2 | Arrow | [0.9, 1.2, 0] → [2.2, 1.2, 0] | 1.3 length | #f5cc7a |
| Map Label | Text | Above arrow | 16pt | #f5cc7a |
| **ENTITY SPACE PHASE** | | | | |
| Entity Circle | Circle | [3.2, 1.2, 0] | radius 0.6 | #e8a838 stroke |
| Entity Dots | Dot×7 | Radial around circle | radius 0.08 | #e8a838 |
| Entity Label | Text | Below circle | 14pt | #e8a838 |
| **HIERARCHICAL SEARCH** | | | | |
| Search Title | Text | [0, -0.5, 0] | 28pt | #e8a838 |
| Search Steps | Text | [0, -1.8, 0] | 20pt | #8c8a84 |
| **EFFICIENCY METRICS** | | | | |
| Efficiency Title | Text | [0, 2.0, 0] | 36pt | #e8a838 |
| Trad Header | Text | [-2.2, 0.8, 0] | 20pt | #8c8a84 |
| Trad Metrics | Text | [-2.2, 0.2, 0] | 18pt | #8c8a84 |
| HierLoc Header | Text | [2.2, 0.8, 0] | 20pt | #e8a838 |
| HierLoc Metrics | Text | [2.2, 0.2, 0] | 18pt | #f5cc7a |
| Improvement | Text | [0, -2.2, 0] | 28pt | #e8a838 |

### Timing Breakdown
- 0-1.0s: Title
- 1.5-20.0s: Pipeline visualization (image → encode → embed → match → entity space)
- 20.0-40.0s: Hierarchical search explanation
- 40.0-70.0s: Efficiency metrics and improvement

### Key Requirements
- ✅ Left-to-right flow (image → embedding → entity space)
- ✅ All boxes and circles use stroke, minimal fill
- ✅ Arrow colors indicate transformation type
- ✅ Entity dots arranged in circle pattern
- ✅ Metrics in two-column layout
- ✅ Key improvement highlighted prominently

---

## Scene 5: RESULTS - Impact

**Duration**: ~45 seconds
**Purpose**: Show state-of-the-art results

### Visual Specification

| Element | Type | Position | Size | Color | Notes |
|---------|------|----------|------|-------|-------|
| Title | Text | Top | 64pt | #e8e4da | "Results" |
| **METRIC CARDS** | | | | | |
| M1 Label | Text | [-2.5, 1.3, 0] | 20pt | #8c8a84 | Geodesic Error |
| M1 Value | Text | [-2.5, 0.7, 0] | 40pt | #e8a838 | "↓ 19.5%" |
| M2 Label | Text | [2.5, 1.3, 0] | 20pt | #8c8a84 | Country Accuracy |
| M2 Value | Text | [2.5, 0.7, 0] | 40pt | #e8a838 | "+8.8%" |
| M3 Label | Text | [0, 1.3, 0] | 20pt | #8c8a84 | Region Accuracy |
| M3 Value | Text | [0, 0.7, 0] | 40pt | #e8a838 | "+20.1%" |
| M4 Label | Text | [0, -0.5, 0] | 22pt | #e8e4da | Subregion Accuracy |
| M4 Value | Text | [0, -1.3, 0] | 48pt | #f5cc7a | "+43.2%" |
| **WHY IT MATTERS** | | | | | |
| Insights Title | Text | [0, 1.5, 0] | 32pt | #e8a838 | "Why This Matters" |
| I1 | Text | [-1.5, 0.4, 0] | 22pt | #e8e4da | Speed insight |
| I2 | Text | [1.5, 0.4, 0] | 22pt | #e8e4da | Memory insight |
| I3 | Text | [0, -0.5, 0] | 22pt | #e8e4da | Interpretability |
| **BIG INSIGHT** | | | | | |
| Big Insight | Text | [0, 0.3, 0] | 32pt | #f5cc7a | Hyperbolic geometry |
| **CALL TO ACTION** | | | | | |
| CTA | Text | [0, -2.0, 0] | 24pt | #e8a838 | Learn more link |

### Timing Breakdown
- 0-1.0s: Title
- 1.5-15.0s: Metric cards appear (M1, M2, M3, then M4 highlights)
- 15.0-28.0s: Why It Matters section
- 28.0-38.0s: Big insight about hyperbolic geometry
- 38.0-45.0s: Call to action + fade out

### Key Requirements
- ✅ M4 (subregion +43.2%) is STANDOUT - largest and brightest color
- ✅ Metric cards arranged in grid
- ✅ Three advantages displayed with emojis
- ✅ Final insight in gold color (#f5cc7a)
- ✅ CTA is link/action-oriented
- ✅ Triumphant tone throughout

---

## Global Specifications

### Canvas & Coordinate System
- **Scene dimensions**: 8 units wide, 4.5 units tall
- **Frame rate**: 60 fps (1080p60)
- **Background**: #0a0a0f (ink/dark cosmos)
- **Origin**: Centered [0, 0, 0]
- **Coordinate system**: Standard Manim (Y increases upward)

### Typography Rules
- **Font**: Futura (modern geometric sans-serif)
- **Title sizes**: 64pt (scene), 96pt (major)
- **Body sizes**: 18-32pt depending on hierarchy
- **Label sizes**: 14-24pt
- **Line spacing**: 1.2-1.4 for multi-line text
- **All fonts**: No serifs (except Optima as fallback)

### Color Palette
```
#0a0a0f  - Background (ink)
#e8a838  - Primary accent (gold)
#f5cc7a  - Light gold (highlights)
#e8e4da  - Text primary (cream)
#8c8a84  - Text muted (secondary)
#14141e  - Surface (panels)
```

### Animation Standards
- **Fade in/out**: 0.6-1.0 seconds
- **Text write**: 0.4-0.8 seconds (linear)
- **Create (shapes)**: 0.6-0.9 seconds
- **Easing**: `rate_functions.ease_in_out_cubic` (smooth)
- **Wait pauses**: 0.3-2.5 seconds between animations

### Images
- **Location**: `/Volumes/SSD/iclr-website/static/images/streetview/`
- **Files**:
  - `Paris_00131_445353063_8c58bd82b1_179_88895879@N00.jpg`
  - `Russia_00019_985802242_5ad0b7dbeb_1190_23707253@N00.jpg`
  - `482314949_dbc149bb10_224_50435419@N00.jpg`
  - `0b_5a_5283974984.jpg`
- **Usage**: Scene 1 (2 images), others optional
- **Height when loaded**: 3.0 units

---

## Future Modifications Checklist

### Before Changes
- [ ] Read entire SCENE_SPECIFICATIONS.md
- [ ] Check coordinates against this document
- [ ] Verify colors from palette
- [ ] Understand timing requirements

### During Changes
- [ ] Plan exact coordinates
- [ ] Test readability at actual size
- [ ] Verify color contrast
- [ ] Check alignment and symmetry
- [ ] Test smooth animations

### After Changes
- [ ] Render single scene to test
- [ ] Verify visual output matches spec
- [ ] Update CHANGELOG.md
- [ ] Commit with reference to spec

---

**Last Updated**: February 20, 2026
**Version**: 0.3.0
**Status**: Specification complete, rendering in progress

