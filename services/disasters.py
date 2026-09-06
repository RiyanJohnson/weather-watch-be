from sqlalchemy.orm import Session
from typing import Optional
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
