# SIH 2026 Official Portal Submission Text Pack (Problem Statement ID: SIH26094)

---

## 👥 OFFICIAL TEAM DETAILS
- **Team Name**: DEKO
- **Team ID**: 141444
- **Team Leader Name**: BALAJI P
- **College Name**: University College of Engineering, Panruti

### Team Members Roster:
| Role | Member Name | Email | Phone | Gender |
| :--- | :--- | :--- | :--- | :--- |
| **LEADER** | BALAJI P | balajikrishnan031@gmail.com | 9342636595 | Male |
| **TEAM_MEMBER** | NAVANEETHAM V | er.navaneetham@gmail.com | 9487461627 | Female |
| **TEAM_MEMBER** | MALINI V | malini28102005v@gmail.com | 8807984385 | Female |
| **TEAM_MEMBER** | DHAVAN R G | rgdhavan50@gmail.com | 9342529181 | Male |
| **TEAM_MEMBER** | DEEBIKA S | deebikasivaprakasam@gmail.com | 6380433293 | Female |
| **TEAM_MEMBER** | DHARA R | dhararamesh2416@gmail.com | 9043644162 | Female |

---

## 📌 FIELD 1: Idea Title (Max 100 Characters)
**Copy & Paste into Portal:**
```text
KEFI AI: Post-Complaint Mental Health Monitoring & Distress Prediction System for Atrocity Victims
```
*(Exact Length: 98 Characters — strictly complies with the <= 100 characters limit)*

---

## 📌 FIELD 2: Technology Bucket (Dropdown Selection)
**Select from Dropdown:**
```text
MedTech / BioTech / HealthTech
```
*(Category: Software | Theme: HealthTech / Social Inclusion / MedTech)*

---

