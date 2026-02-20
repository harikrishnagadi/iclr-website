"""
Scene 1: Hook - The Central Question
Duration: ~24 seconds
Purpose: Pose the mystery of geolocation

Design: Minimal, elegant title + simple text reveals
"""

from manim import *
from config import COLORS, FONTS, setup_manim_config
from utils import create_serif_title, create_sans_body

setup_manim_config(quality="h")


class Scene1Hook(Scene):
    """Opening hook with clean geometry and minimal design"""

    def construct(self):
        self.camera.background_color = COLORS["bg"]

        # ============================================================
        # TITLE ANIMATION: "HierLoc" with gold accent on "Loc"
        # ============================================================
        title = create_serif_title("HierLoc", font_size=96)
        title.move_to(UP * 2.5)

        # Apply gold color to "Loc" (characters 4-7)
        title[4:7].set_color(COLORS["accent"])

        self.play(FadeIn(title, run_time=1.2))
        self.wait(0.5)

        # ============================================================
        # SUBTITLE: "Where Are You?"
        # ============================================================
        subtitle = create_sans_body("Where Are You?", font_size=48)
        subtitle.next_to(title, DOWN, buff=0.6)
        subtitle.set_color(COLORS["text_muted"])

        self.play(FadeIn(subtitle, run_time=0.8))
        self.wait(1.5)

        # ============================================================
        # QUESTION 1: "Can you guess where this photo was taken?"
        # ============================================================
        q1 = create_sans_body(
            "Can you guess where this\nphoto was taken?",
            font_size=40
        )
        q1.move_to(DOWN * 2)

        self.play(FadeOut(subtitle, run_time=0.4))
        self.wait(0.3)
        self.play(Write(q1, run_time=1.2, rate_func=linear))
        self.wait(2.0)

        # ============================================================
        # QUESTION 2: "Without relying on people or landmarks?"
        # ============================================================
        q2 = create_sans_body(
            "Without relying on people\nor landmarks?",
            font_size=40
        )
        q2.move_to(DOWN * 2)

        self.play(FadeOut(q1, run_time=0.4))
        self.wait(0.3)
        self.play(Write(q2, run_time=1.2, rate_func=linear))
        self.wait(2.0)

        # ============================================================
        # FINAL QUESTION: "How would a computer solve this?"
        # ============================================================
        q3_line1 = create_sans_body("How would a", font_size=44)
        q3_line2 = create_sans_body("computer", font_size=44)
        q3_line2.set_color(COLORS["accent"])
        q3_line3 = create_sans_body("solve this?", font_size=44)

        q3 = VGroup(q3_line1, q3_line2, q3_line3)
        q3.arrange(DOWN, buff=0.3)
        q3.move_to(DOWN * 2)

        self.play(FadeOut(q2, run_time=0.4))
        self.wait(0.3)
        self.play(Write(q3, run_time=1.5, rate_func=linear))
        self.wait(3.0)

        # Fade out for transition
        self.play(FadeOut(title, q3, run_time=1.0))
        self.wait(0.5)
