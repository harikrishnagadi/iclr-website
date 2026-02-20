"""
Modern CSS-like Layout System for Manim
Includes: Grid, Flexbox, Readability Checker, Overflow Prevention, Responsive Design
"""

from manim import *
import numpy as np
from config import COLORS, FONTS


class ReadabilityChecker:
    """Validate readability of text and components"""

    # WCAG Contrast Ratios
    MINIMUM_CONTRAST = 4.5  # AA standard
    ENHANCED_CONTRAST = 7   # AAA standard

    # Minimum font sizes (pt)
    MIN_BODY_TEXT = 14
    MIN_SMALL_TEXT = 12
    MIN_LABEL_TEXT = 12

    # Readability standards
    MAX_LINE_LENGTH = 50  # characters
    OPTIMAL_LINE_LENGTH = 45  # characters
    MIN_LINE_HEIGHT_RATIO = 1.2

    @staticmethod
    def check_contrast(color1, color2):
        """
        Calculate contrast ratio between two colors (0-21)
        Returns tuple: (ratio, meets_AA, meets_AAA)
        """
        # Convert hex to RGB
        def hex_to_rgb(hex_color):
            if isinstance(hex_color, str):
                hex_color = hex_color.lstrip('#')
                return tuple(int(hex_color[i:i+2], 16)/255 for i in (0, 2, 4))
            return hex_color

        c1 = hex_to_rgb(color1)
        c2 = hex_to_rgb(color2)

        # Calculate luminance
        def luminance(rgb):
            r, g, b = rgb
            r = r / 12.92 if r <= 0.03928 else ((r + 0.055) / 1.055) ** 2.4
            g = g / 12.92 if g <= 0.03928 else ((g + 0.055) / 1.055) ** 2.4
            b = b / 12.92 if b <= 0.03928 else ((b + 0.055) / 1.055) ** 2.4
            return 0.2126 * r + 0.7152 * g + 0.0722 * b

        l1 = luminance(c1)
        l2 = luminance(c2)

        lighter = max(l1, l2)
        darker = min(l1, l2)

        ratio = (lighter + 0.05) / (darker + 0.05)
        meets_aa = ratio >= ReadabilityChecker.MINIMUM_CONTRAST
        meets_aaa = ratio >= ReadabilityChecker.ENHANCED_CONTRAST

        return ratio, meets_aa, meets_aaa

    @staticmethod
    def validate_text(text_mobject, font_size=None, background_color=None,
                     text_color=None, max_width=None):
        """
        Validate text for readability
        Returns: dict with validation results
        """
        results = {
            'valid': True,
            'warnings': [],
            'errors': [],
            'font_size_ok': True,
            'contrast_ok': True,
            'overflow_ok': True
        }

        # Check font size
        if font_size and font_size < ReadabilityChecker.MIN_BODY_TEXT:
            results['font_size_ok'] = False
            results['errors'].append(
                f"Font size {font_size}pt is below minimum {ReadabilityChecker.MIN_BODY_TEXT}pt"
            )
            results['valid'] = False

        # Check contrast
        if background_color and text_color:
            ratio, meets_aa, meets_aaa = ReadabilityChecker.check_contrast(
                background_color, text_color
            )
            if not meets_aa:
                results['contrast_ok'] = False
                results['errors'].append(
                    f"Contrast ratio {ratio:.2f}:1 below WCAG AA minimum {ReadabilityChecker.MINIMUM_CONTRAST}:1"
                )
                results['valid'] = False
            elif not meets_aaa:
                results['warnings'].append(
                    f"Contrast ratio {ratio:.2f}:1 meets AA but not AAA standard"
                )

        # Check overflow
        if max_width and text_mobject.width > max_width:
            results['overflow_ok'] = False
            results['errors'].append(
                f"Text width {text_mobject.width:.2f} exceeds max {max_width}"
            )
            results['valid'] = False

        return results

    @staticmethod
    def validate_layout(mobject, bounds=None):
        """
        Validate that mobject stays within bounds
        bounds: [x_min, x_max, y_min, y_max]
        """
        if bounds is None:
            bounds = [-7, 7, -4, 4]

        x_min, x_max, y_min, y_max = bounds
        center = mobject.get_center()
        width = mobject.width
        height = mobject.height

        left = center[0] - width / 2
        right = center[0] + width / 2
        top = center[1] + height / 2
        bottom = center[1] - height / 2

        violations = []
        if left < x_min:
            violations.append(f"Left edge {left:.2f} exceeds bounds {x_min}")
        if right > x_max:
            violations.append(f"Right edge {right:.2f} exceeds bounds {x_max}")
        if top > y_max:
            violations.append(f"Top edge {top:.2f} exceeds bounds {y_max}")
        if bottom < y_min:
            violations.append(f"Bottom edge {bottom:.2f} exceeds bounds {y_min}")

        return {
            'valid': len(violations) == 0,
            'violations': violations,
            'bounds': {'left': left, 'right': right, 'top': top, 'bottom': bottom}
        }