## 📌 FIELD 3: Abstract / Summary (Max 10,000 Characters)
**Copy & Paste into Portal:**
```text
PROJECT OVERVIEW & CONTEXT (TEAM DEKO - TEAM ID: 141444)
We built KEFI AI to solve a critical institutional blind spot in India's criminal justice system. Under the Scheduled Castes and Scheduled Tribes (Prevention of Atrocities) Act, 1989, when an individual registers a First Information Report (FIR), the state machinery steps in with legal procedures, police investigations, and statutory financial relief under Rule 12(4). However, our extensive review of post-complaint case histories reveals that the victim's true ordeal often begins after filing the complaint. Survivors and prosecution witnesses face systemic community pressure, direct intimidation by perpetrators to force case withdrawal, social boycotts, economic boycotts, and crushing anxiety stemming from multi-year court adjournments. Existing administrative workflows have no mechanism to observe whether a survivor is quietly slipping into severe depressive withdrawal, experiencing acute PTSD, or contemplating suicide under threats. 

KEFI AI (Kinematic Emotion & Forecasting Intervention System) is our production-ready, trauma-informed digital health platform engineered to provide continuous, proactive mental health monitoring and crisis prediction for atrocity victims throughout the multi-year lifecycle of their legal case. Rather than waiting for a survivor to suffer a mental breakdown or succumb to coercion, KEFI AI maintains a gentle, respectful daily presence across multiple accessible channels, extracts multi-signal emotional indicators, calculates a daily Dynamic Distress Score (DDS), forecasts psychological crises 72 hours before they manifest, and automatically alerts District Magistrates (DMs), Superintendents of Police (SPs), and welfare officers for immediate intervention.

MULTICHANNEL ENGAGEMENT & ETHICAL ONBOARDING
Atrocity victims come from diverse educational, linguistic, and socio-economic backgrounds. A smartphone-only mobile application will fail to reach rural communities. Therefore, we designed KEFI AI as an omnichannel engine accessible through:
1. Low-friction WhatsApp and web-based conversational interface supporting mixed-code vernacular languages (Tanglish, Hinglish, regional Tamil, and Hindi).
2. Automated outbound interactive voice response (IVRS) integrated with the National Helpline Against Atrocities (14566), capable of conducting 60-second guided voice check-ins over basic feature phones.
3. Offline two-way SMS protocols for rural shadow zones lacking stable 3G/4G connectivity.
4. An accessible mobile portal featuring a silent emergency mode and Plutchik-grounded visual emotion wheels for victims unable to express trauma verbally.
Onboarding occurs strictly through explicit informed consent aligned with Section 6(1) of the Digital Personal Data Protection (DPDP) Act, 2023. Victims can pause monitoring, modify check-in frequency, or withdraw consent at any time without compromising their legal standing or statutory compensation rights.

MULTIMODAL SIGNAL EXTRACTION & THE DYNAMIC DISTRESS SCORE (DDS)
Human trauma does not reveal itself solely in explicit words; it reflects in altered vocal patterns, prolonged delays in responding, and shifts in conversational sentiment. KEFI AI processes four distinct telemetry streams while strictly respecting victim privacy:
- Linguistic & Sentiment Analysis: Fine-tuned Indic-BERT and XLM-RoBERTa models analyze text inputs for sentiment polarity, feelings of hopelessness, and high-risk intimidation keywords ("threat", "court", "withdraw", "compromise", "kill", "dhamki").
- Acoustic Voice Prosody Processing: Using lightweight digital signal processing (librosa pipeline running on 20ms audio windows), the system extracts vocal jitter, shimmer, pitch frequency variability, and pause length ratios from voice check-ins, generating a normalized Voice Stress Index (VSI).
- Behavioral Responsiveness Tracking: The system monitors non-verbal behavioral shifts, such as suddenly missed check-ins, prolonged response latencies, and erratic interaction timings that often signal external intimidation or severe depressive immobilization.
- Judicial Case Context: The engine correlates distress trends with proximity to critical court milestones, including chargesheet filings, bail hearings, and cross-examinations.

These dimensions are synthesized into our proprietary Dynamic Distress Score (DDS), a normalized index from 0 to 100 governed by the formula:
DDS = 0.25*E + 0.20*V + 0.15*B + 0.15*H + 0.10*C + 0.15*T
Where E represents conversational emotion valence, V represents voice acoustic stress, B represents behavioral check-in friction, H represents historical trend velocity, C represents court hearing proximity, and T represents threat keyword density.

PREDICTIVE CRISIS FORECASTING & EXPLAINABLE AI (XAI)
A static score is insufficient for preventing suicide or witness intimidation. KEFI AI models longitudinal distress trajectories using time-series trend velocity (dDDS/dt). By evaluating the rate of change over rolling 7-day windows, our system forecasts distress levels 72 hours into the future. When a survivor's trajectory threatens to cross critical thresholds, the platform triggers preventive intervention before an emergency occurs.

To ensure district authorities trust and act upon these recommendations, our platform implements Explainable AI (XAI) powered by SHAP and LIME algorithms. When an alert reaches a District Magistrate or Superintendent of Police, the dashboard does not present an opaque score. Instead, it provides a transparent point attribution breakdown (for example: Base Distress: 28 | Threat Keywords: +21 | Voice Acoustic Jitter: +14 | Missed Check-ins: +12 | Court Trial Proximity: +9 | Projected 72h Score: 84 - RED BAND). This gives protection officers immediate, actionable clarity on whether an intervention requires police witness protection, legal aid counsel, or psychiatric hospitalization.

TRIAGED ESCALATION & MEASURABLE SOCIETAL IMPACT
KEFI AI routes cases through a three-tier intervention matrix:
- Green Band (DDS 0-30): Normal baseline. The system delivers automated daily affirmation check-ins, box-breathing exercises, and informative legal rights explainers.
- Orange Band (DDS 31-60): Moderate distress. Check-in cadence accelerates to twice daily, self-help grounding tools are recommended, and an automated appointment is scheduled with an assigned tele-MANAS or District Mental Health Programme counsellor.
- Red Band (DDS 61-100): High distress or critical threat. The system instantly generates an emergency alert on the District Magistrate and SP Command Dashboard, transmits automated SMS dispatches to designated Sub-Divisional Protection Officers, and initiates witness safety protocols under Section 15A of the SC/ST Act.

By shifting administrative care from reactive post-crisis triage to proactive longitudinal monitoring, KEFI AI safeguards human dignity, eliminates secondary victimization, drastically reduces witness hostility caused by unaddressed coercion, and ensures India's justice machinery actively protects its most vulnerable citizens.
```
*(Exact Length: 7115 Characters — strictly complies with the <= 10,000 characters limit)*

---

