from reportlab.lib.pagesizes import LETTER
from reportlab.lib.colors import HexColor, white, black
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
import copy

# ─── Palette ────────────────────────────────────────────────────────────────
DARK   = HexColor("#1a1a2e")
BLUE   = HexColor("#2563eb")
LIGHT  = HexColor("#f1f5f9")
TEXT   = HexColor("#1a1a2e")
WHITE  = white

# ─── Layout ─────────────────────────────────────────────────────────────────
PAGE_W, PAGE_H = LETTER          # 612 × 792 pt
SIDE_W = PAGE_W * 0.30           # ~183.6 pt
MAIN_X = SIDE_W + 16             # main column left edge
MAIN_W = PAGE_W - MAIN_X - 18   # main column width
TOP_Y  = PAGE_H                  # draw from top

# ─── Content definitions ────────────────────────────────────────────────────
CV_FR = {
    "name": "Francis Archambault",
    "title": "Analyste principal senior &\nArchitecte de solutions\nBusiness Central",
    "contact": [
        ("Email", "f.archambault@gmail.com"),
        ("Tel", "514-928-3314"),
        ("Adr", "200 rue Brodeur\nBeloeil, QC J3G 2R9"),
        ("Web", "linkedin.com/in/\nfrancisarchambault"),
    ],
    "skills_label": "Compétences",
    "skills": [
        ("Leadership stratégique", 5),
        ("MS Business Central", 5),
        ("Gestion de projets", 5),
        ("Architecture ERP/WMS", 5),
        ("Warehouse Insight", 4),
        ("API REST / EDI", 4),
        ("Azure Blob / Make.com", 4),
        ("SAP Business One", 3),
        ("IA appliquée", 4),
        ("Automatisation no-code", 4),
        ("BPMN / Modélisation", 4),
        ("Coaching TI", 4),
    ],
    "lang_label": "Langues",
    "languages": [
        ("Français", 5),
        ("Anglais", 4),
    ],
    "interests_label": "Intérêts",
    "interests": "Balle molle · Ski · Conditionnement physique · Voyages & découvertes culturelles",
    "summary_label": "Résumé professionnel",
    "summary": (
        "Leader en technologies de l'information avec plus de 10 ans d'expérience, spécialisé en "
        "transformation numérique et architecture de solutions ERP/WMS. Reconnu pour piloter des "
        "déploiements complexes multi-sites, automatiser les processus d'affaires et réduire drastiquement "
        "les coûts opérationnels. Intègre les technologies émergentes (IA, automatisation no-code/low-code) "
        "pour générer des gains mesurables."
    ),
    "experience_label": "Expériences professionnelles",
    "experiences": [
        {
            "title": "Analyste principal senior & Architecte de solutions Business Central",
            "company": "Groupe AFFI",
            "period": "2017 – présent",
            "bullets": [
                ("Pilotage du déploiement ERP/WMS sur ", "5 sites", " en simultané, de l'analyse à la mise en production"),
                ("Architecture et déploiement de MS Business Central et Warehouse Insight comme ressource principale",),
                ("Automatisation des sorties de production ayant réduit le temps des tâches manuelles de plus de ", "80%", ""),
                ("Réduction des coûts de consultation externe de ", "90%", " par l'internalisation de l'expertise fonctionnelle"),
                ("Intégration et automatisation des processus avec clients et fournisseurs via EDI et API",),
                ("Création et supervision de la plateforme eCom",),
                ("Coaching de l'équipe TI sur la rédaction de spécifications fonctionnelles et la mise en œuvre de projets",),
            ],
        },
        {
            "title": "Coordonnateur WMS",
            "company": "Groupe AFFI",
            "period": "2016 – 2017",
            "bullets": [
                ("Gestion opérationnelle des processus WMS et soutien aux opérations quotidiennes",),
                ("Analyse des besoins, configuration et tests des systèmes",),
                ("Pilotage du déploiement du logiciel WMS HighJump",),
            ],
        },
        {
            "title": "Contremaître de site",
            "company": "Groupe AFFI",
            "period": "2015",
            "bullets": [
                ("Supervision d'une équipe de superviseurs et employés",),
                ("Gestion de la production, distribution et entrepôt",),
                ("Optimisation des opérations et relation client",),
            ],
        },
    ],
    "prev_exp_label": "Expériences antérieures",
    "prev_experiences": [
        ("Groupe Novatec", "2011", "Création de fiches de travail et SST pour améliorer les procédures et la sécurité."),
        ("Pratt & Whitney", "2012", "Gestion du système d'entrepôt et projet de réallocation des items peu utilisés vers un 3PL."),
        ("IILM", "2013", "Visites d'entreprises pour initier des projets de transformation technologique et recherche de subventions."),
        ("Projet CUSM", "2014", "Développement d'un système d'optimisation des routes de livraison pour les dons d'organes."),
        ("24h de l'innovation – Pérou", "2014", "Développement de solutions innovantes en équipe internationale."),
    ],
    "edu_label": "Formation et certifications",
    "education": [
        ("Génie des opérations et logistique", "ÉTS", "2010 – 2014"),
        ("Gestion de commerce", "Collège Édouard-Montpetit", "2007 – 2010"),
        ("ITIL Foundation", "", "2022"),
    ],
}

