"""
Scene 5: RESULTS - OSV5M Benchmark Performance with Animated Bar Charts
Duration: ~45 seconds
Purpose: Show concrete results from Table 1 using animated bar charts

OSV5M Benchmark Results:
- Methods: SC 0-shot, Regression, ISNs, Hybrid, SC Retrieval, RFM S2, LocDiff
- HierLoc (ViT-L14): GeoScore=3850, Distance=1067, Country=80.1%, Region=52.9%, Subregion=39.0%, City=22.2%
- HierLoc (DinoV3): GeoScore=3963, Distance=861, Country=82.9%, Region=55.0%, Subregion=40.7%, City=23.3%
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


class BarChart(VGroup):
    """Custom animated bar chart for HierLoc results"""

    def __init__(self, title, data, axis_label, y_max=None, bar_width=0.6, **kwargs):
        """
        Create a bar chart

        Args:
            title: Chart title
            data: List of (label, value) tuples
            axis_label: Label for Y-axis
            y_max: Maximum Y value (auto-calculated if None)
            bar_width: Width of each bar
        """
        super().__init__(**kwargs)

        self.title = title
        self.data = data
        self.axis_label = axis_label
        self.y_max = y_max or max([v for _, v in data]) * 1.15
        self.bar_width = bar_width

        # Create chart components
        self._create_bars()

    def _create_bars(self):
        """Create the bar chart structure"""
        # Determine colors: highlight HierLoc in gold, others in muted
        bars_group = VGroup()
        labels_group = VGroup()

        num_bars = len(self.data)
        bar_spacing = 0.8
        total_width = num_bars * bar_spacing
        start_x = -total_width / 2

        for i, (label, value) in enumerate(self.data):
            x_pos = start_x + i * bar_spacing

            # Determine color: HierLoc bars in accent/gold, others in muted
            is_hierloc = "HierLoc" in label or "HierLoc" in str(label)
            bar_color = COLORS["accent"] if is_hierloc else COLORS["text_muted"]

            # Create bar (height normalized to y_max)
            bar_height = (value / self.y_max) * 2.5  # 2.5 units = full height
            bar = Rectangle(
                width=self.bar_width,
                height=0,  # Start at 0, will animate
                fill_color=bar_color,
                fill_opacity=0.8,
                stroke_color=bar_color,
                stroke_width=1.5,
            )
            bar.move_to([x_pos, -1.25, 0])  # Baseline at y=-1.25

            # Store the target height for animation
            bar.target_height = bar_height

            # Create label
            label_text = Text(
                label,
                font=FONTS["sans"],
                font_size=10,
                color=COLORS["text"],
            )
            label_text.next_to(bar, DOWN, buff=0.2)

            # Create value label (will appear at top of bar)
            value_text = Text(
                f"{value:.0f}" if value > 100 else f"{value:.1f}",
                font=FONTS["sans"],
                font_size=9,
                color=bar_color,
            )
            value_text.bar = bar  # Reference for positioning

            bars_group.add(bar)
            labels_group.add(label_text)
            labels_group.add(value_text)

        # Add axes
        y_axis = Line(
            start=[-total_width/2 - 0.3, -1.25, 0],
            end=[-total_width/2 - 0.3, 1.25, 0],
            color=COLORS["text_muted"],
            stroke_width=1,
        )
        x_axis = Line(
            start=[-total_width/2 - 0.3, -1.25, 0],
            end=[total_width/2 + 0.3, -1.25, 0],
            color=COLORS["text_muted"],
            stroke_width=1,
        )

        # Title
        title_text = Text(
            self.title,
            font=FONTS["sans"],
            font_size=16,
            color=COLORS["text"],
        )
        title_text.move_to([0, 2.2, 0])

        # Axis label
        axis_label_text = Text(
            self.axis_label,
            font=FONTS["sans"],
            font_size=10,
            color=COLORS["text_muted"],
        )
        axis_label_text.move_to([-total_width/2 - 0.8, 0, 0])

        self.add(y_axis, x_axis, bars_group, labels_group, title_text, axis_label_text)
        self.bars = bars_group
        self.value_labels = [obj for obj in labels_group if isinstance(obj, Text)]


class Scene5Results(Scene):
    """Results: OSV5M Benchmark with animated bar charts"""

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
                color=COLORS["gold_light"] if i == 4 else COLORS["text_muted"],
                fill_opacity=1.0 if i == 4 else 0.4
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
            "Results: OSV5M Benchmark",
            font=FONTS["sans"],
            font_size=48,
            color=COLORS["text"]
        )
        title.move_to([0, 2.5, 0])

        self.play(FadeIn(title, run_time=1.0))
        self.wait(0.5)

        # ============================================================
        # SEQUENCE 2: GeoScore Chart (1.5-10s)
        # ============================================================
        # Data from Table 1 (selecting key baselines + HierLoc)
        geoscore_data = [
            ("SC 0-shot", 2273),
            ("Regression", 3028),
            ("ISNs", 3331),
            ("SC Retrieval", 3597),
            ("RFM S₂", 3767),
            ("HierLoc\n(ViT-L14)", 3850),
            ("HierLoc\n(DinoV3)", 3963),
        ]

        geoscore_chart = BarChart(
            "GeoScore (higher is better)",
            geoscore_data,
            "GeoScore",
            y_max=4200
        )
        geoscore_chart.scale(0.9)
        geoscore_chart.move_to([0, 0.8, 0])

        self.play(FadeIn(geoscore_chart, run_time=0.8))
        self.wait(0.3)

        # Animate bars growing
        for bar in geoscore_chart.bars:
            self.play(
                bar.animate.set(height=bar.target_height),
                run_time=0.6
            )

        self.wait(2.0)
        self.play(FadeOut(title, geoscore_chart, run_time=0.6))
        self.wait(0.3)

        # ============================================================
        # SEQUENCE 3: Distance Chart (10-18s)
        # ============================================================
        distance_data = [
            ("SC 0-shot", 2854),
            ("Regression", 1481),
            ("ISNs", 2308),
            ("SC Retrieval", 1386),
            ("RFM S₂", 1069),
            ("HierLoc\n(ViT-L14)", 1067),
            ("HierLoc\n(DinoV3)", 861),
        ]

        distance_chart = BarChart(
            "Distance Error in km (lower is better)",
            distance_data,
            "Distance (km)",
            y_max=3000
        )
        distance_chart.scale(0.9)
        distance_chart.move_to([0, 0.8, 0])

        self.play(FadeIn(distance_chart, run_time=0.8))
        self.wait(0.3)

        # Animate bars
        for bar in distance_chart.bars:
            self.play(
                bar.animate.set(height=bar.target_height),
                run_time=0.6
            )

        self.wait(2.0)
        self.play(FadeOut(distance_chart, run_time=0.6))
        self.wait(0.3)

        # ============================================================
        # SEQUENCE 4: Classification Accuracy (18-40s)
        # ============================================================
        # Create 4 subplots for Country, Region, Subregion, City
        accuracy_metrics = [
            {
                "title": "Country Accuracy",
                "data": [
                    ("SC 0-shot", 38.4),
                    ("Regression", 56.5),
                    ("ISNs", 66.8),
                    ("SC Retrieval", 73.4),
                    ("RFM S₂", 76.2),
                    ("HierLoc (ViT)", 80.1),
                    ("HierLoc (D3)", 82.9),
                ],
            },
            {
                "title": "Region Accuracy",
                "data": [
                    ("SC 0-shot", 20.8),
                    ("Regression", 16.3),
                    ("ISNs", 39.4),
                    ("SC Retrieval", 45.8),
                    ("RFM S₂", 44.2),
                    ("HierLoc (ViT)", 52.9),
                    ("HierLoc (D3)", 55.0),
                ],
            },
            {
                "title": "Subregion Accuracy",
                "data": [
                    ("SC 0-shot", 9.9),
                    ("Regression", 1.5),
                    ("ISNs", 10.3),
                    ("SC Retrieval", 28.4),
                    ("RFM S₂", 0.0),  # Not reported
                    ("HierLoc (ViT)", 39.0),
                    ("HierLoc (D3)", 40.7),
                ],
            },
            {
                "title": "City Accuracy",
                "data": [
                    ("SC 0-shot", 14.8),
                    ("Regression", 0.7),
                    ("ISNs", 4.2),
                    ("SC Retrieval", 19.9),
                    ("RFM S₂", 5.4),
                    ("HierLoc (ViT)", 22.2),
                    ("HierLoc (D3)", 23.3),
                ],
            },
        ]

        # Display all 4 accuracy charts in a 2x2 grid
        charts = []
        positions = [
            [-3.5, 1.2, 0],   # Top-left
            [3.5, 1.2, 0],    # Top-right
            [-3.5, -1.2, 0],  # Bottom-left
            [3.5, -1.2, 0],   # Bottom-right
        ]

        for metric, pos in zip(accuracy_metrics, positions):
            chart = BarChart(
                metric["title"],
                metric["data"],
                "Accuracy (%)",
                y_max=100
            )
            chart.scale(0.65)
            chart.move_to(pos)
            charts.append(chart)

        # Fade in title
        accuracy_title = Text(
            "Classification Accuracy across Hierarchy Levels",
            font=FONTS["sans"],
            font_size=20,
            color=COLORS["accent"]
        )
        accuracy_title.move_to([0, 2.8, 0])

        self.play(FadeIn(accuracy_title, run_time=0.6))
        self.wait(0.3)

        # Fade in all 4 charts
        for chart in charts:
            self.play(FadeIn(chart, run_time=0.7))

        self.wait(0.5)

        # Animate bars in all charts simultaneously
        all_bars = []
        for chart in charts:
            all_bars.extend(chart.bars)

        # Animate all bars together for better visual impact
        self.play(
            *[bar.animate.set(height=bar.target_height) for bar in all_bars],
            run_time=1.2
        )

        self.wait(3.0)

        # ============================================================
        # SEQUENCE 5: Key Insight (40-48s)
        # ============================================================
        self.play(
            FadeOut(accuracy_title, *charts, run_time=0.6)
        )
        self.wait(0.3)

        insight = Text(
            "Hyperbolic geometry\nscales to 240k entities\nwith 240 embeddings",
            font=FONTS["sans"],
            font_size=28,
            color=COLORS["gold_light"],
            line_spacing=1.4
        )
        insight.move_to([0, 1.0, 0])

        key_metrics = VGroup(
            Text("-19.5% geodesic error", font=FONTS["sans"], font_size=16, color=COLORS["accent"]),
            Text("+43.2% subregion accuracy", font=FONTS["sans"], font_size=16, color=COLORS["accent"]),
        )
        key_metrics.arrange(DOWN, buff=0.4)
        key_metrics.next_to(insight, DOWN, buff=0.8)

        self.play(FadeIn(insight, run_time=0.8))
        self.wait(0.3)
        self.play(FadeIn(key_metrics, run_time=0.8))
        self.wait(2.0)

        # ============================================================
        # SEQUENCE 6: Final Fade (48-50s)
        # ============================================================
        self.play(
            FadeOut(insight, key_metrics, run_time=1.0)
        )
        self.wait(0.5)
