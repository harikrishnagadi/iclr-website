"""
Scene 3: The Insight - Geographic Hierarchy
Duration: ~39 seconds
Purpose: Reveal that geography is hierarchical and hyperbolic space is the solution

Clean design with:
- Nested rectangles showing Paris ⊂ France ⊂ Europe ⊂ Earth
- Clear tree structure showing exponential branching
- Poincaré disk hint for hyperbolic geometry
"""

from manim import *
import numpy as np
from config import COLORS, FONTS, setup_manim_config
from utils import create_serif_title, create_sans_body

setup_manim_config(quality="h")


class Scene3Insight(Scene):
    """Hierarchy insight with clean, intentional geometry"""

    def construct(self):
        self.camera.background_color = COLORS["bg"]

        # ============================================================
        # TITLE: "Geographic Hierarchy"
        # ============================================================
        title = create_serif_title("Geographic Hierarchy", font_size=64)
        title.to_edge(UP, buff=0.4)
        self.play(FadeIn(title, run_time=1.0))
        self.wait(0.5)

        # ============================================================
        # PART A: Nested Containment (Paris example)
        # ============================================================
        # Start with smallest: City
        city_box = Rectangle(
            width=1.8, height=0.5,
            stroke_color=COLORS["accent"],
            stroke_width=2,
            fill_opacity=0.1,
            fill_color=COLORS["accent"]
        )
        city_box.move_to([0, 0, 0])
        city_label = create_sans_body("Paris", font_size=28)
        city_label.move_to(city_box.get_center())

        self.play(Create(city_box, run_time=0.6))
        self.play(FadeIn(city_label, run_time=0.4))
        self.wait(0.8)

        # Add Country layer
        country_box = Rectangle(
            width=3.0, height=1.0,
            stroke_color=COLORS["accent"],
            stroke_width=2,
            fill_opacity=0.05,
            fill_color=COLORS["accent"]
        )
        country_box.move_to([0, 0, 0])

        country_label = create_sans_body("France", font_size=24)
        country_label.next_to(country_box, UP, buff=0.15)
        country_label.set_color(COLORS["gold_light"])

        self.play(
            Create(country_box, run_time=0.6),
            FadeIn(country_label, run_time=0.4)
        )
        self.wait(0.8)

        # Add Continent layer
        continent_box = Rectangle(
            width=4.5, height=1.8,
            stroke_color=COLORS["accent"],
            stroke_width=2,
            fill_opacity=0.02,
            fill_color=COLORS["accent"]
        )
        continent_box.move_to([0, 0, 0])

        continent_label = create_sans_body("Europe", font_size=22)
        continent_label.next_to(continent_box, UP, buff=0.2)
        continent_label.set_color(COLORS["gold_light"])

        self.play(
            Create(continent_box, run_time=0.6),
            FadeIn(continent_label, run_time=0.4)
        )
        self.wait(0.8)

        # Add World layer
        world_box = Rectangle(
            width=6.0, height=2.8,
            stroke_color=COLORS["accent"],
            stroke_width=2,
            fill_opacity=0.0,
            fill_color=COLORS["accent"]
        )
        world_box.move_to([0, 0, 0])

        world_label = create_sans_body("Earth", font_size=20)
        world_label.next_to(world_box, UP, buff=0.25)
        world_label.set_color(COLORS["gold_light"])

        self.play(
            Create(world_box, run_time=0.6),
            FadeIn(world_label, run_time=0.4)
        )
        self.wait(1.2)

        # ============================================================
        # CLEAR SCENE FOR PART B
        # ============================================================
        self.play(
            FadeOut(city_label, country_label, continent_label, world_label,
                   city_box, country_box, continent_box, world_box, run_time=0.8)
        )
        self.wait(0.5)

        # ============================================================
        # PART B: Tree Structure - Hierarchical Branching
        # ============================================================
        # Earth at top
        earth = Dot(radius=0.08, color=COLORS["accent"])
        earth.move_to([0, 2.5, 0])

        earth_label = create_sans_body("Earth", font_size=20)
        earth_label.next_to(earth, UP, buff=0.2)
        earth_label.set_color(COLORS["accent"])

        self.play(Create(earth, run_time=0.4))
        self.play(FadeIn(earth_label, run_time=0.3))
        self.wait(0.4)

        # Level 1: Continents (7 represented as 5 visible)
        continents = VGroup()
        continent_positions = [
            [-1.5, 1.2, 0], [-0.5, 1.2, 0], [0.5, 1.2, 0], [1.5, 1.2, 0], [2.5, 1.2, 0]
        ]

        for i, pos in enumerate(continent_positions):
            dot = Dot(radius=0.06, color=COLORS["text_muted"])
            dot.move_to(pos)
            continents.add(dot)

            # Connect to Earth with line
            line = Line(earth.get_center(), dot.get_center(),
                       color=COLORS["text_muted"], stroke_width=1, stroke_opacity=0.6)
            self.play(Create(line, run_time=0.2))
            self.play(Create(dot, run_time=0.15))

        self.wait(0.6)

        # Level 2: Countries (3 under one continent)
        countries = VGroup()
        country_positions = [
            [-1.8, 0.2, 0], [-1.5, 0.2, 0], [-1.2, 0.2, 0]
        ]

        for pos in country_positions:
            dot = Dot(radius=0.04, color=COLORS["text_muted"])
            dot.move_to(pos)
            countries.add(dot)

            # Connect to parent continent
            line = Line(continent_positions[0], dot.get_center(),
                       color=COLORS["text_muted"], stroke_width=1, stroke_opacity=0.4)
            self.play(Create(line, run_time=0.2))
            self.play(Create(dot, run_time=0.1))

        self.wait(0.6)

        # Add exponential growth label
        exponential_label = create_sans_body(
            "Exponential\nbranching",
            font_size=26
        )
        exponential_label.to_edge(RIGHT, buff=0.4)
        exponential_label.to_edge(DOWN, buff=1.0)
        exponential_label.set_color(COLORS["accent"])

        self.play(FadeIn(exponential_label, run_time=0.5))
        self.wait(1.0)

        # ============================================================
        # PART C: Euclidean Problem
        # ============================================================
        # Show that deep levels get cramped in Euclidean space
        crowding_label = create_sans_body(
            "In Euclidean space:\ncities get cramped",
            font_size=28
        )
        crowding_label.move_to([0, -2.0, 0])
        crowding_label.set_color(COLORS["text_muted"])

        self.play(
            FadeOut(earth, earth_label, continents, countries, exponential_label, run_time=0.6)
        )
        self.wait(0.3)
        self.play(FadeIn(crowding_label, run_time=0.5))
        self.wait(0.8)

        # ============================================================
        # PART D: Hyperbolic Solution Hint
        # ============================================================
        # Draw a circle (Poincaré disk representation)
        poincare = Circle(
            radius=1.2,
            color=COLORS["accent"],
            stroke_width=2,
            fill_opacity=0.05,
            fill_color=COLORS["accent"]
        )
        poincare.move_to([0, 0, 0])

        solution_label = create_sans_body(
            "Hyperbolic space:\nexponential room",
            font_size=28
        )
        solution_label.move_to([0, -2.0, 0])
        solution_label.set_color(COLORS["gold_light"])

        self.play(
            FadeOut(crowding_label, run_time=0.4),
            FadeIn(poincare, run_time=0.8)
        )
        self.wait(0.5)
        self.play(FadeIn(solution_label, run_time=0.5))
        self.wait(2.0)

        # ============================================================
        # FADE OUT FOR TRANSITION
        # ============================================================
        self.play(
            FadeOut(title, poincare, solution_label, run_time=1.0)
        )
        self.wait(0.5)
