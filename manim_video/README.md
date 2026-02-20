# HierLoc Manim Video Project

A Manim-based animation project for creating explanatory videos about the HierLoc hierarchical visual localization method. This project uses the website's design system and color palette for consistent visual branding.

## Project Structure

```
manim_video/
├── scenes/                    # Animation scene modules
│   ├── __init__.py
│   ├── scene1_hook.py        # Opening hook
│   ├── scene2_problem.py     # Problem statement
│   ├── scene3_insight.py     # Key insight
│   ├── scene4_solution.py    # Method explanation
│   └── scene5_results.py     # Results and impact
├── config.py                  # Color schemes, fonts, and Manim config
├── utils.py                   # Helper functions for styling and animations
├── render.sh                  # Rendering script
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## Setup Instructions

### 1. Create Virtual Environment

```bash
cd manim_video
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
# or
venv\Scripts\activate  # On Windows
```

### 2. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Install FFmpeg (Required by Manim)

**macOS:**
```bash
brew install ffmpeg
```

**Ubuntu/Debian:**
```bash
sudo apt-get install ffmpeg
```

**Windows:**
Download from https://ffmpeg.org/download.html or use:
```bash
choco install ffmpeg
```

## Usage

### Render a Single Scene

```bash
./render.sh scene1    # Renders Scene1Hook
./render.sh scene2    # Renders Scene2Problem
./render.sh scene3    # Renders Scene3Insight
./render.sh scene4    # Renders Scene4Solution
./render.sh scene5    # Renders Scene5Results
```

### Render All Scenes

```bash
./render.sh all
```

### Output

Rendered videos will be saved to the `output/` directory.

## Design System

The project uses colors and fonts from the HierLoc website:

### Colors
- **Ink:** `#0a0a0f` - Primary dark background
- **Accent:** `#e8a838` - Golden accent for highlights
- **Gold Light:** `#f5cc7a` - Light accent variant
- **Text:** `#e8e4da` - Primary text color
- **Text Muted:** `#8c8a84` - Secondary text
- **Surface:** `#14141e` - Alternative background

### Fonts
- **Serif:** DM Serif Display (titles)
- **Sans:** Syne (body text)
- **Mono:** DM Mono (code/technical)

### Easing Functions

Available easing functions in `utils.py`:
- `ease_in` - Accelerating from zero
- `ease_out` - Decelerating to zero
- `ease_in_out` - Accelerating then decelerating
- `ease_in_cubic` - Cubic acceleration
- `ease_out_cubic` - Cubic deceleration

## Creating New Scenes

1. Create a new file in `scenes/` directory
2. Import required modules:
   ```python
   from manim import *
   from config import COLORS, FONTS, setup_manim_config
   from utils import create_serif_title, create_sans_body, ...
   ```
3. Setup Manim config:
   ```python
   setup_manim_config(quality="high_quality")
   ```
4. Create your Scene class:
   ```python
   class YourScene(Scene):
       def construct(self):
           # Your animation code here
           pass
   ```
5. Update `render.sh` to include your new scene

## Utility Functions

### Text Creation
- `create_serif_title(text, **kwargs)` - Creates serif titles
- `create_sans_body(text, **kwargs)` - Creates body text
- `create_mono_code(text, **kwargs)` - Creates monospace code text

### Styling
- `apply_color(mobject, color_key)` - Applies colors from palette
- `create_accent_highlight(mobject, scale_factor)` - Creates highlights

### Visualization
- `create_hierarchy_visualization(levels, level_width)` - Creates hierarchy diagrams
- `get_easing_function(easing_type)` - Gets easing functions

## Configuration

Edit `config.py` to:
- Change colors
- Modify font families
- Add new easing functions
- Adjust Manim settings (resolution, frame rate, quality)

## Troubleshooting

### FFmpeg not found
Ensure FFmpeg is installed and in your system PATH.

### ModuleNotFoundError
Make sure you've activated the virtual environment and installed dependencies:
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### Slow rendering
Use lower quality for testing:
```bash
# Edit render.sh and change QUALITY="low_quality" for faster preview
```

## Next Steps

- Implement animation sequences in each scene
- Add custom camera movements and transitions
- Integrate real benchmark data and visualizations
- Add audio narration and music
- Composite scenes together into final video

## References

- [Manim Documentation](https://docs.manim.community/)
- [Manim Examples](https://github.com/3b1b/manim)
