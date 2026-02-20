"""
Scene 1: HOOK - Paper Introduction & Visual Geolocation Challenge
Duration: ~24 seconds
Purpose: Ground in research, then pose the central question

Improved design with:
- Paper title, authors, affiliations (grounded in research)
- Beautiful geometric background (non-intrusive)
- All text in white (#e8e4da)
- Smooth transition to main challenge
"""

from manim import *
import os
import numpy as np
from pathlib import Path
from config import COLORS, FONTS, setup_manim_config
from utils import create_serif_title, create_sans_body

setup_manim_config(quality="h")


class Scene1Hook(Scene):
    """Opening: Paper info + Geolocation challenge"""

    def construct(self):
        self.camera.background_color = COLORS["bg"]

        # ============================================================
        # BACKGROUND: Beautiful geometric pattern
        # ============================================================
        # Create elegant geometric background (low opacity, gold color)
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
        # SEQUENCE 1: Paper Title (0-2s)
        # ============================================================
        paper_title = Text(
            "HierLoc: Hyperbolic Entity Embeddings\nfor Hierarchical Visual Geolocation",
            font=FONTS["sans"],
            font_size=32,
            color=COLORS["text"],
            line_spacing=1.3
        )
        paper_title.move_to([0, 2.8, 0])

        self.play(FadeIn(paper_title, run_time=1.2))
        self.wait(1.0)

        # ============================================================
        # SEQUENCE 2: Authors (2-3.5s)
        # ============================================================
        authors = Text(
            "Hari Krishna Gadi, Hongyi Luo, Daniel Matos, Lu Liu,\nYongliang Wang, Yanfeng Zhang, Liqiu Meng",
            font=FONTS["sans"],
            font_size=18,
            color=COLORS["text"],
            line_spacing=1.2
        )
        authors.move_to([0, 1.8, 0])

        self.play(FadeIn(authors, run_time=0.8))
        self.wait(0.7)

        # ============================================================
        # SEQUENCE 3: Affiliations (3.5-4.5s)
        # ============================================================
        affiliations = Text(
            "Huawei Riemann Lab, Technical University of Munich",
            font=FONTS["sans"],
            font_size=16,
            color=COLORS["text_muted"]
        )
        affiliations.move_to([0, 1.2, 0])

        self.play(FadeIn(affiliations, run_time=0.6))
        self.wait(0.8)

        # ============================================================
        # SEQUENCE 4: Transition & Main Challenge (4.5-12s)
        # ============================================================
        # Fade out paper info
        self.play(
            FadeOut(paper_title, authors, affiliations, run_time=0.8)
        )
        self.wait(0.5)

        # Main title: "HierLoc" - centered
        title = Text(
            "HierLoc",
            font=FONTS["sans"],
            font_size=100,
            color=COLORS["text"]
        )
        title.move_to([0, 2.5, 0])

        # Apply gold accent to "Loc" (last 3 characters)
        title[4:7].set_color(COLORS["accent"])

        self.play(FadeIn(title, run_time=1.0))
        self.wait(0.5)

        # Subtitle: "Visual Geolocation"
        subtitle = Text(
            "Visual Geolocation",
            font=FONTS["sans"],
            font_size=42,
            color=COLORS["text_muted"]
        )
        subtitle.next_to(title, DOWN, buff=0.4)

        self.play(FadeIn(subtitle, run_time=0.8))
        self.wait(1.0)

        # ============================================================
        # SEQUENCE 5: First Question with Image (12-16s)
        # ============================================================
        q1_text = Text(
            "Can you guess where\nthis photo was taken?",
            font=FONTS["sans"],
            font_size=32,
            color=COLORS["text"],
            line_spacing=1.2
        )
        q1_text.move_to([0, -2.5, 0])

        # Load image from streetview directory
        streetview_dir = "/Volumes/SSD/iclr-website/static/images/streetview"
        image_paths = [
            os.path.join(streetview_dir, "Paris_00131_445353063_8c58bd82b1_179_88895879@N00.jpg"),
            os.path.join(streetview_dir, "Russia_00019_985802242_5ad0b7dbeb_1190_23707253@N00.jpg"),
            os.path.join(streetview_dir, "482314949_dbc149bb10_224_50435419@N00.jpg"),
        ]

        # Verify images exist
        available_images = [p for p in image_paths if os.path.exists(p)]

        if available_images:
            image1 = ImageMobject(available_images[0])
            image1.set_height(3.0)
            image1.move_to([0, 0.5, 0])

            self.play(FadeIn(image1, run_time=0.8))
            self.wait(0.4)
            self.play(FadeIn(q1_text, run_time=0.6))
            self.wait(1.5)

            # ============================================================
            # SEQUENCE 6: Second Question with Different Image (16-20s)
            # ============================================================
            q2_text = Text(
                "Without landmarks,\npeople, or language?",
                font=FONTS["sans"],
                font_size=32,
                color=COLORS["text"],
                line_spacing=1.2
            )
            q2_text.move_to([0, -2.5, 0])

            if len(available_images) > 1:
                image2 = ImageMobject(available_images[1])
                image2.set_height(3.0)
                image2.move_to([0, 0.5, 0])

                # Cross-fade
                self.play(
                    FadeOut(q1_text, run_time=0.5),
                    FadeOut(image1, run_time=0.5)
                )
                self.wait(0.3)
                self.play(FadeIn(image2, run_time=0.6))
                self.wait(0.3)
                self.play(FadeIn(q2_text, run_time=0.6))
                self.wait(1.5)

                # ============================================================
                # SEQUENCE 7: The Challenge (20-24s)
                # ============================================================
                challenge_text = VGroup(
                    Text(
                        "How would a",
                        font=FONTS["sans"],
                        font_size=40,
                        color=COLORS["text"]
                    ),
                    Text(
                        "computer",
                        font=FONTS["sans"],
                        font_size=40,
                        color=COLORS["accent"]
                    ),
                    Text(
                        "solve this?",
                        font=FONTS["sans"],
                        font_size=40,
                        color=COLORS["text"]
                    )
                )
                challenge_text.arrange(DOWN, buff=0.2)
                challenge_text.move_to([0, -2.5, 0])

                # Reveal the challenge
                self.play(FadeOut(q2_text, image2, run_time=0.5))
                self.wait(0.3)

                for i, part in enumerate(challenge_text):
                    self.play(Write(part, run_time=0.4, rate_func=linear))
                    self.wait(0.2)

                self.wait(2.0)

                # ============================================================
                # SEQUENCE 8: Transition to Next Scene (24s)
                # ============================================================
                self.play(
                    FadeOut(title, subtitle, challenge_text, background_elements, run_time=1.0)
                )
                self.wait(0.5)
            else:
                # Fallback if second image not available
                self.play(FadeOut(q1_text, image1, run_time=0.5))
                self.wait(0.3)
                self.play(FadeIn(q2_text, run_time=0.6))
                self.wait(2.0)
                self.play(FadeOut(title, subtitle, q2_text, background_elements, run_time=1.0))
                self.wait(0.5)
        else:
            # Fallback if no images available - proceed with text only
            self.play(FadeIn(q1_text, run_time=0.6))
            self.wait(2.0)

            q2_text = Text(
                "How would a computer\nsolve this challenge?",
                font=FONTS["sans"],
                font_size=32,
                color=COLORS["text"],
                line_spacing=1.2
            )
            q2_text.move_to([0, -2.5, 0])

            self.play(FadeOut(q1_text, run_time=0.5))
            self.wait(0.3)
            self.play(FadeIn(q2_text, run_time=0.6))
            self.wait(2.0)

            self.play(FadeOut(title, subtitle, q2_text, background_elements, run_time=1.0))
            self.wait(0.5)
