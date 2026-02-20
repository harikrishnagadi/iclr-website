"""
Scene 3: THE INSIGHT - Geographic Hierarchy & Hyperbolic Geometry
Duration: ~35 seconds
Purpose: Show hierarchy on map + introduce Lorentz disc hyperbolic model

Key insights from paper:
- Geographic entities form a hierarchy (countries > regions > cities) - SHOWN ON MAP
- Euclidean space compresses deep hierarchies
- Hyperbolic space (Lorentz disc) has exponential volume = perfect for hierarchy
"""

from manim import *
from manim import rate_functions
import numpy as np
import sys
import os
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from config import COLORS, FONTS, setup_manim_config
from utils import create_serif_title, create_sans_body
from layout import ObjectPositioner, ReadabilityChecker

setup_manim_config(quality="high_quality")

# 48.863133, 2.336654 location of paris image in /static/images/streetview/
class Scene3Insight(Scene):
    """Key insight: Hierarchy on maps and hyperbolic geometry"""

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
                color=COLORS["accent"] if i == 2 else COLORS["text_muted"],
                fill_opacity=1.0 if i == 2 else 0.4
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
        # SEQUENCE 1: Hierarchy on Map
        # ============================================================
        hierarchy_title = create_sans_body(
            "Geographic Hierarchy",
            font_size=44,
            color=COLORS["accent"]
        )
        hierarchy_title.move_to([0, 2.2, 0])

        self.play(
            FadeIn(hierarchy_title, run_time=0.8,
                   rate_func=rate_functions.ease_in_out_sine)
        )
        self.wait(0.3)

        # ============================================================
        # Animated Map Zoom Sequence (Paris → France → Europe)
        # ============================================================
        # Load pre-generated animation frames (64 frames total)
        map_frame_dir = "/Volumes/SSD/iclr-website/static/images/map_zoom_frames"

        if os.path.exists(map_frame_dir):
            # Load all animation frames
            frame_files = sorted([f for f in os.listdir(map_frame_dir) if f.endswith('.png')])

            if frame_files:
                print(f"  ✓ Found {len(frame_files)} map animation frames")

                # Load first frame and display
                first_frame_path = os.path.join(map_frame_dir, frame_files[0])
                map_animation = ImageMobject(first_frame_path)
                map_animation.set_height(3.2)
                map_animation.move_to([0, 0.2, 0])

                # FadeIn the map animation
                self.play(FadeIn(map_animation, run_time=0.6, rate_func=rate_functions.ease_in_out_sine))

                # Play through all frames with smooth transitions
                # Each frame shown for ~0.017s (1/60 second) to create animation effect
                for frame_idx in range(1, len(frame_files)):
                    frame_path = os.path.join(map_frame_dir, frame_files[frame_idx])
                    try:
                        next_frame = ImageMobject(frame_path)
                        next_frame.set_height(3.2)
                        next_frame.move_to([0, 0.2, 0])

                        # Quick transition to next frame
                        self.play(FadeOut(map_animation, run_time=0.01),
                                 FadeIn(next_frame, run_time=0.01))
                        map_animation = next_frame
                    except Exception as e:
                        print(f"  ⚠ Error loading frame {frame_idx}: {e}")
                        continue

                # Hold final frame (Europe view)
                self.wait(0.5)

                # Reference for final fadeout
                hierarchy_map = map_animation
            else:
                print("  ⚠ No map animation frames found, using fallback")
                hierarchy_map = VGroup()
        else:
            print(f"  ⚠ Map frame directory not found: {map_frame_dir}")
            hierarchy_map = VGroup()

        # ============================================================
        # SEQUENCE 2: The Challenge - Euclidean Space Problem
        # ============================================================
        problem_title = create_sans_body(
            "The Challenge",
            font_size=32,
            color=COLORS["accent"]
        )
        problem_title.move_to([0, 2.2, 0])

        problem_desc = create_sans_body(
            "Euclidean space compresses hierarchical levels together.\n"
            "Deep levels lose their hierarchical separation.",
            font_size=18,
            color=COLORS["text"]
        )
        problem_desc.move_to([0, 0.5, 0])

        self.play(
            FadeOut(hierarchy_map, hierarchy_title,
                   run_time=0.6,
                   rate_func=rate_functions.ease_in_out_sine)
        )
        self.wait(0.2)

        self.play(
            FadeIn(problem_title, problem_desc, run_time=0.6,
                   rate_func=rate_functions.ease_in_out_sine)
        )
        self.wait(1.5)

        # ============================================================
        # SEQUENCE 3: The Solution - Lorentz Disc Model
        # ============================================================
        solution_title = create_sans_body(
            "The Solution: Hyperbolic Space",
            font_size=38,
            color=COLORS["accent"]
        )
        solution_title.move_to([0, 2.2, 0])

        self.play(
            FadeOut(hierarchy_title, problem_title, problem_desc,
                   run_time=0.6,
                   rate_func=rate_functions.ease_in_out_sine)
        )
        self.wait(0.2)

        self.play(
            FadeIn(solution_title, run_time=0.6,
                   rate_func=rate_functions.ease_in_out_sine)
        )
        self.wait(0.3)

        # Lorentz Disc Model (Upper Hyperboloid Sheet)
        lorentz_disc = self._create_lorentz_disc()
        lorentz_disc.move_to([0, 0.6, 0])

        # Hierarchical points in Lorentz model
        lorentz_points = self._create_hierarchical_lorentz_points()
        lorentz_points.move_to([0, 0.6, 0])

        # Add labels for hierarchy levels
        continent_label = create_sans_body("Continents", font_size=13, color=COLORS["accent"])
        continent_label.move_to([-1.6, 0.6, 0])

        country_label = create_sans_body("Countries", font_size=13, color=COLORS["accent"])
        country_label.move_to([1.8, 0.6, 0])

        city_label = create_sans_body("Cities\n(deep hierarchy)", font_size=12, color=COLORS["text"])
        city_label.move_to([0, -0.5, 0])

        lorentz_visual = VGroup(lorentz_disc, lorentz_points, continent_label, country_label, city_label)

        solution_desc = create_sans_body(
            "Lorentz (Hyperbolic) model:\n"
            "Exponential space enables perfect hierarchy preservation.",
            font_size=18,
            color=COLORS["text"]
        )
        solution_desc.move_to([0, -2.0, 0])

        self.play(
            FadeIn(lorentz_visual, solution_desc, run_time=0.8,
                   rate_func=rate_functions.ease_in_out_sine)
        )
        self.wait(2.0)

        # ============================================================
        # SEQUENCE 4: Final Transition
        # ============================================================
        self.play(
            FadeOut(solution_title, lorentz_visual, solution_desc,
                   divider_line, progress_dots, hierlock_header,
                   run_time=1.0,
                   rate_func=rate_functions.ease_in_out_sine)
        )
        self.wait(0.5)

    def _create_lorentz_disc(self):
        """
        Create Lorentz disc model visualization.
        The Lorentz model uses the upper hyperboloid sheet.
        Display as a circular disc with radial geodesics.
        """
        # Outer circle boundary of Lorentz disc
        boundary_circle = Circle(
            radius=1.5,
            color=COLORS["accent"],
            stroke_width=2.5,
            fill_opacity=0.08,
            fill_color=COLORS["accent"]
        )

        # Radial lines representing geodesics in hyperbolic space
        geodesics = VGroup()
        num_geodesics = 8
        for i in range(num_geodesics):
            angle = 2 * np.pi * i / num_geodesics
            end_point = np.array([
                1.4 * np.cos(angle),
                1.4 * np.sin(angle),
                0
            ])
            geodesic = Line(
                start=np.array([0, 0, 0]),
                end=end_point,
                color=COLORS["text_muted"],
                stroke_width=1.0,
                stroke_opacity=0.3
            )
            geodesics.add(geodesic)

        # Concentric circles representing different distances in hyperbolic space
        circles = VGroup()
        for radius_frac in [0.35, 0.65, 0.95]:
            circle = Circle(
                radius=radius_frac * 1.5,
                color=COLORS["text_muted"],
                stroke_width=0.8,
                stroke_opacity=0.2,
                fill_opacity=0
            )
            circles.add(circle)

        return VGroup(boundary_circle, geodesics, circles)

    def _create_hierarchical_lorentz_points(self):
        """
        Create hierarchical points in Lorentz disc (hyperbolic geometry).
        In hyperbolic space, the boundary represents infinite distance.
        Root (center): continents
        Middle ring: countries
        Boundary (outer): cities (leaves of hierarchy tree)
        """
        points = VGroup()

        # Root level (center) - Continent
        continent_positions = [
            np.array([0.25, 0, 0]),
            np.array([-0.25, 0, 0]),
        ]
        for pos in continent_positions:
            dot = Dot(
                point=pos,
                radius=0.07,
                color=COLORS["accent"],
                fill_opacity=0.7
            )
            points.add(dot)

        # Country level (middle ring)
        country_positions = [
            np.array([0.75, 0.75, 0]),
            np.array([0.75, -0.75, 0]),
            np.array([-0.75, 0.75, 0]),
            np.array([-0.75, -0.75, 0]),
        ]
        for pos in country_positions:
            dot = Dot(
                point=pos,
                radius=0.06,
                color=COLORS["accent"],
                fill_opacity=0.8
            )
            points.add(dot)

        # City level (boundary - deep hierarchy, leaves of tree)
        city_positions = [
            np.array([1.2, 0.2, 0]),
            np.array([1.2, -0.2, 0]),
            np.array([-1.2, 0.2, 0]),
            np.array([-1.2, -0.2, 0]),
            np.array([0.2, 1.2, 0]),
            np.array([-0.2, 1.2, 0]),
            np.array([0.2, -1.2, 0]),
            np.array([-0.2, -1.2, 0]),
        ]
        for pos in city_positions:
            dot = Dot(
                point=pos,
                radius=0.08,
                color=COLORS["text"],
                fill_opacity=0.95
            )
            points.add(dot)

        return points
