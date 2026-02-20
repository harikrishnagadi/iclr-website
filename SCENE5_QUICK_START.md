# Scene 5 - Quick Start Guide

**Status**: ✓ Complete and Ready
**Duration**: ~30 seconds
**Quality**: Production-ready

---

## What Is Scene 5?

The final scene of the HierLoc video, showing **results and impact** in 5 dramatic phases over ~30 seconds.

---

## Quick Facts

| Item | Value |
|------|-------|
| File | `manim_video/scenes/scene5_results.py` |
| Size | 854 lines |
| Class | `Scene5Results(Scene)` |
| Phases | 5 |
| Duration | ~30 seconds |
| Assets Required | None (all procedurally generated) |
| External Dependencies | None (uses config.py, utils.py) |

---

## The 5 Phases

### Phase 1: Results Metrics (5-6s)
**What**: Animated bars showing accuracy improvements
- Mean Geodesic Error: ↓19.5%
- Country: +8.8%
- Region: +20.1%
- **Subregion: +43.2%** ← EMPHASIZED
- City: +16.8%

**Narration**: "The results? State-of-the-art performance across every geographic level"

### Phase 2: Efficiency Comparison (5-6s)
**What**: Side-by-side comparison
- 240k entity embeddings (small box, gold)
- **95% Reduction** (center, big text, gold)
- 5M+ image embeddings (large box, muted)

**Narration**: "95% fewer embeddings to store and search"

### Phase 3: Interpretability (5-6s)
**What**: Hierarchical path reveal
- Image → Germany → Bavaria → Munich
- Arrows connect each level
- Final location highlighted

**Narration**: "And the system is interpretable - you know which entities matched"

### Phase 4: Broader Impact (5-6s)
**What**: Geometric insight with subtle background
- "Hyperbolic Geometry is the right tool for hierarchical data"
- Exponential volume = Exponential hierarchy

**Narration**: "This shows something bigger..."

### Phase 5: Call-to-Action (4-5s)
**What**: Finale with links
- "HierLoc: Hierarchical Visual Geolocation"
- "Learn More"
- "Paper • Code • Website"

**Narration**: Encouraging to explore further

---

## How to Render

### Quick Render (Low Quality)
```bash
manim -ql manim_video/scenes/scene5_results.py Scene5Results
```

### Final Render (High Quality, 1080p, 60fps)
```bash
manim -qh manim_video/scenes/scene5_results.py Scene5Results
```

### With Preview
```bash
manim -qh -p manim_video/scenes/scene5_results.py Scene5Results
```

---

## File Structure

```
scene5_results.py
├── Imports & Setup
│   └── config.py, utils.py
│
├── Scene5Results (class)
│   ├── construct() - Calls all 5 phases
│   ├── phase_1_results_metrics()
│   ├── phase_2_efficiency_comparison()
│   ├── phase_3_interpretability()
│   ├── phase_4_broader_impact()
│   └── phase_5_call_to_action()
│
└── Main block
```

---

## Color Palette

| Name | Hex | Use |
|------|-----|-----|
| Background | #0a0a0f | Scene background |
| Accent Gold | #e8a838 | Primary highlights |
| Light Gold | #f5cc7a | Emphasis/secondary |
| Text | #e8e4da | Primary text |
| Text Muted | #8c8a84 | Secondary text |
| Surface | #14141e | Container backgrounds |
| Red (special) | #e74c3c | Error metric in Phase 1 |

---

## Animation Timing

Phase 1: 5-6s
Phase 2: 5-6s
Phase 3: 5-6s
Phase 4: 5-6s
Phase 5: 4-5s
**Total**: ~30s (with dramatic pauses)

---

## Key Numbers to Know

**Phase 1 Metrics**:
- 19.5% (Mean Geodesic Error)
- 8.8% (Country)
- 20.1% (Region)
- 43.2% (Subregion) ← BIGGEST
- 16.8% (City)

**Phase 2**:
- 240k entity embeddings
- 5M+ image embeddings
- 95% reduction

**Phase 3**:
- Image → Germany → Bavaria → Munich
- 4 levels in hierarchy

---

## Common Customizations

### Change a metric value
In `phase_1_results_metrics()`, modify `metrics_data`:
```python
metrics_data = [
    ("Mean Geodesic\nError", 19.5, 0.8),  # ← Change 19.5
    ...
]
```

### Change efficiency comparison numbers
In `phase_2_efficiency_comparison()`, update labels:
```python
left_label = "240k\nEntity\nEmbeddings"    # ← Change here
right_label = "5M+\nImage\nEmbeddings"    # ← Or here
```

### Change final links
In `phase_5_call_to_action()`, update:
```python
links_text = create_sans_body(
    "Paper  •  Code  •  Website",  # ← Change links here
    ...
)
```

---

## Integration with Other Scenes

Scene 5 follows Scene 4 in the narrative sequence:
1. Scene 1: Hook (problem posed)
2. Scene 2: Problem (why it's hard)
3. Scene 3: Insight (geometric solution)
4. Scene 4: Solution (how it works)
5. **Scene 5: Results** ← You are here

All 5 scenes use the same color palette (#0a0a0f bg, #e8a838 accent) and typography (DM Serif Display + Syne).

---

## Documentation Files

1. **SCENE5_IMPLEMENTATION_REPORT.md** - Complete technical overview
2. **SCENE5_TECHNICAL_REFERENCE.md** - Code-level reference
3. **SCENE5_VISUAL_STRUCTURE.md** - Storyboards and visual flow
4. **SCENE5_QUICK_START.md** - This file (quick reference)
5. **SCENE5_COMPLETION_SUMMARY.md** - Final summary and checklist

---

## Troubleshooting

**Q: Fonts not found?**
A: Manim will use fallbacks (Arial/Helvetica) if DM Serif Display/Syne aren't installed. Visual appearance will be slightly different but animations will work fine.

**Q: Animations too fast/slow?**
A: Adjust `run_time` parameter in animations (it's in seconds). Find the animation, change `run_time=1.0` to `run_time=0.5` to speed up, or `run_time=2.0` to slow down.

**Q: Can't import Scene5Results?**
A: Make sure:
1. You're in the correct directory (`/Volumes/SSD/iclr-website`)
2. config.py and utils.py exist in `manim_video/`
3. You use: `from manim_video.scenes.scene5_results import Scene5Results`

**Q: Want to test just one phase?**
A: Edit `construct()` to call only the phase you want, e.g.:
```python
def construct(self):
    self.camera.background_color = COLORS["bg"]
    self.phase_1_results_metrics()  # Only test Phase 1
    self.wait(1.0)
```

---

## Next Steps

1. ✓ Code is complete and tested
2. ✓ All 5 phases implemented
3. → Render at high quality
4. → Review animations
5. → Add narration (use script from HIERLOC_VIDEO_PLAN.md)
6. → Integrate with Scenes 1-4
7. → Add music and sound design
8. → Export final video

---

## One-Liner Summary

Scene 5 is a **complete, production-ready animation** of the HierLoc video's results phase, showing metrics, efficiency, interpretability, impact, and call-to-action in 5 dramatic phases over ~30 seconds.

---

**Status**: READY TO RENDER ✓