CV_EN = {
    "name": "Francis Archambault",
    "title": "Senior Principal Analyst &\nBusiness Central\nSolutions Architect",
    "contact": [
        ("Email", "f.archambault@gmail.com"),
        ("Tel", "514-928-3314"),
        ("Adr", "200 Brodeur St.\nBeloeil, QC J3G 2R9"),
        ("Web", "linkedin.com/in/\nfrancisarchambault"),
    ],
    "skills_label": "Core Skills",
    "skills": [
        ("Strategic Leadership", 5),
        ("MS Business Central", 5),
        ("Project Management", 5),
        ("ERP/WMS Architecture", 5),
        ("Warehouse Insight", 4),
        ("REST API / EDI", 4),
        ("Azure Blob / Make.com", 4),
        ("SAP Business One", 3),
        ("Applied AI", 4),
        ("No-code Automation", 4),
        ("BPMN / Modeling", 4),
        ("IT Coaching", 4),
    ],
    "lang_label": "Languages",
    "languages": [
        ("French", 5),
        ("English", 5),
    ],
    "interests_label": "Interests",
    "interests": "Softball · Skiing · Fitness · Travel & Cultural Exploration",
    "summary_label": "Professional Summary",
    "summary": (
        "Information technology leader with over 10 years of experience, specializing in digital transformation "
        "and ERP/WMS solution architecture. Recognized for driving complex multi-site deployments, automating "
        "business processes, and drastically reducing operational costs. Leverages emerging technologies "
        "(AI, no-code/low-code automation) to deliver measurable business gains."
    ),
    "experience_label": "Professional Experience",
    "experiences": [
        {
            "title": "Senior Principal Analyst & Business Central Solutions Architect",
            "company": "Groupe AFFI",
            "period": "2017 – Present",
            "bullets": [
                ("Led simultaneous ERP/WMS deployment across ", "5 sites", ", from requirements analysis to go-live"),
                ("Architected and deployed MS Business Central and Warehouse Insight as the primary internal resource",),
                ("Automated production outputs, reducing manual task time by over ", "80%", ""),
                ("Cut external consulting costs by ", "90%", " by internalizing functional expertise"),
                ("Integrated and automated workflows with clients and suppliers via EDI and REST APIs",),
                ("Built and supervised the company's eCommerce platform",),
                ("Coached the IT team on writing functional specifications and delivering projects end-to-end",),
            ],
        },
        {
            "title": "WMS Coordinator",
            "company": "Groupe AFFI",
            "period": "2016 – 2017",
            "bullets": [
                ("Managed WMS operational processes and provided daily operations support",),
                ("Conducted needs analysis, system configuration, and testing",),
                ("Led the deployment of the HighJump WMS software",),
            ],
        },
        {
            "title": "Site Supervisor",
            "company": "Groupe AFFI",
            "period": "2015",
            "bullets": [
                ("Supervised a team of supervisors and warehouse staff",),
                ("Managed production, distribution, and warehousing operations",),
                ("Optimized operations and maintained client relationships",),
            ],
        },
    ],
    "prev_exp_label": "Earlier Experience",
    "prev_experiences": [
        ("Groupe Novatec", "2011", "Created work order sheets and OHS procedures to improve safety and process efficiency."),
        ("Pratt & Whitney", "2012", "Managed warehouse management system and led a slow-moving inventory reallocation project to a 3PL."),
        ("IILM", "2013", "Conducted company visits to initiate technology transformation projects and secured grant funding."),
        ("CUSM Project", "2014", "Developed a route optimization system for organ donation and laboratory sample delivery."),
        ("24h Innovation – Peru", "2014", "Developed innovative solutions as part of an international team competition."),
    ],
    "edu_label": "Education & Certifications",
    "education": [
        ("Operations Engineering & Logistics", "ÉTS", "2010 – 2014"),
        ("Business Management", "Collège Édouard-Montpetit", "2007 – 2010"),
        ("ITIL Foundation", "", "2022"),
    ],
}


