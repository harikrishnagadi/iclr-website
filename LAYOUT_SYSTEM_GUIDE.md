# CSS-Like Layout System for Manim

**Date**: February 20, 2026
**Status**: ✅ Implemented & Integrated
**Version**: 1.0

---

## 🎯 Overview

A professional, CSS-inspired layout system for Manim that provides:

- **Intelligent object positioning** with automatic overlap detection
- **Canvas bounds validation** to prevent cutoff
- **Safe positioning algorithms** that reposition objects automatically
- **Readability guarantees** through spacing and validation
- **Debug support** for layout troubleshooting

---

## 📋 Core Features

### 1. Bounds Calculation (`get_bounds`)

Get complete bounding information for any mobject:

```python
from layout import ObjectPositioner

bounds = ObjectPositioner.get_bounds(text_object)
# Returns:
# {
#     'x_min': -2.5,        # Left edge
#     'x_max': 2.5,         # Right edge
#     'y_min': -0.4,        # Bottom edge
#     'y_max': 0.4,         # Top edge
#     'width': 5.0,         # Object width
#     'height': 0.8,        # Object height
#     'center': [0, 0, 0]   # Center point
# }
```

**Key Features:**
- Works with all Manim mobjects
- Returns None for invalid objects
- Includes center point for easy repositioning
- Precise measurements for overlap detection

### 2. Overlap Detection (`check_overlap`)

Detect if two objects collide:

```python
overlaps = ObjectPositioner.check_overlap(
    bounds1,
    bounds2,
    h_spacing=0.2,  # Horizontal spacing requirement
    v_spacing=0.3   # Vertical spacing requirement
)
# Returns: True if overlapping, False otherwise
```

**Parameters:**
- `bounds1`, `bounds2`: Bounding box dictionaries
- `h_spacing`: Minimum horizontal distance (Manim units)
- `v_spacing`: Minimum vertical distance (Manim units)

**Use Cases:**
- Validate text doesn't overlap images
- Check labels don't collide with each other
- Ensure readable spacing between elements

### 3. Multi-Object Overlap Check (`check_multiple_overlaps`)

Check against multiple objects at once:

```python
overlap_indices = ObjectPositioner.check_multiple_overlaps(
    test_bounds,
    [bounds1, bounds2, bounds3],
    h_spacing=0.2,
    v_spacing=0.3
)
# Returns: [0, 2] - overlaps with objects at index 0 and 2
```

**Advantages:**
- Single call for multiple checks
- Returns indices for easy reference
- More efficient than looping manually

### 4. Canvas Validation (`is_within_canvas`)

Ensure objects stay on screen:

```python
is_valid, errors = ObjectPositioner.is_within_canvas(
    bounds,
    margin=0.2  # Buffer from edges
)

if not is_valid:
    for error in errors:
        print(error)  # "Object extends beyond right edge..."
```

**Canvas Dimensions:**
- Top: Y = 4.0
- Bottom: Y = -4.0
- Left: X = -7.1
- Right: X = 7.1

**Validates:**
- All four edges
- Safe margin (default 0.2 units)
- Reports specific violations

### 5. Position Below Reference (`position_below`)

Calculate safe position below another object:

```python
new_y = ObjectPositioner.position_below(
    reference_bounds,
    object_height=0.6,
    center_x=0,
    v_spacing=0.3
)
# Returns: Y coordinate for safe placement
```

**Calculation:**
- Places object cleanly below reference
- Respects vertical spacing
- Centers horizontally if specified

### 6. Intelligent Y-Position Search (`find_safe_y_position`)

Find non-overlapping position automatically:

```python
safe_y, found, new_bounds = ObjectPositioner.find_safe_y_position(
    target_height=0.6,
    existing_bounds_list=[bounds1, bounds2],
    start_y=0,
    direction='down',
    h_spacing=0.2,
    v_spacing=0.3,
    center_x=0
)

if found:
    obj.move_to([center_x, safe_y, 0])
else:
    print("Could not find safe position")
```

