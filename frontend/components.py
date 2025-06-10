import gradio as gr

def status_component():
    return gr.Textbox(label="AI Summary & Needs", interactive=False, lines=4)