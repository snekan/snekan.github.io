import glob
import re

html_files = glob.glob("*.html")

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add loading="lazy" if not already present
    content = re.sub(r'<img\s+(?!.*loading="lazy")(.*?/?>)', r'<img loading="lazy" \1', content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Added lazy loading to all images.")
