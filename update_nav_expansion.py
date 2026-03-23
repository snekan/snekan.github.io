import glob
import re

html_files = glob.glob("*.html")

new_nav = """            <ul class="nav-menu">
                <li><a href="index.html" class="nav-link{active_index}">About Me</a></li>
                <li><a href="motivation.html" class="nav-link{active_motivation}">Motivation</a></li>
                <li><a href="sop.html" class="nav-link{active_sop}">SOP & Vision</a></li>
                <li><a href="projects.html" class="nav-link{active_projects}">Projects</a></li>
                <li><a href="education.html" class="nav-link{active_education}">Education & Certificates</a></li>
                <li><a href="experience.html" class="nav-link{active_experience}">Work Experience</a></li>
                <li><a href="skills.html" class="nav-link{active_skills}">Skills</a></li>
                <li><a href="purpose.html" class="nav-link{active_purpose}">Purpose & Blog</a></li>
                <li><a href="games.html" class="nav-link{active_games}">The Lab</a></li>
                <li><a href="contact.html" class="nav-link{active_contact}">Contact</a></li>
            </ul>"""

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    a_in = ' active' if file_path == 'index.html' else ''
    a_mo = ' active' if file_path == 'motivation.html' else ''
    a_so = ' active' if file_path == 'sop.html' else ''
    a_pr = ' active' if file_path in ['projects.html', 'projects-research.html'] else ''
    a_ed = ' active' if file_path == 'education.html' else ''
    a_ex = ' active' if file_path == 'experience.html' else ''
    a_sk = ' active' if file_path == 'skills.html' else ''
    a_pu = ' active' if file_path == 'purpose.html' else ''
    a_ga = ' active' if file_path == 'games.html' else ''
    a_co = ' active' if file_path == 'contact.html' else ''

    current_new_nav = new_nav.format(
        active_index=a_in,
        active_motivation=a_mo,
        active_sop=a_so,
        active_projects=a_pr,
        active_education=a_ed,
        active_experience=a_ex,
        active_skills=a_sk,
        active_purpose=a_pu,
        active_games=a_ga,
        active_contact=a_co
    )

    pattern = re.compile(r'<ul class="nav-menu">.*?</ul>', re.DOTALL)
    content = pattern.sub(current_new_nav, content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Updated navigation in {len(html_files)} HTML files.")
