"""
Scene 5: Results & Impact - The Payoff
Duration: ~30 seconds
Purpose: Show concrete results, efficiency gains, interpretability, and broader impact

Visual Sequence 1: Results Metrics (5-6 seconds)
- Animated bar charts/metrics showing accuracy improvements at each geographic level
- Mean Geodesic Error: ↓ 19.5% (headline result, special color)
- Country Accuracy: +8.8%
- Region Accuracy: +20.1%
- Subregion Accuracy: +43.2% (biggest improvement, emphasized)
- City Accuracy: +16.8%
- Animated counters showing improvement percentages
- Narration: "The results? State-of-the-art performance across every geographic level"

Visual Sequence 2: Efficiency Comparison (5-6 seconds)
- Side-by-side comparison visualization
- LEFT: "240k entity embeddings" (small box, gold highlight)
- RIGHT: "5M+ image embeddings" (large box, muted/faded)
- CENTER: "95% Reduction" (large text, gold accent)
- Subtitle: "in storage & search complexity"
- Animated transition showing size difference
- Narration: "95% fewer embeddings to store and search"

Visual Sequence 3: Interpretability (5-6 seconds)
- Show entity path example: Image → Germany → Bavaria → Munich
- Use nested containers or step-by-step reveals with arrows
- Gold highlights for matched entities
- Text: "Know WHICH ENTITIES matched"
- Narration: "And the system is interpretable - you know which entities matched"

Visual Sequence 4: Broader Impact (5-6 seconds)
- Large text statement: "Hyperbolic geometry is the right tool for hierarchical data"
- Visual: Optional hyperbolic disk in background (faded)
- Emphasize elegance and broader implications
- Narration: "This shows something bigger..."

Visual Sequence 5: Call-to-Action & Finale (4-5 seconds)
- Title: "HierLoc: Hierarchical Visual Geolocation" (DM Serif Display, large)
- Subtitle: "Learn More" (Syne, smaller)
- Links/CTA: "Paper • Code • Website" (clickable-looking)
- Optional: Subtle glow effect or key visual replay
- Tone: Triumphant celebration
- Narration: Encouraging to explore further

Technical Implementation Notes:
- Total duration: ~30 seconds
- Five major phases with clear structure
- Uses config.py colors: #0a0a0f bg, #e8a838 accent, #e8e4da text
- Uses DM Serif Display (titles) + Syne (body)
- Import utils.py helpers
- Well-commented code with phase headers
"""

from manim import *
import numpy as np
import os
import sys

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import COLORS, FONTS, setup_manim_config
from utils import create_serif_title, create_sans_body, apply_color

setup_manim_config(quality="high_quality")


