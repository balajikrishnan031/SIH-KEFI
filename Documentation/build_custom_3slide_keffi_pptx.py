import os
import sys
import pptx
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def build_keffi_3slide_pptx():
    print("=== BUILDING KEFFI AI 3-SLIDE MASTER PPTX & PDF ===")

    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    blank_layout = prs.slide_layouts[6] # blank slide

    # COLOR PALETTE (PRIMARY: WHITE & BLACK WITH HIGH CONTRAST TAGS)
    COLOR_WHITE = RGBColor(255, 255, 255)
    COLOR_BLACK = RGBColor(15, 15, 15)
    COLOR_DARK_GRAY = RGBColor(35, 35, 35)
    COLOR_MID_GRAY = RGBColor(90, 90, 90)
    COLOR_LIGHT_BG = RGBColor(248, 249, 250)
    COLOR_BORDER = RGBColor(210, 215, 220)
    
    # TAG ACCENT COLORS (MONOCHROMATIC & DEEP ELEGANCE)
    COLOR_TAG_BG = RGBColor(20, 20, 20)
    COLOR_TAG_TEXT = RGBColor(255, 255, 255)
    COLOR_ACCENT_BG = RGBColor(240, 242, 245)
    COLOR_HIGHLIGHT_BORDER = RGBColor(40, 40, 40)

    FONT_TIMES = "Times New Roman"

    # Helper function to format text frame
    def add_header(slide, title_text, category_tag, subtitle_text=""):
        # Category Tag Box
        tag_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.35), Inches(2.6), Inches(0.35))
        tag_box.fill.solid()
        tag_box.fill.fore_color.rgb = COLOR_TAG_BG
        tag_box.line.color.rgb = COLOR_TAG_BG
        tf_tag = tag_box.text_frame
        tf_tag.word_wrap = True
        tf_tag.margin_left = Inches(0.08)
        tf_tag.margin_top = Inches(0.04)
        p_tag = tf_tag.paragraphs[0]
        p_tag.text = category_tag.upper()
        p_tag.font.name = FONT_TIMES
        p_tag.font.size = Pt(10.5)
        p_tag.font.bold = True
        p_tag.font.color.rgb = COLOR_TAG_TEXT
        p_tag.alignment = PP_ALIGN.CENTER

        # Title Text
        title_box = slide.shapes.add_textbox(Inches(3.5), Inches(0.30), Inches(5.3), Inches(0.75))
        tf_title = title_box.text_frame
        tf_title.word_wrap = True
        p_title = tf_title.paragraphs[0]
        p_title.text = title_text
        p_title.font.name = FONT_TIMES
        p_title.font.size = Pt(19)
        p_title.font.bold = True
        p_title.font.color.rgb = COLOR_BLACK

        if subtitle_text:
            p_sub = tf_title.add_paragraph()
            p_sub.text = subtitle_text
            p_sub.font.name = FONT_TIMES
            p_sub.font.size = Pt(10)
            p_sub.font.color.rgb = COLOR_MID_GRAY

        # PRESENTED BY BALAJI P Prominent Badge (Top Right of Every Slide)
        pres_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.9), Inches(0.3), Inches(3.633), Inches(0.75))
        pres_box.fill.solid()
        pres_box.fill.fore_color.rgb = COLOR_BLACK
        pres_box.line.color.rgb = COLOR_BLACK
        tf_pres = pres_box.text_frame
        tf_pres.word_wrap = True
        tf_pres.margin_top = Inches(0.08)
        p_pres1 = tf_pres.paragraphs[0]
        p_pres1.text = "PRESENTED BY: BALAJI P"
        p_pres1.font.name = FONT_TIMES
        p_pres1.font.size = Pt(13)
        p_pres1.font.bold = True
        p_pres1.font.color.rgb = COLOR_WHITE
        p_pres1.alignment = PP_ALIGN.CENTER

        p_pres2 = tf_pres.add_paragraph()
        p_pres2.text = "Team Leader | Dept. of CSE | UCE Anna University"
        p_pres2.font.name = FONT_TIMES
        p_pres2.font.size = Pt(9)
        p_pres2.font.color.rgb = RGBColor(220, 220, 220)
        p_pres2.alignment = PP_ALIGN.CENTER

        # Divider Line
        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.15), Inches(11.733), Inches(0.02))
        line.fill.solid()
        line.fill.fore_color.rgb = COLOR_BORDER
        line.line.color.rgb = COLOR_BORDER

    def add_footer(slide):
        footer_box = slide.shapes.add_textbox(Inches(0.8), Inches(7.05), Inches(11.733), Inches(0.4))
        tf = footer_box.text_frame
        p = tf.paragraphs[0]
        p.text = "KEFFI AI | Clinical Digital Therapeutics Platform | PRESENTED BY: BALAJI P (Team Leader, CSE, UCE Anna University BIT Campus)"
        p.font.name = FONT_TIMES
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = COLOR_MID_GRAY

    # =========================================================================
    # SLIDE 1: PROBLEM STATEMENT, GLOBAL SCALE & SCIENTIFIC RESEARCH
    # =========================================================================
    slide1 = prs.slides.add_slide(blank_layout)
    add_header(slide1, "PROBLEM STATEMENT & SCIENTIFIC RESEARCH EVIDENCE", "SLIDE 1: CLINICAL NEED", "Global Mental Health Crisis & Failure of Standard Digital Wellness Tools")

    # Left Container: Problem Statement (3 Clinical Failures)
    left_card = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.3), Inches(5.7), Inches(5.6))
    left_card.fill.solid()
    left_card.fill.fore_color.rgb = COLOR_LIGHT_BG
    left_card.line.color.rgb = COLOR_BORDER
    
    tf_left = left_card.text_frame
    tf_left.word_wrap = True
    tf_left.margin_left = Inches(0.25)
    tf_left.margin_top = Inches(0.2)
    tf_left.margin_right = Inches(0.25)

    p = tf_left.paragraphs[0]
    p.text = "[CORE PROBLEM STATEMENT]"
    p.font.name = FONT_TIMES
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = COLOR_BLACK

    p_body = tf_left.add_paragraph()
    p_body.text = "Traditional psychiatric care and generic wellness chatbots suffer from 3 interconnected clinical failures that hinder long-term patient recovery:"
    p_body.font.name = FONT_TIMES
    p_body.font.size = Pt(10.5)
    p_body.font.color.rgb = COLOR_DARK_GRAY

    problems = [
        ("1. Incomplete Symptom Remission (50-60% Failure)", "Standard psychiatric therapy is episodic (once a week). Patients suffer silently between appointments without real-time tracking, leaving symptoms unaddressed."),
        ("2. High Treatment Attrition Rate (up to 70% Dropout)", "70% of digital mental health app users abandon care within 30 days due to social stigma, high costs, lack of progress metrics, and impersonal responses."),
        ("3. Loss to Follow-Up & Severe Relapse Risk", "Clinicians cannot monitor patients 24/7. Undetected emotional distress escalates rapidly into acute psychiatric emergencies without early interventions.")
    ]

    for title, desc in problems:
        p_t = tf_left.add_paragraph()
        p_t.text = f"• {title}"
        p_t.font.name = FONT_TIMES
        p_t.font.size = Pt(11)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_BLACK
        p_t.space_before = Pt(8)

        p_d = tf_left.add_paragraph()
        p_d.text = desc
        p_d.font.name = FONT_TIMES
        p_d.font.size = Pt(10)
        p_d.font.color.rgb = COLOR_DARK_GRAY

    # Right Top Container: Global & Indian Scale
    right_top_card = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.3), Inches(5.733), Inches(2.65))
    right_top_card.fill.solid()
    right_top_card.fill.fore_color.rgb = COLOR_BLACK
    right_top_card.line.color.rgb = COLOR_BLACK
    
    tf_rt = right_top_card.text_frame
    tf_rt.word_wrap = True
    tf_rt.margin_left = Inches(0.25)
    tf_rt.margin_top = Inches(0.18)
    tf_rt.margin_right = Inches(0.25)

    p = tf_rt.paragraphs[0]
    p.text = "[GLOBAL & NATIONAL SCALE DATA]"
    p.font.name = FONT_TIMES
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = COLOR_WHITE

    stats = [
        ("WHO Global Burden", "280 Million+ people suffer from depression globally (~5% of adults). Suicide is the 4th leading cause of death in youth aged 15-29."),
        ("NMHS India Treatment Gap", "1 in 7 Indians suffer from mental health conditions with an 80-90% Treatment Gap (only 0.75 psychiatrists per 100,000 people)."),
        ("Standard Chatbot Abandonment", "73-84% of wellness app users quit after 2-3 sessions due to canned responses and zero biometric or long-term clinical tracking.")
    ]

    for title, desc in stats:
        p_s = tf_rt.add_paragraph()
        p_s.text = f"▪ {title}: {desc}"
        p_s.font.name = FONT_TIMES
        p_s.font.size = Pt(10)
        p_s.font.color.rgb = RGBColor(230, 230, 230)
        p_s.space_before = Pt(4)

    # Right Bottom Container: Scientific Research Evidence
    right_bot_card = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(4.1), Inches(5.733), Inches(2.8))
    right_bot_card.fill.solid()
    right_bot_card.fill.fore_color.rgb = COLOR_LIGHT_BG
    right_bot_card.line.color.rgb = COLOR_BORDER
    
    tf_rb = right_bot_card.text_frame
    tf_rb.word_wrap = True
    tf_rb.margin_left = Inches(0.25)
    tf_rb.margin_top = Inches(0.18)
    tf_rb.margin_right = Inches(0.25)

    p = tf_rb.paragraphs[0]
    p.text = "[SCIENTIFIC RESEARCH CITATIONS & CLINICAL EVIDENCE]"
    p.font.name = FONT_TIMES
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = COLOR_BLACK

    papers = [
        ("Hofmann et al. (2012) - CBT Meta-Analysis", "CBT delivers 50-75% symptom reduction; requires consistent daily practice between visits."),
        ("Norcross & Wampold (2011) - Therapeutic Alliance", "Empathy & validation account for 30% of overall psychiatric clinical success."),
        ("Fitzpatrick et al. (2017) - Woebot Clinical RCT", "Automated conversational CBT achieved 22% depression reduction in 2 weeks."),
        ("Hayes et al. (2006) - ACT & MBSR Grounding", "Somatic vagus nerve grounding reduces acute panic symptoms by 45-50% instantly.")
    ]

    for title, desc in papers:
        p_paper = tf_rb.add_paragraph()
        p_paper.text = f"✔ {title}: {desc}"
        p_paper.font.name = FONT_TIMES
        p_paper.font.size = Pt(9.8)
        p_paper.font.color.rgb = COLOR_DARK_GRAY
        p_paper.space_before = Pt(3)

    add_footer(slide1)


    # =========================================================================
    # SLIDE 2: END-TO-END ARCHITECTURE & LAYER-BY-LAYER TECHNICAL BREAKDOWN
    # =========================================================================
    slide2 = prs.slides.add_slide(blank_layout)
    add_header(slide2, "SYSTEM ARCHITECTURE & LAYER-BY-LAYER ENGINE", "SLIDE 2: TECHNICAL DEEP DIVE", "End-to-End Multimodal Intelligence Pipeline & Database Architecture")

    # Top Mind Map Flowchart Nodes (Visual Diagram Effect)
    node_titles = [
        "1. TOUCHPOINT",
        "2. GATEWAY",
        "3. AI ENGINE",
        "4. DATABASE",
        "5. SAFETY"
    ]
    node_sub = [
        "React + ESP32 PPG",
        "FastAPI & Slang Router",
        "BERT 96 & Groq 70B",
        "SQLite WAL & Vector",
        "n8n Escalation"
    ]

    x_start = Inches(0.8)
    node_w = Inches(2.18)
    gap = Inches(0.2)

    for i in range(5):
        nx = x_start + i * (node_w + gap)
        nshape = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, nx, Inches(1.3), node_w, Inches(0.75))
        nshape.fill.solid()
        if i == 2: # Highlight AI Engine
            nshape.fill.fore_color.rgb = COLOR_BLACK
            t_color = COLOR_WHITE
            st_color = RGBColor(220, 220, 220)
        else:
            nshape.fill.fore_color.rgb = COLOR_LIGHT_BG
            nshape.line.color.rgb = COLOR_BORDER
            t_color = COLOR_BLACK
            st_color = COLOR_MID_GRAY

        tf_n = nshape.text_frame
        tf_n.word_wrap = True
        p1 = tf_n.paragraphs[0]
        p1.text = node_titles[i]
        p1.font.name = FONT_TIMES
        p1.font.size = Pt(10.5)
        p1.font.bold = True
        p1.font.color.rgb = t_color
        p1.alignment = PP_ALIGN.CENTER

        p2 = tf_n.add_paragraph()
        p2.text = node_sub[i]
        p2.font.name = FONT_TIMES
        p2.font.size = Pt(9)
        p2.font.color.rgb = st_color
        p2.alignment = PP_ALIGN.CENTER

    # Left Box: Detailed Layer Breakdown (Layers 1 to 5)
    left_tech = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(2.2), Inches(6.8), Inches(4.7))
    left_tech.fill.solid()
    left_tech.fill.fore_color.rgb = COLOR_LIGHT_BG
    left_tech.line.color.rgb = COLOR_BORDER

    tf_lt = left_tech.text_frame
    tf_lt.word_wrap = True
    tf_lt.margin_left = Inches(0.2)
    tf_lt.margin_top = Inches(0.15)
    tf_lt.margin_right = Inches(0.2)

    p = tf_lt.paragraphs[0]
    p.text = "[DETAILED LAYER-BY-LAYER ARCHITECTURE BREAKDOWN]"
    p.font.name = FONT_TIMES
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = COLOR_BLACK

    layers_info = [
        ("Layer 1: Frontend & Touchpoint", "React + Vite Glassmorphic UI. Captures text, voice prosody (Pitch Hz, Speech Rate WPM, Pause Gaps), and ESP32 PPG Biofeedback (Heart Rate BPM, HRV ms)."),
        ("Layer 2: Gateway & Slang Router", "FastAPI async microservices (main.py) + Cosine Vector Slang Router (semantic_router.py) mapping Tanglish (e.g. 'kaduppa irukku' -> Frustration)."),
        ("Layer 3: AI & Cognitive Engine", "Fine-tuned BERT 96-Emotion Model + Groq Llama-3 70B & Ollama (Modelfile_Keffi) + SHAP/LIME Explainable AI Engine mapping tokens to DSM-5 PHQ-9 criteria."),
        ("Layer 4: Relational DB & Vector Store", "High-performance SQLite WAL Mode (clinical_db.py) + Pinecone Semantic Memory Store for long-term patient trajectory tracking."),
        ("Layer 5: Safety & Automation", "n8n workflow automation (n8n_workflows) executing emergency hotline cards, SMS therapist alerts, and acoustic sanctuary breathing sync.")
    ]

    for l_title, l_desc in layers_info:
        p_l = tf_lt.add_paragraph()
        p_l.text = f"▪ {l_title}"
        p_l.font.name = FONT_TIMES
        p_l.font.size = Pt(10.5)
        p_l.font.bold = True
        p_l.font.color.rgb = COLOR_BLACK
        p_l.space_before = Pt(4)

        p_ld = tf_lt.add_paragraph()
        p_ld.text = l_desc
        p_ld.font.name = FONT_TIMES
        p_ld.font.size = Pt(9.5)
        p_ld.font.color.rgb = COLOR_DARK_GRAY

    # Right Top Box: 7 Core Database Schemas
    right_db = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.8), Inches(2.2), Inches(4.733), Inches(2.7))
    right_db.fill.solid()
    right_db.fill.fore_color.rgb = COLOR_BLACK
    right_db.line.color.rgb = COLOR_BLACK

    tf_db = right_db.text_frame
    tf_db.word_wrap = True
    tf_db.margin_left = Inches(0.2)
    tf_db.margin_top = Inches(0.15)
    tf_db.margin_right = Inches(0.2)

    p = tf_db.paragraphs[0]
    p.text = "[7 CORE CLINICAL DATABASE TABLES]"
    p.font.name = FONT_TIMES
    p.font.size = Pt(11.5)
    p.font.bold = True
    p.font.color.rgb = COLOR_WHITE

    tables = [
        ("1. patients", "MHQ Score (0-100), Baseline Severity, Attrition Risk."),
        ("2. chat_messages", "BERT Emotion, Clinical State, MHQ Delta, SOS Flag."),
        ("3. mood_checkins", "Daily 1-5 Emoji sentiment logs & mood trend."),
        ("4. cognitive_distortion_logs", "CBT distortion types & Reframed thoughts."),
        ("5. biometric_telemetry_logs", "ESP32 Heart Rate BPM, HRV ms, Panic Flags."),
        ("6. voice_prosody_logs", "Pitch Hz, Speech Rate WPM, Pause Gaps."),
        ("7. explainable_ai_logs", "SHAP top feature JSON attributions for audit.")
    ]

    for t_name, t_desc in tables:
        pt = tf_db.add_paragraph()
        pt.text = f"• {t_name}: {t_desc}"
        pt.font.name = FONT_TIMES
        pt.font.size = Pt(9)
        pt.font.color.rgb = RGBColor(230, 230, 230)
        pt.space_before = Pt(2)

    # Right Bottom Box: Embedded Real UI Screenshot Image
    img_arch_path = r'e:\Keffi Ai\Documentation\extracted_report_images\shot_3_landing_tech_architecture.png'
    if not os.path.exists(img_arch_path):
        img_arch_path = r'e:\Keffi Ai\Documentation\extracted_report_images\user_screenshot_5_tech_stack.png'
    
    if os.path.exists(img_arch_path):
        slide2.shapes.add_picture(img_arch_path, Inches(7.8), Inches(5.0), Inches(4.733), Inches(1.9))

    add_footer(slide2)


    # =========================================================================
    # SLIDE 3: CLINICAL SOLUTION, 10 METHODOLOGIES & IMPLEMENTATION STACK
    # =========================================================================
    slide3 = prs.slides.add_slide(blank_layout)
    add_header(slide3, "CLINICAL SOLUTION & 10 PSYCHOTHERAPEUTIC METHODOLOGIES", "SLIDE 3: METHODOLOGY & STACK", "10 Evidence-Based Therapeutic Protocols & Complete System Technology Stack")

    # Top Card: The Comprehensive Solution Offered by Keffi AI
    top_sol = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.3), Inches(11.733), Inches(1.15))
    top_sol.fill.solid()
    top_sol.fill.fore_color.rgb = COLOR_BLACK
    top_sol.line.color.rgb = COLOR_BLACK

    tf_ts = top_sol.text_frame
    tf_ts.word_wrap = True
    tf_ts.margin_left = Inches(0.2)
    tf_ts.margin_top = Inches(0.12)

    p = tf_ts.paragraphs[0]
    p.text = "[THE KEFFI AI CLINICAL SOLUTION]"
    p.font.name = FONT_TIMES
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = COLOR_WHITE

    sol_points = "1. 24/7 Bio-Behavioral Companion (bridges episodic gaps) | 2. Biofeedback-Synced Panic Reduction (ESP32 PPG + 4-7-8 Breathing + Sanctuary Audio) | 3. Predictive Attrition Prevention (MHQ trajectory scoring) | 4. Zero-Stigma Privacy-First Architecture."
    p_sp = tf_ts.add_paragraph()
    p_sp.text = sol_points
    p_sp.font.name = FONT_TIMES
    p_sp.font.size = Pt(10)
    p_sp.font.color.rgb = RGBColor(230, 230, 230)
    p_sp.space_before = Pt(3)

    # Middle Container: The 10 Psychotherapeutic Methodologies Table Matrix
    mid_matrix = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(2.55), Inches(7.5), Inches(4.35))
    mid_matrix.fill.solid()
    mid_matrix.fill.fore_color.rgb = COLOR_LIGHT_BG
    mid_matrix.line.color.rgb = COLOR_BORDER

    tf_mm = mid_matrix.text_frame
    tf_mm.word_wrap = True
    tf_mm.margin_left = Inches(0.2)
    tf_mm.margin_top = Inches(0.15)
    tf_mm.margin_right = Inches(0.2)

    p = tf_mm.paragraphs[0]
    p.text = "[THE 10 PSYCHOTHERAPEUTIC METHODOLOGIES MATRIX]"
    p.font.name = FONT_TIMES
    p.font.size = Pt(11.5)
    p.font.bold = True
    p.font.color.rgb = COLOR_BLACK

    methods = [
        ("1. CBT (Cognitive Behavioral Therapy)", "Identifies 10 cognitive distortions (catastrophizing) and reframes thoughts."),
        ("2. DBT (Dialectical Behavior Therapy)", "Applies TIPP crisis skills (Temperature, Paced breathing) for explosive rage/urges."),
        ("3. ACT (Acceptance & Commitment)", "Cognitive defusion: treats intrusive thoughts as passing clouds in the sky."),
        ("4. Somatic Grounding & MBSR", "Vagus nerve activation via 4-7-8 rhythm breathing & 5-4-3-2-1 sensory grounding."),
        ("5. Rogerian Validation", "Provides non-judgmental active listening, warm validation & emotional mirroring."),
        ("6. Double-Standard Technique", "Challenges self-criticism: asks what user would say to a close friend in same state."),
        ("7. Micro-Behavioral Activation", "Breaks depressive bed-locking through 30-second physical tasks (e.g. sip of water)."),
        ("8. Behavioral Experiment & Exposure", "De-catastrophizes social anxiety by testing feared outcomes in safe micro-trials."),
        ("9. Compassion-Focused Therapy (CFT)", "Activates soothing system via self-soothing touch (hand over heart) & warm self-talk."),
        ("10. Problem-Solving Therapy (PST)", "Deconstructs massive workload overwhelm into 3 bite-sized prioritized steps.")
    ]

    for m_title, m_desc in methods:
        pm = tf_mm.add_paragraph()
        pm.text = f"✔ {m_title}: {m_desc}"
        pm.font.name = FONT_TIMES
        pm.font.size = Pt(9.2)
        pm.font.color.rgb = COLOR_DARK_GRAY
        pm.space_before = Pt(2)

    # Right Container: Technology Stack & Live Screenshot
    right_stack = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.5), Inches(2.55), Inches(4.033), Inches(2.2))
    right_stack.fill.solid()
    right_stack.fill.fore_color.rgb = COLOR_LIGHT_BG
    right_stack.line.color.rgb = COLOR_BORDER

    tf_rs = right_stack.text_frame
    tf_rs.word_wrap = True
    tf_rs.margin_left = Inches(0.18)
    tf_rs.margin_top = Inches(0.12)
    tf_rs.margin_right = Inches(0.18)

    p = tf_rs.paragraphs[0]
    p.text = "[FULL SYSTEM TECH STACK]"
    p.font.name = FONT_TIMES
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = COLOR_BLACK

    stacks = [
        ("Frontend Canvas", "React, Vite, Glassmorphic CSS, WebAudio API."),
        ("Backend Services", "Python 3.11, FastAPI, SQLAlchemy ORM."),
        ("AI / ML Suite", "BERT 96-Emotion, Groq Llama-3 70B, SHAP XAI."),
        ("Database / Storage", "SQLite WAL Mode, Pinecone Vector DB."),
        ("Hardware / Auto", "ESP32 PPG Sensor, n8n Automation Engine.")
    ]

    for s_name, s_val in stacks:
        ps = tf_rs.add_paragraph()
        ps.text = f"▪ {s_name}: {s_val}"
        ps.font.name = FONT_TIMES
        ps.font.size = Pt(8.8)
        ps.font.color.rgb = COLOR_DARK_GRAY
        ps.space_before = Pt(2)

    # Right Bottom: Live Sanctuary Chat UI Screenshot
    img_chat_path = r'e:\Keffi Ai\Documentation\extracted_report_images\shot_5_sanctuary_active_chat.png'
    if not os.path.exists(img_chat_path):
        img_chat_path = r'e:\Keffi Ai\Documentation\extracted_report_images\live_sanctuary_chat.png'

    if os.path.exists(img_chat_path):
        slide3.shapes.add_picture(img_chat_path, Inches(8.5), Inches(4.85), Inches(4.033), Inches(2.05))

    add_footer(slide3)

    # Save PPTX Output Files
    output_pptx_1 = r'e:\Keffi Ai\KEFFI_AI_3PAGE_MASTER_DECK.pptx'
    output_pptx_2 = r'e:\Keffi Ai\Presentations_and_Extracted_Media\KEFFI_AI_3PAGE_MASTER_DECK.pptx'
    output_pptx_3 = r'e:\Keffi Ai\Final_Submission_Pack\KEFFI_AI_3PAGE_MASTER_DECK.pptx'

    prs.save(output_pptx_1)
    prs.save(output_pptx_2)
    prs.save(output_pptx_3)

    print(f"SUCCESSFULLY CREATED PPTX: {output_pptx_1}")

    # Convert PPTX to PDF using win32com PowerPoint COM
    try:
        import win32com.client
        pythoncom = None
        
        output_pdf_1 = r'e:\Keffi Ai\KEFFI_AI_3PAGE_MASTER_DECK.pdf'
        output_pdf_2 = r'e:\Keffi Ai\Presentations_and_Extracted_Media\KEFFI_AI_3PAGE_MASTER_DECK.pdf'
        output_pdf_3 = r'e:\Keffi Ai\Final_Submission_Pack\KEFFI_AI_3PAGE_MASTER_DECK.pdf'

        powerpoint = win32com.client.Dispatch("PowerPoint.Application")
        powerpoint.Visible = True
        
        abs_pptx = os.path.abspath(output_pptx_1)
        abs_pdf = os.path.abspath(output_pdf_1)

        deck = powerpoint.Presentations.Open(abs_pptx)
        deck.SaveAs(abs_pdf, 32) # 32 = ppSaveAsPDF
        deck.Close()
        powerpoint.Quit()

        # Copy to other directories
        import shutil
        shutil.copy(output_pdf_1, output_pdf_2)
        shutil.copy(output_pdf_1, output_pdf_3)
        print(f"SUCCESSFULLY CONVERTED PPTX TO PDF: {output_pdf_1}")
    except Exception as e:
        print(f"PDF Conversion Warning: {e}")

if __name__ == "__main__":
    build_keffi_3slide_pptx()
