from database import Base
from sqlalchemy import Column, Integer, String, Text, DateTime, func
from datetime import datetime

class Report(Base):
    __tablename__ = "research"

    id = Column(Integer, primary_key=True, index=True)
    topic = Column(String(255), nullable=False)
    summary = Column(Text, nullable=False)
    source = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=func.now())