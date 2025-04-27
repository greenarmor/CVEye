from sqlalchemy import create_engine, Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

MYSQL_URL = os.getenv("MYSQL_URL")

engine = create_engine(MYSQL_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class CVE(Base):
    __tablename__ = "cves"

    cve_id = Column(String, primary_key=True, index=True)
    description = Column(String)

Base.metadata.create_all(bind=engine)

def save_metadata(cve):
    db = SessionLocal()
    db_cve = CVE(cve_id=cve['cve_id'], description=cve['description'])
    db.merge(db_cve)
    db.commit()
    db.close()

