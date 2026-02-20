"""
Scene 2: The Problem - Scale and Inefficiency
Duration: ~36 seconds
Purpose: Show why naive geolocation fails at scale

Clean visualization with:
- Organized grid of dots representing scale
- Clear search pattern showing inefficiency
- Minimal text labels
"""

from manim import *
import numpy as np
from config import COLORS, FONTS, setup_manim_config
from utils import create_serif_title, create_sans_body

setup_manim_config(quality="h")


class Scene2Problem(Scene):
    """Problem visualization with clean, intentional geometry"""

    def construct(self):
        self.camera.background_color = COLORS["bg"]

        # ============================================================
        # TITLE: "The Problem"
        # ============================================================
        title = create_serif_title("The Problem", font_size=64)
        title.to_edge(UP, buff=0.4)
        self.play(FadeIn(title, run_time=1.0))
        self.wait(0.5)

        # ============================================================
        # SCALE VISUALIZATION: Grid of dots representing millions
        # ============================================================
        # Create organized grid: 12x12 = 144 dots visible (represents millions)
        dot_grid = VGroup()
        grid_size = 12
        spacing = 0.35

        for i in range(grid_size):
            for j in range(grid_size):
                # Positions arranged in clean grid
                x = (i - grid_size/2) * spacing
                y = (j - grid_size/2) * spacing

                dot = Dot(
                    point=[x, y, 0],
                    radius=0.06,
                    color=COLORS["text_muted"],
                    fill_opacity=0.7
                )
                dot_grid.add(dot)

        # Center grid in scene
        dot_grid.move_to([0, 0.5, 0])

        # Animate grid appearing
        self.play(
            FadeIn(dot_grid, run_time=1.2),
            rate_func=rate_functions.ease_in_out_cubic
        )
        self.wait(1.0)

        # ============================================================
        # SCALE LABEL: "5M+ images"
        # ============================================================
        scale_label = create_sans_body("5M+ images", font_size=32)
        scale_label.next_to(dot_grid, DOWN, buff=0.8)
        scale_label.set_color(COLORS["text_muted"])

        self.play(FadeIn(scale_label, run_time=0.6))
        self.wait(0.8)

        # ============================================================
        # HIGHLIGHT ONE TEST IMAGE: Center dot with gold glow
        # ============================================================
        test_dot = Dot(
            point=[0, 0.5, 0],
            radius=0.12,
            color=COLORS["accent"],
            fill_opacity=1.0
        )

        # Create glow effect (animated circle around test dot)
        glow = Circle(
            radius=0.25,
            color=COLORS["accent"],
            stroke_width=2,
            fill_opacity=0,
            stroke_opacity=0.8
        )
        glow.move_to(test_dot.get_center())

        self.play(
            Create(test_dot, run_time=0.6),
            Create(glow, run_time=0.6)
        )
        self.wait(0.5)

        # ============================================================
        # SEARCH ARROWS: Fan out showing comparison
        # ============================================================
        # Create arrows pointing from test dot to surrounding dots
        num_arrows = 8
        arrow_length = 1.5

        arrows = VGroup()
        for i in range(num_arrows):
            angle = (2 * np.pi * i) / num_arrows

            # Start from test dot
            start = [0, 0.5, 0]
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
                stroke_width=2,
                tip_length=0.2
            )
            arrows.add(arrow)

        # Animate arrows appearing in sequence
        for arrow in arrows:
            self.play(Create(arrow, run_time=0.3))
        self.wait(0.8)

        # ============================================================
        # PROBLEM LABELS: Pain points
        # ============================================================
        problems = VGroup()

        # Problem 1: "Slow"
        p1 = create_sans_body("Slow", font_size=28)
        p1.to_edge(UP, buff=2.0)
        p1.to_edge(LEFT, buff=0.5)
        p1.set_color(COLORS["text_muted"])

        # Problem 2: "Memory-heavy"
        p2 = create_sans_body("Memory\nintensive", font_size=28)
        p2.to_edge(UP, buff=2.0)
        p2.to_edge(RIGHT, buff=0.5)
        p2.set_color(COLORS["text_muted"])

        # Problem 3: "No structure"
        p3 = create_sans_body("No geographic\nstructure", font_size=28)
        p3.to_edge(DOWN, buff=1.2)
        p3.set_color(COLORS["text_muted"])

        problems.add(p1, p2, p3)

        # Animate labels appearing
        for label in problems:
            self.play(FadeIn(label, run_time=0.5))
            self.wait(0.3)

        self.wait(1.5)

        # ============================================================
        # FADE OUT FOR TRANSITION
        # ============================================================
        self.play(
            FadeOut(title, dot_grid, test_dot, glow, arrows, scale_label, problems, run_time=1.0)
        )
        self.wait(0.5)
