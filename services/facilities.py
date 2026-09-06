from sqlalchemy.orm import Session
import uuid

from db.models import FacilityModel

def get_all(db: Session):
    return db.query(FacilityModel).all()

def create(db: Session, data: dict):
    if not data.get("id"):
        data["id"] = f"FAC-{uuid.uuid4().hex[:8].upper()}"
    record = FacilityModel(**data)
    db.add(record)
    db.commit()
    db.refresh(record)
    return record
