import cairosvg
import os

# Social previews directory
social_dir = r"C:\Users\Samar.Khalid\Desktop\Career\GitHub-Profile\social-previews"

# SVG files to convert
svg_files = [
    "prism-analytics.svg",
    "prism-enterprise-benchmark.svg",
    "codex-enterprise.svg",
    "prism-data-generator.svg",
    "odoo-custom-modules.svg",
    "ai-bi-learning.svg"
]

# Convert each SVG to PNG
for svg_file in svg_files:
    svg_path = os.path.join(social_dir, svg_file)
    png_path = os.path.join(social_dir, svg_file.replace('.svg', '.png'))
    
    if os.path.exists(svg_path):
        cairosvg.svg2png(
            url=svg_path,
            write_to=png_path,
            output_width=1280,
            output_height=640
        )
        print(f"✅ Converted: {svg_file} → {svg_file.replace('.svg', '.png')}")
    else:
        print(f"❌ Not found: {svg_file}")

print("\n✅ All conversions complete!")
