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

KEFI AI (Kinematic Emotion & Forecasting Intervention System) is our production-ready, trauma-informed digital health platform engineered to provide continuous, proactive mental health monitoring and crisis prediction for atrocity victims throughout the multi-year lifecycle of their legal case. Rather than waiting for a survivor to suffer a mental breakdown or succumb to coercion, KEFI AI maintains a gentle, respectful daily presence across multiple accessible channels, extracts multi-signal emotional indicators, calculates a daily Dynamic Distress Score (DDS), forecasts psychological crises 72 hours before they manifest, and automatically alerts District Magistrates (DMs), Superintendents of Police (SPs), State Nodal Officers, and welfare administrators for immediate intervention.

MULTICHANNEL ENGAGEMENT & ETHICAL ONBOARDING
Atrocity victims come from diverse educational, linguistic, and socio-economic backgrounds. A smartphone-only mobile application will fail to reach rural communities. Therefore, we designed KEFI AI as an omnichannel engine accessible through:
1. Low-friction WhatsApp and web-based conversational interface supporting mixed-code vernacular languages (Tanglish, Hinglish, regional Tamil, and Hindi).
2. Automated outbound interactive voice response (IVRS) integrated with the National Helpline Against Atrocities (14566), capable of conducting 60-second guided voice check-ins over basic feature phones.
3. Offline two-way SMS protocols for rural shadow zones lacking stable 3G/4G connectivity.
4. An accessible mobile portal featuring a silent emergency mode and Plutchik-grounded visual emotion wheels for victims unable to express trauma verbally.
Onboarding occurs strictly through explicit informed consent aligned with Section 6(1) of the Digital Personal Data Protection (DPDP) Act, 2023. Victims can pause monitoring, modify check-in frequency, or withdraw consent at any time without compromising their legal standing or statutory compensation rights.

MULTIMODAL SIGNAL EXTRACTION & THE DYNAMIC DISTRESS SCORE (DDS)
Human trauma does not reveal itself solely in explicit words; it reflects in altered vocal patterns, prolonged delays in responding, and shifts in conversational sentiment. KEFI AI processes four distinct telemetry streams while strictly respecting victim privacy:
- Linguistic & Sentiment Analysis: Fine-tuned Indic-BERT models analyze text inputs for sentiment polarity, feelings of hopelessness, and high-risk intimidation keywords ("threat", "court", "withdraw", "compromise", "kill", "dhamki").
- Acoustic Voice Prosody Processing: Using lightweight digital signal processing (librosa pipeline running on 20ms audio windows), the system extracts vocal jitter, shimmer, pitch frequency variability, and pause length ratios from voice check-ins, generating a normalized Voice Stress Index (VSI).
- Behavioral Responsiveness Tracking: The system monitors non-verbal behavioral shifts, such as suddenly missed check-ins, prolonged response latencies, and erratic interaction timings that often signal external intimidation or severe depressive immobilization.
- Judicial Case Context: The engine correlates distress trends with proximity to critical court milestones, including chargesheet filings, bail hearings, and cross-examinations.
These dimensions are synthesized into our proprietary Dynamic Distress Score (DDS), a normalized index from 0 to 100 governed by:
DDS = 0.25*E + 0.20*V + 0.15*B + 0.15*H + 0.10*C + 0.15*T

72-HOUR CRISIS FORECASTING & MULTI-DOMAIN INTERVENTION ENGINE
Static monitoring merely records trauma after it peaks. KEFI AI models longitudinal distress trajectories using time-series trend velocity (dDDS/dt). By evaluating the rate of change over rolling 7-day windows, our system forecasts distress levels 72 hours into the future. When a survivor's trajectory threatens to cross critical thresholds, the platform triggers preventive intervention before an emergency occurs.

