from sqlalchemy.orm import Session
from db.models import ReportModel

def get_all(db: Session):
    return db.query(ReportModel).all()
