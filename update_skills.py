import re

skills_html_path = "skills.html"

with open(skills_html_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_grid = """            <div class="grid-2">

                <!-- 1. Technical Skills -->
                <div class="card" style="border-left: 5px solid var(--primary-color);">
                    <h3 style="margin-bottom: 20px; font-size: 1.4rem;">Technical</h3>
                    <div class="tags">
                        <span class="tag">Process Mapping (BPMN)</span>
                        <span class="tag">Data Analysis (Excel, Power BI)</span>
                        <span class="tag">Python</span>
                        <span class="tag">C</span>
                    </div>
                </div>

                <!-- 2. Analytical Skills -->
                <div class="card" style="border-left: 5px solid var(--primary-color);">
                    <h3 style="margin-bottom: 20px; font-size: 1.4rem;">Analytical</h3>
                    <div class="tags">
                        <span class="tag">Systems Thinking</span>
                        <span class="tag">Operational Efficiency</span>
                        <span class="tag">Data-driven Decision Making</span>
                    </div>
                </div>

            </div>"""

pattern = re.compile(r'<div class="grid-2">.*?</div>\s*</div>\s*</section>', re.DOTALL)

replacement = new_grid + "\n        </div>\n    </section>"

new_content = pattern.sub(replacement, content)

with open(skills_html_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Skills updated.")
