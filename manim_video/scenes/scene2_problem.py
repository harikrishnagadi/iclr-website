"""
Scene 2: THE PROBLEM - Naive Approach Fails at Scale
Duration: ~36 seconds
Purpose: Show why traditional methods don't work well

Grounded in paper:
- O(N) comparison complexity against millions of images
- Memory intensive (5M+ embeddings)
- Ignores geographic hierarchy
"""

from manim import *
import numpy as np
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from config import COLORS, FONTS, setup_manim_config
from utils import (
    create_serif_title,
    create_sans_body,
    create_mono_code,
    apply_color,
    create_accent_highlight,
    get_easing_function
)
from layout import ObjectPositioner

setup_manim_config(quality="high_quality")


class Scene2Problem(Scene):
    """Problem visualization: Scale and complexity"""

    def construct(self):
        self.camera.background_color = COLORS["bg"]

        # ============================================================
        # BACKGROUND: Beautiful geometric pattern (matching Scene 1)
        # ============================================================
        background_elements = VGroup()

        # Large concentric circles (subtle, geometric)
        for radius in [1.5, 2.5, 3.5, 4.5]:
            circle = Circle(
                radius=radius,
                color=COLORS["accent"],
                stroke_opacity=0.08,
                stroke_width=1,
                fill_opacity=0
            )
            background_elements.add(circle)

        # Radial lines (8 directions, subtle)
        for angle in np.linspace(0, 2*np.pi, 8, endpoint=False):
            line = Line(
                start=[0, 0, 0],
                end=[4.5 * np.cos(angle), 4.5 * np.sin(angle), 0],
                color=COLORS["accent"],
                stroke_opacity=0.06,
                stroke_width=0.8
            )
            background_elements.add(line)

        # Some decorative dots at key points (very subtle)
        for angle in np.linspace(0, 2*np.pi, 12, endpoint=False):
            dot = Dot(
                point=[3.5 * np.cos(angle), 3.5 * np.sin(angle), 0],
                radius=0.04,
                color=COLORS["accent"],
                fill_opacity=0.15
            )
            background_elements.add(dot)

        background_elements.center()
        self.add(background_elements)

        # ============================================================
        # HEADER & PROGRESS LINE (Top of Scene)
        # ============================================================
        # Full-width divider line below header
        divider_line = Line(
            start=[-7.0, 3.2, 0],
            end=[7.0, 3.2, 0],
            color=COLORS["text_muted"],
            stroke_width=1.5,
            stroke_opacity=0.3
        )

        # Progress dots spread evenly across entire line
        # Scene 2 is the second scene, so second dot should be highlighted yellow
        progress_dots = VGroup()
        num_scenes = 5
        dot_x_positions = np.linspace(-6.8, 6.8, num_scenes)
        for i, x_pos in enumerate(dot_x_positions):
            dot = Dot(
                point=[x_pos, 3.2, 0],
                radius=0.07,
                color=COLORS["gold_light"] if i == 1 else COLORS["text_muted"],
                fill_opacity=1.0 if i == 1 else 0.4
            )
            progress_dots.add(dot)

        # Header title "HierLoc"
        hierlock_header = Text(
            "HierLoc",
            font=FONTS["sans"],
            font_size=48,
            color=COLORS["accent"]
        )
        hierlock_header.move_to([-5.5, 3.6, 0])

        # Add header and progress line
        self.add(divider_line, progress_dots, hierlock_header)

        # ============================================================
        # SEQUENCE 1: Title (0-1s)
        # ============================================================
        title = create_sans_body(
            "The Problem",
            font_size=64,
            color=COLORS["text"]
        )
        title.move_to([0, 2.0, 0])

        self.play(FadeIn(title, run_time=1.0))
        self.wait(0.5)

        # ============================================================
        # SEQUENCE 2: Scale Visualization (1.5-8s)
        # ============================================================
        # Create organized grid representing 5M+ images
        # Grid: 14x14 = 196 dots (visual representation of scale)
        # Coordinates: Centered at origin, spacing 0.32
        dot_grid = VGroup()
        grid_size = 14
        spacing = 0.32

        # Create grid with precise coordinates
        for i in range(grid_size):
            for j in range(grid_size):
                # Offset to center the grid at [0, 0.3, 0]
                x = (i - grid_size/2) * spacing + 0.05
                y = (j - grid_size/2) * spacing + 0.3

                dot = Dot(
                    point=[x, y, 0],
                    radius=0.05,
                    color=COLORS["text_muted"],
                    fill_opacity=0.6
                )
                dot_grid.add(dot)

        self.play(FadeIn(dot_grid, run_time=1.2, rate_func=rate_functions.ease_in_out_cubic))
        self.wait(0.8)

        # Label: "5M+ Images" positioned below grid
        scale_label = create_sans_body(
            "5,000,000+ Images",
            font_size=28,
            color=COLORS["accent"]
        )
        scale_label.move_to([0, -2.8, 0])

        self.play(FadeIn(scale_label, run_time=0.6))
        self.wait(0.8)

        # ============================================================
        # SEQUENCE 3: Test Image Highlight (8-11s)
        # ============================================================
        # Center dot represents the query image
        # Coordinates: [0.05, 0.3, 0] (center of grid)
        test_dot = Dot(
            point=[0.05, 0.3, 0],
            radius=0.15,
            color=COLORS["accent"],
            fill_opacity=1.0,
            z_index=5
        )

        # Glow effect around test dot
        glow = Circle(
            radius=0.3,
            color=COLORS["accent"],
            stroke_width=2,
            fill_opacity=0,
            stroke_opacity=0.7,
            z_index=4
        )
        glow.move_to([0.05, 0.3, 0])

        self.play(
            Create(test_dot, run_time=0.6),
            Create(glow, run_time=0.6)
        )
        self.wait(0.7)

        # Question label
        question_label = create_sans_body(
            "Your image",
            font_size=24,
            color=COLORS["gold_light"]
        )
        question_label.next_to(glow, UP, buff=0.3)

        self.play(FadeIn(question_label, run_time=0.4))
        self.wait(0.8)

        # ============================================================
        # SEQUENCE 4: Search Pattern (11-15s)
        # ============================================================
        # Show comparisons: arrows radiating from center
        # 12 arrows for comprehensive visualization
        num_arrows = 12
        arrows = VGroup()

        for i in range(num_arrows):
            angle = (2 * np.pi * i) / num_arrows
            start = [0.05, 0.3, 0]
            arrow_length = 2.2

            end = [
                start[0] + arrow_length * np.cos(angle),
                start[1] + arrow_length * np.sin(angle),
                0
            ]

            arrow = Arrow(
                start=start,
                end=end,
                buff=0.15,
                color=COLORS["accent"],
                stroke_width=2.5,
                tip_length=0.18
            )
            arrows.add(arrow)

        # Animate arrows appearing in bursts
        for i in range(0, num_arrows, 3):
            for arrow in arrows[i:i+3]:
                self.play(Create(arrow, run_time=0.25), lag_ratio=0.1)
        self.wait(1.0)

        # ============================================================
        # SEQUENCE 5: Problem Labels (15-21s)
        # ============================================================
        # Clear some space first
        self.play(FadeOut(question_label, run_time=0.3))

        # Problem 1: "Slow" - TOP LEFT
        p1_title = create_sans_body("Slow", font_size=26, color=COLORS["accent"])
        p1_desc = create_sans_body("O(N) comparisons", font_size=18, color=COLORS["text_muted"])
        p1 = VGroup(p1_title, p1_desc).arrange(DOWN, buff=0.15)

        # Problem 2: "Memory-Intensive" - TOP RIGHT
        p2_title = create_sans_body("Memory", font_size=26, color=COLORS["accent"])
        p2_desc = create_sans_body("5M+ embeddings", font_size=18, color=COLORS["text_muted"])
        p2 = VGroup(p2_title, p2_desc).arrange(DOWN, buff=0.15)

        # Problem 3: "No Structure" - BOTTOM CENTER
        p3_title = create_sans_body("No Structure", font_size=26, color=COLORS["accent"])
        p3_desc = create_sans_body("Geography ignored", font_size=18, color=COLORS["text_muted"])
        p3 = VGroup(p3_title, p3_desc).arrange(DOWN, buff=0.15)

        # Use layout system to position problem labels
        layout_spec = [
            {'object': p1, 'name': 'Problem 1', 'target_y': 2.2, 'center_x': -2.8, 'width': 2.0, 'height': 1.0},
            {'object': p2, 'name': 'Problem 2', 'target_y': 2.2, 'center_x': 2.8, 'width': 2.0, 'height': 1.0},
            {'object': p3, 'name': 'Problem 3', 'target_y': -2.2, 'center_x': 0, 'width': 2.5, 'height': 1.0},
        ]

        layout_results = ObjectPositioner.layout_objects(self, layout_spec)

        self.play(FadeIn(p1, p2, p3, run_time=0.8))
        self.wait(1.5)

        # ============================================================
        # SEQUENCE 6: Impact Statement (21-28s)
        # ============================================================
        impact = create_sans_body(
            "This doesn't scale.",
            font_size=36,
            color=COLORS["accent"]
        )

        # Position impact statement safely
        impact_bounds = ObjectPositioner.get_bounds(impact)
        safe_y, found, _ = ObjectPositioner.find_safe_y_position(
            target_height=0.6,
            existing_bounds_list=[
                ObjectPositioner.get_bounds(p1),
                ObjectPositioner.get_bounds(p2),
                ObjectPositioner.get_bounds(p3),
            ],
            start_y=-3.5,
            direction='down',
            center_x=0,
            h_spacing=0.2,
            v_spacing=0.3
        )

        if found:
            impact.move_to([0, safe_y, 0])
        else:
            impact.move_to([0, -3.5, 0])

        self.play(FadeIn(impact, run_time=0.7))
        self.wait(1.5)

        # ============================================================
        # SEQUENCE 7: Transition (28-36s)
        # ============================================================
        self.play(
            FadeOut(title, dot_grid, test_dot, glow, scale_label, arrows, p1, p2, p3, impact, background_elements, divider_line, progress_dots, hierlock_header, run_time=1.2)
        )
        self.wait(0.5)