class Box:
    """CSS Box Model implementation"""

    def __init__(self, width=2, height=1, padding=0.1, margin=0,
                 border_color=None, border_width=1, bg_color=None):
        """
        Create a box with CSS properties
        Args:
            width: content width
            height: content height
            padding: space inside border
            margin: space outside border
            border_color: color of border
            border_width: thickness of border
            bg_color: background color
        """
        self.width = width
        self.height = height
        self.padding = padding
        self.margin = margin
        self.border_color = border_color
        self.border_width = border_width
        self.bg_color = bg_color

    def get_box_dimensions(self):
        """Get total dimensions including padding and margin"""
        total_width = self.width + (2 * self.padding) + (2 * self.margin)
        total_height = self.height + (2 * self.padding) + (2 * self.margin)
        return total_width, total_height

    def create_rectangle(self):
        """Create rectangle with border and background"""
        rect_width = self.width + (2 * self.padding)
        rect_height = self.height + (2 * self.padding)

        rect = Rectangle(
            width=rect_width,
            height=rect_height,
            stroke_color=self.border_color or COLORS["accent"],
            stroke_width=self.border_width,
            fill_color=self.bg_color or COLORS["bg"],
            fill_opacity=0.1 if self.bg_color else 0
        )
        return rect


class GridContainer:
    """CSS Grid-like container"""

    def __init__(self, rows=1, cols=1, width=14, height=8, start_pos=[0, 4, 0],
                 row_gap=0.5, col_gap=0.5, padding=0.3, overflow='hidden'):
        """
        Args:
            rows, cols: grid dimensions
            width, height: total size
            start_pos: top-left position
            row_gap, col_gap: gaps between cells
            padding: internal padding
            overflow: 'hidden' (clip), 'visible' (allow), 'scroll' (hint)
        """
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.start_pos = np.array(start_pos)
        self.row_gap = row_gap
        self.col_gap = col_gap
        self.padding = padding
        self.overflow = overflow

        # Calculate cell dimensions
        available_width = width - (2 * padding) - (col_gap * (cols - 1))
        available_height = height - (2 * padding) - (row_gap * (rows - 1))

        self.cell_width = available_width / cols
        self.cell_height = available_height / rows

    def get_position(self, row, col):
        """Get position for grid cell"""
        x = self.start_pos[0] - (self.width / 2) + self.padding + \
            (self.cell_width / 2) + col * (self.cell_width + self.col_gap)
        y = self.start_pos[1] - self.padding - (self.cell_height / 2) - \
            row * (self.cell_height + self.row_gap)
        return [x, y, 0]

    def get_bounds(self):
        """Get container bounds for overflow checking"""
        x_min = self.start_pos[0] - (self.width / 2)
        x_max = self.start_pos[0] + (self.width / 2)
        y_min = self.start_pos[1] - (self.height / 2)
        y_max = self.start_pos[1] + (self.height / 2)
        return [x_min, x_max, y_min, y_max]

    def place(self, mobject, row, col, validate=True):
        """Place mobject in grid cell with overflow check"""
        if row >= self.rows or col >= self.cols:
            raise ValueError(f"Position ({row},{col}) exceeds grid ({self.rows},{self.cols})")

        pos = self.get_position(row, col)
        mobject.move_to(pos)

        if validate and self.overflow == 'hidden':
            bounds = self.get_bounds()
            check = ReadabilityChecker.validate_layout(mobject, bounds)
            if not check['valid']:
                print(f"⚠️  Overflow warning: {check['violations']}")

        return mobject

    def arrange(self, mobjects, validate=True):
        """Arrange mobjects in grid with bounds checking"""
        group = VGroup()
        for idx, mob in enumerate(mobjects):
            row = idx // self.cols
            col = idx % self.cols
            if row < self.rows:
                self.place(mob, row, col, validate=validate)
                group.add(mob)
        return group


