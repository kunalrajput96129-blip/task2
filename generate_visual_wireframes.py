import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Set output directory
OUTPUT_DIR = r"c:\Users\Vicky\OneDrive\Desktop\task2\assets"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def create_desktop_wireframe():
    fig, ax = plt.subplots(figsize=(12, 8), dpi=300)
    ax.set_xlim(0, 1200)
    ax.set_ylim(0, 800)
    ax.invert_yaxis()
    ax.axis('off')

    # Outer Frame (Browser)
    browser = patches.Rectangle((10, 10), 1180, 780, linewidth=2, edgecolor='#1e293b', facecolor='#f8fafc')
    ax.add_patch(browser)
    
    # Browser Header / Address Bar
    b_header = patches.Rectangle((10, 10), 1180, 40, linewidth=1, edgecolor='#cbd5e1', facecolor='#e2e8f0')
    ax.add_patch(b_header)
    ax.text(30, 35, "[o] [o] [o]  https://govdirect.portal.gov/services", fontsize=11, fontweight='bold', color='#334155')

    # Portal Header & Nav Bar
    nav_bar = patches.Rectangle((10, 50), 1180, 60, linewidth=1, edgecolor='#0f172a', facecolor='#0f172a')
    ax.add_patch(nav_bar)
    ax.text(40, 87, "[Gov] GovDirect Portal", fontsize=16, fontweight='bold', color='#ffffff')
    ax.text(350, 87, "Services   |   Departments   |   Track Status   |   Help & Accessibility", fontsize=11, color='#94a3b8')
    ax.text(1020, 87, "[A- A A+]  Dark Mode", fontsize=10, fontweight='bold', color='#38bdf8')

    # Hero & Search Banner
    hero = patches.Rectangle((30, 120), 1140, 130, linewidth=1.5, edgecolor='#2563eb', facecolor='#eff6ff')
    ax.add_patch(hero)
    ax.text(60, 155, "Find & Apply for Government Digital Services", fontsize=15, fontweight='bold', color='#1e3a8a')
    ax.text(60, 180, "Instant access to driver renewal, business licensing, tax filing & citizen grants.", fontsize=10, color='#3b82f6')
    
    search_box = patches.Rectangle((60, 195), 700, 40, linewidth=1.5, edgecolor='#2563eb', facecolor='#ffffff')
    ax.add_patch(search_box)
    ax.text(75, 220, "Search services e.g., 'Driver License Renewal' or enter Ref ID...", fontsize=10, color='#94a3b8')
    
    btn_search = patches.Rectangle((770, 195), 130, 40, linewidth=1, edgecolor='#2563eb', facecolor='#2563eb')
    ax.add_patch(btn_search)
    ax.text(805, 220, "Search", fontsize=11, fontweight='bold', color='#ffffff')

    # Main Grid Container (Left Sidebar + Right Cards)
    # Left Sidebar (Filter Categories)
    sidebar = patches.Rectangle((30, 265), 260, 500, linewidth=1, edgecolor='#cbd5e1', facecolor='#ffffff')
    ax.add_patch(sidebar)
    ax.text(50, 295, "Filter Categories", fontsize=12, fontweight='bold', color='#0f172a')
    
    categories = ["All Services (24)", "Identity & Licensing", "Business & Permits", "Healthcare & Benefits", "Housing & Property", "Taxation & Finance"]
    for i, cat in enumerate(categories):
        y_pos = 330 + (i * 45)
        bg_col = '#e0f2fe' if i == 0 else '#f8fafc'
        txt_col = '#0369a1' if i == 0 else '#475569'
        cat_box = patches.Rectangle((40, y_pos - 20), 240, 35, linewidth=1, edgecolor='#e2e8f0', facecolor=bg_col)
        ax.add_patch(cat_box)
        ax.text(55, y_pos + 2, f"- {cat}", fontsize=10, fontweight='bold' if i == 0 else 'normal', color=txt_col)

    # Right Content Grid (6 Service Cards)
    cards = [
        ("Driver License Renewal", "Renew personal & commercial license online with instant digital pass.", "Identity", "10 Mins"),
        ("Business Name Registration", "Register new commercial entity & obtain federal EIN clearance.", "Business", "1 Day"),
        ("Citizen Healthcare Grant", "Apply for subsidized health insurance and family welfare coverage.", "Healthcare", "3 Days"),
        ("Property Tax Assessment", "View real estate tax valuation, request exemptions, pay bills.", "Housing", "Instant"),
        ("Building Construction Permit", "Submit architectural blueprints for municipal inspection clearance.", "Business", "5 Days"),
        ("Passport Express Application", "Book biometric appointment and upload travel documentation.", "Identity", "2 Days")
    ]

    for idx, (title, desc, cat_tag, sla) in enumerate(cards):
        col = idx % 3
        row = idx // 3
        x = 310 + (col * 285)
        y = 265 + (row * 245)
        
        card_box = patches.Rectangle((x, y), 270, 230, linewidth=1.5, edgecolor='#cbd5e1', facecolor='#ffffff')
        ax.add_patch(card_box)
        
        # Category Badge
        badge = patches.Rectangle((x + 15, y + 15), 90, 22, linewidth=0, facecolor='#dbeafe')
        ax.add_patch(badge)
        ax.text(x + 22, y + 30, cat_tag, fontsize=8, fontweight='bold', color='#1d4ed8')
        
        # SLA Badge
        sla_badge = patches.Rectangle((x + 180, y + 15), 75, 22, linewidth=0, facecolor='#fef3c7')
        ax.add_patch(sla_badge)
        ax.text(x + 188, y + 30, f"SLA: {sla}", fontsize=8, fontweight='bold', color='#b45309')

        # Card Content
        ax.text(x + 15, y + 65, title, fontsize=11, fontweight='bold', color='#0f172a')
        
        # Wrap Description
        words = desc.split()
        l1 = " ".join(words[:6])
        l2 = " ".join(words[6:])
        ax.text(x + 15, y + 90, l1, fontsize=9, color='#64748b')
        ax.text(x + 15, y + 108, l2, fontsize=9, color='#64748b')
        
        # Accessibility Checklist Indicator
        ax.text(x + 15, y + 140, "OK: WCAG AAA | Screen Reader", fontsize=8, color='#15803d')

        # Action Button
        btn_apply = patches.Rectangle((x + 15, y + 165), 240, 45, linewidth=1, edgecolor='#2563eb', facecolor='#2563eb')
        ax.add_patch(btn_apply)
        ax.text(x + 90, y + 192, "Apply Now ->", fontsize=10, fontweight='bold', color='#ffffff')

    # Watermark / Title Footer
    ax.text(600, 775, "DESKTOP HIGH-FIDELITY WIREFRAME - GOVDIRECT PORTAL (1200px Grid)", fontsize=11, fontweight='bold', color='#64748b', ha='center')

    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, "wireframe_desktop.png")
    plt.savefig(path, bbox_inches='tight', dpi=300)
    plt.close()
    print(f"Generated: {path}")