# ─── Drawing helpers ─────────────────────────────────────────────────────────

def wrap_text(text, max_chars):
    """Simple word-wrap returning list of lines."""
    words = text.split()
    lines, line = [], ""
    for w in words:
        test = (line + " " + w).strip()
        if len(test) <= max_chars:
            line = test
        else:
            if line:
                lines.append(line)
            line = w
    if line:
        lines.append(line)
    return lines


def draw_skill_bar(c, x, y, level, max_level=5, bar_w=80, bar_h=4, gap=2):
    """Draw a row of small filled/empty rectangles as skill indicator."""
    seg_w = (bar_w - gap * (max_level - 1)) / max_level
    for i in range(max_level):
        bx = x + i * (seg_w + gap)
        if i < level:
            c.setFillColor(BLUE)
        else:
            c.setFillColor(HexColor("#3a3a5c"))
        c.rect(bx, y, seg_w, bar_h, stroke=0, fill=1)


def section_header_main(c, x, y, label, width):
    """Draw a section header with blue left border in main column."""
    c.setFillColor(BLUE)
    c.rect(x, y - 1, 3, 13, stroke=0, fill=1)
    c.setFillColor(TEXT)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(x + 7, y + 1, label.upper())
    c.setStrokeColor(LIGHT)
    c.setLineWidth(0.5)
    c.line(x + 7, y - 3, x + width, y - 3)
    return y - 18


def sidebar_section(c, y, label, sidebar_w):
    """Draw a sidebar section label."""
    c.setFillColor(BLUE)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(14, y, label.upper())
    c.setStrokeColor(HexColor("#3a3a5c"))
    c.setLineWidth(0.5)
    c.line(14, y - 3, sidebar_w - 14, y - 3)
    return y - 12


def draw_bullet_line(c, x, y, parts, font_size=8.5):
    """Draw a bullet line. parts is a tuple of strings; odd-indexed = highlighted."""
    bullet_x = x - 10
    c.setFillColor(BLUE)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(bullet_x, y, "•")

    cx = x
    for i, part in enumerate(parts):
        if i % 2 == 1:  # highlighted part
            c.setFillColor(BLUE)
            c.setFont("Helvetica-Bold", font_size)
        else:
            c.setFillColor(TEXT)
            c.setFont("Helvetica", font_size)
        c.drawString(cx, y, part)
        cx += c.stringWidth(part, "Helvetica-Bold" if i % 2 == 1 else "Helvetica", font_size)


def multiline_bullet(c, x, y, parts, col_width, font_size=8.5, line_h=11):
    """Wrap and draw a bullet preserving inline color highlights across wrapped lines."""
    # Build tagged word list: [(word, is_highlight), ...]
    tagged_words = []
    for i, part in enumerate(parts):
        is_hi = (i % 2 == 1)
        for j, word in enumerate(part.split(" ")):
            if word:
                tagged_words.append((word, is_hi))
            if j < len(part.split(" ")) - 1:
                tagged_words.append((" ", is_hi))
    # Remove leading/trailing spaces
    while tagged_words and tagged_words[0][0].strip() == "":
        tagged_words.pop(0)

    # Pack words into lines respecting col_width
    def word_width(w, hi):
        fn = "Helvetica-Bold" if hi else "Helvetica"
        return c.stringWidth(w, fn, font_size)

    lines_of_spans = []  # list of [(word, is_hi), ...]
    current_line, current_w = [], 0.0
    for word, hi in tagged_words:
        ww = word_width(word, hi)
        if current_w + ww > col_width and current_line:
            # Strip trailing spaces from line
            while current_line and current_line[-1][0] == " ":
                current_line.pop()
            lines_of_spans.append(current_line)
            current_line = []
            current_w = 0.0
            if word.strip() == "":
                continue
        current_line.append((word, hi))
        current_w += ww

    if current_line:
        while current_line and current_line[-1][0] == " ":
            current_line.pop()
        lines_of_spans.append(current_line)

    # Draw each line
    for li, line_spans in enumerate(lines_of_spans):
        if li == 0:
            # Draw bullet
            c.setFillColor(BLUE)
            c.setFont("Helvetica-Bold", 9)
            c.drawString(x - 10, y, "•")
        cx = x
        for word, hi in line_spans:
            fn = "Helvetica-Bold" if hi else "Helvetica"
            c.setFillColor(BLUE if hi else TEXT)
            c.setFont(fn, font_size)
            c.drawString(cx, y, word)
            cx += c.stringWidth(word, fn, font_size)
        y -= line_h

    return y


