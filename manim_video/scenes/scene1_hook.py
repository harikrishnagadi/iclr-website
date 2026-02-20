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
import sys
import numpy as np
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from config import COLORS, FONTS, setup_manim_config
from utils import create_serif_title, create_sans_body
from layout import ObjectPositioner

setup_manim_config(quality="high_quality")


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
        # SEQUENCE 1: Paper Title (0-1.5s)
        # ============================================================
        paper_title = Text(
            "HierLoc: Hyperbolic Entity Embeddings\nfor Hierarchical Visual Geolocation",
            font=FONTS["sans"],
            font_size=32,
            color=COLORS["text"],
            line_spacing=1.3
        )
        paper_title.move_to([0, 2.2, 0])

        self.play(FadeIn(paper_title, run_time=1.2))
        self.wait(1.0)

        # ============================================================
        # SEQUENCE 2: Authors with Affiliation Numbers (1.5-3s)
        # ============================================================
        # Authors with superscript affiliation numbers
        authors_line1 = Text(
            "Hari Krishna Gadi",
            font=FONTS["sans"],
            font_size=20,
            color=COLORS["text"]
        )
        authors_num1 = Text(
            "1,2",
            font=FONTS["sans"],
            font_size=12,
            color=COLORS["text"]
        )

        authors_line2 = Text(
            "Hongyi Luo",
            font=FONTS["sans"],
            font_size=20,
            color=COLORS["text"]
        )
        authors_num2 = Text(
            "1,2",
            font=FONTS["sans"],
            font_size=12,
            color=COLORS["text"]
        )

        authors_line3 = Text(
            "Daniel Matos, Lu Liu, Yongliang Wang, Yanfeng Zhang",
            font=FONTS["sans"],
            font_size=20,
            color=COLORS["text"]
        )
        authors_num3 = Text(
            "1",
            font=FONTS["sans"],
            font_size=12,
            color=COLORS["text"]
        )

        authors_line4 = Text(
            "Liqiu Meng",
            font=FONTS["sans"],
            font_size=20,
            color=COLORS["text"]
        )
        authors_num4 = Text(
            "2",
            font=FONTS["sans"],
            font_size=12,
            color=COLORS["text"]
        )

        # Combine authors with their numbers (simplified layout)
        authors_group = VGroup(
            Text(
                "Hari Krishna Gadi¹,², Daniel Matos¹, Hongyi Luo¹,²,\nLu Liu¹, Yongliang Wang¹, Yanfeng Zhang¹, Liqiu Meng²",
                font=FONTS["sans"],
                font_size=18,
                color=COLORS["text"],
                line_spacing=1.2
            )
        )
        authors_group.move_to([0, 0.8, 0])

        self.play(FadeIn(authors_group, run_time=0.8))
        self.wait(1.0)

        # ============================================================
        # SEQUENCE 3: Numbered Affiliations (3-4.5s)
        # ============================================================
        affiliation1 = Text(
            "¹ Huawei Riemann Lab",
            font=FONTS["sans"],
            font_size=16,
            color=COLORS["text_muted"]
        )
        affiliation1.move_to([0, -0.2, 0])

        affiliation2 = Text(
            "² Technical University of Munich",
            font=FONTS["sans"],
            font_size=16,
            color=COLORS["text_muted"]
        )
        affiliation2.move_to([0, -0.6, 0])

        self.play(FadeIn(affiliation1, run_time=0.5))
        self.wait(0.3)
        self.play(FadeIn(affiliation2, run_time=0.5))
        self.wait(0.8)

        # ============================================================
        # SEQUENCE 4: Transition to Challenge & Animate Header (4.5-6s)
        # ============================================================
        # Create "HierLoc" text at center (for animation)
        hierlock_title = Text(
            "HierLoc",
            font=FONTS["sans"],
            font_size=64,
            color=COLORS["accent"]
        )
        hierlock_title.move_to([0, 1.0, 0])

        # Fade out paper info
        self.play(
            FadeOut(paper_title, authors_group, affiliation1, affiliation2, run_time=0.8),
            FadeIn(hierlock_title, run_time=0.8)
        )
        self.wait(0.3)

        # Animate HierLoc to top-left corner (header position)
        # Full-width divider line below header
        divider_line = Line(
            start=[-7.0, 3.2, 0],
            end=[7.0, 3.2, 0],
            color=COLORS["text_muted"],
            stroke_width=1.5,
            stroke_opacity=0.3
        )

        # Progress dots spread evenly across entire line
        progress_dots = VGroup()
        num_scenes = 5
        dot_x_positions = np.linspace(-6.8, 6.8, num_scenes)
        for i, x_pos in enumerate(dot_x_positions):
            dot = Dot(
                point=[x_pos, 3.2, 0],
                radius=0.07,
                color=COLORS["accent"] if i == 0 else COLORS["text_muted"],
                fill_opacity=1.0 if i == 0 else 0.4
            )
            progress_dots.add(dot)

        # Animate header to top-left (centered in gap between line and top)
        self.play(
            hierlock_title.animate.scale(0.75).move_to([-5.5, 3.6, 0]),
            FadeIn(progress_dots, divider_line, run_time=0.6)
        )
        self.wait(0.5)

        # ============================================================
        # SEQUENCE 5: Display Street View Images in Grid (6-24s)
        # ============================================================
        # Load all available street view images
        streetview_dir = "/Volumes/SSD/iclr-website/static/images/streetview"
        image_paths = [
            os.path.join(streetview_dir, "Paris_00131_445353063_8c58bd82b1_179_88895879@N00.jpg"),
            os.path.join(streetview_dir, "Russia_00019_985802242_5ad0b7dbeb_1190_23707253@N00.jpg"),
            os.path.join(streetview_dir, "482314949_dbc149bb10_224_50435419@N00.jpg"),
            os.path.join(streetview_dir, "0b_5a_5283974984.jpg"),
        ]

        # Verify images exist
        available_images = [p for p in image_paths if os.path.exists(p)]

        if available_images:
            # Create frames and load images
            frames_group = VGroup()
            image_objects = []

            # Grid positions (2x2 layout)
            positions = [
                [-3.5, 1.5, 0],   # Top-left
                [3.5, 1.5, 0],    # Top-right
                [-3.5, -1.5, 0],  # Bottom-left
                [3.5, -1.5, 0],   # Bottom-right
            ]

            for idx, img_path in enumerate(available_images):
                if idx < len(positions):
                    # Load image
                    img = ImageMobject(img_path)
                    img.set_height(1.8)
                    img.move_to(positions[idx])

                    # Create rounded rectangle frame around image
                    frame = RoundedRectangle(
                        width=img.width + 0.2,
                        height=img.height + 0.2,
                        corner_radius=0.15,
                        color=COLORS["accent"],
                        stroke_width=2,
                        fill_opacity=0,
                        stroke_opacity=0.8
                    )
                    frame.move_to(positions[idx])

                    # Add frame to group (ImageMobject needs to be added separately)
                    frames_group.add(frame)
                    image_objects.append(img)
                    self.add(img)

            # Fade in all frames and images together at once
            self.play(FadeIn(frames_group, run_time=1.2))
            self.wait(2.5)

            # ============================================================
            # SEQUENCE 6: Define Visual Geolocation with Smart Layout (6-16s)
            # ============================================================
            # Get bounds of existing image objects for reference
            image_bounds_list = [ObjectPositioner.get_bounds(img) for img in image_objects]

            # Find the bottom Y position of the bottom two images
            bottom_y_values = [bounds['y_min'] for bounds in image_bounds_list if bounds]
            bottom_image_y = min(bottom_y_values) if bottom_y_values else -1.5

            # Create text elements
            geo_title = Text(
                "Visual Geolocation",
                font=FONTS["sans"],
                font_size=32,
                color=COLORS["accent"]
            )

            # Description text (single line)
            geo_description = Text(
                "Determining the geographic location of an image based on visual features alone",
                font=FONTS["sans"],
                font_size=18,
                color=COLORS["text"],
                line_spacing=1.2
            )

            # Task text (challenge)
            task_text = Text(
                "The Challenge: Guess where each image was taken",
                font=FONTS["sans"],
                font_size=18,
                color=COLORS["accent"]
            )

            # Position text elements manually to ensure no overlaps:
            # - Visual Geolocation title in the middle (center of screen, Y: 0)
            # - Definition below the bottom images (Y: bottom_image_y - 0.6)
            # - Challenge below definition with proper spacing

            # Position title in the middle
            geo_title.move_to([0, 0, 0])

            # Position definition below bottom images
            geo_description.move_to([0, bottom_image_y - 0.6, 0])

            # Position challenge below definition with safe spacing
            # bottom_image_y is around -1.5, so definition is at -2.1
            # Challenge needs to be further down: -2.8 or lower
            task_text.move_to([0, bottom_image_y - 1.4, 0])

            # Verify no overlaps using ObjectPositioner bounds checking
            title_bounds = ObjectPositioner.get_bounds(geo_title)
            desc_bounds = ObjectPositioner.get_bounds(geo_description)
            task_bounds = ObjectPositioner.get_bounds(task_text)

            # Fade in all text
            self.play(FadeIn(geo_title, run_time=0.6))
            self.wait(0.3)
            self.play(FadeIn(geo_description, run_time=0.7))
            self.wait(0.3)
            self.play(FadeIn(task_text, run_time=0.6))
            self.wait(2.0)

            # ============================================================
            # SEQUENCE 7: Isolate Image & Show Location on Earth (16-30s)
            # ============================================================
            # Fade out the other images, keep one (Paris at top-left)
            images_to_fade = [image_objects[1], image_objects[2], image_objects[3]]
            other_frames = [frames_group[1], frames_group[2], frames_group[3]]

            self.play(FadeOut(*images_to_fade, *other_frames, run_time=0.7))
            self.wait(0.3)

            # Keep Paris image (index 0) and move it to center of screen (without scaling)
            paris_image = image_objects[0]
            paris_frame = frames_group[0]
            self.play(
                paris_image.animate.move_to([0, 0, 0]),
                paris_frame.animate.move_to([0, 0, 0]),
                FadeOut(geo_title, geo_description, task_text, run_time=0.5)
            )
            self.wait(0.3)

            # ============================================================
            # CREATE EARTH GLOBE USING SVG
            # ============================================================
            # Load Earth SVG from static/images - positioned far right and lower
            earth_position_x = 5.0  # Far right for visual clarity
            earth_position_y = -0.5  # Lower position

            earth_svg = SVGMobject(
                file_name="/Volumes/SSD/iclr-website/static/images/earth-icon.svg"
            )
            earth_svg.set_height(2.4)  # Diameter of approximately 1.2 radius
            earth_svg.move_to([earth_position_x, earth_position_y, 0])

            # Add subtle shadow/depth effect with darker circle behind
            earth_shadow = Circle(
                radius=1.2,
                color="#0a0a0f",
                fill_color="#0a0a0f",
                fill_opacity=0.2,
                stroke_width=0,
                stroke_opacity=0
            )
            earth_shadow.move_to([earth_position_x + 0.1, earth_position_y - 0.1, 0])

            # Create location marker for Paris with actual coordinates
            lat = 48.8566 * np.pi / 180  # Paris latitude: 48.8566° N
            lon = 2.3522 * np.pi / 180   # Paris longitude: 2.3522° E

            # Position on sphere surface
            marker_x = earth_svg.get_center()[0] + 1.2 * np.cos(lat) * np.cos(lon)
            marker_y = earth_svg.get_center()[1] + 1.2 * np.sin(lat)

            # Location pin with better design
            marker_dot = Dot(
                point=[marker_x, marker_y, 0],
                radius=0.07,
                color=COLORS["accent"],
                fill_opacity=1.0
            )

            # Glow effect (outer ring)
            marker_glow = Circle(
                radius=0.16,
                color=COLORS["accent"],
                stroke_opacity=0.5,
                fill_opacity=0,
                stroke_width=2
            )
            marker_glow.move_to([marker_x, marker_y, 0])

            # Pulse ring effect (subtle animation element)
            marker_pulse = Circle(
                radius=0.25,
                color=COLORS["accent"],
                stroke_opacity=0.2,
                fill_opacity=0,
                stroke_width=1.5
            )
            marker_pulse.move_to([marker_x, marker_y, 0])

            # Improved arrow with curve pointing to the location pin
            # Start from the right edge of the image frame
            paris_frame_bounds = ObjectPositioner.get_bounds(paris_frame)
            arrow_start_x = paris_frame_bounds['x_max'] + 0.2  # Slightly right of frame edge
            arrow_start_y = paris_frame_bounds['center'][1]  # Center height of frame

            arrow_path = CurvedArrow(
                start_point=[arrow_start_x, arrow_start_y, 0],
                end_point=[marker_x, marker_y, 0],
                color=COLORS["accent"],
                stroke_width=2.5,
                tip_length=0.2,
                stroke_opacity=0.8,
                angle=PI/6
            )

            # Enhanced location label with background - positioned below Earth
            location_label = Text(
                "Paris, France",
                font=FONTS["sans"],
                font_size=14,
                color=COLORS["accent"]
            )
            location_label.move_to([earth_position_x, earth_position_y - 1.6, 0])

            # Label background for better readability
            label_bg = SurroundingRectangle(
                location_label,
                buff=0.15,
                color=COLORS["accent"],
                fill_color=COLORS["bg"],
                fill_opacity=0.8,
                stroke_width=1,
                stroke_opacity=0.5,
                corner_radius=0.1
            )
            label_group = VGroup(label_bg, location_label)

            # Assemble Earth group (SVG + shadow)
            earth_group = VGroup(earth_shadow, earth_svg)
            marker_group = VGroup(marker_pulse, marker_glow, marker_dot)

            # Display everything
            self.add(earth_group)
            self.play(
                FadeIn(earth_group, marker_group, arrow_path, run_time=0.8)
            )
            self.wait(0.5)
            self.play(FadeIn(label_group, run_time=0.5))
            self.wait(0.5)

            # Pulse animation on marker
            self.play(
                marker_pulse.animate.scale(1.5).set_opacity(0),
                run_time=1.0,
                rate_func=rate_functions.ease_out_quad
            )

            # Wait for visual impact
            self.wait(2.5)

            # ============================================================
            # SEQUENCE 8: Real-World Use Cases (30-40 seconds)
            # ============================================================
            # Fade out Earth visualization
            self.play(
                FadeOut(paris_image, paris_frame, earth_group, marker_group,
                        arrow_path, label_group, run_time=0.8)
            )
            self.remove(paris_image)
            self.wait(0.3)

            # Use Cases Gallery Section
            usecases_title = Text(
                "Real-World Impact",
                font=FONTS["sans"],
                font_size=40,
                color=COLORS["accent"]
            )
            usecases_title.move_to([0, 2.5, 0])

            # Define 5 key use cases
            use_cases = [
                {
                    "name": "Emergency Response",
                    "description": "Rapid location identification\nfor disaster relief",
                    "icon": "🚑"
                },
                {
                    "name": "News & Journalism",
                    "description": "Verify breaking news\nlocation automatically",
                    "icon": "📰"
                },
                {
                    "name": "Wildlife Conservation",
                    "description": "Monitor endangered species\nat scale",
                    "icon": "🦁"
                },
                {
                    "name": "Urban Planning",
                    "description": "Map cities comprehensively\nfor better infrastructure",
                    "icon": "🏙️"
                },
                {
                    "name": "Climate Action",
                    "description": "Track environmental changes\nglobally in real-time",
                    "icon": "🌍"
                }
            ]

            # Create use case boxes
            usecase_boxes = VGroup()
            x_positions = [-5.0, -2.5, 0, 2.5, 5.0]

            for i, (pos_x, usecase) in enumerate(zip(x_positions, use_cases)):
                # Create box for each use case
                box = RoundedRectangle(
                    width=2.0,
                    height=1.8,
                    corner_radius=0.15,
                    color=COLORS["accent"],
                    stroke_width=2,
                    fill_opacity=0.08,
                    fill_color=COLORS["accent"]
                )
                box.move_to([pos_x, 0.5, 0])

                # Use case name
                name = Text(
                    usecase["name"],
                    font=FONTS["sans"],
                    font_size=14,
                    color=COLORS["accent"]
                )
                name.move_to([pos_x, 1.2, 0])

                # Use case description
                desc = Text(
                    usecase["description"],
                    font=FONTS["sans"],
                    font_size=11,
                    color=COLORS["text"],
                    line_spacing=1.1
                )
                desc.move_to([pos_x, 0.3, 0])

                usecase_item = VGroup(box, name, desc)
                usecase_boxes.add(usecase_item)

            # Display title and use cases
            self.play(FadeIn(usecases_title, run_time=0.6))
            self.wait(0.3)
            self.play(FadeIn(usecase_boxes, run_time=1.0))
            self.wait(2.0)

            # Closing statement
            closing = Text(
                "HierLoc makes visual understanding practical\nat planetary scale",
                font=FONTS["sans"],
                font_size=22,
                color=COLORS["gold_light"],
                line_spacing=1.3
            )
            closing.move_to([0, -2.8, 0])

            self.play(FadeIn(closing, run_time=0.8))
            self.wait(2.0)

            # ============================================================
            # SEQUENCE 9: Transition to Next Scene
            # ============================================================
            # Final fade out
            self.play(
                FadeOut(usecases_title, usecase_boxes, closing,
                        background_elements, run_time=1.0)
            )
            self.wait(0.5)
        else:
            # Fallback if no images available
            no_images_text = Text(
                "Street view images not found",
                font=FONTS["sans"],
                font_size=24,
                color=COLORS["text"]
            )
            self.play(FadeIn(no_images_text, run_time=1.0))
            self.wait(2.0)
            self.play(FadeOut(no_images_text, background_elements, run_time=1.0))
            self.wait(0.5)
