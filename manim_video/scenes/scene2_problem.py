"""
Scene 2: Three Approaches to Visual Geolocation - Sequential Deep Dive
Duration: ~55 seconds (tightened pacing)
Purpose: Explain each approach one at a time with clean, readable layout

Narrative:
- Narrative intro: "These three approaches represent different tradeoffs..."
- Sequence 1: Classification - Divide Earth into grid cells
- Sequence 2: Divider slide - highlight Diffusion as next
- Sequence 3: Diffusion - Generative model approach (spiral convergence)
- Sequence 4: Divider slide - highlight Retrieval as next
- Sequence 5: Retrieval - Database matching on Earth surface
- Sequence 6: Final transition

Changes from v1:
- Fix 1: Grid cell color changed from #000000 to COLORS["accent"]
- Fix 2: Diffusion dots changed from #000000 to COLORS["accent"]
- Fix 3: Highlight FadeIn 0.1->0.15s, FadeOut 0.08->0.12s
- Fix 4: Extracted show_divider_slide() helper (eliminates duplication)
- Fix 5: Divider 1 highlights Diffusion (idx 1), Divider 2 highlights Retrieval (idx 2)
- Fix 6: Grid animation uses LaggedStart, 2s total (was ~6s loop)
- Fix 7: Diffusion uses spiral convergence (was random walk)
- Fix 8: Narrative intro 3.5s added before Sequence 1
- Fix 9: Descriptions expanded to 2-line explanations
- Fix 10: Between-sequence waits reduced 1.5s -> 0.8s
- Fix 11: Progress dot uses COLORS["accent"] (was COLORS["gold_light"])
- Fix 12: Title font_size 52 -> 42
- Fix 13: FadeIn/FadeOut use rate_func=rate_functions.ease_in_out_sine
"""

import os
from manim import *
from manim import rate_functions
import numpy as np
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from config import COLORS, FONTS, setup_manim_config
from utils import (
    create_serif_title,
    create_sans_body,
    create_mono_code,
    apply_color,
    create_accent_highlight,
    get_easing_function
)
from layout import ObjectPositioner

setup_manim_config(quality="high_quality")