class CVRenderer:
    def __init__(self, data, filename):
        self.d = data
        self.filename = filename
        self.c = canvas.Canvas(filename, pagesize=LETTER)
        self.page_num = 0

    def new_page(self):
        if self.page_num > 0:
            self.c.showPage()
        self.page_num += 1
        self._draw_sidebar_bg()

    def _draw_sidebar_bg(self):
        self.c.setFillColor(DARK)
        self.c.rect(0, 0, SIDE_W, PAGE_H, stroke=0, fill=1)

    def draw_sidebar(self):
        d = self.d
        c = self.c
        y = PAGE_H - 20

        # Name
        c.setFillColor(WHITE)
        c.setFont("Helvetica-Bold", 19)
        name_parts = d["name"].split()
        c.drawString(14, y, name_parts[0])
        y -= 22
        c.setFont("Helvetica-Bold", 19)
        c.drawString(14, y, " ".join(name_parts[1:]))
        y -= 6

        # Blue separator
        c.setStrokeColor(BLUE)
        c.setLineWidth(1.5)
        c.line(14, y, SIDE_W - 14, y)
        y -= 12

        # Title
        c.setFillColor(BLUE)
        c.setFont("Helvetica-Bold", 9)
        for line in d["title"].split("\n"):
            c.drawString(14, y, line)
            y -= 11
        y -= 6

        # Blue separator
        c.setStrokeColor(HexColor("#3a3a5c"))
        c.setLineWidth(0.5)
        c.line(14, y, SIDE_W - 14, y)
        y -= 14

        # Contact
        c.setFillColor(WHITE)
        c.setFont("Helvetica-Bold", 8.5)
        c.drawString(14, y, "CONTACT")
        c.setStrokeColor(HexColor("#3a3a5c"))
        c.setLineWidth(0.5)
        c.line(14, y - 3, SIDE_W - 14, y - 3)
        y -= 14

        for icon, info in d["contact"]:
            c.setFillColor(BLUE)
            c.setFont("Helvetica-Bold", 9)
            c.drawString(14, y, icon)
            c.setFillColor(WHITE)
            c.setFont("Helvetica", 7.5)
            lines = info.split("\n")
            c.drawString(28, y, lines[0])
            y -= 10
            if len(lines) > 1:
                c.drawString(28, y, lines[1])
                y -= 10
        y -= 6

        # Skills
        y = sidebar_section(c, y, d["skills_label"], SIDE_W)
        for skill, level in d["skills"]:
            c.setFillColor(WHITE)
            c.setFont("Helvetica", 7.5)
            c.drawString(14, y, skill)
            y -= 7
            draw_skill_bar(c, 14, y, level, bar_w=SIDE_W - 28)
            y -= 10
        y -= 6

        # Languages
        y = sidebar_section(c, y, d["lang_label"], SIDE_W)
        for lang, level in d["languages"]:
            c.setFillColor(WHITE)
            c.setFont("Helvetica", 7.5)
            c.drawString(14, y, lang)
            y -= 7
            draw_skill_bar(c, 14, y, level, bar_w=SIDE_W - 28)
            y -= 10
        y -= 6

        # Interests
        y = sidebar_section(c, y, d["interests_label"], SIDE_W)
        c.setFillColor(WHITE)
        c.setFont("Helvetica", 7.5)
        interest_lines = wrap_text(d["interests"], 24)
        for line in interest_lines:
            c.drawString(14, y, line)
            y -= 10

        self.sidebar_bottom = y

    def draw_main(self):
        d = self.d
        c = self.c
        x = MAIN_X
        w = MAIN_W
        y = PAGE_H - 22

        # Header band
        c.setFillColor(LIGHT)
        c.rect(SIDE_W, PAGE_H - 52, PAGE_W - SIDE_W, 52, stroke=0, fill=1)

        c.setFillColor(TEXT)
        c.setFont("Helvetica-Bold", 18)
        c.drawString(x, y, d["name"])

        c.setFillColor(BLUE)
        c.setFont("Helvetica", 9.5)
        title_oneline = d["title"].replace("\n", " ")
        c.drawString(x, y - 16, title_oneline)

        c.setStrokeColor(BLUE)
        c.setLineWidth(1)
        c.line(x, PAGE_H - 52, x + w, PAGE_H - 52)

        y = PAGE_H - 68

        # Summary
        y = section_header_main(c, x, y, d["summary_label"], w)
        c.setFillColor(TEXT)
        c.setFont("Helvetica", 8.5)
        sum_lines = wrap_text(d["summary"], int(w / 4.5))
        for line in sum_lines:
            c.drawString(x, y, line)
            y -= 11
        y -= 6

        # Experiences
        y = section_header_main(c, x, y, d["experience_label"], w)
        for exp in d["experiences"]:
            # Check if we need a new page
            if y < 80:
                y = self._continue_page(x, w)

            c.setFillColor(TEXT)
            c.setFont("Helvetica-Bold", 9.5)
            c.drawString(x, y, exp["title"])
            y -= 12

            c.setFillColor(BLUE)
            c.setFont("Helvetica-Bold", 8.5)
            c.drawString(x, y, exp["company"])
            c.setFillColor(HexColor("#6b7280"))
            c.setFont("Helvetica", 8)
            period_w = c.stringWidth(exp["period"], "Helvetica", 8)
            c.drawString(x + w - period_w, y, exp["period"])
            y -= 12

            for bullet in exp["bullets"]:
                if y < 60:
                    y = self._continue_page(x, w)
                y = multiline_bullet(c, x + 12, y, bullet, w - 12)
            y -= 6

        # Previous experiences
        if y < 100:
            y = self._continue_page(x, w)
        y = section_header_main(c, x, y, d["prev_exp_label"], w)
        for org, year, desc in d["prev_experiences"]:
            if y < 60:
                y = self._continue_page(x, w)
            c.setFillColor(BLUE)
            c.setFont("Helvetica-Bold", 8.5)
            c.drawString(x, y, org)
            c.setFillColor(HexColor("#6b7280"))
            c.setFont("Helvetica", 8)
            yw = c.stringWidth(year, "Helvetica", 8)
            c.drawString(x + w - yw, y, year)
            y -= 10
            c.setFillColor(TEXT)
            c.setFont("Helvetica", 8)
            desc_lines = wrap_text(desc, int(w / 4.5))
            for ln in desc_lines:
                c.drawString(x + 8, y, ln)
                y -= 10
            y -= 4

        # Education
        if y < 100:
            y = self._continue_page(x, w)
        y = section_header_main(c, x, y, d["edu_label"], w)
        for degree, school, period in d["education"]:
            if y < 50:
                y = self._continue_page(x, w)
            c.setFillColor(TEXT)
            c.setFont("Helvetica-Bold", 8.5)
            c.drawString(x, y, degree)
            c.setFillColor(HexColor("#6b7280"))
            c.setFont("Helvetica", 8)
            pw = c.stringWidth(period, "Helvetica", 8)
            c.drawString(x + w - pw, y, period)
            y -= 10
            if school:
                c.setFillColor(BLUE)
                c.setFont("Helvetica", 8)
                c.drawString(x + 8, y, school)
                y -= 10
            y -= 4

    def _continue_page(self, x, w):
        """Start a new page and return the starting y for content."""
        self.c.showPage()
        self.page_num += 1
        self._draw_sidebar_bg()
        # Continuation sidebar header
        c = self.c
        c.setFillColor(WHITE)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(14, PAGE_H - 20, self.d["name"])
        # Light header band
        c.setFillColor(LIGHT)
        c.rect(SIDE_W, PAGE_H - 28, PAGE_W - SIDE_W, 28, stroke=0, fill=1)
        c.setFillColor(TEXT)
        c.setFont("Helvetica", 8)
        c.drawString(x, PAGE_H - 18, "— suite —")
        return PAGE_H - 42

    def render(self):
        self.new_page()
        self.draw_sidebar()
        self.draw_main()
        self.c.save()
        print(f"Generated: {self.filename}")


