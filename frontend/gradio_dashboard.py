import gradio as gr
import requests
import os

BACKEND_URL = os.environ.get("BACKEND_URL", "http://localhost:8000/submit_report/")

def submit_report(description, location, image):
    files = {"image": image} if image is not None else {}
    data = {"description": description, "location": location}
    try:
        response = requests.post(BACKEND_URL, data=data, files=files)
        if response.ok:
            result = response.json()
            summary = result["ai_result"]["summary"]
            needs = ", ".join(result["ai_result"]["needs"])
            urgency = result["ai_result"]["urgency"]
            return f"Summary: {summary}\nNeeds: {needs}\nUrgency: {urgency}"
        else:
            return "Submission failed."
    except Exception as e:
        return f"Error: {e}"

iface = gr.Interface(
    fn=submit_report,
    inputs=[
        gr.Textbox(label="Describe the situation", lines=3, placeholder="e.g. Flood in the area, people trapped, need medical assistance."),
        gr.Textbox(label="Location (address or GPS)", placeholder="e.g. 123 Main St, Springfield"),
        gr.Image(label="Optional photo (damage, situation)", type="filepath")
    ],
    outputs=gr.Textbox(label="AI Summary & Needs", lines=4),
    title="Disaster Relief - Situation Reporting",
    description="Submit disaster reports. Our AI will assess and summarize needs for coordination.",
)
if __name__ == "__main__":
    iface.launch()