class Scene2Problem(Scene):
    """Sequential exploration of 3 geolocation approaches"""

    # ================================================================
    # HELPER: Divider Slide with Animated Earth Visualizations + Golden Highlight
    # ================================================================
    def show_divider_slide(self, active_next_index, previous_index=None):
        """
        Display the three-method navigation divider slide with Earth animations and golden highlight.

        Args:
            active_next_index: 0=Classification, 1=Diffusion, 2=Retrieval
                               A golden rectangle highlight indicates this section.
            previous_index: If provided, highlight animates from previous_index to active_next_index

        The method handles its own full animation lifecycle:
        FadeIn -> run animations -> wait -> FadeOut
        """
        earth_path = "/Volumes/SSD/iclr-website/static/images/earth-icon.svg"

        divider_title = create_sans_body(
            "Three Approaches to Geolocation",
            font_size=36,
            color=COLORS["accent"]
        )
        divider_title.move_to([0, 2.6, 0])

        # Layout: 3 columns at specific x positions
        section_specs = [
            ("Classification", -4.35, COLORS["accent"], COLORS["accent"]),
            ("Diffusion",       0.0, COLORS["accent"], COLORS["accent"]),
            ("Retrieval",       4.35, COLORS["gold_light"], COLORS["text_muted"]),
        ]

        earth_radius = 0.45  # Mini Earth radius
        earth_height = earth_radius * 2  # 0.90 units tall
        earth_y_center = 0.3  # Vertical center of Earth

        section_groups = []  # Will store VGroup for each section

        # ============================================================
        # BUILD ALL THREE SECTIONS WITH ANIMATIONS
        # ============================================================
        for sec_idx, (method_name, x_center, circle_color, dot_color) in enumerate(section_specs):
            section_group = VGroup()

            # --- Mini Earth SVG ---
            if os.path.exists(earth_path):
                try:
                    earth_svg = SVGMobject(file_name=earth_path)
                    earth_svg.set_height(earth_height)
                    earth_svg.move_to([x_center, earth_y_center, 0])
                    section_group.add(earth_svg)
                except Exception:
                    pass

            # --- Circle frame ---
            circle_frame = Circle(
                radius=earth_radius,
                color=circle_color,
                fill_opacity=0,
                stroke_opacity=0.8,
                stroke_width=2
            )
            circle_frame.move_to([x_center, earth_y_center, 0])
            section_group.add(circle_frame)

            # --- Visualization based on approach ---
            if sec_idx == 0:  # Classification: 9x9 grid
                grid_size = 9
                cell_dim = (earth_radius * 2) / grid_size
                grid_group = VGroup()

                x_start = x_center - earth_radius
                y_top = earth_y_center + earth_radius

                for row in range(grid_size):
                    for col in range(grid_size):
                        x_pos = x_start + col * cell_dim + cell_dim / 2
                        y_pos = y_top - row * cell_dim - cell_dim / 2

                        dist_from_center = np.sqrt(
                            (x_pos - x_center) ** 2 +
                            (y_pos - earth_y_center) ** 2
                        )

                        if dist_from_center <= earth_radius * 0.95:
                            cell = Rectangle(
                                width=cell_dim * 0.92,
                                height=cell_dim * 0.92,
                                color=circle_color,
                                stroke_width=0.3,
                                fill_opacity=0.15,
                                stroke_opacity=0.8
                            )
                            cell.move_to([x_pos, y_pos, 0])
                            grid_group.add(cell)

                section_group.add(grid_group)
                section_group.grid_anims = grid_group  # Store for later animation

            elif sec_idx == 1:  # Diffusion: 20 spiral dots (land-only filtered)
                dots_group = VGroup()
                num_dots = 20
                rng_diff = np.random.default_rng(99)

                dot_angles = rng_diff.uniform(0, 2 * np.pi, num_dots * 2)  # Generate extra for filtering
                dot_radii = rng_diff.uniform(0.5, 1.0, num_dots * 2) * earth_radius

                valid_angles = []
                valid_radii = []

                for i in range(num_dots * 2):
                    x_init = x_center + dot_radii[i] * np.cos(dot_angles[i])
                    y_init = earth_y_center + dot_radii[i] * np.sin(dot_angles[i])

                    # Filter to land areas only
                    dist_from_center = np.sqrt(
                        (x_init - x_center) ** 2 +
                        (y_init - earth_y_center) ** 2
                    )

                    if dist_from_center <= earth_radius * 0.82:  # Land-only filter
                        dot = Dot(
                            point=[x_init, y_init, 0],
                            radius=0.03,
                            color=dot_color,
                            fill_opacity=0.7
                        )
                        dots_group.add(dot)
                        valid_angles.append(dot_angles[i])
                        valid_radii.append(dot_radii[i])

                        if len(dots_group) >= num_dots:  # Stop once we have enough
                            break

                section_group.add(dots_group)
                section_group.dot_positions = list(zip(valid_angles, valid_radii))
                section_group.dots_group = dots_group
                section_group.x_center = x_center
                section_group.earth_y_center = earth_y_center
                section_group.earth_radius = earth_radius
                section_group.rng_diff = rng_diff

            elif sec_idx == 2:  # Retrieval: 40 database dots
                db_dots_group = VGroup()
                num_db = 40
                rng_ret = np.random.default_rng(7)

                for i in range(num_db):
                    angle = rng_ret.uniform(0, 2 * np.pi)
                    radius = rng_ret.uniform(0.0, earth_radius * 0.85)

                    x_pos = x_center + radius * np.cos(angle)
                    y_pos = earth_y_center + radius * np.sin(angle)

                    dist_from_center = np.sqrt(
                        (x_pos - x_center) ** 2 +
                        (y_pos - earth_y_center) ** 2
                    )

                    if dist_from_center <= earth_radius * 0.82:
                        db_dot = Dot(
                            point=[x_pos, y_pos, 0],
                            radius=0.03,
                            color=dot_color,
                            fill_opacity=0.5
                        )
                        db_dots_group.add(db_dot)

                section_group.add(db_dots_group)
                section_group.db_dots = db_dots_group
                section_group.x_center = x_center

            # --- Section label below ---
            label = create_sans_body(
                method_name,
                font_size=20,
                color=circle_color
            )
            label.move_to([x_center, -0.5, 0])
            section_group.add(label)

            section_groups.append(section_group)

        # Create golden highlight rectangle
        highlight_box = RoundedRectangle(
            width=2.9,
            height=2.1,
            corner_radius=0.3,
            color=COLORS["gold_light"],
            stroke_width=2.5,
            fill_opacity=0.0,
            stroke_opacity=0.8
        )

        # If transitioning from a previous approach, start there; otherwise start at active
        if previous_index is not None:
            highlight_box.move_to([section_specs[previous_index][1], 0.2, 0])
        else:
            highlight_box.move_to([section_specs[active_next_index][1], 0.2, 0])

        # ============================================================
        # ANIMATE IN
        # ============================================================
        self.play(
            FadeIn(divider_title, run_time=0.6,
                   rate_func=rate_functions.ease_in_out_sine)
        )
        self.wait(0.2)

        all_sections = VGroup(*section_groups)
        self.play(
            FadeIn(all_sections, highlight_box, run_time=1.0,
                   rate_func=rate_functions.ease_in_out_sine)
        )

        # If transitioning, animate highlight to new position
        if previous_index is not None:
            self.play(
                highlight_box.animate.move_to([section_specs[active_next_index][1], 0.2, 0]).set_run_time(0.7)
            )

        # --- Run all approach animations simultaneously ---
        # Classification: Grid fill
        clf_section = section_groups[0]
        if hasattr(clf_section, 'grid_anims'):
            grid_anims = [
                clf_section.grid_anims[j].animate.set_fill(opacity=0.5)
                for j in range(len(clf_section.grid_anims))
            ]
        else:
            grid_anims = []

        # Diffusion: Spiral convergence (2 steps)
        diff_section = section_groups[1]
        diff_anims = []
        if hasattr(diff_section, 'dots_group'):
            tangential_factor = 0.15
            for step_idx, spread_frac in enumerate([0.7, 0.4]):
                step_anims = []
                for i, (angle, init_radius) in enumerate(diff_section.dot_positions):
                    dot = diff_section.dots_group[i]
                    current_pos = dot.get_center()

                    cx = diff_section.x_center
                    cy = diff_section.earth_y_center
                    dx = current_pos[0] - cx
                    dy = current_pos[1] - cy
                    dist = np.sqrt(dx ** 2 + dy ** 2) + 1e-6

                    target_dist = spread_frac * diff_section.earth_radius * diff_section.rng_diff.uniform(0.5, 1.0)
                    norm_dx = dx / dist
                    norm_dy = dy / dist

                    tang_dx = -norm_dy * tangential_factor * diff_section.earth_radius
                    tang_dy = norm_dx * tangential_factor * diff_section.earth_radius

                    new_x = cx + norm_dx * target_dist + tang_dx
                    new_y = cy + norm_dy * target_dist + tang_dy

                    final_dist = np.sqrt((new_x - cx) ** 2 + (new_y - cy) ** 2)
                    if final_dist > diff_section.earth_radius * 0.92:
                        scale = (diff_section.earth_radius * 0.92) / final_dist
                        new_x = cx + (new_x - cx) * scale
                        new_y = cy + (new_y - cy) * scale

                    step_anims.append(dot.animate.move_to([new_x, new_y, 0]))

                self.play(
                    LaggedStart(*step_anims, lag_ratio=0.01, run_time=0.6)
                )

        # Retrieval: Highlight pulses
        ret_section = section_groups[2]
        if hasattr(ret_section, 'db_dots'):
            num_available = len(ret_section.db_dots)
            if num_available > 0:
                num_to_highlight = min(8, num_available)
                rng_scan = np.random.default_rng(13)
                highlight_indices = rng_scan.choice(num_available, num_to_highlight, replace=False)

                for idx in highlight_indices:
                    highlight_circle = Circle(
                        radius=0.05,
                        color=COLORS["gold_light"],
                        fill_opacity=0.3,
                        stroke_opacity=0.8,
                        stroke_width=1.5
                    )
                    highlight_circle.move_to(ret_section.db_dots[idx].get_center())

                    self.play(
                        FadeIn(highlight_circle, run_time=0.08,
                               rate_func=rate_functions.ease_in_out_sine)
                    )
                    self.play(
                        FadeOut(highlight_circle, run_time=0.06,
                                rate_func=rate_functions.ease_in_out_sine)
                    )

        self.wait(1.0)

        # ============================================================
        # ANIMATE OUT
        # ============================================================
        self.play(
            FadeOut(divider_title, all_sections, highlight_box, run_time=0.7,
                   rate_func=rate_functions.ease_in_out_sine)
        )
        self.wait(0.3)

    # ================================================================
    # MAIN CONSTRUCT
    # ================================================================
    def construct(self):
        self.camera.background_color = COLORS["bg"]

        # ============================================================
        # HEADER & PROGRESS LINE (Top of Scene - stays throughout)
        # ============================================================
        divider_line = Line(
            start=[-7.0, 3.2, 0],
            end=[7.0, 3.2, 0],
            color=COLORS["text_muted"],
            stroke_width=1.5,
            stroke_opacity=0.3
        )

        # Progress dots - Fix 11: use COLORS["accent"] for active dot
        progress_dots = VGroup()
        num_scenes = 5
        dot_x_positions = np.linspace(-6.8, 6.8, num_scenes)
        for i, x_pos in enumerate(dot_x_positions):
            dot = Dot(
                point=[x_pos, 3.2, 0],
                radius=0.07,
                color=COLORS["accent"] if i == 1 else COLORS["text_muted"],
                fill_opacity=1.0 if i == 1 else 0.4
            )
            progress_dots.add(dot)

        # Header title
        hierlock_header = Text(
            "HierLoc",
            font=FONTS["sans"],
            font_size=48,
            color=COLORS["accent"]
        )
        hierlock_header.move_to([-5.5, 3.6, 0])

        self.add(divider_line, progress_dots, hierlock_header)

        # ============================================================
        # FIX 8: NARRATIVE INTRO (3.5 seconds)
        # ============================================================
        intro_line1 = create_sans_body(
            "Visual Geolocation Existing Approaches.",
            font_size=28,
            color=COLORS["text"]
        )
        intro_line1.move_to([0, 0.5, 0])

        intro_line2 = create_sans_body(
            "Let's explore each one.",
            font_size=24,
            color=COLORS["text_muted"]
        )
        intro_line2.move_to([0, -0.1, 0])

        self.play(
            FadeIn(intro_line1, run_time=0.9,
                   rate_func=rate_functions.ease_in_out_sine)
        )
        self.wait(0.3)
        self.play(
            FadeIn(intro_line2, run_time=0.7,
                   rate_func=rate_functions.ease_in_out_sine)
        )
        self.wait(1.4)
        self.play(
            FadeOut(intro_line1, intro_line2, run_time=0.6,
                    rate_func=rate_functions.ease_in_out_sine)
        )
        self.wait(0.3)

        # ============================================================
        # SEQUENCE 0: INITIAL DIVIDER SLIDE (Teaser - Classification highlighted)
        # ============================================================
        self.show_divider_slide(active_next_index=0)

        # ============================================================
        # SEQUENCE 1: CLASSIFICATION
        # ============================================================
        # Title - Fix 12: font_size 52 -> 42
        clf_title = create_sans_body(
            "Classification",
            font_size=42,
            color=COLORS["accent"]
        )
        clf_title.move_to([0, 2.4, 0])

        # Fix 13: ease_in_out_sine on FadeIn
        self.play(
            FadeIn(clf_title, run_time=0.8,
                   rate_func=rate_functions.ease_in_out_sine)
        )
        self.wait(0.3)

        # Subtitle - Fix 9: 2-line description
        clf_sub1 = create_sans_body(
            "Divide the Earth into geographic grid cells.",
            font_size=22,
            color=COLORS["text"]
        )
        clf_sub1.move_to([0, 1.88, 0])

        clf_sub2 = create_sans_body(
            "Predict which cell contains the query image.",
            font_size=20,
            color=COLORS["text_muted"]
        )
        clf_sub2.move_to([0, 1.56, 0])

        self.play(
            FadeIn(clf_sub1, run_time=0.5,
                   rate_func=rate_functions.ease_in_out_sine)
        )
        self.play(
            FadeIn(clf_sub2, run_time=0.5,
                   rate_func=rate_functions.ease_in_out_sine)
        )
        self.wait(0.5)

        # Create Earth visualization
        earth_radius = 1.1
        earth_center = np.array([0, 0.2, 0])
        earth_path = "/Volumes/SSD/iclr-website/static/images/earth-icon.svg"

        clf_visual = VGroup()

        if os.path.exists(earth_path):
            try:
                clf_earth = SVGMobject(file_name=earth_path)
                clf_earth.set_height(earth_radius * 2)
                clf_earth.move_to(earth_center)
                clf_visual.add(clf_earth)
            except Exception:
                pass

        # Circle frame
        clf_circle = Circle(
            radius=earth_radius,
            color=COLORS["accent"],
            fill_opacity=0,
            stroke_opacity=0.8,
            stroke_width=2
        )
        clf_circle.move_to(earth_center)
        clf_visual.add(clf_circle)

        # Create grid - Fix 1: color changed from #000000 to COLORS["accent"]
        grid_rows = 11
        grid_cols = 11
        cell_width = (earth_radius * 2) / grid_cols
        cell_height = (earth_radius * 2) / grid_rows

        x_start = earth_center[0] - earth_radius
        y_top = earth_center[1] + earth_radius

        clf_grid_rects = VGroup()
        for row in range(grid_rows):
            for col in range(grid_cols):
                x_pos = x_start + col * cell_width + cell_width / 2
                y_pos = y_top - row * cell_height - cell_height / 2

                dist_from_center = np.sqrt(
                    (x_pos - earth_center[0]) ** 2 +
                    (y_pos - earth_center[1]) ** 2
                )

                if dist_from_center <= earth_radius * 0.95:
                    cell = Rectangle(
                        width=cell_width * 0.92,
                        height=cell_height * 0.92,
                        color=COLORS["accent"],   # Fix 1: was "#000000"
                        stroke_width=0.3,
                        fill_opacity=0.15,
                        stroke_opacity=0.8
                    )
                    cell.move_to([x_pos, y_pos, 0])
                    clf_grid_rects.add(cell)

        clf_visual.add(clf_grid_rects)

        self.play(
            FadeIn(clf_visual, run_time=1.0,
                   rate_func=rate_functions.ease_in_out_sine)
        )
        self.wait(0.4)

        # Fix 6: Grid animation with LaggedStart, 2s total (was ~6s loop)
        if len(clf_grid_rects) > 0:
            grid_animations = [
                clf_grid_rects[j].animate.set_fill(opacity=0.5)
                for j in range(len(clf_grid_rects))
            ]
            self.play(
                LaggedStart(*grid_animations, lag_ratio=0.04, run_time=2.0)
            )

        # Fix 10: wait reduced 1.5s -> 0.8s
        self.wait(0.8)

        # Description bottom - Fix 9: 2-line description
        clf_desc1 = create_sans_body(
            "Fast inference, scales to millions of images.",
            font_size=20,
            color=COLORS["text_muted"]
        )
        clf_desc1.move_to([0, -2.8, 0])

        clf_desc2 = create_sans_body(
            "Limited by cell granularity - imprecise near borders.",
            font_size=18,
            color=COLORS["text_muted"]
        )
        clf_desc2.move_to([0, -3.15, 0])

        self.play(
            FadeIn(clf_desc1, run_time=0.5,
                   rate_func=rate_functions.ease_in_out_sine)
        )
        self.play(
            FadeIn(clf_desc2, run_time=0.5,
                   rate_func=rate_functions.ease_in_out_sine)
        )
        # Fix 10: 1.5s -> 0.8s
        self.wait(0.8)

        # FADE OUT ALL CLASSIFICATION CONTENT - Fix 13: easing
        self.play(
            FadeOut(
                clf_title, clf_sub1, clf_sub2,
                clf_visual, clf_desc1, clf_desc2,
                run_time=0.8,
                rate_func=rate_functions.ease_in_out_sine
            )
        )
        # Fix 10: 0.5s -> 0.3s
        self.wait(0.3)

        # ============================================================
        # SEQUENCE 2: DIVIDER SLIDE - highlight Diffusion next (animated from Classification)
        # ============================================================
        self.show_divider_slide(active_next_index=1, previous_index=0)

        # ============================================================
        # SEQUENCE 3: DIFFUSION
        # ============================================================
        # Title - Fix 12: 52 -> 42
        diff_title = create_sans_body(
            "Diffusion",
            font_size=42,
            color=COLORS["accent"]
        )
        diff_title.move_to([0, 2.4, 0])

        # Fix 13: easing
        self.play(
            FadeIn(diff_title, run_time=0.8,
                   rate_func=rate_functions.ease_in_out_sine)
        )
        self.wait(0.3)

        # Fix 9: 2-line subtitle
        diff_sub1 = create_sans_body(
            "A generative model iteratively denoises a location estimate.",
            font_size=22,
            color=COLORS["text"]
        )
        diff_sub1.move_to([0, 1.88, 0])

        diff_sub2 = create_sans_body(
            "Starts from noise, refines toward a precise prediction.",
            font_size=20,
            color=COLORS["text_muted"]
        )
        diff_sub2.move_to([0, 1.56, 0])

        self.play(
            FadeIn(diff_sub1, run_time=0.5,
                   rate_func=rate_functions.ease_in_out_sine)
        )
        self.play(
            FadeIn(diff_sub2, run_time=0.5,
                   rate_func=rate_functions.ease_in_out_sine)
        )
        self.wait(0.5)

        # Create Earth with diffusion dots
        earth_radius_diff = 1.1
        earth_center_diff = np.array([0, 0.2, 0])

        diff_visual = VGroup()

        if os.path.exists(earth_path):
            try:
                diff_earth = SVGMobject(file_name=earth_path)
                diff_earth.set_height(earth_radius_diff * 2)
                diff_earth.move_to(earth_center_diff)
                diff_visual.add(diff_earth)
            except Exception:
                pass

        # Circle frame
        diff_circle = Circle(
            radius=earth_radius_diff,
            color=COLORS["accent"],
            fill_opacity=0,
            stroke_opacity=0.8,
            stroke_width=2
        )
        diff_circle.move_to(earth_center_diff)
        diff_visual.add(diff_circle)

        # Fix 7: Spiral convergence - dots start spread, spiral toward center
        # Spread radii decrease each step: 1.0 -> 0.7 -> 0.4 -> 0.15
        num_dots = 50
        diff_dots = VGroup()

        # Seed for reproducibility in spiral positions
        rng = np.random.default_rng(42)

        # Initial positions: spread uniformly across earth disk, filtered to land areas
        dot_angles = rng.uniform(0, 2 * np.pi, num_dots * 2)  # Generate extra to account for filtering
        dot_radii = rng.uniform(0.5, 1.0, num_dots * 2) * earth_radius_diff

        for i in range(num_dots * 2):
            x_init = earth_center_diff[0] + dot_radii[i] * np.cos(dot_angles[i])
            y_init = earth_center_diff[1] + dot_radii[i] * np.sin(dot_angles[i])

            # Filter to land areas only (distance threshold like Retrieval)
            dist_from_center = np.sqrt(
                (x_init - earth_center_diff[0]) ** 2 +
                (y_init - earth_center_diff[1]) ** 2
            )

            if dist_from_center <= earth_radius_diff * 0.82:  # Land-only filter
                dot = Dot(
                    point=[x_init, y_init, 0],
                    radius=0.04,
                    color=COLORS["accent"],   # Fix 2: was "#000000"
                    fill_opacity=0.7
                )
                diff_dots.add(dot)

                if len(diff_dots) >= num_dots:  # Stop once we have enough dots
                    break

        diff_visual.add(diff_dots)

        self.play(
            FadeIn(diff_visual, run_time=1.0,
                   rate_func=rate_functions.ease_in_out_sine)
        )
        self.wait(0.4)

        # Fix 7: Spiral convergence animation - 4 steps narrowing spread
        # Each step moves dots 30% closer to center plus small tangential offset
        # spread_fractions: remaining fraction of earth_radius used as max spread
        spread_fractions = [0.7, 0.4, 0.15]
        tangential_factor = 0.15  # small spiral component

        for step_idx, spread_frac in enumerate(spread_fractions):
            step_animations = []
            for i in range(len(diff_dots)):
                current_pos = diff_dots[i].get_center()
                cx = earth_center_diff[0]
                cy = earth_center_diff[1]

                # Vector from center to current dot
                dx = current_pos[0] - cx
                dy = current_pos[1] - cy
                dist = np.sqrt(dx ** 2 + dy ** 2) + 1e-6

                # Target: reduce distance to spread_frac * earth_radius_diff
                target_dist = spread_frac * earth_radius_diff * rng.uniform(0.5, 1.0)
                norm_dx = dx / dist
                norm_dy = dy / dist

                # Tangential (perpendicular) component for spiral look
                tang_dx = -norm_dy * tangential_factor * earth_radius_diff
                tang_dy = norm_dx * tangential_factor * earth_radius_diff

                new_x = cx + norm_dx * target_dist + tang_dx
                new_y = cy + norm_dy * target_dist + tang_dy

                # Clamp to stay within earth circle
                final_dist = np.sqrt((new_x - cx) ** 2 + (new_y - cy) ** 2)
                if final_dist > earth_radius_diff * 0.92:
                    scale = (earth_radius_diff * 0.92) / final_dist
                    new_x = cx + (new_x - cx) * scale
                    new_y = cy + (new_y - cy) * scale

                step_animations.append(
                    diff_dots[i].animate.move_to([new_x, new_y, 0])
                )

            self.play(
                LaggedStart(*step_animations, lag_ratio=0.01, run_time=0.7)
            )

        # Fix 10: 1.2s -> 0.8s
        self.wait(0.8)

        # Fix 9: 2-line description
        diff_desc1 = create_sans_body(
            "Flexible: can model complex geographic distributions.",
            font_size=20,
            color=COLORS["text_muted"]
        )
        diff_desc1.move_to([0, -2.8, 0])

        diff_desc2 = create_sans_body(
            "High compute cost: inference requires many denoising steps.",
            font_size=18,
            color=COLORS["text_muted"]
        )
        diff_desc2.move_to([0, -3.15, 0])

        self.play(
            FadeIn(diff_desc1, run_time=0.5,
                   rate_func=rate_functions.ease_in_out_sine)
        )
        self.play(
            FadeIn(diff_desc2, run_time=0.5,
                   rate_func=rate_functions.ease_in_out_sine)
        )
        # Fix 10: 1.5s -> 0.8s
        self.wait(0.8)

        # FADE OUT ALL DIFFUSION CONTENT - Fix 13: easing
        self.play(
            FadeOut(
                diff_title, diff_sub1, diff_sub2,
                diff_visual, diff_desc1, diff_desc2,
                run_time=0.8,
                rate_func=rate_functions.ease_in_out_sine
            )
        )
        # Fix 10: 0.5s -> 0.3s
        self.wait(0.3)

        # ============================================================
        # SEQUENCE 4: DIVIDER SLIDE - highlight Retrieval next (animated from Diffusion)
        # ============================================================
        self.show_divider_slide(active_next_index=2, previous_index=1)

        # ============================================================
        # SEQUENCE 5: RETRIEVAL
        # ============================================================
        # Title - Fix 12: 52 -> 42
        ret_title = create_sans_body(
            "Retrieval",
            font_size=42,
            color=COLORS["gold_light"]
        )
        ret_title.move_to([0, 2.4, 0])

        # Fix 13: easing
        self.play(
            FadeIn(ret_title, run_time=0.8,
                   rate_func=rate_functions.ease_in_out_sine)
        )
        self.wait(0.3)

        # Fix 9: 2-line subtitle
        ret_sub1 = create_sans_body(
            "Encode the query image, search a global embedding database.",
            font_size=22,
            color=COLORS["text"]
        )
        ret_sub1.move_to([0, 1.88, 0])

        ret_sub2 = create_sans_body(
            "Return the GPS coordinates of the nearest match.",
            font_size=20,
            color=COLORS["text_muted"]
        )
        ret_sub2.move_to([0, 1.56, 0])

        self.play(
            FadeIn(ret_sub1, run_time=0.5,
                   rate_func=rate_functions.ease_in_out_sine)
        )
        self.play(
            FadeIn(ret_sub2, run_time=0.5,
                   rate_func=rate_functions.ease_in_out_sine)
        )
        self.wait(0.5)

        # Create Earth with database dots
        earth_radius_ret = 1.1
        earth_center_ret = np.array([0, 0.2, 0])

        ret_visual = VGroup()

        if os.path.exists(earth_path):
            try:
                ret_earth = SVGMobject(file_name=earth_path)
                ret_earth.set_height(earth_radius_ret * 2)
                ret_earth.move_to(earth_center_ret)
                ret_visual.add(ret_earth)
            except Exception:
                pass

        # Circle frame
        ret_circle = Circle(
            radius=earth_radius_ret,
            color=COLORS["gold_light"],
            fill_opacity=0,
            stroke_opacity=0.8,
            stroke_width=2
        )
        ret_circle.move_to(earth_center_ret)
        ret_visual.add(ret_circle)

        # Database dots on land
        ret_db_dots = VGroup()
        num_db_dots = 100
        rng_ret = np.random.default_rng(7)

        for i in range(num_db_dots):
            angle = rng_ret.uniform(0, 2 * np.pi)
            radius = rng_ret.uniform(0.0, earth_radius_ret * 0.85)

            x_pos = earth_center_ret[0] + radius * np.cos(angle)
            y_pos = earth_center_ret[1] + radius * np.sin(angle)

            dist_from_center = np.sqrt(
                (x_pos - earth_center_ret[0]) ** 2 +
                (y_pos - earth_center_ret[1]) ** 2
            )

            if dist_from_center <= earth_radius_ret * 0.82:
                db_dot = Dot(
                    point=[x_pos, y_pos, 0],
                    radius=0.04,
                    color=COLORS["text_muted"],
                    fill_opacity=0.5
                )
                ret_db_dots.add(db_dot)

        ret_visual.add(ret_db_dots)

        self.play(
            FadeIn(ret_visual, run_time=1.0,
                   rate_func=rate_functions.ease_in_out_sine)
        )
        self.wait(0.4)

        # Scanning animation - Fix 3: FadeIn 0.1->0.15, FadeOut 0.08->0.12
        num_available = len(ret_db_dots)
        num_to_highlight = min(15, num_available)
        rng_scan = np.random.default_rng(13)
        highlight_indices = rng_scan.choice(num_available, num_to_highlight, replace=False)

        for idx in highlight_indices:
            highlight_circle = Circle(
                radius=0.08,
                color=COLORS["gold_light"],
                fill_opacity=0.3,
                stroke_opacity=0.8,
                stroke_width=1.5
            )
            highlight_circle.move_to(ret_db_dots[idx].get_center())

            # Fix 3: 0.1 -> 0.15, Fix 13: easing
            self.play(
                FadeIn(highlight_circle, run_time=0.15,
                       rate_func=rate_functions.ease_in_out_sine)
            )
            # Fix 3: 0.08 -> 0.12, Fix 13: easing
            self.play(
                FadeOut(highlight_circle, run_time=0.12,
                        rate_func=rate_functions.ease_in_out_sine)
            )

        # Fix 10: 1.0s -> 0.6s
        self.wait(0.6)

        # Fix 9: 2-line description
        ret_desc1 = create_sans_body(
            "High accuracy with efficient approximate nearest-neighbor search.",
            font_size=20,
            color=COLORS["text_muted"]
        )
        ret_desc1.move_to([0, -2.8, 0])

        ret_desc2 = create_sans_body(
            "Scales to 100M+ references with index structures like FAISS.",
            font_size=18,
            color=COLORS["text_muted"]
        )
        ret_desc2.move_to([0, -3.15, 0])

        self.play(
            FadeIn(ret_desc1, run_time=0.5,
                   rate_func=rate_functions.ease_in_out_sine)
        )
        self.play(
            FadeIn(ret_desc2, run_time=0.5,
                   rate_func=rate_functions.ease_in_out_sine)
        )
        # Fix 10: 1.5s -> 0.8s
        self.wait(0.8)

        # ============================================================
        # SEQUENCE 6: Final Transition
        # ============================================================
        self.play(
            FadeOut(
                ret_title, ret_sub1, ret_sub2,
                ret_visual, ret_desc1, ret_desc2,
                divider_line, progress_dots, hierlock_header,
                run_time=1.2,
                rate_func=rate_functions.ease_in_out_sine
            )
        )
        self.wait(0.5)
