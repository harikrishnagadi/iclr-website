"""
Create professional PNG icons for Scene 4
Colors match HierLoc design: #e8a838 (accent)
"""

from PIL import Image, ImageDraw
import os

# HierLoc colors
ACCENT_COLOR = "#e8a838"
ACCENT_RGB = (232, 168, 56)
BG_COLOR = (10, 10, 15)  # Dark background

def create_image_icon():
    """Create image/photo icon"""
    size = 256
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Frame (rectangle)
    margin = 30
    draw.rectangle(
        [(margin, margin), (size-margin, size-margin)],
        outline=ACCENT_RGB,
        width=8
    )
    
    # Circle (lens)
    circle_center = (size // 2, size // 2)
    circle_radius = 40
    draw.ellipse(
        [(circle_center[0]-circle_radius, circle_center[1]-circle_radius),
         (circle_center[0]+circle_radius, circle_center[1]+circle_radius)],
        outline=ACCENT_RGB,
        width=6
    )
    
    # Dot (highlight)
    dot_pos = (size // 2 + 60, 80)
    dot_radius = 12
    draw.ellipse(
        [(dot_pos[0]-dot_radius, dot_pos[1]-dot_radius),
         (dot_pos[0]+dot_radius, dot_pos[1]+dot_radius)],
        fill=ACCENT_RGB
    )
    
    img.save("image_icon.png")
    print("✓ Image icon created")

def create_location_icon():
    """Create location pin icon"""
    size = 256
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Pin shape (inverted teardrop)
    center_x, center_y = size // 2, size // 2
    radius = 50
    
    # Pin point (triangle at bottom)
    points = [
        (center_x, center_y + radius + 40),  # Bottom point
        (center_x - 30, center_y),  # Left
        (center_x + 30, center_y),  # Right
    ]
    draw.polygon(points, outline=ACCENT_RGB, width=6)
    
    # Circle (pin head)
    draw.ellipse(
        [(center_x - radius, center_y - radius),
         (center_x + radius, center_y + radius)],
        outline=ACCENT_RGB,
        width=8
    )
    
    # Center dot
    dot_radius = 15
    draw.ellipse(
        [(center_x - dot_radius, center_y - dot_radius),
         (center_x + dot_radius, center_y + dot_radius)],
        fill=ACCENT_RGB
    )
    
    img.save("location_icon.png")
    print("✓ Location icon created")

def create_name_icon():
    """Create name/text icon"""
    size = 256
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Text "Aa"
    try:
        # Try to use a bold font
        import PIL.ImageFont as ImageFont
        try:
            font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 120)
        except:
            font = ImageFont.load_default()
    except:
        font = None
    
    # Draw "Aa" text
    text = "Aa"
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    
    text_x = (size - text_width) // 2
    text_y = (size - text_height) // 2 - 20
    
    draw.text((text_x, text_y), text, fill=ACCENT_RGB, font=font)
    
    # Underline
    underline_y = size // 2 + 60
    draw.line(
        [(60, underline_y), (size - 60, underline_y)],
        fill=ACCENT_RGB,
        width=10
    )
    
    img.save("name_icon.png")
    print("✓ Name icon created")

if __name__ == "__main__":
    os.chdir("/Volumes/SSD/iclr-website/manim_video/assets/icons")
    create_image_icon()
    create_location_icon()
    create_name_icon()
    print("\n✓ All icons created successfully!")
