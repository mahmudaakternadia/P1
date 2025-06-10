from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional

app = FastAPI()

# Enable CORS so the frontend can talk to the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/submit_report/")
async def submit_report(
    description: str = Form(...),
    location: str = Form(...),
    image: Optional[UploadFile] = File(None)
):
    # Example dummy AI processing (replace with your real logic)
    ai_result = {
        "summary": f"Report received: {description[:100]}...",
        "needs": ["rescue", "medical assistance"],
        "urgency": "High" if "urgent" in description.lower() else "Medium"
    }

    # Optionally handle the uploaded image (saving, processing, etc.)
    if image:
        contents = await image.read()
        # (For demo: just get the size)
        image_size = len(contents)
    else:
        image_size = 0

    return {
        "success": True,
        "ai_result": ai_result,
        "image_size": image_size
    }