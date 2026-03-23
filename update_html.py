import os
import glob

html_files = glob.glob("*.html")

new_footer = """    <!-- Footer -->
    <footer style="padding: 40px 0; border-top: 1px solid rgba(0,0,0,0.05); color: var(--text-light); background-color: var(--bg-body);">
        <div class="container" style="display: flex; flex-direction: column; align-items: center; gap: 20px;">
            <div style="display: flex; gap: 20px; flex-wrap: wrap; justify-content: center;">
                <a href="impressum.html" style="color: var(--text-secondary); text-decoration: none; font-weight: 500;">Impressum</a>
                <a href="datenschutz.html" style="color: var(--text-secondary); text-decoration: none; font-weight: 500;">Datenschutz</a>
                <a href="https://linkedin.com/in/snekanthbabu" target="_blank" style="color: var(--text-secondary); text-decoration: none; font-weight: 500;">LinkedIn</a>
                <a href="https://github.com/snekan" target="_blank" style="color: var(--text-secondary); text-decoration: none; font-weight: 500;">GitHub</a>
                <a href="games.html" style="color: var(--text-secondary); text-decoration: none; font-weight: 500;">Playground</a>
            </div>
            <p style="text-align: center;">&copy; 2026 Snekanth Babu. Built with Warm Minimalism.</p>
        </div>
    </footer>"""

import re

for file_path in html_files:
    if file_path in ['impressum.html', 'datenschutz.html']:
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove games from nav
    content = re.sub(r'<li>\s*<a href="games\.html".*?>Games</a>\s*</li>', '', content)

    # Replace footer
    # Find the footer block
    footer_pattern = re.compile(r'<!--\s*Simple Footer\s*-->\s*<footer.*?>\s*<p>&copy; 2026 Snekanth Babu.*?</p>\s*</footer>', re.DOTALL)
    
    if footer_pattern.search(content):
        content = footer_pattern.sub(new_footer, content)
    else:
        # Sometimes there might just be <footer>...</footer>, let's try a broader match if not found
        fallback_pattern = re.compile(r'<footer.*?>.*?</footer\s*>', re.DOTALL)
        content = fallback_pattern.sub(new_footer, content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Updated {len(html_files)} HTML files.")

# Create impressum.html and datenschutz.html based on index.html's head and nav template
template_with_nav = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Snekanth Babu</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>

    <!-- Navigation -->
    <nav class="navbar">
        <div class="container nav-container">
            <a href="index.html" class="logo">Snekanth<span>.</span></a>
            <button class="mobile-toggle" aria-label="Toggle navigation">☰</button>
            <ul class="nav-menu">
                <li><a href="index.html" class="nav-link">About Me</a></li>
                <li><a href="projects-research.html" class="nav-link">Projects & Research</a></li>
                <li><a href="education.html" class="nav-link">Education & Certificates</a></li>
                <li><a href="experience.html" class="nav-link">Work Experience</a></li>
                <li><a href="skills.html" class="nav-link">Skills</a></li>
                <li><a href="purpose.html" class="nav-link">Purpose & Blog</a></li>
                <li><a href="contact.html" class="nav-link">Contact</a></li>
            </ul>
        </div>
    </nav>

    <section>
        <div class="container">
            <h1 class="section-title">{title}</h1>
            <p class="section-subtitle" style="margin-bottom: 40px;">{subtitle}</p>
            <div class="card" style="max-width: 800px; line-height: 1.8;">
{content}
            </div>
        </div>
    </section>

""" + new_footer + """

    <script src="js/main.js"></script>
</body>
</html>
"""

impressum_content = """                <h3 style="margin-bottom: 20px;">Angaben gemäß § 5 TMG</h3>
                <p style="margin-bottom: 15px;">
                    Snekanth Babu<br>
                    Berlin, Germany<br>
                </p>
                <h3 style="margin-bottom: 20px; margin-top: 30px;">Kontakt</h3>
                <p>
                    E-Mail: snekanthbabu@example.com<br>
                </p>"""

datenschutz_content = """                <h3 style="margin-bottom: 20px;">1. Datenschutz auf einen Blick</h3>
                <h4 style="margin-bottom: 10px; margin-top: 20px;">Allgemeine Hinweise</h4>
                <p style="margin-bottom: 15px;">
                    Die folgenden Hinweise geben einen einfachen Überblick darüber, was mit Ihren personenbezogenen Daten passiert, wenn Sie diese Website besuchen. Personenbezogene Daten sind alle Daten, mit denen Sie persönlich identifiziert werden können.
                </p>
                <h4 style="margin-bottom: 10px; margin-top: 20px;">Datenerfassung auf dieser Website</h4>
                <p style="margin-bottom: 15px;">
                    Die Datenverarbeitung auf dieser Website erfolgt durch den Websitebetreiber. Diese Website erhebt keine personenbezogenen Daten, da es sich um eine statische Portfolio-Seite handelt. Falls Sie per E-Mail Kontakt aufnehmen, werden Ihre Daten nur zur Bearbeitung der Anfrage verwendet.
                </p>
"""

with open('impressum.html', 'w', encoding='utf-8') as f:
    f.write(template_with_nav.format(title="Impressum", subtitle="Legal Notice", content=impressum_content))

with open('datenschutz.html', 'w', encoding='utf-8') as f:
    f.write(template_with_nav.format(title="Datenschutz", subtitle="Privacy Policy (GDPR)", content=datenschutz_content))

print("Created impressum.html and datenschutz.html.")