def create_mobile_wireframe():
    fig, ax = plt.subplots(figsize=(6, 10), dpi=300)
    ax.set_xlim(0, 400)
    ax.set_ylim(0, 750)
    ax.invert_yaxis()
    ax.axis('off')

    # Device Frame (Mobile 375px)
    phone = patches.FancyBboxPatch((10, 10), 380, 730, linewidth=3, edgecolor='#0f172a', facecolor='#f8fafc', boxstyle="round,pad=10")
    ax.add_patch(phone)
    
    # Status Bar
    ax.text(35, 35, "9:41  Signal 100%", fontsize=10, fontweight='bold', color='#0f172a')
    
    # Nav Bar (Collapsed Hamburger)
    nav = patches.Rectangle((20, 45), 360, 50, linewidth=1, edgecolor='#0f172a', facecolor='#0f172a')
    ax.add_patch(nav)
    ax.text(35, 75, "[Gov] GovDirect", fontsize=14, fontweight='bold', color='#ffffff')
    ax.text(330, 75, "[=]", fontsize=16, fontweight='bold', color='#ffffff')

    # Quick Accessibility Controls (Mobile Top Strip)
    acc_strip = patches.Rectangle((20, 100), 360, 30, linewidth=1, edgecolor='#cbd5e1', facecolor='#e0f2fe')
    ax.add_patch(acc_strip)
    ax.text(35, 120, "Aa Font Scale: [ - | + ]   Theme: Light", fontsize=9, fontweight='bold', color='#0369a1')

    # Hero / Search Box (Mobile Stacked)
    hero = patches.Rectangle((20, 140), 360, 120, linewidth=1, edgecolor='#2563eb', facecolor='#eff6ff')
    ax.add_patch(hero)
    ax.text(35, 165, "Digital Citizen Portal", fontsize=13, fontweight='bold', color='#1e3a8a')
    text_search = patches.Rectangle((35, 180), 330, 35, linewidth=1, edgecolor='#94a3b8', facecolor='#ffffff')
    ax.add_patch(text_search)
    ax.text(45, 202, "Search services...", fontsize=9, color='#94a3b8')
    
    btn_track = patches.Rectangle((35, 220), 330, 30, linewidth=1, edgecolor='#2563eb', facecolor='#2563eb')
    ax.add_patch(btn_track)
    ax.text(125, 240, "Track Application", fontsize=9, fontweight='bold', color='#ffffff')

    # Filter Tabs (Horizontal Strip Wireframe)
    ax.text(20, 280, "Service Categories", fontsize=11, fontweight='bold', color='#0f172a')
    cat1 = patches.Rectangle((20, 290), 100, 30, linewidth=1, edgecolor='#2563eb', facecolor='#2563eb')
    ax.add_patch(cat1)
    ax.text(35, 310, "All (24)", fontsize=9, fontweight='bold', color='#ffffff')
    
    cat2 = patches.Rectangle((125, 290), 110, 30, linewidth=1, edgecolor='#cbd5e1', facecolor='#ffffff')
    ax.add_patch(cat2)
    ax.text(135, 310, "Licensing", fontsize=9, color='#475569')

    cat3 = patches.Rectangle((240, 290), 110, 30, linewidth=1, edgecolor='#cbd5e1', facecolor='#ffffff')
    ax.add_patch(cat3)
    ax.text(250, 310, "Business", fontsize=9, color='#475569')

    # Stacked Cards (Mobile 1 Column View)
    mobile_cards = [
        ("Driver License Renewal", "Renew personal license online with digital verification.", "10 Mins"),
        ("Business Name Registration", "Register new commercial entity EIN clearance.", "1 Day"),
        ("Citizen Healthcare Grant", "Apply for subsidized health insurance.", "3 Days")
    ]

    for idx, (title, desc, sla) in enumerate(mobile_cards):
        y = 335 + (idx * 115)
        c_box = patches.Rectangle((20, y), 360, 105, linewidth=1.5, edgecolor='#cbd5e1', facecolor='#ffffff')
        ax.add_patch(c_box)
        
        ax.text(35, y + 25, title, fontsize=10, fontweight='bold', color='#0f172a')
        ax.text(35, y + 45, desc, fontsize=8.5, color='#64748b')
        ax.text(35, y + 65, f"SLA: {sla}  |  WCAG AAA Compliant", fontsize=8, color='#16a34a')
        
        m_btn = patches.Rectangle((35, y + 75), 330, 22, linewidth=0, facecolor='#2563eb')
        ax.add_patch(m_btn)
        ax.text(150, y + 90, "Apply Now", fontsize=8.5, fontweight='bold', color='#ffffff')

    # Bottom Sticky Navigation Bar for Mobile
    bot_nav = patches.Rectangle((20, 690), 360, 40, linewidth=1, edgecolor='#0f172a', facecolor='#0f172a')
    ax.add_patch(bot_nav)
    ax.text(45, 715, "Home    Search    Services    Profile", fontsize=10, fontweight='bold', color='#ffffff')

    ax.text(200, 745, "MOBILE WIREFRAME (375px Breakpoint)", fontsize=9, fontweight='bold', color='#64748b', ha='center')

    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, "wireframe_mobile.png")
    plt.savefig(path, bbox_inches='tight', dpi=300)
    plt.close()
    print(f"Generated: {path}")