class FlexContainer:
    """CSS Flexbox-like container"""

    def __init__(self, direction='row', justify='start', align='start',
                 gap=0.5, wrap=False, padding=0.3, width=14, height=8):
        """
        Args:
            direction: 'row' or 'column'
            justify: 'start', 'center', 'end', 'space-between', 'space-around', 'space-evenly'
            align: 'start', 'center', 'end', 'stretch'
            gap: space between items
            wrap: wrap to next line/column
            padding: internal padding
            width, height: container dimensions
        """
        self.direction = direction
        self.justify = justify
        self.align = align
        self.gap = gap
        self.wrap = wrap
        self.padding = padding
        self.width = width
        self.height = height

    def arrange(self, mobjects, start_pos=[0, 0, 0], validate=True):
        """Arrange mobjects with flexbox logic"""
        if self.direction == 'row':
            return self._arrange_row(mobjects, start_pos, validate)
        else:
            return self._arrange_column(mobjects, start_pos, validate)

    def _arrange_row(self, mobjects, start_pos, validate):
        """Arrange items horizontally"""
        group = VGroup()
        current_x = start_pos[0]

        total_width = sum(mob.width for mob in mobjects) + \
                     (self.gap * (len(mobjects) - 1))

        if self.justify == 'center':
            current_x = start_pos[0] - total_width / 2
        elif self.justify == 'end':
            current_x = start_pos[0] - total_width
        elif self.justify == 'space-between':
            if len(mobjects) > 1:
                spacing = (self.width - total_width) / (len(mobjects) - 1)
            else:
                spacing = 0
            current_x = start_pos[0] - self.width / 2

        for i, mob in enumerate(mobjects):
            if self.justify == 'space-between' and len(mobjects) > 1:
                mob.move_to([current_x + mob.width / 2, start_pos[1], 0])
                current_x += spacing
            else:
                mob.move_to([current_x + mob.width / 2, start_pos[1], 0])
                current_x += mob.width + self.gap

            if validate:
                check = ReadabilityChecker.validate_layout(mob)
                if not check['valid']:
                    print(f"⚠️  Layout warning: {check['violations']}")

            group.add(mob)

        return group

    def _arrange_column(self, mobjects, start_pos, validate):
        """Arrange items vertically"""
        group = VGroup()
        current_y = start_pos[1]

        total_height = sum(mob.height for mob in mobjects) + \
                      (self.gap * (len(mobjects) - 1))

        if self.justify == 'center':
            current_y = start_pos[1] + total_height / 2
        elif self.justify == 'end':
            current_y = start_pos[1] - total_height
        elif self.justify == 'space-between':
            if len(mobjects) > 1:
                spacing = (self.height - total_height) / (len(mobjects) - 1)
            else:
                spacing = 0
            current_y = start_pos[1] + self.height / 2

        for i, mob in enumerate(mobjects):
            if self.justify == 'space-between' and len(mobjects) > 1:
                mob.move_to([start_pos[0], current_y - mob.height / 2, 0])
                current_y -= spacing
            else:
                mob.move_to([start_pos[0], current_y - mob.height / 2, 0])
                current_y -= mob.height + self.gap

            if validate:
                check = ReadabilityChecker.validate_layout(mob)
                if not check['valid']:
                    print(f"⚠️  Layout warning: {check['violations']}")

            group.add(mob)

        return group