Crucially, our system does not issue generic alerts. It runs a specialized Context-Aware Statutory Recommendation Engine that uses NLP intent detection and acoustic thresholds to recommend four targeted interventions:
1. Medical Treatment & Psychiatric Care: Triggered by somatic trauma cues, panic attacks, or extreme acoustic jitter -> Direct dispatch to District Hospital, 108 EMS, and tele-MANAS 24/7 psychiatric support.
2. Relocation Support & Witness Sanctuary: Triggered by spatial intimidation, midnight incursions, or arson threats under Section 15A(6)(b) -> Recommends DM/SP to activate emergency government safehouse transit, travel stipend, and secure housing.
3. Legal Aid & Special Public Prosecutor (SPP) Assistance: Triggered by compromise pressure, court date anxiety, or trial fear -> Auto-notifies District Legal Services Authority (DLSA) to assign a senior empaneled advocate under Section 15A(11).
4. Financial Assistance & Livelihood Relief: Triggered by economic distress, wage denial, or delayed relief under Rule 12(4) -> Auto-flags District Welfare Officer for expedited Direct Benefit Transfer (DBT).

3-TIER ADMINISTRATIVE DASHBOARD HIERARCHY (DISTRICT -> STATE -> NATIONAL)
To operationalize accountability across federal and provincial jurisdictions, KEFI AI delivers a three-tier dashboard architecture:
- District Level (DM, SP, SDPO, DLSA): Case-level real-time telemetry, SHAP explainable decision cards (+21 threat keyword, +14 vocal jitter, +12 missed check-ins), and direct crisis team dispatch.
- State Level (State Nodal Officer / Principal Secretary, Social Welfare & ADGP Human Rights): Statewide macro heatmaps, district-to-district distress velocity comparisons, inter-district clinical counselor redistribution, and statewide Rule 12(4) compensation compliance monitoring.
- National Level (Ministry of Social Justice and Empowerment - MoSJE Central Command): Centrally sponsored scheme monitoring, nationwide vulnerability hot-spot identification, policy effectiveness metrics, and automated reporting to parliamentary committees.