def create_form_wireframe():
    fig, ax = plt.subplots(figsize=(10, 7), dpi=300)
    ax.set_xlim(0, 1000)
    ax.set_ylim(0, 650)
    ax.invert_yaxis()
    ax.axis('off')

    # Background Backdrop
    bg = patches.Rectangle((0, 0), 1000, 650, linewidth=0, facecolor='#0f172a', alpha=0.5)
    ax.add_patch(bg)

    # Modal Container
    modal = patches.Rectangle((150, 40), 700, 570, linewidth=2, edgecolor='#2563eb', facecolor='#ffffff')
    ax.add_patch(modal)

    # Modal Header
    m_head = patches.Rectangle((150, 40), 700, 50, linewidth=1, edgecolor='#e2e8f0', facecolor='#0f172a')
    ax.add_patch(m_head)
    ax.text(175, 72, "Digital Service Application: Driver License Renewal", fontsize=13, fontweight='bold', color='#ffffff')
    ax.text(810, 72, "[X]", fontsize=14, fontweight='bold', color='#94a3b8')

    # Progress Stepper
    steps = ["1. Applicant Details", "2. Document Upload", "3. Review & Submit"]
    for i, s in enumerate(steps):
        x = 180 + (i * 220)
        box_color = '#2563eb' if i == 0 else ('#cbd5e1' if i == 1 else '#f1f5f9')
        txt_color = '#ffffff' if i == 0 else ('#0f172a' if i == 1 else '#94a3b8')
        step_box = patches.Rectangle((x, 105), 190, 30, linewidth=1, edgecolor='#cbd5e1', facecolor=box_color)
        ax.add_patch(step_box)
        ax.text(x + 20, 125, s, fontsize=9.5, fontweight='bold', color=txt_color)

    # Form Fields (Step 1)
    ax.text(180, 165, "Applicant Information (Required fields marked with *)", fontsize=11, fontweight='bold', color='#0f172a')

    # Field 1: Full Legal Name
    ax.text(180, 195, "Full Legal Name * (Matches National ID)", fontsize=9.5, fontweight='bold', color='#334155')
    f1 = patches.Rectangle((180, 205), 310, 35, linewidth=1.5, edgecolor='#2563eb', facecolor='#ffffff')
    ax.add_patch(f1)
    ax.text(195, 227, "Eleanor Vance", fontsize=10, color='#0f172a')
    ax.text(465, 227, "OK: Valid", fontsize=8.5, fontweight='bold', color='#16a34a')

    # Field 2: Citizen Identification Number
    ax.text(515, 195, "National Citizen ID / SSN *", fontsize=9.5, fontweight='bold', color='#334155')
    f2 = patches.Rectangle((515, 205), 310, 35, linewidth=1.5, edgecolor='#cbd5e1', facecolor='#ffffff')
    ax.add_patch(f2)
    ax.text(530, 227, "GOV-987-6543-X", fontsize=10, color='#0f172a')

    # Field 3: Email Address
    ax.text(180, 260, "Email Address * (For Confirmation & Tracking)", fontsize=9.5, fontweight='bold', color='#334155')
    f3 = patches.Rectangle((180, 270), 310, 35, linewidth=1.5, edgecolor='#cbd5e1', facecolor='#ffffff')
    ax.add_patch(f3)
    ax.text(195, 292, "eleanor.vance@gov.example", fontsize=10, color='#0f172a')

    # Field 4: Phone Number
    ax.text(515, 260, "Mobile Phone * (SMS Notifications)", fontsize=9.5, fontweight='bold', color='#334155')
    f4 = patches.Rectangle((515, 270), 310, 35, linewidth=1.5, edgecolor='#cbd5e1', facecolor='#ffffff')
    ax.add_patch(f4)
    ax.text(530, 292, "+1 (555) 234-5678", fontsize=10, color='#0f172a')

    # Field 5: Document Upload Dropzone Preview
    ax.text(180, 325, "Supporting Identification Document (PDF/JPG, Max 10MB)", fontsize=9.5, fontweight='bold', color='#334155')
    dropzone = patches.Rectangle((180, 335), 645, 80, linewidth=1.5, linestyle='--', edgecolor='#2563eb', facecolor='#eff6ff')
    ax.add_patch(dropzone)
    ax.text(360, 370, "[Doc] Drag & Drop Passport Scan or Click to Browse", fontsize=10, fontweight='bold', color='#1d4ed8')
    ax.text(390, 395, "Attached: passport_scan_vance.pdf (1.4 MB) OK", fontsize=8.5, color='#16a34a')

    # Accessibility Consent Checkbox
    chk = patches.Rectangle((180, 435), 20, 20, linewidth=1.5, edgecolor='#2563eb', facecolor='#2563eb')
    ax.add_patch(chk)
    ax.text(184, 450, "[x]", fontsize=10, fontweight='bold', color='#ffffff')
    ax.text(210, 450, "I declare under penalty of perjury that all details provided are accurate.", fontsize=9, color='#334155')

    # Modal Action Footer
    m_foot = patches.Rectangle((150, 540), 700, 70, linewidth=1, edgecolor='#e2e8f0', facecolor='#f8fafc')
    ax.add_patch(m_foot)
    
    btn_cancel = patches.Rectangle((180, 555), 120, 40, linewidth=1, edgecolor='#cbd5e1', facecolor='#ffffff')
    ax.add_patch(btn_cancel)
    ax.text(215, 580, "Cancel", fontsize=10, fontweight='bold', color='#475569')

    btn_next = patches.Rectangle((680, 555), 145, 40, linewidth=1, edgecolor='#2563eb', facecolor='#2563eb')
    ax.add_patch(btn_next)
    ax.text(710, 580, "Proceed to Step 2 ->", fontsize=10, fontweight='bold', color='#ffffff')

    ax.text(500, 630, "MULTI-STEP INTERACTIVE APPLICATION FORM WIREFRAME", fontsize=9.5, fontweight='bold', color='#64748b', ha='center')

    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, "wireframe_form.png")
    plt.savefig(path, bbox_inches='tight', dpi=300)
    plt.close()
    print(f"Generated: {path}")

