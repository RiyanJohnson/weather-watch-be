from sqlalchemy.orm import Session
from db.models import FacilityModel

def get_all(db: Session):
    return db.query(FacilityModel).all()