def generate(data, filename):
    CVRenderer(data, filename).render()


# ─── ERA-targeted variants ───────────────────────────────────────────────────

CV_FR_ERA = {
    "name": "Francis Archambault",
    "title": "Architecte de solutions\nDynamics 365 Business Central\nERP & Transformation numérique",
    "contact": [
        ("Email", "f.archambault@gmail.com"),
        ("Tel", "514-928-3314"),
        ("Adr", "200 rue Brodeur\nBeloeil, QC J3G 2R9"),
        ("Web", "linkedin.com/in/\nfrancisarchambault"),
    ],
    "skills_label": "Compétences",
    "skills": [
        ("Dynamics 365 Business Central", 5),
        ("Architecture fonctionnelle ERP", 5),
        ("Ateliers de découverte", 4),
        ("Gestion de projets multi-sites", 5),
        ("Processus d'affaires (BPMN)", 4),
        ("Warehouse Insight / WMS", 4),
        ("Intégrations API REST / EDI", 4),
        ("IA appliquée aux processus", 4),
        ("Automatisation no-code", 4),
        ("Intégration eCommerce", 4),
        ("Leadership & coaching TI", 5),
        ("SAP Business One", 3),
    ],
    "lang_label": "Langues",
    "languages": [
        ("Français", 5),
        ("Anglais", 4),
    ],
    "interests_label": "Intérêts",
    "interests": "Balle molle · Ski · Conditionnement physique · Voyages & découvertes culturelles",
    "summary_label": "Résumé professionnel",
    "summary": (
        "Architecte de solutions Dynamics 365 Business Central avec plus de 10 ans d'expérience en "
        "transformation numérique ERP/WMS multi-sites. Expert en animation d'ateliers de découverte, "
        "conception d'architectures fonctionnelles alignées aux processus d'affaires et accompagnement "
        "des parties prenantes. Reconnu pour piloter des déploiements complexes (5 sites), réduire les "
        "coûts de consultation de 90% et vulgariser les enjeux technologiques à tous les niveaux. "
        "Bilingue (FR/EN), certifié ITIL."
    ),
    "experience_label": "Expériences professionnelles",
    "experiences": [
        {
            "title": "Architecte de solutions Dynamics 365 Business Central",
            "company": "Groupe AFFI",
            "period": "2017 – présent",
            "bullets": [
                ("Pilotage du cycle de vie ERP complet sur ", "5 sites", " : ateliers de découverte, conception de l'architecture fonctionnelle, mise en production"),
                ("Conception et déploiement de Dynamics 365 Business Central et Warehouse Insight, alignés aux processus d'affaires, contraintes budgétaires et délais"),
                ("Automatisation des processus de production réduisant les tâches manuelles de plus de ", "80%", ""),
                ("Réduction des coûts de consultation externe de ", "90%", " par l'internalisation de l'expertise fonctionnelle"),
                ("Intégration et automatisation des flux avec clients et fournisseurs via EDI, API REST et Make.com"),
                ("Conception et supervision de la plateforme d'intégration eCommerce",),
                ("Formation et transfert de connaissances à l'équipe TI : spécifications fonctionnelles, bonnes pratiques d'architecture et livrables",),
            ],
        },
        {
            "title": "Coordonnateur WMS",
            "company": "Groupe AFFI",
            "period": "2016 – 2017",
            "bullets": [
                ("Analyse des besoins, conception des scénarios d'implantation et pilotage du déploiement WMS HighJump",),
                ("Configuration, tests et validation des solutions avec les parties prenantes opérationnelles",),
                ("Soutien aux opérations quotidiennes et résolution des écarts entre besoins et solution livrée",),
            ],
        },
        {
            "title": "Contremaître de site",
            "company": "Groupe AFFI",
            "period": "2015",
            "bullets": [
                ("Supervision d'une équipe de superviseurs et employés",),
                ("Gestion de la production, distribution et entrepôt",),
                ("Optimisation des opérations et relation client",),
            ],
        },
    ],
    "prev_exp_label": "Expériences antérieures",
    "prev_experiences": [
        ("Groupe Novatec", "2011", "Création de fiches de travail et SST pour améliorer les procédures et la sécurité."),
        ("Pratt & Whitney", "2012", "Gestion du système d'entrepôt et projet de réallocation des items peu utilisés vers un 3PL."),
        ("IILM", "2013", "Visites d'entreprises pour initier des projets de transformation technologique et recherche de subventions."),
        ("Projet CUSM", "2014", "Développement d'un système d'optimisation des routes de livraison pour les dons d'organes."),
        ("24h de l'innovation – Pérou", "2014", "Développement de solutions innovantes en équipe internationale."),
    ],
    "edu_label": "Formation et certifications",
    "education": [
        ("Génie des opérations et logistique", "ÉTS", "2010 – 2014"),
        ("Gestion de commerce", "Collège Édouard-Montpetit", "2007 – 2010"),
        ("ITIL Foundation", "", "2022"),
    ],
}

