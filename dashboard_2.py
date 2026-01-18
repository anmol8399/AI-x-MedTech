import gradio as gr

def get_doctor_list():
    # Mock data based on the "Doctor Repository" file
    return [
        ["Dr. James Anderson", "Cardiology", "Europe", "4.9", "Active"],
        ["Dr. Rachel Phillips", "Neurology", "Europe", "4.7", "Active"],
        ["Dr. Jennifer Harris", "Neurology", "Europe", "4.6", "Active"],
        ["Dr. Benjamin Reed", "Cardiology", "Europe", "4.8", "Active"]
    ]

with gr.Blocks(title="MedTech Doctor Repository", theme=gr.themes.Soft()) as demo:
    with gr.Row():
        # --- SIDEBAR (Left) ---
        with gr.Column(scale=1, min_width=200):
            gr.Markdown("## 🏥 MedTech")
            gr.Button("🏠 Dashboard", variant="secondary")
            gr.Button("👨‍⚕️ Doctors", variant="primary")
            gr.Button("🏥 Hospitals", variant="secondary")
            gr.Button("🌍 Regions", variant="secondary")
            gr.Button("📈 Analytics", variant="secondary")
            gr.Button("⚙️ Settings", variant="secondary")
            gr.Markdown("---")
            gr.Markdown("**User:** Jenn Ana")

        # --- MAIN CONTENT (Center) ---
        with gr.Column(scale=4):
            gr.Markdown("# Doctor Repository")
            
            with gr.Row():
                region_filter = gr.Dropdown(["Any Region", "Europe", "North America"], value="Europe", label="Region")
                specialty_filter = gr.Dropdown(["Any Specialty", "Cardiology", "Neurology"], value="Any Specialty", label="Specialty")
                search_btn = gr.Button("🔍 Search", variant="primary")
                clear_btn = gr.Button("Clear Filters")

            gr.Markdown("### Europe (128 Doctors)")
            doctor_table = gr.Dataframe(
                headers=["Doctor Name", "Specialty", "Region", "Rating", "Status"],
                value=get_doctor_list(),
                interactive=False
            )

            with gr.Row():
                gr.Button("Schedule")
                gr.Button("Message")
                gr.Button("Assign Reviewer")
                gr.Button("Export Evidence Trail")

        # --- AI RECOMMENDATION PANEL (Right) ---
        with gr.Column(scale=2):
            with gr.Group():
                gr.Markdown("### ✨ Final AI Recommendation")
                gr.Info(
                    "AI recommends generating a draft ICSR for Noemstat due to a 40% Increase in dizziness reports in Western Europe. [cite: 40]"
                )
                gr.Markdown("**Causality Assessment:** Probable [cite: 41]")
                gr.Markdown("**Confidence:** High [cite: 42]")
                
                with gr.Row():
                    gr.Button("Generate Report", variant="primary")
                    gr.Button("Promote", variant="secondary")

            with gr.Group():
                gr.Markdown("### 🏥 Featured Facility")
                gr.Markdown("**Johns Hopkins Hospital**\nParis, France [cite: 9, 23]")
                #gr.Image("https://www.hopkinsmedicine.org/-/media/feature/pagemeta/johns-hopkins-default-share-image.jpg?h=350&iar=0&w=700&hash=0D8B4D4B1C6B4B1B5B1B5B1B5B1B5B1B", label="Facility Image")

demo.launch()
