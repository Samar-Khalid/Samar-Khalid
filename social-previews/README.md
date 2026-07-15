# Social Preview Images Guide

## How to Use These Images

### Step 1: Convert SVG to PNG

These SVG files need to be converted to PNG (1280x640px) for GitHub.

#### Option 1: Online Converter
1. Go to https://convertio.co/svg-png/
2. Upload the SVG file
3. Download the PNG

#### Option 2: Using Python
```python
from cairosvg import svg2png

svg_files = [
    "prism-analytics.svg",
    "prism-enterprise-benchmark.svg",
    "codex-enterprise.svg",
    "prism-data-generator.svg",
    "odoo-custom-modules.svg",
    "ai-bi-learning.svg"
]

for svg_file in svg_files:
    svg2png(url=svg_file, write_to=svg_file.replace('.svg', '.png'))
```

#### Option 3: Using Inkscape
```bash
inkscape --export-type=png --export-filename=output.png input.svg
```

### Step 2: Upload to GitHub

For each repository:

1. Go to the repository on GitHub
2. Click **Settings** (gear icon next to "About")
3. In the **Social preview** section, click **Edit**
4. Upload the PNG file (1280x640px)
5. Click **Save changes**

### Step 3: Verify

After uploading, your repository will show the preview image when shared on:
- Twitter/X
- LinkedIn
- Facebook
- Slack
- Any other platform that supports Open Graph

---

## Image Files

| File | Repository | Color |
|------|-----------|-------|
| `prism-analytics.svg` | Prism-Analytics | Blue (#58A6FF) |
| `prism-enterprise-benchmark.svg` | Prism-Enterprise-Benchmark | Purple (#A78BFA) |
| `codex-enterprise.svg` | Codex-Enterprise | Red (#FF7B72) |
| `prism-data-generator.svg` | Prism-Data-Generator | Yellow (#D29922) |
| `odoo-custom-modules.svg` | Odoo-Custom-Modules | Odoo Purple (#875A7B) |
| `ai-bi-learning.svg` | AI-BI-Learning | Light Blue (#38BDF8) |

---

## Design Features

Each image includes:
- Dark gradient background (#0D1117 to #161B22)
- Corner decorations
- Emoji logo
- Project title
- Subtitle description
- Technology badges
- Tagline
- Author name

---

## Quick Commands

### Convert all SVGs to PNGs
```bash
# Using ImageMagick
for file in *.svg; do
    convert -background none -density 300 "$file" "${file%.svg}.png"
done

# Using Python
pip install cairosvg
python convert_svg.py
```

### Upload all to GitHub
```bash
gh repo edit Samar-Khalid/Prism-Analytics --add-topic social-preview
# Then manually upload via web UI
```
