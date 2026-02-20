"""
Scene 4: The Solution - HierLoc Approach
Duration: ~70 seconds
Purpose: Show how HierLoc encodes images and does hierarchical search

Clean design with:
- Left side: Image being encoded to embedding
- Right side: Entity space with hierarchical entities
- Center: Connection showing the matching process
- Bottom: Efficiency metrics
"""

from manim import *
import numpy as np
from config import COLORS, FONTS, setup_manim_config
from utils import create_serif_title, create_sans_body

setup_manim_config(quality="h")


class Scene4Solution(Scene):
    """Solution visualization with clean, intentional geometry"""

    def construct(self):
        self.camera.background_color = COLORS["bg"]

        # ============================================================
        # TITLE: "The Solution: HierLoc"
        # ============================================================
        title = create_serif_title("The Solution", font_size=64)
        title.to_edge(UP, buff=0.4)
        self.play(FadeIn(title, run_time=1.0))
        self.wait(0.5)

        # ============================================================
        # LEFT SIDE: Image → Encoding Pipeline
        # ============================================================
        # Image placeholder
        image_box = Rectangle(
            width=1.8, height=1.4,
            stroke_color=COLORS["accent"],
            stroke_width=2,
            fill_opacity=0.15,
            fill_color=COLORS["surface"]
        )
        image_box.move_to([-3.5, 1.0, 0])

        image_label = create_sans_body("Image", font_size=22)
        image_label.move_to(image_box.get_center())

        self.play(Create(image_box, run_time=0.6))
        self.play(FadeIn(image_label, run_time=0.4))
        self.wait(0.6)

        # Encoding arrow
        encode_arrow = Arrow(
            start=[-2.6, 1.0, 0],
            end=[-1.2, 1.0, 0],
            buff=0.1,
            color=COLORS["accent"],
            stroke_width=2,
            tip_length=0.15
        )

        encode_label = create_sans_body("Encode", font_size=18)
        encode_label.next_to(encode_arrow, UP, buff=0.1)
        encode_label.set_color(COLORS["accent"])

        self.play(Create(encode_arrow, run_time=0.5))
        self.play(FadeIn(encode_label, run_time=0.3))
        self.wait(0.4)

        # Embedding vector
        embedding_box = Rectangle(
            width=1.2, height=1.2,
            stroke_color=COLORS["accent"],
            stroke_width=2,
            fill_opacity=0.1,
            fill_color=COLORS["accent"]
        )
        embedding_box.move_to([-0.4, 1.0, 0])

        embedding_label = create_sans_body("v", font_size=28)
        embedding_label.move_to(embedding_box.get_center())
        embedding_label.set_color(COLORS["accent"])

        self.play(Create(embedding_box, run_time=0.6))
        self.play(FadeIn(embedding_label, run_time=0.4))
        self.wait(0.8)

        # ============================================================
        # RIGHT SIDE: Entity Space
        # ============================================================
        # Title for entity space
        entity_label = create_sans_body("Entity Space", font_size=24)
        entity_label.move_to([3.0, 2.2, 0])
        entity_label.set_color(COLORS["text_muted"])

        self.play(FadeIn(entity_label, run_time=0.4))
        self.wait(0.3)

        # Create hierarchical entity structure with dots
        entities = VGroup()

        # Level 0: Countries (3 dots)
        country_positions = [
            [2.2, 1.0, 0], [3.0, 1.0, 0], [3.8, 1.0, 0]
        ]
        for pos in country_positions:
            dot = Dot(radius=0.08, color=COLORS["accent"], fill_opacity=1.0)
            dot.move_to(pos)
            entities.add(dot)

        self.play(Create(entities[0], run_time=0.3))
        self.wait(0.2)
        self.play(Create(entities[1], run_time=0.3))
        self.wait(0.2)
        self.play(Create(entities[2], run_time=0.3))
        self.wait(0.4)

        # Level 1: Cities under first country (2 dots)
        city_positions = [
            [1.8, -0.3, 0], [2.6, -0.3, 0]
        ]
        for i, pos in enumerate(city_positions):
            dot = Dot(radius=0.06, color=COLORS["text_muted"], fill_opacity=0.8)
            dot.move_to(pos)
            entities.add(dot)

            # Connect to parent
            line = Line(country_positions[0], dot.get_center(),
                       color=COLORS["text_muted"], stroke_width=1, stroke_opacity=0.5)
            self.play(Create(line, run_time=0.2))
            self.play(Create(dot, run_time=0.2))

        self.wait(0.4)

        # ============================================================
        # CENTER: Matching Process
        # ============================================================
        # Arrow from image embedding to entity space
        match_arrow = Arrow(
            start=[-0.4, 0.7, 0],
            end=[1.8, 0.7, 0],
            buff=0.1,
            color=COLORS["gold_light"],
            stroke_width=3,
            tip_length=0.2
        )

        match_label = create_sans_body("Match", font_size=20)
        match_label.next_to(match_arrow, UP, buff=0.15)
        match_label.set_color(COLORS["gold_light"])

        self.play(Create(match_arrow, run_time=0.6))
        self.play(FadeIn(match_label, run_time=0.3))
        self.wait(0.8)

        # Highlight the best match with glow
        best_match = Dot(radius=0.12, color=COLORS["accent"], fill_opacity=1.0)
        best_match.move_to(country_positions[1])

        glow = Circle(
            radius=0.2,
            color=COLORS["gold_light"],
            stroke_width=2,
            fill_opacity=0,
            stroke_opacity=0.8
        )
        glow.move_to(country_positions[1])

        self.play(
            Create(best_match, run_time=0.4),
            Create(glow, run_time=0.4)
        )
        self.wait(1.0)

        # ============================================================
        # HIERARCHICAL SEARCH VISUALIZATION
        # ============================================================
        search_label = create_sans_body(
            "Hierarchical Search:\nCountry → Region → City",
            font_size=24
        )
        search_label.move_to([0, -1.5, 0])
        search_label.set_color(COLORS["accent"])

        self.play(FadeIn(search_label, run_time=0.6))
        self.wait(1.2)

        # ============================================================
        # EFFICIENCY METRICS
        # ============================================================
        # Clear for metrics
        self.play(
            FadeOut(image_box, image_label, encode_arrow, encode_label,
                   embedding_box, embedding_label, match_arrow, match_label,
                   entity_label, entities, best_match, glow, search_label,
                   run_time=0.8)
        )
        self.wait(0.4)

        # Metrics display
        efficiency_title = create_sans_body(
            "Efficiency Gains",
            font_size=32
        )
        efficiency_title.move_to([0, 1.5, 0])
        efficiency_title.set_color(COLORS["accent"])

        # Left metric
        metric_left = VGroup(
            create_sans_body("Traditional", font_size=20),
            create_sans_body("5M+ embeddings", font_size=20),
            create_sans_body("O(N) search", font_size=20)
        )
        metric_left.arrange(DOWN, buff=0.4)
        metric_left.move_to([-2.5, 0, 0])
        metric_left[1:].set_color(COLORS["text_muted"])

        # Right metric
        metric_right = VGroup(
            create_sans_body("HierLoc", font_size=20),
            create_sans_body("240K entities", font_size=20),
            create_sans_body("Sub-linear search", font_size=20)
        )
        metric_right.arrange(DOWN, buff=0.4)
        metric_right.move_to([2.5, 0, 0])
        metric_right[1:].set_color(COLORS["gold_light"])

        self.play(FadeIn(efficiency_title, run_time=0.5))
        self.wait(0.4)
        self.play(FadeIn(metric_left, metric_right, run_time=0.8))
        self.wait(2.0)

        # Efficiency gain highlight
        gain_label = create_sans_body(
            "95% fewer embeddings",
            font_size=28
        )
        gain_label.move_to([0, -1.5, 0])
        gain_label.set_color(COLORS["accent"])

        self.play(FadeIn(gain_label, run_time=0.6))
        self.wait(2.0)

        # ============================================================
        # FADE OUT FOR TRANSITION
        # ============================================================
        self.play(
            FadeOut(title, efficiency_title, metric_left, metric_right, gain_label, run_time=1.0)
        )
        self.wait(0.5)
