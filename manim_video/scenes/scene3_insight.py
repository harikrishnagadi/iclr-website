"""
Scene 3: THE INSIGHT - Geographic Hierarchy & Hyperbolic Geometry
Duration: ~39 seconds
Purpose: Reveal that geography is hierarchical + introduce hyperbolic space

Key insights from paper:
- Geographic entities form a hierarchy (countries > regions > cities)
- Euclidean space compresses deep hierarchies
- Hyperbolic space has exponential volume = perfect for hierarchy
"""

from manim import *
import numpy as np
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from config import COLORS, FONTS, setup_manim_config
from utils import create_serif_title, create_sans_body
from layout import ObjectPositioner

setup_manim_config(quality="h")


class Scene3Insight(Scene):
    """Key insight: Hierarchy and hyperbolic geometry"""

    def construct(self):
        self.camera.background_color = COLORS["bg"]

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
        # Scene 3 is the third scene, so third dot should be highlighted yellow
        progress_dots = VGroup()
        num_scenes = 5
        dot_x_positions = np.linspace(-6.8, 6.8, num_scenes)
        for i, x_pos in enumerate(dot_x_positions):
            dot = Dot(
                point=[x_pos, 3.2, 0],
                radius=0.07,
                color=COLORS["gold_light"] if i == 2 else COLORS["text_muted"],
                fill_opacity=1.0 if i == 2 else 0.4
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
        title = Text(
            "The Insight",
            font=FONTS["sans"],
            font_size=64,
            color=COLORS["text"]
        )
        title.move_to([0, 2.0, 0])

        self.play(FadeIn(title, run_time=1.0))
        self.wait(0.5)

        # ============================================================
        # SEQUENCE 2: Hierarchy Revelation (1.5-13s)
        # ============================================================
        # Start with smallest unit: City
        city_box = Rectangle(
            width=2.0, height=0.6,
            stroke_color=COLORS["accent"],
            stroke_width=2.5,
            fill_opacity=0.08,
            fill_color=COLORS["accent"]
        )
        city_box.move_to([0, 1.0, 0])

        city_label = Text(
            "Paris",
            font=FONTS["sans"],
            font_size=28,
            color=COLORS["accent"],
            
        )
        city_label.move_to(city_box.get_center())

        self.play(Create(city_box, run_time=0.7))
        self.play(FadeIn(city_label, run_time=0.4))
        self.wait(0.8)

        # Add Region layer
        region_box = Rectangle(
            width=3.2, height=1.2,
            stroke_color=COLORS["accent"],
            stroke_width=2.5,
            fill_opacity=0.04,
            fill_color=COLORS["accent"]
        )
        region_box.move_to([0, 1.0, 0])

        region_label = Text(
            "Île-de-France",
            font=FONTS["sans"],
            font_size=22,
            color=COLORS["gold_light"]
        )
        region_label.next_to(region_box, UP, buff=0.25)

        self.play(Create(region_box, run_time=0.7))
        self.play(FadeIn(region_label, run_time=0.4))
        self.wait(0.8)

        # Add Country layer
        country_box = Rectangle(
            width=4.4, height=1.8,
            stroke_color=COLORS["accent"],
            stroke_width=2.5,
            fill_opacity=0.02,
            fill_color=COLORS["accent"]
        )
        country_box.move_to([0, 1.0, 0])

        country_label = Text(
            "France",
            font=FONTS["sans"],
            font_size=20,
            color=COLORS["gold_light"]
        )
        country_label.next_to(country_box, UP, buff=0.3)

        self.play(Create(country_box, run_time=0.7))
        self.play(FadeIn(country_label, run_time=0.4))
        self.wait(0.8)

        # Add Continent layer
        continent_box = Rectangle(
            width=5.6, height=2.6,
            stroke_color=COLORS["accent"],
            stroke_width=2.5,
            fill_opacity=0,
            fill_color=COLORS["accent"]
        )
        continent_box.move_to([0, 1.0, 0])

        continent_label = Text(
            "Europe",
            font=FONTS["sans"],
            font_size=18,
            color=COLORS["gold_light"]
        )
        continent_label.next_to(continent_box, UP, buff=0.35)

        self.play(Create(continent_box, run_time=0.7))
        self.play(FadeIn(continent_label, run_time=0.4))
        self.wait(1.2)

        # ============================================================
        # SEQUENCE 3: The Problem in Euclidean Space (13-22s)
        # ============================================================
        problem_text = Text(
            "In Euclidean space:\nentities at deep levels\nget compressed together",
            font=FONTS["sans"],
            font_size=28,
            color=COLORS["text_muted"],
            line_spacing=1.3
        )

        # Position below hierarchy boxes
        safe_y, found, _ = ObjectPositioner.find_safe_y_position(
            target_height=1.2,
            existing_bounds_list=[],
            start_y=-2.3,
            direction='down',
            center_x=0,
            h_spacing=0.2,
            v_spacing=0.3
        )
        problem_text.move_to([0, safe_y if found else -2.3, 0])

        self.play(
            FadeOut(city_label, region_label, country_label, continent_label, run_time=0.5)
        )
        self.wait(0.2)
        self.play(FadeIn(problem_text, run_time=0.6))
        self.wait(1.5)

        # ============================================================
        # SEQUENCE 4: The Solution - Hyperbolic Space (22-35s)
        # ============================================================
        # Clear the boxes
        self.play(
            FadeOut(city_box, region_box, country_box, continent_box, problem_text, run_time=0.6)
        )
        self.wait(0.3)

        # Introduce Hyperbolic Space (Poincaré disk)
        poincare_circle = Circle(
            radius=1.4,
            color=COLORS["accent"],
            stroke_width=3,
            fill_opacity=0.06,
            fill_color=COLORS["accent"]
        )
        poincare_circle.move_to([0, 0.8, 0])

        solution_title = Text(
            "Hyperbolic Space",
            font=FONTS["sans"],
            font_size=32,
            color=COLORS["accent"],
            
        )
        solution_title.move_to([0, 2.4, 0])

        solution_desc = Text(
            "Exponential volume growth\n= Perfect for hierarchy",
            font=FONTS["sans"],
            font_size=24,
            color=COLORS["gold_light"],
            line_spacing=1.2
        )
        solution_desc.move_to([0, -2.2, 0])

        self.play(Create(poincare_circle, run_time=0.9))
        self.play(FadeIn(solution_title, run_time=0.5))
        self.wait(0.5)
        self.play(FadeIn(solution_desc, run_time=0.6))
        self.wait(2.0)

        # ============================================================
        # SEQUENCE 5: Transition (35-39s)
        # ============================================================
        self.play(
            FadeOut(title, poincare_circle, solution_title, solution_desc, run_time=1.0)
        )
        self.wait(0.5)
