# HierLoc Video - Design System & Style Guide

**Version**: 0.3.0
**Status**: Active (Award-winning redesign)

Comprehensive design system for maintaining visual consistency across all scenes and future modifications.

---

## Color System

### Primary Colors
```
BACKGROUND     #0a0a0f   Dark cosmos/ink - calm, sophisticated
PRIMARY_ACCENT #e8a838   Geodesic gold - attention, energy
LIGHT_GOLD     #f5cc7a   Highlight gold - emphasis, standout
TEXT_PRIMARY   #e8e4da   Cream/off-white - excellent readability
TEXT_MUTED     #8c8a84   Gray-brown - secondary info
SURFACE        #14141e   Panel color - subtle hierarchy
```

### Color Usage Rules

**Background (#0a0a0f)**
- Never change background color for scenes
- Provides calm, sophisticated foundation
- High contrast with text

**Primary Accent (#e8a838)**
- Use for: Scene titles, key labels, main highlights
- Draws attention without being flashy
- Used in ~15-20% of visual elements
- Creates visual rhythm

**Light Gold (#f5cc7a)**
- Use for: Standout metrics, "aha moments", emphasis
- Brighter than primary accent
- Used sparingly for climactic moments
- Reserved for Scene 5 results

**Text Primary (#e8e4da)**
- Use for: All main text, titles, body copy
- Excellent contrast on #0a0a0f background
- Readable at all font sizes 14pt+
- Professional, warm tone

**Text Muted (#8c8a84)**
- Use for: Secondary labels, descriptions, supporting text
- Less prominent than primary text
- Still readable, creates hierarchy
- Paired with primary text

### Contrast Requirements
- **Minimum**: 4.5:1 ratio for readability
- **Background + Text**: #0a0a0f + #e8e4da = 13:1 (excellent)
- **Background + Muted**: #0a0a0f + #8c8a84 = 7.2:1 (excellent)
- **Background + Gold**: #0a0a0f + #e8a838 = 8.1:1 (excellent)

---

## Typography System

### Font Selection
- **Primary Font**: Futura (modern geometric sans-serif)
- **Fallback**: Helvetica Neue (if Futura unavailable)
- **Monospace**: Menlo (for code, rarely used)
- **Serif**: Optima (not used in current design, reserved for future)

### Font Hierarchy

#### Scale 1: Major Titles (96pt)
- **Font**: Futura
- **Color**: #e8e4da (primary text)
- **Accent**: #e8a838 (specific chars like "Loc" in "HierLoc")
- **Use**: Opening title, main scene names
- **Examples**: "HierLoc", "Visual Geolocation"
- **Tracking**: 1.2x (slightly loose)
- **Weight**: Regular (not bold)

#### Scale 2: Scene Titles (64pt)
- **Font**: Futura
- **Color**: #e8e4da
- **Use**: Scene section headers
- **Examples**: "The Problem", "The Insight", "Results"
- **Line height**: 1.0x
- **Weight**: Regular

#### Scale 3: Headers/Emphasis (28-40pt)
- **Font**: Futura
- **Color**: #e8a838 or #f5cc7a (depending on emphasis level)
- **Use**: Subsection titles, key messages
- **Examples**: "Efficiency", "Why It Matters"
- **Line height**: 1.2x
- **Weight**: Regular

#### Scale 4: Body/Labels (18-24pt)
- **Font**: Futura
- **Color**: #e8e4da (primary) or #8c8a84 (secondary)
- **Use**: Descriptions, metric labels, explanations
- **Examples**: "Country Accuracy", "5M+ images"
- **Line height**: 1.3-1.4x (multi-line)
- **Weight**: Regular

#### Scale 5: Small Text (14-16pt)
- **Font**: Futura
- **Color**: #8c8a84 (muted)
- **Use**: Annotations, tiny labels
- **Examples**: "O(N) comparisons"
- **Minimum**: 14pt (never smaller for readability)
- **Weight**: Regular

### Text Styling Rules

**Do**:
- ✅ Use consistent line height (1.2-1.4x)
- ✅ Align text to logical centers
- ✅ Use color to create hierarchy
- ✅ Leave generous spacing between text elements
- ✅ Use multi-line text for long content

**Don't**:
- ❌ Use bold/italic (use size or color instead)
- ❌ Use ALL CAPS (reduce readability)
- ❌ Justify text (causes awkward spacing)
- ❌ Use colors outside the approved palette
- ❌ Drop below 14pt font size
- ❌ Mix fonts in same scene (Futura only)

### Line Spacing Examples
```python
# 1-line text: No special spacing
title = Text("The Problem", font_size=64)

# 2-3 line text: Use line_spacing=1.3
description = Text(
    "Exponential volume growth\n= Perfect for hierarchy",
    font_size=24,
    line_spacing=1.3
)

# Grouped text: Use .arrange(DOWN, buff=0.3)
group = VGroup(label, value)
group.arrange(DOWN, buff=0.3)
```

---

## Visual Hierarchy

### Element Priority Levels

#### Level 1 - Critical Information (Highest Priority)
- Scene titles
- Main numerical results (+43.2%, ↓19.5%)
- Key insights
- **Appearance**: Largest size, brightest color (#e8a838 or #f5cc7a)
- **Placement**: Prominent position (center, top)
- **Emphasis**: First thing viewer sees

#### Level 2 - Important Information
- Subsection headers
- Metric labels
- Problem descriptions
- **Appearance**: Medium size (28-40pt), primary color (#e8e4da)
- **Placement**: Visible but supporting Level 1
- **Emphasis**: Clear secondary hierarchy

#### Level 3 - Supporting Information
- Descriptions
- Small labels
- Secondary metrics
- **Appearance**: Smaller size (18-24pt), muted color (#8c8a84)
- **Placement**: Below or beside primary elements
- **Emphasis**: Provide context without distraction

#### Level 4 - Background/Context
- Geometric shapes
- Container boxes
- Stroke elements
- **Appearance**: Minimal fill, subtle stroke
- **Color**: Accent colors at low opacity
- **Emphasis**: Frame information without competing

### Spatial Hierarchy
```
TOP        [Scene Title - maximum prominence]

MIDDLE     [Main Content - primary focus area]

           [Supporting Elements]

BOTTOM     [Captions, Labels - least prominent]
```

### Example: Scene 5 (Results)
```
TOP:       "Results" (64pt, primary)

MIDDLE:    Metrics (40pt, gold)
           Labels (20pt, muted)

           "Why It Matters" (32pt, accent)
           Three insights (22pt, primary)

BOTTOM:    "Learn more" (24pt, accent)
```

---

## Geometry & Layout

### Positioning Rules

**Centering**
- Use `[0, Y, 0]` for horizontal center
- Use `to_edge(UP/DOWN/LEFT/RIGHT, buff=0.5)` for edges
- `buff` value creates padding from edge

**Relative Positioning**
```python
# After a reference object
new_element.next_to(reference, direction, buff=spacing)

# Examples:
subtitle.next_to(title, DOWN, buff=0.4)     # Below title
label.next_to(box, UP, buff=0.25)           # Above box
element.next_to(point, RIGHT, buff=0.5)     # Right of point
```

**Grid Alignment**
- All major elements align to 0.5-unit grid
- No random placements
- Spacing values: 0.3, 0.5, 0.8 units (no decimals)

### Shape Sizing Rules

**Rectangles** (for emphasis boxes)
```python
# Width:Height ratio should be intentional
Rectangle(width=2.0, height=1.6)   # ~1.25:1 (slightly wide)
Rectangle(width=4.4, height=1.8)   # ~2.4:1 (wider)
Rectangle(width=5.6, height=2.6)   # ~2.1:1 (consistent)
```

**Circles** (for entity spaces, glows)
```python
Circle(radius=0.6)  # Small entity cluster
Circle(radius=1.2)  # Medium (Poincaré disk)
Circle(radius=1.4)  # Large emphasis
```

**Dots** (for entities, data points)
```python
Dot(radius=0.04)    # Tiny (far away points)
Dot(radius=0.06)    # Small (grid dots)
Dot(radius=0.08)    # Medium (entities)
Dot(radius=0.12)    # Large (highlighted)
Dot(radius=0.15)    # Extra large (focus)
```

### Stroke vs Fill
```python
# Emphasis box (uses stroke, minimal fill)
Rectangle(
    stroke_color=COLORS["accent"],
    stroke_width=2.5,        # Visible but not heavy
    fill_opacity=0.08,       # Very subtle
    fill_color=COLORS["accent"]
)

# Grid dot (uses fill, no stroke)
Dot(
    radius=0.06,
    color=COLORS["text_muted"],
    fill_opacity=0.6         # Visible but transparent
)
```

---

## Animation Principles

### Easing Functions
- **Default**: `rate_functions.ease_in_out_cubic` (smooth, professional)
- **Linear**: Only for text writes (Write animation)
- **Custom**: Never use ease_in or ease_out alone

```python
# Smooth fade
self.play(FadeIn(element, run_time=0.8, rate_func=rate_functions.ease_in_out_cubic))

# Text reveal (always linear)
self.play(Write(text, run_time=0.6, rate_func=linear))

# Shape creation
self.play(Create(shape, run_time=0.7, rate_func=rate_functions.ease_in_out_cubic))
```

### Animation Duration Standards

| Animation Type | Duration | Use Case |
|---|---|---|
| Fade in/out | 0.6-1.0s | Transitions, elements appearing |
| Write (text) | 0.4-0.8s | Text reveals, character by character |
| Create (shape) | 0.6-0.9s | Drawing rectangles, circles, arrows |
| Multiple objects | Staggered 0.2-0.3s | Sequence of related elements |
| Wait/Pause | 0.3-2.5s | Viewer absorption time |

### Wait/Pause Guidelines
- **After animation**: 0.3-0.5s (reader buffer)
- **Between related elements**: 0.4-0.8s (connection time)
- **After important reveal**: 1.0-2.5s (emphasis time)
- **Scene conclusion**: 1.0-2.0s (takeaway time)

### Parallel vs Sequential Animations
```python
# Parallel (simultaneous)
self.play(
    FadeIn(element1, run_time=0.8),
    FadeIn(element2, run_time=0.8),
    FadeIn(element3, run_time=0.8)
)

# Sequential (one after another)
self.play(Create(box, run_time=0.7))
self.play(FadeIn(label, run_time=0.4))
self.wait(0.5)
self.play(Create(arrow, run_time=0.6))
```

---

## Readability Checklist

### Before Finalizing Any Scene

**Text Readability**
- [ ] All text 14pt or larger
- [ ] Primary text (#e8e4da) has 13:1 contrast on background
- [ ] Multi-line text uses 1.2-1.4x line spacing
- [ ] No text overlaps with other elements
- [ ] Text centered or left-aligned (never justified)

**Visual Clarity**
- [ ] Can viewer instantly identify the main message?
- [ ] Are shapes and boxes intentionally positioned?
- [ ] Is there appropriate negative space?
- [ ] Do colors create correct hierarchy?
- [ ] Are all elements aligned to invisible grid?

**Timing & Pacing**
- [ ] Does the scene flow smoothly without abrupt cuts?
- [ ] Are there enough pauses for viewer comprehension?
- [ ] Do animations complete before new ones begin?
- [ ] Is the total timing within budget (24-70s)?

**Color & Contrast**
- [ ] Are colors from approved palette only?
- [ ] Is gold (#e8a838) reserved for emphasis?
- [ ] Is light gold (#f5cc7a) used only for standout moments?
- [ ] Do text colors maintain minimum 4.5:1 contrast?

---

## Common Design Patterns

### Scene Opening
```python
# Standard opening sequence
title = Text("Title", font=FONTS["sans"], font_size=64, color=COLORS["text"])
title.to_edge(UP, buff=0.5)
self.play(FadeIn(title, run_time=1.0))
self.wait(0.5)
```

### Information Box
```python
# Emphasis rectangle with label
box = Rectangle(
    width=2.0, height=1.6,
    stroke_color=COLORS["accent"],
    stroke_width=2,
    fill_opacity=0.1,
    fill_color=COLORS["accent"]
)
label = Text("Label", font_size=20, color=COLORS["accent"])
label.move_to(box.get_center())

self.play(Create(box, run_time=0.6))
self.play(FadeIn(label, run_time=0.4))
```

### Metric Display
```python
# Card-style metric
label = Text("Label", font_size=20, color=COLORS["text_muted"])
value = Text("↓ 19.5%", font_size=40, color=COLORS["accent"])
metric = VGroup(label, value).arrange(DOWN, buff=0.3)
metric.move_to(position)

self.play(FadeIn(metric, run_time=0.7))
```

### Transitional Arrow
```python
# Connecting elements
arrow = Arrow(
    start=from_position,
    end=to_position,
    buff=0.1,
    color=COLORS["accent"],
    stroke_width=2.5,
    tip_length=0.15
)
self.play(Create(arrow, run_time=0.5))
```

### Scene Conclusion
```python
# Standard fade-out
self.play(
    FadeOut(element1, element2, element3, element4, run_time=1.0)
)
self.wait(0.5)
```

---

## Design Philosophy

### Core Principles

**1. Intentionality**
- Every element has a purpose
- Every placement is meaningful
- Nothing is accidental or arbitrary
- Results in "professional" feel

**2. Clarity**
- Viewers instantly understand each scene
- Visual hierarchy guides attention
- No visual clutter or distraction
- Information is easily absorbed

**3. Elegance**
- Minimal design (remove unnecessary elements)
- Clean geometry (proper proportions)
- Sophisticated color palette
- Smooth animations (cubic easing)

**4. Consistency**
- Same fonts, colors, spacing throughout
- Predictable animations and timing
- Unified visual language
- Creates coherence across 5 scenes

### Design Process
1. **Plan**: Sketch coordinates and layout
2. **Build**: Create elements at exact positions
3. **Test**: Check readability and alignment
4. **Refine**: Adjust based on visual feedback
5. **Verify**: Confirm matches style guide

---

## Future Modifications

### When Adding Elements
1. Check SCENE_SPECIFICATIONS.md for coordinate system
2. Use colors only from approved palette
3. Maintain minimum font size of 14pt
4. Verify contrast ratios
5. Test readability on 1080p screen
6. Use cubic easing for smooth animations
7. Update CHANGELOG.md with changes

### When Removing Elements
1. Ensure remaining layout is balanced
2. Update specifications if needed
3. Verify no readability issues
4. Test smooth transitions
5. Document removal in CHANGELOG.md

### Prohibited Changes
- ❌ Changing background color
- ❌ Using fonts outside approved list
- ❌ Adding colors outside palette
- ❌ Making text smaller than 14pt
- ❌ Using easing other than cubic
- ❌ Violating 4.5:1 contrast ratio

---

**Last Updated**: February 20, 2026
**Version**: 0.3.0
**Maintained by**: Claude Code & Future Agents