**Algorithm:**
1. Start at `start_y`
2. Check for overlaps with all existing bounds
3. If overlap found, move in specified direction
4. Repeat up to 20 times
5. Return successful position or None

**Parameters:**
- `direction`: 'down' or 'up' for movement direction
- `h_spacing`, `v_spacing`: Minimum spacing requirements
- `center_x`: X coordinate to center object

### 7. Multi-Object Layout (`layout_objects`)

Position entire groups with automatic repositioning:

```python
from layout import ObjectPositioner

objects = [
    {
        'object': title_text,
        'name': 'Title',
        'target_y': 0,
        'center_x': 0,
        'width': 6.0,
        'height': 0.8
    },
    {
        'object': body_text,
        'name': 'Body',
        'target_y': -1.0,
        'center_x': 0,
        'width': 7.0,
        'height': 1.2
    }
]

results = ObjectPositioner.layout_objects(scene, objects)

if results['success']:
    print("All objects placed successfully!")
else:
    print(f"Warnings: {results['warnings']}")
    print(f"Errors: {results['errors']}")
```

**Returns:**
```python
{
    'success': True,
    'placed_objects': ['Title', 'Body'],
    'skipped_objects': [],
    'bounds_list': [...],
    'warnings': [...],
    'errors': [...]
}
```

**Features:**
- Batch positioning with single call
- Automatic repositioning if overlaps
- Detailed reporting
- Validates canvas bounds
- Respects spacing requirements

### 8. Debug Support (`debug_layout`)

Print detailed layout report:

```python
ObjectPositioner.debug_layout(scene, objects, results)

# Output:
# ============================================================
# LAYOUT POSITIONING RESULTS
# ============================================================
# Success: True
# Placed Objects: 2
# Skipped Objects: 0
#
# Placed:
#   ✓ Title
#   ✓ Body
#
# Warnings: [...]
# Errors: [...]
# ============================================================
```

---

## 🎬 Scene 1 Implementation

### Current Usage

The new layout system is integrated into Scene 1 for positioning the Visual Geolocation definition text:

```python
from layout import ObjectPositioner

# Get reference bounds from images
image_bounds_list = [ObjectPositioner.get_bounds(img) for img in image_objects]

# Find bottom of images
bottom_y_values = [bounds['y_min'] for bounds in image_bounds_list if bounds]
bottom_image_y = min(bottom_y_values)

# Define text elements to position
objects_to_position = [
    {
        'object': geo_title,
        'name': 'Visual Geolocation Title',
        'target_y': bottom_image_y - 0.8,
        'center_x': 0,
        'width': 6.0,
        'height': 0.8
    },
    {
        'object': geo_description,
        'name': 'Visual Geolocation Definition',
        'target_y': bottom_image_y - 1.6,
        'center_x': 0,
        'width': 8.0,
        'height': 0.6
    },
    {
        'object': task_text,
        'name': 'Challenge Text',
        'target_y': bottom_image_y - 2.3,
        'center_x': 0,
        'width': 7.0,
        'height': 0.6
    }
]

# Apply smart layout
layout_results = ObjectPositioner.layout_objects(self, objects_to_position)

# Show debug information
ObjectPositioner.debug_layout(self, objects_to_position, layout_results)

# Position elements
if layout_results['success']:
    self.play(FadeIn(geo_title, geo_description, task_text))
```

### Results

✅ All text positioned below bottom images
✅ No overlaps between text elements
✅ No cutoff at canvas edges
✅ Proper vertical spacing maintained
✅ Automatic fallback if issues occur

---

## 📏 Layout Constants

