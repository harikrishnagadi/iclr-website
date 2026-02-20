"""
HierLoc Manim Utilities
Helper functions for creating styled animations
"""

from manim import *
from config import COLORS, FONTS, EASING


def create_serif_title(text, **kwargs):
    """
    Create a styled serif title using DM Serif Display

    Args:
        text: Title text
        **kwargs: Additional arguments for Text object

    Returns:
        Manim Text object with serif styling
    """
    default_kwargs = {
        "font": FONTS["serif"],
        "color": COLORS["text"],
        "font_size": 60,
    }
    default_kwargs.update(kwargs)
    return Text(text, **default_kwargs)


def create_sans_body(text, **kwargs):
    """
    Create styled body text using Syne sans-serif

    Args:
        text: Body text
        **kwargs: Additional arguments for Text object

    Returns:
        Manim Text object with sans-serif styling
    """
    default_kwargs = {
        "font": FONTS["sans"],
        "color": COLORS["text"],
        "font_size": 36,
    }
    default_kwargs.update(kwargs)
    return Text(text, **default_kwargs)


def create_mono_code(text, **kwargs):
    """
    Create styled code text using DM Mono

    Args:
        text: Code text
        **kwargs: Additional arguments for Text object

    Returns:
        Manim Text object with monospace styling
    """
    default_kwargs = {
        "font": FONTS["mono"],
        "color": COLORS["accent"],
        "font_size": 24,
    }
    default_kwargs.update(kwargs)
    return Text(text, **default_kwargs)


def apply_color(mobject, color_key):
    """
    Apply a color from the palette to a mobject

    Args:
        mobject: Manim mobject
        color_key: Key from COLORS dictionary

    Returns:
        mobject with applied color
    """
    if color_key in COLORS:
        mobject.set_color(COLORS[color_key])
    return mobject


def create_hierarchy_visualization(levels, level_width=2):
    """
    Create a hierarchy visualization for HierLoc

    Args:
        levels: List of level names from root to leaf
        level_width: Width of each level box

    Returns:
        VGroup containing the hierarchy visualization
    """
    hierarchy_group = VGroup()

    for i, level in enumerate(levels):
        y_pos = 3 - (i * 1.5)

        # Create level box
        box = Rectangle(
            width=level_width,
            height=0.8,
            fill_color=COLORS["accent"],
            fill_opacity=0.3,
            stroke_color=COLORS["accent"],
            stroke_width=2,
        )
        box.move_to([0, y_pos, 0])

        # Create level text
        level_text = Text(
            level,
            font=FONTS["sans"],
            color=COLORS["text"],
            font_size=20,
        )
        level_text.move_to(box.get_center())

        # Add connection line if not first level
        if i > 0:
            prev_y = 3 - ((i - 1) * 1.5)
            line = Line(
                start=[0, prev_y - 0.4, 0],
                end=[0, y_pos + 0.4, 0],
                color=COLORS["text_muted"],
                stroke_width=1,
            )
            hierarchy_group.add(line)

        hierarchy_group.add(box, level_text)

    return hierarchy_group


def create_accent_highlight(mobject, scale_factor=1.2):
    """
    Create an accent highlight animation for a mobject

    Args:
        mobject: Manim mobject to highlight
        scale_factor: Scale factor for the highlight

    Returns:
        Highlight rectangle around mobject
    """
    highlight = Rectangle(
        width=mobject.width * scale_factor,
        height=mobject.height * scale_factor,
        fill_opacity=0,
        stroke_color=COLORS["gold_light"],
        stroke_width=3,
    )
    highlight.move_to(mobject.get_center())
    return highlight


def get_easing_function(easing_type="ease_in_out"):
    """
    Get an easing function by name

    Args:
        easing_type: Key from EASING dictionary

    Returns:
        Easing function
    """
    return EASING.get(easing_type, EASING["ease_in_out"])


if __name__ == "__main__":
    print("HierLoc Manim Utilities")
    print(f"Available fonts: {FONTS}")
    print(f"Available colors: {list(COLORS.keys())}")
    print(f"Available easing: {list(EASING.keys())}")
