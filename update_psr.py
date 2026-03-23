import re

projects_data = {
    "RSSI": {
        "title": "RSSI Indoor Positioning Integrated Classroom Attendance",
        "search_pattern": r"A technology-driven project that uses RSSI-based indoor.*?\(Practically Tested in Classroom\)",
        "old_p": r'<p style="color: var\(--text-secondary\); font-size: 0\.95rem; margin-bottom: 25px; flex-grow: 1;">\s*A technology-driven project that uses RSSI-based indoor positioning to automate classroom\s*attendance\. The system enhances accuracy and efficiency by integrating wireless signal\s*strength analysis for indoor localization\. \(Practically Tested in Classroom\)\s*</p>',
        "psr": """<div style="color: var(--text-secondary); font-size: 0.95rem; margin-bottom: 25px; flex-grow: 1; display: flex; flex-direction: column; gap: 10px;">
                            <p><strong style="color: var(--primary-color);">Problem:</strong> Manual attendance tracking is inefficient and prone to errors.</p>
                            <p><strong style="color: var(--primary-color);">Solution:</strong> Engineered an automated system using RSSI-based indoor positioning and wireless signal analysis.</p>
                            <p><strong style="color: var(--primary-color);">Result:</strong> Achieved enhanced localization accuracy; practically validated in a live classroom environment.</p>
                        </div>"""
    },
    "Power BI": {
        "title": "Power BI & Sales Analysis",
        "search_pattern": r"Sales Account analysis using Power BI and Excel case studies\..*?through data visualization and reporting\.",
        "old_p": r'<p style="color: var\(--text-secondary\); font-size: 0\.95rem; margin-bottom: 25px; flex-grow: 1;">\s*Sales Account analysis using Power BI and Excel case studies\. It focuses on analyzing sales\s*performance, trends, and key business insights through data visualization and reporting\.\s*</p>',
        "psr": """<div style="color: var(--text-secondary); font-size: 0.95rem; margin-bottom: 25px; flex-grow: 1; display: flex; flex-direction: column; gap: 10px;">
                            <p><strong style="color: var(--primary-color);">Problem:</strong> Complex sales data lacked actionable insights and clear visibility into market trends.</p>
                            <p><strong style="color: var(--primary-color);">Solution:</strong> Developed interactive Power BI dashboards and Excel models for comprehensive sales account analysis.</p>
                            <p><strong style="color: var(--primary-color);">Result:</strong> Delivered clear visualizations that highlight key performance indicators and drive strategic decision-making.</p>
                        </div>"""
    },
    "Organisational": {
        "title": "Organisational Development & Change",
        "search_pattern": r"Case study on organizational development and change management.*?Examines leadership strategies and restructuring processes\.",
        "old_p": r'<p style="color: var\(--text-secondary\); font-size: 0\.95rem; margin-bottom: 25px; flex-grow: 1;">\s*Case study on organizational development and change management within a family-owned\s*business \(NOVEMA GmbH\)\. Examines leadership strategies and restructuring processes\.\s*</p>',
        "psr": """<div style="color: var(--text-secondary); font-size: 0.95rem; margin-bottom: 25px; flex-grow: 1; display: flex; flex-direction: column; gap: 10px;">
                            <p><strong style="color: var(--primary-color);">Problem:</strong> Structural inefficiencies and market shifts challenged a family-owned business (NOVEMA GmbH).</p>
                            <p><strong style="color: var(--primary-color);">Solution:</strong> Analyzed leadership strategies and proposed change management and restructuring initiatives.</p>
                            <p><strong style="color: var(--primary-color);">Result:</strong> Formulated actionable organizational development plans to ensure long-term business sustainability.</p>
                        </div>"""
    },
    "Accident": {
        "title": "Automatic Accident Informer",
        "search_pattern": r"Embedded systems project that detects vehicle accidents and sends real-time alerts.*?improve emergency response times\.",
        "old_p": r'<p style="color: var\(--text-secondary\); font-size: 0\.95rem; margin-bottom: 25px; flex-grow: 1;">\s*Embedded systems project that detects vehicle accidents and sends real-time alerts using GSM\s*and FM modules to improve emergency response times\.\s*</p>',
        "psr": """<div style="color: var(--text-secondary); font-size: 0.95rem; margin-bottom: 25px; flex-grow: 1; display: flex; flex-direction: column; gap: 10px;">
                            <p><strong style="color: var(--primary-color);">Problem:</strong> Delayed emergency response to vehicle accidents causes preventable fatalities.</p>
                            <p><strong style="color: var(--primary-color);">Solution:</strong> Built an embedded hardware system utilizing GSM and FM modules to detect impacts and trigger alerts.</p>
                            <p><strong style="color: var(--primary-color);">Result:</strong> Successfully prototyped real-time notification capabilities, significantly reducing potential emergency response times.</p>
                        </div>"""
    },
    "R language": {
        "title": "R language",
        "search_pattern": r"This project is a peer-graded assignment developed using the R programming language\..*?reproducible research using R\.",
        "old_p": r'<p style="color: var\(--text-secondary\); font-size: 0\.95rem; margin-bottom: 25px; flex-grow: 1;">\s*This project is a peer-graded assignment developed using the R programming language\. It\s*focuses on prediction and statistical analysis by applying data exploration, model building,\s*and result interpretation\. The project demonstrates foundational skills in data analysis,\s*statistical reasoning, and reproducible research using R\.\s*</p>',
        "psr": """<div style="color: var(--text-secondary); font-size: 0.95rem; margin-bottom: 25px; flex-grow: 1; display: flex; flex-direction: column; gap: 10px;">
                            <p><strong style="color: var(--primary-color);">Problem:</strong> High-dimensional datasets require robust statistical models for accurate predictive exploration.</p>
                            <p><strong style="color: var(--primary-color);">Solution:</strong> Applied R programming for data cleaning, statistical reasoning, and building predictive models.</p>
                            <p><strong style="color: var(--primary-color);">Result:</strong> Demonstrated proficiency in reproducible research and delivered highly accurate statistical analyses.</p>
                        </div>"""
    },
    "Retail": {
        "title": "The New Kings of the Shelf",
        "search_pattern": r"A research-based project analyzing the competitive dynamics between manufacturers and\s*private-label brands\..*?consumer\s*behavior shaping modern retail\.",
        "old_p": r'<p style="color: var\(--text-secondary\); font-size: 0\.95rem; margin-bottom: 25px; flex-grow: 1;">\s*A research-based project analyzing the competitive dynamics between manufacturers and\s*private-label brands\. The study explores market trends, strategic implications, and consumer\s*behavior shaping modern retail\.\s*</p>',
        "psr": """<div style="color: var(--text-secondary); font-size: 0.95rem; margin-bottom: 25px; flex-grow: 1; display: flex; flex-direction: column; gap: 10px;">
                            <p><strong style="color: var(--primary-color);">Problem:</strong> Rapid rise of private-label brands disrupts traditional manufacturer dominance in retail.</p>
                            <p><strong style="color: var(--primary-color);">Solution:</strong> Conducted in-depth market research on competitive dynamics, consumer behavior, and retail strategies.</p>
                            <p><strong style="color: var(--primary-color);">Result:</strong> Authored a comprehensive report detailing strategic implications and future trends in the retail revolution.</p>
                        </div>"""
    }
}

for filename in ['projects.html', 'projects-research.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for key, data in projects_data.items():
        content = re.sub(data['old_p'], data['psr'], content)
        
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated projects with PSR framework.")
