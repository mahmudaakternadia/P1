import os
from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from backend.mcp_server import process_report
from backend.db import save_report, init_db

from shutil import copyfileobj

# Ensure data folder exists
DATA_DIR = os.path.join(os.path.dirname(__file__), "../data")
os.makedirs(DATA_DIR, exist_ok=True)

app = FastAPI()

# CORS for Gradio
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    init_db()

@app.post("/submit_report/")
async def submit_report(
    description: str = Form(...),
    location: str = Form(...),
    image: UploadFile = None
):
    img_filename = None
    if image:
        img_filename = f"{image.filename}"
        img_path = os.path.join(DATA_DIR, img_filename)
        with open(img_path, "wb") as f:
            copyfileobj(image.file, f)
    report_id = save_report(description, location, img_filename)
    ai_result = process_report(report_id)
    return {"status": "received", "ai_result": ai_result, "report_id": report_id}