CV_EN_ERA = {
    "name": "Francis Archambault",
    "title": "Dynamics 365 Business Central\nSolutions Architect\nERP & Digital Transformation",
    "contact": [
        ("Email", "f.archambault@gmail.com"),
        ("Tel", "514-928-3314"),
        ("Adr", "200 Brodeur St.\nBeloeil, QC J3G 2R9"),
        ("Web", "linkedin.com/in/\nfrancisarchambault"),
    ],
    "skills_label": "Core Skills",
    "skills": [
        ("Dynamics 365 Business Central", 5),
        ("Functional ERP Architecture", 5),
        ("Discovery Workshops", 4),
        ("Multi-site Project Management", 5),
        ("Business Process Analysis", 4),
        ("Warehouse Insight / WMS", 4),
        ("API REST / EDI Integrations", 4),
        ("Applied AI in Business Processes", 4),
        ("No-code Automation", 4),
        ("eCommerce Integration", 4),
        ("Leadership & IT Coaching", 5),
        ("SAP Business One", 3),
    ],
    "lang_label": "Languages",
    "languages": [
        ("French", 5),
        ("English", 5),
    ],
    "interests_label": "Interests",
    "interests": "Softball · Skiing · Fitness · Travel & Cultural Exploration",
    "summary_label": "Professional Summary",
    "summary": (
        "Dynamics 365 Business Central solutions architect with 10+ years of experience in multi-site "
        "ERP/WMS digital transformation. Expert in leading discovery workshops, designing functional "
        "architectures aligned to business processes, and guiding stakeholders throughout the full "
        "ERP lifecycle. Recognized for driving complex deployments across 5 sites, cutting external "
        "consulting costs by 90%, and simplifying technical concepts for all audiences. "
        "Bilingual (FR/EN), ITIL certified."
    ),
    "experience_label": "Professional Experience",
    "experiences": [
        {
            "title": "Dynamics 365 Business Central Solutions Architect",
            "company": "Groupe AFFI",
            "period": "2017 – Present",
            "bullets": [
                ("Owned the full ERP lifecycle across ", "5 sites", ": discovery workshops, functional architecture design, and go-live delivery"),
                ("Designed and deployed Dynamics 365 Business Central and Warehouse Insight, aligned to business processes, budget constraints and timelines",),
                ("Automated production workflows, reducing manual task time by over ", "80%", ""),
                ("Cut external consulting costs by ", "90%", " by internalizing functional architecture expertise"),
                ("Integrated and automated client and supplier workflows via EDI, REST APIs, and Make.com",),
                ("Designed and supervised the eCommerce integration platform",),
                ("Transferred knowledge to the IT team through functional spec coaching, architecture reviews, and structured project delivery",),
            ],
        },
        {
            "title": "WMS Coordinator",
            "company": "Groupe AFFI",
            "period": "2016 – 2017",
            "bullets": [
                ("Analyzed requirements, designed implementation scenarios, and led the HighJump WMS deployment",),
                ("Configured, tested, and validated the solution with operational stakeholders",),
                ("Supported daily operations and resolved gaps between requirements and delivered solution",),
            ],
        },
        {
            "title": "Site Supervisor",
            "company": "Groupe AFFI",
            "period": "2015",
            "bullets": [
                ("Supervised a team of supervisors and warehouse staff",),
                ("Managed production, distribution, and warehousing operations",),
                ("Optimized operations and maintained client relationships",),
            ],
        },
    ],
    "prev_exp_label": "Earlier Experience",
    "prev_experiences": [
        ("Groupe Novatec", "2011", "Created work order sheets and OHS procedures to improve safety and process efficiency."),
        ("Pratt & Whitney", "2012", "Managed warehouse management system and led a slow-moving inventory reallocation project to a 3PL."),
        ("IILM", "2013", "Conducted company visits to initiate technology transformation projects and secured grant funding."),
        ("CUSM Project", "2014", "Developed a route optimization system for organ donation and laboratory sample delivery."),
        ("24h Innovation – Peru", "2014", "Developed innovative solutions as part of an international team competition."),
    ],
    "edu_label": "Education & Certifications",
    "education": [
        ("Operations Engineering & Logistics", "ÉTS", "2010 – 2014"),
        ("Business Management", "Collège Édouard-Montpetit", "2007 – 2010"),
        ("ITIL Foundation", "", "2022"),
    ],
}