```python
# Canvas dimensions (Manim units)
CANVAS_TOP = 4.0          # Top edge Y coordinate
CANVAS_BOTTOM = -4.0      # Bottom edge Y coordinate
CANVAS_LEFT = -7.1        # Left edge X coordinate
CANVAS_RIGHT = 7.1        # Right edge X coordinate
CANVAS_WIDTH = 14.2       # Total width
CANVAS_HEIGHT = 8.0       # Total height

# Minimum spacing
MIN_VERTICAL_SPACING = 0.3     # Between vertically stacked objects
MIN_HORIZONTAL_SPACING = 0.2   # Between horizontally adjacent objects

# Canvas margin
DEFAULT_MARGIN = 0.2      # Buffer from edges to prevent cutoff
```

---

## 🔧 Advanced Usage

### Custom Spacing Rules

```python
# Tight spacing (for dense layouts)
tight_spacing = {
    'h_spacing': 0.1,
    'v_spacing': 0.15
}

# Comfortable spacing (for readability)
comfortable_spacing = {
    'h_spacing': 0.3,
    'v_spacing': 0.4
}

# Use in overlap check
overlaps = ObjectPositioner.check_multiple_overlaps(
    bounds,
    existing_bounds,
    **comfortable_spacing
)
```

### Dynamic Positioning

```python
# Position object relative to multiple references
def position_between(obj, top_bounds, bottom_bounds, margin=0.3):
    gap = top_bounds['y_min'] - bottom_bounds['y_max']
    if gap > obj.height + margin * 2:
        # Enough space - center in gap
        center_y = (top_bounds['y_min'] + bottom_bounds['y_max']) / 2
    else:
        # Use smart search
        safe_y, found, _ = ObjectPositioner.find_safe_y_position(
            obj.height,
            [top_bounds, bottom_bounds],
            start_y=0,
            direction='down'
        )
        center_y = safe_y

    return center_y
```

### Batch Repositioning

```python
# Reposition group if any overlaps occur
def reposition_group(scene, mobjects, reference_bounds, start_y=0):
    results_list = []

    for i, obj in enumerate(mobjects):
        safe_y, found, bounds = ObjectPositioner.find_safe_y_position(
            obj.height,
            reference_bounds + [b for b in results_list],
            start_y=start_y - (i * 0.8),
            direction='down'
        )

        if found:
            obj.move_to([0, safe_y, 0])
            results_list.append(bounds)

    return results_list
```

---

## 🎯 Common Patterns

### Pattern 1: Text Below Image

```python
image_bounds = ObjectPositioner.get_bounds(image)
text_y = ObjectPositioner.position_below(
    image_bounds,
    text.height,
    center_x=image_bounds['center'][0],
    v_spacing=0.5
)
text.move_to([image_bounds['center'][0], text_y, 0])
```

### Pattern 2: Column of Text

```python
objects = [title, subtitle, body, footer]
y_pos = 3.0

for obj in objects:
    bounds = ObjectPositioner.get_bounds(obj)
    y_pos = ObjectPositioner.position_below(
        {'y_min': y_pos, 'y_max': y_pos + 0.1},
        obj.height,
        center_x=0,
        v_spacing=0.2
    )
    obj.move_to([0, y_pos, 0])
```

### Pattern 3: Safe Grid Layout

```python
# Position items in grid without overlaps
grid_items = [...]
cols = 3
spacing = 0.4

for i, item in enumerate(grid_items):
    col = i % cols
    row = i // cols

    x = -3.0 + col * 4.0
    y = 2.0 - row * spacing

    bounds = ObjectPositioner.get_bounds(item)
    if not ObjectPositioner.is_within_canvas(bounds)[0]:
        # Find safe position
        y, found, _ = ObjectPositioner.find_safe_y_position(
            item.height,
            placed_bounds,
            start_y=y,
            center_x=x
        )

    item.move_to([x, y, 0])
```

---

## 📊 Performance Considerations

### Complexity
- `get_bounds()`: O(1)
- `check_overlap()`: O(1)
- `check_multiple_overlaps()`: O(n) where n = number of objects
- `find_safe_y_position()`: O(n × 20) worst case
- `layout_objects()`: O(n²) where n = number of objects