class Layout:
    """Modern CSS utilities for Manim"""

    # Screen dimensions
    SCREEN_WIDTH = 14
    SCREEN_HEIGHT = 8

    # Safe content area (with margins)
    CONTENT_LEFT = -6.5
    CONTENT_RIGHT = 6.5
    CONTENT_TOP = 3.5
    CONTENT_BOTTOM = -3.5

    # Named positions
    TOP_LEFT = [-6.5, 3.5, 0]
    TOP_CENTER = [0, 3.5, 0]
    TOP_RIGHT = [6.5, 3.5, 0]
    CENTER_LEFT = [-6.5, 0, 0]
    CENTER = [0, 0, 0]
    CENTER_RIGHT = [6.5, 0, 0]
    BOTTOM_LEFT = [-6.5, -3.5, 0]
    BOTTOM_CENTER = [0, -3.5, 0]
    BOTTOM_RIGHT = [6.5, -3.5, 0]

    @staticmethod
    def constrain(mobject, bounds=None, clamp=True):
        """
        Constrain mobject within bounds (prevent overflow)
        bounds: [x_min, x_max, y_min, y_max]
        clamp: if True, adjust position; if False, return violations
        """
        if bounds is None:
            bounds = [Layout.CONTENT_LEFT, Layout.CONTENT_RIGHT,
                     Layout.CONTENT_BOTTOM, Layout.CONTENT_TOP]

        x_min, x_max, y_min, y_max = bounds
        center = mobject.get_center()
        width = mobject.width
        height = mobject.height

        left = center[0] - width / 2
        right = center[0] + width / 2
        top = center[1] + height / 2
        bottom = center[1] - height / 2

        if clamp:
            new_x = center[0]
            new_y = center[1]

            if left < x_min:
                new_x += (x_min - left)
            if right > x_max:
                new_x -= (right - x_max)
            if top > y_max:
                new_y -= (top - y_max)
            if bottom < y_min:
                new_y += (y_min - bottom)

            mobject.move_to([new_x, new_y, 0])

        return mobject

    @staticmethod
    def position(mobject, x=None, y=None, constrain=True):
        """Position mobject with optional constraint"""
        pos = [x if x is not None else mobject.get_center()[0],
               y if y is not None else mobject.get_center()[1],
               0]
        mobject.move_to(pos)
        if constrain:
            Layout.constrain(mobject)
        return mobject

    @staticmethod
    def center_h(mobject):
        """Center horizontally"""
        Layout.position(mobject, x=0, constrain=False)
        return mobject

    @staticmethod
    def center_v(mobject):
        """Center vertically"""
        Layout.position(mobject, y=0, constrain=False)
        return mobject

    @staticmethod
    def center(mobject):
        """Center both axes"""
        Layout.position(mobject, x=0, y=0, constrain=False)
        return mobject

    @staticmethod
    def horizontal_line(y=0, width=None, **kwargs):
        """Create horizontal line"""
        if width is None:
            width = Layout.SCREEN_WIDTH
        return Line(start=[-width/2, y, 0], end=[width/2, y, 0], **kwargs)

    @staticmethod
    def vertical_line(x=0, height=None, **kwargs):
        """Create vertical line"""
        if height is None:
            height = Layout.SCREEN_HEIGHT
        return Line(start=[x, -height/2, 0], end=[x, height/2, 0], **kwargs)

    @staticmethod
    def distribute_h(items, start=-6.5, end=6.5):
        """Distribute items evenly horizontally"""
        positions = np.linspace(start, end, len(items))
        for item, x in zip(items, positions):
            Layout.position(item, x=x, constrain=True)
        return VGroup(*items)

    @staticmethod
    def distribute_v(items, start=3.5, end=-3.5):
        """Distribute items evenly vertically"""
        positions = np.linspace(start, end, len(items))
        for item, y in zip(items, positions):
            Layout.position(item, y=y, constrain=True)
        return VGroup(*items)

    @staticmethod
    def stack_h(items, spacing=0.5, center_y=0, center_x=0):
        """Stack items horizontally"""
        total_width = sum(item.width for item in items) + \
                     (spacing * (len(items) - 1))
        current_x = center_x - total_width / 2

        for item in items:
            Layout.position(item, x=current_x + item.width/2, y=center_y)
            current_x += item.width + spacing

        return VGroup(*items)

    @staticmethod
    def stack_v(items, spacing=0.5, center_x=0, center_y=0):
        """Stack items vertically"""
        total_height = sum(item.height for item in items) + \
                      (spacing * (len(items) - 1))
        current_y = center_y + total_height / 2

        for item in items:
            Layout.position(item, x=center_x, y=current_y - item.height/2)
            current_y -= item.height + spacing

        return VGroup(*items)

    @staticmethod
    def add_margin(mobject, top=0, right=0, bottom=0, left=0):
        """Add CSS-like margin"""
        center = mobject.get_center()
        mobject.move_to([
            center[0] + (right - left) / 2,
            center[1] + (top - bottom) / 2,
            0
        ])
        return mobject

    @staticmethod
    def scale_responsive(mobject, max_width=None, max_height=None):
        """Scale mobject to fit bounds responsively"""
        if max_width and mobject.width > max_width:
            scale = max_width / mobject.width
            mobject.scale(scale)

        if max_height and mobject.height > max_height:
            scale = max_height / mobject.height
            mobject.scale(scale)

        return mobject