By shifting administrative care from reactive post-crisis triage to proactive longitudinal monitoring, KEFI AI safeguards human dignity, eliminates secondary victimization, drastically reduces witness hostility caused by unaddressed coercion, and ensures India's justice machinery actively protects its most vulnerable citizens.
```
*(Exact Length: 7386 Characters — strictly complies with the <= 10,000 characters limit)*

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

6. CONTEXT-AWARE MULTI-DOMAIN INTERVENTION ENGINE (AI NLP RECOMMENDATION LOGIC)
Problem Statement SIH26094 explicitly mandates that the system provide targeted recommendations across four vital administrative domains. KEFI AI implements a multi-class NLP intent classifier and threshold logic that translates distress patterns into concrete statutory actions:

A. Medical Treatment & Psychiatric Care
- AI Trigger Conditions: High emotional hopelessness markers (E > 65), acoustic speech jitter > 2.8%, prolonged pause ratios (> 45%), or explicit text references to insomnia, severe panic, chest tightness, physical injuries, or self-harm thoughts.
- System Action: Instantly generates a priority medical referral card on the District Health Officer and DM dashboards. Automatically establishes an emergency telephonic bridge with tele-MANAS (14416) or the nearest District Government Hospital psychiatric emergency unit, and dispatches 108 Emergency Medical Services if acute physical harm is detected.

B. Safe Relocation Support & Witness Sanctuary (Section 15A(6)(b))
- AI Trigger Conditions: High threat keyword density (T > 60), detection of spatial threat phrases ("veetukku vanthu merattunaanga", "house surrounded", "arson", "midnight visit", "village boycott", "they will kill if I go outside"), or sudden complete cessation of check-ins following verified intimidation.
- System Action: Formulates an immediate statutory relocation recommendation under Section 15A of the SC/ST (PoA) Act. The dashboard alerts the District Magistrate and Superintendent of Police to immediately authorize: (1) Temporary transit accommodation in a government safehouse or secure guest house, (2) Travel stipend disbursement, and (3) Physical police escort for immediate evacuation from the hostile village.

C. Legal Aid & Special Public Prosecutor (SPP) Assistance (Section 15A(11))
- AI Trigger Conditions: Judicial anxiety spikes (C > 70), text references to coercive compromise ("settle panna solraanga", "case vaabass vaanga solraanga", "vakil varala", "defense lawyer threatened"), or procedural confusion surrounding chargesheet filings or bail hearings.
- System Action: Generates an automated statutory legal aid requisition to the Member Secretary of the District Legal Services Authority (DLSA). Recommends the immediate appointment of an empaneled senior advocate or independent legal counsel under Section 15A(11), and schedules an urgent case briefing with the designated Special Public Prosecutor (SPP) of the Special Court.

D. Expedited Financial Assistance & Livelihood Relief (Rule 12(4))
- AI Trigger Conditions: Detection of economic starvation, wage boycott, agricultural employment denial, loss of sole earning family member, or pending statutory compensation installments past the 7-day mandate under Rule 12(4).
- System Action: Automatically cross-references the state treasury portal and flags the District Social Welfare Officer (DSWO) and District Collector. Formulates an expedited Direct Benefit Transfer (DBT) sanction docket for instant release of the mandated 25%, 50%, or 100% relief slab into the victim's verified Aadhaar-linked bank account.

7. 3-TIER ADMINISTRATIVE COMMAND HIERARCHY (DISTRICT -> STATE -> NATIONAL)
Public administration in India operates across strict federal and state hierarchies. To ensure seamless coordination without jurisdictional confusion, KEFI AI provides tailored dashboard views across all three governing levels:

A. District Level Command HUD (DM, SP, SDPO & DLSA)
- Designed for tactical, case-by-case intervention and rapid field response.
- Displays individual beneficiary cards with live Dynamic Distress Scores, 7-day velocity curves, and real-time audio prosody stress meters.
- Implements Explainable AI (SHAP / LIME) decision attribution cards (e.g., Base: 24 | Threat Keywords: +21 | Voice Jitter: +14 | Missed Check-ins: +12 | Court Trial Proximity: +9 | Projected 72h DDS: 80 - RED BAND).
- Empowers the District Magistrate and SP to authorize one-click witness protection deployment, psychiatric ambulance dispatch, or DLSA advocate assignment.

B. State Level Command Dashboard (State Nodal Officer / Principal Secretary & ADGP Human Rights)
- Designed for inter-district resource allocation, macro-level oversight, and legislative compliance.
- Visualizes statewide district-by-district distress heatmaps, identifying emerging caste violence clusters and regional tension hotspots before communal unrest spreads.
- Tracks statewide compliance metrics under Rule 12(4) of the SC/ST (PoA) Rules, highlighting districts lagging behind the mandatory 7-day relief disbursement timeline.
- Facilitates the dynamic redistribution of mobile tele-counselling teams, psychiatric social workers, and Special Public Prosecutors from low-burden districts to overburdened tribal or rural districts.

C. National Level Central Command HUD (Ministry of Social Justice and Empowerment - MoSJE Central Command)
- Designed for strategic policymaking, centrally sponsored scheme oversight, and national statutory reporting.
- Aggregates anonymized macro telemetry across all 700+ districts and 36 States/UTs in India.
- Evaluates the national impact and effectiveness of the National Helpline Against Atrocities (14566) and Centrally Sponsored Schemes for SC/ST protection.
- Automatically generates auditable, data-driven annual reports for the National Commission for Scheduled Castes (NCSC), National Commission for Scheduled Tribes (NCST), and Parliamentary Standing Committees.

8. INSTITUTIONAL 3-TIER ACTION MATRIX
KEFI AI translates predictive insights into concrete administrative standard operating procedures:
- Green Band (DDS 0 - 30): Normal baseline. Routine check-in frequency once every 48 hours. Delivers self-guided resilience audio, multilingual psychoeducation stories, Plutchik emotion journaling, Box Breathing visualizers, and digital SC/ST Act rights booklets.
- Orange Band (DDS 31 - 60): Moderate distress. Check-in frequency accelerates to twice daily (morning and evening). Automatically alerts the assigned District Welfare Officer or NGO social worker, and schedules an appointment with a tele-MANAS counsellor (14416) or district hospital psychiatrist.
- Red Band (DDS 61 - 100): High crisis / critical threat. Instantly generates emergency SMS and dashboard push alerts to the DM, SP, and SDPO. Activates Section 15A witness protection, dispatches local police personnel to verify physical safety, and establishes an immediate telephonic bridge with an emergency psychiatric counselor while alerting DLSA.

9. DATA PRIVACY, LEGAL COMPLIANCE & ETHICAL GOVERNANCE
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

10. FIELD IMPLEMENTATION ROADMAP & COST ECONOMICS
We developed KEFI AI with an uncompromising focus on frugal engineering and fiscal sustainability:
- Pilot Phase (Months 1 - 3): Deployment across 5 high-burden districts in Tamil Nadu in active collaboration with District Social Welfare Offices, DLSA, and local Special Courts. Onboarding 1,000 active survivors across diverse rural and semi-urban taluks.
- State-Wide Integration (Months 4 - 6): Integration with state police CCTNS (Crime and Criminal Tracking Network & Systems) and the National Helpline Against Atrocities (14566) call routing infrastructure.
- National Scaling (Months 7 - 12): Phased rollout across all 700+ districts in India under the administrative umbrella of the Ministry of Social Justice and Empowerment.

Cost Feasibility:
- Cloud Inference Optimization: By quantizing our transformer models (INT8 precision) and utilizing serverless event-driven architecture on open-source frameworks (FastAPI, PostgreSQL, Redis, n8n), the operational compute cost per beneficiary is less than ₹0.15 per daily check-in.
- Telephony Economics: Leveraging existing government toll-free infrastructure (14566 and 14416) ensures negligible recurring telecommunications costs for both the state and the victim.

11. EXPECTED TANGIBLE OUTCOMES & SOCIETAL IMPACT
Deploying KEFI AI delivers five transformative outcomes aligned with national priorities:
1. Early Identification of Trauma: Intercepting mental health crises and preventing survivor suicides through continuous, non-intrusive monitoring.
2. Comprehensive Psychological Rehabilitation: Operationalizing the long-neglected psycho-social mandate of Rule 12(4) of the SC/ST (PoA) Rules by connecting victims directly to professional psychiatric and counselling networks.
3. Enhanced Witness Protection & Conviction Integrity: Preventing witness hostility and forced case retractions by detecting intimidation early and activating Section 15A protection protocols, directly improving conviction rates in Special Courts.
4. Intelligent Welfare Resource Allocation: Providing District Magistrates, State Nodal Officers, and MoSJE leadership with real-time distress heatmaps, enabling data-driven deployment of counsellors, legal aid clinics, and rehabilitation funds.
5. Restoration of Human Dignity: Rebuilding the survivor's faith in the constitutional justice system by ensuring they are never abandoned to suffer in silence after lodging a complaint.
```
*(Exact Length: 21289 Characters — strictly complies with the <= 50,000 characters limit)*