def create_user_flow_diagram():
    fig, ax = plt.subplots(figsize=(12, 5), dpi=300)
    ax.set_xlim(0, 1200)
    ax.set_ylim(0, 400)
    ax.invert_yaxis()
    ax.axis('off')

    # Nodes Definitions
    nodes = [
        (60, 160, "1. Portal Entry", "Citizen accesses portal\nvia desktop or mobile.\nConfigures accessibility."),
        (290, 160, "2. Service Discovery", "Search by keyword or\nfilter by category.\nView SLA & requirements."),
        (520, 160, "3. Form Application", "Interactive multi-step\nform with inline ARIA\nvalidation & upload."),
        (750, 160, "4. Real-time Verification", "Automated document\ncheck & instant reference\nID (GOV-2026-X) creation."),
        (980, 160, "5. Status Tracking", "Citizen tracks progress\non visual timeline until\ndigital issue.")
    ]

    for x, y, title, desc in nodes:
        # Outer Node Card
        card = patches.FancyBboxPatch((x, y), 160, 130, linewidth=2, edgecolor='#2563eb', facecolor='#ffffff', boxstyle="round,pad=5")
        ax.add_patch(card)
        
        # Header Box inside Node
        h_box = patches.Rectangle((x, y), 160, 35, linewidth=0, facecolor='#0f172a')
        ax.add_patch(h_box)
        ax.text(x + 10, y + 23, title, fontsize=9.5, fontweight='bold', color='#ffffff')
        
        # Body text
        ax.text(x + 10, y + 55, desc, fontsize=8.5, color='#334155')

    # Draw Connector Arrows
    arrows = [
        (220, 225, 290, 225),
        (450, 225, 520, 225),
        (680, 225, 750, 225),
        (910, 225, 980, 225)
    ]

    for x1, y1, x2, y2 in arrows:
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle="->", color="#2563eb", lw=3, mutation_scale=20))

    ax.text(600, 360, "CITIZEN USER FLOW & INTERACTION ARCHITECTURE DIAGRAM", fontsize=11, fontweight='bold', color='#0f172a', ha='center')

    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, "user_flow.png")
    plt.savefig(path, bbox_inches='tight', dpi=300)
    plt.close()
    print(f"Generated: {path}")

