from sqlalchemy.orm import Session
from typing import Optional
from datetime import datetime
import uuid

from db.models import DisasterModel

def get_all(db: Session, severity: Optional[str], type: Optional[str], status: Optional[str]):
    query = db.query(DisasterModel)
    if severity:
        query = query.filter(DisasterModel.severity == severity)
    if type:
        query = query.filter(DisasterModel.type == type)
    if status:
        query = query.filter(DisasterModel.status == status)
    return query.all()

def get_by_id(db: Session, id: str):
    return db.query(DisasterModel).filter(DisasterModel.id == id).first()

def create(db: Session, data: dict):
    if not data.get("id"):
        data["id"] = f"DIS-{uuid.uuid4().hex[:8].upper()}"
    if not data.get("timestamp"):
        data["timestamp"] = datetime.utcnow()
    # strip fields not on the ORM model (e.g. recommendations list)
    data.pop("recommendations", None)
    record = DisasterModel(**data)
    db.add(record)
    db.commit()
    db.refresh(record)
    return record

def update_status(db: Session, id: str, status: str):
    record = db.query(DisasterModel).filter(DisasterModel.id == id).first()
    if record:
        record.status = status
        db.commit()
        db.refresh(record)
    return record

def delete(db: Session, id: str):
    record = db.query(DisasterModel).filter(DisasterModel.id == id).first()
    if record:
        db.delete(record)
        db.commit()
    return record