class ObjectPositioner:
    """Advanced object positioning with overlap detection and readability validation"""

    # Minimum safe spacing between objects (in Manim units)
    MIN_VERTICAL_SPACING = 0.3
    MIN_HORIZONTAL_SPACING = 0.2
    CANVAS_TOP = 4.0
    CANVAS_BOTTOM = -4.0
    CANVAS_LEFT = -7.1
    CANVAS_RIGHT = 7.1
    CANVAS_WIDTH = CANVAS_RIGHT - CANVAS_LEFT
    CANVAS_HEIGHT = CANVAS_TOP - CANVAS_BOTTOM

    @staticmethod
    def get_bounds(mobject):
        """
        Get bounding box of a mobject
        Returns: dict with x_min, x_max, y_min, y_max, width, height, center
        """
        if not hasattr(mobject, 'get_center'):
            return None

        center = mobject.get_center()
        width = mobject.width if hasattr(mobject, 'width') else 0
        height = mobject.height if hasattr(mobject, 'height') else 0

        return {
            'x_min': center[0] - width / 2,
            'x_max': center[0] + width / 2,
            'y_min': center[1] - height / 2,
            'y_max': center[1] + height / 2,
            'width': width,
            'height': height,
            'center': center
        }

    @staticmethod
    def check_overlap(bounds1, bounds2, h_spacing=0, v_spacing=0):
        """
        Check if two bounding boxes overlap
        Returns: True if overlapping, False otherwise
        """
        if not bounds1 or not bounds2:
            return False

        h_overlap = (bounds1['x_max'] + h_spacing > bounds2['x_min'] and
                     bounds1['x_min'] - h_spacing < bounds2['x_max'])
        v_overlap = (bounds1['y_max'] + v_spacing > bounds2['y_min'] and
                     bounds1['y_min'] - v_spacing < bounds2['y_max'])

        return h_overlap and v_overlap

    @staticmethod
    def check_multiple_overlaps(bounds, existing_bounds_list, h_spacing=0, v_spacing=0):
        """
        Check if bounds overlaps with any object in the list
        Returns: list of overlapping object indices
        """
        overlaps = []
        for idx, existing_bounds in enumerate(existing_bounds_list):
            if ObjectPositioner.check_overlap(bounds, existing_bounds, h_spacing, v_spacing):
                overlaps.append(idx)
        return overlaps

    @staticmethod
    def is_within_canvas(bounds, margin=0.2):
        """
        Check if object is within canvas bounds
        Returns: (is_within, errors)
        """
        errors = []

        if bounds['x_min'] < ObjectPositioner.CANVAS_LEFT + margin:
            errors.append(f"Object extends beyond left edge (x_min: {bounds['x_min']})")

        if bounds['x_max'] > ObjectPositioner.CANVAS_RIGHT - margin:
            errors.append(f"Object extends beyond right edge (x_max: {bounds['x_max']})")

        if bounds['y_min'] < ObjectPositioner.CANVAS_BOTTOM + margin:
            errors.append(f"Object extends beyond bottom edge (y_min: {bounds['y_min']})")

        if bounds['y_max'] > ObjectPositioner.CANVAS_TOP - margin:
            errors.append(f"Object extends beyond top edge (y_max: {bounds['y_max']})")

        return len(errors) == 0, errors

    @staticmethod
    def position_below(reference_bounds, height, center_x=0, v_spacing=0.3):
        """
        Calculate position for object below reference object
        Returns: y_position
        """
        return reference_bounds['y_min'] - v_spacing - height / 2

    @staticmethod
    def find_safe_y_position(target_height, existing_bounds_list,
                            start_y=0, direction='down', h_spacing=0.2, v_spacing=0.3,
                            center_x=0):
        """
        Find safe Y position for object without overlaps
        Returns: (safe_y, success, used_bounds)
        """
        sorted_bounds = sorted(existing_bounds_list,
                              key=lambda b: b['y_min'] if direction == 'down' else b['y_max'],
                              reverse=(direction == 'down'))

        current_y = start_y
        attempts = 0
        max_attempts = 20

        while attempts < max_attempts:
            # Create temporary bounds at current position
            test_bounds = {
                'x_min': center_x - 3.0,
                'x_max': center_x + 3.0,
                'y_min': current_y - target_height / 2,
                'y_max': current_y + target_height / 2,
                'width': 6.0,
                'height': target_height,
                'center': [center_x, current_y]
            }

            # Check overlaps
            overlaps = ObjectPositioner.check_multiple_overlaps(
                test_bounds, sorted_bounds, h_spacing, v_spacing
            )

            # Check canvas bounds
            within_canvas, errors = ObjectPositioner.is_within_canvas(test_bounds, margin=0.2)

            if not overlaps and within_canvas:
                return current_y, True, test_bounds

            # Move to next position
            if overlaps:
                # Move past the overlapping object
                overlap_idx = overlaps[0]
                overlap_obj = sorted_bounds[overlap_idx]
                if direction == 'down':
                    current_y = overlap_obj['y_min'] - v_spacing - target_height / 2
                else:
                    current_y = overlap_obj['y_max'] + v_spacing + target_height / 2
            else:
                # Move within bounds
                if direction == 'down':
                    current_y -= 0.5
                else:
                    current_y += 0.5

            attempts += 1

        return None, False, None

    @staticmethod
    def layout_objects(scene, objects_with_specs):
        """
        Position multiple objects safely on canvas

        Args:
            scene: Manim scene
            objects_with_specs: list of dicts with:
                - 'object': mobject
                - 'target_y': desired y position
                - 'center_x': x center (default 0)
                - 'width': object width estimate
                - 'height': object height
                - 'name': object name (for debugging)

        Returns: dict with positioning results and any issues
        """
        results = {
            'success': True,
            'placed_objects': [],
            'skipped_objects': [],
            'bounds_list': [],
            'warnings': [],
            'errors': []
        }

        # First pass: collect all bounds
        placed_bounds = []
        for spec in objects_with_specs:
            obj = spec['object']
            bounds = ObjectPositioner.get_bounds(obj)

            if bounds:
                placed_bounds.append({
                    'bounds': bounds,
                    'spec': spec,
                    'name': spec.get('name', 'unknown')
                })

        # Second pass: check for overlaps and reposition if necessary
        for item in placed_bounds:
            bounds = item['bounds']
            spec = item['spec']
            obj = spec['object']
            name = item['name']

            # Check for overlaps with already placed objects
            overlaps = ObjectPositioner.check_multiple_overlaps(
                bounds,
                [b['bounds'] for b in placed_bounds if b['name'] != name],
                h_spacing=ObjectPositioner.MIN_HORIZONTAL_SPACING,
                v_spacing=ObjectPositioner.MIN_VERTICAL_SPACING
            )

            # Check canvas bounds
            within_canvas, errors = ObjectPositioner.is_within_canvas(bounds, margin=0.2)

            if overlaps:
                # Try to find safe position
                safe_y, found_safe, new_bounds = ObjectPositioner.find_safe_y_position(
                    bounds['height'],
                    [b['bounds'] for b in placed_bounds if b['name'] != name],
                    start_y=spec.get('target_y', 0),
                    direction='down',
                    center_x=spec.get('center_x', 0),
                    h_spacing=ObjectPositioner.MIN_HORIZONTAL_SPACING,
                    v_spacing=ObjectPositioner.MIN_VERTICAL_SPACING
                )

                if found_safe:
                    obj.move_to([spec.get('center_x', 0), safe_y, 0])
                    results['warnings'].append(
                        f"{name}: Repositioned from Y={spec.get('target_y', 0):.2f} to Y={safe_y:.2f} to avoid overlap"
                    )
                    item['bounds'] = new_bounds
                    results['placed_objects'].append(name)
                else:
                    results['errors'].append(
                        f"{name}: Could not find safe position without overlaps"
                    )
                    results['skipped_objects'].append(name)
                    results['success'] = False
            elif not within_canvas:
                results['errors'].extend(errors)
                results['errors'].append(f"{name}: Object extends beyond canvas bounds")
                results['skipped_objects'].append(name)
                results['success'] = False
            else:
                results['placed_objects'].append(name)

        results['bounds_list'] = [item['bounds'] for item in placed_bounds]
        return results

    @staticmethod
    def debug_layout(scene, objects_with_specs, results):
        """
        Visualize layout for debugging (shows bounding boxes)
        """
        if not hasattr(scene, 'add'):
            return

        # Print results
        print("\n" + "="*60)
        print("LAYOUT POSITIONING RESULTS")
        print("="*60)
        print(f"Success: {results['success']}")
        print(f"Placed Objects: {len(results['placed_objects'])}")
        print(f"Skipped Objects: {len(results['skipped_objects'])}")

        if results['placed_objects']:
            print("\nPlaced:")
            for name in results['placed_objects']:
                print(f"  ✓ {name}")

        if results['skipped_objects']:
            print("\nSkipped:")
            for name in results['skipped_objects']:
                print(f"  ✗ {name}")

        if results['warnings']:
            print("\nWarnings:")
            for warning in results['warnings']:
                print(f"  ⚠ {warning}")

        if results['errors']:
            print("\nErrors:")
            for error in results['errors']:
                print(f"  ✗ {error}")

        print("="*60 + "\n")
