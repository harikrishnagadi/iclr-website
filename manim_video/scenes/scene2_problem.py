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
from config import COLORS, FONTS, setup_manim_config
from utils import create_serif_title, create_sans_body

setup_manim_config(quality="h")


class Scene2Problem(Scene):
    """Problem visualization: Scale and complexity"""

    def construct(self):
        self.camera.background_color = COLORS["bg"]

        # ============================================================
        # SEQUENCE 1: Title (0-1s)
        # ============================================================
        title = Text(
            "The Problem",
            font=FONTS["sans"],
            font_size=64,
            color=COLORS["text"],
            
        )
        title.to_edge(UP, buff=0.5)

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
        scale_label = Text(
            "5,000,000+ Images",
            font=FONTS["sans"],
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
        question_label = Text(
            "Your image",
            font=FONTS["sans"],
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
                tip_length=0.18,
                max_tip_angle=0.3
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
        p1_title = Text("Slow", font=FONTS["sans"], font_size=26, color=COLORS["accent"], )
        p1_desc = Text("O(N) comparisons", font=FONTS["sans"], font_size=18, color=COLORS["text_muted"])
        p1 = VGroup(p1_title, p1_desc).arrange(DOWN, buff=0.15)
        p1.move_to([-2.8, 2.2, 0])

        # Problem 2: "Memory-Intensive" - TOP RIGHT
        p2_title = Text("Memory", font=FONTS["sans"], font_size=26, color=COLORS["accent"], )
        p2_desc = Text("5M+ embeddings", font=FONTS["sans"], font_size=18, color=COLORS["text_muted"])
        p2 = VGroup(p2_title, p2_desc).arrange(DOWN, buff=0.15)
        p2.move_to([2.8, 2.2, 0])

        # Problem 3: "No Structure" - BOTTOM CENTER
        p3_title = Text("No Structure", font=FONTS["sans"], font_size=26, color=COLORS["accent"], )
        p3_desc = Text("Geography ignored", font=FONTS["sans"], font_size=18, color=COLORS["text_muted"])
        p3 = VGroup(p3_title, p3_desc).arrange(DOWN, buff=0.15)
        p3.move_to([0, -2.2, 0])

        self.play(FadeIn(p1, p2, p3, run_time=0.8))
        self.wait(1.5)

        # ============================================================
        # SEQUENCE 6: Impact Statement (21-28s)
        # ============================================================
        impact = Text(
            "This doesn't scale.",
            font=FONTS["sans"],
            font_size=36,
            color=COLORS["accent"],
            
        )
        impact.move_to([0, -3.5, 0])

        self.play(FadeIn(impact, run_time=0.7))
        self.wait(1.5)

        # ============================================================
        # SEQUENCE 7: Transition (28-36s)
        # ============================================================
        self.play(
            FadeOut(title, dot_grid, test_dot, glow, scale_label, arrows, p1, p2, p3, impact, run_time=1.2)
        )
        self.wait(0.5)
