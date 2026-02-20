"""
Scene 5: Results - Impact and Call to Action
Duration: ~45 seconds
Purpose: Show concrete results and impact of HierLoc

Clean design with:
- Results metrics displayed clearly
- Efficiency gains visualization
- Final call to action
"""

from manim import *
import numpy as np
from config import COLORS, FONTS, setup_manim_config
from utils import create_serif_title, create_sans_body

setup_manim_config(quality="h")


class Scene5Results(Scene):
    """Results visualization with clean metrics and impact"""

    def construct(self):
        self.camera.background_color = COLORS["bg"]

        # ============================================================
        # TITLE: "Results"
        # ============================================================
        title = create_serif_title("Results", font_size=64)
        title.to_edge(UP, buff=0.4)
        self.play(FadeIn(title, run_time=1.0))
        self.wait(0.5)

        # ============================================================
        # PART A: Performance Metrics
        # ============================================================
        # Metric 1: Error reduction
        metric1_label = create_sans_body("Mean Geodesic Error", font_size=22)
        metric1_value = create_sans_body("↓ 19.5%", font_size=36)
        metric1_value.set_color(COLORS["accent"])

        metric1 = VGroup(metric1_label, metric1_value)
        metric1.arrange(DOWN, buff=0.3)
        metric1.move_to([-2.5, 1.2, 0])

        self.play(FadeIn(metric1_label, run_time=0.4))
        self.wait(0.3)
        self.play(FadeIn(metric1_value, run_time=0.6))
        self.wait(0.6)

        # Metric 2: Country accuracy
        metric2_label = create_sans_body("Country Accuracy", font_size=22)
        metric2_value = create_sans_body("+8.8%", font_size=36)
        metric2_value.set_color(COLORS["accent"])

        metric2 = VGroup(metric2_label, metric2_value)
        metric2.arrange(DOWN, buff=0.3)
        metric2.move_to([0, 1.2, 0])

        self.play(FadeIn(metric2_label, run_time=0.4))
        self.wait(0.3)
        self.play(FadeIn(metric2_value, run_time=0.6))
        self.wait(0.6)

        # Metric 3: City accuracy
        metric3_label = create_sans_body("City Accuracy", font_size=22)
        metric3_value = create_sans_body("+43.2%", font_size=36)
        metric3_value.set_color(COLORS["accent"])

        metric3 = VGroup(metric3_label, metric3_value)
        metric3.arrange(DOWN, buff=0.3)
        metric3.move_to([2.5, 1.2, 0])

        self.play(FadeIn(metric3_label, run_time=0.4))
        self.wait(0.3)
        self.play(FadeIn(metric3_value, run_time=0.6))
        self.wait(0.8)

        # ============================================================
        # PART B: Key Advantages
        # ============================================================
        advantages_title = create_sans_body("Why It Matters", font_size=28)
        advantages_title.move_to([0, 0.2, 0])
        advantages_title.set_color(COLORS["accent"])

        # Advantage 1: Faster
        adv1 = create_sans_body("⚡ Sub-linear search", font_size=20)
        adv1.move_to([-2.5, -0.8, 0])

        # Advantage 2: Smaller footprint
        adv2 = create_sans_body("💾 95% fewer embeddings", font_size=20)
        adv2.move_to([0, -0.8, 0])

        # Advantage 3: Interpretable
        adv3 = create_sans_body("🔍 Interpretable paths", font_size=20)
        adv3.move_to([2.5, -0.8, 0])

        self.play(FadeOut(metric1, metric2, metric3, run_time=0.6))
        self.wait(0.3)
        self.play(FadeIn(advantages_title, run_time=0.5))
        self.wait(0.4)
        self.play(FadeIn(adv1, adv2, adv3, run_time=0.8))
        self.wait(1.5)

        # ============================================================
        # PART C: Final Message
        # ============================================================
        final_message = create_sans_body(
            "Hyperbolic geometry is the\nright tool for hierarchy",
            font_size=28
        )
        final_message.move_to([0, -2.0, 0])
        final_message.set_color(COLORS["gold_light"])

        self.play(
            FadeOut(advantages_title, adv1, adv2, adv3, run_time=0.6)
        )
        self.wait(0.3)
        self.play(FadeIn(final_message, run_time=0.8))
        self.wait(2.0)

        # ============================================================
        # PART D: Call to Action
        # ============================================================
        cta_label = create_sans_body("Learn more", font_size=24)
        cta_label.move_to([0, -2.8, 0])
        cta_label.set_color(COLORS["accent"])

        self.play(FadeIn(cta_label, run_time=0.6))
        self.wait(2.0)

        # ============================================================
        # FADE OUT FOR COMPLETION
        # ============================================================
        self.play(
            FadeOut(title, final_message, cta_label, run_time=1.0)
        )
        self.wait(0.5)
