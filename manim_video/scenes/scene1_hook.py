"""
Scene 1: HOOK - Visual Geolocation Challenge
Duration: ~24 seconds
Purpose: Pose the central question + show why it's hard

Award-winning design with:
- Professional title animation
- Actual street view images
- Clean text reveals
- Perfect geometry and readability
"""

from manim import *
import os
from pathlib import Path
from config import COLORS, FONTS, setup_manim_config
from utils import create_serif_title, create_sans_body

setup_manim_config(quality="h")


class Scene1Hook(Scene):
    """Opening hook: The geolocation challenge"""

    def construct(self):
        self.camera.background_color = COLORS["bg"]

        # ============================================================
        # SEQUENCE 1: Title Introduction (0-1.5s)
        # ============================================================
        # Main title: "HierLoc" - clean, centered
        # Position: Y=3.0 (top third of scene)
        title = Text(
            "HierLoc",
            font=FONTS["sans"],
            font_size=100,
            color=COLORS["text"],
            
        )
        title.move_to([0, 3.0, 0])

        # Apply gold accent to "Loc" (last 3 characters)
        title[4:7].set_color(COLORS["accent"])

        self.play(FadeIn(title, run_time=1.0))
        self.wait(0.5)

        # ============================================================
        # SEQUENCE 2: Subtitle (1.5-2.5s)
        # ============================================================
        subtitle = Text(
            "Visual Geolocation",
            font=FONTS["sans"],
            font_size=42,
            color=COLORS["text_muted"]
        )
        subtitle.next_to(title, DOWN, buff=0.4)

        self.play(FadeIn(subtitle, run_time=0.8))
        self.wait(0.3)

        # ============================================================
        # SEQUENCE 3: First Question with Image (2.5-6s)
        # ============================================================
        # Question 1 text
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
            self.wait(2.0)

            # ============================================================
            # SEQUENCE 4: Second Question with Different Image (6-9.5s)
            # ============================================================
            q2_text = Text(
                "Without landmarks,\npeople, or language?",
                font=FONTS["sans"],
                font_size=32,
                color=COLORS["text"],
                line_spacing=1.2
            )
            q2_text.move_to([0, -2.5, 0])

            # Load second image (different region)
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
                self.wait(2.0)

                # ============================================================
                # SEQUENCE 5: The Challenge (9.5-15s)
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
                        color=COLORS["accent"],
                        
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

                self.wait(2.5)

                # ============================================================
                # SEQUENCE 6: Transition to Next Scene (15-24s)
                # ============================================================
                self.play(
                    FadeOut(title, subtitle, challenge_text, run_time=1.0)
                )
                self.wait(0.5)
            else:
                # Fallback if second image not available
                self.play(FadeOut(q1_text, image1, run_time=0.5))
                self.wait(0.3)
                self.play(FadeIn(q2_text, run_time=0.6))
                self.wait(2.0)
                self.play(FadeOut(title, subtitle, q2_text, run_time=1.0))
                self.wait(0.5)
        else:
            # Fallback if no images available
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
            self.play(FadeOut(title, subtitle, q2_text, run_time=1.0))
            self.wait(0.5)
