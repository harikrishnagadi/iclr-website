"""
Scene 4: THE SOLUTION - Entity Features & Embeddings
Duration: ~80 seconds
Purpose: Explain how geographical entities are represented as embeddings

Structure:
1. Entity features: Images, Location, Name
2. Feature embeddings: z_img, z_loc, z_name
3. Entity representation: Combined vector
4. Hierarchical search in embedding space
"""

from manim import *
import numpy as np
import sys
from pathlib import Path
import os

sys.path.insert(0, str(Path(__file__).parent.parent))

from config import COLORS, FONTS, setup_manim_config
from layout import ObjectPositioner

setup_manim_config(quality="high_quality")

# Get absolute paths for assets
ASSETS_DIR = Path(__file__).parent.parent / "assets"
ICONS_DIR = ASSETS_DIR / "icons"


class Scene4Solution(Scene):
    """Entity features and embeddings explanation"""

    def construct(self):
        self.camera.background_color = COLORS["bg"]

        # ============================================================
        # HEADER & PROGRESS LINE
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
        # SEQUENCE 2: Three Entity Features (1.5-20s)
        # ============================================================
        subtitle = Text(
            "How entities are defined",
            font=FONTS["sans"],
            font_size=18,
            color=COLORS["text_muted"]
        )
        subtitle.move_to([0, 1.3, 0])

        self.play(FadeIn(subtitle, run_time=0.6))
        self.wait(0.4)

        # Three feature panels with proper CSS layout
        feature_labels = [
            {"title": "Images", "desc": "Visual content\nfrom location"},
            {"title": "Location", "desc": "Geographic\ncoordinates"},
            {"title": "Name", "desc": "Entity name\nand metadata"}
        ]

        feature_panels = VGroup()

        for i, feat in enumerate(feature_labels):
            # Panel box
            panel = RoundedRectangle(
                width=2.0,
                height=2.2,
                corner_radius=0.15,
                color=COLORS["accent"],
                stroke_width=2,
                fill_opacity=0.06,
                fill_color=COLORS["accent"]
            )

            # Title
            feat_title = Text(
                feat["title"],
                font=FONTS["sans"],
                font_size=16,
                color=COLORS["accent"],
                weight=BOLD
            )

            # Description
            feat_desc = Text(
                feat["desc"],
                font=FONTS["sans"],
                font_size=12,
                color=COLORS["text_muted"],
                line_spacing=1.2
            )

            # Stack vertically with proper spacing
            content = VGroup(feat_title, feat_desc).arrange(DOWN, buff=0.3)
            panel.move_to([0, 0, 0])
            content.move_to(panel.get_center())

            feature_group = VGroup(panel, content)
            feature_panels.add(feature_group)

        # Layout 3 panels horizontally with CSS-style spacing
        feature_panels.arrange(RIGHT, buff=0.8, center=True)
        feature_panels.move_to([0, 0.5, 0])

        self.play(FadeIn(feature_panels, run_time=0.8))
        self.wait(2.0)

        # ============================================================
        # SEQUENCE 3: Feature Embeddings (20-35s)
        # ============================================================
        self.play(FadeOut(subtitle, run_time=0.4))
        self.wait(0.2)

        embedding_title = Text(
            "Convert to embeddings",
            font=FONTS["sans"],
            font_size=20,
            color=COLORS["accent"]
        )
        embedding_title.move_to([0, 1.3, 0])

        self.play(FadeIn(embedding_title, run_time=0.6))
        self.wait(0.3)

        # Arrows down from features
        arrows = VGroup()
        for i in range(3):
            arrow = Arrow(
                start=feature_panels[i].get_bottom(),
                end=[feature_panels[i].get_center()[0], -0.6, 0],
                buff=0.1,
                color=COLORS["gold_light"],
                stroke_width=2.5,
                tip_length=0.12
            )
            arrows.add(arrow)

        self.play(Create(arrows, run_time=0.6))
        self.wait(0.4)

        # Embedding labels
        embedding_texts = ["z_img", "z_loc", "z_name"]
        embedding_labels = VGroup()

        for i, embed_label in enumerate(embedding_texts):
            label = Text(
                embed_label,
                font=FONTS["sans"],
                font_size=16,
                color=COLORS["gold_light"]
            )
            label.move_to([feature_panels[i].get_center()[0], -1.3, 0])
            embedding_labels.add(label)

        self.play(FadeIn(embedding_labels, run_time=0.6))
        self.wait(1.5)

        # ============================================================
        # SEQUENCE 4: Entity Vector (35-50s)
        # ============================================================
        self.play(
            FadeOut(feature_panels, arrows, embedding_labels, embedding_title, run_time=0.6)
        )
        self.wait(0.3)

        entity_title = Text(
            "Entity Representation",
            font=FONTS["sans"],
            font_size=24,
            color=COLORS["accent"]
        )
        entity_title.move_to([0, 1.5, 0])

        # Entity vector equation
        entity_eq = Text(
            "e = [z_img, z_loc, z_name]",
            font=FONTS["sans"],
            font_size=20,
            color=COLORS["gold_light"]
        )
        entity_eq.move_to([0, 0.7, 0])

        # Explanation
        explanation = Text(
            "Combined vector in hyperbolic space\nenables hierarchical matching",
            font=FONTS["sans"],
            font_size=14,
            color=COLORS["text_muted"],
            line_spacing=1.2
        )
        explanation.move_to([0, -0.3, 0])

        self.play(FadeIn(entity_title, entity_eq, explanation, run_time=0.8))
        self.wait(2.0)

        # ============================================================
        # SEQUENCE 5: Search Process (50-65s)
        # ============================================================
        self.play(
            FadeOut(entity_title, entity_eq, explanation, run_time=0.5)
        )
        self.wait(0.2)

        search_title = Text(
            "Hierarchical Search",
            font=FONTS["sans"],
            font_size=28,
            color=COLORS["accent"]
        )
        search_title.move_to([0, 1.8, 0])

        # Search steps in organized layout
        search_steps = VGroup()
        steps_text = [
            "1. Query image → z_query",
            "2. Find similar entities",
            "3. Rank by geography:\n   Countries → Regions → Cities"
        ]

        for i, step in enumerate(steps_text):
            step_text = Text(
                step,
                font=FONTS["sans"],
                font_size=14,
                color=COLORS["text_muted"],
                line_spacing=1.1
            )
            search_steps.add(step_text)

        search_steps.arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        search_steps.move_to([0, 0.3, 0])

        self.play(FadeIn(search_title, run_time=0.6))
        self.wait(0.3)
        self.play(FadeIn(search_steps, run_time=0.8))
        self.wait(2.0)

        # ============================================================
        # SEQUENCE 6: Key Insight (65-75s)
        # ============================================================
        self.play(
            FadeOut(search_title, search_steps, run_time=0.5)
        )
        self.wait(0.2)

        insight_box = RoundedRectangle(
            width=6.0,
            height=1.8,
            corner_radius=0.15,
            color=COLORS["accent"],
            stroke_width=2.5,
            fill_opacity=0.08,
            fill_color=COLORS["accent"]
        )
        insight_box.move_to([0, 0.3, 0])

        insight_text = Text(
            "Hyperbolic geometry preserves hierarchical structure\nwhile enabling efficient similarity search",
            font=FONTS["sans"],
            font_size=16,
            color=COLORS["text"],
            line_spacing=1.3
        )
        insight_text.move_to(insight_box.get_center())

        self.play(Create(insight_box, run_time=0.6))
        self.play(FadeIn(insight_text, run_time=0.6))
        self.wait(2.5)

        # ============================================================
        # SEQUENCE 7: Transition (75-80s)
        # ============================================================
        self.play(
            FadeOut(title, insight_box, insight_text, run_time=1.0)
        )
        self.wait(0.5)