## 📌 FIELD 4: Idea Description (Max 50,000 Characters)
**Copy & Paste into Portal:**
```text
1. PROBLEM CONTEXT AND IN-DEPTH FIELD REALITY
The Scheduled Castes and the Scheduled Tribes (Prevention of Atrocities) Act, 1989 (amended in 2015 and 2018) is one of India's most significant legislative instruments designed to protect marginalized communities against institutionalized discrimination, physical violence, and social oppression. The Ministry of Social Justice and Empowerment (MoSJE), along with state welfare departments and the National Helpline Against Atrocities (14566), manages procedures for recording FIRs, disbursing statutory relief payments under Rule 12(4), and overseeing legal prosecutions in Special Courts.

Despite these established legal structures, deep field realities reveal that the legal complaint is rarely the conclusion of a victim's ordeal; rather, it marks the beginning of an intensely vulnerable, multi-year struggle. When an atrocity complaint is lodged in a rural or semi-urban jurisdiction, survivors and eyewitnesses are immediately subjected to intense structural, social, and psychological pressures:
- Direct and Indirect Coercion: Accused persons, often possessing significant economic or political influence, routinely deploy coercive tactics, ranging from midnight house visits to covert threats against family members, demanding the formal withdrawal or compromise of the case.
- Social and Economic Boycotts: Entire victim families frequently face ostracization, exclusion from local agricultural employment, and denial of basic village resources.
- Judicial Exhaustion and Trauma: The average trial duration in Special Courts under the SC/ST Act often extends across several years. Repeated adjournments, hostile defense cross-examinations, and the requirement to relive violent incidents inflict profound secondary trauma.
- Severe Mental Health Deterioration: A substantial percentage of atrocity survivors experience acute Post-Traumatic Stress Disorder (PTSD), severe clinical depression, persistent panic episodes, and suicidal ideation.

Crucially, the current administrative framework has no continuous mechanism to monitor the psychological well-being of survivors once an FIR is filed. The state intervenes only after an irreversible disaster occurs—such as a witness turning hostile out of fear, a survivor attempting self-harm, or a family quietly withdrawing their testimony. Problem Statement SIH26094 demands a transformative, compassionate technological bridge: an automated, continuous, and dynamic mental health monitoring and distress prediction system that actively accompanies the victim throughout their legal journey.

2. SYSTEM ARCHITECTURE & ENGINEERING SPECIFICATION
To address this challenge, Team DEKO (Team ID: 141444, University College of Engineering, Panruti) conceived, architected, and built KEFI AI. The name derives from the Greek concept of 'Kefi' (Κέφι)—representing emotional vitality, passion, inner resilience, and the triumph of the human spirit over adversity.

KEFI AI is built as a cloud-native, fault-tolerant microservices platform designed for high security, horizontal scalability, and low-latency interaction:
- Frontend Client Layer: A responsive Single Page Application (SPA) built using React 18, Vite, and modern CSS design systems. The interface is engineered with a mobile-first philosophy, incorporating high-contrast modes, simplified tactile navigation, an interactive Plutchik Emotion Wheel, guided Box Breathing (4-4-4-4 technique), and a single-tap "Silent Emergency Mode" that instantly conceals the application behind a standard utility screen.
- Omnichannel Ingestion Gateway: An API integration gateway deployed on FastAPI (Python 3.11) and Node.js that interfaces with multiple communication channels:
  1. WhatsApp Integration Engine: Utilizing conversational webhook endpoints to conduct friendly, automated bi-daily check-ins.
  2. National Helpline (14566) IVRS Bridge: A telephony gateway utilizing Asterisk/Twilio telephony APIs to deliver scheduled 60-second automated outbound voice check-ins for survivors who possess basic feature phones or cannot read.
  3. SMS Fallback Engine: A lightweight two-way GSM modem/SMS bridge designed specifically for remote tribal hamlets and rural shadow zones with no mobile internet.
- Secure Authentication & Identity Management: Integrates role-based access control (RBAC) supporting three distinct user profiles: Beneficiary/Survivor, Protection Officer/Counsellor, and District Magistrate/Superintendent of Police Command HUD. Sessions are authenticated using cryptographic JWT tokens with strict timeout policies.
- Data Persistence & Time-Series Engine: Uses PostgreSQL 16 for relational case management data paired with TimescaleDB hypertables for continuous telemetry, distress vector histories, and audit logs. All at-rest data partitions are encrypted using AES-256-GCM.

3. MULTIMODAL DISTRESS EXTRACTION PIPELINE
Human distress manifests across several interconnected behavioral and physiological dimensions. KEFI AI avoids relying on any single fragile metric. Instead, it aggregates data through four synchronized intelligence pipelines:

A. Natural Language Processing & Dialect Understanding
Atrocity victims rarely communicate in formal, textbook language. In regions like Tamil Nadu, conversations seamlessly blend Tamil and English ("Tanglish"), such as: "Enakku romba bayama irukku, court hearings nala stress aaguthu". In Northern states, mixed Hinglish is standard.
Our NLP engine employs a fine-tuned Indic-BERT model integrated with multilingual RoBERTa tokenizers, specialized on regional colloquialisms and emotional subtexts. The pipeline extracts:
- Sentiment Polarity (-1.0 to +1.0) and Emotional Valence.
- Hopelessness & Depressive Markers: Detecting linguistic patterns associated with resignation, severe grief, insomnia, and self-harm vulnerability.
- Coercion & Intimidation Lexicon: A specialized statutory threat dictionary that scans for contextual keywords and phrases indicating illegal pressure ("withdraw", "settle pannu", "threat", "dhamki", "court delay", "police complaint cancel", "compromise").

B. Acoustic Voice Prosody Digital Signal Processing (DSP)
When survivors interact via voice notes or automated IVRS telephone check-ins, the audio stream is passed through an automated acoustic DSP pipeline powered by librosa and PyTorch Audio:
- Frame-Level Segmentation: Speech signals are sampled at 16 kHz and sliced into 20ms Hamming-windowed frames with a 10ms overlap.
- Fundamental Frequency (F0) & Pitch Tremor Extraction: Measures involuntary pitch instability, micro-tremors, and voice cracking indicative of acute fight-or-flight anxiety.
- Vocal Jitter and Shimmer: Measures cycle-to-cycle frequency variations (jitter %) and amplitude perturbations (shimmer %) that correlate clinically with vocal cord muscle tension under emotional distress.
- Pause-to-Speech Ratio & Speech Latency: Quantifies abnormal hesitations, prolonged silence intervals, and slowed speech tempo characteristic of clinical trauma and depressive psychomotor retardation.
The DSP pipeline synthesizes these acoustic parameters into a normalized Voice Stress Index (VSI) ranging from 0.00 to 1.00.

C. Longitudinal Behavioral Analytics
Victim distress frequently manifests as passive behavioral withdrawal. KEFI AI continuously measures:
- Check-in Response Delay: The time delta between an outbound prompt and the victim's interaction.
- Check-in Omission Rate: Tracking consecutive skipped check-ins. If a previously responsive survivor abruptly ceases communication for 48 hours, this behavioral anomaly immediately flags potential physical intimidation, phone confiscation, or acute depressive immobilization.
- Interaction Duration Variance: Abrupt drops in conversation length indicating heightened reluctance or fear of surveillance by perpetrators.

D. Judicial & Case Milestone Modeling
Trauma is non-linear and spikes predictably around formal legal milestones. By integrating with the e-Courts portal and district prosecution databases, KEFI AI dynamically tracks case progression. The system elevates monitoring sensitivity during high-risk litigation phases:
- Bail hearing of accused perpetrators.
- Chargesheet submission and witness summons issuance.
- In-court witness cross-examination dates.
- Periodic statutory compensation disbursement milestones under Rule 12(4).

4. MATHEMATICAL FORMULATION OF THE DYNAMIC DISTRESS SCORE (DDS)
To transform complex multimodal inputs into an objective, standardized metric, we formulated the Dynamic Distress Score (DDS). The DDS produces a continuous numerical index bounded between 0 and 100:

DDS = 0.25*E + 0.20*V + 0.15*B + 0.15*H + 0.10*C + 0.15*T

Where each parameter is normalized on a scale of [0, 100]:
- E (Emotion Valence Factor, weight = 0.25): Derived from Indic-BERT sentiment classification and Plutchik emotional mapping, scoring sadness, fear, and panic.
- V (Voice Stress Index, weight = 0.20): Derived from acoustic DSP jitter, shimmer, pitch variability, and vocal tension metrics.
- B (Behavioral Engagement Gap, weight = 0.15): Calculated as a function of missed check-in frequency and response latency anomalies over a rolling 5-day baseline.
- H (Historical Trend Velocity, weight = 0.15): Represents the first derivative of the distress trajectory over time (dDDS/dt), reflecting whether emotional state is stabilizing or rapidly escalating.
- C (Case Proximity Factor, weight = 0.10): Computed from the temporal distance (in days) to upcoming court appearances, bail decisions, or sensitive trial proceedings.
- T (Threat & Coercion Keyword Density, weight = 0.15): Reflects the contextual frequency and intensity of verified intimidation vocabulary detected in beneficiary communication.

5. 72-HOUR LONGITUDINAL CRISIS FORECASTING ENGINE
Static monitoring merely records trauma after it peaks. The primary innovation of KEFI AI is proactive 72-hour predictive forecasting.
Using historical time-series vectors stored in TimescaleDB, the system computes the instantaneous distress velocity:
Velocity = dDDS / dt = (DDS_t - DDS_{t-k}) / k
And the distress acceleration:
Acceleration = d^2(DDS) / dt^2

A lightweight autoregressive LSTM / Exponential Smoothing model projects the expected distress curve over subsequent 24-hour, 48-hour, and 72-hour horizons. If a survivor's current DDS is 48 (Orange Band) but exhibiting a steep velocity of +12 points/day due to an upcoming bail hearing and sudden missed check-ins, the forecasting engine projects a 72-hour score of 84 (Red Band). This triggers proactive protective intervention before the victim reaches a breaking point.

6. EXPLAINABLE AI (XAI) & DISTRICT ADMINISTRATIVE HUD
A severe flaw in modern AI deployments within public administration is the "black-box" dilemma. A District Magistrate, Superintendent of Police, or District Welfare Officer cannot legally dispatch a police escort or crisis team based solely on an unexplained percentage score.

KEFI AI integrates SHAP (SHapley Additive exPlanations) and LIME to generate instantaneous, human-readable Decision Cards on the Officer Command Dashboard. When an alert fires, the system presents an audit-ready point attribution:
- Baseline Risk Contribution: +22 points (Persistent trauma symptoms)
- Threat Keyword Trigger: +21 points (Explicit references to case withdrawal threats)
- Acoustic Prosody Tension: +14 points (Severe vocal jitter and tremor in last voice note)
- Behavioral Check-in Absence: +12 points (Two consecutive missed check-in cycles)
- Judicial Hearing Proximity: +9 points (High Court bail hearing scheduled in 48 hours)
- Total Computed DDS: 78 / 100 (CRITICAL RED BAND)
- Recommended Statutory Action: Urgent witness protection dispatch under Section 15A; assignment of senior tele-MANAS clinical psychologist.

This transparency empowers judicial and police officers to make rapid, defensible, and legally sound decisions without second-guessing algorithmic recommendations.

7. INSTITUTIONAL 3-TIER ACTION MATRIX
KEFI AI translates predictive insights into concrete administrative standard operating procedures:

A. Green Band (DDS 0 - 30): Mild or Baseline State
- Routine check-in frequency: Once every 48 hours.
- Intervention: Self-guided resilience support, multilingual psychoeducation audio stories, Plutchik emotion journaling, and automated progress badges.
- Victim Resources: Access to pre-loaded Box Breathing visualizers and digital booklets on SC/ST Act rights and legal entitlements.

B. Orange Band (DDS 31 - 60): Moderate Distress State
- Check-in frequency: Increased to twice daily (morning and evening).
- Automated Intervention: Triggers an automated notification to the assigned District Welfare Officer or NGO social worker.
- Clinical Support: Automated scheduling of a tele-counselling consultation with the nearest district hospital psychiatrist or tele-MANAS nodal centre (14416).
- Legal Guidance: Transmits informative updates regarding case status to reduce anxiety caused by procedural ambiguity.

C. Red Band (DDS 61 - 100): High Crisis / Threat State
- Immediate Action: Automatically issues high-priority SMS and dashboard push alerts to the District Magistrate, District Superintendent of Police, and Sub-Divisional Police Officer (SDPO).
- Witness Protection Protocol: Activates Section 15A of the SC/ST (PoA) Act, dispatching local protection personnel to verify victim physical safety.
- Emergency Escalation: System establishes an immediate, direct telephonic bridge between the victim and a certified crisis counselor while alerting the District Legal Services Authority (DLSA).

8. DATA PRIVACY, LEGAL COMPLIANCE & ETHICAL GOVERNANCE
Handling the mental health and legal data of vulnerable citizens demands the highest standards of data security and constitutional ethics:
- Digital Personal Data Protection (DPDP) Act, 2023 Compliance:
  * Section 6(1) Explicit Consent: Collected digitally with multi-language voice and text explainers detailing exactly how data will be analyzed.
  * Right to Withdraw & Right to Erasure: Survivors retain the unconditional right to pause monitoring or request the permanent deletion of their conversational records without affecting their ongoing prosecution or statutory compensation.
  * Purpose Limitation: Collected telemetry is strictly ring-fenced for mental health support and victim protection; it cannot be shared with third parties or repurposed for commercial profiling.
- Cryptographic Security Architecture:
  * Transport Security: All network communication operates exclusively over TLS 1.3.
  * Database Encryption: AES-256-GCM encryption applied to all database tables at rest.
  * End-to-End Anonymization: Conversational text and voice logs are stripped of Personally Identifiable Information (PII) before passing into AI inference pipelines. Officer dashboards display pseudonymized tokens (e.g., Case Token: #POA-TN-2026-0891) unless an emergency Red Band override is authorized by the District Magistrate.
  * Immutable Audit Trails: Every officer view, score calculation, and intervention dispatch is logged onto a SHA-256 tamper-evident append-only ledger for judicial scrutiny.

9. FIELD IMPLEMENTATION ROADMAP & COST ECONOMICS
We developed KEFI AI with an uncompromising focus on frugal engineering and fiscal sustainability:
- Pilot Phase (Months 1 - 3): Deployment across 5 high-burden districts in Tamil Nadu in active collaboration with District Social Welfare Offices, DLSA, and local Special Courts. Onboarding 1,000 active survivors across diverse rural and semi-urban taluks.
- State-Wide Integration (Months 4 - 6): Integration with state police CCTNS (Crime and Criminal Tracking Network & Systems) and the National Helpline Against Atrocities (14566) call routing infrastructure.
- National Scaling (Months 7 - 12): Phased rollout across all 700+ districts in India under the administrative umbrella of the Ministry of Social Justice and Empowerment.

Cost Feasibility:
- Cloud Inference Optimization: By quantizing our transformer models (INT8 precision) and utilizing serverless event-driven architecture on open-source frameworks (FastAPI, PostgreSQL, Redis, n8n), the operational compute cost per beneficiary is less than ₹0.15 per daily check-in.
- Telephony Economics: Leveraging existing government toll-free infrastructure (14566 and 14416) ensures negligible recurring telecommunications costs for both the state and the victim.

10. EXPECTED TANGIBLE OUTCOMES & SOCIETAL IMPACT
Deploying KEFI AI delivers five transformative outcomes aligned with national priorities:
1. Early Identification of Trauma: Intercepting mental health crises and preventing survivor suicides through continuous, non-intrusive monitoring.
2. Comprehensive Psychological Rehabilitation: Operationalizing the long-neglected psycho-social mandate of Rule 12(4) of the SC/ST (PoA) Rules by connecting victims directly to professional psychiatric and counselling networks.
3. Enhanced Witness Protection & Conviction Integrity: Preventing witness hostility and forced case retractions by detecting intimidation early and activating Section 15A protection protocols, directly improving conviction rates in Special Courts.
4. Intelligent Welfare Resource Allocation: Providing District Magistrates and MoSJE leadership with real-time district-level distress heatmaps, enabling data-driven deployment of counsellors, legal aid clinics, and rehabilitation funds.
5. Restoration of Human Dignity: Rebuilding the survivor's faith in the constitutional justice system by ensuring they are never abandoned to suffer in silence after lodging a complaint.
```
*(Exact Length: 17666 Characters — strictly complies with the <= 50,000 characters limit)*

---

## 📌 FIELD 5: Idea Template (File Upload - Max 10 MB PDF)
**File to Upload:**
- **Local File Path**: `e:\SIH Keffi\SIH2026_DEKO_SIH26094_Presentation.pdf`
- **File Size**: `4.95 MB` (Strictly under the 10 MB portal limit)
- **Slide Count**: Exactly 5 standard SIH-compliant widescreen slides
- **Contents**:
  - Slide 1: Cover Slide with Official MoSJE Theme, Team DEKO details, and Problem ID SIH26094.
  - Slide 2: Ground-Level Problem Statement, SC/ST Act Context, and Statutory Shortcomings.
  - Slide 3: Proposed Solution, Multichannel Access (IVRS 14566, Chat, SMS), and Core Innovations.
  - Slide 4: Technical Architecture, Mathematical DDS Formula, 72h Forecasting, XAI & Security.
  - Slide 5: All 5 Expected Outcomes mapped directly with 5 authentic, high-resolution screenshots from the live KEFFI Chatbot platform.

---
*Created by Team DEKO (Team ID: 141444) for Smart India Hackathon 2026 | Problem Statement: SIH26094*
