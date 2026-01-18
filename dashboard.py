import gradio as gr
import numpy as np
import pandas as pd
import plotly.express as px

def get_patient_data():
    # Placeholder for actual EHR data logic
    return {
        "name": "Emily Carter",
        "status": "Active",
        "demographics": "68, Female | San Diego, USA",
        "history": "Hypertension, Diabetes Type 2, CKD",
        "narrative": "Patient reports dizziness and nausea after starting Noemstat 20mg. Symptoms began 3 days post initiation...",
        "meds": [["Simvastatin 20mg", "High"], ["Metformin 500mg", "Medium"], ["Enalapril 10mg", "Medium"]]
    }

def generate_vitals_data():
    dates = pd.date_range(start='2023-01-01', periods=30, freq='D')
    heart_rate = np.random.normal(75, 5, len(dates)).round().astype(int)
    systolic_bp = np.random.normal(120, 10, len(dates)).round().astype(int)
    diastolic_bp = np.random.normal(80, 5, len(dates)).round().astype(int)

    df = pd.DataFrame({
        'Date': dates,
        'Heart Rate (bpm)': heart_rate,
        'Systolic BP (mmHg)': systolic_bp,
        'Diastolic BP (mmHg)': diastolic_bp
    })
    return df

# Generate vitals data
vitals_df = generate_vitals_data()

# Create Plotly figure for vitals
fig = px.line(vitals_df, x='Date', y=['Heart Rate (bpm)', 'Systolic BP (mmHg)', 'Diastolic BP (mmHg)'], title="Patient Vitals Over Time", markers=True)
fig.update_layout(hovermode='x unified')

with gr.Blocks(title="MedTech Intake & Safety", theme=gr.themes.Soft()) as demo:
    # --- Header Section ---
    gr.Markdown("# ✤ MedTech Intake & Safety Dashboard")

    with gr.Row():
        # --- LEFT COLUMN: Patient Info & Narrative ---
        with gr.Column(scale=2):
            gr.Markdown("### ❦ Source Narrative")
            with gr.Group():
                patient = get_patient_data()
                gr.Markdown(f"**{patient['name']}** | {patient['status']}")
                gr.Markdown(f"✆ {patient['demographics']}")
                gr.Markdown(f"✉ *History:* {patient['history']}")

                narrative_box = gr.Textbox(
                    value=patient['narrative'],
                    label="Initial Intake Narrative",
                    lines=5,
                    interactive=False
                )

            gr.Markdown("### ✈ Current Medications")
            med_table = gr.Dataframe(
                headers=["Medication", "Risk Level"],
                value=patient['meds'],
                interactive=False
            )

        # --- MIDDLE COLUMN: Risk & Compliance ---
        with gr.Column(scale=1):
            gr.Markdown("### ✇ Risk Score Card")
            with gr.Group():
                score = gr.Label(value={"HIGH RISK": 8}, label="Risk Score")
                gr.Markdown("**Supporting Factors:**\n- Age > 60\n- Polypharmacy detected\n- Known class effect")

            gr.Markdown("### ✄ Missing Info Detected")
            gr.CheckboxGroup(
                ["Dose", "Symptom(s)", "Onset Date"],
                value=["Dose", "Symptom(s)"],
                label="Compliance Checklist"
            )

        # --- RIGHT COLUMN: Tracker & Actions ---
        with gr.Column(scale=1):
            gr.Markdown("### ✃ Follow-Up Tracker")
            with gr.Group():
                gr.Radio(
                    ["Initial Intake", "Criteria Check", "Initiate Follow-Up", "Case Complete"],
                    label="Current Phase",
                    value="Initiate Follow-Up"
                )

            btn_followup = gr.Button("Initiate Follow-Up", variant="primary")
            btn_complete = gr.Button("Complete Case")
            gr.Button("Cancel", variant="stop")

    # Vitals Tracking Plot - moved to its own row for full width
    gr.Markdown("### ❤️ Patient Vitals Tracking")
    with gr.Row():
        gr.Plot(fig, label="Vitals Trend")

    # --- Footer Logs ---
    with gr.Accordion("System Logs", open=False):
        gr.Markdown("Risk score generated using demographic + drug interaction model.")

demo.launch()