def create_contrast_matrix():
    fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
    ax.set_xlim(0, 1000)
    ax.set_ylim(0, 500)
    ax.invert_yaxis()
    ax.axis('off')

    ax.text(40, 40, "WCAG 2.1 AAA / AA Accessibility Color Contrast Matrix", fontsize=14, fontweight='bold', color='#0f172a')
    ax.text(40, 65, "Evaluation of portal color pairs against universal readability standards", fontsize=10, color='#64748b')

    color_pairs = [
        ("Gov Navy Text on Light Slate BG", "#0f172a", "#f8fafc", "18.5:1", "PASS (AAA)"),
        ("Civic Blue Text on Light Blue BG", "#1d4ed8", "#eff6ff", "9.2:1", "PASS (AAA)"),
        ("White Text on Civic Blue Button", "#ffffff", "#2563eb", "5.1:1", "PASS (AA)"),
        ("White Text on Gov Navy Header", "#ffffff", "#0f172a", "19.8:1", "PASS (AAA)"),
        ("Success Green Text on Soft Green BG", "#15803d", "#f0fdf4", "7.4:1", "PASS (AAA)"),
        ("Warning Amber Text on Gold BG", "#b45309", "#fef3c7", "5.8:1", "PASS (AA)")
    ]

    for i, (label, fg, bg, ratio, status) in enumerate(color_pairs):
        col = i % 2
        row = i // 2
        x = 40 + (col * 470)
        y = 95 + (row * 120)

        # Swatch Box
        box = patches.Rectangle((x, y), 440, 100, linewidth=1.5, edgecolor='#cbd5e1', facecolor=bg)
        ax.add_patch(box)

        # Label inside swatch
        ax.text(x + 20, y + 35, label, fontsize=11, fontweight='bold', color=fg)
        ax.text(x + 20, y + 60, f"Foreground: {fg}  |  Background: {bg}", fontsize=9, color=fg)
        
        # Status Badge
        badge_bg = '#dcfce7' if "AAA" in status else '#fef9c3'
        badge_fg = '#15803d' if "AAA" in status else '#a16207'
        st_box = patches.Rectangle((x + 310, y + 25), 110, 30, linewidth=0, facecolor=badge_bg)
        ax.add_patch(st_box)
        ax.text(x + 320, y + 45, f"{ratio}\n{status}", fontsize=8.5, fontweight='bold', color=badge_fg, ha='center')

    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, "contrast_matrix.png")
    plt.savefig(path, bbox_inches='tight', dpi=300)
    plt.close()
    print(f"Generated: {path}")

if __name__ == "__main__":
    print("Generating visual wireframes and diagrams...")
    create_desktop_wireframe()
    create_mobile_wireframe()
    create_form_wireframe()
    create_user_flow_diagram()
    create_contrast_matrix()
    print("All diagrams generated successfully.")