### Optimization Tips
- Reuse bounds calculations instead of recalculating
- Sort existing bounds for faster search
- Limit number of iterations in position search
- Use appropriate spacing values (not too tight)

### Caching
```python
# Cache bounds to avoid recalculation
bounds_cache = {
    'image1': ObjectPositioner.get_bounds(img1),
    'image2': ObjectPositioner.get_bounds(img2),
    'text1': ObjectPositioner.get_bounds(txt1),
}

# Use cache in overlaps
overlaps = ObjectPositioner.check_multiple_overlaps(
    bounds_cache['text1'],
    [bounds_cache['image1'], bounds_cache['image2']]
)
```

---

## ✅ Implementation Checklist

For other scenes using this system:

- [ ] Import ObjectPositioner
- [ ] Collect bounds for reference objects (images, existing text)
- [ ] Define objects to position with metadata
- [ ] Call `layout_objects()` or use individual functions
- [ ] Check results for success/warnings
- [ ] Implement fallback positioning
- [ ] Add debug output for troubleshooting
- [ ] Test with different canvas configurations
- [ ] Document custom spacing requirements

---

## 🐛 Debugging Tips

1. **Use debug output**
   ```python
   ObjectPositioner.debug_layout(scene, objects, results)
   ```

2. **Print bounds**
   ```python
   bounds = ObjectPositioner.get_bounds(obj)
   print(f"Object bounds: {bounds}")
   ```

3. **Check canvas limits**
   ```python
   is_valid, errors = ObjectPositioner.is_within_canvas(bounds)
   print(errors)
   ```

4. **Test overlap detection**
   ```python
   overlaps = ObjectPositioner.check_overlap(b1, b2)
   print(f"Overlapping: {overlaps}")
   ```

5. **Visualize positions** (in Manim)
   ```python
   # Add bounding box rectangles for debugging
   rect = Rectangle(
       width=bounds['width'],
       height=bounds['height'],
       color=RED,
       opacity=0.3
   )
   rect.move_to(bounds['center'])
   scene.add(rect)
   ```

---

## 🚀 Future Enhancements

Potential improvements:

1. **Gravity-based positioning** - Objects "fall" to lowest safe position
2. **Constraint solving** - Complex layout rules (equal spacing, alignment, etc.)
3. **Responsive scaling** - Automatically scale objects to fit without overlaps
4. **Layout presets** - Pre-defined layouts (sidebar, centered, grid, etc.)
5. **Visual layout tool** - Interactive layout designer
6. **Accessibility checks** - Color contrast, font size, readability metrics

---

## 📞 Integration Guide

### For Scene 2+

```python
from layout import ObjectPositioner

# In your scene's construct method:

# 1. Get reference bounds
ref_bounds = [
    ObjectPositioner.get_bounds(image1),
    ObjectPositioner.get_bounds(image2),
]

# 2. Define your layout
layout_spec = [
    {
        'object': title_text,
        'name': 'Title',
        'target_y': 2.0,
        'center_x': 0,
        'width': 6.0,
        'height': 0.8
    },
    # ... more objects
]

# 3. Apply layout
results = ObjectPositioner.layout_objects(self, layout_spec)

# 4. Handle results
if results['success']:
    # Animate elements
    self.play(FadeIn(*[obj['object'] for obj in layout_spec]))
else:
    # Log errors for debugging
    print(results['errors'])
```

---

## 📝 Summary

The ObjectPositioner layout system provides:

✅ Professional object positioning
✅ Automatic overlap detection
✅ Canvas boundary validation
✅ Intelligent repositioning
✅ Readability guarantees
✅ Comprehensive debugging
✅ Flexible API for all use cases
✅ Performance-optimized algorithms

Ready to use in all Manim scenes for perfect layout every time!

---

**Status**: ✅ Production Ready
**Integration**: Scene 1 ✅, Ready for Scenes 2-5
**Documentation**: Complete
**Testing**: ✅ Scene 1 verified
