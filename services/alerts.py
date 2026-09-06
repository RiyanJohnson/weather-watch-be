from sqlalchemy.orm import Session
import uuid

from db.models import AlertModel

def get_all(db: Session):
    return db.query(AlertModel).all()

def acknowledge(db: Session, id: str):
    alert = db.query(AlertModel).filter(AlertModel.id == id).first()
    if alert:
        alert.acknowledged = True
        db.commit()
        db.refresh(alert)
    return alert

def create(db: Session, data: dict):
    if not data.get("id"):
        data["id"] = f"ALT-{uuid.uuid4().hex[:8].upper()}"
    record = AlertModel(**data)
    db.add(record)
    db.commit()
    db.refresh(record)
    return record
