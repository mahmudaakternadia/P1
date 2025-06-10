import gradio as gr
import requests
import os

BACKEND_URL = os.environ.get("BACKEND_URL", "http://localhost:8000/submit_report/")

def submit_report(description, location, image):
    data = {"description": description, "location": location}
    files = {"image": open(image, "rb")} if image else None
    try:
        response = requests.post(BACKEND_URL, data=data, files=files)
        if files:
            files["image"].close()
        if response.ok:
            result = response.json()
            # Example: adjust this to match your actual backend response
            summary = result.get("ai_result", {}).get("summary", "")
            needs = ", ".join(result.get("ai_result", {}).get("needs", []))
            urgency = result.get("ai_result", {}).get("urgency", "")
            return f"Summary: {summary}\nNeeds: {needs}\nUrgency: {urgency}"
        else:
            return f"Submission failed: {response.text}"
    except Exception as e:
        return f"Error: {e}"

iface = gr.Interface(
    fn=submit_report,
    inputs=[
        gr.Textbox(label="Describe the situation", lines=3),
        gr.Textbox(label="Location (address or GPS)"),
        gr.Image(label="Optional photo (damage, situation)", type="filepath")
    ],
    outputs=gr.Textbox(label="AI Summary & Needs", lines=4),
    title="Disaster Relief - Situation Reporting",
    description="Submit disaster reports. Our AI will assess and summarize needs for coordination.",
)
if __name__ == "__main__":
    iface.launch()