---

## 📌 FIELD 5: Idea Template (File Upload - Max 10 MB PDF)
**File to Upload:**
- **Local File Path**: `e:\SIH Keffi\SIH2026_DEKO_SIH26094_Presentation.pdf`
- **File Size**: `4.95 MB` (Strictly under the 10 MB portal limit)
- **Slide Count**: Exactly 5 standard SIH-compliant widescreen slides
- **Contents**:
  - Slide 1: Cover Slide with Official MoSJE Theme, Team DEKO details, and Problem ID SIH26094.
  - Slide 2: Ground-Level Problem Statement, SC/ST Act Context, Statutory Shortcomings, and 3-Tier Command HUD (District -> State -> National).
  - Slide 3: Proposed Solution, Multichannel Access (IVRS 14566, Chat, SMS), 20ms Acoustic DSP, Mathematical DDS Formula, and AI Statutory Multi-Domain Recommendation Engine.
  - Slide 4: Feasibility & Viability Analysis, DPDP Act 2023 Compliance, SHA-256 Audit Trail, and Problem vs Solution Matrix.
  - Slide 5: All 5 Expected Outcomes mapped directly with 5 authentic, high-resolution screenshots from the live KEFFI Chatbot platform (Tanglish Chat, Plutchik Wheel, Box Breathing, 7-Day DDS Trend, Officer HUD) + Targeted Statutory Redress.

---
*Created by Team DEKO (Team ID: 141444) for Smart India Hackathon 2026 | Problem Statement: SIH26094*
