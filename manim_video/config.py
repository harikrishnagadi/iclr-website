"""
HierLoc Manim Configuration
Color scheme and styling from website design
"""

from manim import config as manim_config

# Website Color Palette
COLORS = {
    "ink": "#0a0a0f",
    "accent": "#e8a838",
    "gold_light": "#f5cc7a",
    "text": "#e8e4da",
    "text_muted": "#8c8a84",
    "surface": "#14141e",
    "bg": "#0a0a0f",
    "fg": "#e8e4da",
}

# Font Families - Modern Apple Fonts
FONTS = {
    "serif": "Optima",  # Modern serif similar to SF Pro
    "sans": "Helvetica Neue",  # Clean modern sans-serif (Apple standard)
    "mono": "Menlo",  # Apple's modern monospace
}

# Animation Easing Functions
EASING = {
    "ease_in": lambda t: t ** 2,
    "ease_out": lambda t: 1 - (1 - t) ** 2,
    "ease_in_out": lambda t: 3 * t ** 2 - 2 * t ** 3,
    "ease_in_cubic": lambda t: t ** 3,
    "ease_out_cubic": lambda t: 1 - (1 - t) ** 3,
}

# Manim Configuration
def setup_manim_config(quality="high_quality", resolution="1920x1080"):
    """
    Setup Manim configuration with HierLoc styling

    Args:
        quality: "low_quality", "medium_quality", "high_quality", "4k_quality"
        resolution: resolution string like "1920x1080"
    """
    # Background and foreground colors
    manim_config.background_color = COLORS["bg"]

    # Quality settings
    if quality == "low_quality":
        manim_config.pixel_height = 480
        manim_config.pixel_width = 854
        manim_config.frame_rate = 15
    elif quality == "medium_quality":
        manim_config.pixel_height = 720
        manim_config.pixel_width = 1280
        manim_config.frame_rate = 30
    elif quality == "high_quality":
        manim_config.pixel_height = 1080
        manim_config.pixel_width = 1920
        manim_config.frame_rate = 60
    elif quality == "4k_quality":
        manim_config.pixel_height = 2160
        manim_config.pixel_width = 3840
        manim_config.frame_rate = 60

    # Output directory
    manim_config.media_dir = "./output"
    manim_config.log_to_file = False

    return manim_config


if __name__ == "__main__":
    print("HierLoc Manim Configuration")
    print(f"Colors: {COLORS}")
    print(f"Fonts: {FONTS}")
