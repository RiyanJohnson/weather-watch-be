from sqlalchemy.orm import Session
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
