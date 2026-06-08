"""Generate PWA icons for AI Companion"""
from PIL import Image, ImageDraw, ImageFont
import os

SIZES = [72, 96, 128, 144, 152, 192, 384, 512]
OUT_DIR = 'icons'

os.makedirs(OUT_DIR, exist_ok=True)

def create_icon(size):
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Gradient background circle
    for y in range(size):
        for x in range(size):
            dx = x - size/2
            dy = y - size/2
            dist = (dx*dx + dy*dy) ** 0.5
            if dist < size/2:
                ratio = min(1.0, (size/2 - dist + 2) / (size/2 + 2))
                # Purple to Blue gradient
                r = int(91 + (139 - 91) * (y / size))
                g = int(106 + (92 - 106) * (y / size))
                b = int(240 + (246 - 240) * (y / size))
                alpha = int(255 * ratio)
                img.putpixel((x, y), (r, g, b, alpha))

    # Draw a simple chat bubble symbol
    cx, cy = size // 2, size // 2
    bubble_scale = size / 192

    # Outer chat bubble
    bubble_w = int(80 * bubble_scale)
    bubble_h = int(56 * bubble_scale)
    bx1 = cx - bubble_w // 2
    by1 = cy - bubble_h // 2 - int(2 * bubble_scale)
    bx2 = cx + bubble_w // 2
    by2 = cy + bubble_h // 2

    # Rounded rectangle for chat bubble
    draw.rounded_rectangle(
        [bx1, by1, bx2, by2],
        radius=int(12 * bubble_scale),
        fill=(255, 255, 255, 220)
    )

    # Small triangle tail
    tail_points = [
        (cx + bubble_w // 4, by2),
        (cx + bubble_w // 2, by2 + int(12 * bubble_scale)),
        (cx + bubble_w // 4 + int(8 * bubble_scale), by2)
    ]
    draw.polygon(tail_points, fill=(255, 255, 255, 220))

    # Dots in bubble
    dot_r = int(4 * bubble_scale)
    dot_y = by1 + bubble_h // 2 - dot_r
    for i in range(3):
        dx = cx - int(14 * bubble_scale) + i * int(14 * bubble_scale)
        draw.ellipse(
            [dx - dot_r, dot_y - dot_r, dx + dot_r, dot_y + dot_r],
            fill=(91, 106, 240, 200)
        )

    # Save
    path = os.path.join(OUT_DIR, f'icon-{size}.png')
    img.save(path, 'PNG')
    print(f'  Created {path}')

    # Also save as maskable padding version for 192 and 512
    if size in (192, 512):
        # Create a version with safe zone padding for Android adaptive icons
        pad_img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        pad_size = int(size * 0.8)
        inner = img.resize((pad_size, pad_size), Image.LANCZOS)
        offset = (size - pad_size) // 2
        pad_img.paste(inner, (offset, offset), inner)
        mask_path = os.path.join(OUT_DIR, f'maskable-{size}.png')
        pad_img.save(mask_path, 'PNG')
        print(f'  Created {mask_path}')

print('Generating icons...')
for s in SIZES:
    create_icon(s)
print('Done!')
