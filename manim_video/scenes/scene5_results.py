"""
Scene 5: RESULTS - Impact and Achievement
Duration: ~45 seconds
Purpose: Show concrete results from the paper (OSV5M benchmark)

From paper:
- 19.5% mean geodesic error reduction
- +8.8% country accuracy
- +20.1% region accuracy
- +43.2% subregion accuracy
"""

from manim import *
from config import COLORS, FONTS, setup_manim_config

setup_manim_config(quality="h")


class Scene5Results(Scene):
    """Results: State-of-the-art performance"""

    def construct(self):
        self.camera.background_color = COLORS["bg"]

        # ============================================================
        # SEQUENCE 1: Title (0-1s)
        # ============================================================
        title = Text(
            "Results",
            font=FONTS["sans"],
            font_size=64,
            color=COLORS["text"],
            
        )
        title.to_edge(UP, buff=0.5)

        self.play(FadeIn(title, run_time=1.0))
        self.wait(0.5)

        # ============================================================
        # SEQUENCE 2: Performance Metrics (1.5-15s)
        # ============================================================
        # Metric 1: Geodesic Error
        m1_label = Text(
            "Mean Geodesic Error",
            font=FONTS["sans"],
            font_size=20,
            color=COLORS["text_muted"]
        )
        m1_value = Text(
            "↓ 19.5%",
            font=FONTS["sans"],
            font_size=40,
            color=COLORS["accent"],
            
        )
        metric1 = VGroup(m1_label, m1_value).arrange(DOWN, buff=0.3)
        metric1.move_to([-2.5, 1.0, 0])

        # Metric 2: Country Accuracy
        m2_label = Text(
            "Country Accuracy",
            font=FONTS["sans"],
            font_size=20,
            color=COLORS["text_muted"]
        )
        m2_value = Text(
            "+8.8%",
            font=FONTS["sans"],
            font_size=40,
            color=COLORS["accent"],
            
        )
        metric2 = VGroup(m2_label, m2_value).arrange(DOWN, buff=0.3)
        metric2.move_to([2.5, 1.0, 0])

        # Metric 3: Region Accuracy
        m3_label = Text(
            "Region Accuracy",
            font=FONTS["sans"],
            font_size=20,
            color=COLORS["text_muted"]
        )
        m3_value = Text(
            "+20.1%",
            font=FONTS["sans"],
            font_size=40,
            color=COLORS["accent"],
            
        )
        metric3 = VGroup(m3_label, m3_value).arrange(DOWN, buff=0.3)
        metric3.move_to([0, 1.0, 0])

        self.play(FadeIn(metric1, run_time=0.7))
        self.wait(0.5)
        self.play(FadeIn(metric2, run_time=0.7))
        self.wait(0.5)
        self.play(FadeIn(metric3, run_time=0.7))
        self.wait(1.5)

        # Metric 4: Subregion (standout achievement)
        m4_label = Text(
            "Subregion Accuracy",
            font=FONTS["sans"],
            font_size=22,
            color=COLORS["text"]
        )
        m4_value = Text(
            "+43.2%",
            font=FONTS["sans"],
            font_size=48,
            color=COLORS["gold_light"],
            
        )
        metric4 = VGroup(m4_label, m4_value).arrange(DOWN, buff=0.4)
        metric4.move_to([0, -1.2, 0])

        self.play(FadeIn(metric4, run_time=0.9))
        self.wait(2.0)

        # ============================================================
        # SEQUENCE 3: Key Insights (15-28s)
        # ============================================================
        self.play(
            FadeOut(metric1, metric2, metric3, metric4, run_time=0.6)
        )
        self.wait(0.3)

        insights_title = Text(
            "Why This Matters",
            font=FONTS["sans"],
            font_size=32,
            color=COLORS["accent"],
            
        )
        insights_title.move_to([0, 1.5, 0])

        # Insight 1: Speed
        i1 = Text(
            "⚡ Sub-linear search time",
            font=FONTS["sans"],
            font_size=22,
            color=COLORS["text"]
        )
        i1.move_to([-1.5, 0.4, 0])

        # Insight 2: Memory
        i2 = Text(
            "💾 95% fewer embeddings",
            font=FONTS["sans"],
            font_size=22,
            color=COLORS["text"]
        )
        i2.move_to([1.5, 0.4, 0])

        # Insight 3: Interpretability
        i3 = Text(
            "🔍 Interpretable predictions",
            font=FONTS["sans"],
            font_size=22,
            color=COLORS["text"]
        )
        i3.move_to([0, -0.5, 0])

        self.play(FadeIn(insights_title, run_time=0.6))
        self.wait(0.4)
        self.play(FadeIn(i1, i2, i3, run_time=0.8))
        self.wait(2.0)

        # ============================================================
        # SEQUENCE 4: The Big Insight (28-38s)
        # ============================================================
        self.play(
            FadeOut(insights_title, i1, i2, i3, run_time=0.6)
        )
        self.wait(0.3)

        big_insight = Text(
            "Hyperbolic geometry is\nthe right tool for\nhierarchical data",
            font=FONTS["sans"],
            font_size=32,
            color=COLORS["gold_light"],
            ,
            line_spacing=1.4
        )
        big_insight.move_to([0, 0.3, 0])

        self.play(FadeIn(big_insight, run_time=1.0))
        self.wait(2.5)

        # ============================================================
        # SEQUENCE 5: Call to Action (38-45s)
        # ============================================================
        cta = Text(
            "Learn more: HierLoc paper & code",
            font=FONTS["sans"],
            font_size=24,
            color=COLORS["accent"]
        )
        cta.move_to([0, -2.0, 0])

        self.play(FadeIn(cta, run_time=0.8))
        self.wait(2.0)

        # ============================================================
        # SEQUENCE 6: Final Fade (45s)
        # ============================================================
        self.play(
            FadeOut(title, big_insight, cta, run_time=1.0)
        )
        self.wait(0.5)
