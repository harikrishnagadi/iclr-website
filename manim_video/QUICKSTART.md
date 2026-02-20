# HierLoc Manim Video - Quick Start Guide

## 1. Initial Setup (One-time)

```bash
cd manim_video
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## 2. Rendering Videos

### Single Scene
```bash
./render.sh scene1    # Renders Scene 1 (Hook)
./render.sh scene2    # Renders Scene 2 (Problem)
./render.sh scene3    # Renders Scene 3 (Insight)
./render.sh scene4    # Renders Scene 4 (Solution)
./render.sh scene5    # Renders Scene 5 (Results)
```

### All Scenes
```bash
./render.sh all       # Renders all 5 scenes
```

## 3. Output Location
- Videos: `output/videos/`
- Images: `output/images/`

## 4. Quick Reference: Design System

### Colors (in config.py)
```python
COLORS = {
    "accent": "#e8a838",      # Gold accent
    "text": "#e8e4da",        # Main text
    "text_muted": "#8c8a84",  # Secondary text
    "bg": "#0a0a0f",          # Dark background
}
```

### Text Functions (in utils.py)
```python
from utils import create_serif_title, create_sans_body, create_mono_code

title = create_serif_title("My Title", font_size=60)
body = create_sans_body("My text", font_size=32)
code = create_mono_code("code_here()", font_size=24)
```

### Creating Animations
```python
from manim import *
from config import COLORS, FONTS, setup_manim_config
from utils import create_serif_title

setup_manim_config(quality="high_quality")

class MyScene(Scene):
    def construct(self):
        title = create_serif_title("My Scene")
        self.play(FadeIn(title))
        self.wait(2)
```

## 5. File Organization

Each scene file follows this structure:
```python
from manim import *
from config import COLORS, FONTS, setup_manim_config
from utils import create_serif_title, ...

setup_manim_config(quality="high_quality")

class SceneXName(Scene):
    def construct(self):
        # Your animations here
        pass
```

## 6. Quality Settings

For quick testing:
```bash
# Edit render.sh, change QUALITY="high_quality" to:
QUALITY="low_quality"      # 480p, 15fps (fastest)
QUALITY="medium_quality"   # 720p, 30fps (medium)
QUALITY="high_quality"     # 1080p, 60fps (default)
QUALITY="4k_quality"       # 2160p, 60fps (slowest)
```

## 7. Troubleshooting

**FFmpeg error?**
- macOS: `brew install ffmpeg`
- Ubuntu: `sudo apt-get install ffmpeg`
- Windows: Download from https://ffmpeg.org/

**ModuleNotFoundError?**
- Activate venv: `source venv/bin/activate`
- Install deps: `pip install -r requirements.txt`

**Slow rendering?**
- Use lower quality for previews
- Render single scenes instead of all

## 8. Next Steps

1. Edit scene files in `scenes/` directory
2. Use utils functions for consistent styling
3. Test with low quality first
4. Render to high quality when satisfied
5. Output videos are in `output/videos/`
