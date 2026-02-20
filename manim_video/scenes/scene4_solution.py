"""
Scene 4: THE SOLUTION - HierLoc Architecture
Duration: ~70 seconds
Purpose: Show how HierLoc works (from paper Figure 1)

Pipeline:
1. Image encoding
2. Mapping to hyperbolic entity space
3. Hierarchical search (country → region → city)
4. Efficiency gains (240K entities vs 5M+ images)
"""

from manim import *
import numpy as np
from config import COLORS, FONTS, setup_manim_config

setup_manim_config(quality="h")


class Scene4Solution(Scene):
    """HierLoc solution architecture"""

    def construct(self):
        self.camera.background_color = COLORS["bg"]

        # ============================================================
        # SEQUENCE 1: Title (0-1s)
        # ============================================================
        title = Text(
            "HierLoc Solution",
            font=FONTS["sans"],
            font_size=64,
            color=COLORS["text"],
            
        )
        title.to_edge(UP, buff=0.5)

        self.play(FadeIn(title, run_time=1.0))
        self.wait(0.5)

        # ============================================================
        # SEQUENCE 2: Pipeline Overview (1.5-20s)
        # ============================================================
        # Step 1: Image input (LEFT) at [-3.0, 1.2, 0]
        image_box = Rectangle(
            width=2.0, height=1.6,
            stroke_color=COLORS["accent"],
            stroke_width=2,
            fill_opacity=0.1,
            fill_color=COLORS["surface"]
        )
        image_box.move_to([-3.0, 1.2, 0])

        image_label = Text(
            "Image",
            font=FONTS["sans"],
            font_size=20,
            color=COLORS["accent"]
        )
        image_label.move_to(image_box.get_center())

        self.play(Create(image_box, run_time=0.6))
        self.play(FadeIn(image_label, run_time=0.3))
        self.wait(0.8)

        # Arrow 1: Encoding
        arrow1 = Arrow(
            start=[-2.0, 1.2, 0],
            end=[-0.8, 1.2, 0],
            buff=0.1,
            color=COLORS["accent"],
            stroke_width=2.5,
            tip_length=0.15
        )
        label1 = Text("Encode", font=FONTS["sans"], font_size=16, color=COLORS["accent"])
        label1.next_to(arrow1, UP, buff=0.15)

        self.play(Create(arrow1, run_time=0.5))
        self.play(FadeIn(label1, run_time=0.3))
        self.wait(0.6)

        # Step 2: Embedding vector
        embedding_box = Rectangle(
            width=1.4, height=1.4,
            stroke_color=COLORS["accent"],
            stroke_width=2,
            fill_opacity=0.08,
            fill_color=COLORS["accent"]
        )
        embedding_box.move_to([0.2, 1.2, 0])

        embedding_label = Text(
            "z_img",
            font=FONTS["sans"],
            font_size=18,
            color=COLORS["accent"]
        )
        embedding_label.move_to(embedding_box.get_center())

        self.play(Create(embedding_box, run_time=0.6))
        self.play(FadeIn(embedding_label, run_time=0.3))
        self.wait(0.8)

        # Arrow 2: Map to hyperbolic space
        arrow2 = Arrow(
            start=[0.9, 1.2, 0],
            end=[2.2, 1.2, 0],
            buff=0.1,
            color=COLORS["gold_light"],
            stroke_width=3,
            tip_length=0.15
        )
        label2 = Text("Map", font=FONTS["sans"], font_size=16, color=COLORS["gold_light"])
        label2.next_to(arrow2, UP, buff=0.15)

        self.play(Create(arrow2, run_time=0.5))
        self.play(FadeIn(label2, run_time=0.3))
        self.wait(0.6)

        # Step 3: Entity space visualization
        entity_circle = Circle(
            radius=0.6,
            color=COLORS["accent"],
            stroke_width=2,
            fill_opacity=0.08,
            fill_color=COLORS["accent"]
        )
        entity_circle.move_to([3.2, 1.2, 0])

        # Small dots inside representing entities
        dots = VGroup()
        for angle in np.linspace(0, 2*np.pi, 7)[:-1]:
            dot = Dot(
                point=[3.2 + 0.4*np.cos(angle), 1.2 + 0.4*np.sin(angle), 0],
                radius=0.08,
                color=COLORS["accent"],
                fill_opacity=0.8
            )
            dots.add(dot)

        entity_label = Text(
            "Entity Space\n(240K entities)",
            font=FONTS["sans"],
            font_size=14,
            color=COLORS["accent"],
            line_spacing=1.0
        )
        entity_label.next_to(entity_circle, DOWN, buff=0.4)

        self.play(Create(entity_circle, run_time=0.6))
        self.play(FadeIn(dots, run_time=0.4))
        self.play(FadeIn(entity_label, run_time=0.3))
        self.wait(1.0)

        # ============================================================
        # SEQUENCE 3: Hierarchical Search (20-40s)
        # ============================================================
        search_title = Text(
            "Hierarchical Search",
            font=FONTS["sans"],
            font_size=28,
            color=COLORS["accent"],
            
        )
        search_title.move_to([0, -0.5, 0])

        search_steps = Text(
            "1. Match to countries\n2. Refine to regions\n3. Narrow to cities",
            font=FONTS["sans"],
            font_size=20,
            color=COLORS["text_muted"],
            line_spacing=1.3
        )
        search_steps.move_to([0, -1.8, 0])

        self.play(FadeOut(arrow1, label1, arrow2, label2, run_time=0.5))
        self.wait(0.3)
        self.play(FadeIn(search_title, search_steps, run_time=0.8))
        self.wait(2.5)

        # ============================================================
        # SEQUENCE 4: Efficiency Gains (40-70s)
        # ============================================================
        self.play(
            FadeOut(image_box, image_label, embedding_box, embedding_label,
                   entity_circle, dots, entity_label, search_title, search_steps,
                   run_time=0.8)
        )
        self.wait(0.3)

        # Efficiency comparison
        efficiency_title = Text(
            "Efficiency",
            font=FONTS["sans"],
            font_size=36,
            color=COLORS["accent"],
            
        )
        efficiency_title.move_to([0, 2.0, 0])

        # Left column: Traditional
        trad_header = Text(
            "Traditional",
            font=FONTS["sans"],
            font_size=20,
            color=COLORS["text_muted"],
            
        )
        trad_metrics = Text(
            "5M+ embeddings\nO(N) search\nHigh memory",
            font=FONTS["sans"],
            font_size=18,
            color=COLORS["text_muted"],
            line_spacing=1.4
        )
        trad = VGroup(trad_header, trad_metrics).arrange(DOWN, buff=0.3)
        trad.move_to([-2.2, 0.5, 0])

        # Right column: HierLoc
        hierloc_header = Text(
            "HierLoc",
            font=FONTS["sans"],
            font_size=20,
            color=COLORS["accent"],
            
        )
        hierloc_metrics = Text(
            "240K entities\nSub-linear search\nEfficient",
            font=FONTS["sans"],
            font_size=18,
            color=COLORS["gold_light"],
            line_spacing=1.4
        )
        hierloc = VGroup(hierloc_header, hierloc_metrics).arrange(DOWN, buff=0.3)
        hierloc.move_to([2.2, 0.5, 0])

        self.play(FadeIn(efficiency_title, run_time=0.6))
        self.wait(0.4)
        self.play(FadeIn(trad, hierloc, run_time=0.8))
        self.wait(1.5)

        # Highlight the key improvement
        improvement = Text(
            "95% fewer embeddings to store",
            font=FONTS["sans"],
            font_size=28,
            color=COLORS["accent"],
            
        )
        improvement.move_to([0, -2.2, 0])

        self.play(FadeIn(improvement, run_time=0.8))
        self.wait(2.5)

        # ============================================================
        # SEQUENCE 5: Transition (70s)
        # ============================================================
        self.play(
            FadeOut(title, efficiency_title, trad, hierloc, improvement, run_time=1.0)
        )
        self.wait(0.5)
