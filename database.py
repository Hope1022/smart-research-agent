import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import DeclarativeBase, sessionmaker

engine = create_engine( "sqlite:///research.db",
    echo=False
)
class Base(DeclarativeBase):
    pass

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
def get_db():
    
    return sessionLocal()