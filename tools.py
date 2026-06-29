import os
import json
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_community.utilities import GoogleSerperAPIWrapper
from sqlalchemy.orm import Session
from database import get_db
from model import Report
db = get_db()
load_dotenv()
serper = GoogleSerperAPIWrapper()

@tool
def search_web(query: str) ->str:
    """Searches the web for information about a topic and returns results."""
    results = serper.run(query)
    return results

@tool 
def save_report(topic: str, summary: str, source: str) -> str:
    """"Saves the research report and its sources to the database. Use this after writing the final summary."""
    report = Report(topic=topic, summary=summary, source=source)
    db.add(report)
    db.commit()
    db.refresh(report)
    db.close()
    return f"Report saved with ID: {report.id}"

tools = [search_web, save_report]

