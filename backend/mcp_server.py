from backend.db import get_report
from backend.ai_utils import summarize_text, classify_needs

def process_report(report_id):
    report = get_report(report_id)
    if not report:
        return {"error": "Report not found."}
    desc = report["description"]
    summary = summarize_text(desc)
    needs = classify_needs(desc)
    urgency = "high" if "injury" in desc.lower() or "trapped" in desc.lower() else "medium"
    return {
        "summary": summary,
        "needs": needs,
        "urgency": urgency
    }