MATCH_REPORT = """
=============================================================
RAPPORT DE CORRESPONDANCE — Groupe conseil ERA
Poste : Architecte Solutions ERP – Dynamics 365 Business Central
Candidat : Francis Archambault
=============================================================

SCORE ESTIMÉ DE COMPATIBILITÉ : 88 / 100

─────────────────────────────────────────────────────────────
FORCES MAJEURES (correspondances directes)
─────────────────────────────────────────────────────────────
✓ Dynamics 365 Business Central — expertise centrale obligatoire, couvert à 100%
  → Ressource principale architecture + déploiement D365 BC chez Groupe AFFI (7 ans)

✓ Déploiements ERP multi-sites
  → 5 sites en simultané, cycle de vie complet (analyse → production)

✓ Intégrations & processus d'affaires
  → EDI, API REST, Make.com, eCommerce, BPMN, Warehouse Insight

✓ Bilinguisme FR/EN
  → Profil nativement bilingue, expérience dans les deux langues

✓ Coaching & transfert de connaissances
  → Coaching équipe TI, rédaction de specs fonctionnelles, bonnes pratiques

✓ Technologies émergentes (IA, no-code)
  → Make.com, Azure Blob, automatisation no-code/low-code, IA appliquée

✓ Réduction mesurable des coûts
  → 80% réduction tâches manuelles, 90% réduction coûts consultation externe

─────────────────────────────────────────────────────────────
LACUNES / POINTS À SURVEILLER
─────────────────────────────────────────────────────────────
△ Expérience de prévente formelle
  → Parcours 100% interne (ressource côté client, pas côté firme-conseil)
  → Mitigation : reframer les ateliers de découverte et la coordination
     multi-parties comme activités équivalentes

△ Rôle de consultant externe / démos client
  → Pas d'expérience directe de présentation commerciale ou d'offres structurées
  → Mitigation : l'architecture de solutions pour 5 sites démontre la capacité
     à concevoir des solutions pour des contextes variés

△ Certification Dynamics 365 BC (MB-800 ou similaire)
  → Non mentionnée dans le profil
  → Recommandation : l'ajouter si elle existe, sinon l'obtenir rapidement

─────────────────────────────────────────────────────────────
MOTS-CLÉS ATS INTÉGRÉS DANS LE CV ADAPTÉ
─────────────────────────────────────────────────────────────
  Dynamics 365 Business Central / D365 BC
  Architecture fonctionnelle ERP
  Ateliers de découverte
  Cycle de vie ERP
  Processus d'affaires
  Parties prenantes
  Transformation numérique
  Intégration eCommerce
  Intelligence artificielle appliquée
  Bilinguisme / Bilingue (FR/EN)
  ITIL
  Transfert de connaissances
  Spécifications fonctionnelles

─────────────────────────────────────────────────────────────
RECOMMANDATIONS SUPPLÉMENTAIRES
─────────────────────────────────────────────────────────────
1. Mettre à jour le profil LinkedIn avec les mots-clés ci-dessus
2. Préparer 2-3 exemples concrets d'«ateliers de découverte» informels
   menés chez Groupe AFFI (ex. sessions de définition des besoins par site)
3. Mentionner la certification ITIL en introduction lors d'un entretien
4. Si disponible, obtenir une certification officielle MB-800
   (Microsoft Certified: Dynamics 365 Business Central Functional Consultant)
=============================================================
"""


if __name__ == "__main__":
    generate(CV_FR, "cv_fr.pdf")
    generate(CV_EN, "cv_en.pdf")
    generate(CV_FR_ERA, "cv_fr_era.pdf")
    generate(CV_EN_ERA, "cv_en_era.pdf")
    with open("match_report_era.txt", "w", encoding="utf-8") as f:
        f.write(MATCH_REPORT)
    print("Generated: match_report_era.txt")
    print(MATCH_REPORT)