class Scene5Results(Scene):
    """
    Results and impact scene - The final celebration.

    Structure:
    - Phase 1: Results Metrics (5-6 seconds)
    - Phase 2: Efficiency Comparison (5-6 seconds)
    - Phase 3: Interpretability (5-6 seconds)
    - Phase 4: Broader Impact (5-6 seconds)
    - Phase 5: Call-to-Action & Finale (4-5 seconds)

    Total duration: ~30 seconds
    """

    def construct(self):
        """Main scene construction"""
        # ════════════════════════════════════════════════════════════════════════════
        # SETUP: Configure scene
        # ════════════════════════════════════════════════════════════════════════════
        self.camera.background_color = COLORS["bg"]

        # ════════════════════════════════════════════════════════════════════════════
        # PHASE 1: RESULTS METRICS (5-6 seconds)
        # ════════════════════════════════════════════════════════════════════════════
        # Visual: Animated bar charts showing accuracy improvements

        self.phase_1_results_metrics()

        # ════════════════════════════════════════════════════════════════════════════
        # PHASE 2: EFFICIENCY COMPARISON (5-6 seconds)
        # ════════════════════════════════════════════════════════════════════════════
        # Visual: Side-by-side box comparison with dramatic size difference

        self.phase_2_efficiency_comparison()

        # ════════════════════════════════════════════════════════════════════════════
        # PHASE 3: INTERPRETABILITY (5-6 seconds)
        # ════════════════════════════════════════════════════════════════════════════
        # Visual: Entity path visualization showing hierarchical matching

        self.phase_3_interpretability()

        # ════════════════════════════════════════════════════════════════════════════
        # PHASE 4: BROADER IMPACT (5-6 seconds)
        # ════════════════════════════════════════════════════════════════════════════
        # Visual: Statement on geometric insight and broader implications

        self.phase_4_broader_impact()

        # ════════════════════════════════════════════════════════════════════════════
        # PHASE 5: CALL-TO-ACTION & FINALE (4-5 seconds)
        # ════════════════════════════════════════════════════════════════════════════
        # Visual: Final title, subtitle, and links

        self.phase_5_call_to_action()

        # Final fade out
        self.wait(1.0)

    # ════════════════════════════════════════════════════════════════════════════════
    # PHASE 1: RESULTS METRICS (5-6 seconds)
    # ════════════════════════════════════════════════════════════════════════════════

    def phase_1_results_metrics(self):
        """
        Visual Sequence 1: Results Metrics
        - Animated bar charts showing accuracy improvements at each level
        - Mean Geodesic Error: ↓ 19.5% (special color)
        - Country Accuracy: +8.8%
        - Region Accuracy: +20.1%
        - Subregion Accuracy: +43.2% (emphasized)
        - City Accuracy: +16.8%
        - Animated counters showing percentages
        Duration: ~5-6 seconds
        """

        # ────────────────────────────────────────────────────────────────────────────
        # Title
        # ────────────────────────────────────────────────────────────────────────────
        title = create_serif_title(
            "State-of-the-Art Results",
            font_size=48,
            color=COLORS["text"]
        )
        title.to_edge(UP, buff=0.5)

        self.play(FadeIn(title), run_time=1.0)
        self.wait(0.3)

        # ────────────────────────────────────────────────────────────────────────────
        # Create metric bars/rectangles for each accuracy metric
        # ────────────────────────────────────────────────────────────────────────────

        # Data: label, improvement %, baseline height
        metrics_data = [
            ("Mean Geodesic\nError", 19.5, 0.8),  # Special metric, larger baseline
            ("Country\nAccuracy", 8.8, 0.6),
            ("Region\nAccuracy", 20.1, 0.6),
            ("Subregion\nAccuracy", 43.2, 0.6),  # Biggest improvement
            ("City\nAccuracy", 16.8, 0.6),
        ]

        # Create metric group
        metrics_group = VGroup()
        metric_objects = []

        # Starting X position for bars
        start_x = -4.5
        bar_width = 1.6
        spacing = 0.2

        for i, (label, improvement, baseline_height) in enumerate(metrics_data):
            x_pos = start_x + i * (bar_width + spacing)

            # ────────────────────────────────────────────────────────────────────────
            # Create bar background (unfilled)
            # ────────────────────────────────────────────────────────────────────────
            max_height = 2.0
            bar_bg = Rectangle(
                width=bar_width * 0.8,
                height=max_height,
                fill_color=COLORS["surface"],
                fill_opacity=0.3,
                stroke_color=COLORS["text_muted"],
                stroke_width=1
            )
            bar_bg.move_to([x_pos, -0.5, 0])

            # ────────────────────────────────────────────────────────────────────────
            # Create bar that will animate (growing)
            # ────────────────────────────────────────────────────────────────────────
            # Scale improvement to height (normalize to max 50%)
            bar_height = (improvement / 50.0) * max_height

            # Special color for geodesic error (red-ish tone), others in gold
            if i == 0:  # Mean Geodesic Error
                bar_color = "#e74c3c"  # Red accent for negative metric
            elif i == 3:  # Subregion (43.2% - biggest improvement)
                bar_color = COLORS["gold_light"]
            else:
                bar_color = COLORS["accent"]

            bar = Rectangle(
                width=bar_width * 0.8,
                height=0.01,  # Start with minimal height
                fill_color=bar_color,
                fill_opacity=0.9,
                stroke_color=bar_color,
                stroke_width=1.5
            )
            bar.move_to([x_pos, -0.5, 0])

            # ────────────────────────────────────────────────────────────────────────
            # Create label text
            # ────────────────────────────────────────────────────────────────────────
            label_text = create_sans_body(
                label,
                font_size=16,
                color=COLORS["text"]
            )
            label_text.move_to([x_pos, -1.3, 0])

            # ────────────────────────────────────────────────────────────────────────
            # Create improvement percentage counter
            # ────────────────────────────────────────────────────────────────────────
            counter = DecimalNumber(
                0,
                num_decimal_places=1,
                color=bar_color,
                font_size=20
            )
            counter.move_to([x_pos, bar_height - 0.8, 0])

            # Add percentage sign
            percent_sign = Text(
                "%",
                font=FONTS["sans"],
                color=bar_color,
                font_size=16
            )
            percent_sign.next_to(counter, RIGHT, buff=0.1)

            metric_objects.append({
                "bar": bar,
                "bar_bg": bar_bg,
                "label": label_text,
                "counter": counter,
                "percent": percent_sign,
                "target_height": bar_height,
                "target_value": improvement
            })

            metrics_group.add(bar_bg, bar, label_text, counter, percent_sign)

        # Position metrics group
        metrics_group.move_to([0, 0.5, 0])

        # Show backgrounds
        self.play(FadeIn(metrics_group), run_time=1.0)
        self.wait(0.5)

        # Animate bars and counters growing
        animations = []
        for i, metric in enumerate(metric_objects):
            # Stagger animations
            delay_factor = i * 0.15

            # Animate bar growth
            animations.append(
                metric["bar"].animate.set_height(metric["target_height"])
            )

            # Animate counter
            animations.append(
                ChangingDecimal(
                    metric["counter"],
                    lambda v, tv=metric["target_value"]: tv * v
                )
            )

        # Play all animations together
        self.play(
            *animations,
            run_time=2.5,
            lag_ratio=0.15
        )

        self.wait(1.0)

        # ────────────────────────────────────────────────────────────────────────────
        # Highlight the biggest improvement (Subregion at 43.2%)
        # ────────────────────────────────────────────────────────────────────────────
        subregion_metric = metric_objects[3]
        highlight = Rectangle(
            width=subregion_metric["bar"].width + 0.3,
            height=subregion_metric["bar"].height + 0.3,
            fill_opacity=0.0,
            stroke_color=COLORS["gold_light"],
            stroke_width=3
        )
        highlight.move_to(subregion_metric["bar"].get_center())

        self.play(Create(highlight), run_time=0.8)
        self.wait(0.3)

        # ────────────────────────────────────────────────────────────────────────────
        # Emphasis text for biggest win
        # ────────────────────────────────────────────────────────────────────────────
        emphasis_text = create_sans_body(
            "43.2% Subregion Improvement",
            font_size=24,
            color=COLORS["gold_light"]
        )
        emphasis_text.move_to([4.5, 2.0, 0])

        self.play(FadeIn(emphasis_text), run_time=0.8)
        self.wait(0.8)

        # ────────────────────────────────────────────────────────────────────────────
        # Cleanup Phase 1
        # ────────────────────────────────────────────────────────────────────────────
        self.play(
            FadeOut(title),
            FadeOut(metrics_group),
            FadeOut(highlight),
            FadeOut(emphasis_text),
            run_time=1.5
        )
        self.wait(0.3)

    # ════════════════════════════════════════════════════════════════════════════════
    # PHASE 2: EFFICIENCY COMPARISON (5-6 seconds)
    # ════════════════════════════════════════════════════════════════════════════════

    def phase_2_efficiency_comparison(self):
        """
        Visual Sequence 2: Efficiency Comparison
        - Side-by-side comparison
        - LEFT: "240k entity embeddings" (small box, gold highlight)
        - RIGHT: "5M+ image embeddings" (large box, muted/faded)
        - CENTER: "95% Reduction" (large text, gold accent)
        - Subtitle: "in storage & search complexity"
        Duration: ~5-6 seconds
        """

        # ────────────────────────────────────────────────────────────────────────────
        # Title
        # ────────────────────────────────────────────────────────────────────────────
        title = create_serif_title(
            "Efficiency Breakthrough",
            font_size=48,
            color=COLORS["text"]
        )
        title.to_edge(UP, buff=0.5)

        self.play(FadeIn(title), run_time=1.0)
        self.wait(0.3)

        # ────────────────────────────────────────────────────────────────────────────
        # Create LEFT box: Small entity embeddings
        # ────────────────────────────────────────────────────────────────────────────
        left_box = Rectangle(
            width=1.5,
            height=1.5,
            fill_color=COLORS["accent"],
            fill_opacity=0.4,
            stroke_color=COLORS["accent"],
            stroke_width=2.5
        )
        left_box.move_to([-2.5, 0, 0])

        left_label = create_sans_body(
            "240k\nEntity\nEmbeddings",
            font_size=20,
            color=COLORS["accent"]
        )
        left_label.move_to(left_box.get_center())

        # ────────────────────────────────────────────────────────────────────────────
        # Create RIGHT box: Large image embeddings (much larger)
        # ────────────────────────────────────────────────────────────────────────────
        right_box = Rectangle(
            width=4.0,
            height=4.0,
            fill_color=COLORS["surface"],
            fill_opacity=0.2,
            stroke_color=COLORS["text_muted"],
            stroke_width=2
        )
        right_box.move_to([2.5, 0, 0])

        right_label = create_sans_body(
            "5M+\nImage\nEmbeddings",
            font_size=24,
            color=COLORS["text_muted"]
        )
        right_label.move_to(right_box.get_center())

        # Fade in both boxes
        self.play(
            FadeIn(left_box),
            FadeIn(left_label),
            run_time=1.0
        )
        self.wait(0.3)

        self.play(
            FadeIn(right_box),
            FadeIn(right_label),
            run_time=1.2
        )
        self.wait(0.5)

        # ────────────────────────────────────────────────────────────────────────────
        # Create center comparison text: "95% Reduction"
        # ────────────────────────────────────────────────────────────────────────────
        reduction_number = create_serif_title(
            "95%",
            font_size=72,
            color=COLORS["gold_light"]
        )
        reduction_number.move_to([0, 1.2, 0])

        reduction_label = create_sans_body(
            "Reduction",
            font_size=28,
            color=COLORS["accent"]
        )
        reduction_label.move_to([0, 0.3, 0])

        subtitle = create_sans_body(
            "in storage & search\ncomplexity",
            font_size=20,
            color=COLORS["text_muted"]
        )
        subtitle.move_to([0, -0.5, 0])

        # Animate center text appearing with emphasis
        self.play(
            FadeIn(reduction_number),
            run_time=1.0
        )
        self.wait(0.2)

        self.play(
            FadeIn(reduction_label),
            FadeIn(subtitle),
            run_time=0.8
        )
        self.wait(1.2)

        # ────────────────────────────────────────────────────────────────────────────
        # Add arrow or visual connection showing comparison
        # ────────────────────────────────────────────────────────────────────────────
        # Create a visual line showing the dramatic size difference
        comparison_arrow = DoubleArrow(
            start=left_box.get_right() + [0.2, 0, 0],
            end=right_box.get_left() - [0.2, 0, 0],
            color=COLORS["accent"],
            stroke_width=2.5,
            buff=0.1
        )

        self.play(FadeIn(comparison_arrow), run_time=0.6)
        self.wait(0.5)

        # ────────────────────────────────────────────────────────────────────────────
        # Cleanup Phase 2
        # ────────────────────────────────────────────────────────────────────────────
        self.play(
            FadeOut(title),
            FadeOut(left_box),
            FadeOut(left_label),
            FadeOut(right_box),
            FadeOut(right_label),
            FadeOut(reduction_number),
            FadeOut(reduction_label),
            FadeOut(subtitle),
            FadeOut(comparison_arrow),
            run_time=1.5
        )
        self.wait(0.3)

    # ════════════════════════════════════════════════════════════════════════════════
    # PHASE 3: INTERPRETABILITY (5-6 seconds)
    # ════════════════════════════════════════════════════════════════════════════════

    def phase_3_interpretability(self):
        """
        Visual Sequence 3: Interpretability
        - Show entity path example: Image → Germany → Bavaria → Munich
        - Use nested containers or step-by-step reveals with arrows
        - Gold highlights for matched entities
        - Text: "Know WHICH ENTITIES matched"
        Duration: ~5-6 seconds
        """

        # ────────────────────────────────────────────────────────────────────────────
        # Title
        # ────────────────────────────────────────────────────────────────────────────
        title = create_serif_title(
            "Interpretable Results",
            font_size=48,
            color=COLORS["text"]
        )
        title.to_edge(UP, buff=0.5)

        self.play(FadeIn(title), run_time=1.0)
        self.wait(0.3)

        # ────────────────────────────────────────────────────────────────────────────
        # Create hierarchical path visualization
        # ────────────────────────────────────────────────────────────────────────────

        # Define path hierarchy
        path_elements = [
            ("Street View\nImage", 2.0),
            ("Germany", 1.6),
            ("Bavaria", 1.2),
            ("Munich", 0.8)
        ]

        path_group = VGroup()
        path_objects = []

        # Starting position
        start_y = 1.0
        step_down = 0.8

        for i, (label, width) in enumerate(path_elements):
            y_pos = start_y - (i * step_down)

            # Create container box
            container = Rectangle(
                width=width,
                height=0.6,
                fill_color=COLORS["accent"],
                fill_opacity=0.2 if i == 0 else 0.1,
                stroke_color=COLORS["accent"] if i == 0 else COLORS["text_muted"],
                stroke_width=2.5 if i == 0 else 1.5
            )
            container.move_to([-2.0 + (i * 0.3), y_pos, 0])

            # Create label text
            label_text = create_sans_body(
                label,
                font_size=20 if i == 0 else 18,
                color=COLORS["gold_light"] if i == 0 else COLORS["text"]
            )
            label_text.move_to(container.get_center())

            path_objects.append({
                "container": container,
                "label": label_text,
                "y_pos": y_pos
            })

            path_group.add(container, label_text)

        # Fade in first element (image)
        self.play(
            FadeIn(path_objects[0]["container"]),
            FadeIn(path_objects[0]["label"]),
            run_time=1.0
        )
        self.wait(0.3)

        # Reveal path elements one by one
        for i in range(1, len(path_objects)):
            # Create arrow pointing down
            arrow = Arrow(
                start=[path_objects[i-1]["container"].get_bottom()[0],
                       path_objects[i-1]["container"].get_bottom()[1] - 0.1, 0],
                end=[path_objects[i]["container"].get_top()[0],
                     path_objects[i]["container"].get_top()[1] + 0.1, 0],
                color=COLORS["gold_light"] if i == 1 else COLORS["text_muted"],
                stroke_width=2,
                max_tip_length_to_length_ratio=0.15,
                buff=0.05
            )

            # Animate arrow and new element
            self.play(
                Create(arrow),
                FadeIn(path_objects[i]["container"]),
                FadeIn(path_objects[i]["label"]),
                run_time=0.8
            )
            self.wait(0.2)

        self.wait(0.5)

        # ────────────────────────────────────────────────────────────────────────────
        # Add interpretability message
        # ────────────────────────────────────────────────────────────────────────────
        interpretability_msg = create_sans_body(
            "Know WHICH ENTITIES matched",
            font_size=24,
            color=COLORS["gold_light"]
        )
        interpretability_msg.move_to([3.0, 1.2, 0])

        self.play(FadeIn(interpretability_msg), run_time=0.8)
        self.wait(0.8)

        # ────────────────────────────────────────────────────────────────────────────
        # Highlight the final location (Munich) with special effect
        # ────────────────────────────────────────────────────────────────────────────
        final_highlight = Rectangle(
            width=path_objects[-1]["container"].width + 0.3,
            height=path_objects[-1]["container"].height + 0.3,
            fill_opacity=0.0,
            stroke_color=COLORS["gold_light"],
            stroke_width=3
        )
        final_highlight.move_to(path_objects[-1]["container"].get_center())

        self.play(Create(final_highlight), run_time=0.5)
        self.wait(0.3)

        # ────────────────────────────────────────────────────────────────────────────
        # Cleanup Phase 3
        # ────────────────────────────────────────────────────────────────────────────
        self.play(
            FadeOut(title),
            FadeOut(path_group),
            FadeOut(interpretability_msg),
            FadeOut(final_highlight),
            run_time=1.5
        )
        self.wait(0.3)

    # ════════════════════════════════════════════════════════════════════════════════
    # PHASE 4: BROADER IMPACT (5-6 seconds)
    # ════════════════════════════════════════════════════════════════════════════════

    def phase_4_broader_impact(self):
        """
        Visual Sequence 4: Broader Impact
        - Large text statement: "Hyperbolic geometry is the right tool for hierarchical data"
        - Optional: Subtle hyperbolic disk visualization in background
        - Emphasize elegance and broader implications
        Duration: ~5-6 seconds
        """

        # ────────────────────────────────────────────────────────────────────────────
        # Create subtle hyperbolic background visualization
        # ────────────────────────────────────────────────────────────────────────────
        hyperbolic_bg = VGroup()

        # Create radial lines (suggesting hyperbolic geometry)
        num_radial_lines = 16
        for i in range(num_radial_lines):
            angle = 2 * np.pi * i / num_radial_lines
            end_x = 2.0 * np.cos(angle)
            end_y = 2.0 * np.sin(angle)

            line = Line(
                start=[0, 0, 0],
                end=[end_x, end_y, 0],
                color=COLORS["accent"],
                stroke_width=0.6,
                stroke_opacity=0.1
            )
            hyperbolic_bg.add(line)

        # Create concentric circles (hyperbolic structure)
        for radius in [0.6, 1.2, 1.8]:
            circle = Circle(
                radius=radius,
                color=COLORS["accent"],
                fill_opacity=0.0,
                stroke_width=0.6,
                stroke_opacity=0.08
            )
            hyperbolic_bg.add(circle)

        # Position background
        hyperbolic_bg.move_to([0, 0, 0])

        self.play(FadeIn(hyperbolic_bg), run_time=1.0)
        self.wait(0.2)

        # ────────────────────────────────────────────────────────────────────────────
        # Create main statement text
        # ────────────────────────────────────────────────────────────────────────────
        statement = create_serif_title(
            "Hyperbolic Geometry",
            font_size=56,
            color=COLORS["gold_light"]
        )
        statement.move_to([0, 1.5, 0])

        subtitle_statement = create_sans_body(
            "is the right tool for\nhierarchical data",
            font_size=32,
            color=COLORS["text"]
        )
        subtitle_statement.move_to([0, 0.2, 0])

        # Animate text appearing
        self.play(FadeIn(statement), run_time=1.2)
        self.wait(0.3)

        self.play(FadeIn(subtitle_statement), run_time=1.0)
        self.wait(2.0)

        # ────────────────────────────────────────────────────────────────────────────
        # Add supporting insight
        # ────────────────────────────────────────────────────────────────────────────
        insight = create_sans_body(
            "Exponential volume = Exponential hierarchy",
            font_size=24,
            color=COLORS["text_muted"]
        )
        insight.move_to([0, -1.2, 0])

        self.play(FadeIn(insight), run_time=0.8)
        self.wait(0.8)

        # ────────────────────────────────────────────────────────────────────────────
        # Cleanup Phase 4
        # ────────────────────────────────────────────────────────────────────────────
        self.play(
            FadeOut(hyperbolic_bg),
            FadeOut(statement),
            FadeOut(subtitle_statement),
            FadeOut(insight),
            run_time=1.5
        )
        self.wait(0.3)

    # ════════════════════════════════════════════════════════════════════════════════
    # PHASE 5: CALL-TO-ACTION & FINALE (4-5 seconds)
    # ════════════════════════════════════════════════════════════════════════════════

    def phase_5_call_to_action(self):
        """
        Visual Sequence 5: Call-to-Action & Finale
        - Title: "HierLoc: Hierarchical Visual Geolocation"
        - Subtitle: "Learn More"
        - Links/CTA: "Paper • Code • Website"
        - Optional: Subtle glow effect
        - Tone: Triumphant celebration
        Duration: ~4-5 seconds
        """

        # ────────────────────────────────────────────────────────────────────────────
        # Main title
        # ────────────────────────────────────────────────────────────────────────────
        main_title = create_serif_title(
            "HierLoc",
            font_size=80,
            color=COLORS["text"]
        )
        main_title.move_to([0, 1.8, 0])

        # Animate title in
        self.play(FadeIn(main_title), run_time=1.0)
        self.wait(0.2)

        # ────────────────────────────────────────────────────────────────────────────
        # Subtitle
        # ────────────────────────────────────────────────────────────────────────────
        subtitle = create_sans_body(
            "Hierarchical Visual Geolocation",
            font_size=28,
            color=COLORS["gold_light"]
        )
        subtitle.move_to([0, 0.9, 0])

        self.play(FadeIn(subtitle), run_time=0.8)
        self.wait(0.3)

        # ────────────────────────────────────────────────────────────────────────────
        # Call-to-action text
        # ────────────────────────────────────────────────────────────────────────────
        cta_label = create_sans_body(
            "Learn More",
            font_size=24,
            color=COLORS["text_muted"]
        )
        cta_label.move_to([0, 0.1, 0])

        self.play(FadeIn(cta_label), run_time=0.6)
        self.wait(0.3)

        # ────────────────────────────────────────────────────────────────────────────
        # Links: Paper • Code • Website
        # ────────────────────────────────────────────────────────────────────────────
        links_text = create_sans_body(
            "Paper  •  Code  •  Website",
            font_size=22,
            color=COLORS["accent"]
        )
        links_text.move_to([0, -0.6, 0])

        # Add subtle underline to make it look clickable
        underline = Line(
            start=links_text.get_left() - [0.1, 0, 0],
            end=links_text.get_right() + [0.1, 0, 0],
            color=COLORS["accent"],
            stroke_width=1.5,
            stroke_opacity=0.4
        )
        underline.next_to(links_text, DOWN, buff=0.1)

        self.play(FadeIn(links_text), run_time=0.7)
        self.play(FadeIn(underline), run_time=0.5)
        self.wait(1.2)

        # ────────────────────────────────────────────────────────────────────────────
        # Optional: Add subtle glow effect around title
        # ────────────────────────────────────────────────────────────────────────────
        glow = Circle(
            radius=2.0,
            fill_opacity=0.0,
            stroke_color=COLORS["accent"],
            stroke_width=1,
            stroke_opacity=0.15
        )
        glow.move_to(main_title.get_center())

        self.play(FadeIn(glow), run_time=0.6)
        self.wait(1.5)

        # ────────────────────────────────────────────────────────────────────────────
        # Final fade out to black
        # ────────────────────────────────────────────────────────────────────────────
        self.play(
            FadeOut(main_title),
            FadeOut(subtitle),
            FadeOut(cta_label),
            FadeOut(links_text),
            FadeOut(underline),
            FadeOut(glow),
            run_time=2.0
        )
        self.wait(0.5)


if __name__ == "__main__":
    print("Scene 5: Results & Impact")
    print("Duration: ~30 seconds")
    print("5 phases: Results → Efficiency → Interpretability → Impact → CTA")
