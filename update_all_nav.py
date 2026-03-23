import glob
import re

html_files = glob.glob("*.html")

new_nav = """            <ul class="nav-menu">
                <li><a href="index.html" class="nav-link{active_index}"><span class="lang-de">Home</span><span class="lang-en" style="display:none;">Home</span></a></li>
                <li><a href="experience.html" class="nav-link{active_experience}"><span class="lang-de">Erfahrung</span><span class="lang-en" style="display:none;">Experience</span></a></li>
                <li><a href="projects.html" class="nav-link{active_projects}"><span class="lang-de">Projekte</span><span class="lang-en" style="display:none;">Projects</span></a></li>
                <li><a href="education.html" class="nav-link{active_education}"><span class="lang-de">Bildung</span><span class="lang-en" style="display:none;">Education</span></a></li>
                <li><a href="sop.html" class="nav-link{active_sop}"><span class="lang-de">Vision</span><span class="lang-en" style="display:none;">Vision</span></a></li>
                <li><a href="games.html" class="nav-link{active_games}"><span class="lang-de">Labor</span><span class="lang-en" style="display:none;">The Lab</span></a></li>
                <li><a href="contact.html" class="nav-link{active_contact}"><span class="lang-de">Kontakt</span><span class="lang-en" style="display:none;">Contact</span></a></li>
                <li style="display: flex; align-items: center; margin-left: 10px;">
                    <span class="toggle-label de active" style="margin-right: 8px;">DE</span>
                    <label class="toggle-switch">
                        <input type="checkbox" id="langToggle">
                        <span class="slider round"></span>
                    </label>
                    <span class="toggle-label en" style="margin-left: 8px; color: var(--text-light);">EN</span>
                </li>
            </ul>"""

new_footer = """    <footer style="background-color: var(--bg-accent); padding: 60px 0; border-top: 1px solid rgba(0,0,0,0.05); margin-top: 80px;">
        <div class="container" style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 20px;">
            <p style="color: var(--text-secondary); font-size: 0.9rem;">&copy; 2026 Snekanth Babu. All rights reserved.</p>
            <div style="display: flex; gap: 30px;">
                <a href="impressum.html" style="text-decoration: none; color: var(--text-secondary); font-size: 0.9rem;">Impressum</a>
                <a href="datenschutz.html" style="text-decoration: none; color: var(--text-secondary); font-size: 0.9rem;">Datenschutz</a>
            </div>
        </div>
    </footer>"""

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Determine active classes
    a_in = ' active' if file_path == 'index.html' else ''
    a_mot = ' active' if file_path == 'motivation.html' else ''
    a_sop = ' active' if file_path == 'sop.html' else ''
    a_pr = ' active' if file_path == 'projects.html' else ''
    a_ed = ' active' if file_path == 'education.html' else ''
    a_ex = ' active' if file_path == 'experience.html' else ''
    a_sk = ' active' if file_path == 'skills.html' else ''
    a_pu = ' active' if file_path == 'purpose.html' else ''
    a_ga = ' active' if file_path == 'games.html' else ''
    a_co = ' active' if file_path == 'contact.html' else ''
    a_va = ' active' if file_path == 'vault.html' else ''

    current_new_nav = new_nav.format(
        active_index=a_in,
        active_motivation=a_mot,
        active_sop=a_sop,
        active_projects=a_pr,
        active_education=a_ed,
        active_experience=a_ex,
        active_skills=a_sk,
        active_purpose=a_pu,
        active_games=a_ga,
        active_contact=a_co,
        active_vault=a_va
    )

    # 1. Update Navigation
    nav_pattern = re.compile(r'<ul class="nav-menu">.*?</ul>', re.DOTALL)
    if nav_pattern.search(content):
        content = nav_pattern.sub(current_new_nav, content)

    # 2. Update Footer (Inject before </body> or replace old footer)
    footer_pattern = re.compile(r'<footer.*?>.*?</footer>', re.DOTALL)
    if footer_pattern.search(content):
        content = footer_pattern.sub(new_footer, content)
    else:
        content = content.replace('</body>', f'{new_footer}\n</body>')

    # 3. Clean up old fonts and Ensure Inter/Lora are ready (handled by style.css but let's clean head)
    content = re.sub(r'<link.*?family=Outfit.*?>', '', content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Synced {file_path}")

print("Global structural sync complete!")
