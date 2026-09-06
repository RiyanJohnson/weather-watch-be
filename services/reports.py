from sqlalchemy.orm import Session
import uuid

from db.models import ReportModel

def get_all(db: Session):
    return db.query(ReportModel).all()

def create(db: Session, data: dict):
    if not data.get("id"):
        data["id"] = f"RPT-{uuid.uuid4().hex[:8].upper()}"
    record = ReportModel(**data)
    db.add(record)
    db.commit()
    db.refresh(record)
    return record
