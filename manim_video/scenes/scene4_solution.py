"""
Scene 4: THE SOLUTION - HierLoc Entity Features & Embeddings
Duration: ~80 seconds
Purpose: Explain how geographical entities are represented with features and embeddings

Pipeline:
1. Entity features (image, location, name)
2. Feature embeddings (z_img, z_loc, z_name)
3. Aggregation example (Paris)
4. Entity representation in hyperbolic space
5. Hierarchical search
"""

from manim import *
import numpy as np
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from config import COLORS, FONTS, setup_manim_config
from layout import ObjectPositioner

setup_manim_config(quality="high_quality")


class Scene4Solution(Scene):
    """HierLoc entity features and embeddings"""

    def construct(self):
        self.camera.background_color = COLORS["bg"]

        # ============================================================
        # HEADER & PROGRESS LINE (Top of Scene)
        # ============================================================
        divider_line = Line(
            start=[-7.0, 3.2, 0],
            end=[7.0, 3.2, 0],
            color=COLORS["text_muted"],
            stroke_width=1.5,
            stroke_opacity=0.3
        )

        progress_dots = VGroup()
        num_scenes = 5
        dot_x_positions = np.linspace(-6.8, 6.8, num_scenes)
        for i, x_pos in enumerate(dot_x_positions):
            dot = Dot(
                point=[x_pos, 3.2, 0],
                radius=0.07,
                color=COLORS["gold_light"] if i == 3 else COLORS["text_muted"],
                fill_opacity=1.0 if i == 3 else 0.4
            )
            progress_dots.add(dot)

        hierlock_header = Text(
            "HierLoc",
            font=FONTS["sans"],
            font_size=48,
            color=COLORS["accent"]
        )
        hierlock_header.move_to([-5.5, 3.6, 0])

        self.add(divider_line, progress_dots, hierlock_header)

        # ============================================================
        # SEQUENCE 1: Title (0-1s)
        # ============================================================
        title = Text(
            "Entity Representation",
            font=FONTS["sans"],
            font_size=56,
            color=COLORS["text"]
        )
        title.move_to([0, 2.2, 0])

        self.play(FadeIn(title, run_time=1.0))
        self.wait(0.5)

        # ============================================================
        # SEQUENCE 2: Entity Features (1.5-15s)
        # ============================================================
        subtitle = Text(
            "What defines a geographical entity?",
            font=FONTS["sans"],
            font_size=20,
            color=COLORS["text_muted"]
        )
        subtitle.move_to([0, 1.4, 0])

        self.play(FadeIn(subtitle, run_time=0.6))
        self.wait(0.4)

        # Three feature boxes with icons
        features = [
            {"name": "Images", "desc": "Photos from location", "x": -3.5, "icon": "../assets/icons/image_icon.svg"},
            {"name": "Location", "desc": "Coordinates (lat, lon)", "x": 0.0, "icon": "../assets/icons/location_icon.svg"},
            {"name": "Name", "desc": "City/region name", "x": 3.5, "icon": "../assets/icons/name_icon.svg"}
        ]

        feature_boxes = VGroup()
        for feat in features:
            # Load SVG icon
            try:
                icon = SVGMobject(feat["icon"])
                icon.scale(0.8)
                icon.move_to([feat["x"], 0.7, 0])
            except:
                # Fallback to colored circle if icon not found
                icon = Circle(radius=0.4, color=COLORS["accent"], stroke_width=2)
                icon.move_to([feat["x"], 0.7, 0])

            # Name
            name = Text(
                feat["name"],
                font=FONTS["sans"],
                font_size=14,
                color=COLORS["accent"]
            )
            name.move_to([feat["x"], 0.1, 0])

            # Description
            desc = Text(
                feat["desc"],
                font=FONTS["sans"],
                font_size=10,
                color=COLORS["text_muted"],
                line_spacing=1.1
            )
            desc.move_to([feat["x"], -0.6, 0])

            feature_group = VGroup(icon, name, desc)
            feature_boxes.add(feature_group)

        self.play(FadeIn(feature_boxes, run_time=1.0))
        self.wait(2.0)

        # ============================================================
        # SEQUENCE 3: Feature Embeddings (15-35s)
        # ============================================================
        self.play(FadeOut(subtitle, run_time=0.4))
        self.wait(0.2)

        embedding_title = Text(
            "Convert each feature to embedding",
            font=FONTS["sans"],
            font_size=22,
            color=COLORS["accent"]
        )
        embedding_title.move_to([0, 1.4, 0])

        self.play(FadeIn(embedding_title, run_time=0.6))
        self.wait(0.4)

        # Arrows pointing down from features
        arrows = VGroup()
        for feat in features:
            arrow = Arrow(
                start=[feat["x"], -0.2, 0],
                end=[feat["x"], -1.2, 0],
                buff=0,
                color=COLORS["gold_light"],
                stroke_width=2,
                tip_length=0.12
            )
            arrows.add(arrow)

        self.play(Create(arrows, run_time=0.6))
        self.wait(0.3)

        # Embedding labels
        embeddings = [
            {"label": "z_img", "x": -3.5},
            {"label": "z_loc", "x": 0.0},
            {"label": "z_name", "x": 3.5}
        ]

        embedding_labels = VGroup()
        for emb in embeddings:
            label = Text(
                emb["label"],
                font=FONTS["sans"],
                font_size=18,
                color=COLORS["gold_light"]
            )
            label.move_to([emb["x"], -1.6, 0])
            embedding_labels.add(label)

        self.play(FadeIn(embedding_labels, run_time=0.6))
        self.wait(1.5)

        # ============================================================
        # SEQUENCE 4: Aggregation Example - Paris (35-55s)
        # ============================================================
        self.play(
            FadeOut(feature_boxes, arrows, embedding_labels, embedding_title, run_time=0.6)
        )
        self.wait(0.3)

        example_title = Text(
            "Example: Paris",
            font=FONTS["sans"],
            font_size=28,
            color=COLORS["accent"]
        )
        example_title.move_to([0, 2.0, 0])

        self.play(FadeIn(example_title, run_time=0.6))
        self.wait(0.4)

        # Load and display real Paris image
        try:
            paris_img = ImageMobject("../assets/images/paris_eiffel.jpg")
            paris_img.scale(1.2)
            paris_img.move_to([-4.5, 0.8, 0])

            self.play(FadeIn(paris_img, run_time=0.6))
            self.wait(0.4)
        except:
            paris_img = None

        # Image aggregation explanation
        img_explain = Text(
            "Multiple images from Paris",
            font=FONTS["sans"],
            font_size=16,
            color=COLORS["text_muted"]
        )
        img_explain.move_to([0, 1.2, 0])

        self.play(FadeIn(img_explain, run_time=0.4))
        self.wait(0.3)

        # Show multiple image embeddings
        img_dots = VGroup()
        img_labels = []
        for i, offset in enumerate([-0.6, -0.2, 0.2, 0.6]):
            dot = Dot(
                point=[-1.5 + offset, 0.5, 0],
                radius=0.08,
                color=COLORS["gold_light"]
            )
            img_dots.add(dot)

            label = Text(
                f"z_img_{i+1}",
                font=FONTS["sans"],
                font_size=10,
                color=COLORS["text_muted"]
            )
            label.move_to([-1.5 + offset, -0.1, 0])
            img_labels.append(label)

        img_labels_group = VGroup(*img_labels)
        self.play(FadeIn(img_dots, img_labels_group, run_time=0.6))
        self.wait(0.6)

        # Mean aggregation arrow
        mean_arrow = Arrow(
            start=[-0.9, 0.5, 0],
            end=[0.6, 0.5, 0],
            buff=0,
            color=COLORS["accent"],
            stroke_width=2.5,
            tip_length=0.12
        )

        mean_label = Text(
            "mean",
            font=FONTS["sans"],
            font_size=14,
            color=COLORS["accent"]
        )
        mean_label.next_to(mean_arrow, UP, buff=0.1)

        self.play(Create(mean_arrow, run_time=0.4))
        self.play(FadeIn(mean_label, run_time=0.3))
        self.wait(0.4)

        # Result: single embedding
        result_embedding = Text(
            "z_img_Paris",
            font=FONTS["sans"],
            font_size=18,
            color=COLORS["gold_light"]
        )
        result_embedding.move_to([1.8, 0.5, 0])

        self.play(FadeIn(result_embedding, run_time=0.4))
        self.wait(0.4)

        # Location and name embeddings for Paris
        paris_info = Text(
            "z_loc_Paris: (48.8566°N, 2.3522°E)\nz_name_Paris: semantic embedding",
            font=FONTS["sans"],
            font_size=14,
            color=COLORS["text_muted"],
            line_spacing=1.3
        )
        paris_info.move_to([0, -0.5, 0])

        self.play(FadeIn(paris_info, run_time=0.6))
        self.wait(1.5)

        # ============================================================
        # SEQUENCE 5: Complete Entity Vector (55-65s)
        # ============================================================
        fade_objects = [img_explain, img_dots, img_labels_group, mean_arrow,
                       mean_label, result_embedding, paris_info]
        if paris_img is not None:
            fade_objects.append(paris_img)

        self.play(
            FadeOut(*fade_objects, run_time=0.6)
        )
        self.wait(0.2)

        entity_vector_title = Text(
            "Entity Vector for Paris",
            font=FONTS["sans"],
            font_size=24,
            color=COLORS["accent"]
        )
        entity_vector_title.move_to([0, 1.2, 0])

        entity_vector = Text(
            "e_Paris = [z_img_Paris, z_loc_Paris, z_name_Paris]",
            font=FONTS["sans"],
            font_size=18,
            color=COLORS["gold_light"]
        )
        entity_vector.move_to([0, 0.4, 0])

        hyperbolic_text = Text(
            "Mapped to Hyperbolic Space\nfor hierarchical representation",
            font=FONTS["sans"],
            font_size=14,
            color=COLORS["text_muted"],
            line_spacing=1.2
        )
        hyperbolic_text.move_to([0, -0.5, 0])

        self.play(FadeIn(entity_vector_title, run_time=0.5))
        self.play(FadeIn(entity_vector, run_time=0.5))
        self.wait(0.3)
        self.play(FadeIn(hyperbolic_text, run_time=0.5))
        self.wait(1.5)

        # ============================================================
        # SEQUENCE 6: Search Process (65-75s)
        # ============================================================
        self.play(
            FadeOut(example_title, entity_vector_title, entity_vector,
                   hyperbolic_text, run_time=0.6)
        )
        self.wait(0.2)

        search_title = Text(
            "Query Image → Query Embedding",
            font=FONTS["sans"],
            font_size=24,
            color=COLORS["accent"]
        )
        search_title.move_to([0, 1.5, 0])

        search_steps = Text(
            "1. Encode query image to z_query\n"
            "2. Find similar entities in hyperbolic space\n"
            "3. Hierarchical ranking: country → region → city",
            font=FONTS["sans"],
            font_size=16,
            color=COLORS["text_muted"],
            line_spacing=1.3
        )
        search_steps.move_to([0, -0.2, 0])

        self.play(FadeIn(search_title, run_time=0.6))
        self.wait(0.3)
        self.play(FadeIn(search_steps, run_time=0.6))
        self.wait(2.0)

        # ============================================================
        # SEQUENCE 7: Transition (75-80s)
        # ============================================================
        self.play(
            FadeOut(title, search_title, search_steps, run_time=1.0)
        )
        self.wait(0.5)
