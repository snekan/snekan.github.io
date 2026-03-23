import re

project_files = ["projects.html", "projects-research.html"]

new_projects = """            <div class="grid-auto">

                <!-- Case Study 1 -->
                <div class="card" style="padding: 0; overflow: hidden; display: flex; flex-direction: column; border-top: 4px solid var(--primary-color);">
                    <div style="padding: 30px; display: flex; flex-direction: column; flex-grow: 1;">
                        <span class="badge" style="align-self: flex-start; margin-bottom: 15px;">Case Study</span>
                        <h3 style="margin-bottom: 15px; font-size: 1.25rem;">Warehouse Returns Workflow Analysis</h3>
                        <div style="color: var(--text-secondary); font-size: 0.95rem; margin-bottom: 25px; flex-grow: 1; display: flex; flex-direction: column; gap: 10px;">
                            <p><strong style="color: var(--primary-color);">Problem:</strong> High return rates and inefficient processing led to warehouse bottlenecks and increased operational costs.</p>
                            <p><strong style="color: var(--primary-color);">Solution:</strong> Mapped current return workflows using BPMN, identified critical bottlenecks, and proposed data-driven process optimizations.</p>
                            <p><strong style="color: var(--primary-color);">Result:</strong> Delivered a streamlined workflow model that significantly reduces processing time and minimizes waste.</p>
                        </div>
                    </div>
                </div>

                <!-- Case Study 2 -->
                <div class="card" style="padding: 0; overflow: hidden; display: flex; flex-direction: column; border-top: 4px solid var(--primary-color);">
                    <div style="padding: 30px; display: flex; flex-direction: column; flex-grow: 1;">
                        <span class="badge" style="align-self: flex-start; margin-bottom: 15px;">Case Study</span>
                        <h3 style="margin-bottom: 15px; font-size: 1.25rem;">Supply Chain Logistics Simulation</h3>
                        <div style="color: var(--text-secondary); font-size: 0.95rem; margin-bottom: 25px; flex-grow: 1; display: flex; flex-direction: column; gap: 10px;">
                            <p><strong style="color: var(--primary-color);">Problem:</strong> Lack of visibility into supply chain dynamics caused unpredictable delays and resource underutilization.</p>
                            <p><strong style="color: var(--primary-color);">Solution:</strong> Built a simulated logistical model applying systems thinking to evaluate operational efficiency under various constraints.</p>
                            <p><strong style="color: var(--primary-color);">Result:</strong> Identified actionable strategies for inventory management and scalable logistics distribution.</p>
                        </div>
                    </div>
                </div>

                <!-- Case Study 3 -->
                <div class="card" style="padding: 0; overflow: hidden; display: flex; flex-direction: column; border-top: 4px solid var(--primary-color);">
                    <div style="padding: 30px; display: flex; flex-direction: column; flex-grow: 1;">
                        <span class="badge" style="align-self: flex-start; margin-bottom: 15px;">Case Study</span>
                        <h3 style="margin-bottom: 15px; font-size: 1.25rem;">Operations Data Dashboard (Power BI)</h3>
                        <div style="color: var(--text-secondary); font-size: 0.95rem; margin-bottom: 25px; flex-grow: 1; display: flex; flex-direction: column; gap: 10px;">
                            <p><strong style="color: var(--primary-color);">Problem:</strong> Disconnected data sources hindered management's ability to make real-time, data-driven operational decisions.</p>
                            <p><strong style="color: var(--primary-color);">Solution:</strong> Aggregated multiple data streams into a centralized Excel and Power BI reporting infrastructure.</p>
                            <p><strong style="color: var(--primary-color);">Result:</strong> Deployed interactive dashboards that track operational KPIs and provide clear oversight of system performance.</p>
                        </div>
                    </div>
                </div>

            </div>"""

for filename in project_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # replace everything between <div class="grid-auto"> ... closing </div> logic
    pattern = re.compile(r'<div class="grid-auto">.*?</div>\s*</div>\s*</section>', re.DOTALL)
    replacement = new_projects + "\n        </div>\n    </section>"
    
    new_content = pattern.sub(replacement, content)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("Updated projects files with Case Studies.")
