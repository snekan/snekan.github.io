import glob
import re

html_files = glob.glob("*.html")

new_nav = """            <ul class="nav-menu">
                <li><a href="index.html" class="nav-link{active_index}">About Me</a></li>
                <li><a href="index.html#motivation" class="nav-link">Motivation & Vision</a></li>
                <li><a href="projects.html" class="nav-link{active_projects}">Projects</a></li>
                <li><a href="skills.html" class="nav-link{active_skills}">Skills</a></li>
                <li><a href="games.html" class="nav-link{active_games}">The Lab</a></li>
                <li><a href="contact.html" class="nav-link{active_contact}">Contact</a></li>
            </ul>"""

# The active mapping could be tricky, let's just replace the whole ul block carefully
# But we need to maintain the 'active' class on the correct link for each page.
# Actually, it might be easier to just regex replace the <ul> block with dynamic substitution.

for file_path in html_files:
    if file_path in ['impressum.html', 'datenschutz.html']:
        # They don't have active classes specifically, just regular navigation
        pass

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Determine active classes
    a_in = ' active' if file_path == 'index.html' else ''
    # projects-research and projects both go to projects active conceptually, but let's map them
    a_pr = ' active' if file_path in ['projects.html', 'projects-research.html'] else ''
    a_sk = ' active' if file_path == 'skills.html' else ''
    a_ga = ' active' if file_path == 'games.html' else ''
    a_co = ' active' if file_path == 'contact.html' else ''

    current_new_nav = new_nav.format(
        active_index=a_in,
        active_projects=a_pr,
        active_skills=a_sk,
        active_games=a_ga,
        active_contact=a_co
    )

    # find the ul block
    pattern = re.compile(r'<ul class="nav-menu">.*?</ul>', re.DOTALL)
    content = pattern.sub(current_new_nav, content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Updated navigation in {len(html_files)} HTML files.")
